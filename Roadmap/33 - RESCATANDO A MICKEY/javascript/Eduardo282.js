// Representación del laberinto
let laberinto = [
  ["⬜️", "⬜️", "⬛️", "⬜️", "⬛️", "⬜️"],
  ["⬛️", "⬛️", "⬛️", "⬜️", "⬛️", "⬜️"],
  ["⬜️", "⬜️", "⬜️", "⬜️", "⬛️", "⬜️"],
  ["⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬜️"],
  ["⬜️", "🐭", "⬜️", "⬛️", "⬜️", "⬜️"],
  ["⬜️", "⬛️", "⬜️", "⬛️", "⬜️", "🚪"],
];

// Posición inicial de Mickey
let posicionMickey = { x: 4, y: 1 };

// Función para mostrar el laberinto
function mostrarLaberinto() {
  laberinto.forEach((fila) => console.log(fila.join(" ")));
  console.log();
}

// Función para mover a Mickey
function moverMickey(direccion) {
  let { x, y } = posicionMickey;
  let nuevaPosicion;

  switch (direccion) {
    case "arriba":
      nuevaPosicion = { x: x - 1, y: y };
      break;
    case "abajo":
      nuevaPosicion = { x: x + 1, y: y };
      break;
    case "izquierda":
      nuevaPosicion = { x: x, y: y - 1 };
      break;
    case "derecha":
      nuevaPosicion = { x: x, y: y + 1 };
      break;
    default:
      console.log(
        "Dirección no válida. Usa 'arriba', 'abajo', 'izquierda' o 'derecha'."
      );
      return false;
  }

  let { x: nx, y: ny } = nuevaPosicion;

  // Validar límites y obstáculos
  if (nx < 0 || nx >= 6 || ny < 0 || ny >= 6) {
    console.log("¡No puedes salir del laberinto!");
    return false;
  } else if (laberinto[nx][ny] === "⬛️") {
    console.log("¡Cuidado! Hay un obstáculo.");
    return false;
  } else if (laberinto[nx][ny] === "🚪") {
    console.log("¡Felicidades! ¡Mickey ha encontrado la salida!");
    return true;
  } else {
    // Actualizar la posición de Mickey en el laberinto
    laberinto[x][y] = "⬜️";
    laberinto[nx][ny] = "🐭";
    posicionMickey = { x: nx, y: ny };
    return false;
  }
}

// Ciclo principal del juego
function jugar() {
  while (true) {
    mostrarLaberinto();
    let direccion = prompt(
      "¿Hacia dónde debería ir Mickey? (arriba, abajo, izquierda, derecha):"
    ).toLowerCase();
    if (moverMickey(direccion)) {
      break;
    }
  }
  console.log("¡Juego terminado!");
}

// Ejecutar el juego
jugar();
