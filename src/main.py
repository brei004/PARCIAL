import random

MAP_SIZE = 5

# Diferentes tipos de territorios
TERRAIN_TYPES = ['Pradera', 'Bosque', 'Montaña']
RESOURCE_TYPES = ['Agua', 'Madera', 'Comida']

# Clase Jugador que acumula recursos
class Player:
    def __init__(self):        
        self.resources = { #Recursos del jugador
            'Agua': 0,
            'Madera': 0,
            'Comida': 0
        }
        self.money = 100 #Dinero disponible
    
    def add_resources(self, resource_type): #Funcion para ganar recursos
        self.resources[resource_type] += 1
    
    def buy_terrain(self, money): #Funcion para gastar dinero
        self.money -= money

    def show_resources(self): #Funcion para mostar los recursos actuales
        print(f"Player tiene los siguientes recursos:")
        print("Dinero: ",self.money)
        for resource, amount in self.resources.items():
            print(f"{resource}: {amount}")

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
            else:
                print("Territorio ya conquistado, elige otro.")
        except (ValueError, IndexError):
            print("Entrada inválida. Ingresa coordenadas válidas.")

# Verificar si hay territorios disponibles
def is_game_over(map_grid):
    for row in map_grid:
        for territory in row:
            if territory.owner == '_':  # Hay al menos un territorio no conquistado sino, acaba
                return False
    return True

def main():
    
    player = Player()  # Crear el jugador
    map_grid = create_map()  # Generación aleatoria del mapa
    print(f"¡Bienvenido a Conquista de Territorios!")

    while not is_game_over(map_grid):
        # Mostrar el estado del mapa
        display_map(map_grid)

        # Mostrar los recursos del jugador
        player.show_resources()

        # Turno del jugador
        player_turn(player, map_grid)

        # Verificar si el juego ha terminado
        if is_game_over(map_grid):
            break

    # Mostrar recursos finales al terminar el juego
    print("\nEl juego ha terminado.")
    player.show_resources()

if __name__ == "__main__":
    main()
