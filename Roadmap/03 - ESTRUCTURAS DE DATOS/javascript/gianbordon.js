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
 * - El programa no puede dejar introducir números de teléfono no numéricos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
 */

// Arrays

console.group("Arrays:");

//
// Creación de un Array
//
let numeros = [1, 2, 3, 4, 6, 7, 8, 9];
console.log("Array inicial:", numeros);

//
// Adición de elementos
//
numeros.push(10); // Agrega al final
console.log("Adición con push:", numeros);

numeros.unshift(0); // Agrega al principio
console.log("Adición con unshift:", numeros);

//
// Eliminación de elementos
//
numeros.pop(); // Elimina el último
console.log("Eliminación con pop:", numeros);

numeros.shift(); // Elimina el primero
console.log("Eliminación con shift:", numeros);

//
// Eliminación con splice
//
let numerosII = numeros.splice(4, 1); // Elimina desde el índice 4, 1 elemento
console.log(
    "Eliminación con splice:",
    "Resultado:",
    numeros,
    "Eliminado:",
    numerosII
);

//
// Modificación de un elemento
//
numeros[3] = 10; // Cambia el valor en el índice 3
console.log("Modificación de valor:", numeros);

//
// Ordenación del array
//
numeros.sort((a, b) => a - b); // Orden ascendente
console.log("Array ordenado:", numeros);

//
// Métodos adicionales
//
console.log("¿Incluye el 3?:", numeros.includes(3));
console.log("Índice del número 3:", numeros.indexOf(3));
console.log("Array invertido:", numeros.reverse());

console.groupEnd();

/// Objetos

console.group("Objetos:");

//
// Creación de un objeto
//
let persona = {
    name: "Gian",
    age: 26,
    email: "gianbordonpresti@hotmail.com",
    saludar() {
        console.log(`Hola, soy ${this.name}`);
    },    
};
console.log("Objeto inicial:", persona);

//
// Acceso a propiedades del objeto
//
console.log("Acceso con punto:", persona.name);
console.log("Acceso con corchetes:", persona["age"]);

//
// Métodos útiles de objetos
//
console.log("Claves del objeto:", Object.keys(persona));
console.log("Valores del objeto:", Object.values(persona));
console.log("Entradas del objeto:", Object.entries(persona));

//
// Uso de método dentro del objeto
//
persona.saludar();

//
// Agregar nuevas propiedades
//
persona.surname = "Bordon";
persona["alias"] = "Giasin";
console.log("Después de agregar propiedades:", persona);

//
// Eliminar propiedades
//
delete persona.alias;
console.log("Después de eliminar alias:", persona);

//
// Modificar propiedades existentes
//
persona.surname = "Prestifilippo";
persona.age = 34;
console.log("Después de modificar propiedades:", persona);

//
// Función constructora de objetos
//
function Person(name, surname, age, alias) {
    this.name = name;
    this.surname = surname;
    this.age = age;
    this.alias = alias;
}

const personaCreada = new Person("Estevan", "Ruiz", 23, "Estevanquito");
console.log("Objeto creado con función constructora:", personaCreada);

console.groupEnd();

// Sets

console.group("Sets:");

//
// Creación de un Set
//
let animal = new Set(["perro", "golden", 4, "Adoptado"]);
console.log("Set inicial:", animal);

//
// Agregar elementos al Set
//
animal.add("Familia Perez");
console.log("Después de agregar un elemento:", animal);

//
// Eliminar elementos del Set
//
animal.delete("perro");
animal.delete(4);
console.log("Después de eliminar elementos:", animal);

//
// Verificar existencia de un valor
//
console.log("¿Contiene 'Adoptado'?:", animal.has("Adoptado"));

//
// Obtener tamaño del Set
//
console.log("Tamaño del Set:", animal.size);

//
// Convertir Set en Array y viceversa
//
let arr = Array.from(animal);
console.log("Convertido a Array:", arr);

animal = new Set(arr);
console.log("Convertido nuevamente a Set:", animal);

//
// Metodo Clear
//
animal.clear();
console.log("Set después de clear():", animal);

console.groupEnd();

// Maps

console.group("Maps:");

//
// Declaración de un Map vacío
//
let materia = new Map();
console.log("Map vacío:", materia);

//
// Inicialización con pares clave-valor
//
materia = new Map([
    ["name", "Lengua"],
    ["Horario", "11hs a 13hs"],
    ["Profesor", "Dominguez"],
]);
console.log("Map inicializado:", materia);

//
// Inserción de un nuevo valor
//
materia.set("curso", "3º B");
console.log("Después de insertar 'curso':", materia);

//
// Modificación de un valor existente
//
materia.set("Horario", "9 a.m. a 11 a.m.");
console.log("Después de modificar 'Horario':", materia);

//
// Eliminación de un valor
//
materia.delete("Profesor");
console.log("Después de eliminar 'Profesor':", materia);

//
// Verificación de existencia (has)
//
console.log("¿Existe 'Horario'?:", materia.has("Horario"));
console.log("¿Existe 'Profesor'?:", materia.has("Profesor"));

//
// Obtener claves, valores y entradas
//
console.log("Claves:", materia.keys());
console.log("Valores:", materia.values());
console.log("Entradas:", materia.entries());

//
// Tamaño del Map
//
console.log("Tamaño del Map:", materia.size);

//
// Transformar en Array y viceversa
//
let arrDesdeMap = Array.from(materia);
console.log("Map convertido a Array:", arrDesdeMap);

materia = new Map(arrDesdeMap);
console.log("Array reconvertido a Map:", materia);

//
// Vaciar el Map
//
materia.clear();
console.log("Después de clear():", materia);

console.groupEnd();

//
// EXTRA
//

const agenda = [];
const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

