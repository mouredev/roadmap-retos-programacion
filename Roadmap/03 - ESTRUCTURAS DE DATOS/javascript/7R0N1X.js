// Array
let numbers = [5, 0, 1]

numbers.push(2) // Añadir un elemento al final

numbers.unshift(-1) // Añadir un elemento al principio

numbers.pop() // Eliminar el último elemento

numbers.shift() // Eliminar el primer elemento

numbers[1] = 2 // Actualizar un elemento

numbers.sort() // Ordenación

// console.log(numbers)



// Set
let mySet = new Set(numbers)

mySet.add(4) // Añadir un elemento

mySet.delete(5) // Elimina un elemento en específico

// console.log(mySet.has(5)) // Verifica si un elemento existe en el set

// console.log(mySet.size) // Devuelve el tamaño del set

mySet.clear() // Elimina todos los elementos del set

// Los sets no soportan ordenamiento

// console.log(mySet)



// Objetos
let myCar = new Object()

myCar.make = "Ford"; // Añadir un elemento
myCar.model = "Mustang";
myCar.year = 2024;

delete myCar["year"] // Elimina un elemeneto en específico

myCar["model"] = "Ranger" // Actualización

// Los objetos no soportan ordenamiento

// console.log(myCar)



// Map
let myMap = new Map()

myMap.set("Name", "7R0N1X") // Añadir un elemento
myMap.set("Age", 24)
myMap.set("Country", "Colombia")

myMap.delete("Age") // Eliminar

myMap.set("Country", "Ecuador") // Actualizar

// Los maps no soportan ordenamiento

// console.log(myMap)



// Dificultad extra
let readline = require('readline')
let rl = readline.createInterface({ input: process.stdin, output: process.stdout })
let opc = 0
let contacts = []

const App = () => {
  console.log(`
    **************************************************
    *                                                *
    *              GESTIÓN DE CONTACTOS              *
    *                                                *
    **************************************************
    *                                                *
    *    1. Buscar contacto                          *
    *    2. Ingresar nuevo contacto                  *
    *    3. Actualizar contacto                      *
    *    4. Eliminar contacto                        *
    *    5. Salir                                    *
    *                                                *
    **************************************************
    `);

  rl.question('Opción: ', (answer) => {
    opc = parseInt(answer)

    switch (opc) {
      case 1:
        if (contacts.length === 0) {
          alerta('No hay contactos')
          App()
        } else {
          rl.question('Nombre: ', (nombre) => {
            filtrar(nombre)
            App()
          })
        }
        break
      case 2:
        rl.question('Nombre: ', (nombre) => {
          if (existe(nombre)) {
            alerta('Error: Nombre ya existe')
            App()
          } else {
            rl.question('Numero: ', (numero) => {
              if (/^\d{1,11}$/.test(numero) && Number(numero)) {
                let contact = { nombre, numero }
                ingresar(contact)
                alerta('Contacto ingresado correctamente')
                App()
              } else {
                alerta('Error: Número no válido')
                App()
              }
            })
          }
        })
        break
      case 3:
        rl.question('Nombre: ', (nombre) => {
          if (existe(nombre)) {
            rl.question('Numero: ', (numero) => {
              let contact = { nombre, numero }
              actualizar(contact)
              alerta('Contacto actualizado correctamente')
              App()
            })
          } else {
            alerta('Error: Nombre no existe')
            App()
          }
        })
        break
      case 4:
        rl.question('Nombre: ', (nombre) => {
          if (existe(nombre)) {
            eliminar(nombre)
            alerta('Contacto eliminado correctamente')
            App()
          } else {
            alerta('Error: El contacto no existe')
            App()
          }

        })
        break
      case 5:
        rl.close()
        break
      default:
        alerta('Error: Opción desconocida')
        App()
    }
  })

  function filtrar(nombre) {
    existe(nombre) ? mostrar(contacts.filter((contact) => contact.nombre === nombre)) : alerta('Error: El contacto no existe')
  }

  function existe(nombre) {
    return contacts.find((contact) => contact.nombre === nombre)
  }

  function ingresar(contact) {
    contacts = [...contacts, contact]
  }

  function actualizar(contact) {
    let { nombre, numero } = contact
    contacts.map((contact) => {
      if (contact.nombre === nombre) {
        contact.numero = numero
      }
    })
  }

  function eliminar(nombre) {
    contacts = contacts.filter((contact) => contact.nombre !== nombre)
  }

  function mostrar(contacts) {
    console.log(`
    **************************************************
    *                                                *
    *                LISTA DE CONTACTOS              *
    *                                                *
    **************************************************
    `);
    contacts.map((contact) => {
      let { nombre, numero } = contact
      console.log(`
    **************************************************                     
        Nombre: ${nombre}                           
        Teléfono: ${numero}                         
    **************************************************
    `)
    })
  }

  function alerta(mensaje) {
    console.log(`
    **************************************************
        ${mensaje}
    **************************************************
    `)
  }

}

App()
