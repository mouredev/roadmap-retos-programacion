import  fs  from "fs"

const colors = {
  red: "\x1b[31m",
  green: "\x1b[32m",
  yellow: "\x1b[33m",
  cyan: "\x1b[34m",
  reset: "\x1b[0m",
}

class Renderer {
  static error(message) {
    console.log(colors.red + "Error: " + message + colors.reset)
  }

  static success(message) {
    console.log(colors.green + "Success: " + message + colors.reset)
  }

  static info(info) {
    console.log(info + colors.reset)
  }
}

function getUsers(csv) {
  const usersActives = (csv.split('\r\n')).map(arr => arr.split(',')).filter(arr => arr[2] === 'activo')

  const visited = new Set()

  const users = [...usersActives.filter(user => {
      if (!visited.has(user[0]) || !visited.has(user[1])) {
        visited.add(user[0])
        visited.add(user[1])
        return true
      } else {
        return false
      }
    })]

  return users
}

function printWinners(winners) {
  Renderer.info(colors.yellow + "The winner of a subscription is:")
  Renderer.info(colors.green + `   Email --> ${winners[0][1]}` + 
                    `\n   ID --> ${winners[0][0]}`)

  Renderer.info(colors.yellow + "\nThe winner of a discount is:")
  Renderer.info(colors.green + `   Email --> ${winners[1][1]}` + 
                    `\n   ID --> ${winners[1][0]}`)

  Renderer.info(colors.yellow + "\nThe winner of a book is:")
  Renderer.info(colors.green + `   Email --> ${winners[2][1]}` + 
                    `\n   ID --> ${winners[2][0]}`)
}

function program() {
  const csv = fs.readFileSync('text.csv', 'utf-8')

  const users = getUsers(csv)
  let winners = []

  if (users.length >= 3) {
    for (let i = 0; i < 3; i++) {
      winners.push(users[Math.floor(Math.random() * users.length)])
    }

    printWinners(winners)

  } else Renderer.error("There are not enough active users to hold the draw")
}

program()