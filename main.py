import random

MAP_SIZE = 2

# Diferentes tipos de territorios
TERRAIN_TYPES = ['Pradera', 'Bosque', 'Montaña']
RESOURCE_TYPES = ['Agua', 'Madera', 'Comida']
# Movimientos posibles en el combate
MOVES = ['Piedra', 'Papel', 'Tijera'] 

# Clase Jugador que acumula recursos y puntuación
class Player:
    def __init__(self, name="Jugador"):
        self.resources = {
            'Agua': 0,
            'Madera': 0,
            'Comida': 0
        }
        self.money = 100
        self.score = 0
        self.name = name

    def add_resources(self, resource_type):
        self.resources[resource_type] += 1
        self.score += 10  # Ganas 10 puntos por cada recurso

    def buy_terrain(self, money):
        self.money -= money
        self.score += 20  # Ganas 20 puntos por cada terreno conquistado
    
    def combat_cost(self):
        self.money -= 10

    def show_resources(self):
        print(f"{self.name} tiene los siguientes recursos:")
        print(f"Dinero: {self.money} | Puntuación: {self.score}")
        for resource, amount in self.resources.items():
            print(f"{resource}: {amount}")

# IA similar al jugador
class IA(Player):
    def __init__(self):
        super().__init__(name="IA")

# Territorio como una clase
class Territory:
    def __init__(self):
        self.terrain = random.choice(TERRAIN_TYPES)
        self.cost = random.randint(5,10)
        self.resources = random.choice(RESOURCE_TYPES)
        self.owner = '_'  # Sin conquistar: '_', Jugador: 'J', Computadora: 'C'
    
    def __str__(self):
        return f"{self.terrain}-{self.resources}-{self.cost}$-#{self.owner}"    

# Crear el mapa de territorios
def create_map():
    return [[Territory() for _ in range(MAP_SIZE)] for _ in range(MAP_SIZE)]

# Mostrar el mapa
def display_map(map_grid):
    for row in map_grid:
        print(' '.join(str(territory) for territory in row))
    print()

# Sistema de combate: Piedra, Papel o Tijera
def combat(player_name):
    player_move = input("Elige tu movimiento (Piedra, Papel, Tijera): ")
    ia_move = random.choice(MOVES)
    print(f"La IA ha jugado: {ia_move}")

    if player_move == ia_move:
        print("¡Empate! Jueguen de nuevo.")
        return combat(player_name)  # Reintenta en caso de empate
    elif (player_move == 'Piedra' and ia_move == 'Tijera') or (player_move == 'Papel' and ia_move == 'Piedra') or (player_move == 'Tijera' and ia_move == 'Papel'):
        print(f"{player_name} gana el combate!")
        return True
    else:
        print("La IA gana el combate!")
        return False

# Turno del jugador
def player_turn(player, map_grid):
    while True:
        try:
            x, y = map(int, input("Ingresa las coordenadas del territorio que quieres conquistar (x y): ").split())
            if map_grid[x][y].owner == '_':
                map_grid[x][y].owner = 'J'  # 'J' para jugador
                resource_type = map_grid[x][y].resources
                player.add_resources(resource_type)  # Añadir recursos al jugador
                player.buy_terrain(map_grid[x][y].cost)

                print(f"Has conquistado el territorio en ({x}, {y}) y ganado {resource_type}")
                break
            elif map_grid[x][y].owner == 'C':
                print("El territorio está ocupado por la IA. ¡A combatir!")
                player.combat_cost()
                if combat(player.name):
                    map_grid[x][y].owner = 'J'  # El jugador gana el territorio
                    resource_type = map_grid[x][y].resources
                    player.add_resources(resource_type)
                    player.buy_terrain(map_grid[x][y].cost)
                    print(f"Has conquistado el territorio en ({x}, {y}) y ganado {resource_type}")
                break
            else:
                print("Territorio ya conquistado, elige otro.")
        except (ValueError, IndexError):
            print("Entrada inválida. Ingresa coordenadas válidas.")

# Turno de la IA
def ia_turn(ia,map_grid):
    while True:
        x, y = random.randint(0, MAP_SIZE - 1), random.randint(0, MAP_SIZE - 1)
        if map_grid[x][y].owner == '_':
            map_grid[x][y].owner = 'C'  # 'C' para IA
            ia.add_resources(map_grid[x][y].resources)
            ia.buy_terrain(map_grid[x][y].cost)
            print(f"La IA ha conquistado el territorio en ({x}, {y})")
            break
        elif map_grid[x][y].owner == 'J':
            print(f"La IA quiere conquistar tu territorio en ({x}, {y}). ¡A combatir!")
            ia.combat_cost()
            if not combat("Jugador"):  # El jugador defiende el territorio
                map_grid[x][y].owner = 'C'
                ia.add_resources(map_grid[x][y].resources)
                ia.buy_terrain(map_grid[x][y].cost)
                print(f"La IA ha conquistado tu territorio en ({x}, {y})")
            break

# Verificar si hay territorios disponibles
def is_game_over(map_grid):
    for row in map_grid:
        for territory in row:
            if territory.owner == '_':  # Hay al menos un territorio no conquistado
                return False
    return True

def ganador(player, ia):
    print("\nPuntuaciones finales:")
    player.show_resources()
    ia.show_resources()

    if player.score > ia.score:
        print(f"¡{player.name} gana el juego con {player.score} puntos!")
    elif player.score < ia.score:
        print(f"La {ia.name} gana el juego con {ia.score} puntos.")
    else:
        print("Es un empate.")

def main():
    print("Inicio de juego")
    player = Player() #Jugador  
    ia= IA()   #IA
    map_grid = create_map()  # Generación aleatoria del mapa
    print(f"¡Bienvenido a Conquista de Territorios!")

    while not is_game_over(map_grid):
        # Mostrar el estado del mapa
        display_map(map_grid)

        # Mostrar los recursos del jugador
        player.show_resources()

        # Turno del jugador
        player_turn(player, map_grid)

        player.show_resources()

        # Turno de la IA
        ia_turn(ia,map_grid)

        #Mostrar recursos de IA
        ia.show_resources()

        # Verificar si el juego ha terminado
        if is_game_over(map_grid):
            display_map(map_grid)
            break

    # Mostrar recursos finales al terminar el juego
    print("\nEl juego ha terminado.")
    ganador(player,ia)

if __name__ == "__main__":
    main()