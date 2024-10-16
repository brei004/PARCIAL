Feature: Conquista de Territorios

  Scenario: Generación y visualización del mapa
    Given el jugador inicia el juego
    When se genera el mapa aleatorio
    Then el jugador debería ver un mapa de 2x2 territorios
