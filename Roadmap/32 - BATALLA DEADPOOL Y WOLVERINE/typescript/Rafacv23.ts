/*
    Creado por Rafa Canosa
    Github: https://github.com/Rafacv23
    Website: https://www.rafacanosa.dev
*/

interface Character {
  name: string
  health: number
  critic: boolean
  minDamage: number
  maxDamage: number
  dodge: number
}

// Definimos las constantes de la vida de ambos personajes
let deadpoolHealth: number = 1000
let wolverineHealth: number = 1000
let turn: number = 0

// Definimos los objetos con los datos de cada personaje
const characters: Character[] = [
  {
    name: "Deadpool",
    health: deadpoolHealth,
    critic: false,
    minDamage: 10,
    maxDamage: 100,
    dodge: 0.25,
  },
  {
    name: "Wolverine",
    health: wolverineHealth,
    critic: false,
    minDamage: 10,
    maxDamage: 120,
    dodge: 0.2,
  },
]

// Función para generar el valor del ataque de cada personaje
function getAttackValue(min: number, max: number): number {
  min = Math.ceil(min)
  max = Math.floor(max)
  return Math.floor(Math.random() * (max - min) + min)
}

// Función para hacer que el bucle se espere un segundo entre cada iteración (turno del combate)
function sleep(ms: number): Promise<void> {
  return new Promise((resolve) => setTimeout(resolve, ms))
}

// Función que ejecuta el turno de cada personaje
function attack(atack: string, defend: string): number | undefined {
  // Buscamos dentro del array characters el personaje que es atacante y el defensor
  const attacker = characters.find((character) => character.name === atack)
  const defender = characters.find((character) => character.name === defend)

  if (attacker && defender) {
    if (defender.critic === true) {
      // Comprobamos que el personaje que tiene que defender no haya hecho crítico en el turno anterior
      console.log(
        `${attacker.name} no puede atacar en este turno, tiene que regenerarse.`
      )
      return defender.health
    } else {
      // Asignamos valor al ataque del personaje
      let attackerDamage = getAttackValue(
        attacker.minDamage,
        attacker.maxDamage
      )

      // Comprobamos si el ataque ha sido crítico
      if (attackerDamage === attacker.maxDamage) {
        console.log(
          `${attacker.name} ha hecho un golpe crítico: ${attackerDamage}`
        )
        attacker.critic = true
      } else {
        console.log(
          `El ataque de ${attacker.name} tiene un valor de ${attackerDamage}`
        )
        attacker.critic = false
      }

      // Comprobamos si el defensor evade el ataque
      if (Math.random() <= defender.dodge) {
        console.log(
          `${defender.name} ha esquivado el ataque de ${attacker.name}`
        )
        attackerDamage = 0
      }

      // Restamos la vida del defensor
      defender.health -= attackerDamage

      console.log(`Vida restante de ${defender.name}: ${defender.health}`)

      // Comprobamos que siga vivo
      if (defender.health <= 0) {
        console.log(`${defender.name} ha muerto.`)
      }

      // Retornamos el valor para comprobar la siguiente iteración del bucle
      return defender.health
    }
  }

  // En caso de que no se encuentren los personajes, retornamos `undefined`
  return undefined
}

// Función autoejecutada
;(async () => {
  // Mientras la vida de los dos personajes sea superior a cero ejecutamos el bucle
  while (deadpoolHealth > 0 && wolverineHealth > 0) {
    await sleep(1000) // Esperamos un segundo entre cada turno

    // Incrementamos el turno al inicio de cada iteración del bucle
    turn = turn + 1

    console.log(`Turno: ${turn}`)

    wolverineHealth = attack("Deadpool", "Wolverine") ?? wolverineHealth

    if (wolverineHealth <= 0) {
      console.log("Deadpool ha ganado.")
      break
    }

    deadpoolHealth = attack("Wolverine", "Deadpool") ?? deadpoolHealth

    if (deadpoolHealth <= 0) {
      console.log("Wolverine ha ganado.")
      break
    }
  }
})()
