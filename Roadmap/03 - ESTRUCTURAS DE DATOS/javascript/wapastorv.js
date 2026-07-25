/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en Javascript.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 */
 
/* Array:
    Los arrays permiten almacenar listas ordenas de elementos y permite insertar, borrar, actualizar y ordenar los valores
    conozca más en: https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Array
*/
    // Sintaxis de creación de un array vacío
        const arrayVacio = [];
        console.log(arrayVacio);
        // Sintaxis de creación de un array con elementos
        const array = [1, 2, 3, 4, 5];
        console.log(array);
        // sintaxis de creación de un array con el constructor Array
        let frutas = Array('Manzana', 'Banana', 'Naranja'); 
        console.log(frutas);
        // Creacion de array mixto
        let mixto = [1, 'Manzana', true, 3.14];
        console.log(mixto);// [1, 'Manzana', true, 3.14]

    // Operaciones de inserción
        // Insertar al final
        array.push(6);
        console.log(array);
        
        // Insertar al principio
        array.unshift(0);
        console.log(array);
        
        // Insertar en una posición específica
        array.splice(3, 0, 2.5);// Inserta 2.5 en la posición 3 del array, el 0 indica que no se eliminará ningún elemento 
        console.log(array);
        
        // Insertar varios elementos
        array.splice(3, 0, 2.1, 2.2, 2.3, 2.4);// Inserta varios elementos en la posición 3 del array
        console.log(array);// [0, 1, 2, 2.1, 2.2, 2.3, 2.4, 2.5, 3, 4, 5, 6]
        
        // Insertar un array en otro array
        array.splice(3, 0, [2.1, 2.2, 2.3, 2.4]);// Inserta un array en la posición 3 del array
        console.log(array);// [0, 1, 2, [2.1, 2.2, 2.3, 2.4], 2.1, 2.2, 2.3, 2.4, 2.5, 3, 4, 5, 6]  
        
        // Insertar un array en otro array con spread operator
        let array2 = [2.1, 2.2, 2.3, 2.4];
        array.splice(3, 0, ...array2);// Inserta un array en la posición 3 del array
        console.log(array);// [0, 1, 2, 2.1, 2.2, 2.3, 2.4, 2.1, 2.2, 2.3, 2.4, 2.5, 3, 4, 5, 6]
        
        // Insertar un array en otro array con concat
        //array = array.concat([7, 8, 9]);//Inserta un array al final del array
        console.log(array);// [0, 1, 2, 2.1, 2.2, 2.3, 2.4, 2.1, 2.2, 2.3, 2.4, 2.5, 3, 4, 5, 6, 7, 8, 9]
        
    // Operaciones de borrado
        
        // Borrar al final
        array.pop();// Elimina el último elemento del array
        console.log(array);// [0, 1, 2, 2.1, 2.2, 2.3, 2.4, 2.1, 2.2, 2.3, 2.4, 2.5, 3, 4, 5, 6, 7, 8]

        // Borrar al principio
        array.shift();// Elimina el primer elemento del array
        console.log(array);// [1, 2, 2.1, 2.2, 2.3, 2.4, 2.1, 2.2, 2.3, 2.4, 2.5, 3, 4, 5, 6, 7, 8] 

        // Borrar en una posición específica
        array.splice(3, 1);// Elimina un elemento en la posición 3 del array
        console.log(array);// [1, 2, 2.1, 2.3, 2.4, 2.1, 2.2, 2.3, 2.4, 2.5, 3, 4, 5, 6, 7, 8]

        // Borrar varios elementos
        array.splice(3, 4);// Elimina varios elementos en la posición 3 del array, el 4 indica que se eliminarán 4 elementos
        console.log(array);// [1, 2, 2.1, 2.1, 2.2, 2.3, 2.4, 2.5, 3, 4, 5, 6, 7, 8]

        // Borra un rango de elementos
        array.splice(3, 3, 2.3, 2.4, 2.5);// Elimina 3 elementos en la posición 3 del array y añade 3 nuevos elementos en la misma posición
        console.log(array);// [1, 2, 2.1, 2.3, 2.4, 2.5, 2.5, 3, 4, 5, 6, 7, 8]

        // Borrar un rango de elementos con slice
        array = array.slice(3, 6);// Elimina los elementos desde la posición 3 hasta la 6
        console.log(array);// [2.3, 2.4, 2.5]

    // Operaciones de actualización

        // Actualizar un elemento
        array[0] = 1;
        console.log(array);// [1, 2.4, 2.5]

        // Actualizar varios elementos
        array.splice(1, 2, 2.1, 2.2, 2.3);// Actualiza varios elementos en la posición 1 del array, el 2 indica que se actualizarán 2 elementos y se añaden 3 nuevos elementos
        console.log(array);// [1, 2.1, 2.2, 2.3]

    // Operaciones de ordenación

        // Ordenar un array
        frutas.sort();// Ordena los elementos del array en orden alfabético
        console.log(frutas);// ['Banana', 'Manzana', 'Naranja']

        // Ordenar un array de números
        let numeros = [1, 5, 3, 2, 4];
        numeros.sort((a, b) => a - b);// Ordena los elementos del array en orden ascendente
        console.log(numeros);// [1, 2, 3, 4, 5]
        numeros.sort();// Ordena los elementos del array en orden descendente
        console.log(numeros);// [5, 4, 3, 2, 1]

        // Ordenar un array de objetos
        let personas = [
            {nombre: 'Juan', edad: 25},
            {nombre: 'Ana', edad: 20},
            {nombre: 'Pedro', edad: 30}
        ];
        personas.sort((a, b) => a.edad - b.edad);// Ordena los elementos del array en orden ascendente según la edad
        console.log(personas);// [{nombre: 'Ana', edad: 20}, {nombre: 'Juan', edad: 25}, {nombre: 'Pedro', edad: 30}]
        personas.sort((a, b) => a.nombre.localeCompare(b.nombre));// Ordena los elementos del array en orden alfabético según el nombre, localeCompare compara cadenas de texto teniendo en cuenta el orden alfabético
        console.log(personas);// [{nombre: 'Ana', edad: 20}, {nombre: 'Juan', edad: 25}, {nombre: 'Pedro', edad: 30}]   

