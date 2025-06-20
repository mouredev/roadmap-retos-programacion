/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto
 *   en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
 *   y a continuación los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no numéricos y con más
 *   de 11 dígitos (o el número de dígitos que quieras).
 * - También se debe proponer una operación de finalización del programa.
 */

// Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
    let arr: number[] = [1, 2, 3, 4, 5]; // Array de números
    console.log("Array original:", arr);            
    let arr2: string[] = ["A", "B", "C"]; // Array de cadenas de texto
    console.log("Array de cadenas:", arr2);
    let arr3: boolean[] = [true, false, true]; // Array de boolean
    console.log("Array de booleanos:", arr3);
    let arr4: (number | string)[] = [1, "dos", 3, "cuatro"]; // Array de números y cadenas
    console.log("Array mixto:", arr4);
    let arr5: Array<number> = new Array(1, 2, 3); // Otra forma de crear un array de números
    console.log("Array creado con el constructor:", arr5);
    let arr6: Array<string> = new Array("A", "B", "C"); // Otra forma de crear un array de cadenas
    console.log("Array de cadenas creado con el constructor:", arr6);
    let arr7: Array<boolean> = new Array(true, false, true); // Otra forma de crear un array de booleanos
    console.log("Array de booleanos creado con el constructor:", arr7);
    let obj: { [key: string]: number } = { "uno": 1, "dos": 2, "tres": 3 }; // Objeto con claves y valores numéricos
    console.log("Objeto original:", obj);
    let set: Set<string> = new Set(["A", "B", "C"]); // Set de cadenas de texto
    console.log("Set original:", set);
    let map: Map<string, number> = new Map([["uno", 1], ["dos", 2], ["tres", 3]]); // Mapa con claves de tipo cadena y valores numéricos
    console.log("Mapa original:", map);

// Utiliza operaciones de inserción, borrado, actualización y ordenación.
    arr.push(6); // Inserción
    console.log("Array después de insertar 6:", arr);
    arr.splice(0, 1); // Borrado
    console.log("Array después de borrar el primer elemento:", arr);
    arr[0] = 10; // Actualización
    console.log("Array después de actualizar el primer elemento a 10:", arr);
    arr.sort((a, b) => a - b); // Ordenación
    console.log("Array después de ordenar:", arr);
    obj["cuatro"] = 4; // Inserción
    console.log("Objeto después de insertar 'cuatro':", obj);
    delete obj["dos"]; // Borrado
    console.log("Objeto después de borrar 'dos':", obj);
    obj["uno"] = 11; // Actualización
    console.log("Objeto después de actualizar 'uno' a 11:", obj);
    set.add("D"); // Inserción
    console.log("Set después de insertar 'D':", set);
    set.delete("B"); // Borrado
    console.log("Set después de borrar 'B':", set);
    set.forEach(value => console.log("Valor en el set:", value)); // Iteración
    map.set("cuatro", 4); // Inserción
    console.log("Mapa después de insertar 'cuatro':", map);
    map.delete("dos"); // Borrado
    console.log("Mapa después de borrar 'dos':", map);    
    map.set("uno", 11); // Actualización
    console.log("Mapa después de actualizar 'uno' a 11:", map);

// DIFICULTAD EXTRA (opcional):

//  Crea una agenda de contactos por terminal.    
//  - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
//  - Cada contacto debe tener un nombre y un número de teléfono.   

//  - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
//    y a continuación los datos necesarios para llevarla a cabo.
//  - El programa no puede dejar introducir números de teléfono no numéricos y con más
//    de 11 dígitos (o el número de dígitos que quieras).
//  - También se debe proponer una operación de finalización del programa.

//  - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
//    y a continuación los datos necesarios para llevarla a cabo.
//  - El programa no puede dejar introducir números de teléfono no numéricos y con más
//    de 11 dígitos (o el número de dígitos que quieras).
//  - También se debe proponer una operación de finalización del programa.
let agenda: Map<string, string> = new Map();
function isValidPhoneNumber(phone: string): boolean {
    const phoneRegex = /^\d{1,11}$/; // Validación de números de teléfono de hasta 11 dígitos
    return phoneRegex.test(phone);
}
function showMenu() {
    console.log("Seleccione una operación:");
    console.log("1. Insertar contacto");
    console.log("2. Actualizar contacto");
    console.log("3. Eliminar contacto");
    console.log("4. Buscar contacto");
    console.log("5. Mostrar agenda");
    console.log("6. Salir");
}
function insertContact(name: string, phone: string) {
    if (isValidPhoneNumber(phone)) {
        agenda.set(name, phone);
        console.log(`Contacto ${name} insertado con éxito.`);
    } else {
        console.log("Número de teléfono no válido.");
    }
}
function updateContact(name: string, phone: string) {
    if (agenda.has(name)) {
        if (isValidPhoneNumber(phone)) {
            agenda.set(name, phone);
            console.log(`Contacto ${name} actualizado con éxito.`);
        } else {
            console.log("Número de teléfono no válido.");
        }
    } else {
        console.log(`Contacto ${name} no encontrado.`);
    }
}
function deleteContact(name: string) {
    if (agenda.has(name)) {
        agenda.delete(name);
        console.log(`Contacto ${name} eliminado con éxito.`);
    } else {
        console.log(`Contacto ${name} no encontrado.`);
    }
}
function searchContact(name: string) {
    if (agenda.has(name)) {
        console.log(`Contacto encontrado: ${name} - ${agenda.get(name)}`);
    } else {
        console.log(`Contacto ${name} no encontrado.`);
    }
}
function showAgenda() {
    if (agenda.size > 0) {
        console.log("Agenda de contactos:");
        agenda.forEach((phone, name) => {
            console.log(`${name}: ${phone}`);
        });
    } else {
        console.log("La agenda está vacía.");
    }
}
function main(): void {
    showMenu();

    const operation = prompt("Seleccione una operación (1-6):");

    switch (operation) {
        case '1': {
            const name = prompt("Ingrese el nombre del contacto:");
            const phone = prompt("Ingrese el número de teléfono:");
            if (name && phone) {
                insertContact(name, phone);
            }
            main();
            break;
        }
        case '2': {
            const name = prompt("Ingrese el nombre del contacto a actualizar:");
            const phone = prompt("Ingrese el nuevo número de teléfono:");
            if (name && phone) {
                updateContact(name, phone);
            }
            main();
            break;
        }
        case '3': {
            const name = prompt("Ingrese el nombre del contacto a eliminar:");
            if (name) {
                deleteContact(name);
            }
            main();
            break;
        }
        case '4': {
            const name = prompt("Ingrese el nombre del contacto a buscar:");
            if (name) {
                searchContact(name);
            }
            main();
            break;
        }
        case '5':
            showAgenda();
            main();
            break;
        case '6':
            console.log("Saliendo del programa.");
            break;
        default:
            console.log("Operación no válida. Intente nuevamente.");
            main();
    }
}
// Iniciar el programa
console.log("Bienvenido a la agenda de contactos.");
main();