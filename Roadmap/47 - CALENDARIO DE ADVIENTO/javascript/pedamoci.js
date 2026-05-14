import readline from "readline";

const COLUMNS = 6
const ROWS = 12
const MSG_ADVENT_DEV = {
  1: "Like the first day of Advent, every project begins with a single line of code.",
  2: "Patience in debugging mirrors the waiting spirit of Advent.",
  3: "Each function is a small gift, wrapped in logic and purpose.",
  4: "Refactoring code is like preparing your heart—making space for something better.",
  5: "Advent teaches us that good things take time, just like clean code.",
  6: "Every bug fixed is a light shining in the darkness of errors.",
  7: "Code reviews remind us that collaboration makes everything stronger.",
  8: "Writing tests is like lighting candles—bringing clarity step by step.",
  9: "A well-structured program reflects the harmony we seek during Advent.",
  10: "Learning new frameworks is a journey of growth, just like the Advent season.",
  11: "Small commits lead to meaningful progress, one day at a time.",
  12: "Debugging requires faith that a solution is always near.",
  13: "Consistency in coding mirrors the steady anticipation of Advent.",
  14: "Each algorithm solves a problem, just like each day brings new hope.",
  15: "Clean code is a gift to your future self.",
  16: "Version control helps us remember where we started and how far we’ve come.",
  17: "Every deploy is a step closer to something complete.",
  18: "Programming teaches us to embrace challenges with patience.",
  19: "Like Advent, coding is about preparation before the big release.",
  20: "Errors guide us toward better solutions, just like reflection guides growth.",
  21: "A good developer writes code that others can understand and build upon.",
  22: "Each day of coding adds a new piece to the final creation.",
  23: "Optimization is the art of making things better with care and intention.",
  24: "The final build is like Christmas Day—a moment to celebrate what you've created."
};

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
})

const ask = q => new Promise(r => rl.question(q,r))

const sleep = ms => new Promise(r => setTimeout(r, ms))

class Renderer {
  static error(msg) {
    console.error(`\nError: ${msg}\n`)
  }

  static gift(day) {
    console.log(`\nYou discovered on the day ${day}\n${MSG_ADVENT_DEV[day]}\n`)
  }

  static finish() {
    console.log("Congratulations! You've completed the Advent calendar")
  }
}

const createAdventCalendar = () => {
  const adventCalendar = []
  let row = []

  for (let day = 1, r = 0, c = 1; r < ROWS; c++) {
    if (r % 3 === 1) {
      row.push(`*${String(day).padStart(2, "0")}*`)
      day++
    } else {
      row.push("****")
    }

    if (c % COLUMNS === 0) {
      adventCalendar.push(row)
      row = []
      r++
    }
  }

  return adventCalendar
}

const printAdventCalendar = adventCalendar => {
  for (const row of adventCalendar) {
    console.log(row.join(" "))
  }
}

const discoverDay = (day, adventCalendar) => {
  const rowIndex = Math.floor((day - 1) / COLUMNS) * 3 + 1
  const colIndex = (day - 1) % COLUMNS

  adventCalendar[rowIndex][colIndex] = "****"
}

async function main() {
  const adventCalendar = createAdventCalendar()
  const discoveredDays = new Set()
  do {
    printAdventCalendar(adventCalendar)
    try {
      const day = Number(await ask("Enter the day you want to discover: "))
  
      if (Number.isNaN(day) || day < 1 || day > 24 || !Number.isInteger(day)) throw new Error("The day must be an integer between 1 and 24\n")
      if (discoveredDays.has(day)) throw new Error("You've already discovered that day\n")
  
      discoverDay(day, adventCalendar)
  
      discoveredDays.add(day)
  
      Renderer.gift(day)
      await sleep(2000)

    } catch (e) {
      Renderer.error(e.message)
      await sleep(1000)
    }
  } while (discoveredDays.size < 24)

  Renderer.finish()

  rl.close()
}

main()