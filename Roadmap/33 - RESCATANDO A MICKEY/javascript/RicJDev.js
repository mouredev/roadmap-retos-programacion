/*
  EJERCICIO:

- Se ejecuta en Node.js, importando el módulo 'Readline/promises' (https://nodejs.org/api/readline.html)

  @RicJDev
*/

//PARTE I: modelado del laberinto (estático) y las funciones para dibujar y mover al personaje.

const maze = [
  [0, 0, 0, 1, 0, 1],
  [0, 1, 1, 1, 0, 1],
  [0, 0, 0, 1, 0, 0],
  [1, 0, 1, 1, 1, 0],
  [0, 0, 0, 0, 1, 0],
  [0, 0, 1, 0, 0, 0],
]

const character = { y: 5, x: 0 }

const door = { y: 0, x: 4 }

function drawMaze() {
  maze[door.y][door.x] = 5
  maze[character.y][character.x] = 6

  const items = {
    0: '⬜️',
    1: '⬛️',
    5: '🚪',
    6: '🐭',
  }

  maze.forEach((row) => {
    let rowString = ''

    row.forEach((cell) => {
      rowString += items[cell] || items[0]
    })

    console.log(rowString)
  })
}

function moveCharacter(dy, dx) {
  let newY = character.y + dy
  let newX = character.x + dx

  if (maze[newY] && maze[newY][newX] !== 1 && maze[newY][newX] !== undefined) {
    maze[character.y][character.x] = 0

    character.x = newX
    character.y = newY
  }
}

const move = {
  up: () => moveCharacter(-1, 0),
  down: () => moveCharacter(1, 0),
  left: () => moveCharacter(0, -1),
  right: () => moveCharacter(0, 1),
}

function isGoal() {
  return character.y === door.y && character.x === door.x
}

//PARTE II: Implementación en terminal con manejo básico de entradas erróneas

import * as readline from 'readline/promises'
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
})

let invalid = false
let [message1, message2] = ['\nMueve a Mickey! ', '\nOpcion no valida. A dónde se mueve Mickey? ']

while (true) {
  console.clear()
  console.log('\nAYUDA A MICKEY A ESCAPAR!\n')

  drawMaze()

  if (isGoal()) {
    console.log('\nHas liberado a Mickey. ¡Prepárate para una demanda por copyright!\n')

    rl.close()
    break
  }

  let message

  if (invalid) {
    message = message2
    invalid = false
  } else {
    message = message1
  }

  console.log('\n(w) Arriba. (s) Abajo. (a) Izquierda. (d) Derecha.\n(x) Salir')
  let answer = await rl.question(message)

  if (answer === 'x') {
    console.log('\nSaliendo del programa...')

    rl.close()
    break
  }

  const movements = {
    w: move.up,
    s: move.down,
    a: move.left,
    d: move.right,
  }

  const action =
    movements[answer.toLowerCase()] ||
    function () {
      invalid = true
    }

  action()
}
