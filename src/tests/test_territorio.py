import pytest
from src.main import Territory, TERRAIN_TYPES, RESOURCE_TYPES

def test_territory_initialization():
    territory = Territory() #Instancia territorio
    assert territory.terrain in TERRAIN_TYPES #Verificar que sea correcto el terreno de nuestras 3 opciones
    assert territory.resources in RESOURCE_TYPES#Verificar que sea correcto el recurso de nuestras 3 opciones
    assert territory.owner == '_' #Por defecto no tiene dueño

