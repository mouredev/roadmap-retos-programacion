/*
# #03 ESTRUCTURAS DE DATOS
> #### Dificultad: Media | Publicación: 15/01/24 | Corrección: 22/01/24

## Ejercicio

```
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
 * - El programa no puede dejar introducir números de teléfono no numéricos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
 */

/*
#### Tienes toda la información extendida sobre el roadmap de retos de programación en **[retosdeprogramacion.com/roadmap](https://retosdeprogramacion.com/roadmap)**.

Sigue las **[instrucciones](../../README.md)**, consulta las correcciones y aporta la tuya propia utilizando el lenguaje de programación que quieras.

> Recuerda que cada semana se publica un nuevo ejercicio y se corrige el de la semana anterior en directo desde **[Twitch](https://twitch.tv/mouredev)**. Tienes el horario en la sección "eventos" del servidor de **[Discord](https://discord.gg/mouredev)**.
*/

console.log("--------------------------------------")
console.log("** ARRAY **")
console.log("--------------------------------------")
console.log("** Declaración **")
console.log(`let myArray = []`)
let myArray = []
console.log(myArray, "\n")

console.log("** Inserción **")
console.log("push() -> Añade al final")
myArray.push("Peter")
myArray.push("Parker")
myArray.push("Spiderman")
console.log(myArray, "\n")
console.log("unshift() -> Añade al principio")
myArray.unshift("Marvel Hero")
console.log(myArray, "\n")

console.log("** Borrado **")
console.log("pop() -> Elimina el último")
myArray.pop() //Elimina el último, puede almacenarse
console.log(myArray, "\n")
console.log("shift() -> Elimina el primero")
myArray.shift()
console.log(myArray, "\n")
console.log("splice() -> Elimina un elemento en la posición indicada")
myArray.splice(1, 2) // elimina desde la posición 1, 2 elementos
console.log(myArray, "\n")

console.log("** Actualización **")
myArray = ["Peter", "Parker", "Spiderman"]
console.log(myArray)
// console.log("indexOf() -> ")
console.log((myArray[myArray.indexOf("Spiderman")] = "Spidey"))
// console.log(myArray,"\n")

console.log("** Ordenación **")
console.log("sort()")
myArray.sort()
console.log(myArray, "\n")

console.log("--------------------------------------")
console.log("** SET **")
// set - son datos ordenados sin indices, no se pueden repetir los elementos
console.log("--------------------------------------")
console.log("** Declaración **")
console.log(`Opción 1 -let mySet = new Set()`)
let mySet = new Set()
console.log(mySet, "\n")
console.log(`
Opción 2 - mySet_two = new Set([
    "Bruce",
    "Banner",
    "Hulk",
    40,
  ]) `)
mySet_two = new Set(["Bruce", "Banner", "Hulk", 40])
console.log(mySet_two, "\n")

console.log("** Inserción **")
console.log(`add()
mySet.add("Tony")
mySet.add("Stark")
mySet.add("Iron Man")\n
    `)
mySet.add("Tony")
mySet.add("Stark")
mySet.add("Iron Man")
console.log(mySet, "\n")

console.log("** Borrado **")
// delete -> elimina un elemento especifico, devuelve true si lo ha eliminado
console.log(` delete() -> elimina un elemento especifico, devuelve true si lo ha eliminado
console.log(mySet.delete("Iron Man"))
    `)
console.log(mySet.delete("Iron Man"))
console.log(mySet, "\n")

console.log("** Actualización **")
console.log(`
No permite modificación inmediata:
1. Elimina el valor existente con delete()
2. Añade con add()    
    `)

console.log("** Ordenación **")
console.log(`
En el set el orden es el de la incorporación, si fuera necesario
deberia convertirse en array y ordenarlo, y convertir de nuevo   
\n`)

console.log("--------------------------------------")
console.log("** MAP **")
console.log("--------------------------------------")
console.log("** Declaración **")
console.log(`
let myMap = new Map();
    `)
let myMap = new Map()
console.log(myMap, "\n")

console.log("** Inserción **")
console.log(`
- Permite cualquier tipo de dato como clave
myMap.set("name", "Peter")
myMap.set(42, "Edad")
myMap.set(true, "Es un héroe")
    `)
myMap.set("name", "Peter")
myMap.set(42, "Edad")
myMap.set(true, "Es un héroe")
console.log(myMap, "\n")

console.log("** Borrado **")
console.log(`
 delete() -> elimina un elemento según clave   
 console.log(myMap.delete("name"))
    `)
console.log(myMap.delete("name"))
console.log(myMap, "\n")
console.log(`
clear() -> elimina todos los elementos`)
myMap.clear()
console.log(myMap)

console.log("** Actualización **")
console.log("Igual que inserción\n")

