import readline from "readline"

const colors = {
  red: "\x1b[31m",
  green: "\x1b[32m",
  yellow: "\x1b[33m",
  cyan: "\x1b[34m",
  reset: "\x1b[0m",
}

class Asks {
  constructor() {
    this.readline = readline.createInterface({
      input: process.stdin,
      output: process.stdout
    })
  }

  #ask(question) {
    return new Promise(resolve => {
      this.readline.question(question, (answer) => resolve(answer))
    })
  }

  close() {
    this.readline.close()
  }

  async askLabel(label) {
    const response = await this.#ask(colors.cyan + `Enter the ${label}: ` + colors.reset)
    return response
  }
}

class Renderer {
  static error(message) {
    console.log(colors.red + "Error: " + message + colors.reset)
  }

  static success(message) {
    console.log(colors.green + "Success: " + message + colors.reset)
  }

  static info(ringSauron, ringsElfs, ringsDwarf, ringsHumans) {
    console.log(colors.yellow + 
                `\nSauron: ${ringSauron}`+ 
                `\nElfs: ${ringsElfs}`+ 
                `\nDwarfs: ${ringsDwarf}`+ 
                `\nHumans: ${ringsHumans}` + colors.reset)
  }
}

const asks = new Asks()

class DistributionRings {
  constructor() {
    this.ringsElfs
    this.ringsHumans
    this.ringsDwarf
    this.ringSauron
    this.rings
  }

  assingRings(num) {
    this.rings = num
  }

  assingOneSauron(){
    this.rings--
    this.ringSauron = 1
  }

  assingPrimeNumberDwarf(){
    let dividing = Math.floor(Math.sqrt(this.rings))

    while (dividing > 1) {
      if (this.rings % dividing === 0) return false
      dividing--
    }

    this.ringsDwarf = this.rings
    this.rings -= this.ringsDwarf
    return true
  }

  assingOddNumberElfs(){
    let num = Math.floor(Math.random() * (this.rings - 4) + 1)

    if (num % 2 === 0) num--

    this.ringsElfs = num
    this.rings -= this.ringsElfs
  }

  assingEvenNumberHumans() {
    let num = Math.floor(Math.random() * (this.rings - 4) + 2)

    if (num % 2 !== 0) num--

    this.ringsHumans = num
    this.rings -= this.ringsHumans
  }

  startDistribution() {
    if (Math.random() > 0.5) {
      this.assingEvenNumberHumans()
      this.assingOddNumberElfs()
    } else {
      this.assingOddNumberElfs()
      this.assingEvenNumberHumans()
    }
    this.checkDistribution()
  }

  checkDistribution() {
    while (this.rings !== 0) {
      if (this.rings % 2 === 0){
        this.ringsDwarf = 2

        if (Math.random() > 0.5) {
          this.ringsElfs += (this.rings - 2)
          this.rings = 0
        } else {
          this.ringsHumans += (this.rings - 2)
          this.rings = 0
        }
      } else if (!this.assingPrimeNumberDwarf()){
        if (Math.random() > 0.5) {
          this.ringsElfs += 2
          this.rings -= 2
        } else {
          this.ringsHumans += 2
          this.rings -= 2
        }
      }
    }
  }
}

class ControllerDistribution {
  constructor(distributionRings) {
    this.distributionRings = distributionRings
  }

  async start(){
    const rings = Number.parseInt(await asks.askLabel("number of rings"))

    if (!(rings >= 6)) {
      Renderer.error("The number of rings must be greater than or equal to 6")
      return this.start()
    }

    this.distributionRings.rings = rings

    this.distributionRings.assingOneSauron()

    this.distributionRings.startDistribution()

    Renderer.success("The rings have been distributed correctly")
    Renderer.info(this.distributionRings.ringSauron, this.distributionRings.ringsElfs, this.distributionRings.ringsDwarf, this.distributionRings.ringsHumans)
    asks.close()
  }
}

const controllerDistribution = new ControllerDistribution(new DistributionRings)
controllerDistribution.start()