/**
 * Reto de programación #03 - javaScript
 * Autor: Yoandy Doble Herrera
 * Fecha: 08/12/2024
 */

/*
 * EJERCICIO:
 * [x] Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * [x] Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * [-] Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * [-] Cada contacto debe tener un nombre y un número de teléfono.
 * [-] El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * [-] El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * [-] También se debe proponer una operación de finalización del programa.
 */

/* 1- Estructura de dato: Array */
let equipoBaseball = [
  "Pinar del Río",
  "Mayabeque",
  "Artemisa",
  "Industriales",
  "Matanzas",
  "Cienfuegos",
  "Villaclara",
  "Ciego de Ávila",
  "Holguín",
  "Granma",
  "Sancti Spiritus",
  "Santiago de Cuba",
  "Guantánamo",
  "Camagüey",
]
console.log("Array", equipoBaseball)
//inserción, borrado, actualización y ordenación

//Insertar elemento en array al final
equipoBaseball.push("Isla de la Juventud")
console.log("Array con nuevo elemento al final", equipoBaseball)

//Insertar elemento al principio en array
let newArrayLength = equipoBaseball.unshift("Chicago White Sox")
console.log("Array con nuevo elemento al incio", equipoBaseball, "\nNueva longitud: ", newArrayLength)

//Eliminar elemento en array al final
let elementoRemoved = equipoBaseball.pop()
console.log("Array con nuevo elemento al final", equipoBaseball, "\nElemento borrado al final: ", elementoRemoved)

//Eliminar elemento al principio en array
let elementShifted = equipoBaseball.shift()
console.log("Array con nuevo elemento al incio", equipoBaseball, "\nElemento borrado al inicio: ", elementShifted)

//Actualizar elemento en el array
equipoBaseball[0] = "Team Challenger"
console.log("Array con nuevo elemento al incio actualizado", equipoBaseball)

//Ordenación Sort in place
console.log("Elementos ordenados:", equipoBaseball.sort())

/* 2- Estructura de dato: Set */
const palabrasUnicas = new Set(["laptop", "boy", "boy", "keyboard", "javaScript", "flute"])
console.log(palabrasUnicas) //no se muestran elementos repetidos

//Insertar elemento en Set
palabrasUnicas.add("car")
console.log("Nuevo elemento en Set insertado al final", palabrasUnicas)

//Eliminar elemento en Set
let apearElem = palabrasUnicas.delete("boy")
console.log("Elimina elemento: (boy) true si aparece en el Set ", palabrasUnicas, "\nrespuesta:", apearElem)

//Actualizar elemento en el array
/* No es posible porque son elementos únicos */

//Ordenación Sort in place
let palabrasArray = Array.from(palabrasUnicas)
palabrasArray.sort()
console.log("Set convertido en array para ordanar\n", palabrasArray)
let newSetPalabras = new Set(palabrasArray)
console.log("Nuevo SET ordenado:\n", newSetPalabras)

/* 3- Estructura de dato: Map */
const misContactos = new Map([
  ["Yoandy", 5312365478],
  ["Mabel", 5365897452],
  ["Ariana", 548793112125],
])
console.log(misContactos)

//inserción, borrado, actualización y ordenación
// Insertar tupla
misContactos.set("Barbarita", 5369874123625)
console.log("ELemento insertado al MAP", misContactos)

// Eliminar por key
misContactos.delete("Mabel")
console.log("Eliminada key: Mabel", misContactos)

//Actualizar value en Set
misContactos.set("Yoandy", 5989325789)
console.log("Actulizado valor número de teléfono key: Yoandy", misContactos.get("Yoandy"))

// Ordenacion
let arrayEnOrden = [...misContactos].sort((a, b) => a[0].localeCompare(b[0]))
console.log(arrayEnOrden)
let newContactos = new Map(arrayEnOrden)
console.log(newContactos)

/* 4- Estructura de dato: Object */
let auto = {
  brand: "Dodge Challenger",
  price: 25000,
  color: "Black",
  date: "08/12/2024",
  isnew: true,
  owner: "Yoandy Doble Herrera",
}

// Insertar propiedad a Objeto
auto["seller"] = "Rick Ortiz"
console.log("Nuevo elemento al Objeto", auto)

//borrado propiedad a Objeto
delete auto.color
console.log("Propiedad color eliminada de Objeto", auto)

// Actualización de propiedades
auto["seller"] = "Rick Ortiz Martínez"
console.log(auto)

// Ordenación
/* Utilizando sort de Array impacto en eficiencia */
console.time()
const autoArray = Object.keys(auto).sort()
//console.log(autoArray)

