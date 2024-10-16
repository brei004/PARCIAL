import random

MAP_SIZE = 5

# Diferentes tipos de territorios
TERRAIN_TYPES = ['Pradera', 'Bosque', 'Montaña']
RESOURCE_TYPES = ['Agua', 'Madera', 'Comida']
# Movimientos posibles en el combate
MOVES = ['Piedra', 'Papel', 'Tijera'] 

# Clase Jugador que acumula recursos
class Player:
    def __init__(self):        
        self.resources = { #Recursos del jugador
            'Agua': 0,
            'Madera': 0,
            'Comida': 0
        }
        self.money = 100
        self.name = "Alumno"
    
    def add_resources(self, resource_type): #Funcion para ganar recursos
        self.resources[resource_type] += 1
    
    def buy_terrain(self, money): #Funcion para gastar dinero
        self.money -= money

    def show_resources(self):
        print(f"{self.name} tiene los siguientes recursos:")
        print("Dinero: ",self.money)
        for resource, amount in self.resources.items():
            print(f"{resource}: {amount}")

class IA:
    def __init__(self):        
        self.resources = {
            'Agua': 0,
            'Madera': 0,
            'Comida': 0
        }
        self.money = 100
        self.name = "IA"
    
    def add_resources(self, resource_type):
        self.resources[resource_type] += 1
    
    def buy_terrain(self, money):
        self.money -= money

    def show_resources(self):
        print(f"{self.name} tiene los siguientes recursos:")
        print("Dinero: ",self.money)

# Territorio como una clase
class Territory:
    def __init__(self):
        self.terrain = random.choice(TERRAIN_TYPES) #Eleccion aleatoria de terreno
        self.resources = random.choice(RESOURCE_TYPES)#Eleccion aleatoria de recurso
        self.owner = '_'  # Sin conquistar: '_', Jugador: 'J', Computadora: 'C'
        self.cost= 10 # Se añadió el costo del territorio 
    
    def __str__(self):
        return f"{self.terrain[0]}-{self.resources[0]}-{self.cost}$-#{self.owner}"    

# Crear el mapa de territorios
def create_map():
    return [[Territory() for _ in range(MAP_SIZE)] for _ in range(MAP_SIZE)]

# Mostrar el mapa
def display_map(map_grid):
    for row in map_grid: #Para cada fila
        print(' '.join(str(territory) for territory in row)) #Imprimimos cada terreno
    print()

# Sistema de combate: Piedra, Papel o Tijera
def combat(player_name):
    # Le pedimos al jugador que elija su movimiento
    player_move = input("Elige tu movimiento (Piedra, Papel, Tijera): ")
    
    # La IA elige un movimiento aleatorio
    ia_move = random.choice(MOVES)
    print(f"La IA ha jugado: {ia_move}")

    # Si hay empate, vuelve a jugarse
    if player_move == ia_move:
        print("¡Empate! Jueguen de nuevo.")
        return combat(player_name)  # Se llama otra vez hasta que no haya empate

    # Condiciones donde el jugador gana el combate
    elif (player_move == 'Piedra' and ia_move == 'Tijera') or \
         (player_move == 'Papel' and ia_move == 'Piedra') or \
         (player_move == 'Tijera' and ia_move == 'Papel'):
        print(f"{player_name} gana el combate!")
        return True  # Si el jugador gana, devuelve True

    # En cualquier otro caso, la IA gana
    else:
        print("La IA gana el combate!")
        return False  # Devuelve False si la IA gana


# Turno del jugador
def player_turn(player, map_grid):
    while True:
        try:
            #Ingreso de coordenadas del mapa
            x, y = map(int, input("Ingresa las coordenadas del territorio que quieres conquistar (x y): ").split())
            #Si está disponible obtenemos el territorio y pagamos el costo del mismo
            if map_grid[x][y].owner == '_':
                #Asignación
                map_grid[x][y].owner = 'J'  # 'J' para jugador
                #De recursos
                resource_type = map_grid[x][y].resources
                player.add_resources(resource_type)  # Añadir recursos al jugador
                #Gasto de dinero
                player.buy_terrain(map_grid[x][y].cost)

                print(f"Has conquistado el territorio en ({x}, {y}) y ganado {resource_type}")
                break
            elif map_grid[x][y].owner == 'C':
                print("El territorio está ocupado por la IA. ¡A combatir!")
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
            ia.buy_terrain(map_grid[x][y].cost)
            print(f"La IA ha conquistado el territorio en ({x}, {y})")
            break
        elif map_grid[x][y].owner == 'J':
            print(f"La IA quiere conquistar tu territorio en ({x}, {y}). ¡A combatir!")
            if not combat("Jugador"):  # El jugador defiende el territorio
                map_grid[x][y].owner = 'C'
                ia.buy_terrain(map_grid[x][y].cost)
                print(f"La IA ha conquistado tu territorio en ({x}, {y})")
            break

# Verificar si hay territorios disponibles
def is_game_over(map_grid):
    for row in map_grid:
        for territory in row:
            if territory.owner == '_':  # Hay al menos un territorio no conquistado sino, acaba
                return False
    return True

def main():
    
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
    player.show_resources()

if __name__ == "__main__":
    main()
