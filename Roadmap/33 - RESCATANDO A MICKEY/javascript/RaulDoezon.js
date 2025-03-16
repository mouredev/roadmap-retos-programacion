/*
  EJERCICIO:
  ¡Disney ha presentado un montón de novedades en su D23! 
  Pero... ¿Dónde está Mickey?
  Mickey Mouse ha quedado atrapado en un laberinto mágico 
  creado por Maléfica.
  Desarrolla un programa para ayudarlo a escapar.
  Requisitos:
  1. El laberinto está formado por un cuadrado de 6x6 celdas.
  2. Los valores de las celdas serán:
     - ⬜️ Vacío
     - ⬛️ Obstáculo
     - 🐭 Mickey
     - 🚪 Salida
  Acciones:
  1. Crea una matriz que represente el laberinto (no hace falta
  que se genere de manera automática).
  2. Interactúa con el usuario por consola para preguntarle hacia
  donde se tiene que desplazar (arriba, abajo, izquierda o derecha).
  3. Muestra la actualización del laberinto tras cada desplazamiento.
  4. Valida todos los movimientos, teniendo en cuenta los límites
  del laberinto y los obtáculos. Notifica al usuario.
  5. Finaliza el programa cuando Mickey llegue a la salida.
*/

const maze = [
  ["🐭", "⬛️", "⬛️", "⬛️", "⬜️", "⬜️"],
  ["⬜️", "⬛️", "⬜️", "⬜️", "⬜️", "⬛️"],
  ["⬜️", "⬛️", "⬜️", "⬛️", "⬜️", "⬛️"],
  ["⬜️", "⬜️", "⬜️", "⬛️", "⬜️", "⬜️"],
  ["⬜️", "⬛️", "⬜️", "⬜️", "⬛️", "⬜️"],
  ["⬜️", "⬜️", "⬛️", "⬜️", "⬛️", "🚪"],
];

const moves = "Arriba, Abajo, Izquierda, Derecha";
let columnPosition = "";
let rowPosition = "";

function mickeyPosition() {
  for (let column = 0; column < maze.length; column++) {
    for (let row = 0; row < maze[column].length; row++) {
      if (maze[column][row] == "🐭") {
        columnPosition = column;
        rowPosition = row;
      }
    }
  }
}

function moveTop() {
  mickeyPosition();

  if (columnPosition - 1 < 0 || maze[columnPosition - 1][rowPosition].includes("⬛️")) {
    alert("No puedes ir hacia arriba. Hay un obstáculo.");
  } else {
    maze[columnPosition][rowPosition] = "⬜️";

    if (maze[columnPosition - 1][rowPosition].includes("🚪")) {
      alert("¡Mickey encontró la salida!");
    } else {
      maze[columnPosition - 1][rowPosition] = "🐭";
    }
  }

  console.table(maze);
}

function moveDown() {
  mickeyPosition();

  if (columnPosition + 1 === maze.length || maze[columnPosition + 1][rowPosition].includes("⬛️")) {
    alert("No puedes ir hacia abajo. Hay un obstáculo.");
  } else {
    maze[columnPosition][rowPosition] = "⬜️";

    if (maze[columnPosition + 1][rowPosition].includes("🚪")) {
      alert("¡Mickey encontró la salida!");
    } else {
      maze[columnPosition + 1][rowPosition] = "🐭";
    }
  }

  console.table(maze);
}

function moveLeft() {
  mickeyPosition();

  if (maze[columnPosition][rowPosition - 1] === undefined || maze[columnPosition][rowPosition - 1].includes("⬛️")) {
    alert("No puedes ir a la izquierda. Hay un obstáculo.");
  } else {
    maze[columnPosition][rowPosition] = "⬜️";

    if (maze[columnPosition][rowPosition - 1].includes("🚪")) {
      alert("¡Mickey encontró la salida!");
    } else {
      maze[columnPosition][rowPosition - 1] = "🐭";
    }
  }

  console.table(maze);
}

function moveRight() {
  mickeyPosition();

  if (maze[columnPosition][rowPosition + 1] === undefined ||  maze[columnPosition][rowPosition + 1].includes("⬛️")) {
    alert("No puedes ir a la derecha. Hay un obstáculo.");
  } else {
    maze[columnPosition][rowPosition] = "⬜️";

    if (maze[columnPosition][rowPosition + 1].includes("🚪")) {
      alert("¡Mickey encontró la salida!");
    } else {
      maze[columnPosition][rowPosition + 1] = "🐭";
    }
  }

  console.table(maze);
}

do {
  const userInteraction = prompt(moves);

  switch (userInteraction) {
    case "Arriba":
      moveTop();
      break;

    case "Abajo":
      moveDown();
      break;

    case "Izquierda":
      moveLeft();
      break;

    case "Derecha":
      moveRight();
      break;

    default:
      alert("Por favor, ingresa una opción válida.");
      break;
  }
} while (maze.find((mickey) => mickey.includes("🐭")) !== undefined);
