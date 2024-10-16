// Hecho por @Rafacv23 | https://github.com/Rafacv23 | https://twitter.com/rafacanosa  | https://www.rafacanosa.dev

// Global constants
const EVADE_CHANCE = 0.2
const HEALTH = 100

class Fighter {
  constructor(nombre, velocidad, ataque, defensa) {
    this.nombre = nombre
    this.velocidad = this.checkAttribute(velocidad, "velocidad")
    this.ataque = this.checkAttribute(ataque, "ataque")
    this.defensa = this.checkAttribute(defensa, "defensa")
    this.salud = HEALTH // Inicialmente, todos tienen 100 de salud
  }

  // ensure that the attribute are between 0 and 100
  checkAttribute(value, attribute) {
    if (value < 0 || value > 100) {
      throw new Error(`El valor de ${attribute} debe ser entre 0 y 100`)
    }
    return value
  }

  attack(defender) {
    if (defender.salud === 0) {
      console.log(`${defender.nombre} ha perdido toda su salud`)
      return
    }

    // calculamos si el defensor evita el ataque o no
    const evade = Math.random()

    if (evade < EVADE_CHANCE) {
      console.log(`${defender.nombre} ha esquivado el ataque`)
      return
    }
    // Calcular el daño
    let damage

    if (defender.defensa > this.ataque || defender.defensa === this.ataque) {
      damage = this.ataque * 0.1 // Recibe solo el 10% del ataque
      console.log(`${defender.nombre} bloquea gran parte del daño!`)
    } else {
      damage = this.ataque - defender.defensa // Full damage
    }

    // Evitar que el daño sea negativo
    if (damage < 0) damage = 0

    // Aplicar el daño al defensor
    defender.salud -= damage

    console.log(
      `${this.nombre} ha atacado a ${defender.nombre} con ${damage.toFixed(
        2
      )} de daño`
    )
    console.log(`Salud restante de ${defender.nombre}: ${defender.salud}`)
  }

  showInfo() {
    console.log(`Nombre: ${this.nombre}`)
    console.log(`Velocidad: ${this.velocidad}`)
    console.log(`Ataque: ${this.ataque}`)
    console.log(`Defensa: ${this.defensa}`)
    console.log(`Salud: ${this.salud}`)
  }
}

const fighters = [
  new Fighter("Goku", 85, 95, 80),
  new Fighter("Vegeta", 80, 90, 85),
  new Fighter("Piccolo", 70, 75, 90),
  new Fighter("Gohan", 88, 92, 78),
  new Fighter("Trunks", 78, 88, 82),
  new Fighter("Kefla", 60, 90, 85),
  new Fighter("Freezer", 75, 85, 80),
  new Fighter("Cell", 83, 87, 90),
]

function shuffleFighters(fighters) {
  for (let i = fighters.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1))
    ;[fighters[i], fighters[j]] = [fighters[j], fighters[i]]
  }
  return fighters
}

function drawFighters() {
  let round = 1

  while (fighters.length > 1) {
    if (fighters.length === 2) {
      console.log(`\n--- Ronda Final ---`)
    } else {
      console.log(`\n--- Ronda ${round} ---`)
    }

    // Shuffle fighters for random matchups
    shuffleFighters(fighters)

    // Process battles in pairs
    for (let i = 0; i < fighters.length; i++) {
      const fighter1 = fighters[i]
      const fighter2 = fighters[i + 1]

      console.log(
        `\n${fighter1.nombre} (Salud: ${fighter1.salud}) vs ${fighter2.nombre} (Salud: ${fighter2.salud})`
      )

      // Decide who attacks first based on speed
      let attacker, defender
      if (fighter1.velocidad >= fighter2.velocidad) {
        attacker = fighter1
        defender = fighter2
      } else {
        attacker = fighter2
        defender = fighter1
      }

      // Fight until one of them loses
      while (attacker.salud > 0 && defender.salud > 0) {
        attacker.attack(defender)
        if (defender.salud > 0) {
          defender.attack(attacker)
        }
      }

      // Remove the defeated fighter
      if (attacker.salud <= 0) {
        console.log(`${attacker.nombre} ha sido eliminado`)
        console.log(`${defender.nombre} avanza a la siguiente ronda`)
        fighters.splice(fighters.indexOf(attacker), 1)
      } else if (defender.salud <= 0) {
        console.log(`${defender.nombre} ha sido eliminado`)
        console.log(`${attacker.nombre} avanza a la siguiente ronda`)
        fighters.splice(fighters.indexOf(defender), 1)
      }
    }

    round++
  }

  // The last remaining fighter is the winner
  if (fighters.length === 1) {
    console.log("\n¡El torneo ha terminado! El ganador/a es:")
    fighters[0].showInfo()
  }
}

// function that sims the tournament
;(function tournament() {
  if (
    (fighters.length & (fighters.length - 1)) !== 0 ||
    fighters.length === 0
  ) {
    console.log("El número de luchadores debe ser una potencia de 2")
    return
  }
  drawFighters()
})()
