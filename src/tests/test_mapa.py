from src.main import create_map, display_map
from src.main import Territory

def test_create_map():
    map_grid = create_map() #Creación de mapa
    assert len(map_grid) == 5 #Verificamos las dimensiones del mapa 5 x 5
    assert len(map_grid[0]) == 5 #Verificamos la cantidad de columnas

    #Verificamos que cada celda tenga un objeto territory
    assert all(isinstance(territory, Territory) for row in map_grid for territory in row) 
    
