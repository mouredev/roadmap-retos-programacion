// ** -1-

// * Estructuras de Datos

let number = 8
number = 8.8
number = NaN

let string = 'ocho'

let boolean = true
boolean = false

let nullNull = null

let undefined

let symbol = Symbol("foo")

let object = {
    Nombre: 'Bernat',
    Apellido: 'Cucarella'
}

let array = [1, 2, 3, 4, 5, 6, 7, 8]

function funcion(){
}

let fecha = new Date

// * Estructuras de Control

if (number === 8){

} else if (number > 8){

} else {

}

switch (number) {
    case 8:
        
        break;

    default:
        break;
}

for (index = 0; index < 8; index++) {
}

for (const key in object) {
    if (Object.hasOwnProperty.call(object, key)) {
        const element = object[key];
        
    }
}

do {
    
} while (index < 8);

try { 
    
} catch (error) {
    
}

// ** EXTRA (simple) ** -----------------------------------------------------------------------------------------------------------------------------------------------

const agendaContactos = [
    {
        Nombre: 'Bernat',
        Numero: '674863572'
    }
];

// Inserción

function compruebaNumero(nuevoNumero) {
    if (String(nuevoNumero).length === 9) {
        return parseInt(nuevoNumero, 10);
    }
    console.error("El formato del número no es correcto");
    return undefined;
}

function nuevoContacto(nuevoNombre, nuevoNumero) {
    let numeroValidado = compruebaNumero(nuevoNumero);
    if (numeroValidado) {
        let nuevoContacto = {
            Nombre: nuevoNombre,
            Numero: numeroValidado
        };
        agendaContactos.push(nuevoContacto);
        console.log(`El contacto ${nuevoNombre} ha sido añadido con éxito`);
    } else {
        console.error(`No se pudo añadir el contacto ${nuevoNombre} debido a un número inválido.`);
    }
}

// Busqueda

function buscarNúmero(buscarNombre) {
    for (let index = 0; index < agendaContactos.length; index++) {
        if (agendaContactos[index].Nombre === buscarNombre) {
            console.log(`El número del contacto ${agendaContactos[index].Nombre} es: ${agendaContactos[index].Numero}`);
            return; 
        } 
    }
    console.error('Este contacto no existe');
}

// Actualización

function actualizarNumero(buscarNombre, nuevoNumero) {
    for (let index = 0; index < agendaContactos.length; index++) {
        if (agendaContactos[index].Nombre == buscarNombre) {
            agendaContactos[index].Numero = compruebaNumero(nuevoNumero)
            console.log(`El contacto ${agendaContactos[index].Nombre} ha sido actualizado con éxito`)
            return; 
        } 
    }
    console.error('Este contacto no existe');
}


function actualizarNombre(buscarNombre, nuevoNombre) {
    for (let index = 0; index < agendaContactos.length; index++) {
        if (agendaContactos[index].Nombre == buscarNombre) {
            agendaContactos[index].Nombre = nuevoNombre
            console.log(`El contacto ${agendaContactos[index].Nombre} ha sido actualizado con éxito`)
            return; 
        } 
    }
    console.error('Este contacto no existe');
}

// Eliminación de contactos

function eliminarContacto(buscarNombre) {
    for (let index = 0; index < agendaContactos.length; index++) {
        if (agendaContactos[index].Nombre == buscarNombre) {
            console.log(`El contacto ${agendaContactos[index].Nombre} ha sido borrado con éxito`)
            agendaContactos.splice(index, 1)
            return; 
        } 
    }
    console.error('Este contacto no existe');
}

// ** EXTRA ** -----------------------------------------------------------------------------------------------------------------------------------------------

const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});

function listinTelefonico(){
    readline.question('¿Qué quiere hacer? Elija entre [búsqueda], [inserción], [actualización] y [eliminación] y escriba el comando a continuación: ', (respuesta) => {
        switch (respuesta.toLowerCase()) {
            case 'búsqueda':
                readline.question('Ingrese el nombre del contacto que desea buscar: ', (nombre) => {
                    buscarNúmero(nombre);
                    listinTelefonico();
                });
                break;
            case 'inserción':
                readline.question('Ingrese el nombre del nuevo contacto: ', (nombre) => {
                    readline.question('Ingrese el número del nuevo contacto: ', (numero) => {
                        nuevoContacto(nombre, numero);
                        listinTelefonico();
                    });
                });
                break;
            case 'actualización':
                readline.question('¿Desea actualizar el [nombre] o el [número]?: ', (tipoActualizacion) => {
                    if (tipoActualizacion.toLowerCase() === 'nombre') {
                        readline.question('Ingrese el nombre del contacto a actualizar: ', (nombre) => {
                            readline.question('Ingrese el nuevo nombre: ', (nuevoNombre) => {
                                actualizarNombre(nombre, nuevoNombre);
                                listinTelefonico();
                            });
                        });
                    } else if (tipoActualizacion.toLowerCase() === 'número') {
                        readline.question('Ingrese el nombre del contacto a actualizar: ', (nombre) => {
                            readline.question('Ingrese el nuevo número: ', (nuevoNumero) => {
                                actualizarNumero(nombre, nuevoNumero);
                                listinTelefonico();
                            });
                        });
                    } else {
                        console.error('Opción no reconocida');
                        listinTelefonico();
                    }
                });
                break;
            case 'eliminación':
                readline.question('Ingrese el nombre del contacto que desea eliminar: ', (nombre) => {
                    eliminarContacto(nombre);
                    listinTelefonico();
                });
                break;
            default:
                console.error(`No reconocí "${respuesta}".`);
                listinTelefonico();
        }
    });
}

listinTelefonico()