/*
 * EJERCICIO:
 * He presentado mi proyecto más importante del año: mouredev pro.
 * Un campus para la comunidad, que lanzaré en octubre, donde estudiar
 * programación de una manera diferente.
 * Cualquier persona suscrita a la newsletter de https://mouredev.pro
 * accederá a sorteos mensuales de suscripciones, regalos y descuentos.
 *
 * Desarrolla un programa que lea los registros de un fichero .csv y
 * seleccione de manera aleatoria diferentes ganadores.
 * Requisitos:
 * 1. Crea un .csv con 3 columnas: id, email y status con valor "activo"
 *    o "inactivo" (y datos ficticios).
 *    Ejemplo: 1 | test@test.com | activo
 *             2 | test2@test.com | inactivo
 *    (El .csv no debe subirse como parte de la corrección)
 * 2. Recupera los datos desde el programa y selecciona email aleatorios.
 * Acciones:
 * 1. Accede al fichero .csv y selecciona de manera aleatoria un email
 *    ganador de una suscripción, otro ganador de un descuento y un último
 *    ganador de un libro (sólo si tiene status "activo" y no está repetido).
 * 2. Muestra los emails ganadores y su id.
 * 3. Ten en cuenta que la primera fila (con el nombre de las columnas)
 *    no debe tenerse en cuenta.
 */

class User{
    constructor(id, email, state) {
        this.id = id
        this.email = email
        this.state = state
    }
}

function readCSV(path) {
    const fs = require('node:fs');
    
    try {
        const data = fs.readFileSync(path, 'utf8');
        const allLines = data.split(/\r\n|\n/)
        return allLines
    } catch (err) {
        console.error(err);
        return null
    }
}

const lines = readCSV("C:\\Users\\isaac\\Desktop\\usuarios.csv")
let users = new Map()

// Asignar datos al Map
if (lines != null) {
    for (let line of lines) {
        const data = line.split(",")
        
        if (!parseInt(data[0])) {
            continue
        }

        users.set(parseInt(data[0]), new User(data[0], data[1], data[2]))
    }
    //console.log(users)
}

// Generar ganadores
let winner1
let winner2
let winner3
let id = 0

do {
    id = Math.floor(Math.random() * users.size) + 1

    if (users.has(id)) {
        winner1 = users.get(id)
    }
} while (winner1 == undefined)

do {
    id = Math.floor(Math.random() * users.size) + 1

    if (users.has(id) & winner1 != users.get(id)) {
        winner2 = users.get(id)
    }
} while (winner2 == undefined)

do {
    id = Math.floor(Math.random() * users.size) + 1

    if (users.has(id) & winner1 != users.get(id) & winner2 != users.get(id) & users.get(id).state == "activo") {
        winner3 = users.get(id)
    }
} while (winner3 == undefined)

console.log(`Ganador suscripción: ${winner1.id} - ${winner1.email}`)
console.log(`Ganador descuento: ${winner2.id} - ${winner2.email}`)
console.log(`Ganador libro: ${winner3.id} - ${winner3.email}`)





