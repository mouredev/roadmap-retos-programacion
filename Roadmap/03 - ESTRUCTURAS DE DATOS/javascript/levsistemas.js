/*# #03 ESTRUCTURAS DE DATOS
> #### Dificultad: Media | Publicación: 15/01/24 | Corrección: 22/01/24

## Ejercicio

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
 
#### Tienes toda la información extendida sobre el roadmap de retos de programación en **[retosdeprogramacion.com/roadmap](https://retosdeprogramacion.com/roadmap)**.

Sigue las **[instrucciones](../../README.md)**, consulta las correcciones y aporta la tuya propia utilizando el lenguaje de programación que quieras.

> Recuerda que cada semana se publica un nuevo ejercicio y se corrige el de la semana anterior en directo desde **[Twitch](https://twitch.tv/mouredev)**. Tienes el horario en la sección "eventos" del servidor de **[Discord](https://discord.gg/mouredev)**.
*/

// ESTRUCTURAS SOPORTADAS

// ARRAY O ARREGLOS

let myArray1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

console.log("\nArray númerico:", myArray1)

let myArrayString = ["Pedro", "Marcos", "Horacio", "Carlos", "Mauricio"]

console.log("\nArray de nombres:", myArrayString)

console.log("\nMi array organizado:", myArrayString.sort())

//Agregando un elemento al array
myArray1.push(10)

console.log("\nElemento al final:", myArray1)

myArray1[5] = 16

console.log("\nElemento posicion 4 modificado:", myArray1)

//Eliminando el primer elemento e imprimiendo en pantalla
myArray1.shift()

console.log("\nEliminado el primer elemento:", myArray1)

//Elimina el último elemento indizado del arreglo
myArray1.pop()

console.log("\nEliminado el último elemento:", myArray1)

//Agregar elementos al principio del array
myArray1.unshift("Brais", "Moure", "Developer")

console.log("\nAgregado un elemento al principio:", myArray1)

//Realizar un recorrido de los indices comenzando en el indice 2 hasta la posicion 4
const result = myArray1.slice(2, 5)

//Realizar un recorrido de los indices comenzando en el indice 1 hasta la posicion 6
console.log("\nVisualizando algunos elementos del array:", myArray1.slice(1, 7))
console.log("\nVisualizando otros elementos del array:", result)

//Eliminar a partir de la posicion o indice 2 del array en ADELANTE hasta la posicion o indice 4 incluido
console.log("\nModo splice:", myArray1.splice(2, 4))

//Objeto
let mySelf = { name: "Leandro", age: 38 }

console.log("\nEstilo:", mySelf)

//Objeto - Agregar

mySelf.country = "Argentina"

console.log("\nAgregando pais:", mySelf)

//Objeto - Eliminar

delete mySelf.age

console.log("\nEliminando edad:", mySelf)

//Objeto - Actualizar

mySelf.name = "SlipKnot"

console.log("\nModificando nombre:", mySelf)

let myNewSet = new Set()
myNewSet = new Set(["Brais", "Moure", 38, "Brais"])

console.log("\nNuevo set:", myNewSet)

myNewSet.add("Mouredev.pro")

console.log("\nAgregando string al set:", myNewSet)

myNewSet.delete("Brais")

console.log("\nEliminando la palabra Brais del set:", myNewSet)

console.log("\nEl set contiene la palabra: Moure...", myNewSet.has("Moure"))

console.log("\nVerificando tamaño:", myNewSet.size)

//Convertir el Set en Array
let myArrayOfSet = Array.from(myNewSet)

console.log("\nSet convertido a array:", myArrayOfSet)

//Convertir Array "nuevamente" en un Set
myNewSetAgain = new Set(myArrayOfSet)

console.log("\nConvertir array en set de nuevo:", myNewSetAgain)

myNewMap = new Map([["name", "Brais"], ["email", "braismoure@gmail.com"], ["age", 37]])

console.log("\nNuevo map:", myNewMap)

//Agregados 2 items (clave, valor) al set myNewMap
myNewMap.set("alias", "mouredev")
myNewMap.set("name", "Brais Moure")

console.log("\nDos nuevos items clave y valor:", myNewMap)

myNewMap.get("alias")
myNewMap.has("Hello World")

myNewMap.delete("alias")

console.log("\nBorrado alias:", myNewMap)

console.log("\nTamaño del mapa:", myNewMap.size)

//Limpiar completamente el Map myNewMap
myNewMap.clear()

//DIFICULTAD EXTRA
let nombre
let telefono
let contacto

let contactos = []
const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});

function menu() {
    console.log("\nMenú de opciones:\n")
    readline.question("1) Agregar un nuevo contacto.\n2) Editar un contacto.\n3) Eliminar un contacto.\n4) Buscar un contacto o registro.\n5) Salir.\n\nSelecciona una opción del menú: ", respuesta => {
        switch (respuesta) {
            case "1": {
                addContact()
                break;
            }
            case "2": {
                editPerson()
                break;
            }
            case "3": {
                deleteContact()
                break;
            }
            case "4": {
                findContact()
                break;
            }
            case "5": {
                exit()
                process.exit()
            }
            default:
                console.log("opción incorrecta, regresando al menú")
                menu()
        }
    })
}

