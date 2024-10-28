# Torneo Dragon Ball

Este proyecto pertenece al [reto 42](https://github.com/mouredev/roadmap-retos-programacion/blob/main/Roadmap/42%20-%20TORNEO%20DRAGON%20BALL/ejercicio.md) de los [retos de programación de mouredev](https://retosdeprogramacion.com/).

## Instalación

Para instalar las dependencias del proyecto, ejecuta lo siguiente:

### pipenv

```bash
pipenv install
```

### venv

```bash
python -m venv .venv
.venv/Scripts/activate
pip install -r requirements.txt
```

## Ejecución

Para ejecutar el proyecto, ejecuta el siguiente comando:

```bash
reflex run
```

Se abrirá un servidor en la dirección `http://localhost:3000`.

## Características

- **Número de luchadores**
  - Se podrá elegir un número de luchadores dentro del conjunto $\{ 2^n \mid n \in \mathbb{Z}, 1 \leq n \leq 10 \}$ *
  - Para los mortales, esto es: 2, 4, 8, 16, 32, 64, 128, 256, 512 o 1024.
  - Es necesaria una potencia de 2 para que el torneo funcione correctamente.
- **Nombre y atributos de los luchadores**
  - Se deberá escribir un nombre para cada luchador y rellenar sus atributos (velocidad, ataque y defensa)
  - Los valores permitidos son del 1 al 100.
  - Existe un botón para rellenar automáticamente los nombres y atributos.
    - Los atributos seguirán una distribución normal con una media entre 40 y 60 y una desviación estándar entre 10 y 15.
    - La nacionalidad de los nombres aleatorios podrá ser configurada a través del botón adyacente al de rellenar aleatoriamente.
- **Torneo**
  - Se iniciará el torneo al pulsar el botón "Iniciar torneo".
  - Aparecerán páginas para cada ronda, pudiendo consultar en cada momento cualquier ronda.
  - Cuando todos los luchadores de una ronda estén listos, se podrá realizar un sorteo para determinar los emparejamientos.
- **Combate**
  - Los luchadores empezarán el combate con 100 de salud.
  - Usando los atributos del luchador y un estado de forma (aleatorio), se obtendrán los valores mínimos y máximos para cada atributo de ese luchador en ese combate.
  - Cada luchador preparará su próximo ataque con valores aleatorios dentro de los límites de sus atributos para ese combate.
    - La velocidad determinará el tiempo en el que realizará su ataque ($100/velocidad$ segundos).
  - El luchador con menor tiempo atacará primero y el oponente realizará su defensa.
    - La defensa siempre tiene un 20% de probabilidad de esquivar el ataque.
    - Si el golpe no es esquivado, el atacante hará $ataque - defensa$ de daño al oponente, con un mínimo del 10% del ataque.
    - Después de cada ataque, el atacante preparará su próximo ataque y el tiempo en el que lo realizará.
    - Un luchador rápido puede hacer más de un ataque antes del ataque de su rival.
  - El combate terminará cuando uno de los dos luchadores se quede sin salud. El ganador pasará a la siguiente ronda y se quedará en espera hasta que todos los combates de la ronda terminen, momento en el que se podrá realizar el sorteo de la siguiente ronda.
