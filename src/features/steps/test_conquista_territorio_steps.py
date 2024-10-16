from behave import given, when, then
from src.main import Player, create_map, is_game_over, Territory

# Se crea el jugador y el mapa, inicializando dinero y recursos.
@given("el jugador inicia con 100 dinero y 0 recursos")
def step_given_jugador_inicia(context):
    context.player = Player()
    context.map_grid = create_map()
    context.player.money = 100

# El jugador conquista el territorio en (0, 0) de forma directa.
@when("el jugador elige conquistar el territorio en (0, 0)")
def step_when_jugador_conquista(context):
    if context.map_grid[0][0].owner == '_':
        context.map_grid[0][0].owner = 'J'
        resource_type = context.map_grid[0][0].resources
        context.player.add_resources(resource_type)
        context.player.buy_terrain(context.map_grid[0][0].cost)

# Verificamos que el territorio en (0, 0) esté conquistado por el jugador.
@then("el territorio en (0, 0) debería estar conquistado por el jugador")
def step_then_territorio_conquistado(context):
    assert context.map_grid[0][0].owner == 'J'

# Confirmamos que el jugador ha gastado dinero.
@then("el jugador debería tener menos dinero")
def step_then_jugador_menos_dinero(context):
    assert context.player.money < 100

# Comprobamos que el jugador recibió 1 recurso del tipo correspondiente.
@then("el jugador debería tener 1 recurso del tipo de ese territorio")
def step_then_jugador_tiene_recurso(context):
    resource_type = context.map_grid[0][0].resources
    assert context.player.resources[resource_type] == 1

# Configuramos el mapa con todos los territorios conquistados menos uno.
@given("todos los territorios están conquistados excepto uno")
def step_given_un_territorio_libre(context):
    context.player = Player()
    context.map_grid = create_map()
    for row in context.map_grid:
        for territory in row:
            territory.owner = 'J'
    context.map_grid[4][4].owner = '_'  # El último territorio libre

# El jugador conquista el último territorio libre sin interacción manual.
@when("el jugador conquista el último territorio disponible")
def step_when_conquista_ultimo(context):
    if context.map_grid[4][4].owner == '_':
        context.map_grid[4][4].owner = 'J'
        resource_type = context.map_grid[4][4].resources
        context.player.add_resources(resource_type)
        context.player.buy_terrain(context.map_grid[4][4].cost)

# Verificamos que no quedan territorios libres y que el juego termina.
@then("el juego debería terminar")
def step_then_juego_termina(context):
    assert is_game_over(context.map_grid)

# Se muestra el resumen de recursos del jugador.
@then("el jugador debería ver su resumen de recursos")
def step_then_mostrar_resumen(context):
    context.player.show_resources()
