Feature: Selección de Dificultad y Sistema de Puntaje

  Scenario: Selección de dificultad en el juego
    Given el juego se ha iniciado
    When el jugador selecciona la dificultad "2"
    Then el tamaño del mapa debería ser 4x4

  Scenario: Puntaje del jugador al recolectar recursos
    Given el jugador ha comenzado con 0 puntos
    When el jugador conquista un territorio con recurso "Madera"
    Then el puntaje del jugador debería ser 10

  Scenario: Puntaje del jugador al comprar terrenos
    Given el jugador ha comenzado con 0 puntos y 100 de dinero
    When el jugador compra un terreno de costo 20
    Then el puntaje del jugador debería ser 20
    And el dinero del jugador debería ser 80
