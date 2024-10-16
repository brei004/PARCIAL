from behave import given, when, then
from src.main import Player, create_map, validate_difficulty

@given("el juego se ha iniciado")
def step_given_juego_iniciado(context):
    context.player = Player()

@when('el jugador selecciona la dificultad "{difficulty}"')
def step_when_selecciona_dificultad(context, difficulty):
    if validate_difficulty(difficulty):
        context.map_grid = create_map(int(difficulty))

@then("el tamaño del mapa debería ser 4x4")
def step_then_tamano_mapa(context):
    assert len(context.map_grid) == 4
    assert len(context.map_grid[0]) == 4

@given("el jugador ha comenzado con 0 puntos")
def step_given_jugador_con_puntaje_cero(context):
    context.player = Player()
    context.player.score = 0

@when('el jugador conquista un territorio con recurso "Madera"')
def step_when_conquista_territorio(context):
    context.player.add_resources("Madera")

@then("el puntaje del jugador debería ser 10")
def step_then_puntaje_jugador(context):
    assert context.player.score == 10

@given("el jugador ha comenzado con 0 puntos y 100 de dinero")
def step_given_jugador_con_dinero_y_puntos(context):
    context.player = Player()
    context.player.score = 0
    context.player.money = 100

@when("el jugador compra un terreno de costo 20")
def step_when_compra_terreno(context):
    context.player.buy_terrain(20)

@then("el puntaje del jugador debería ser 20")
def step_then_puntaje_terreno(context):
    assert context.player.score == 20

@then("el dinero del jugador debería ser 80")
def step_then_dinero_jugador(context):
    assert context.player.money == 80
