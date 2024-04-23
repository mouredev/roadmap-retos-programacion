// Mostrar ejemplo de creación de estructuras soportadas por tu lenguaje
const separator = '- - - - - - - - - - - - - - - - - -';
// Array
// Colección de datos ordenados, puede contener cualquier tipo de dato.

let arrayNames = ['John', 'Peter', 'Pedro', 'Javier'];
console.log(`${separator} \nLog Array Inicial ArrayNames: \n ${arrayNames}`);

// Métodos Array

// push(): Inserta uno o mas elementos al final del array y retorna la longitud del array.
arrayNames.push('Sergio')
console.log(`${separator} \nLog despues de utilizar push: \n ${arrayNames}`);

// pop(): Elimina un elemento al final del array y lo retorna
arrayNames.pop();
console.log(`${separator} \nLog despues de utilizar pop: \n ${arrayNames}`);

// slice(): Retorna una copia del array de acuerdo a los indices entregados (i incluido, n no incluido);
let nuevoArray = arrayNames.slice(1,3);
console.log(`${separator} \nLog despues de utilizar slice: \n ${nuevoArray}`);

// shift(): Elimina el primer elemento de un array y lo retorna
arrayNames.shift();
console.log(`${separator} \nLog despues de utilizar shift(): \n ${arrayNames}`);

// unshift(): Inserta uno o mas elementos al inicio del array y retorna la longitud del array.
arrayNames.unshift('Daniel', 'Sebastian');
console.log(`${separator} \nLog despues de utilizar unshift(): \n ${arrayNames}`);

// sort(): Ordena los elementos en un array y lo retorna. Este orden se guia por la conversión de los elementos en string.
arrayNames.sort();
console.log(`${separator} \nLog despues de utilizar sort(): \n ${arrayNames}`);


// Objects
// Son colecciones de propiedades, donde cada propiedad esta compuesta por una key: value.

const monster = {
    name : 'poring',
    type : 'neutral',
    level : 5,
    color: 'pink'
}


monster['height'] = 20; // Insertar propiedad
delete monster.level; // Eliminar propiedad
monster.name = 'Drops' // Actualizacion de valor

console.log(monster)

// Sets
// Colecciones de valores únicos, ya que no acepta duplicados.
let arrayNumeros = [1,1,1,2,2,2,3,3,3,4,4,4];
let noRepetidos = new Set(arrayNumeros);
noRepetidos.add(6); // Agrega elemento
noRepetidos.delete(2); // Elimina elemento

console.log(noRepetidos);

// Maps 
// Es similar a objects, solo que admite keys de cualquier tipo de dato y mantiene el orden en el que se insertaron los eleentos.

const regiones = new Map([
    ["RM", "Región Metropolitana"],
    [5, "Valparaíso"]
]);
regiones.set(15, "Arica y Parinacota"); // Agregar elementos
regiones.set(1, "Tarapacá")

console.log(regiones);

regiones.delete(6); //Elimina elemento y devuelve true si lo elimino y false si no

// Para modificar elemento, se utiliza set
regiones.set(15, "Ariquita :D!");

console.log(regiones);
 
// Ejercicio
// ****************************************

// Importamos elmódulo 'readline' de Node.js para poder recuperar los datos de terminal
const readline = require('readline');

// Interfaz de lectura
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

const miAgenda = new Map();
miAgenda.set('Juan', 123456789);

function mostrarAgenda(){
    console.log(miAgenda);
    leerEntrada();
}

function agregarContacto(){
     rl.question('Ingrese el nombre del nuevo contacto: ', (nombre) => {
        dato1 = nombre;
        if(!miAgenda.has(nombre)){
            rl.question('Ingrese el Número de Teléfono: ', (telefono) => {
            dato2 = telefono;

            miAgenda.set(nombre, telefono);
            console.log(`- - - - - - - - - -\nSe ha ingresado su nuevo contacto correctamente!!\n- - - - - - - - - -`);
            leerEntrada();
            
            });  
        } else {
            console.log('- - - - - - - - - -\nEl contacto ya existe en la Agenda :(!\nInserte un nombre valido\n- - - - - - - - - -');
            agregarContacto();
        }
    });
}

function buscar(){
    rl.question('Ingrese Nombre de Contacto para buscar su Telefono: ', (nombre) => {
        console.log(`- - - - - - - - - -\nEl telefono de ${nombre} es: ${miAgenda.get(nombre)}\n- - - - - - - - - -`);
        leerEntrada();
    })
}

function modificarContacto(){
    rl.question('Ingrese el nombre del contacto el cual quiere modificar: ', (nombre) => {
        if(miAgenda.has(nombre)){
            rl.question('Ingrese el número de teléfono nuevo: ', (telefono) => {
                miAgenda.set(nombre, telefono);
                console.log('- - - - - - - - - Su Contacto fue Modificado con exito - - - - - - - - - -')
                leerEntrada();
            })
        } else {
            console.log('El contacto ingresado no existe en su Agenda, Ingrese un nombre valido');
            modificarContacto();
        }
    })
    
}

function eliminarContacto(){
    rl.question('Ingrese el nombre del contacto que desea eliminar: ', nombre => {
        miAgenda.delete(nombre);
        console.log('- - - - - - - - - - Su Contacto Fue Eliminado Con Exito - - - - - - - - -')
        leerEntrada();
    });
}

function opciones(opcion){
        switch (opcion) {
        case "1":
            mostrarAgenda();
            break;
        case "2":
            buscar();
            break;
        case "3":
            agregarContacto();
            break;
        case "4":
            modificarContacto();
            break;
        case "5":
            eliminarContacto();
            break;
}};

function leerEntrada(){

    // Consulta al usuario y esperar respuesta
    rl.question("Ingrese la opción requerida: \n 1: Mostrar Agenda\n 2: Buscar \n 3: Agregar contacto\n 4: Modificar Contacto\n 5: Eliminar Contacto\n 0: Salir\n", (opcion) => {
        if(opcion === '0') {
            control = false;
            console.log('Se ha terminado la ejecución muchas gracias :D!');
            rl.close(); // Finaliza la interfaz de readline
            process.exit(0); // Finaliza el proceso en node.js
        } else if(opcion > 0 && opcion <= 5){
            opciones(opcion)
        } else {
            console.log('- - - - Ingrese una opción valida - - - -')
            leerEntrada(); //Vuelve a preguntar
        }
    } );
}

leerEntrada();