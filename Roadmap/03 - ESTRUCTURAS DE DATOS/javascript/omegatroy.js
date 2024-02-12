/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 * DIFICULTAD EXTRA (opcional):
 * - Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
 */

// Arrays conjunto de elementos del mismo tipo o diferentes tipos
let myArray = [10,7,9,4,5];
let myArray2 = ['hola',2,true,[1,"mundo"]];

// Insertar un nuevo elemento del array
myArray.push(10)

console.log(myArray)
console.log(myArray2)

// Borrar un elemento del array 
myArray.pop() // --> Elimino el ultimo elemento (10)
console.log(myArray)

  //Actualizar un valor de un array 
  //  0,1,2,3,4 --> posición de los elemantos
  // [1,2,3,4,13]
myArray.splice(4,1,13) // --> Primer parámetro (4) indico la posición del número a modificar
console.log(myArray)   // --> Segundo parámetro (1) indico cuantos elementos quiero modificar
                        // --> Tercer parámetro (13) indico el valor nuevo modificado

// ordenar arrays
myArray.sort((a,b)=> a-b) // con esa arrow function indico que me los ordene de menor a mayor
console.log(myArray)


//Maps almacenan pares clave-valor pero con más flexibilidad que los objetos
// Forma 1
let mapStructura = new Map([
  ["uno", 1],
  ["dos", 2],
  ["tres", 3],
  ["cuatro", 4],
  ["cinco", 11],
]);

mapStructura.set("seis", 6); //Inserción
mapStructura.delete("seis"); //Borrado
mapStructura.get("cinco"); //Busqueda
mapStructura.set("cinco", 5); //Actualización
mapStructura.clear(); //Borrado - Elimina todos los elementos


// Forma 2
let newMap = new Map()
newMap.set("lenguaje","Javascript")
newMap.set("area","front")
console.log(newMap)

//Insertar un elemento en un Map
newMap.set("back","Java")
console.log(newMap)

//Borrar un elemento del mapa
newMap.delete("area")
console.log(newMap)

//Actualizar el valor de un mapa
newMap.set("back","Rust")
console.log(newMap)


// Sets Colección de valores únicos donde no puede haber duplicados
let mySet = new Set ([1,2,3,4,5])
console.log(mySet)
//Insertar un elemento en un Set
mySet.add(6)
console.log(mySet)

//Borrar un elemento del set
mySet.delete(4)
console.log(mySet)

//Actualizar un elemento en el set
/*No se puede cambiar el valor de un elemento pero
si podemos quitar y añadir como hemos visto antes*/

//Ordenar sets 
/*
  Para ordenar los elementos de un set primero lo convertimos a array 
  y luego ordenamos sus elementos como hemos hecho anteriormente 
*/
