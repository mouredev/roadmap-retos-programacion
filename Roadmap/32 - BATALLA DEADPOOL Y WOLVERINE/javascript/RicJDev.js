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
  constructor(name, hp, attackRange = { min: 0, max: 50 }, defenseRate) {
    this.name = name
    this.hp = this.validateHp(hp)

    this.attackRange = attackRange
    this.defenseRate = defenseRate

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
      message = `ataque efectivo! ${defender.name} ${pc.magenta(`-${damage} hp`)}`

      if (damage === attacker.attackRange.max) {
        message += pc.magenta(' [CRITICAL]')

        defender.canAttack = false
      }
    } else {
      message = `${defender.name} ha esquivado el ataque`
    }
  } else {
    message = `recibió un golpe crítico. No puede atacar`

    attacker.canAttack = true
  }

  console.log(`\nTurno de ${attacker.name}: ${message}\n`)
}

function simulateBattle(playerA, playerB) {
  let turn = true

  const battle = setInterval(() => {
    console.clear()

    console.log(pc.underline('\nBATALLA EN CURSO!'))
    display(playerA, playerB)

    if (turn) {
      simulateAttack(playerA, playerB)
    } else {
      simulateAttack(playerB, playerA)
    }

    turn = !turn

    if (playerA.hp === 0 || playerB.hp === 0) {
      clearInterval(battle)

      console.clear()

      console.log(pc.underline('BATALLA FINALIZADA!'))
      display(playerA, playerB)
      console.log(`\n${playerA.hp === 0 ? playerB.name : playerA.name} ha ganado!\n`)
    }
  }, 1100)
}

//Implementacion en terminal
async function main() {
  console.clear()
  console.log(pc.underline('\nBIENVENIDO AL SIMULADOR!\n'))

  //Deadpool
  let deadpoolHP = parseInt(await rl.question('Indique la cantidad de vida para Deadpool. '))
  const Deadpool = new Character(pc.red('Deadpool'), deadpoolHP, { min: 10, max: 100 }, 25)

  //Wolverine
  let wolverineHP = parseInt(await rl.question('Indique la cantidad de vida para Wolverine. '))
  const Wolverine = new Character(pc.yellow('Wolverine'), wolverineHP, { min: 10, max: 120 }, 20)

  console.log(pc.gray('Cargando...'))
  simulateBattle(Deadpool, Wolverine)

  rl.close()
}

main()