/* Object:
        Los objetos permiten almacenar colecciones de pares clave-valor y permite insertar, borrar y actualizar los valores
        conozca más en: https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Object

*/
        //sintaxis de creación de un objeto vacío
        const objetoVacio = {};
        console.log(objetoVacio);// {}

        //sintaxis de creación de un objeto con propiedades
        const objetoPersona = {
            nombre: 'Juan',
            edad: 25,
            casado: false
        };
        console.log(objetoPersona);// {nombre: 'Juan', edad: 25, casado: false}

        // Operaciones con la clave
            // Insertar una propiedad
            objetoPersona.apellido = 'Pérez';
            console.log(objetoPersona);// {nombre: 'Juan', edad: 25, casado: false, apellido: 'Pérez'}

            // Borrar una propiedad
            delete objetoPersona.casado;
            console.log(objetoPersona);// {nombre: 'Juan', edad: 25, apellido: 'Pérez'}

            // Actualizar una propiedad
            objetoPersona.nombre = 'Pedro';
            console.log(objetoPersona);// {nombre: 'Pedro', edad: 25, apellido: 'Pérez'}
            // Ordenar un propiedades de un objeto
            const ordered = {};
            Object.keys(objetoPersona).sort().forEach(function(key) {
                ordered[key] = objetoPersona[key];
            });
            console.log(ordered);// {apellido: 'Pérez', edad: 25, nombre: 'Pedro'}


        // Operaciones con el valor
            // Insertar un valor
            objetoPersona.edad = 30;
            console.log(objetoPersona);// {nombre: 'Pedro', edad: 30, apellido: 'Pérez'}

            // Borrar un valor
            objetoPersona.edad = undefined;
            console.log(objetoPersona);// {nombre: 'Pedro', edad: undefined, apellido: 'Pérez'}

            // Actualizar un valor
            objetoPersona.edad = 35;
            console.log(objetoPersona);// {nombre: 'Pedro', edad: 35, apellido: 'Pérez'}



