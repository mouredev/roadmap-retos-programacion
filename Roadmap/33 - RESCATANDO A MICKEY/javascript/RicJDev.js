/*
  EJERCICIO:

- Se ejecuta en Node.js, importando el módulo 'Readline/promises' (https://nodejs.org/api/readline.html)

  @RicJDev
*/

const maze = [
  [0, 1, 1, 1, 0, 1],
  [0, 1, 0, 1, 0, 1],
  [0, 1, 0, 0, 0, 0],
  [0, 0, 1, 0, 1, 0],
  [1, 0, 0, 0, 1, 0],
  [1, 1, 0, 1, 1, 1],
]

const mickey = {
  y: 5,
  x: 2,
}

const door = {
  y: 0,
  x: 4,
}

function drawMaze() {
  maze[door.y][door.x] = 5
  maze[mickey.y][mickey.x] = 6

  const items = new Map([
    [0, '⬛️'],
    [1, '⬜️'],
    [5, '🚪'],
    [6, '🐭'],
  ])

  maze.forEach((row) => {
    let item
    let rowString = ''

    row.forEach((cell) => {
      item = items.get(cell) || items.get(0)
      rowString += item
    })

    console.log(rowString)
  })
}

function moveMickey(y, x) {
  let newY = mickey.y + y
  let newX = mickey.x + x

  if (maze[newY] && maze[newY][newX] !== 1 && maze[newY][newX] !== undefined) {
    maze[mickey.y][mickey.x] = 0

    mickey.y = newY
    mickey.x = newX
  }
}

import * as readline from 'readline/promises'
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
})

let invalid = false
let message = '\nMueve a Mickey! '

while (true) {
  console.clear()
  console.log('\nAYUDA A MICKEY A ESCAPAR!\n')

  drawMaze()

  if (mickey.y === door.y && mickey.x === door.x) {
    console.log('\nHas liberado a Mickey! Prepárate para una demanda por copyright!\n')

    rl.close()
    break
  }

  if (invalid) {
    message = '\nOpcion no valida. '
    invalid = false
  }

  const actions = new Map([
    ['1', () => moveMickey(-1, 0)],
    ['2', () => moveMickey(1, 0)],
    ['3', () => moveMickey(0, -1)],
    ['4', () => moveMickey(0, 1)],
  ])

  console.log('\n(1) Arriba. (2) Abajo. (3) Izquierda. (4) Derecha.\n(x) Salir')
  let answer = await rl.question(message)

  message = '\nMueve a Mickey! '

  if (answer === 'x') {
    console.log('\nSaliendo del programa...')

    rl.close()
    break
  }

  const action =
    actions.get(answer) ||
    function () {
      invalid = true
    }

  action()
}
