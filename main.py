import random

MAP_SIZE = 5

# Diferentes tipos de territorios
TERRAIN_TYPES = ['Pradera', 'Bosque', 'Montaña']
RESOURCE_TYPES = ['Gold', 'Wood', 'Food']

# Territorio como una clase
class Territory:
    def __init__(self):
        self.terrain = random.choice(TERRAIN_TYPES)
        self.resources = random.choice(RESOURCE_TYPES)
        self.owner = '_'  # Sin conquistar: '_', Jugador: 'J', Computadora: 'C'
    def __str__(self):
        return f"{self.terrain[0]}-{self.resources[0]}"    

# Crear el mapa de territorios
def create_map():
    return [[Territory() for _ in range(MAP_SIZE)] for _ in range(MAP_SIZE)]

# Mostrar el mapa
def display_map(map_grid):
    for row in map_grid:
        print(' '.join(str(territory) for territory in row))
    print()


def main():
    map_grid = create_map()  # Generación aleatoria del mapa
    print("¡Bienvenido a Conquista de Territorios!")

    display_map(map_grid)

if __name__ == "__main__":
    main()