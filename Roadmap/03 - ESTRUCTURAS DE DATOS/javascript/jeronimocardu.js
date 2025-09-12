// ESTRUCTURAS SOPORTADAS DE JS

const { clear } = require('console');
const { read } = require('fs');

//          Primitivos
let number = 12;
let string = 'Hola mundo!';
let boolean = true;
let indefinito = undefined;
let isNull = null;

//          Objetos
let objeto1 = {
    nombre: 'Jeronimo',
    edad: 22,
    lenguaje: 'javascript',
};
objeto1["sexo"] = 'hombre';     // insercion
delete objeto1.lenguaje;        // borrado
objeto1.edad = 20               // actualizacion
console.log(objeto1)

let arreglo1 = [1, 2, 3, 4];
let arreglo2 = ['a', 'b', 'c', 'd'];
arreglo1.push(7);       // insercion
arreglo2.pop();         // borrado
arreglo1[0] = 0;        // actualizado
arreglo1.reverse();     // ordenado

console.log(arreglo1);
console.log(arreglo2);

function unaFuncion(){
    console.log('Soy una funcion');
}

let fecha = new Date();

//          Otros
let promesa = new Promise((res, rej) => {
    // operacion
})

async function funcionAsync(){
    let variable = await promesa//....
};



// EXTRA
let contactos = [
    {nombre: 'Jeronimo', numero: 123456788},
]

const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout,
})
// Busqueda de contacto
function busqueda(name){
    let encontrado = false;
    for(let i of contactos){
        if(i.nombre === name){
            console.log(`\nEl número telefonico de ${name} es: ${i.numero}`);
            encontrado = true;
        }
    }
    if(!encontrado) console.log(`\n${name} no esta en nuestra agenda`);
    espera();
}
// Insercion de contacto
function insercion(newName, newNumber){
    let encontrado = false;
    for(let i of contactos){
        if(i.numero === newNumber){
            console.log('\nEste numero ya esta agendado, debe haber un error..');
            encontrado = true;
        }
    }
    if(newNumber.toString().length >= 11 || isNaN(newNumber)){
        console.log('\nDebe ser numerico y menor a 11 digitos de largo..')
    }
    if(!encontrado && !isNaN(newNumber) && newNumber.toString().length < 11) {
        contactos.push({nombre: newName, numero: newNumber});
        console.log(`\nContacto agregado: ${newName} - ${newNumber}`);
    }
    espera();
}
function actualizacion(toUpdate, newName, newNumber){
    let encontrado = false;
    for(let i of contactos){
        if(i.nombre === toUpdate){
            i.nombre = newName;
            i.numero = newNumber;
            encontrado = true;
            break;
        }
    }
    if(!encontrado) console.log(`\n${toUpdate} no está en nuestra agenda`);
    if(newNumber.toString().length >= 11 || isNaN(newNumber)) console.log('\nDebe ser numerico y menor a 11 digitos de largo..');
    espera();
}
function eliminar(conctact){
    let incialLength = contactos.length;
    contactos = contactos.filter(persona => persona.nombre !== conctact);
    if(incialLength > contactos.length){
        console.log(`\n${conctact} se ha eliminado con exito!`);
    } else{
        console.log(`No se encontro ${conctact} en nuestros contactos`)
    }
    espera();
}
function espera(){
    readline.question('\nPrecione ENTER para continuar..', (tecla) =>{
        if(tecla === ''){
            console.clear();
            agenda()
        } else{
            espera();
        }
    })
}
function makeNumber(str){
    let number = parseInt(str);
    return number;
}
function makeName(name){
    let nameMod = name[0].toUpperCase() + name.slice(1).toLowerCase();
    return nameMod;
}

function agenda(){
    console.log(`
======= Agenda Telefonica ======= \n
    1. Buscar contacto
    2. Agregar contacto
    3. Actulizar contacto
    4. Borrar contacto
    0. Salir \n`);

    readline.question('Elija una opcion: ', (opcion) => {
        opcionNumber = parseInt(opcion);
        switch (opcionNumber){
            case 1:
                readline.question('Ingrese el nombre de la persona que quiere buscar: ', (nombreBuscado) =>{
                    busqueda(makeName(nombreBuscado));
                })
                break;
            case 2:
                readline.question('Ingrese el nombre del contacto que quiere agregar: ', (newNameContact) => {
                    readline.question('Ahora ingrese el número del nuevo contacto: ', (newNumContact) => {
                        insercion(makeName(newNameContact), makeNumber(newNumContact));
                    })
                })
                break;
            case 3:
                readline.question('Ingrese el nombre del contacto que quiere actualizar: ', (contactToUpdate) => {
                    readline.question('Ingrese el nuevo nombre del contacto: ', (nameUpdate) =>{
                        readline.question('Ingrese el nuevo número del contacto: ', (numberUpdate) => {
                            actualizacion(makeName(contactToUpdate), makeName(nameUpdate), makeNumber(numberUpdate));
                        })
                    })
                })
                break;
            case 4:
                readline.question('Ingrese el nombre del contacto que desea eliminar: ', (contactToDelete) =>{
                    eliminar(makeName(contactToDelete));
                })
                break;
            case 0:
                console.log('\nSaliendo..')
                readline.close();
                break;
            default:
                console.log(`"${opcionNumber}" no es una opcion valida`);
                espera();
        }
    })
}
agenda()