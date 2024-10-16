import pytest
from src.main import validate_difficulty, validate_combat_move, validate_coordinates

# Test para validar la selección de nivel usando regex
def test_validate_difficulty():
    assert validate_difficulty("1") == True  # Nivel Fácil
    assert validate_difficulty("2") == True  # Nivel Medio
    assert validate_difficulty("3") == True  # Nivel Difícil
    assert validate_difficulty("0") == False  # Nivel inválido
    assert validate_difficulty("4") == False  # Nivel inválido
    assert validate_difficulty("a") == False  # Entrada no numérica
    assert validate_difficulty("12") == False  # Más de un dígito

# Test para validar que el movimiento de combate sea correcto usando regex
def test_validate_combat_move():
    assert validate_combat_move("Piedra") == True
    assert validate_combat_move("Papel") == True
    assert validate_combat_move("Tijera") == True
    assert validate_combat_move("piedra") == True  # Insensible a mayúsculas
    assert validate_combat_move("papel") == True  # Insensible a mayúsculas
    assert validate_combat_move("scissors") == False  # Movimiento inválido
    assert validate_combat_move("Rock") == False  # Movimiento en otro idioma

# Test para validar que las coordenadas ingresadas por el usuario sean correctas usando regex
def test_validate_coordinates():
    assert validate_coordinates("2 3") == True  # Formato correcto
    assert validate_coordinates("10 5") == True  # Formato correcto con dos dígitos
    assert validate_coordinates("a b") == False  # Letras en lugar de números
    assert validate_coordinates("1,2") == False  # Uso de coma en lugar de espacio
    assert validate_coordinates("3") == False  # Solo un número sin par
    assert validate_coordinates(" 4 5") == False  # Espacio al inicio

# Test para validar que la entrada del nivel no sea válida si hay caracteres extraños
def test_validate_difficulty_extra_cases():
    assert validate_difficulty("1\n") == True  # Caracter de nueva línea adicional
    assert validate_difficulty(" 2 ") == False  # Espacios adicionales
    assert validate_difficulty("3abc") == False  # Texto junto con el número
