from behave import given, when, then
from src.main import Player, IA, create_map, combat, player_turn, ia_turn

@given("el jugador inicia con 100 dinero y 0 recursos")
def step_given_jugador_inicia(context):
    context.player = Player()
    context.map_grid = create_map()

@when("el jugador elige conquistar un territorio ocupado por la IA")
def step_when_conquistar_territorio(context):
    context.map_grid[0][0].owner = 'C'  # IA tiene el territorio

@when("el jugador gana el combate")
def step_when_jugador_gana(context):
    # Simulación de combate donde el jugador siempre gana
    context.map_grid[0][0].owner = 'J'
    resource_type = context.map_grid[0][0].resources
    context.player.add_resources(resource_type)
    context.player.buy_terrain(context.map_grid[0][0].cost)

@then("el jugador debería conquistar el territorio")
def step_then_conquistar_territorio(context):
    assert context.map_grid[0][0].owner == 'J'

@then("el jugador debería tener menos dinero")
def step_then_menos_dinero(context):
    assert context.player.money < 100

@given("el jugador y la IA han conquistado territorios")
def step_given_territorios_conquistados(context):
    context.player = Player()
    context.ia = IA()
    context.map_grid = create_map()
    context.map_grid[0][0].owner = 'J'  # Jugador
    context.map_grid[0][1].owner = 'C'  # IA

@when("la IA intenta conquistar un territorio del jugador")
def step_when_ia_intenta_conquistar(context):
    # Simulación de que la IA decide atacar el territorio del jugador
    context.target_position = (0, 0)

@when("la IA gana el combate")
def step_when_ia_gana(context):
    # Simulación directa de la IA ganando el combate y conquistando el territorio
    x, y = context.target_position
    context.map_grid[x][y].owner = 'C'

@then("el territorio debería pertenecer a la IA")
def step_then_territorio_ia(context):
    assert context.map_grid[0][0].owner == 'C'

@given("el mapa está generado y el jugador y la IA tienen 100 dinero")
def step_given_mapa_generado(context):
    context.player = Player()
    context.ia = IA()
    context.map_grid = create_map()

@when("el jugador toma su turno para conquistar un territorio")
def step_when_jugador_turno(context):
    # Simulación de turno del jugador
    x, y = 0, 0
    if context.map_grid[x][y].owner == '_':
        context.map_grid[x][y].owner = 'J'
        resource_type = context.map_grid[x][y].resources
        context.player.add_resources(resource_type)
        context.player.buy_terrain(context.map_grid[x][y].cost)

@when("luego la IA toma su turno para conquistar un territorio")
def step_when_ia_turno(context):
    # Simulación de turno de la IA
    x, y = 0, 1
    if context.map_grid[x][y].owner == '_':
        context.map_grid[x][y].owner = 'C'
        context.ia.buy_terrain(context.map_grid[x][y].cost)

@then("ambos deberían tener territorios conquistados")
def step_then_territorios_conquistados(context):
    assert context.map_grid[0][0].owner == 'J'  # Jugador conquistó
    assert context.map_grid[0][1].owner == 'C'  # IA conquistó
