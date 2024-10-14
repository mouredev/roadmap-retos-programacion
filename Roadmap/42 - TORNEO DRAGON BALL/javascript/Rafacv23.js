const fighters = [
  {
    nombre: "Goku",
    velocidad: 85,
    ataque: 95,
    defensa: 80,
    salud: 100,
  },
  {
    nombre: "Vegeta",
    velocidad: 80,
    ataque: 90,
    defensa: 85,
    salud: 100,
  },
  {
    nombre: "Piccolo",
    velocidad: 70,
    ataque: 75,
    defensa: 90,
    salud: 100,
  },
  {
    nombre: "Gohan",
    velocidad: 88,
    ataque: 92,
    defensa: 78,
    salud: 100,
  },
  {
    nombre: "Trunks",
    velocidad: 78,
    ataque: 88,
    defensa: 82,
    salud: 100,
  },
  {
    nombre: "Kefla",
    velocidad: 60,
    ataque: 99,
    defensa: 85,
    salud: 100,
  },
  {
    nombre: "Freezer",
    velocidad: 75,
    ataque: 85,
    defensa: 80,
    salud: 100,
  },
  {
    nombre: "Cell",
    velocidad: 83,
    ataque: 87,
    defensa: 90,
    salud: 100,
  },
]

class Fighter {
  constructor(nombre, velocidad, ataque, defensa) {
    this.nombre = nombre
    this.velocidad = this.checkAttribute(velocidad, "velocidad")
    this.ataque = this.checkAttribute(ataque, "ataque")
    this.defensa = this.checkAttribute(defensa, "defensa")
    this.salud = 100 // Inicialmente, todos tienen 100 de salud
  }

  // ensure that the attribute are between 0 and 100
  checkAttribute(value, attribute) {
    if (value < 0 || value > 100) {
      throw new Error(`El valor de ${attribute} debe ser entre 0 y 100`)
    }
    return value
  }

  attack(attacker, defender) {
    if (this.salud === 0) {
      console.log(`${attacker.nombre} ha perdido toda su salud`)
      return
    }
    if (defender.salud === 0) {
      console.log(`${defender.nombre} ha perdido toda su salud`)
      return
    }
    let damage = this.ataque - defender.defensa
    if (defender.defensa > this.ataque) {
      damage = this.ataque - defender.defensa * 0.1
    }
    defender.salud -= damage
    console.log(
      `${attacker.nombre} ha atacado ${defender.nombre} con ${damage} de daño`
    )
    console.log(`El daño restante de ${defender.nombre} es ${defender.salud}`)
    console.log(`El daño restante de ${attacker.nombre} es ${attacker.salud}`)
  }

  showInfo() {
    console.log(`Nombre: ${this.nombre}`)
    console.log(`Velocidad: ${this.velocidad}`)
    console.log(`Ataque: ${this.ataque}`)
    console.log(`Defensa: ${this.defensa}`)
    console.log(`Salud: ${this.salud}`)
  }
}

// function that sims the tournament
function tournament(fighters) {
  if (
    (fighters.length & (fighters.length - 1)) !== 0 ||
    fighters.length === 0
  ) {
    console.log("El número de luchadores debe ser una potencia de 2")
    return
  }
  console.log("¡El torneo puede comenzar!")
}
