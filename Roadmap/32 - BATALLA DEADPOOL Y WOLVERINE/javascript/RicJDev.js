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
    this.hp = hp

    if (this.hp > 2000) {
      console.log(pc.gray('Se ha establecido en el máximo de 2000 hp.'))
      this.hp = 2000
    } else if (hp < 500 || isNaN(hp)) {
      console.log(pc.gray('Se ha establecido en el mínimo de 500 hp.'))
      this.hp = 500
    }

    this.canAttack = true

    this.attackRange = attackRange
    this.defenseRate = defenseRate
  }

  attack() {
    let damage = 0

    if (this.canAttack) {
      damage = Math.floor(
        Math.random() * (this.attackRange.max - this.attackRange.min + 1) + this.attackRange.min
      )
    }

    return damage
  }

  defense(damage) {
    let result = Math.floor(Math.random() * 100 + 1)

    if (result > 100 - this.defenseRate) {
      damage = 0
    }

    this.hp -= damage

    if (this.hp < 0) {
      this.hp = 0
    }

    return damage
  }

  get lifeBar() {
    let bars = pc.green('|'.repeat(Math.floor(this.hp / 25)))

    if (this.hp === 0) {
      bars = pc.gray(' - ')
    }

    return pc.bgBlack(`${bars}`)
  }
}

//Funciones del simulador
function display(playerA, playerB) {
  console.log(`\n${playerA.name} (${playerA.hp}):\n${playerA.lifeBar} `)
  console.log(`\n${playerB.name} (${playerB.hp}):\n${playerB.lifeBar} `)
}

function simulateAtack(playerA, playerB) {
  let message

  if (playerA.canAttack) {
    let defenseResult = playerB.defense(playerA.attack())

    if (defenseResult > 0) {
      message = `ataque efectivo! ${playerB.name} ${pc.magenta(`-${defenseResult} hp`)}`

      if (defenseResult === playerA.attackRange.max) {
        message += pc.magenta(' [CRITICAL]')

        playerB.canAttack = false
      }
    } else {
      message = `${playerB.name} ha esquivado el ataque`
    }
  } else {
    message = `recibió un golpe crítico. No puede atacar`

    playerA.canAttack = true
  }

  console.log(`\nTurno de ${playerA.name}: ${message}\n`)
}

let turn = true

function simulateTurn(playerA, playerB) {
  display(playerA, playerB)

  if (turn) {
    simulateAtack(playerA, playerB)

    turn = false
  } else {
    simulateAtack(playerB, playerA)

    turn = true
  }
}

function simulateBattle(playerA, playerB) {
  let battle = setInterval(() => {
    console.clear()
    console.log(pc.underline('\nBATALLA EN CURSO!'))

    simulateTurn(playerA, playerB)

    if (playerA.hp === 0 || playerB.hp === 0) {
      clearInterval(battle)

      console.clear()
      console.log(pc.underline('BATALLA FINALIZADA!'))

      display(playerA, playerB)

      if (playerA.hp === 0) {
        console.log(`\n${playerB.name} ha ganado!\n`)
      } else if (playerB.hp === 0) {
        console.log(`\n${playerA.name} ha ganado!\n`)
      }
    }
  }, 1100)
}

//Implementacion en terminal
async function main() {
  console.clear()
  console.log(pc.underline('\nBIENVENIDO AL SIMULADOR!\n'))

  //Deadpool
  let deadpoolHP = await rl.question('Indique la cantidad de vida para Deadpool. ')
  deadpoolHP = parseInt(deadpoolHP)

  const Deadpool = new Character(pc.red('Deadpool'), deadpoolHP, { min: 10, max: 100 }, 25)

  //Wolverine
  let wolverineHP = await rl.question('Indique la cantidad de vida para Wolverine. ')
  wolverineHP = parseInt(wolverineHP)

  const Wolverine = new Character(pc.yellow('Wolverine'), wolverineHP, { min: 10, max: 120 }, 20)

  console.log(pc.gray('Cargando...'))
  simulateBattle(Deadpool, Wolverine)

  rl.close()
}

main()