function addContact() {
    function person() {
        readline.question("¿Cual es tu nombre? ", respuesta => {
            nombre = respuesta
            phone()
        })
    }

    function phone() {
        readline.question("¿Tu número de telefono? ", respuesta => {
            if (respuesta.length <= 10) {
                telefono = parseInt(respuesta)
                if (isNaN(telefono)) {
                    console.log(`¡La respuesta ${telefono} no fue un número de teléfono, digita solo números!`)
                    phone()
                } else if (typeof telefono === 'number') {
                    telefono = telefono.toString()
                    addContactResult()
                }
            } else {
                console.log(`Solo se acepta una cantidad máxima de 10 dígitos (se ingresaron ${respuesta.length} dígitos)`)
                phone()
            }
        })
    }

    person()
}

function addContactResult() {
    contactos.push([nombre, telefono])
    console.log("¡Contacto agendado exitosamente!", contactos)
    menu()
}

function editPerson() {
    if (contactos.length === 0) {
        console.log("No hay contactos agendados.")
        menu()
    } else {
        console.log("\nElige el contacto a editar: \n")
        contactos.map((contacto, index) => {
            console.log(index, contacto)
        })

        readline.question("\nNúmero de contacto: ", respuesta => {
            contacto = parseInt(respuesta)
            if (isNaN(contacto)) {
                console.log("\nDato inválido, por favor selecciona un número")
                editPerson()
            } else if (typeof contacto === 'number') {
                if (contacto >= 0 && contacto <= contactos.length - 1) {
                    editName()
                } else {
                    console.log("\nEl número ingresado para editar el contacto no es valido, verificá...")
                    editPerson()
                }
            }
        })

        function editName() {
            readline.question("Edita Nombre: ", respuesta => {
                nombre = respuesta
                editPhone()
            })
        }

        function editPhone() {
            readline.question("Edita Telefono: ", respuesta => {
                if (respuesta.length <= 10) {
                    telefono = parseInt(respuesta)
                    if (isNaN(telefono)) {
                        console.log(`\n¡La respuesta ${telefono} no fue un número de teléfono, digita solo números!`)
                        editPhone()
                    } else if (typeof telefono === 'number') {
                        telefono = telefono.toString()
                        contactos[contacto] = [nombre, telefono]
                        console.log(contactos)
                        console.log("\nRegistro actualizado exitosamente número " + contacto)
                        menu()
                    }
                } else {
                    console.log(`\nSolo se acepta una cantidad máxima de 10 dígitos (se ingresaron ${respuesta.length} dígitos)`)
                    editPhone()
                }
            })
        }
    }
}

function deleteContact() {
    if (contactos.length === 0) {
        console.log("No hay contactos agendados.")
        menu()
    } else {
        console.log("\nElige el contacto: \n")
        contactos.map((contacto, index) => {
            console.log(index, contacto)
        })

        readline.question("\nNúmero de contacto: ", respuesta => {
            contacto = respuesta
            removeContact()
        })

        function removeContact() {
            console.log("\nEl contacto seleccionado para eliminar es:", contactos[contacto])
            contactos.splice(contacto, 1)
            console.log("\nCantidad de contactos:", contactos)
            menu()
        }
    }
}

function findContact() {
    console.log(contactos)
    if (contactos.length === 0) {
        console.log("\nNo hay contactos agendados.\n")
        menu()
    } else {
        readline.question("\nEscribe lo que estas buscando (parte de un nombre y/o números): ", respuesta => {
            contacto = respuesta
            contact()
        })

        function contact() {
            nuevoResultado = new Set()
            contactos.find(elemento => {
                if(typeof elemento === 'object') {
                    elemento.find(indice => {
                        if(indice.includes(contacto)) {
                            nuevoResultado.add(elemento)
                        }
                    })
                }
            })

            console.log("\nResultados filtrados sin repetir:\n")
            Array.from(nuevoResultado).map(item => console.log(item))

            console.log('\nCantidad:', nuevoResultado.size, '\n')
            
            if (nuevoResultado.size === 0) {
                console.log(`¡No se ha encontrado el resultado que buscas para: ${contacto}!`)
            }
            if (nuevoResultado.size === 1) {
                console.log(`¡Con referencia a "${contacto}", se ha encontrado ${nuevoResultado.size} coincidencia!`)
            } else if (nuevoResultado.size > 1) {
                console.log(`¡En referencia a "${contacto}", se han encontrado ${nuevoResultado.size} coincidencias!`)
            }

            menu()
        }
    }
}

function exit() {
    readline.close()
}

menu()