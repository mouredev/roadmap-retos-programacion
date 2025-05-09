const readline = require("readline") // importamos para poder pedir al usuario inputs a través de la terminal.

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
})

/* 
    Creado por Rafa Canosa
    Github: https://github.com/Rafacv23
    Website: https://www.rafacanosa.dev
*/

// Creamos el tabler de juego de 6x6

const board = [
  ["⬜", "⬜", "⬛", "⬜", "⬜", "⬜"],
  ["⬛", "⬜", "⬜", "⬜", "⬛", "⬜"],
  ["⬛", "⬛", "⬛", "⬛", "⬛", "⬜"],
  ["⬜", "⬜", "🚪", "⬛", "⬛", "⬜"],
  ["⬜", "⬛", "⬛", "⬛", "⬜", "⬜"],
  ["⬜", "⬜", "⬜", "⬜", "⬜", "⬛"],
]

let position = { x: 0, y: 0 } // posicion del jugador, la posicion inicial siempre es 0,0

// funcion encargada de pintar el tablero
function showLabyrinth() {
  console.clear() // limpiamos la consola antes de pintar el tablero

  console.log(
    `Utiliza las teclas WASD para elegir la dirección a la que quieres moverte y después pulsa ENTER para confirmar. Presiona Crtl+C para salir del juego.`
  )

  for (let y = 0; y < board.length; y++) {
    let row = ""
    for (let x = 0; x < board[y].length; x++) {
      if (x === position.x && y === position.y) {
        row += "🐭" // representa al jugador
      } else {
        row += board[y][x]
      }
    }
    console.log(row)
  }
}

// función encargada de mover al jugador a través del tablero y de verificar si se ha ganado.
function movePlayer(dir) {
  const newPosition = { ...position }

  if (dir === "w") newPosition.y -= 1 // arriba
  if (dir === "s") newPosition.y += 1 // abajo
  if (dir === "a") newPosition.x -= 1 // izquierda
  if (dir === "d") newPosition.x += 1 // derecha

  // Verificar que la nueva posición esté dentro de los límites del tablero
  if (
    newPosition.x >= 0 &&
    newPosition.x < board[0].length &&
    newPosition.y >= 0 &&
    newPosition.y < board.length
  ) {
    // Verificar si la nueva posición es un muro
    if (board[newPosition.y][newPosition.x] === "⬛") {
      console.log(
        `Mickey 🐭 se ha chocado contra un muro ⬛, prueba a moverte en otra dirección.`
      )
    } else {
      // Solo si la nueva posición no es un muro, actualiza la posición del jugador
      position = newPosition
    }
  } else {
    console.log(
      `Mickey 🐭 no puede salir del tablero, prueba a moverte en otra dirección.`
    )
  }

  if (board[position.y][position.x] === "🚪") {
    console.log("Has ganado, Mickey 🐭 ha salido del laberinto.")
    rl.close()
    process.exit(0)
  }

  showLabyrinth()
}

showLabyrinth()

rl.on("line", (input) => {
  movePlayer(input)
})
