from src.main import combat

# Test para verificar que el jugador gana el combate
def test_combat_player_win(mocker):
    # Simulamos que el jugador siempre elige "Piedra"
    mocker.patch('builtins.input', return_value='Piedra') 
    # Simulamos que la IA siempre elige "Tijera"
    mocker.patch('random.choice', return_value='Tijera')
    # Ejecutamos la función de combate y verificamos que el jugador gane
    result = combat("Alumno")
    assert result == True  # El jugador debería ganar porque "Piedra" vence a "Tijera"

# Test para verificar que la IA gana el combate
def test_combat_ia_win(mocker):
    # Simulamos que el jugador siempre elige "Piedra"
    mocker.patch('builtins.input', return_value='Piedra')
    # Simulamos que la IA siempre elige "Papel"
    mocker.patch('random.choice', return_value='Papel')
    # Ejecutamos la función de combate y verificamos que la IA gane
    result = combat("Alumno")
    assert result == False  # La IA debería ganar porque "Papel" vence a "Piedra"
