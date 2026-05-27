import readline from "readline";

const colors = {
  red: "\x1b[31m",
  green: "\x1b[32m",
  yellow: "\x1b[33m",
  cyan: "\x1b[34m",
  reset: "\x1b[0m",
}

class Asks {
  constructor() {
    this.rl = readline.createInterface({
      input: process.stdin,
      output: process.stdout,
    });
  }

  ask(question) {
    return new Promise((resolve) => {
      this.rl.question(question, (answer) => resolve(answer));
    });
  }

  close() {
    this.rl.close();
  }
}

const asks = new Asks()

function createPath() {
  let start = [Math.round(Math.random() * 5), 0]
  let visited = [start]
  const path = new Set([`${start[0]},${start[1]}`])
  let resetLimit = 40

  while (visited[visited.length - 1][1] !== 5 && resetLimit > 0) {
    const MOVES = [
      [1, 0],
      [-1, 0],
      [0, 1],
      [0, -1]
    ]

    const [y, x] = visited[visited.length - 1]

    const move = MOVES[Math.floor(Math.random() * 4)]

    const nx = x + move[1]
    const ny = y + move[0]

    const newMove = `${ny},${nx}`;

    const isInside = ny >= 0 && ny < 6 && nx >= 0 && nx < 6;

    if (isInside && !path.has(newMove)) {
      visited.push([ny, nx])
      path.add(newMove)
    }

    resetLimit--
  }

  if (resetLimit === 0) {
    console.log(colors.yellow + 'Resetting path creation...' + colors.reset)
    return createPath()
  }
  return path
}

function createMaze(path) {
  const maze = []
  let row = []

  for (let i = 0, j = 0; i < 6; j++) {
    if (path.has(`${i},${j}`)) {
      row.push(0)
    }
    else row.push(1)

    if (j === 5) {
      maze.push(row)
      i++
      j = -1
      row = []
    }
  }

  return maze
}

function prettyMaze(maze, mickey) {
  return new Promise((resolve) => {
    const viewMaze = maze.map((column, indexRow) => {
      return column.map((cell, indexColumn) => {
        if (indexRow === mickey[0] && indexColumn === mickey[1]) {
          return '🐭'
        }
        else if (cell === 0) {
          if (indexColumn === 5) return '🚪'
          else return '⬜️'
        }
        else if (cell === 1) {
          return '⬛️'
        }
      })
    })

    console.log(viewMaze.join('\n').replaceAll(',', ' '))
  resolve()
  })
}

function checkMove({ move, mickey, maze }) {
  let [y, x] = mickey

  if (move === 'w' && y > 0 && maze[y-1][x] === 0) return [y-1, x]
  if (move === 's' && y < 5 && maze[y+1][x] === 0) return [y+1, x]
  if (move === 'a' && x > 0 && maze[y][x-1] === 0) return [y, x-1]
  if (move === 'd' && x < 5 && maze[y][x+1] === 0) return [y, x+1]

  console.log(colors.red + "Invalid move!" + colors.reset)
  return mickey
}

function checkWin(mickey) {
  if (mickey[1] === 5) {
    console.log(colors.green + '\n🎉🎊 YOU WIN! Mickey has been rescued! 🎊🎉' + colors.reset)
  }
}

async function start() {
  const maze = createMaze(createPath())

  const startPosition = [maze.findIndex(row => row[0] === 0), 0]
  let mickey = startPosition

  while (mickey[1] !== 5) {
    console.log(colors.cyan + '\nCurrent Maze:' + colors.reset)

    await prettyMaze(maze, mickey)

    const move = (await asks.ask(colors.cyan + '\nEnter your move (w/a/s/d): ' + colors.reset)).toLowerCase()

    mickey = checkMove({ move, mickey, maze })

    checkWin(mickey)
  }

  asks.close()
}

start()
