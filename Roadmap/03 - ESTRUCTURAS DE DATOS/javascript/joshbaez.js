// EJERCICIO

/* - Muestra ejemplos de creación de todas las estructuras soportadas por defecto
   en tu lenguaje.
 - Utiliza operaciones de inserción, borrado, actualización y ordenación.

 DIFICULTAD EXTRA (opcional):
 Crea una agenda de contactos por terminal.
 - Debes implementar funcionalidades de búsqueda, inserción, actualización
   y eliminación de contactos.
 - Cada contacto debe tener un nombre y un número de teléfono.
 - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
   y a continuación los datos necesarios para llevarla a cabo.
 - El programa no puede dejar introducir números de teléfono no númericos y con más
   de 11 dígitos (o el número de dígitos que quieras).
 - También se debe proponer una operación de finalización del programa.
*/


//  ARRAYS 


// creacion 
let numeros = [1, 2, 3, 4, 5];

// acceso
console.log(numeros[0]);

// actualizacion 
numeros[0] = 10;
console.log(numeros[0]);

// agregar elementos 
numeros.push(6); // agregar al final
numeros.unshift(0); // agregar al inicio 

// eliminar elementos 
numeros.pop(); // elimina el ultimo elemento
numeros.shift(); // eliminar el primer elemento 

// eliminar elemento de una sona espesifica 
numeros.splice(2, 1);  // Elimina 1 elemento en la posición 2

// otros metodos 
numeros.includes(3); // true
numeros.indexOf(3); // 2
numeros.reverse(); // Invierte el array
numeros.sort(); // Ordena el array



// OBJETOS 


// creacio 
let persona = {
    nombre: "Joshua",
    edad: 25,
    ciudad: "Boston"
};

// acceso
console.log(persona.nombre); // joshua 

// actualizacion 
persona.edad = 26;

// agregar propiedad 
persona.profesion = "Ingeniero";

// eliminar propiedad 
delete persona.ciudad;

// otros metodos
 Object.keys(persona); // ["nombre", "edad", "profesion"]
 Object.values(persona); // ["Joshua", 26, "Ingeniero"]
 Object.entries(persona); // [["nombre", "Joshua"], ["edad", 26], ["profesion", "Ingeniero"]]



 // MAPAS (MAPS)



// creacion 
let mapa = new Map();
mapa.set("nombre", "Joshua");
mapa.set("edad", 25);


// acceso 
console.log(mapa.get("nombre")); // "Joshua"

// actualizacion 
mapa.set("edad", 26);

// eliminar elemento 
mapa.delete("edad");

// verificar existencia 
mapa.has("nombre"); // true

// otros metodos 
mapa.size; // 1
mapa.clear(); // Elimina todos los elementos



// CONJUNTOS 



// creacion
let conjunto = new Set();
conjunto.add(1);
conjunto.add(2);
conjunto.add(2); // No se agrega porque ya existe

// acceso 
console.log(conjunto.has(1)); // true

// elminar elemento 
conjunto.delete(1);

// verificar existencia
conjunto.has(1); // false

// otros metodos 
conjunto.size; // 1
conjunto.clear(); // Elimina todos los elementos



// CADENA DE TEXTO STRING 



// creacion 
let cadena = "Hola, mundo!";

// acceso 
console.log(cadena[0]); // "H"

// actualizacion 
cadena = cadena.replace("mundo", "Joshua");

// otros metodos
cadena.length; // 12
cadena.toUpperCase(); // "HOLA, JOSHUA!"
cadena.toLowerCase(); // "hola, joshua!"
cadena.includes("Joshua"); // true
cadena.indexOf("Joshua"); // 6
cadena.split(", "); // ["Hola", "Joshua!"]
cadena.substring(0, 4); // "Hola"



// NUMEROS 



// creacion 
let entero = 42;
let decimal = 3.14;

// operaciones 
let suma = entero + decimal;
let resta = entero - decimal;
let multiplicacion = entero * decimal;
let division = entero / decimal;


// metodos 
Math.round(decimal); // 3
Math.ceil(decimal); // 4
Math.floor(decimal); // 3
Math.max(1, 2, 3); // 3
Math.min(1, 2, 3); // 1
Math.random(); // Número aleatorio entre 0 y 1



