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




// SOLUCION:


/* En Javascript tenemos las siguientes estructuras de datos nativas con sus respectivos metodos de creacion, insercion, borrrado, actualizacion y orden.
1- Array        <-- Estructura ordenada de datos (string, numbers, arrays, objetos, etc)
2- Objetos      <-- Coleccion Clave - Valor tipo diccionario
3- MAP          <-- Coleccion clave - valor
4- SET          <-- Conjunto de valores unicos
*/


/////////////////////////// ARRAY /////////////////////////
console.log('Array: ')

// Creacion
let familiares = ['Imanol', 'Sebastian', 'Carolina', 'Alexis']
console.log(familiares)

// Insercion
familiares.push('Pablo')
console.log(familiares)

// Actualizacion
familiares[0] = 'Santino'
console.log(familiares)

//Borrado
familiares.pop()
console.log(familiares)

// Ordenar
familiares.sort((a, b) => a - b)
console.log(familiares)

/////////////////////////// OBJETOS /////////////////////////
console.log('OBJETO: ')

// Creacion
let pais = { nombre: 'Argentina', poblacion: 50000000 }
console.log(pais)

// Insercion
pais.capital = 'Buenos Aires'
console.log(pais)

// Actualizacion
pais.poblacion = 47000000
console.log(pais)

// Borrado
delete pais.capital
console.log(pais)

/////////////////////////// MAP /////////////////////////
console.log('MAP: ')

// Creacion
let mapa = new Map([
    ['uno', 1],
    ['dos', 2],
])
console.log(mapa)

// Insercion
mapa.set('tres', 3)
console.log(mapa)

// Actualizacion
mapa.set('uno', 0)
console.log(mapa)

// Borrado
mapa.delete('uno')

// Ordenado
// let nuevoMapaOrdenado = new Map([...mapa.entries().sort()])

/////////////////////////// SET /////////////////////////
console.log('SET: ')

// Creacion
let conjuntoSet = new Set([5, 2, 3, 4, 1])
console.log(conjuntoSet)

// Insercion
conjuntoSet.add(0)
console.log(conjuntoSet)

// Borrado
conjuntoSet.delete(5)
console.log(conjuntoSet)

// Actualizacion
conjuntoSet.delete(1)
conjuntoSet.add(10)
console.log(conjuntoSet)


/*
    * DIFICULTAD EXTRA(opcional):
* Crea una agenda de contactos por terminal.
* - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
    * los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no numéricos y con más de 11 dígitos.
 * (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
 */

console.log(`\n\n\n\n\n\n\n\n Bienvenido a tu Agenda de Contactos`)

const readline = require('readline')
const { stdin: input, stdout: output } = require('node:process')

const rl = readline.createInterface({ input, output })


function programa() {


    const agenda = [
        { id: 1, nombre: 'Imanol', numero: 3624701656 },
        { id: 2, nombre: 'Lucas', numero: 3624156585 },
        { id: 3, nombre: 'Sebastian', numero: 3624255554 },
    ]
    // console.log()

    function menu() {
        rl.question(`
                Selecciona el tipo de operaciono a realizar:
                1 <-- para Ver Agenta Completa
                2 <-- para Agendar un nuevo contacto
                3 <-- para Actualizar un Contacto
                4 <-- para Eliminar un Contacto
                5 <-- para Buscar un Contacto Especifico
                0 <-- Cerrar menu/programa
                `, (respuesta) => {

            switch (respuesta) {
                case '1':
                    mostrarAgenda()
                    break;
                case '2':
                    crearNuevoContacto()
                    break;
                case '3':
                    actualizarContacto()
                    break;
                case '4':
                    eliminarContacto()
                    break;
                case '5':
                    buscarContacto()
                    break;
                case '0':
                    console.clear()
                    console.log('Menu/programa finalizado !!!!')
                    rl.close()
                default:
                    'No has seleccionado ninguna de las opciones !'
                    rl.question('')
            }
        })
    }
    menu()


    const mostrarAgenda = () => {
        console.clear()
        console.log(`Agenda completa: `)
        console.log(agenda)

        rl.question('Presione (m) para volver al menu: ', (res) => { if (res === 'm') return menu() })
    }

    const crearNuevoContacto = () => {
        console.clear()
        console.log(agenda)
        rl.question('Escribe Nombre del nuevo contaco: ', (nombre) => {
            rl.question('Ahora escribe el Numero: ', (numero) => {
                agenda.push({ id: agenda.length + 1, nombre: nombre, numero: Number(numero) })
                console.log('Contacto Agendado:  \n ', agenda)


                // console.cls()
                rl.question('Presione (m) para volver al menu: ', (res) => {
                    if (res === 'm') {
                        menu()
                    }
                })
            })
        })


    }

    const actualizarContacto = () => {
        console.clear()
        console.log('\n Agenda de Contactos:  \n', agenda.map(a => `id: ${a.id}, nombre: ${a.nombre}, numero: ${a.numero}`))
        rl.question('Selecciona el ID del contacto que quieres Actualizar: ', (id) => {
            let idContact = Number(id)
            agenda.map(contact => {
                if (contact.id === Number(idContact)) {
                    console.clear(), console.log(`\n Contacto a ser Actualizado: id: ----> id: ${contact.id}, nombre: ${contact.nombre}, numero: ${contact.numero}`)

                    rl.question('Escribe Nuevo Nombre del Contacto: ', (nombreActualizado) => {
                        rl.question('Escribe Nuevo Numero del Contacto: ', (numeroActualizado) => {
                            contact.nombre = nombreActualizado
                            contact.numero = numeroActualizado
                            // agenda.push({ id: contact.id, nombre: contact.nombre, numero: contact.numero })
                            mostrarAgenda()
                        })
                    })
                }
            })
        })

    }

    const eliminarContacto = () => {
        console.clear()
        console.log('\n Agenda de Contactos:  \n', agenda.map(a => `id: ${a.id}, nombre: ${a.nombre}, numero: ${a.numero}`))

        rl.question('Selecciona el (ID) del Contacto a Eliminar: ', (resId) => {

            let contactToDelete = agenda.findIndex(i => agenda.id === Number(resId) - 1)
            agenda.splice(contactToDelete, 1)


            rl.question('Presione (m) para volver al menu: ', (res) => {
                if (res === 'm') {
                    menu()
                }
            })
        })
    }

    const buscarContacto = () => {
        console.clear()

        rl.question('Escriba el Nombre o Numero del contacto Agendado a Buscar: ', (toSearch) => {

            const buscarContacto = agenda.find(c =>
                c.nombre.toLowerCase() == toSearch.toLowerCase() ||
                c.numero == Number(toSearch)
            )

            if (buscarContacto) {
                console.log('Contacto Encontrado: ', buscarContacto)
            } else {
                console.log('No se ha encontrado ningun Contacto.')
            }



            rl.question('Presione (m) para volver al menu: ', (res) => {
                if (res === 'm') {
                    menu()
                }
            })
        })

    }
}


programa()





