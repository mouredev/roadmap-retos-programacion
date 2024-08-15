const maze = [
  [1, 0, 1, 1, 2, 1],
  [0, 0, 0, 1, 0, 1],
  [1, 1, 0, 0, 0, 0],
  [1, 0, 1, 0, 1, 0],
  [1, 0, 0, 0, 1, 0],
  [1, 1, 0, 1, 1, 1],
]

const mickey = {
  y: 5,
  x: 2,
}

function drawMaze() {
  const items = new Map([
    [0, '⬛️'],
    [1, '⬜️'],
    [2, '🚪'],
    [5, '🐭'],
  ])

  maze[mickey.y][mickey.x] = 5

  maze.map((row) => {
    let item
    let rowString = ''

    row.map((cell) => {
      item = items.get(cell) || items.get(0)
      rowString += item
    })

    console.log(rowString)
  })
}

function canMove(newY, newX) {
  return maze[newY] && maze[newY][newX] !== 1
}

function moveUp() {
  if (canMove(mickey.y - 1, mickey.x)) {
    maze[mickey.y][mickey.x] = 0
    mickey.y--
  }
}
function moveDown() {
  if (canMove(mickey.y + 1, mickey.x)) {
    maze[mickey.y][mickey.x] = 0
    mickey.y++
  }
}
function moveLeft() {
  if (canMove(mickey.y, mickey.x - 1)) {
    maze[mickey.y][mickey.x] = 0
    mickey.x--
  }
}
function moveRight() {
  if (canMove(mickey.y, mickey.x + 1)) {
    maze[mickey.y][mickey.x] = 0

    mickey.x++
  }
}

import * as readline from 'readline/promises'
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
})

while (true) {
  console.clear()
  console.log('\nAYUDA A MICKEY A ESCAPAR!\n')

  drawMaze()

  const actions = new Map([
    ['1', moveUp],
    ['2', moveDown],
    ['3', moveLeft],
    ['4', moveRight],
  ])

  console.log('\n(1) Arriba. (2) Abajo. (3) Izquierda. (4) Derecha.\n(x) Salir')

  let answer = await rl.question('\nMueve a Mickey! ')

  if (answer === 'x') {
    console.log('\nSaliendo del programa...')

    rl.close()
    break
  }

  const action =
    actions.get(answer.toLowerCase()) ||
    function () {
      console.log('Opcion no valida')
    }

  action()
}