// BOLEANOS 

// creacion 
let esVerdadero = true;
let esFalso = false;


// operaciones logicas 
console.log(esVerdadero && esFalso); // false
console.log(esVerdadero || esFalso); // true
console.log(!esVerdadero); // false




// FUNCIONES 



//creacion 
function saludar(nombre) {
    return "Hola, " + nombre + "!";
}

// llamada a una funcion 
console.log(saludar("Joshua")); // "Hola, Joshua!"


// funcion anonima 
let sumar = function(a, b) {
    return a + b;
};


// funcion flecha
let restar = (a, b) => a - b;



// CLASES 



// creacion 
class Persona {
    constructor(nombre, edad) {
        this.nombre = nombre;
        this.edad = edad;
    }

    saludar() {
        return "Hola, " + this.nombre + "!";
    }
}


// instanciacion 
let joshua = new Persona("Joshua", 25);


// acceso a metodos 
console.log(joshua.saludar()); // "Hola, Joshua!"




//  SIMBOLOS 


// creacion
let simbolo1 = Symbol("descripcion");
let simbolo2 = Symbol("descripcion");


// comparacion 
console.log(simbolo1 === simbolo2); // false


// uso como propiedad de un objeto 
let objeto = {
    [simbolo1]: "valor"
};
console.log(objeto[simbolo1]); // "valor"



// BIGLNT



// creacion 
let numeroGrande = BigInt(123456789012345678901234567890);
let otroNumeroGrande = 123456789012345678901234567890n;

// operaciones 
let sumaGrande = numeroGrande + otroNumeroGrande;
console.log(sumaGrande); // 246913578024691357802469135780n

const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let contactos = {};

function mostrarMenu() {
    console.log("\nAgenda de Contactos");
    console.log("1. Buscar contacto");
    console.log("2. Insertar contacto");
    console.log("3. Actualizar contacto");
    console.log("4. Eliminar contacto");
    console.log("5. Salir");
    rl.question("Seleccione una opción: ", (opcion) => {
        switch (opcion) {
            case '1':
                buscarContacto();
                break;
            case '2':
                insertarContacto();
                break;
            case '3':
                actualizarContacto();
                break;
            case '4':
                eliminarContacto();
                break;
            case '5':
                finalizarPrograma();
                break;
            default:
                console.log("Opción no válida. Intente de nuevo.");
                mostrarMenu();
                break;
        }
    });
}

function buscarContacto() {
    rl.question("Ingrese el nombre del contacto: ", (nombre) => {
        if (contactos[nombre]) {
            console.log(`Contacto encontrado: ${nombre} - ${contactos[nombre]}`);
        } else {
            console.log("Contacto no encontrado.");
        }
        mostrarMenu();
    });
}

function insertarContacto() {
    rl.question("Ingrese el nombre del contacto: ", (nombre) => {
        rl.question("Ingrese el número de teléfono: ", (telefono) => {
            if (validarTelefono(telefono)) {
                contactos[nombre] = telefono;
                console.log("Contacto agregado.");
            } else {
                console.log("Número de teléfono no válido.");
            }
            mostrarMenu();
        });
    });
}

function actualizarContacto() {
    rl.question("Ingrese el nombre del contacto a actualizar: ", (nombre) => {
        if (contactos[nombre]) {
            rl.question("Ingrese el nuevo número de teléfono: ", (telefono) => {
                if (validarTelefono(telefono)) {
                    contactos[nombre] = telefono;
                    console.log("Contacto actualizado.");
                } else {
                    console.log("Número de teléfono no válido.");
                }
                mostrarMenu();
            });
        } else {
            console.log("Contacto no encontrado.");
            mostrarMenu();
        }
    });
}

function eliminarContacto() {
    rl.question("Ingrese el nombre del contacto a eliminar: ", (nombre) => {
        if (contactos[nombre]) {
            delete contactos[nombre];
            console.log("Contacto eliminado.");
        } else {
            console.log("Contacto no encontrado.");
        }
        mostrarMenu();
    });
}

function finalizarPrograma() {
    console.log("Finalizando programa...");
    rl.close();
}

function validarTelefono(telefono) {
    return /^\d{1,11}$/.test(telefono);
}

mostrarMenu();