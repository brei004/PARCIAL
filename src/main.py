import random

MAP_SIZE = 5

# Diferentes tipos de territorios
TERRAIN_TYPES = ['Pradera', 'Bosque', 'Montaña']
RESOURCE_TYPES = ['Agua', 'Madera', 'Comida']

# Territorio como una clase
class Territory:
    def __init__(self):
        self.terrain = random.choice(TERRAIN_TYPES) #Eleccion aleatoria de terreno
        self.resources = random.choice(RESOURCE_TYPES)#Eleccion aleatoria de recurso
        self.owner = '_'  # Sin conquistar: '_', Jugador: 'J', Computadora: 'C'
    def __str__(self):
        return f"{self.terrain[0]}-{self.resources[0]}"  #impresión de celda 

# Mostrar el mapa
def display_map(map_grid):
    for row in map_grid: #Para cada fila
        print(' '.join(str(territory) for territory in row)) #Imprimimos cada terreno
    print()

# Crear el mapa de territorios
def create_map():
    return [[Territory() for _ in range(MAP_SIZE)] for _ in range(MAP_SIZE)] #Crear un territorio para cada celda del mapa


def main():
    map_grid = create_map()  # Generación aleatoria del mapa
    print("¡Bienvenido a Conquista de Territorios!")

    display_map(map_grid)

if __name__ == "__main__":
    main()