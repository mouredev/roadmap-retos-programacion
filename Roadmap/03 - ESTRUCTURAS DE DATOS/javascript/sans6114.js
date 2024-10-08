/*
//==============================
// ARRAYS (LISTAS)
//==============================
const miArray = [1, 2, 3, 4];

console.log("=== ARRAY ORIGINAL ===");
console.log(miArray);

// 1. INSERCIÓN
// ----------------------------
// AL FINAL DEL ARRAY
miArray.push(5);
console.log("\n=== Inserción al final ===");
console.log(miArray);

// AL PRINCIPIO DEL ARRAY
miArray.unshift(0);
console.log("\n=== Inserción al principio ===");
console.log(miArray);

// EN UNA POSICIÓN ESPECÍFICA
miArray.splice(2, 0, 10);
console.log("\n=== Inserción en posición específica ===");
console.log(miArray);

// 2. BORRADO
// ----------------------------
// DEL FINAL DEL ARRAY
miArray.pop();
console.log("\n=== Borrado del final ===");
console.log(miArray);

// DEL PRINCIPIO DEL ARRAY
miArray.shift();
console.log("\n=== Borrado del principio ===");
console.log(miArray);

// DE UNA POSICIÓN ESPECÍFICA
miArray.splice(2, 1);
console.log("\n=== Borrado en posición específica ===");
console.log(miArray);

// 3. ACTUALIZACIÓN
// ----------------------------
miArray[0] = 100;
console.log("\n=== Actualización del primer elemento ===");
console.log(miArray);

// 4. ORDENACIÓN
// ----------------------------
miArray.sort();
console.log("\n=== Ordenación del array ===");
console.log(miArray);

//==============================
// OBJETOS
//==============================
const miObjeto = {
    creacion: '',
    nombre: 'objeto uno',
    utilidad: 'ninguna'
};

console.log("\n=== Objeto Original ===");
console.log(miObjeto);

// 1. INSERCIÓN
// ----------------------------
miObjeto.apellido = 'Sosa';  // Inserción de nueva propiedad
miObjeto['actividad'] = 'cortar el pasto';  // Otra forma de insertar propiedad
console.log("\n=== Inserción en el objeto ===");
console.log(miObjeto);

// 2. BORRADO
// ----------------------------
delete miObjeto.apellido;  // Borrado de una propiedad
console.log("\n=== Borrado de la propiedad 'apellido' ===");
console.log(miObjeto);

// 3. ACTUALIZACIÓN
// ----------------------------
miObjeto.creacion = '31 de diciembre';  // Actualización de una propiedad existente
miObjeto['nombre'] = 'Santiago';  // Otra forma de actualizar una propiedad
console.log("\n=== Actualización del objeto ===");
console.log(miObjeto);

// 4. ORDENACIÓN (Por claves del objeto)
// ----------------------------
// Se ordenan las claves del objeto y se crea un nuevo objeto ordenado
let sortedKeys = Object.keys(miObjeto).sort();
let sortedObject = {};
sortedKeys.forEach(key => {
    sortedObject[key] = miObjeto[key];
});
console.log("\n=== Objeto con claves ordenadas ===");
console.log(sortedObject);

//==============================
// MAPAS
//==============================
const map1 = new Map();
map1.set('prop1', '1');
map1.set('prop2', 'hola');
map1.set('prop3', '10');

console.log("\n=== Mapa ===");
console.log(`Prop1: ${map1.get('prop1')}`);
console.log(`Tamaño del mapa: ${map1.size}`);

// BORRADO EN EL MAPA
map1.delete('prop3');
console.log("\n=== Mapa tras borrar prop3 ===");
console.log(`Tamaño del mapa: ${map1.size}`);

//==============================
// SETS
//==============================
let set = new Set([1, 2, 3, 4, 5, 6]);

console.log("\n=== Set ===");
console.log(set);

//==============================
// LISTA ENLAZADA (LINKED LIST)
//==============================
class Node {
    constructor(value, next = null) {
        this.value = value;
        this.next = next;
    }
}

class LinkedList {
    constructor() {
        this.head = null;
        this.tail = null;
    }

    append(value) {
        const newNode = new Node(value);
        if (!this.head) {
            this.head = newNode;
            this.tail = newNode;
        } else {
            this.tail.next = newNode;
            this.tail = newNode;
        }
    }

    traverse(callback) {
        let currentNode = this.head;
        while (currentNode !== null) {
            callback(currentNode);
            currentNode = currentNode.next;
        }
    }
}

const printNode = (node) => console.log(`valor: ${node.value}${node.next ? ` | next: ${node.next.value}` : ''}`);

const list = new LinkedList();
list.append(1);
list.append(2);
list.append(3);

console.log("\n=== Lista Enlazada ===");
list.traverse(printNode);
/*
/* DIFICULTAD EXTRA (opcional):
* Crea una agenda de contactos por terminal.
* - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
* - Cada contacto debe tener un nombre y un número de teléfono.
* - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
*   los datos necesarios para llevarla a cabo.
* - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
*   (o el número de dígitos que quieras)
* - También se debe proponer una operación de finalización del programa.
*/

const { select, input } = require('@inquirer/prompts');