/* Set:
        Los sets permiten almacenar colecciones de valores únicos y permite insertar, borrar y actualizar los valores
        conozca más en: https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Set
*/

    // Sintaxis de creación de un set vacío
        const setVacio = new Set();
        console.log(setVacio);// Set {}

    // Sintaxis de creación de un set con elementos
        const set = new Set([1, 2, 3, 4, 5]);
        console.log(set);// Set {1, 2, 3, 4, 5}
    
    // Operaciones de inserción
        set.add(6);
        console.log(set);// Set {1, 2, 3, 4, 5, 6}
        set.add(6);// No se puede añadir un valor duplicado, el set solo permite valores únicos
        console.log(set);// Set {1, 2, 3, 4, 5, 6}
        set.add(7);
        console.log(set);// Set {1, 2, 3, 4, 5, 6, 7}
        set.add(8);
        console.log(set);// Set {1, 2, 3, 4, 5, 6, 7, 8}
    
    // Operaciones de borrado
        set.delete(8);
        console.log(set);// Set {1, 2, 3, 4, 5, 6, 7}
        set.clear();
        console.log(set);// Set {}
    
    // Operaciones de actualización
        set.add(1);
        set.add(2);
        set.add(3);
        set.add(4);
        set.add(5);
        set.add(6);
        set.add(7);
        console.log(set);// Set {1, 2, 3, 4, 5, 6, 7}
        set.add(8);
        console.log(set);// Set {1, 2, 3, 4, 5, 6, 7, 8}
        set.add(9);
        console.log(set);// Set {1, 2, 3, 4, 5, 6, 7, 8, 9}
        set.add(13);
        set.add(11);
        set.add(10);
        set.add(12);
        console.log(set);// Set {1, 2, 3, 4, 5, 6, 7, 8, 9, 13, 11, 10, 12}

    // Operaciones de ordenación
    let setOrdenado = new Set([...set].sort((a, b) => a - b));
    console.log(setOrdenado);// Set {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}

/* Map:
    Los maps permiten almacenar colecciones de pares clave-valor, donde las claves pueden ser de cualquier tipo.
    Mantienen el orden de inserción de los elementos.
*/

    // Sintaxis de creación de un map vacío
        const mapVacio = new Map();
        console.log(mapVacio);// Map {}

    // Sintaxis de creación de un map con elementos
        const map = new Map([
            ['nombre', 'Juan'],
            ['edad', 25],
            ['casado', false]
        ]);
        console.log(map);// Map {'nombre' => 'Juan', 'edad' => 25, 'casado' => false}   

    // Operaciones de inserción
        map.set('apellido', 'Pérez');// Inserta un nuevo par clave-valor
        console.log(map);// Map {'nombre' => 'Juan', 'edad' => 25, 'casado' => false, 'apellido' => 'Pérez'}
    
    // Operaciones de borrado
        map.delete('casado');// Elimina un par clave-valor
        console.log(map);// Map {'nombre' => 'Juan', 'edad' => 25, 'apellido' => 'Pérez'}
        map.clear();// Elimina todos los pares clave-valor
        console.log(map);// Map {}
    
    // Operaciones de actualización
        map.set('nombre', 'Pedro');// Actualiza un valor
        console.log(map);// Map {'nombre' => 'Pedro'}
        map.set('edad', 30);// Actualiza un valor
        map.set('apellido', 'Pérez');// Inserta un nuevo par clave-valor
        console.log(map);// Map {'nombre' => 'Pedro', 'edad' => 30, 'apellido' => 'Pérez'}
    
    // Operaciones de ordenación
        let mapOrdenado = new Map([...map].sort((a, b) => a[0] - b[0]));
        console.log(mapOrdenado);// Map {'apellido' => 'Pérez', 'edad' => 30, 'nombre' => 'Pedro'}

/* Pilas (stack):
    las pilas permiten almacenar colecciones de elementos siguiendo el principio LIFO (Last In, First Out), 
    lo que significa que el último elemnto en entrar es el primero en salir.
    Se puede implementar una pila con un array.
    conozca más en: https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Array
*/
        // Sintaxis de creación de una pila
        let pila = [];
        console.log(pila);// [] pila vacía

        //Operaciones de inserción
        pila.push(1);// Inserta un elemento en la pila
        pila.push(2);// Inserta un elemento en la pila
        pila.push(3);// Inserta un elemento en la pila
        console.log(pila);// [1, 2, 3]

        //Operaciones de borrado
        pila.pop();// Elimina el último elemento de la pila
        console.log(pila);// [1, 2]

        //Operaciones de actualización
        pila[pila.length - 1] = 4;// Actualiza el último elemento de la pila
        console.log(pila);// [1, 4]


