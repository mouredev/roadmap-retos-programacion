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
 * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
 */

// Ejemplo de creación de estructuras de datos en JavaScript
// -------------------------------------------------------

// Array
// -----
var array = [1, 2, 3, 4, 5];
console.log(array);

// Inserción
array.push(6);
array.unshift(0);
console.log(array);

// Borrado
array.pop();
array.shift();
console.log(array);



// Actualización
array[0] = 0;
console.log(array);

// Ordenación
array.sort();
console.log(array);

// Diccionario
// -----------
var diccionario = {
    "nombre": "Giovany",
    "apellido": "Osorio",
    "edad": 28
};
console.log(diccionario);

// Inserción
diccionario["sexo"] = "Hombre";
console.log(diccionario);

// Borrado
delete diccionario.sexo;
console.log(diccionario);

// Actualización
diccionario.nombre = "Giovany Andres";
console.log(diccionario);

// Conjunto
// --------
var conjunto = new Set();
conjunto.add(1);
conjunto.add(2);
conjunto.add(3);

console.log(conjunto);

// Inserción
conjunto.add(4);
console.log(conjunto);

// Borrado
conjunto.delete(4);
console.log(conjunto);


// Cola
// ----
var cola = [];
cola.push(1);
cola.push(2);
cola.push(3);
console.log(cola);

// Inserción
cola.push(4);
console.log(cola);

// Borrado
cola.shift();
console.log(cola);

// Actualización
cola[0] = 0;
console.log(cola);

// Dificultad Extra
// ----------------
var contactos = {};
var readline = require('readline');
var rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const opciones=()=>{
    rl.question('Que desea hacer?\n1. Buscar contacto\n2. Insertar contacto\n3. Actualizar contacto\n4. Eliminar contacto\n5. Salir\n', (answer) => {
        switch (answer) {
            case "1":
                buscarContacto();
                break;
            case "2":
                insertarContacto();
                break;
            case "3":
                actualizarContacto();
                break;
            case "4":
                eliminarContacto();
                break;
            case "5":
                rl.close();
                break;
            default:
                console.log("Opcion no valida");
                opcion();
                break;
        }
    });

}


function buscarContacto() {
    rl.question("ingrese el nombre del contacto que desea buscar: ",(nombre)=>{
        if(contactos[nombre]){
            console.log(`Contacto encontrado: ${nombre} Telefono ${contactos[nombre]}`)
        }
        else{
            console.log("contacto no existe")
        }
        opciones()
    })
}

function insertarContacto(){
    rl.question("Ingresa el nombre del contacto: ",(nombre)=>{
        if(contactos[nombre]){
            console.log('Este contacto ya existe.');
            opciones()
        }
        else{
            rl.question('Ingrese el número de teléfono: ', (telefono) => {
                if(!isNaN(telefono)){
                contactos[nombre] = telefono;
                console.log('Contacto insertado con éxito.');
                console.log(contactos)
                }else{
                    console.log('Número de teléfono inválido.');
                }
                opciones()
            })
        }
    })
}

function actualizarContacto(){
    rl.question("ingrese el nombre del contacto que quiere actualizar: ",(nombre)=>{
        if(contactos[nombre]){
            rl.question("ingrese el nuevo numero telefonico: ",(telefono)=>{
                contactos[nombre] = telefono;
                console.log('Contacto actualizado con éxito.');   
                opciones(); 
            })
           
        }else{
            console.log('Contacto no encontrado.') 
            opciones();
        }

    })
}

function eliminarContacto(){
    rl.question("Ingrese el nombre del contacto a eliminar: ",(nombre)=>{
        if(contactos[nombre]){
            delete contactos[nombre]
            console.log("Contacto eliminado con exito")
            opciones();
        }else{
            console.log("no se encontro el contacto a eliminar")
        }
    })
}
opciones()