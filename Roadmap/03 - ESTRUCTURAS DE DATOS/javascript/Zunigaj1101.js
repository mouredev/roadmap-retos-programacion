/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto
 *   en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
*/

// Arrays

let myArray = [1,2,3,4,5]
let myArray2 = new Array (6,7,8,9)

// Insercion
myArray.push(6,7) // se añade al final del array
myArray.unshift (1,10) // se añade al inicio del array

// Actualización
myArray[1] = 100 // actualiza el valor segun su indice
myArray.splice(1,1,500,2) // indico el indice, cuantos valores elimino, y cuantos añado 

// Ordenacion
myArray.sort ()  // convierte los elementos a cadenas y los ordena en orden lexicográfico
myArray.sort ((a, b)=> b - a) // orden descendente

// Borrar
myArray.splice (2,3) // eliminar elementos especificos
myArray.shift() // elimina el primer elemento de una array
myArray.length = 4 // elimina los elementos de una array hasta dejar solo indice especificado
myArray = [] // vacia el array

console.log (myArray)
console.log (myArray2)

// Objects 

let myObjects = {name: "Jose", age: 30, alias: "Chee"}
let myObjetcs2 = new Object ({name:'Juan', age:29})

// Inserción
myObjects.email = 'Che@gmail.com' // añado un elemento ya que no exite la clave

// Actualización
myObjects.name = 'Juanito' // acutalizo la clave existente

// Eliminacion
delete myObjects.age // elimina el par clave:valor

console.log (myObjects)
console.log (myObjects.name)
console.log (typeof myObjetcs2)

// Maps 

let myMap = new Map ([['alias', 'Che'], ['name', 'Juan'] ])

// Insercion
myMap.set ("age", 30) // añade ya que no exite la clave

// Actualizacion 
myMap.set ('age', 20) // actualiza ya que existe la clave

// Borrar
myMap.delete ('age') // elimina mediate la clave

console.log (myMap)
console.log (typeof myMap)

// Sets

// Isercion
let mySet = new Set([1,3,4,6,7,2])
mySet.add (10)
mySet.add (2) // no se añade porque el valor ya existe
mySet.add (1)
mySet.add (myMap)

// Acutalizacion y Delete
// no se acualiza diretamente, se borra y se añade el elemento

if (mySet.has(3)) {
    mySet.delete(3); // elimina el elemento de un Set
    mySet.add(30);
}

console.log (mySet)

// WeakMap

let myWeakMap = new WeakMap ()
myWeakMap.set(myObjects, 'Nuevo valor')

console.log (myWeakMap.get(myObjects))

// WeakSet

let myWeakSet = new WeakSet ()
myWeakSet.add (myMap)

console.log (myWeakSet.has(myMap))


// * DIFICULTAD EXTRA (opcional):
// * Crea una agenda de contactos por terminal.
// * - Debes implementar funcionalidades de búsqueda, inserción, actualización
// *   y eliminación de contactos.
// * - Cada contacto debe tener un nombre y un número de teléfono.
// * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
// *   y a continuación los datos necesarios para llevarla a cabo.
// * - El programa no puede dejar introducir números de teléfono no númericos y con más
// *   de 11 dígitos (o el número de dígitos que quieras).
// * - También se debe proponer una operación de finalización del programa.

let agenda = new Array ()
agenda.push({name:'Jose', phone:123456789})

const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const agregarContacto = () => {
    rl.question ('Nombre del contacto: ', (nameCon) => {
        if (/^.{1,50}$/.test(nameCon)) {
            console.log ('\nNombre guardado')
            rl.question ('Numero del contacto: ', (phoneCon) => {
                if (/^[0-9]{1,11}$/.test(phoneCon)) {
                    agenda.push ({name:nameCon, phone:parseInt(phoneCon)})
                    console.log ('\n==================')
                    console.log ('Contacto guardado')
                    console.log ('==================\n')
                } else {
                    console.log ('\nNumero de contacto invalido\n')
                }
                mostrarMenu ();
            })
        } else {
            console.log ('\nNombre invalido\n')
            mostrarMenu ();
        }
    })
}

const buscarContacto = () => {
    rl.question ('Nombre del contacto: ', (nameCon) => {
        if (agenda.some(c => c.name === nameCon)) {
            let contacto = agenda.find (c => c.name === nameCon)
            console.log ('')
            console.log (contacto)
        } else {
            console.log (`\n${nameCon} no esta registrado.\n`)
        }
        mostrarMenu();
    });
}

const actualizarContacto = () => {
    rl.question ('Buscar contacto a actualizar: ', (nameCon) => {
        if (agenda.some (c => c.name === nameCon)) {
                console.log ('Contacto encontrado')
            rl.question ('Nuevo nombre de contacto: ', (nameConNuevo) => {
                if (/^.{1,50}$/.test(nameConNuevo)) {
                    rl.question ('Nuevo numero de telefono: ', (phoneCon) => {
                        if (/^[0-9]{1,11}$/.test(phoneCon)) {
                            let contactoIdx = agenda.findIndex (c => c.name === nameCon)
                            agenda.splice (contactoIdx, 1, {name: nameConNuevo, phone: parseInt(phoneCon)})
                            console.log ('\nContacto actualizado:')
                            console.log (agenda[contactoIdx])
                            mostrarMenu();
                        } else {
                            console.log ('\nNumero de contacto invalido\n')
                            mostrarMenu();
                        }
                    })
                }
            })              
        } else {
            console.log ('\nContacto invalido\n')
            mostrarMenu();
        }
    });
}

const eliminarContacto = () => {
    rl.question ('Bucar el contacto a eliminar: ', (nameCon) => {
        if (agenda.some(c => c.name === nameCon)) {
            let contactoIdx = agenda.findIndex (c => c.name === nameCon)
            rl.question(`Escriba "S" para elminar el contacto: `, (value) =>{
                if (value === 'S' || value === 's') {
                    agenda.splice(contactoIdx, 1)
                    console.log ('\nContacto ' + nameCon + ' eliminado.')
                    mostrarMenu();
                } else {
                    console.log ('\nNo se elimino el contacto')
                    mostrarMenu();
                }
            })
        } else {
            console.log (`\nEl Contacto ${nameCon} no existe`)
            mostrarMenu ();
        }
    })
}

const mostrarMenu = () => {
    console.log ("\n1. Mostrar Catalogo")
    console.log ("2. Buscar contacto")
    console.log ("3. Agregar Contacto")
    console.log ("4. Actualizar Contacto")
    console.log ("5. Eliminar Contacto")
    console.log ("0. Salir")
    rl.question ("Selecione una opcion: ", opciones)
}

function opciones(option) {
    switch (parseInt(option)){
        case 1:
            console.table (agenda)
            break;
        case 2:
            buscarContacto();
            return
        case 3:
            agregarContacto ();
            return;
        case 4:
            actualizarContacto ();
            return;
        case 5:
            eliminarContacto();
            return;
        case 0:
            console.log ('\n==================')
            console.log (' Agenda Cerrada')
            console.log ('==================\n')
            rl.close();
            return;
        default:
            console.log ('Opcion incorrecta, seleccione una opcion del 1 al 6.')
            break;
    }
    mostrarMenu();
}

mostrarMenu();