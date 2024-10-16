from prometheus_client import Counter, Gauge, start_http_server
import random
import re
import time

# Definición de métricas
player_score = Gauge('player_score', 'Puntuación actual del jugador')
ia_score = Gauge('ia_score', 'Puntuación actual de la IA')
player_resources = Counter('player_resources_collected', 'Recursos recolectados por el jugador', ['resource'])
ia_resources = Counter('ia_resources_collected', 'Recursos recolectados por la IA', ['resource'])

# Iniciar servidor de métricas Prometheus
start_http_server(8000)

MAP_SIZE_BASE = 2

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
        player_resources.labels(resource_type).inc()  # Incrementar contador de recursos
        player_score.set(self.score) # Actualizar metricas

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

# IA
class IA(Player):
    def __init__(self):
        super().__init__(name="IA")

# Territorio como una clase
class Territory:
    def __init__(self,difficulty=1):
        self.terrain = random.choice(TERRAIN_TYPES)
        self.cost = random.randint(5* difficulty,10 * difficulty)
        self.resources = random.choice(RESOURCE_TYPES)
        self.owner = '_'  # Sin conquistar: '_', Jugador: 'J', Computadora: 'C'
    
    def __str__(self):
        return f"{self.terrain[0]}-{self.resources[0]}-{self.cost}$-#{self.owner}"    

# Crear el mapa de territorios
def create_map(difficulty=1):
    MAP_SIZE = difficulty * MAP_SIZE_BASE
    return [[Territory(difficulty) for _ in range(MAP_SIZE)] for _ in range(MAP_SIZE)]

# Mostrar el mapa
def display_map(map_grid):
    for row in map_grid:
        print(' '.join(str(territory) for territory in row))
    print()

def validate_combat_move(input_str):
    # Regex para aceptar solo 'Piedra', 'Papel' o 'Tijera' 
    pattern = r'^(Piedra|Papel|Tijera)$'
    return re.match(pattern, input_str, re.IGNORECASE) is not None

# Sistema de combate: Piedra, Papel o Tijera
def combat(player_name):
    while True:
        player_move = input("Elige tu movimiento (Piedra, Papel, Tijera): ")
        if not validate_combat_move(player_move):
            print("Movimiento inválido. Por favor elige 'Piedra', 'Papel' o 'Tijera'.")
            continue
        
        ia_move = random.choice(MOVES)
        print(f"La IA ha jugado: {ia_move}")

        if player_move == ia_move:
            print("¡Empate! Jueguen de nuevo.")
            continue  # Evitar recursión, usa bucle para reintentar en caso de empate
        elif (player_move == 'Piedra' and ia_move == 'Tijera') or (player_move == 'Papel' and ia_move == 'Piedra') or (player_move == 'Tijera' and ia_move == 'Papel'):
            print(f"{player_name} gana el combate!")
            return True
        else:
            print("La IA gana el combate!")
            return False




def validate_coordinates(input_str):
    # Regex para validar que la entrada sea dos números separados por un espacio
    pattern = r'^\d+\s\d+$'
    return re.match(pattern, input_str) is not None

# Turno del jugador
def player_turn(player, map_grid):
    while True:
        try:
            # Usar la función de validación para verificar las coordenadas
            user_input = input("Ingresa las coordenadas del territorio que quieres conquistar (x y): ")
            if not validate_coordinates(user_input):
                print("Entrada inválida. Debe ingresar dos números separados por un espacio.")
                continue  # Solicita la entrada nuevamente si no es válida
            
            x, y = map(int, user_input.split())
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
    map_size = len(map_grid)
    while True:
        x, y = random.randint(0, map_size - 1), random.randint(0, map_size - 1)
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
def validate_difficulty(input_str):
    # Regex para aceptar solo '1', '2' o '3'
    pattern = r'^[1-3]$'
    return re.match(pattern, input_str) is not None

def nivel(difficulty=1):
    while True:
        difficulty = input("Selecciona la dificultad (1: Fácil, 2: Media, 3: Difícil): ")
        if validate_difficulty(difficulty):
            return int(difficulty)
        print("Dificultad no válida, intenta de nuevo.")


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
    dificultad = nivel()
    player = Player() #Jugador  
    ia= IA()   #IA
    map_grid = create_map(dificultad)  # Generación aleatoria del mapa
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