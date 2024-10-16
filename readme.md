
### KANBAN 

Se definieron 6 historias de usuario

![alt text](image.png)

Con el siguiente formato usando gherkin 

![alt text](image-1.png)

### Configuración de branches

![alt text](imagenes/image-1.png)

### Observación 

Para el uso de pytest se presentaron problemas con la importación de modulos, por ese motivo todas las clases se encuentran en la carpeta main.py para evitar esos problemas.

## Creación de mapa (branch feature/mapa)

Nuestro juego tendrá 3 tipos de zonas (Pradera, Bosque, Montaña) y 3 tipos de recompensas (Agua, Madera, Comida)

Según la historia de usuario definida en el kanban necesitamos que se cree el mapa aleatoriamente indicando la zona y los recursos correspondiente

Por defecto, el terreno no tiene dueño. Por ese motivo se indicará como sin reclamar -> "_" Jugador -> "J" Computadora -> "C"

![alt text](imagenes/image-2.png)

#### Pruebas unitarias

```python
test.territorio
```

![alt text](imagenes/image-3.png)

```python
test.mapa
```
![alt text](imagenes/image-4.png)

```python
Ejecución
```
![alt text](imagenes/image-8.png)
#### BDD

```python
steps
```
Para el desarrollo guiado comportamiento usaremos behave

![alt text](imagenes/image-5.png)

```python
feature
```

![alt text](imagenes/image-6.png)

```python
Ejecución
```

![alt text](imagenes/image-7.png)

#### CI/CD

El archivo main.yml se configura para establecer un pipeline automatizado que facilita la integración continua (CI) y la entrega continua (CD). Este pipeline tiene como objetivo mejorar la calidad del desarrollo y la eficiencia del despliegue al automatizar tareas clave durante el ciclo de vida del proyecto.

![alt text](imagenes/image-57.png)

- Con dependencias 

![alt text](imagenes/image-58.png)

- Ejecución

![alt text](imagenes/image-59.png)

### Actualización kanban 

![alt text](image-2.png)

## Sistema de recolección de recursos y conquista (branch feature/recursos-expansion)

Cada usuario deberá contar con dinero para poder comprar el territorio

Cada usuario gastará dinero para obtener el territorio y obtendrá los recursos de este mismo

- Cambios en el código

![alt text](imagenes/image-9.png)

![alt text](imagenes/image-11.png)

- Turno del jugador

Necesitamos que el jugador pueda jugar por turnos 

![alt text](imagenes/image-10.png)

Necesitamos que el juego acabe cuando ya no queden territorios por conquistar

![alt text](imagenes/image-12.png)


- Bucle principal

![alt text](imagenes/image-13.png)

```python
Ejecución
```

![alt text](imagenes/image-14.png)

#### Pruebas unitarias

Debido a que se añadió la clase Player y la lógica del turno del jugador se definen nuevos test

![alt text](imagenes/image-15.png)

![alt text](imagenes/image-16.png)

```python
Ejecución
```

![alt text](imagenes/image-17.png)

### BDD

```python
Feature: Conquista de territorio
```

![alt text](imagenes/image-18.png)


```python
test_conquista_territorio_steps.py
```

La acción when para "el jugador elige conquista el territorio"
se selecciona la casilla automaticamente, evitando tener que ingresar manualmente las coordenadas


![alt text](imagenes/image-19.png)

![alt text](imagenes/image-20.png)

![alt text](imagenes/image-21.png)

```python
Ejecución
```

![alt text](imagenes/image-22.png)

```python
CI/CD Pipeline
```
![alt text](imagenes/image-27.png)

### Actualización kanban 

![alt text](image-3.png)

## Sistema de combate y ia (branch feature/combate-ia)

Vamos a definir la clase de la ia, para que también pueda gastar dinero

![alt text](imagenes/image-24.png)

La ia jugará su turno luego que nosotros e intentará conquistar una tierra disponible

![alt text](imagenes/image-25.png)

Por otro lado, cuando se intente conquistar un territorio enemigo se decidirá quien lo obtiene mediante piedra, papel o tijera

![alt text](imagenes/image-23.png)

- Actualizamos el flujo del programa

![alt text](imagenes/image-26.png)

### Test

En los siguientes tests se usará mocker, una herramienta que nos permite simular el comportamiento de funciones en nuestros tests, por ejemplo simular el ingreso de datos por consola.

