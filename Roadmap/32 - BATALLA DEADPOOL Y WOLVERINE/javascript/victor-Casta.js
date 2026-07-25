const readline = require('node:readline')
const { stdin: input, stdout: output } = require('node:process')
const rl = readline.createInterface({ input, output })

class Battle {
  constructor() {
    this.player_1 = { name: 'Deadpool', life: 1000, canAttack: true }
    this.player_2 = { name: 'Wolverine', life: 1000, canAttack: true }
  }

  assignamentPlayerLife() {
    rl.question(`Ingresa la vida inicial de Deadpool: `, (lifeFirstPlayer) => {
      rl.question(`Ingresa la vida inicial de Wolverine: `, (lifeSecondPlayer) => {
        let formatLifeFirstPlayer = parseInt(lifeFirstPlayer)
        let formatLifeSecondPlayer = parseInt(lifeSecondPlayer)

        if (formatLifeFirstPlayer > 0 && formatLifeSecondPlayer > 0) {
          this.player_1.life = formatLifeFirstPlayer
          this.player_2.life = formatLifeSecondPlayer
          console.log(this.player_1)
          console.log(this.player_2)

          this.fight()
        } else {
          console.log('La vida del personaje no puede ser menor que 0')
        }
        rl.close()
      })
    })
  }

  fight() {
    console.log('\n¡Comienza la batalla!\n')
    while (this.player_1.life > 0 && this.player_2.life > 0) {
      if (this.player_1.canAttack) {
        const damageToPlayer2 = Math.round(Math.random() * (100 - 10) + 10)
        const dodgeChancePlayer2 = Math.random() * 100

        if (damageToPlayer2 === 100) {
          console.log(`${this.player_2.name} recibe el daño máximo y no puede atacar la próxima ronda.`)
          this.player_2.canAttack = false
        } else if (dodgeChancePlayer2 <= 25) {
          console.log(`${this.player_2.name} esquivó el ataque de ${this.player_1.name}`)
        } else {
          this.player_2.life -= damageToPlayer2
          console.log(
            `${this.player_1.name} ataca a ${this.player_2.name} y le hace ${damageToPlayer2} de daño. Vida restante de ${this.player_2.name}: ${this.player_2.life}`
          )
        }
      } else {
        console.log(`${this.player_2.name} está recuperándose y no puede atacar esta ronda.`)
        this.player_2.canAttack = true
      }

      if (this.player_2.life <= 0) {
        console.log('\n¡Gana Deadpool!')
        return
      }

      if (this.player_2.canAttack) {
        const damageToPlayer1 = Math.round(Math.random() * (100 - 10) + 10)
        const dodgeChancePlayer1 = Math.random() * 100

        if (damageToPlayer1 === 100) {
          console.log(`${this.player_1.name} recibe el daño máximo y no puede atacar la próxima ronda.`)
          this.player_1.canAttack = false
        } else if (dodgeChancePlayer1 <= 20) {
          console.log(`${this.player_1.name} esquivó el ataque de ${this.player_2.name}`)
        } else {
          this.player_1.life -= damageToPlayer1
          console.log(
            `${this.player_2.name} ataca a ${this.player_1.name} y le hace ${damageToPlayer1} de daño. Vida restante de ${this.player_1.name}: ${this.player_1.life}`
          )
        }
      } else {
        console.log(`${this.player_1.name} está recuperándose y no puede atacar esta ronda.`)
        this.player_1.canAttack = true
      }

      if (this.player_1.life <= 0) {
        console.log('\n¡Gana Wolverine!')
        return
      }
    }
  }
}

const legendBattle = new Battle()
legendBattle.assignamentPlayerLife()
