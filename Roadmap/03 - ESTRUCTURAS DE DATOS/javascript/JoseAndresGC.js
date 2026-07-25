// Array

let cars = ['corolla', 'corsa', 'explorer', 'yaris']

console.log(cars.shift()); // 'corolla' remueve y retorna el primer elemento
console.log(cars); //['corsa', 'explorer', 'yaris']

console.log(cars.pop()); // remueve y retorna el último elemento del array
console.log(cars); // ['corsa', 'explorer']

console.log(cars.unshift('corolla cross', 'mazda')); // 4 Agrega uno o más elementos al principio y retorna la longitud que en ese momento tome el array
console.log(cars); // ['corolla cross', 'mazda', 'corsa', 'explorer']

console.log(cars.push('aveo')); // 5 Agrega uno o más elementos al final y retorna la longitud que en ese momento tome el array
console.log(cars); // ['corolla cross', 'mazda', 'corsa', 'explorer', 'aveo']

console.log(cars.join(', ')); // concatena todos los elementos de un array en una sola línea de texto. Hay que aclarar el separador

console.log(cars.splice()); // se puede agregar, eliminar o reemplazar elementos de un array / sintaxis: .splice(inicio, del, elem1, elem2, ...)
console.log(cars.splice(1, 2)); // eliminar: retorna los elementos eliminados del array ['mazda', 'corsa'] cars retorna ['corolla cross', 'explorer', 'aveo']

console.log(cars.splice(1, 0, 'mustang', 'camaro')); // agregar: retorna un array vacío, pero agrega 'mustrang' y 'camaro' al array original cars. por ende retorna cars ['corolla cross', 'mustang', 'camaro', 'explorer', 'aveo']

console.log(cars.splice(3, 1, 'explorer limited' )); // reemplazar: retorna el elemento eliminado y se reemplaza a su vez por otro elemento 'explorer limited' cars retorna ['corolla cross', 'mustang', 'camaro', 'explorer limited', 'aveo']

console.log(cars.slice()); // retorna una porción de un array. No confundir con splice // .slice(inicio, final)
console.log(cars.slice(0, 3)); // ['corolla cross', 'mustang', 'camaro'] 

console.log(cars.reverse()); // retorna el array, pero al reves

console.log(cars.fill('relleno/reemplazo', 1, 3));  // Rellena un array con un valor estático, devuelve el array original y modificado, sintaxis: .fill(valor, inicio, fin);
console.log(cars); // ['aveo,' 'relleno/reemplazo', 'relleno/reemplazo', 'mustang', 'corolla cross']

// Object

let persona = {
    nombre: "Andrés",
    edad: 22,
    altura: 1.70,
}; // creación de un objeto

console.log(persona); // obtengo todas las propiedades del objeto {nombre: 'Andrés, edad: 22, altura: 1.7}
console.log(persona.nombre); // obtengo una propiedad específica
console.log(persona.nombre = 'José'); // cambio el valor de la propiedad accedida
console.log(persona.vivo = true);// añado nueva/s propiedades al objeto

// Map

let persona2 = new Map();

persona2.set('elemento', 'valor'); // agrego un elemento elemento
console.log(persona2.set('nombre', 'José')); // { 'nombre' : 'José' }

persona2.get('elemento') // obtengo el valor del elemento
console.log(persona2.get('nombre')) // 'José'

console.log(persona2);

console.log(persona2.size); // devuelve el número de elementos en el Map
console.log(persona2.clear()); // Elimina todos los elementos del Map

// Set

let mySet = new Set();

mySet.add('añadirElemento'); // añadiendo elemento/s al Set
mySet.add(5);
mySet.add(1);
mySet.add(1); // este elemento no se añade al set porque ya forma parte

mySet.delete('añadirElemento'); // eliminar elemento del set
mySet.clear(); // Elimina todos los elementos del Set

mySet // {}

// DIFICULTAD EXTRA:

const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});

let agenda = {};

function app(){
    console.log(`
        '********************'
        'LISTA DE CONTACTOS'
        '********************'`
    );

    while (true) {
        console.log('---Qué desea hacer?---');
    console.log('1. Añadir contacto');
    console.log('2. Buscar contacto');
    console.log('3. Actualizar contacto');
    console.log('4. Eliminar contacto');
    console.log('5. Salir');
    console.log('-----------------------');
    
    readline.question('Ingrese una opción: ', (opcion) => {
        console.log('Opción', opcion);
        switch(opcion) {
            case '1': // añadir contacto
                nombre = readline.question('Ingrese el nombre: ');
                telefono = readline.question('Ingre el teléfono: ');
                if (telefono.length > 0 && telefono.length <= 11) {
                    agenda[nombre] = telefono;
                } else {
                    console.log('Número de teléfono inválido. Ingresa un número de 11 dígitos');
                }
                app();
                break
            case '2': // buscar contacto
                nombre = readline.question('Ingrese el nombre a buscar: ');
                // si nombre está en agenda obtengo el numero de teléfono y lo muestro
                // si no está, muestro un mensaje de que no se encontró el contacto 
                if (agenda.hasOwnProperty(nombre)) {
                    console.log('Número de teléfono: ', agenda[nombre]);
                } else {
                    console.log('Contacto no encontrado');
                }
                break
            case '3': // actualizar contacto
                nombre = readline.question('Ingrese el nombre a actualizar: ');
                telefono = readline.question('Ingrese el nuevo número de teléfono: ');
                if (telefono.length > 0 && telefono.length <= 11) {
                    agenda[nombre] = telefono;
                } else {
                    console.log('Número de teléfono inválido. Ingresa un número de 11 dígitos');
                }
                break
            case '4': // borrar contacto
                nombre = readline.question('Ingrese el nombre a eliminar:');
                if (agenda.hasOwnProperty(nombre)) {
                    delete agenda[nombre];
                } else {
                    console.log('Contacto no encontrado');
                }
                break
            case '5': // salir
                console.log('Saliendo... ');
                break;
            default: 
                console.log('Opción no válida, Elige una opción válida');
                agenda();
                break;
        }
    });
}
    }

app();