Se define un test para los combates por el territorio

![alt text](imagenes/image-30.png)


Tests para inicializacion de clases 

![alt text](imagenes/image-31.png)

Tests para comprar y obtención de recursos 

![alt text](imagenes/image-32.png)


### BDD

Se actualiza el feature de conquista de territorios

Ahora en el contexto de combates, analizamos el compartamiento para las caracteristicas añadidas

![alt text](imagenes/image-28.png)


Steps escenario 1

![alt text](imagenes/image-34.png)

Steps escenario 2

![alt text](imagenes/image-35.png)

Steps escenario 3

![alt text](imagenes/image-36.png)

### Actualización de pipeline 

Como se añadió mocker necesitamos agregarlo en el pipeline

![alt text](imagenes/image-37.png)

```python
Ejecución
```

![alt text](imagenes/image-38.png)

![alt text](imagenes/image-39.png)   

### Actualización kanban 

![alt text](image-4.png)

## Sistema de puntuacion y dificultad (branch feature/puntuacion-dificultad)

Para este caso, el sistema de puntucación funciona así:

- 10 puntos por recurso obtenido
- 20 puntos por territorio conquistado

El sistema de dificultad tiene la siguientes caracteristicas:

Tamaño base 2 x 2

Cada nivel tiene un tamaño de tamaño_base * nivel 

Cada territorio va a costar desde random(5,10) * nivel

#### Cambios en el código

- Sistema de puntaje 

Player e IA comparten estas caracterisiticas y al ser IA practicamente una Herencia de Player se hizo lo siguiente: 

![alt text](imagenes/image-41.png)

Configuración de puntajes

![alt text](imagenes/image-40.png)

Conteo de puntos 

![alt text](imagenes/image-42.png)

- Sistema de dificultad 

Tamaño de mapa = tamaño base * nivel

![alt text](imagenes/image-43.png)

Costo de compra random(5,10) * nivel

![alt text](imagenes/image-44.png)

#### REGEX 

- Validación de combate 

Solo podemos elegir piedra, papel o tijera

![alt text](imagenes/image-45.png)

- Validación de coordenadas

Las coordenadas solo serán numéricas y separadas por un espacio

![alt text](imagenes/image-46.png)

- Validación de dificultad

La dificultad solo podrá ser un número entre 1 y 3

![alt text](imagenes/image-47.png)


#### Test 

Luego de agregar esas validaciones al código se crearon los siguientes tests 

![alt text](imagenes/image-48.png)

![alt text](imagenes/image-49.png)

#### BDD 

Se agregó lo siguiente en test_dificultad_puntaje.feature 

![alt text](imagenes/image-50.png)


- Escenario 1

![alt text](imagenes/image-51.png)


- Escenario 2

![alt text](imagenes/image-52.png)

- Escenario 3

![alt text](imagenes/image-53.png)

### Ejecución 

- CI / CD

![alt text](imagenes/image-54.png)

- Consola

![alt text](imagenes/image-55.png)

- Puntaje 

![alt text](imagenes/image-56.png)

### Actualización kanban 

![alt text](image-5.png)

## Rama Develop

Ahora vamos a juntar el proyecto en la rama develop para empezar a **contenerizar** el proyecto y darle metricas en **graphana**y **prometheus**

- Dockerfile

![alt text](imagenes/image-60.png)

- Construcción de imagen 

![alt text](imagenes/image-61.png)

- Ejecución de contenedor

![alt text](imagenes/image-62.png)

- Vista en docker desktop 

![alt text](imagenes/image-63.png)

## Graphana y prometheus

Para las gráficas añadimos métricas

![alt text](imagenes/image-64.png)

Tal que cada vez que se agreguen recursos se monitoree

![alt text](imagenes/image-65.png)

- docker-compose

Usamos docker-compose para correr diferentes servicios en nuestro contenedor, indicando su puerto correspondiente

![alt text](imagenes/image-66.png)

- prometheus.yml

Usamos este archivo para poder obtener desde el puerto de la app las métricas y prometheus pueda leerlas

![alt text](imagenes/image-67.png)

- Ejecución

Sucede un error, debido a que se tiene que ingresar datos por consola, el flujo de la aplicación se interrumpe

![alt text](imagenes/image-68.png)

### Kanban final 

Finalmente, queda en revisión el uso de métricas con prometheus y graphana

![alt text](image-7.png)