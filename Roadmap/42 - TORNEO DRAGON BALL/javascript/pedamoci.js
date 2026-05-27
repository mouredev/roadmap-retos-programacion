import readline from "readline"

const EVADE_CHANCE = 0.2
const REDUCTOR_DAMAGE_FACTOR = 0.1

const COLORS = Object.freeze({
  red: "\x1b[31m",
  green: "\x1b[32m",
  yellow: "\x1b[33m",
  cyan: "\x1b[34m",
  purple: "\x1b[35m",
  reset: "\x1b[0m",
})

const INITIAL_FIGHTERS = [
  {name : "Goku", stats: {health: 100, attack: 94, defense: 92, speed: 95}},
  {name : "Vegeta", stats: {health: 100, attack: 97, defense: 90, speed: 95}},
  {name : "Gohan", stats: {health: 100, attack: 91, defense: 88, speed: 88}},
  {name : "Piccolo", stats: {health: 100, attack: 84, defense: 89, speed: 85}},
  {name : "Freezer", stats: {health: 100, attack: 94, defense: 85, speed: 92}},
  {name : "Cell", stats: {health: 100, attack: 90, defense: 91, speed: 88}},
  {name : "Majin Buu", stats: {health: 100, attack: 92, defense: 99, speed: 80}},
  {name : "Trunks of the Future", stats: {health: 100, attack: 89, defense: 85, speed: 88}},
  {name : "Android 18", stats: {health: 100, attack: 81, defense: 86, speed: 80}},
  {name : "Broly", stats: {health: 100, attack: 100, defense: 95, speed: 85}},
  {name : "Jiren", stats: {health: 100, attack: 99, defense: 96, speed: 98}},
  {name : "Hit", stats: {health: 100, attack: 90, defense: 80, speed: 98}},
  {name : "Krillin", stats: {health: 100, attack: 70, defense: 65, speed: 75}},
  {name : "Ten Shin Han", stats: {health: 100, attack: 72, defense: 68, speed: 75}},
  {name : "Black Goku", stats: {health: 100, attack: 93, defense: 87, speed: 92}}
]

function delay(ms) {
  return new Promise(resolve => {
    setTimeout(() => {
      resolve()
    }, ms);
  })
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

  async askLabel() {
    const response = await this.#ask(COLORS.cyan + `Would you like to add a fighter?` + '\n' + "(Y/N): " + COLORS.reset)
    return response
  }
}

const asks = new Asks()

class Renderer {
  static error(message) {
    console.log(COLORS.red + "Error: " + message + COLORS.reset)
  }

  static success(message) {
    console.log(COLORS.green + "Success: " + message + COLORS.reset)
  }

  static info(message) {
    console.log(COLORS.purple + message + COLORS.reset)
  }

  static evade(name) {
    console.log(`${COLORS.green}${name} evaded the attack${COLORS.reset}`)
  }

  static damage(name, damage) {
    console.log(`🗡️   ${name} inflicted ${damage} points of damage`)
  }

  static round(num) {
    console.log(COLORS.cyan + `--- Round ${num} ---` + COLORS.reset)
  }

  static status(fighterOneName, fighterOneHealth, fighterTwoName, fighterTwoHealth) {
    console.log(`❤️   ${COLORS.red}${fighterOneName} health: ${fighterOneHealth}` + '\n' +
                `❤️   ${fighterTwoName} health: ${fighterTwoHealth}${COLORS.reset}` + '\n')
  }

  static winFight(fighterName) {
    console.log(COLORS.yellow + `WINNER ${fighterName}` + '\n' + COLORS.reset)
  }

  static winTournament(fighterName) {
    console.log(COLORS.green + `The winner of the torunament is ${fighterName}` + COLORS.reset)
  }
}

class Validator {
  isExistingFighter(name, fighters) {
    return fighters.some(fighter => fighter.name.toLowerCase() === name.toLowerCase())
  }

  isValidAttribute(attribute) {
    if (typeof attribute !== "number" || attribute < 0 || attribute > 100) {
      return false
    }

    return true
  }

  isValidName(name) {
    if (typeof name !== "string") {
      return false
    }

    return true
  }

