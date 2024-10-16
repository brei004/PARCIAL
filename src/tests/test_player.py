import pytest
from src.main import Player

# Verifica que al iniciar el jugador tenga dinero y recursos correctos.
def test_player_initialization():
    player = Player()
    assert player.money == 100
    assert player.resources == {'Agua': 0, 'Madera': 0, 'Comida': 0}

# Añade recursos y verifica que se actualicen correctamente.
def test_add_resources():
    player = Player()
    player.add_resources('Agua')
    assert player.resources['Agua'] == 1
    player.add_resources('Madera')
    assert player.resources['Madera'] == 1

# Realiza compras de terreno y verifica la deducción del dinero.
def test_buy_terrain():
    player = Player()
    player.buy_terrain(10)
    assert player.money == 90
    player.buy_terrain(30)
    assert player.money == 60

# Captura la salida de recursos y dinero del jugador y verifica su formato.
def test_show_resources(capsys):
    player = Player()
    player.add_resources('Agua')
    player.add_resources('Comida')
    player.buy_terrain(10)
    player.show_resources()
    captured = capsys.readouterr() #Captura la salida
    assert "Dinero: 90" in captured.out  
    assert "Agua: 1" in captured.out
    assert "Comida: 1" in captured.out