/* Cola:
    Las colas permiten almacenar colecciones de elementos siguiendo el principio FIFO (First In, First Out).
    Se puede implementar una cola con un array.
    conozca más en: https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Array

*/

    // Sintaxis de creación de una cola
        let cola = [];
        console.log(cola);// [] cola vacía
    
    // Operaciones de inserción
        cola.push(1);// Inserta un elemento en la cola
        cola.push(2);// Inserta un elemento en la cola
        cola.push(3);// Inserta un elemento en la cola
        console.log(cola);// [1, 2, 3]

    // Operaciones de borrado
        cola.shift();// Elimina el primer elemento de la cola
        console.log(cola);// [2, 3]

    // Operaciones de actualización 
        cola[0] = 4;// Actualiza el primer elemento de la cola
        console.log(cola);// [4, 3]


/* Ejemplo de uso de estructuras de datos en Javascript */

/* Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
 */

const readline = require('readline');// Importa el módulo readline para leer la entrada por terminal
const rl = readline.createInterface({// Crea una interfaz de lectura
    input: process.stdin,// Establece la entrada por defecto
    output: process.stdout// Establece la salida por defecto
});

let agenda = new Map();// Crea un mapa para almacenar los contactos

function buscarContacto(nombre) {
    if (agenda.has(nombre)) {
        console.log(`Nombre: ${nombre}, Teléfono: ${agenda.get(nombre)}`);
    } else {
        console.log('Contacto no encontrado');
    }
}

function insertarContacto(nombre, telefono) {
    agenda.set(nombre, telefono);
    console.log('Contacto insertado');
}

function actualizarContacto(nombre, telefono) {
    if (agenda.has(nombre)) {
        agenda.set(nombre, telefono);
        console.log('Contacto actualizado');
    } else {
        console.log('Contacto no encontrado');
    }
}   

function eliminarContacto(nombre) {
    if (agenda.has(nombre)) {
        agenda.delete(nombre);
        console.log('Contacto eliminado');
    } else {
        console.log('Contacto no encontrado');
    }
}

function mostrarMenu() {
    console.log('1. Buscar contacto');
    console.log('2. Insertar contacto');
    console.log('3. Actualizar contacto');
    console.log('4. Eliminar contacto');
    console.log('5. Salir');
}

function leerOpcion() {
    rl.question('Introduce una opción: ', (opcion) => {
        switch (opcion) {
            case '1':
                rl.question('Introduce el nombre del contacto: ', (nombre) => {
                    buscarContacto(nombre);
                    mostrarMenu();
                    leerOpcion();
                });
                break;
            case '2':
                rl.question('Introduce el nombre del contacto: ', (nombre) => {
                    rl.question('Introduce el teléfono del contacto: ', (telefono) => {
                        insertarContacto(nombre, telefono);
                        mostrarMenu();
                        leerOpcion();
                    });
                });
                break;
            case '3':
                rl.question('Introduce el nombre del contacto: ', (nombre) => {
                    rl.question('Introduce el teléfono del contacto: ', (telefono) => {
                        actualizarContacto(nombre, telefono);
                        mostrarMenu();
                        leerOpcion();
                    });
                });
                break;
            case '4':
                rl.question('Introduce el nombre del contacto: ', (nombre) => {
                    eliminarContacto(nombre);
                    mostrarMenu();
                    leerOpcion();
                });
                break;
            case '5':
                rl.close();
                break;
            default:
                console.log('Opción no válida');
                mostrarMenu();
                leerOpcion();
        }
    });
}

mostrarMenu();
leerOpcion();

rl.on('close', () => {  
    console.log('Adiós');
    process.exit(0);
});
// Para ejecutar el programa, copia y pega el código en un archivo con extensión .js y ejecútalo con Node.js
// node nombreArchivo.js
// Sigue las instrucciones por terminal para interactuar con el programa



