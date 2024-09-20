/*
 * EJERCICIO:
 * ¡Deadpool y Wolverine se enfrentan en una batalla épica!
 * Crea un programa que simule la pelea y determine un ganador.
 * El programa simula un combate por turnos, donde cada protagonista posee unos
 * puntos de vida iniciales, un daño de ataque variable y diferentes cualidades
 * de regeneración y evasión de ataques.
 * Requisitos:
 * 1. El usuario debe determinar la vida inicial de cada protagonista.
 * 2. Cada personaje puede impartir un daño aleatorio:
 *    - Deadpool: Entre 10 y 100.
 *    - Wolverine: Entre 10 y 120.
 * 3. Si el daño es el máximo, el personaje que lo recibe no ataca en el
 * siguiente turno, ya que tiene que regenerarse (pero no aumenta vida).
 * 4. Cada personaje puede evitar el ataque contrario:
 *    - Deadpool: 25% de posibilidades.
 *    - Wolverine: 20% de posibilidades.
 * 5. Un personaje pierde si sus puntos de vida llegan a cero o menos.
 * Acciones:
 * 1. Simula una batalla.
 * 2. Muestra el número del turno (pausa de 1 segundo entre turnos).
 * 3. Muestra qué pasa en cada turno.
 * 4. Muestra la vida en cada turno.
 * 5. Muestra el resultado final.
 */

class Character {
    constructor(name, health, minDamage, maxDamage, evasion) {
        this.name = name
        this.health = health
        this.minDamage = minDamage
        this.maxDamage = maxDamage
        this.evasion = evasion
    }

    // Devuelve el numero de daño generado
    attack() {
        return Math.floor(Math.random() * this.maxDamage) + this.minDamage
    }

    // Devuelve true si esquiva el ataque, false si no lo esquiva y le resta puntos de vida
    dodge(damage) {
        let isEvasion = Math.floor(Math.random() * 100) + 1

        // Ha evadido el ataque
        if (isEvasion <= this.evasion) {
            return true
        } else {
            if ((this.health - damage) < 0) {
                this.health = 0
            } else {
                this.health -= damage
            }

            return false
        }
    }
}

const rl = require('readline-sync');

// Pide los puntos de vida que tendra Deadpool
let health = rl.question("Inserte la cantidad de vida que tendra Deadpool? ")
let deadpool = new Character("Deadpool", parseInt(health), 10, 100, 25)

// Pide los puntos de vida que tendra Wolverine
health = rl.question("Inserte la cantidad de vida que tendra Wolverine? ")
let wolverine = new Character("Wolverine", parseInt(health), 10, 120, 20)

console.log("Estadisticas Deadpool")
console.table(deadpool)

console.log("Estadisticas Wolverine")
console.table(wolverine)

battle()

async function battle() {
    let alternate = true
    let evasion = false
    let damage = 0
    let wolverineInitialHealth = wolverine.health
    let deadpoolInitialHealth = deadpool.health

    do {

        // Deadpool
        if (alternate) {
            console.log("Turno de Deadpool")
        
            // Realizar ataque
            damage = deadpool.attack()
            console.log(`Deadpool hace un ataque de ${damage} puntos de daño`)
        
            // Evasión
            evasion = wolverine.dodge(damage)
            if (evasion) {
                console.log("Wolverine ha esquivado el ataque")
            } else {
                console.log(`Wolverine a recibido un ataque de ${damage} puntos de daño`)
            }

            // Comprovar si el turno canvia
            if (damage == deadpool.maxDamage & !evasion) {
                console.log("Wolverine entra en modo de regeneración")
                alternate = true
            } else {
                alternate = false
            }
        } else { // Wolverine
            console.log("Turno de Wolverine")
        
            // Realizar ataque
            damage = wolverine.attack()
            console.log(`Wolverine hace un ataque de ${damage} puntos de daño`)
        
            // Evasión
            evasion = deadpool.dodge(damage)
            if (evasion) {
                console.log("Deadpool ha esquivado el ataque")
            } else {
                console.log(`Deadpool a recibido un ataque de ${damage} puntos de daño`)
            }

            // Comprovar si el turno canvia
            if (damage == wolverine.maxDamage & !evasion) {
                console.log("Deadpool entra en modo de regeneración")
                alternate = false
            } else {
                alternate = true
            }
        }

        // Mostrar vida de los personajes a final de turno
        console.log(`Deadpool: ${deadpool.health}/${deadpoolInitialHealth}`)
        console.log(`Wolverine: ${wolverine.health}/${wolverineInitialHealth}`)

        // Pausa de 1 segundo
        await new Promise(r => setTimeout(r, 1000));
    } while(deadpool.health > 0 & wolverine.health > 0)

    if (deadpool.health == 0) {
        console.log("Wolverine ha ganado la pelea")
    } else {
        console.log("Deadpool ha ganado la pelea")
    }
}