let contactos = []
class Contacto {
    constructor(nombre, numero) {
        this.nombre = nombre;
        this.numero = numero;
    }
}
//FUNCION PARA OBTENER UN CONTACTO POR NOMBRE
const getByName = (nombre) => {
    return contactos.find(c => c.nombre === nombre)
}
//FUNCION PARA MOSTRAR EL MENÚ
const menu = async () => {
    const answer = await select({
        message: 'Select what do you want to do:',
        choices: (contactos.length > 0) ? [
            'Mis contactos',
            'Añadir contacto',
            'Buscar contacto',
            'Eliminar contacto',
            'Actualizar contacto',
            'Salir'
        ] : [
            'Añadir contacto',
            'Buscar contacto',
            'Eliminar contacto',
            'Actualizar contacto',
            'Salir'
        ]
    });
    return answer
}
//FUNCION PARA MOSTRAR QUE CAMPOS CAMBIAR
const changeContact = async () => {
    const optionsForChange = await select({
        message: 'What do you want to change?',
        choices: [
            'Nombre',
            'Numero'
        ]
    })
    return optionsForChange;
}

async function miAgenda() {
    let continuar = true;
    while (continuar) {

        try {
            const answer = await menu()
            if (!answer) {
                console.log('please put an option of menu')
                await menu()
            }

            switch (answer) {
                case 'Mis contactos':
                    //lógica para mostrar mis contactos de forma completa
                    if (contactos.length < 0) {
                        console.log('no tienes contactos')
                    } else {
                        contactos.forEach((c, index) => {
                            console.log(`contacto ${index + 1}, datos: ${c.nombre}, ${c.numero}`)
                        })
                    }
                    break;

                case 'Añadir contacto':
                    const contactName = await input({
                        message: 'Pon el nombre de tu nuevo contacto',
                        required: true
                    })
                    let contactNumber;
                    do {
                        contactNumber = await input({
                            message: `Pon el número de tu contacto con nombre: ${contactName}`,
                            required: true,
                        })
                        if (contactNumber.toString().length > 11 || isNaN(contactNumber)) {
                            console.log('Error! solo se aceptan caracteres numericos y menos de 11 caracteres.')
                        }
                        contactNumber = +contactNumber
                    } while (contactNumber.toString().length > 11 || isNaN(contactNumber));
                    const nuevoContacto = new Contacto(contactName, contactNumber)
                    contactos.push(nuevoContacto)
                    break;

                case 'Buscar contacto':
                    // Lógica para buscar contacto
                    const contactFind = await input({
                        message: 'Escribe el nombre del contacto que quieres buscar',
                        required: true
                    })
                    const contacto = getByName(contactFind)
                    if (!contacto) {
                        console.log('contacto no encontrado')
                    }
                    console.log(`Encontramos al contacto con nombre: ${contacto.nombre}, número: ${contacto.numero}`)
                    break;

                case 'Eliminar contacto':
                    // Lógica para eliminar contacto
                    const contactDelete = await input({
                        message: 'Escribe el nombre del contacto que quieres eliminar',
                        required: true
                    })
                    const contactoForDelete = getByName(contactDelete)
                    if (!contactDelete) {
                        console.log('contacto no encontrado')
                    }
                    contactos = contactos.filter(c => c.nombre !== contactoForDelete.nombre)
                    console.log(`contacto con nombre: ${contactoForDelete.nombre}, numero: ${contactoForDelete.numero} fue eliminado de tu lista de contactos correctamente.`)
                    break;

                case 'Actualizar contacto':
                    // Lógica para actualizar contacto
                    const contactForChange = await input({
                        message: 'Escribe el nombre del contacto que quieres actualizar',
                        required: true
                    })
                    const contactChange = getByName(contactForChange)
                    if (contactChange) {
                        const answer = await changeContact()
                        switch (answer) {
                            case 'Nombre':
                                const changeName = await input({
                                    message: `Escribe el nuevo nombre para el contacto, actualmente los datos son: ${contactChange.nombre}, ${contactChange.numero}`,
                                    required: true
                                })
                                contactos.map(c => {
                                    if (c.nombre === contactChange.nombre) {
                                        c.nombre = changeName
                                    }
                                    return c
                                })
                                break;

                            case 'Numero':
                                let changeNumber;
                                do {
                                    changeNumber = await input({
                                        message: `Escribe el nuevo numero para el contacto, actualmente los datos son: nombre: ${contactChange.nombre}, numero: ${contactChange.numero}(solo se aceptan caracteres numericos)`,
                                        required: true
                                    })

                                } while (isNaN(changeNumber));
                                const myChange = contactos.map(c => {
                                    if (c.nombre === contactChange.nombre) {
                                        c.numero = changeNumber
                                    }
                                    return c
                                })
                                if (myChange) {
                                    console.log('Bien! datos cambiados correctamente!')
                                }
                                break;
                            default:
                                console.log('elige una opción correcta');
                        }
                    }
                    break;

                case 'Salir':
                    continuar = false;
                    console.log('thanks for use the program')
                    return;

                default:
                    // Opción por defecto en caso de error
                    break;
            }
        } catch (error) {
            console.log('ups! error', error)
        }
    }
}

miAgenda();
