Feature: Conquista de Territorios

  Scenario: Jugador conquista un territorio
    Given el jugador inicia con 100 dinero y 0 recursos
    When el jugador elige conquistar el territorio en (0, 0)
    Then el territorio en (0, 0) debería estar conquistado por el jugador
    And el jugador debería tener menos dinero
    And el jugador debería tener 1 recurso del tipo de ese territorio

  Scenario: Fin del juego cuando todos los territorios son conquistados
    Given todos los territorios están conquistados excepto uno
    When el jugador conquista el último territorio disponible
    Then el juego debería terminar
    And el jugador debería ver su resumen de recursos
