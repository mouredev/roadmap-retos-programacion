//EJERCICIO
//Modelado de personajes
class Character {
  constructor(name, hp, attackRange = { min: 0, max: 50 }, defenseRate) {
    this.name = name
    this.hp = hp

    if (this.hp > 1500) {
      console.log(pc.gray('Se ha establecido un máximo de 1500 hp.'))
      this.hp = 1500
    } else if (hp < 500 || isNaN(hp)) {
      console.log(pc.gray('Se ha establecido un mínimo de 500 hp.'))
      this.hp = 500
    }

    this.attackRange = attackRange
    this.defenseRate = defenseRate
  }

  attactk() {
    let damage = Math.floor(
      Math.random() * (this.attackRange.max - this.attackRange.min + 1) + this.attackRange.min
    )

    return damage
  }

  defense(damageReceived) {
    let result = Math.floor(Math.random() * 100 + 1)

    if (result > 100 - this.defenseRate) {
      damageReceived = 0
    }

    this.hp -= damageReceived

    if (this.hp < 0) {
      this.hp = 0
    }
  }

  get lifeBar() {
    let bars = Math.floor(this.hp / 25)

    if (this.hp === 0) {
      return pc.gray('-'.repeat(20))
    }

    return pc.green('|'.repeat(bars))
  }
}

let test = new Character('Juan', 1300, { min: 5, max: 90 }, 0)
console.log(test.hp)
console.log(test.lifeBar)

for (let i = 0; i < 10; i++) {
  let attack = test.attactk()

  if (attack === test.attackRange.max) {
    console.log(pc.red('CRITICAL:'), attack)
  }

  test.defense(attack)
}

console.log(test.hp)
console.log(test.lifeBar)

/*

  - Se ejecuta en Node.js, importando el modulo Readline/promises (https://nodejs.org/api/readline.html)
  - Se ha instalado Picocolors, un libreria para colorear texto en terminal (https://www.npmjs.com/package/picocolors)

*/

import * as readline from 'node:readline/promises'
import pc from 'picocolors'

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
})

let Deadpool
let Wolverine

async function main() {
  console.clear()

  console.log(pc.underline('\nBIENVENIDO AL SIMULADOR!'))
  console.log(' ')

  let deadpoolHP = await rl.question('Indique la cantidad de vida para Deadpool. ')
  deadpoolHP = parseInt(deadpoolHP)

  Deadpool = new Character('Deadpool', deadpoolHP, { min: 10, max: 100 }, 25)

  let wolverineHP = await rl.question('Indique la cantidad de vida para Wolverine. ')
  wolverineHP = parseInt(wolverineHP)

  Wolverine = new Character('Wolverine', wolverineHP, { min: 10, max: 120 }, 20)

  console.log(pc.gray('Cargando...'))

  function display() {
    console.clear()
    console.log(`\n${pc.red(Deadpool.name)} (${Deadpool.hp}):\n${Deadpool.lifeBar} `)
    console.log(`\n${pc.yellow(Wolverine.name)} (${Wolverine.hp}):\n${Wolverine.lifeBar} `)
  }

  setTimeout(display, 1000)

  rl.close()
}

//main()
rl.close()