const objCar = {}
autoArray.forEach((value) => {
  objCar[value] = auto[value]
})
console.log(objCar)
console.timeEnd()

/* Utilizar un mapa más rápido*/
console.time()
const mapOrdenado = new Map()
for (clave in auto) {
  mapOrdenado.set(clave, auto[clave])
}

for (const [clave, valor] of mapOrdenado) {
  console.log(clave, valor) //aplicar ordenación
}
console.timeEnd()

/**
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * [-] Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * [x] Cada contacto debe tener un nombre y un número de teléfono.
 * [x] El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * [x] El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * [x] También se debe proponer una operación de finalización del programa.
 */

const readline = require("node:readline")
const { stdin: input, stdout: output } = require("node:process")
const rl = readline.createInterface({ input, output })

const libretaContactos = new Map()

/**
 * Menú interactivo con readline para Proyecto ¡Agenda de Contactos!
 */
const menu = () => {
  console.info(
    `\nApp: ¡Agenda de contactos!
  1. Insertar contacto
  2. Eliminar contacto
  3. Buscar contacto
  4. Actualizar contacto
  5. Salir
  `
  )
  rl.question("Seleccione una opción -> ", (answer) => {
    switch (answer) {
      case "1":
        insertarContacto()
        break
      case "2":
        eliminarContacto()
        break
      case "3":
        buscarContacto()
        break
      case "4":
        actualizarContacto()
        break
      case "5":
        rl.close()
        break
      default:
        console.log("Opción inválida")
        menu()
    }
  })
}

/**
 * Insertar un contacto en la libreta de direcciones (void function)
 * Readline: nombre de contacto, un número de 11 dígitos
 */
const insertarContacto = () => {
  rl.question("Nombre del contacto -> ", (nombre) => {
    rl.question("Número del contacto -> ", (numero) => {
      if (String(nombre).length === 0 && String(numero).length === 0) {
        console.log("Error debes insertar un nombre de contacto y un número de telefono.")
      } else if (String(nombre).length === 0) {
        console.log("Error debes insertar un nombre de contacto.")
      } else if (String(numero).length === 0) {
        console.log("Error debes insertar un número de telefono.")
      } else if (isNaN(parseInt(numero))) {
        console.log("Error debes insertar un número de telefono.")
      } else if (String(numero).length > 11 || String(numero).length < 11) {
        console.log("Error el número de teléfono debe ser de solo 11 dígitos")
      } else {
        const contactUser = { id: libretaContactos.size + 1, nombre: nombre, numero: numero }
        libretaContactos.set(contactUser.id, contactUser)
        console.log(`Contacto agregado\nNombre: ${nombre}\nNúmero de teléfono: ${numero}`)
      }
      menu()
    })
  })
}

/**
 * Eliminar un contacto de la libreta de contactos por el nombre
 */
const eliminarContacto = () => {
  rl.question("Nombre del contacto a eliminar -> ", (nombre) => {
    let isDeleted = false
    if (String(nombre).length === 0) {
      console.log("Error debes insertar un nombre de contacto.")
    } else if (libretaContactos.size === 0) {
      console.log("Error libreta de contactos vacía.")
    } else {
      for (const [key, value] of libretaContactos) {
        if (value.nombre === nombre) {
          libretaContactos.delete(key)
          console.info(`Contacto eliminado.\nNombre: ${value.nombre}\nNúmero de teléfono: ${value.numero}`)
          isDeleted = true
          break
        }
      }
      if (!isDeleted) {
        console.log("Contacto no encontrado.")
      }
    }
    menu()
  })
}

/**
 * Buscar un contacto en la libreta telefónica
 */
const buscarContacto = () => {
  //TODO Buscar un contacto por nombre
  rl.question("Inserte el nombre del contacto -> ", (answer) => {
    let isContact = false
    if (String(answer).length === 0) {
      console.log("Error debes insertar un nombre para buscar.")
    } else if (libretaContactos.size === 0) {
      console.log("Error libreta de contactos vacía.")
    } else {
      for (const value of libretaContactos.values()) {
        if (value.nombre === String(answer)) {
          console.info(`Contacto encontrado.\nNombre: ${value.nombre}\nNúmero de teléfono: ${value.numero}`)
          isContact = true
          break
        }
      }
      if (!isContact) {
        console.log("Contacto no encontrado.")
      }
    }
    menu()
  })
}

/**
 * Actualizar un contacto en la libreta telefónica
 */
const actualizarContacto = () => {
  //TODO Actualizar número de teléfono de contacto
}

menu()