function menu() {
    console.clear();

    console.log("╔═══════════════════════════════════════╗");
    console.log("║         📒 AGENDA DE CONTACTOS        ║");
    console.log("╠═══════════════════════════════════════╣");
    console.log("║ 1. Agregar contacto                   ║");
    console.log("║ 2. Buscar contacto                    ║");
    console.log("║ 3. Actualizar contacto                ║");
    console.log("║ 4. Eliminar contacto                  ║");
    console.log("║ 5. Mostrar todos                      ║");
    console.log("║ 0. Salir                              ║");
    console.log("╚═══════════════════════════════════════╝");

    rl.question("Seleccioná una opción (1 al 6): ", (opc) => {
        switch (opc) {
        case "1":
            console.log("→ Elegiste AGREGAR contacto.");
            addContact()
            break;
        case "2":
            console.log("→ Elegiste BUSCAR contacto.");
            searchContact()
            break;
        case "3":
            console.log("→ Elegiste ACTUALIZAR contacto.");
            modifyContact()
            break;
        case "4":
            console.log("→ Elegiste ELIMINAR contacto.");
            deleteContact()
            break;
        case "5":
            console.log("→ Elegiste MOSTRAR todos.");
            showContacts()
            break;
        case "0":
            console.log("→ Programa finalizado.");
            rl.close();
            break;
        default:
            console.log("❌ Opción inválida.");
            setTimeout(menu, 1500); 
        }
    });
}

function Contact(name, num) {
    this.name = name;
    this.num = num;
}

function verifyNumber(num) {
    const onlyNumbers = /^\d+$/;
    if (!onlyNumbers.test(num)) {
        console.log('❌ El valor ingresado no contiene solo números');
        return null;
    }
    if (num.length >= 11) {
        return num;
    } else {
        console.log('❌ El número no es mayor o igual a 11');
        return null;
    }
}

function addContact() {
    rl.question("Introduzca el nombre del contacto que desea agregar: ", (name) => {
        const requestNumber = () => {
            rl.question("Introduzca el número del contacto (exactamente 11 dígitos): ", (num) => {
                const numeroVerificado = verifyNumber(num);
                if (numeroVerificado) {
                    const contact = new Contact(name, numeroVerificado);
                    agenda.push(contact);
                    console.log(`✅ Contacto agregado: ${contact.name} - ${contact.num}`);
                    backToMenu();
                } else {
                    console.log("🔁 Número inválido. Intente nuevamente.\n");
                    requestNumber(); 
                }
            });
        };
        requestNumber(); 
    });
}

function contactFound(value){
    let index = - 1
    agenda.forEach((contact, i)=>{
        if(contact.name.toLowerCase().includes(value.toLowerCase()) ||              
            (contact.num.toLowerCase().includes(value.toLowerCase()))){
                console.log(`🔎 Contacto encontrado: ${contact.name} - ${contact.num}`);
                index = i;
        }
    })
    if (index === -1) {
        console.log("❌ No se encontró ningún contacto con ese criterio.");
    }
    backToMenu()
}

function searchContact(name){
    rl.question("🔍 Ingrese el nombre o número a buscar: ", (name) =>{
        contactFound(name)
    })
    backToMenu()
}

function searchIndex(value){
    let index = - 1
    agenda.forEach((contact, i)=>{
        if(contact.name.toLowerCase().includes(value.toLowerCase()) ||              
            (contact.num.toLowerCase().includes(value.toLowerCase()))){
                index = i;
                return
        }
    })
    return index
}

function modifyContact(){
    rl.question("🔍 Ingrese el nombre o número a buscar: ", (name) =>{
        const index = searchIndex(name)
        if(index === -1){
            console.log("❌ No se encontró ningún contacto con ese criterio.");
            return backToMenu()
        }
        console.log(`🔎 Contacto encontrado: ${agenda[index].name} - ${agenda[index].num}`);
        console.log("╔═══════════════════════════════════════╗");
        console.log("║ 1. Nombre                             ║");
        console.log("║ 2. Número                             ║");
        console.log("╚═══════════════════════════════════════╝");
        rl.question("Seleccione la opcion que desea modificar? ", (res) =>{

            switch (res) {
                case "1":
                    rl.question("Ingrese el nuevo nombre:",(name)=>{
                        agenda[index].name = name
                        console.log("✅ Nombre actualizado.")
                        backToMenu()
                    })
                    break;
                case "2":
                    rl.question("Ingrese el nuevo numero", (num)=>{
                        const numVerf = verifyNumber(num)
                        if(numVerf){
                            agenda[index].num = num
                            console.log("✅ Número actualizado.")
                        } else {
                            console.log("❌ Número inválido. No se modificó.");
                        }
                        backToMenu()
                    })
                    break
                default: 
                    console.log("❌ Opción no válida.");
                    backToMenu()
                    break;
            }
        })
    })
}

function deleteContact(){
    rl.question("🔍 Ingrese el nombre o número a buscar: ", (name) =>{
        const index = searchIndex(name)
        if(index === -1){
            console.log("❌ No se encontró ningún contacto con ese criterio.");
            return backToMenu()
        } else {
            console.log(`⚠️ Eliminando contacto: ${agenda[index].name} - ${agenda[index].num}`);
            agenda.splice(index, 1);
            console.log("✅ Contacto eliminado correctamente.");
        }
        backToMenu()
    })
}

function showContacts() {
    console.log("📋 Contactos en la agenda:");
    if (agenda.length === 0) {
        console.log("→ No hay contactos aún.");
    } else {
        agenda.forEach((c, i) => {
            console.log(`${i + 1}. ${c.name} - ${c.num}`);
        });
    }
    backToMenu();
}


function backToMenu() {
    rl.question("Presioná ENTER para volver al menú...", () => {
        menu();
    });  
}
menu();