console.log("** Ordenación **")
console.log(`
En el map el orden es el de la incorporación  
\n`)
console.log(`
Podemos ordenarlos por claves o por valores  
    \n`)


console.log("--------------------------------------")
console.log("** OBJETOS **")
console.log("--------------------------------------")
console.log("** Declaración **")
console.log(`
let persona = {
    nombre: "Peter",
    apellido: "Parker",
    email: "parker@parker.com",
    edad: 25,
  } 
    `)

let persona = {
    nombre: "Peter",
    apellido: "Parker",
    email: "parker@parker.com",
    edad: 25,
  }
console.log(persona)

console.log("** Inserción **")
console.log(`
persona.year=2025
    `)
persona.year=2025
console.log(persona)

console.log("** Borrado **")
console.log(`
delete persona.year
    `)
delete persona.year
console.log(persona)

console.log("** Actualización **")
console.log('Asignar sobre clave existente\n')

console.log("** Ordenación **")
console.log("Sin orden específico, para ordenar convertir en array y sort()")

console.log("--------------------------------------")
console.log("--------------------------------------")
console.log("**** EXTRA ****")
console.log("--------------------------------------")

// * DIFICULTAD EXTRA (opcional):
// * Crea una agenda de contactos por terminal.
// * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
// * - Cada contacto debe tener un nombre y un número de teléfono.
// * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
// *   los datos necesarios para llevarla a cabo.
// * - El programa no puede dejar introducir números de teléfono no numéricos y con más de 11 dígitos.
// *   (o el número de dígitos que quieras)
// * - También se debe proponer una operación de finalización del programa.

const readline = require("readline")

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
})

let contacts = []

function showMenu() {
  console.log("\n===========================")
  console.log("       *** AGENDA ***")
  console.log("===========================")
  console.log("1. Nuevo contacto")
  console.log("2. Buscar contacto")
  console.log("3. Actualizar contacto")
  console.log("4. Eliminar contacto")
  console.log("5. Listar contactos")
  console.log("6. Salir\n")
  rl.question("Selecciona una opción: ", handleMenu)
}

function handleMenu(option) {
  switch (option) {
    case "1":
      addContact()
      break
    case "2":
      searchContact()
      break
    case "3":
      updateContact()
      break
    case "4":
      deleteContact()
      break
    case "5":
      showContacts()
      break
    case "6":
      console.log("Saliendo...")
      rl.close()
      break
    default:
      console.log("Opción no válida")
      showMenu()
  }
}

function addContact() {
  rl.question("Nombre: ", (name) => {
    rl.question("Número de teléfono: ", (phone) => {
      if (!/^[0-9]{1,11}$/.test(phone)) {
        console.log("Número de teléfono inválido (máx. 11 dígitos)")
        return showMenu()
      }
      contacts.push({ name, phone })
      console.log("-- Contacto añadido --")
      showMenu()
    })
  })
}

function searchContact() {
  rl.question("Nombre a buscar: ", (name) => {
    const results = contacts.filter((c) =>
      c.name.toLowerCase().includes(name.toLowerCase())
    )
    if (results.length) {
      console.log("-- Resultados:", results)
    } else {
      console.log("-- No se encontraron contactos --")
    }
    showMenu()
  })
}

function updateContact() {
  rl.question("Nombre del contacto a actualizar: ", (name) => {
    const index = contacts.findIndex(
      (c) => c.name.toLowerCase() === name.toLowerCase()
    )
    if (index === -1) {
      console.log("-- Contacto no encontrado --")
      return showMenu()
    }
    rl.question("Nuevo número de teléfono: ", (phone) => {
      if (!/^[0-9]{1,11}$/.test(phone)) {
        console.log("Número de teléfono inválido (máx. 11 dígitos)")
        return showMenu()
      }
      contacts[index].phone = phone
      console.log("Contacto actualizado")
      showMenu()
    })
  })
}

function deleteContact() {
  rl.question("Nombre del contacto a eliminar: ", (name) => {
    const index = contacts.findIndex(
      (c) => c.name.toLowerCase() === name.toLowerCase()
    )
    if (index === -1) {
      console.log("Contacto no encontrado")
      return showMenu()
    }
    rl.question(
      "Seguro que quieres eliminar el contacto? (S/N): \n",
      (respuesta) => {
        if (respuesta == "S" || respuesta == "s") {
          contacts.splice(index, 1)
          console.log("-- Contacto eliminado --")
          showMenu()
        } else {
          showMenu()
        }
      }
    )
  })
}

function showContacts() {
  if (contacts.length === 0) {
    console.log("No hay contactos guardados")
  } else {
    console.log("Lista de contactos:\n", contacts)
  }
  showMenu()
}

showMenu()