  isValidFighter(name, attack, defense, speed, fighters) {
    if (!this.isValidAttribute(attack)) {
      const msg = "The fighter's attack must be a number between 0 and 100"
      return {
        valid: false,
        message: msg
      }
    }

    if (!this.isValidAttribute(defense)) {
      const msg = "The fighter's defense must be a number between 0 and 100"
      return {
        valid: false,
        message: msg
      }
    }

    if (!this.isValidAttribute(speed)) {
      const msg = "The fighter's speed must be a number between 0 and 100"
      return {
        valid: false,
        message: msg
      }
    }

    if (!this.isValidName(name)) {
      const msg = "The fighter's name must be a string"
      return {
        valid: false,
        message: msg
      }
    }

    if (this.isExistingFighter(name, fighters)) {
      const msg = "Fighter already added to the tournament"
      return {
        valid: false,
        message: msg
      }
    }

    const msg = "The fighter was added"
    return {
      valid: true,
      message: msg
    } 
  }

  isValidNumberOfFighters(fighters) {
    const num = fighters.length

    if (num <= 1 || (num & (num - 1)) !== 0) {
      const msg = `the tournament can't start with ${num} participants`
      return {
        valid: false,
        message: msg
      }
    }
    return {
      valid: true
    }
  }
}

class FightController {
  calculateDamage(attack, defense) {
    if (defense >= attack) {
      let dmg = Math.round(attack * REDUCTOR_DAMAGE_FACTOR)
      return dmg
    }

    return (attack - defense)
  }

  evade() {
    return (Math.random() < EVADE_CHANCE)
  }

  checkFighterStart(fighterOne, fighterTwo){
    if (fighterOne.stats.speed > fighterTwo.stats.speed){
      return [fighterOne, fighterTwo]
    } else if (fighterOne.stats.speed < fighterTwo.stats.speed){
      return [fighterTwo, fighterOne]
    } else if (Math.random() > 0.5) {
      return [fighterOne, fighterTwo]
    } else {
      return [fighterTwo, fighterOne]
    }
  }

  async fight(fighterOne, fighterTwo) {
    let [attacker, defender] = this.checkFighterStart(fighterOne, fighterTwo)

    for (let i = 0; attacker.stats.health > 0 ; i++) {
      Renderer.round(i + 1)
      if (this.evade()) {
        Renderer.evade(defender.name)
      } else {
        const damage = this.calculateDamage(attacker.stats.attack, defender.stats.defense)
        defender.stats.health = Math.max(0, defender.stats.health - damage)
        Renderer.damage(attacker.name, damage)
      }

      (i % 2 === 0) ? Renderer.status(attacker.name, attacker.stats.health, defender.name, defender.stats.health)
                    : Renderer.status(defender.name, defender.stats.health, attacker.name, attacker.stats.health)

      await delay(500)

      if (defender.stats.health < 1) {
        attacker.stats.health = 100

        Renderer.winFight(attacker.name)

        await delay(1000)

        return defender.name
      } else {
        [attacker, defender] = [defender, attacker]
      }
    }
  }
}

class TournamentController {
  constructor(validator, fightController) {
    this.participants = [...INITIAL_FIGHTERS]
    this.validator = validator
    this.fightController = fightController
  }

  addParticipant() {
      const name = "Android 17"
      const attack = 88
      const defense = 92
      const speed = 92

      let result = this.validator.isValidFighter(name, attack, defense, speed, this.participants)

      if (!result.valid) {
        Renderer.error(result.msg)
        return
      }

      this.participants.push({name, stats: {health: 100, attack, defense, speed}})
      Renderer.success(result.msg)
      return 
  }

  getRandomFighter(fighters) {
    const index = Math.floor(Math.random() * fighters.length)
    const fighter = fighters[index]
    fighters.splice(index, 1)
    return fighter
  }

  async startTournament() {
    Renderer.info(`current number of participants in the tournament: ${this.participants.length}`)

    let response

    do {
      response = await asks.askLabel()

      if (response.toLowerCase() === "y") {
        this.addParticipant()
      }
    } while (response.toLowerCase() !== "n")

    let result = this.validator.isValidNumberOfFighters(this.participants)
    if (!result.valid) {
      Renderer.error(result.message)
      return this.startTournament()
    }

    while (this.participants.length > 1) {
      let fighters = [...this.participants]
      let rounds = fighters.length / 2

      for (let i = 0; i < rounds; i++) {
        const fighterOne = this.getRandomFighter(fighters)
        const fighterTwo = this.getRandomFighter(fighters)

        const loserName = await this.fightController.fight(fighterOne, fighterTwo)

        this.participants = this.participants.filter(fighter => fighter.name !== loserName)
      }

      if (this.participants.length > 1) {
        Renderer.info(`There are ${this.participants.length} fighters left in the tournament` + '\n')
      }

      await delay(1500)
    }

    Renderer.winTournament(this.participants[0].name)

    asks.close()
  }
}

const tournamentController = new TournamentController(new Validator(), new FightController())
tournamentController.startTournament()