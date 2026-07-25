// Array ******************************************************************** //

let lista = [4, 6, 1, 7, 5, 8, 2, 3]
console.log("Lista original: " + lista)

//Inserción
lista.push(0) //Agrego un elemento al final de la lista 
// [4, 6, 1, 7, 5, 8, 2, 3, 0]

lista.unshift(9) //Agrego un elemento al principio de la lista
// [9, 4, 6, 1, 7, 5, 8, 2, 3, 0]

lista.splice(2, 0, 10) //Agrego el 10 en la posición 3
// [9, 4, 10, 6, 1, 7, 5, 8, 2, 3, 0]

//Borrado
lista.pop() //Elimino el ultimo elemento de la lista
// [9, 4, 10, 6, 1, 7, 5, 8, 2, 3]

lista.shift() //Elimino el primer elemento de la lista
// [4, 10, 6, 1, 7, 5, 8, 2, 3]

lista.splice(3, 1) //Elimino el elemento en la posición 4
// [4, 10, 6, 7, 5, 8, 2, 3]

//Actualización
lista[6] = 9 //Reemplazo el elemento de la posición 7
// [4, 10, 6, 7, 5, 8, 9, 3]

//Ordenación
lista.sort(function (a, b) { return a - b }) //Ordeno la lista de menor a mayor
// [3, 4, 5, 6, 7, 8, 9, 10]

lista.reverse(function (a, b) { return a - b }) //Ordeno la lista de mayor a menor
// [10, 9, 8, 7, 6, 5, 4, 3]

// Objet ******************************************************************** //
var person = {
    name: "Fra",
    lastname: "velz",
    age: 9999999n
}

//Inserción
person["ciudad"] = "Rosario"
// { name: 'Fra', lastname: 'velz', age: 9999999n, ciudad: 'Rosario' }

//Borrado
delete person.lastname
// { name: 'Fra', age: 9999999n, ciudad: 'Rosario' }

//Actualización
person.name = "Javier"
// { name: 'Javier', age: 9999999n, ciudad: 'Rosario' }

// Map ********************************************************************** //

let mapa = new Map()

//Inserción
mapa.set("rojo", "red")
mapa.set("verde", "green")
mapa.set("azul", "blue")
// { 'rojo' => 'red', 'verde' => 'green', 'azul' => 'blue' }

//Borrado
mapa.delete("verde")
// { 'rojo' => 'red', 'azul' => 'blue' }

//Actualización
mapa.set("rojo", "vermelho")
// { 'rojo' => 'vermelho', 'azul' => 'blue' }

let mapa2 = new WeakMap();

/* { <object> => 'valor' } a diferencia del Map, el WeakMap no impide que el
objeto clave sea recolectado por el garbage collector si no hay otras referencias
a él. Esto significa que si el objeto clave es eliminado, la entrada
correspondiente en el WeakMap también será eliminada automáticamente.
*/

// Set ********************************************************************** //

let numeros = new Set([4, 6, 1, 7])
// { 4, 6, 1, 7 }

//Inserción
numeros.add(0)
// { 4, 6, 1, 7, 0 }

//Borrado
numeros.delete(1)
// { 4, 6, 7, 0 }

let sets = new WeakSet();

/* { <object>, <object>, ... } a diferencia del Set, el WeakSet no impide que los
objetos sean recolectados por el garbage collector si no hay otras referencias
a ellos. Esto significa que si un objeto es eliminado, la entrada correspondiente
en el WeakSet también será eliminada automáticamente.
*/

/* *****************************************************************************
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
***************************************************************************** */


var agenda = new Map()
var nombre
var telefono
var op

import readline from 'readline'


function obtenerInput(pregunta) {
    const rl = readline.createInterface({ input: process.stdin, output: process.stdout })

    return new Promise((resolve) => {
        rl.question(pregunta, (respuesta) => {
            resolve(respuesta); rl.close();
        });
    });
}

do {
    console.log(`\n****************************************`);
    console.log("* 1. Search contact");
    console.log("* 2. Add contact");
    console.log("* 3. Update contact");
    console.log("* 4. Delete contact");
    console.log("* 5. Exit");
    console.log(`****************************************`);

    op = await obtenerInput('* > Please enter an option: ');

    switch (op) {
        case "1":
            nombre = await obtenerInput("* > Enter name to search: ");

            if (agenda.get(nombre))
                console.log(`The phone number for ${nombre} is: ${agenda.get(nombre)}`);
            else
                console.log(`The contact ${nombre} does not exist in the agenda`);
            break;

        case "2":
            nombre = await obtenerInput('Name: ');
            telefono = await obtenerInput('Phone number: ');

            if (!isNaN(telefono) && telefono.length > 0 && telefono.length < 12) {
                agenda.set(nombre, telefono);
                console.log("The contact was successfully created");
            } else {
                console.log("You must enter a number with less than 12 digits");
            }

            break;

        case "3":
            nombre = await obtenerInput('* > Enter the name of the contact to update: ');

            if (agenda.get(nombre)) {
                telefono = await obtenerInput('* > Enter the new phone number: ');
                if (!isNaN(telefono) && telefono.length > 0 && telefono.length < 12) {
                    agenda.set(nombre, telefono);
                    console.log("The contact was successfully updated");
                } else {
                    console.log("You must enter a number with less than 12 digits");
                }
            } else {
                console.log(`The contact ${nombre} does not exist in the agenda`);
            }
            break;

        case "4":
            nombre = await obtenerInput('* > Enter the name of the contact to delete: ');
            if (agenda.get(nombre)) {
                agenda.delete(nombre);
                console.log(`The contact ${nombre} was successfully deleted`);
            } else {
                console.log(`The contact ${nombre} does not exist in the agenda`);
            }
            break;

        default: console.log("Invalid option. Please try again.");
    }
} while (op != "5");

// > Autor: Fravelz
