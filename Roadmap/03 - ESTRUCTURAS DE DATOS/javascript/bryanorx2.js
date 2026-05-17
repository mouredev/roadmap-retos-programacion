/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto
 *   en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 */

//1. Arrays

let countriesArray = ["Argentina", "Brasil", "Colombia"]
console.log(countriesArray)

//Inserción
countriesArray.unshift("Perú")
countriesArray.push("Ecuador")
console.log(countriesArray)

//Eliminación
countriesArray.pop()
console.log(countriesArray)

//Actualización
countriesArray[4] = "Uruguay"
console.log(countriesArray)

//Ordenación
countriesArray.sort()
console.log(countriesArray)

//2. Object
let person = {
    name: "Bryan",
    age: 30,
    email: "bryanorx@gmail.com"
}
console.log(person)

//Inserción
person.cellphoneNumber = "987654321"
console.log(person)

//Eliminación
delete person.email
console.log(person)

//Actualización
person.name = "Bryan Orlando"
console.log(person)

//Ordenación
let keysPerson = Object.keys(person)
keysPerson.sort()
console.log(keysPerson)

//3. Maps
let daysMap = new Map ([
    ["name", "Orlando"],
    ["alias", "bryanorx2"],
    ["age", 30],
])
console.log(daysMap)

//Inserción
daysMap.set("email","bryanorx2@gmail.com")
console.log(daysMap)

//Eliminación
daysMap.delete("alias")
console.log(daysMap)

//Actualización
daysMap.set("name","Bryan")
console.log(daysMap)

//Ordenación
let keysMap = Array.from(daysMap.keys())
console.log(keysMap.sort())

//4. Sets
let fruitsSet = new Set (["manzana", "pera", "uva", "naranja"])
console.log(fruitsSet)

//Inserción
fruitsSet.add("sandía")
console.log(fruitsSet)

//Eliminación
fruitsSet.delete("pera")
console.log(fruitsSet)

//Actualización
//No permite agregar duplicados
fruitsSet.add("uva")
console.log(fruitsSet)
fruitsSet.delete("uva")
fruitsSet.add("mandarina")
console.log(fruitsSet)

//Ordenación
let valuesSet = Array.from(fruitsSet.values())
console.log(valuesSet.sort())


const { format } = require("path")
/* DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización
 *   y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
 *   y a continuación los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no numéricos y con más
 *   de 11 dígitos (o el número de dígitos que quieras).
 * - También se debe proponer una operación de finalización del programa.
*/

const readline = require("readline")
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

function menu(){
    console.log("--AGENDA DE CONTACTOS--")
    let arrayOptions = ["1. Buscar contacto", "2. Insertar contacto", "3. Actualizar contacto", "4. Eliminar contacto", "5. Salir"]
    
    for (let i of arrayOptions) {
        console.log(i)
    }
    
    rl.question("Elige una opcion: ",(option) => {
        if (option === "5"){
            console.log("Hasta luego")
            rl.close()
        } else if (option === "1") {
            buscar()
        } else if (option === "2") {
            insertar()
        } else if (option === "3") {
            actualizar()
        } else if (option === "4") {
            eliminar()
        } else {
            console.log("Opción no válida ❌")
            setTimeout(menu, 1500)
        }
})
}
menu()

let contactos = {}
const onlyNumbers = /^\d+$/

function insertar() {
    rl.question("Nombre del nuevo contacto: ", (nombre) => {
        rl.question("Teléfono del nuevo contacto: ", (telefono) => {
            if (!(onlyNumbers.test(telefono) && telefono.length === 9)) {
                console.log("Formato de número incorrecto! ❌")
                setTimeout(menu, 1500)
            } else {
                contactos[nombre] = telefono
                console.log("Datos guardados correctamente ✅")
                setTimeout(menu, 1500)
            }
        })
    })
}

function buscar() {
    rl.question("Nombre del contacto a buscar: ", nombre => {
        if (!(nombre in contactos)) {
            console.log("Contacto no existe!! ❌")
            setTimeout(menu, 1500)
        } else {
                console.log(`Teléfono de ${nombre}: ${contactos[nombre]}`)
                setTimeout(menu, 1500)
            }
    })
}

function eliminar() {
    rl.question("Nombre del contacto a eliminar: ", nombre => {
        if (!(nombre in contactos)) {
            console.log("Contacto no existe!!")
            console.log("No se puede eliminar ❌")
            setTimeout(menu, 1500)
        } else {
            delete contactos[nombre]
            console.log("Contacto eliminado correctamente ✅")
            setTimeout(menu, 1500)
        }
    })
}

function actualizar() {
    rl.question("Nombre del contacto a actualizar: ", nombre => {
        if (!(nombre in contactos)) {
            console.log("Contacto no existe, no se puede actualizar ❌")
            setTimeout(menu, 1500)
        } else {
            console.log("Contacto existe")
            console.log(`Nombre: ${nombre}, teléfono: ${contactos[nombre]}`)
            rl.question("Desea actualizar nombre (1) o teléfono (2): ", option => {
                if (option !== "1" && option !== "2"){
                    console.log("Opción no válida ❌")
                    setTimeout(menu, 1500)
                } else if (option === "1") {
                    let nombreAntiguo = nombre
                    rl.question("Ingresa el nombre actualizado: ", nombre => {
                        let telefono = contactos[nombreAntiguo]
                        delete contactos[nombreAntiguo]
                        contactos[nombre] = telefono
                        console.log("Nombre actualizado correctamente ✅")
                        setTimeout(menu, 1500)
                    })
                } else if (option === "2") {
                    rl.question("Ingresa el teléfono actualizado: ", telefono => {
                        if (!(onlyNumbers.test(telefono) && telefono.length === 9)) {
                            console.log("Formato de teléfono incorrecto! ❌")
                            setTimeout(menu, 1500)
                        } else {
                            contactos[nombre] = telefono
                            console.log("Teléfono actualizado correctamente ✅")
                            setTimeout(menu, 1500)
                        }
                    })
                }
            })
        }
    })
}