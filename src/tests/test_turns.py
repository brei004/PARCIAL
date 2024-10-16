from src.main import create_map, player_turn, ia_turn, Player, IA

# Prueba para verificar que el jugador pueda tomar su turno y conquistar un territorio.
def test_player_turn(mocker):
    player = Player()
    map_grid = create_map()
    # Simulamos la entrada del usuario para elegir las coordenadas (0, 0)
    mocker.patch('builtins.input', return_value="0 0")
    # Aseguramos que el territorio en (0, 0) esté disponible
    map_grid[0][0].owner = '_'
    # Ejecutamos el turno del jugador
    player_turn(player, map_grid)
    # Comprobamos que el jugador haya conquistado el territorio
    assert map_grid[0][0].owner == 'J'

def test_ia_turn(mocker):
    ia = IA()
    map_grid = create_map()
    # Simula que la IA elija aleatoriamente 0 para x y 0 para y
    mocker.patch('random.randint', side_effect=[0, 0])
    # Asegura que el territorio en (0, 0) esté disponible
    map_grid[0][0].owner = '_'
    # Ejecuta el turno de la IA
    ia_turn(ia, map_grid)
    assert map_grid[0][0].owner == 'C'
