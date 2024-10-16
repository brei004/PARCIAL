from behave import given, when, then
from src.main import create_map

@given("el jugador inicia el juego")
def step_given_jugador_inicia_el_juego(context):
    # Contexto del juego
    context.map_grid = None

@when("se genera el mapa aleatorio")
def step_when_se_genera_el_mapa_aleatorio(context):
    # Generación del mapa
    context.map_grid = create_map()

@then("el jugador debería ver un mapa de 5x5 territorios")
def step_then_el_jugador_ve_mapa(context):
    assert context.map_grid is not None, "El mapa no fue generado"
    assert len(context.map_grid) == 5, "El mapa no tiene 5 filas"
    assert all(len(row) == 5 for row in context.map_grid), "Alguna fila del mapa no tiene 5 territorios"
