Feature: Conquista de Territorios

  Scenario: El jugador gana un combate contra la IA
    Given el jugador inicia con 100 dinero y 0 recursos
    When el jugador elige conquistar un territorio ocupado por la IA
    And el jugador gana el combate
    Then el jugador debería conquistar el territorio
    And el jugador debería tener menos dinero

  Scenario: La IA gana un combate y conquista un territorio del jugador
    Given el jugador y la IA han conquistado territorios
    When la IA intenta conquistar un territorio del jugador
    And la IA gana el combate
    Then el territorio debería pertenecer a la IA

  Scenario: Turnos alternos del jugador y la IA
    Given el mapa está generado y el jugador y la IA tienen 100 dinero
    When el jugador toma su turno para conquistar un territorio
    And luego la IA toma su turno para conquistar un territorio
    Then ambos deberían tener territorios conquistados
