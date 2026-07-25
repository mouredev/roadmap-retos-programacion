/*
_____________________________________
https://github.com/kenysdev
2024 - JavaScript
_______________________________________
03 ESTRUCTURAS DE DATOS
---------------------------------------
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

// ________________________________________________________
// 1. Arrays(Listas Ordenadas y Flexibles)
console.log("Arreglos");

let numeros = [3, 2, 1];
let palabras = ["Hola", "Mundo"];

// Acceder:
console.log(numeros[0]); // 3

// Modificar:
palabras[1] = "Ben";

// Ordenación:
numeros.sort((a, b) => a - b); // Ordenar de menor a mayor

// Iteración:
for (let i = 0; i < numeros.length; i++) {
    console.log(`Índice ${i}: ${numeros[i]}`);
}

// ________________________________________________________
// 2. Sets(Colecciones de Valores Únicos)
console.log("\nConjuntos");

let miConjunto = new Set();
let otroConjunto = new Set([2, 3, 4]);

// Inserción:
miConjunto.add(1);
miConjunto.add(2);

// Buscar:
console.log(otroConjunto.has(3)); // true

// Eliminación:
miConjunto.delete(2);

// Verificación:
console.log(miConjunto.has(1)); // true

// Operaciones:
miConjunto = new Set([...miConjunto, ...otroConjunto]); // Unión

// Iteración:
otroConjunto.forEach(elemento => {
    console.log(elemento);
});

// ________________________________________________________
// 3. Maps(Pares Clave-Valor con Claves de Cualquier Tipo)
console.log("\nMaps");

let map = new Map();

// Agregar pares clave-valor:
map.set("nombre", "Zoe");
map.set("edad", 27);
map.set("activo", true);

// Acceder
console.log(map.get("nombre")); // "Zoe"
console.log(map.get("edad"));   // 27

// Verificar
console.log(map.has("activo")); // true

// Obtener el tamaño del Map:
console.log(map.size); // 3

// Modificar
map.set("edad", 28);
console.log(map.get("edad")); // 28

// Comprobar
console.log(map.has("activo")); // false

// Iteración
map.forEach((valor, clave) => {
    console.log(`Clave: ${clave}, Valor: ${valor}`);
});

for (let [clave, valor] of map) {
    console.log(`Clave: ${clave}, Valor: ${valor}`);
}

// Eliminar un par clave-valor:
map.delete("activo");

// Eliminar todos los elementos del Map:
map.clear();

// ________________________________________________________
// 4. Objects(Pares Clave-Valor para Estructuras Complejas)
console.log("Objetos");

let persona = {
    nombre: "Zoe",
    edad: 27,
    activo: true
};

// Acceder
console.log(persona.nombre); // "Zoe"
console.log(persona["edad"]); // 27

// Modificar
persona.edad = 28;
console.log(persona.edad); // 28

// Agregar
persona.pais = "España";
console.log(persona.pais); // "España"

// ________________________________________________________
// DIFICULTAD EXTRA

const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let myAgenda = new Map();

const msg_home = `
Agenda de contactos
╔═══════════════════════════╗
║ 1. Nuevo      4. Editar   ║
║ 2. Buscar     5. Eliminar ║
║ 3. Lista      6. Salir    ║
╚═══════════════════════════╝
`;

const Create = () => {
    rl.question("Escribe el nombre: ", (name) => {
        if (name.length < 1) {
            Create();
        } else if (name === "6") {
            console.log("Cancelado");
            Agenda();
        } else if (myAgenda.has(name)) {
            console.log("El nombre ya existe.");
            Create();
        } else {
            rl.question("Escribe el número: ", (number) => {
                if (isNaN(number) || number.length === 0 || number.length > 11) {
                    console.log("Número no válido.");
                    Create();
                } else {
                    myAgenda.set(name, number);
                    console.log("Guardado");
                    Agenda();
                }
            });
        }
    });
};

const Search = () => {
    rl.question("Escribe el nombre: ", (name) => {
        if (name === "6") {
            console.log("Cancelado");
            Agenda();
        } else if (myAgenda.has(name)) {
            console.log(myAgenda.get(name));
            Agenda();
        } else {
            console.log("Contacto no encontrado.");
            Agenda();
        }
    });
};

const List = () => {
    console.log("Lista de contactos:");
    const sortedAgenda = new Map([...myAgenda].sort());
    for (const [key, value] of sortedAgenda) {
        console.log(`${key}: ${value}`);
    }
    Agenda();
};

const Edit = () => {
    rl.question("Escribe el nombre: ", (name) => {
        if (name === "6") {
            console.log("Cancelado");
            Agenda();
        } else if (myAgenda.has(name)) {
            rl.question("Escribe el nuevo número: ", (newNumber) => {
                if (isNaN(newNumber) || newNumber.length === 0 || newNumber.length > 11) {
                    console.log("Número no válido.");
                    Edit();
                } else {
                    myAgenda.set(name, newNumber);
                    console.log("Contacto editado");
                    Agenda();
                }
            });
        } else {
            console.log("Contacto no encontrado.");
            Agenda();
        }
    });
};

const Delete = () => {
    rl.question("Escribe el nombre: ", (name) => {
        if (name === "6") {
            console.log("Cancelado");
            Agenda();
        } else if (myAgenda.has(name)) {
            myAgenda.delete(name);
            console.log("Contacto eliminado");
            Agenda();
        } else {
            console.log("Contacto no encontrado.");
            Agenda();
        }
    });
};

const Agenda = () => {
    rl.question("Número de opción: ", (option) => {
        switch (option) {
            case "1":
                Create();
                break;
            case "2":
                Search();
                break;
            case "3":
                List();
                break;
            case "4":
                Edit();
                break;
            case "5":
                Delete();
                break;
            case "6":
                console.log("Adiós");
                rl.close();
                break;
            default:
                console.log("Elija una opción entre 1 y 6.");
                Agenda();
                break;
        }
    });
};

Agenda();
