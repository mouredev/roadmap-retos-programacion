/*
  EJERCICIO:

- Se ejecuta en Node.js, importando el modulo Readline/promises (https://nodejs.org/api/readline.html)
- Se ha instalado Picocolors, un libreria para colorear texto en terminal (https://www.npmjs.com/package/picocolors)

  @RicJDev
*/

import * as readline from 'node:readline/promises'
import pc from 'picocolors'

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
})

//Modelado de personajes
class Character {
  /**
   * @param {string} name
   * @param {number} hp
   * @param {number} defenseRate
   * @param {{ min: number, max: number, }} attackRange
   */

  constructor(name, hp, defenseRate, attackRange) {
    this.name = name
    this.hp = this.validateHp(hp)

    this.defenseRate = defenseRate
    this.attackRange = attackRange

    this.canAttack = true
  }

  validateHp(hp) {
    if (hp > 2000) {
      console.log(pc.gray('Se ha establecido en el máximo de 2000 hp.'))
      return 2000
    } else if (hp < 500 || isNaN(hp)) {
      console.log(pc.gray('Se ha establecido en el mínimo de 500 hp.'))
      return 500
    }

    return hp
  }

  attack() {
    if (!this.canAttack) return 0

    return Math.floor(
      Math.random() * (this.attackRange.max - this.attackRange.min + 1) + this.attackRange.min
    )
  }

  defense(damage) {
    if (Math.floor(Math.random() * 100 + 1) > 100 - this.defenseRate) return 0

    this.hp = Math.max(this.hp - damage, 0)

    return damage
  }

  get lifeBar() {
    if (this.hp === 0) {
      return '💀'
    }

    return pc.green('|'.repeat(Math.floor(this.hp / 25)))
  }
}

//Funciones del simulador
function display(playerA, playerB) {
  console.log(`\n${playerA.name} (${playerA.hp}):\n${playerA.lifeBar} `)
  console.log(`\n${playerB.name} (${playerB.hp}):\n${playerB.lifeBar} `)
}

function simulateAttack(attacker, defender) {
  let message

  if (attacker.canAttack) {
    let damage = defender.defense(attacker.attack())

    if (damage > 0) {
      message = `${attacker.name} ha golpeado a ${defender.name}! ${pc.magenta(`-${damage} hp`)}`

      if (damage === attacker.attackRange.max) {
        message = `Golpe crítico de ${attacker.name}! ${pc.magenta(`-${damage} hp`)}\n${
          defender.name
        } no atacará en el siguiente turno`

        defender.canAttack = false
      }
    } else {
      message = `${defender.name} ha esquivado el ataque de ${attacker.name}!`
    }
  } else {
    message = `${attacker.name} recibió un golpe crítico. No puede atacar`

    attacker.canAttack = true
  }

  console.log(' ')
  console.log(message)
  console.log(' ')
}

function simulateBattle(playerA, playerB) {
  let alternate = true
  let turn = 1

  const battle = setInterval(() => {
    console.clear()

    console.log('\nBATALLA EN CURSO!')
    console.log('Turno:', turn)
    turn++

    display(playerA, playerB)

    if (alternate) {
      simulateAttack(playerA, playerB)
    } else {
      simulateAttack(playerB, playerA)
    }

    alternate = !alternate

    if (playerA.hp === 0 || playerB.hp === 0) {
      clearInterval(battle)

      console.clear()

      console.log('BATALLA FINALIZADA!')
      display(playerA, playerB)
      console.log(`\n${playerA.hp === 0 ? playerB.name : playerA.name} ha ganado!\n`)
    }
  }, 1100)
}

//Implementacion en terminal
async function main() {
  console.clear()
  console.log('\nBIENVENIDO AL SIMULADOR!\n')

  //Deadpool
  let deadpoolHP = parseInt(await rl.question('Indique la cantidad de vida para Deadpool. '))
  const Deadpool = new Character(pc.red('Deadpool'), deadpoolHP, 25, { min: 10, max: 100 })

  //Wolverine
  let wolverineHP = parseInt(await rl.question('Indique la cantidad de vida para Wolverine. '))
  const Wolverine = new Character(pc.yellow('Wolverine'), wolverineHP, 20, { min: 10, max: 120 })

  console.log(pc.gray('Cargando...'))
  simulateBattle(Deadpool, Wolverine)

  rl.close()
}

main()
