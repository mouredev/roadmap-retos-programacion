const readline = require('node:readline')
const { stdin: input, stdout: output } = require('node:process')
const rl = readline.createInterface({ input, output })

const WALL = '⬛️'
const PATH = '⬜️'
const MOUSE = '🐭'
const END = '🚪'

const maze = [
  [MOUSE, WALL, WALL, WALL, PATH, WALL],
  [PATH, PATH, PATH, PATH, PATH, WALL],
  [WALL, PATH, PATH, WALL, PATH, WALL],
  [PATH, WALL, PATH, WALL, WALL, WALL],
  [PATH, PATH, PATH, PATH, PATH, PATH],
  [PATH, WALL, WALL, PATH, WALL, END],
]

function printMaze(maze) {
  maze.forEach(row => {
    console.log(row.join(' '))
  })
}

function findMouse() {
  let position = undefined
  for (let row = 0; row < maze.length; row++) {
    const col = maze[row].findIndex(value => value === MOUSE)
    if (col !== -1) {
      position = { row, col }
      break
    }
  }
  return position
}

function moveToRight(mousePosition) {
  const row = mousePosition.row
  const col = mousePosition.col

  if (col + 1 >= maze[row].length || maze[row][col + 1] === WALL) {
    console.log('No se puede mover a la derecha: fuera de los límites o hay un muro')
    return false
  }

  if (maze[row][col + 1] === END) {
    console.log('¡Has llegado al final!')
    return true
  }

  maze[row][col] = PATH
  maze[row][col + 1] = MOUSE
  mousePosition.col++
  console.log('Ratón movido a la derecha')
  return false
}

function moveToLeft(mousePosition) {
  const row = mousePosition.row
  const col = mousePosition.col

  if (col - 1 < 0 || maze[row][col - 1] === WALL) {
    console.log('No se puede mover a la izquierda: fuera de los límites o hay un muro')
    return false
  }

  maze[row][col] = PATH
  maze[row][col - 1] = MOUSE
  mousePosition.col--
  console.log('Ratón movido a la izquierda')
  return false
}

function moveToDown(mousePosition) {
  const row = mousePosition.row
  const col = mousePosition.col

  if (row + 1 >= maze.length || maze[row + 1][col] === WALL) {
    console.log('No se puede mover hacia abajo: fuera de los límites o hay un muro')
    return false
  }

  if (maze[row + 1][col] === END) {
    console.log('¡Has llegado al final!')
    return true
  }

  maze[row][col] = PATH
  maze[row + 1][col] = MOUSE
  mousePosition.row++
  console.log('Ratón movido hacia abajo')
  return false
}

function moveToUp(mousePosition) {
  const row = mousePosition.row
  const col = mousePosition.col

  if (row - 1 < 0 || maze[row - 1][col] === WALL) {
    console.log('No se puede mover hacia arriba: fuera de los límites o hay un muro')
    return false
  }

  maze[row][col] = PATH
  maze[row - 1][col] = MOUSE
  mousePosition.row--
  console.log('Ratón movido hacia arriba')
  return false
}

let mousePosition = findMouse()

function program() {
  printMaze(maze)
  console.log('1. mover arriba')
  console.log('2. mover abajo')
  console.log('3. mover izquierda')
  console.log('4. mover derecha')
  console.log('0. salir')

  rl.question('Ingresa una opción: ', (answer) => {
    let isEnd = false
    switch (answer) {
      case '1':
        isEnd = moveToUp(mousePosition)
        break
      case '2':
        isEnd = moveToDown(mousePosition)
        break
      case '3':
        isEnd = moveToLeft(mousePosition)
        break
      case '4':
        isEnd = moveToRight(mousePosition)
        break
      case '0':
        rl.close()
        return
      default:
        console.log('Opción inválida')
        program()
        return
    }

    if (isEnd) {
      rl.close()
    } else {
      program()
    }
  })
}

program()