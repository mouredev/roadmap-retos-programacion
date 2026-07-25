/* -------------------------- RETO 1 -------------------------- */
function getBatmanDay(year) {
  const date = new Date(`September 1, ${year} 12:00:00`)

  const day = 21 - date.getDay()

  return day 
}

function celebrateBatmanDay() {
  let numberOfYearsCelebrated = 85
  let year = 2024

  while (numberOfYearsCelebrated <= 100) {
    const batmanDay = getBatmanDay(year)

    console.log(`In ${year}, Batman Day will be ${numberOfYearsCelebrated} years old and will be celebrated on September ${batmanDay}\n`)

    year++
    numberOfYearsCelebrated++
  }
}

celebrateBatmanDay()

/* -------------------------- RETO 2 -------------------------- */
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

class Creator {
  constructor() {
    this.map = []
    this.txt = ""
  }

  crateMap(dimensions) {
    for (let row = 0; row < dimensions; row++) {
      this.map.push([])
      for (let column = 0; column < dimensions; column++) {
        this.map[row].push(0)
      }
    }

    return this.map
  }

  createTXT(info) {
    this.txt += `Coordinates of the most threatened area: X = ${info.coords[0]}  Y = ${info.coords[1]}`
    this.txt += `\nSums of threats: ${info.threatValues.join(" + ")}`
    this.txt += `\nDistance from the Batcave to the center of the threat: ${info.coords[0] + info.coords[1]}`

    return this.txt
  }
}

class Sensors {
  constructor() {
    this.report = []
  }

  theartLevelReport(map) {
    const rows = map.length
    const columns = map[0].length

    for (let row = 0; row < rows; row++) {
      for (let column = 0; column < columns; column++) {
        this.report.push([column, row, Math.floor(Math.random() * 11)])
      }
      
    }

    return this.report
  }
}

class Analyzer {
  constructor() {
    this.greatestThreat = {threat: 0, threatValues: [], coords: [0, 0]}
  }

  analyzeThreatLevel(report, dimensions) {
    for (let row = 0; row < dimensions - 2; row++) {
      for (let column = 0; column < dimensions - 2; column++) {
        const levelThreat = (report[row * dimensions + column][2] + report[row * dimensions + column + 1][2] + report[row * dimensions + column + 2][2] +
                            report[(row + 1) * dimensions + column][2] + report[(row + 1) * dimensions + column + 1][2] + report[(row + 1) * dimensions + column + 2][2] +
                            report[(row + 2) * dimensions + column][2] + report[(row + 2) * dimensions + column + 1][2] + report[(row + 2) * dimensions + column + 2][2])

        if (levelThreat > this.greatestThreat.threat) {
          this.greatestThreat.threat = levelThreat
          this.greatestThreat.threatValues = [report[row * dimensions + column][2], report[row * dimensions + column + 1][2], report[row * dimensions + column + 2][2],
                                              report[(row + 1) * dimensions + column][2], report[(row + 1) * dimensions + column + 1][2], report[(row + 1) * dimensions + column + 2][2],
                                              report[(row + 2) * dimensions + column][2], report[(row + 2) * dimensions + column + 1][2], report[(row + 2) * dimensions + column + 2][2]]
          this.greatestThreat.coords = [column + 1, row + 1]
        }
      }
    }

    return this.greatestThreat
  }
}

class Controller {
  constructor(creator, sensors, analyzer) {
    this.creator = creator
    this.sensors =sensors
    this.analyzer = analyzer
    this.dimensions = 20
  }

  start() {
    const map = this.creator.crateMap(this.dimensions)

    const report = this.sensors.theartLevelReport(map)

    const greatestThreat = this.analyzer.analyzeThreatLevel(report, this.dimensions)

    const txt = this.creator.createTXT(greatestThreat)

    Renderer.info(colors.yellow + txt)

    if (greatestThreat.threat >= 20)
      Renderer.info(colors.red + `\nThe threat level is ${greatestThreat.threat}, activate security protocol`)
  }
}

const controller = new Controller(new Creator(), new Sensors(), new Analyzer())
controller.start()