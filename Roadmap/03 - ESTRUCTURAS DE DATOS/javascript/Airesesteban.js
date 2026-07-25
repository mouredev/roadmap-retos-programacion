// Arrays
let numbers = [1,2,3,4,5]
console.log("Array", numbers)

// Operaciones con arrays

// Inserción
numbers.push(6)
console.log("Array despues de agregar al final un valor",numbers)

// Borrado
numbers.splice(2,1)
console.log("Array despues de eliminar un valor",numbers)

// Actualización
numbers[1]= 10
console.log("Array despues de actualizar un valor",numbers)

// Orden
numbers.sort()
console.log("Array despues de ordenar",numbers)


// Objetos

let objeto = {nombre: "Esteban", edad: 38}
console.log("Objeto",objeto)

// Operaciones con objetos

// Inserción
objeto.direccion = " Calle 123"
console.log("Objeto despues de inserción:",objeto)

// Borrado
delete objeto.edad
console.log("Objeto despues de borrado:",objeto)

// Actualización
objeto.nombre = "Pedro"
console.log("Objeto despues de actualizacion:",objeto)

// Mapas

let mapa = new Map()
mapa.set("clave1", "valor1")
mapa.set("clave2", "valor2")
console.log('Mapa:', mapa)

// Operaciones con mapas

// Inserción
mapa.set("clave3","valor3")
console.log('Mapa después de inserción:', mapa)

// Borrado
mapa.delete("clave2")
console.log('Mapa después de borrado:', mapa)

// Actualización
mapa.set("clave1","NewValor1")
console.log('Mapa después de actualizacion:', mapa)

// Conjuntos
let conjunto = new Set([1, 2, 3, 4, 5])
console.log('Conjunto:', conjunto)

// Operaciones con conjuntos

// Inserción
conjunto.add(6)
console.log('Conjunto después de inserción:', conjunto)


// Borrado
conjunto.delete(6) 
console.log('Conjunto después de borrado:', conjunto);

// Actualización
conjunto = new Set([...conjunto].map(x => x * 2))
console.log('Conjunto después de actualización:', conjunto)


// Ejercicio extra: Agenda de contactos por terminal

const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
const agenda = []

const my_agenda = () => {

    console.log("Agenda de contactos")
    console.log("Digite el numero de la opcion que quiere utilizar")
    console.log("1 - Buscar contacto")
    console.log("2 - Agregar contacto")
    console.log("3 - Actualizar contacto")
    console.log("4 - Borrar contacto")
    console.log("5 - Salir")

    rl.question("Opción: ", (answer) => {
        opcion = parseInt(answer)

    switch (opcion){
        case 1:
            buscarContacto()
            break;
        case 2:
            ingresarContacto()
            break;
        case 3:
            actualizarContacto()
            break;
        case 4:
            borrarContacto()
            break;
        case 5:
            console.log("Saliendo de la agenda")
            rl.close()
            break;   
        default:
            console.log("Opcion no valida. Solo se admiten numeros del 1 al 5") 
            my_agenda()                
    }})
}


function ingresarContacto(){
    rl.question("Ingrese el nombre del nuevo contacto:", (nuevoNombre) => {
        rl.question("Ingrese el numero de teléfono (maximo 10 digitos):", (nuevoNumero) => {
            if (nuevoNumero.length > 10){
                console.log("El teléfono no puede superar los 10 digitos")
        }    
        else if (agenda.some(i => i.nombre.toLowerCase()=== nuevoNombre.toLowerCase())){
            console.log("El contacto ya existe, intente con otro nombre")
        }else{  
            agenda.push({nombre: nuevoNombre, telefono: nuevoNumero})
            console.log("Contacto agendado exitosamente")
        }
        my_agenda()
    })
    })
}

function buscarContacto(){
    rl.question("Ingresa el nombre del contacto a buscar", (nombreConsulta) => {
        const contacto = agenda.find(i => i.nombre.toLowerCase() === nombreConsulta.toLowerCase())
    if (contacto) {
        console.log(`Nombre: ${contacto.nombre}, Teléfono:${contacto.telefono}`)
    }else{
        console.log("No se encontro un contacto con ese nombre")
    }
    my_agenda()
    }) 
}

function borrarContacto(){
    rl.question('Nombre del contacto a eliminar: ', (nombre) => {
        const index = agenda.findIndex(c => c.nombre === nombre);
        if (index !== -1) {
            agenda.splice(index, 1);
            console.log('Contacto eliminado.');
        } else {
            console.log('Contacto no encontrado.');
        }
        my_agenda()
    })
}
function actualizarContacto(){
    rl.question('Nombre del contacto a actualizar: ', (nombre) => {
        const contacto = agenda.find(c => c.nombre === nombre);
        if (contacto) {
            rl.question("Ingrese el numero de teléfono (maximo 10 digitos):", (nuevoNumero) => {
                if (nuevoNumero.length > 10){
                    console.log("El teléfono no puede superar los 10 digitos")
                }    
                else {
                    contacto.telefono = nuevoNumero;
                    console.log('Contacto actualizado.');
                }
                my_agenda()
            });
        } else {
            console.log('Contacto no encontrado.');
           my_agenda()
        }
    }); 
}


my_agenda()