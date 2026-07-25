/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
 */

//OBJETO
interface Person {
    names: string;
    age: number;
}

let persona1: Person = {
    names: "Sebastian Rodriguez",
    age: 33,
}

console.log(persona1)
console.log(`La edad de ${persona1.names} es de ${persona1.age} años`)

interface Person { //insercion opcional directo en interface
    city?: string
}

persona1.city = "Barranquilla"
console.log(persona1)
console.log(`La edad de ${persona1.names} es de ${persona1.age} años y su ciudad es en ${persona1.city}`)

persona1.age = 34 //actualizacion
console.log(`Cambiamos la edad de persona1, antes era 33 y ahora es: ${persona1.age}`)

persona1["hobby"] = "Tocar la guitarra" // insercion directa 
console.log(persona1)

delete persona1.city //borre la propiedad city de persona1
console.log(persona1)


// ARRAY

const myArray: number[] = [1,2,3,4,5] // este es un array de numeros
console.log(myArray)

myArray.push(6) //push se utiliza para agregar
console.log(myArray)

const lastElement = myArray.pop() //ELIMINA EL ULTIMO ELEMENTO DEL ARRAY
console.log(lastElement)
console.log(myArray)

const firstElement = myArray.shift() // ELIMINA EL PRIMER ELEMENTO DEL ARRAY
console.log(firstElement)
console.log(myArray)

myArray.unshift(0,1) // AGREGA 1 O VARIOS ELEMENTOS AL COMIENZO DEL ARRAY
console.log(myArray)

myArray.splice(1, 0, 10) //agrega un elemento en la posicion deseada
console.log(myArray)

myArray.splice(1, 1) // ELIMINA UN ELEMENTO EN LA POSICION DESEADA
console.log(myArray)

myArray.sort() // ORDENA EN EL ARRAY EN ORDEN ACENDENTE
console.log(myArray)

myArray.reverse() // INVIERTE EL ORDEN DE LOS ELEMENTOS
console.log(myArray)

// CLASES = MAPS

const myMap = new Map<string, number>() // CREACION DE CLASE

myMap.set("sebastian", 30) //INSERCION CON .SET
myMap.set("laura", 31)
console.log(myMap)

let laura = myMap.get("laura") // BUSQUEDA
console.log(laura)

myMap.delete("laura") // ELIMINA UNA CLASE DEL MAP
console.log(myMap)

// VERIFICA SI EXISTE LA CLASE
console.log(myMap.has("sebastian"))
console.log(myMap.has("laura"))

console.log(myMap.size) // CON SIZE PUEDO SABER EL TAMAÑO DEL MAP

// SET

const mySet = new Set<number>([1,2,3,4,5])
console.log(mySet)

mySet.add(6) // INSERCION
console.log(mySet)
mySet.add(5) // NO ACEPTA DUPLICACIONES
console.log(mySet)

mySet.delete(2) //BORRA
console.log(mySet)

console.log(mySet.has(2)) // VERIFICA SI CONTIENE EL ELEMENTO Y DEVUELVE TRUE O FALSE
console.log(mySet.has(4)) // VERIFICA SI CONTIENE EL ELEMENTO Y DEVUELVE TRUE O FALSE

console.log(mySet.size) // MUESTRA EL TAMAÑO DE SET

mySet.clear() // LIMPIA TODO EL SET
console.log(mySet)
console.log(mySet.size)

// EXTRA - AGENDA DE CONTACTOS

const readline = require("readline")!

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

const contactos = new Map<string, string>()

const addContact = ()=>{
    rl.question("Escriba su nombre: ", (nombre:string)=>{
        rl.question("Escriba su numero de celular: ", (celular:string)=>{
            const regex = /^\d{1,9}$/;
            if (contactos.has(nombre)) {
                console.log("El contacto ya existe")
                console.log("")
                addContact()
            }else {
                if (!regex.test(celular)) {
                    contactos.set(nombre, celular)
                    console.log("")
                    console.log(`Contacto nuevo: ${nombre}: ${contactos.get(nombre)}`)
                    console.log("")
                    console.log(`Tienes "${contactos.size}" contactos`)
                    console.log("")
                    agenda()
                } else{
                    console.log("esta errado")
                    addContact()
                }
            }
            
        })
    })
}

const searchContacts = ()=>{
    rl.question("Escribe el nombre del contacto que deseas buscar: ",(nombre: string)=>{
        if (contactos.has(nombre)) {
            console.log("")
            console.log(`nombre: ${nombre}`)
            console.log(`telefono: ${contactos.get(nombre)}`)
            console.log("")
            agenda()
        } else{
            console.log("el contacto no existe")
            agenda()
        }
    })
}

const deleteContact = ()=>{
    console.table(contactos)
    console.log("")
    if (contactos.size === 0) {
        console.log("no hay contactos para eliminar")
        console.log("")
        agenda()
    } else{
        rl.question("Escriba el nombre del contacto que desea eliminar: ", (nombre:string)=>{
            let deleteContact = nombre
            contactos.delete(nombre)
            console.log("")
            console.table(contactos)
            console.log("")
            console.log(`Contacto "${deleteContact}" eliminado`)
            agenda()
        })
    }
}

const replaceContact = ()=>{
    rl.question("Cual es el contacto que deseas reemplazar: ", (nombre: string)=>{
        let usuario: string = nombre
        let telefono = contactos.get(nombre)
        console.log("")
        if (contactos.has(nombre)) {
            console.log(`${usuario}: ${telefono}`)
            console.log("")
            rl.question("que deseas reemplazar, nombre o telefono: ", (opcion: string)=>{
                if (opcion === "nombre") {
                    contactos.delete(nombre)
                    console.log("")
                    rl.question("cual es el nuevo nombre: ", (nuevoNombre: string)=>{
                        contactos.set(nuevoNombre, telefono!)
                        console.table(contactos)
                        console.log("contacto reemplazado")
                        console.log("")
                        agenda()
                    })
                } else if (opcion === "telefono") {
                    contactos.delete(nombre)
                    console.log("")
                    rl.question("cual es el nuevo telefono: ", (nuevoTelefono: string)=>{
                        contactos.set(usuario, nuevoTelefono)
                        console.table(contactos)
                        console.log("contacto reemplazado")
                        console.log("")
                        agenda()
                    })
                }
            })
        } else {
            console.log(`El contacto ${nombre} no existe`)
            console.log("")
            agenda()
        }
    })
}

const viewContact = ()=>{
    console.table(contactos)
    console.log("")
    console.log(`Total contactos: ${contactos.size}`)
    console.log("")
    agenda()
}

const agenda = ()=>{
    console.log("BIENVENIDO A TU AGENDA DE CONTACTOS")
    console.log("")
    rl.question(`Que deseas hacer ahora:
        1. Agregar contacto
        2. Buscar contacto
        3. Eliminar contacto
        4. Reemplazar contacto
        5. Mostrar contactos
        6. Salir
    
        `,(numero:string) =>{
            switch (numero) {
                case "1":
                    addContact()
                    break;
                case "2":
                    searchContacts()
                    break
                case "3":
                    deleteContact()
                    break
                case "4":
                    replaceContact()
                    break
                case "5":
                    viewContact()
                    break
                case "6":
                    rl.close()
                default:
                    break;
            }
        })
}

agenda()