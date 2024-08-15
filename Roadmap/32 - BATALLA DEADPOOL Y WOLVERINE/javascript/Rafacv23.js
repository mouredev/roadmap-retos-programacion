/* 
    Creado por Rafa Canosa
    Github: https://github.com/Rafacv23
    Website: https://www.rafacanosa.dev
*/

// Definimos las constantes de la vida de ambos personajes
let DEADPOOL_HEALTH = 1000
let WOLVERINE_HEALTH = 1000
let turn = 0

// Definimos los objetos con los datos de cada personaje
const characters = [
  {
    name: "Deadpool",
    health: DEADPOOL_HEALTH,
    critic: false,
    minDamage: 10,
    maxDamage: 100,
    dodge: 0.25,
  },
  {
    name: "Wolverine",
    health: WOLVERINE_HEALTH,
    critic: false,
    minDamage: 10,
    maxDamage: 120,
    dodge: 0.2,
  },
]

//Funcion para generar el valor del ataque de cada personaje
function getAttackValue(min, max) {
  min = Math.ceil(min)
  max = Math.floor(max)
  return Math.floor(Math.random() * (max - min) + min)
}

// Función para hacer que el bucle se espere un segundo entre cada iteracion (turno del combate)
function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms))
}

// función que ejecuta el turno de cada personaje
function attack(atack, defend) {
  // Buscamos dentro del array characters el personaje que es atacante y el defensor
  const attacker = characters.find((character) => character.name === atack)
  const defender = characters.find((character) => character.name === defend)

  // Comprobamos que el personaje que tiene que defender no haya hecho crítico en el turno anterior
  if (defender.critic === true) {
    console.log(
      `${attacker.name} no puede atacar en este turno, tiene que regenerarse.`
    )
  } else {
    // asignamos valor al ataque del personaje
    let attackerDamage = getAttackValue(attacker.minDamage, attacker.maxDamage)

    // comprobamos si el ataque ha sido crítico
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

    //comprobamos si el defensor evade el ataque
    if (Math.random() <= defender.dodge) {
      console.log(`${defender.name} ha esquivado el ataque de ${attacker.name}`)
      attackerDamage = 0
    }

    // Restamos la vida del defensor

    defender.health -= attackerDamage

    console.log(`Vida restante de ${defender.name}: ${defender.health}`)

    // Comprobamos que siga vivo

    if (defender.health <= 0) {
      console.log(`${defender.name} ha muerto.`)
    }

    // retornamos el valor para comprobar la siguiente iteración del bucle
    return defender.health
  }
}

// funcion autoejecutada
;(async () => {
  // Mientras la vida de los dos personajes sea superior a cero ejecutamos el bucle
  while (DEADPOOL_HEALTH > 0 || WOLVERINE_HEALTH > 0) {
    await sleep(1000) // esperamos un segundo entre cada turno

    //Incrementamos el turno al inicio de cada iteración del bucle
    turn = turn + 1

    console.log(`Turno: ${turn}`)

    DEADPOOL_HEALTH = attack("Deadpool", "Wolverine")

    if (DEADPOOL_HEALTH <= 0) {
      break
    }

    WOLVERINE_HEALTH = attack("Wolverine", "Deadpool")

    if (WOLVERINE_HEALTH <= 0) {
      break
    }
  }
})()
