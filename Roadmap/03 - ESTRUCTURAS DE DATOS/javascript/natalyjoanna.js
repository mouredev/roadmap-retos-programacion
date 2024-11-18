
Arreglos
let arrayString = ["Morado", "Rosa", "Verde", "Azul", "Rojo"]
let arrayNumeros = [ 2021, 2023, 2022, 2020, 2024]
let arrayMixto = ["Chico", 12, false, "Mediano", true, 16, "Grande", 23, true]

console.log("Lista de strings", arrayString)
console.log("Lista de numeros", arrayNumeros)
console.log("Lista de mixtos", arrayMixto)

// Arreglos | Insertar dato al final de una lista
arrayString.push("Naranja")
console.log("Lista actualizada string: ", arrayString)

// Arreglos | Insertar dato al principio de una lista
arrayMixto.unshift("WTF")
console.log("Lista actualizada mixto: ", arrayMixto)

// Arreglos | Insertar dato en una posicion en concreto
arrayString.splice(2,1,"Dorado")
console.log("Lista actualizada string con Dorado: ", arrayString)

// Arreglos | Actualizar dato especifico de la lista
arrayString[3] = "Azul Marino"
console.log("Dato actualizado string: ", arrayString)


// Arreglos | Eliminar dato ultima de una lista
arrayNumeros.pop()
console.log("Lista actualizada numeros: ", arrayNumeros)

// Arreglos | Eliminar dato primero de una lista
arrayNumeros.shift()
console.log("Lista actualizada numeros: ", arrayNumeros)

// Arreglos | Concatenar dos listas
let concatenado = arrayString.concat(arrayNumeros)
console.log("Concatenado: ", concatenado)

// Arreglos | Ubicar dato especifico en una lista por su indice
let index = 4
console.log(`En el indice ${index} se encuentra el elemento ${arrayMixto.at(index)} `)

// Arreglos | Ordenar lista
let listaOrdenata = arrayNumeros.sort()
console.log("Lista ordenada numeros: ", listaOrdenata)

// Objetos

let objeto = {
  titulo: "Deadpool & Wolverine",
  genero: "Accion",
  año: 2024
}
console.log("Objeto: ", objeto)
console.log("Genero de la pelicula: ", objeto.genero)
objeto["director"] = "Shawn Levy" // Agregar dato
console.log("Objeto actualizado: ", objeto)
objeto["genero"] = "Comedia" // Modificar valor
console.log("Objeto genero actualizado: ", objeto)
// Set

let set = new Set()
set.add(1)
set.add(2)
set.add(3)
set.add(1) // No añade datos repetidos

console.log("Set: ", set)
console.log("Set actualizado: ", set)
set.delete(1)
console.log("Set actualizado: ", set)
set.clear() // Limpiar set

// DIFICULTAD EXTRA

let contacto = {}

const readline = require('readline')
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

function agendaMenu() {
  console.log("1. Mostrar todos los contactos")
  console.log("2. Buscar contacto")
  console.log("3. Insertar contacto")
  console.log("4. Actualizar contacto")
  console.log("5. Eliminar contacto")
  console.log("6. Salir\n")
  rl.question("Elige una opcion: ", (opcion) => {
    switch (opcion) {
      case '1':
          mostrarContactos();
          break;
      case '2':
          buscar();
          break;
      case '3':
          insertar();
          break;
      case '4':
          actualizar();
          break;
      case '5':
          eliminar();
          break;
      case '6':
          salir();
          break;
      default:
          console.log("Debes introducir un valor.");
          agendaMenu();
          break;
  }
  })
}

function mostrarContactos() { 
  for(con in contacto) {
    console.log(`Contactos: Nombre: ${con} - Telefono: ${contacto[con]}\n`)
  }
  agendaMenu();
}


function buscar() {
  rl.question("Nombre del contacto: ", (nombre) => {
    if (contacto[nombre]) {
      console.log(`Contacto encontrado: ${nombre} - ${contacto[nombre]}\n`)
    } else {
      console.log("No se encontro el contacto\n")
    }
    agendaMenu()
  })
}

function insertar() {
  rl.question("Nombre del nuevo contacto: ", (nombre) => {
    rl.question("Telefono del nuevo contacto: ", (telefono) => {
      if(validarTelefono(telefono)) {
        contacto[nombre] = telefono
        console.log("Se agrego el contacto\n")
      } else {
        console.log("Numero de telefono no valido\n")
        agendaMenu()
      }
      agendaMenu()
    })
  })
}

function actualizar() {
  rl.question("Nombre del contacto a actualizar: ", (nombre) => {
    if(contacto[nombre]) {
      rl.question("Actualizar telefono: ", (telefono) => {
        if (validarTelefono(telefono)) {
          contacto[nombre] = telefono
          console.log("Se actualizo el contacto\n")
        } else {
          console.log("Numero de telefono no valido\n")
          agendaMenu()
        }
      })
    } else {
      console.log("No se encontro el contacto\n")
    }
    agendaMenu()
  })
}

function eliminar() {
  rl.question("Nombre del contacto: ", (nombre) => {
    if (contacto[nombre]) {
      delete contacto[nombre]
      console.log("Se elimino el contacto\n")
    } else {
      console.log("No se encontro el contacto\n")
    }
    agendaMenu()
  })
}

function salir() {
console.log("Saliendo...");
 rl.close()
}

function validarTelefono(telefono) {
  const regex = /^\d{10}$/;
  return regex.test(telefono);
}

agendaMenu()