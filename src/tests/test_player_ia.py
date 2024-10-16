import pytest
from src.main import Player, IA, Territory

# Test para verificar la inicialización correcta del jugador
def test_player_initialization():
    player = Player()
    # Verifica que el jugador comience con 100 de dinero
    assert player.money == 100
    # Verifica que el jugador tenga 0 unidades de cada recurso
    assert player.resources == {'Agua': 0, 'Madera': 0, 'Comida': 0}
    # Verifica que el nombre del jugador sea "Jugador"
    assert player.name == "Jugador"

# Test para verificar la inicialización correcta de la IA
def test_ia_initialization():
    ia = IA()
    # Verifica que la IA comience con 100 de dinero
    assert ia.money == 100
    # Verifica que la IA tenga 0 unidades de cada recurso
    assert ia.resources == {'Agua': 0, 'Madera': 0, 'Comida': 0}
    # Verifica que el nombre de la IA sea "IA"
    assert ia.name == "IA"

# Test para verificar que el jugador puede añadir recursos correctamente
def test_add_resources_player():
    player = Player()
    # Simula que el jugador adquiere "Agua" como recurso
    player.add_resources('Agua')
    # Verifica que el recurso "Agua" se incremente a 1
    assert player.resources['Agua'] == 1

# Test para verificar que la IA puede añadir recursos correctamente
def test_add_resources_ia():
    ia = IA()
    # Simula que la IA adquiere "Madera" como recurso
    ia.add_resources('Madera')
    # Verifica que el recurso "Madera" se incremente a 1
    assert ia.resources['Madera'] == 1

# Test para verificar que el jugador puede comprar un terreno y se deduzca el dinero correctamente
def test_buy_terrain_player():
    player = Player()
    # Simula la compra de un terreno que cuesta 10
    player.buy_terrain(10)
    # Verifica que el dinero del jugador se reduzca a 90
    assert player.money == 90

# Test para verificar que la IA puede comprar un terreno y se deduzca el dinero correctamente
def test_buy_terrain_ia():
    ia = IA()
    # Simula la compra de un terreno que cuesta 20
    ia.buy_terrain(20)
    # Verifica que el dinero de la IA se reduzca a 80
    assert ia.money == 80
