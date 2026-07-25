/**
 * Estructuras de datos en typescript
 * 
 * @author rubenplazavi
 * @version 1.0
 * 
 * 
 * index:
 * 1. Arrays
 * 2. Tuplas
 * 3. Enumeraciones
 * 4. Objetos
 * 5. Mapas
 * 6. Conjuntos
 * 7. Pilas
 * 8. Colas
 * 9. Listas enlazadas
 * 10. Árboles
 * 11. Grafos
 * 
 * 
 * * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 * 
 *  * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
 */

//!--------------------- Arrays -------------------
console.log("Arrays");
let arrayOfNumbers: number[] = [1,2,3,4,5];
let arrayOfNumbers2: Array<number> = new Array(1,2,3,4,5);
let arrayOfNumbers3: number[] = [];

let arrayOfStrings: Array<string> = ["a","b","c","d","e"];
let ArrayOfMixedTypes: Array<any> = ["a", 1, {name:"John", surname:"Doe"}, true];

console.log("array of numbers: ",arrayOfNumbers);
console.log(arrayOfNumbers2);
console.log(arrayOfNumbers3);
console.log("array of strings: ", arrayOfStrings);
console.log("array of mixed types: ", ArrayOfMixedTypes);

//Inserción
arrayOfNumbers.push(6);
console.log(arrayOfNumbers);

//Borrado
arrayOfNumbers.pop();
console.log(arrayOfNumbers);

arrayOfNumbers.splice(1, 1);
console.log("Borrado 2o elemento: ", arrayOfNumbers);

//Actualizacion
arrayOfNumbers[2] = 7;
console.log("actualizacion de array de numeros: ", arrayOfNumbers);

arrayOfStrings[2] = "w";
console.log("actualizacion de array de strings: ", arrayOfStrings);	

//Ordenacion
arrayOfNumbers.sort((a, b) => b - a);
console.log("Ordenacion descendente de array de numeros: ",arrayOfNumbers);

arrayOfStrings.sort((a, b) => b.localeCompare(a));
console.log("Ordenacion descendente de array de strings: ",arrayOfStrings);

//!--------------------- Tuplas -------------------

let product: [number, string] = [1, "Tornillos"];
console.log(product[0], product[1]);

product.push(2, "Ladrillos");
product.push(3, "Pisos");

console.log(product);

product.pop();
product.pop();

console.log(product);

console.log(product[1])


//!--------------------- Enumeraciones -------------------
/**
 * Un enum (enumeración) en TypeScript es un tipo de dato especial que permite definir un conjunto de constantes con nombre.
 * Los enums en TypeScript tienen dos tipos principales: enum numéricos y enum de cadena.
 * 
 * Uso: Permiten a las variables ser uno de los valores predefinidos, mejorando la legibilidad y seguridad del código.
 * Valores Específicos: Pueden tener valores numéricos o strings específicos.
 * Operaciones: Se pueden convertir entre strings y números, y se pueden iterar, pero no se pueden modificar después de su definición.
 */
enum DAYS{
    Lunes = 1,
    Martes = 2,
    Miercoles = 3,
    Jueves = 4,
    Viernes = 5,
    Sabado = 6,
    Domingo = 7,
}
enum WEEK_DAYS{
    Lunes = "lunes",
    Martes = "martes",
    Miercoles = "miercoles",
    Jueves = "jueves",
    Viernes = "viernes",
    Sabado = "sabado",
    Domingo = "domingo",
}

console.log("iterar enmueracion dias de la semana cuando son strings: ");
for( let day in WEEK_DAYS){
    console.log(WEEK_DAYS[day]);
}

console.log("iterar enmueracion dias de la semana cuando son numéricos\n (nota, en este caso, es bidireccional, escribe la clave y el valor del enum): ");
Object.keys(DAYS).forEach(key => console.log(key));


//!--------------------- Objetos -------------------
//Creacion
type User = {
    name: string,
    surname: string,
    age: number,
    address?: {
        street: string,
        number: number,
        city: string,
        country?: string
    }
}
const carlos: User = {
    name: "Carlos",
    surname: "Perez",
    age: 30,
}
console.log("Datos Usuario Carlos: ", carlos);

//Inserción
carlos.address = {
    street: "Calle Mayor",
    number: 1,
    city: "Madrid",
    country: "España"
}
console.log("Datos añadidos de direccion para Carlos: ", carlos);

//Borrado
// delete carlos.age;  // No se puede borrar la edad, porque es campo obligatorio
//? Todo lo que se quiera borrar debe ser opcional en la declaración del tipo

delete carlos.address.country;
console.log("Datos address pais borrados: ", carlos);
console.log(arrayOfNumbers);

//Actualizacion
carlos.age = 31;
console.log("Datos Actualizados edad Carlos: ", carlos);

//Ordenacion

//!--------------------- Maps -------------------
/**
 * Los objetos Map son colecciones de tuplas tipo llave-valor. Una llave en Map puede aparecer solo una vez; 
 * es única en la colección de Map. Un objeto Map es iterado por sus tuplas llave-valor —un bucle for...of 
 * regresa un arreglo de [llave, valor] por cada iteración. La iteración sucede en orden de inserción, 
 * la cual corresponde al orden en el que cada tupla llave-valor fue incertada inicialmente en el map por el método set()
 *  (eso es, si no había una llave con el mismo valor en el map, cuando set() fué llamado).

La especificación requiere que los maps sean implementados "que, en promedio, proporcione tiempos de acceso que 
sean sublineales al numero de elementos en la colección". Por lo tanto, podría ser representado internamente como una 
tabla hash (con una busqueda O(1)), un árbol de búsqueda (con una busqueda de O(log(N))), o cualquier otra estructura de 
datos, mientras la complejidad sea mejor que O(N).
 */

//Creación
const mapInicializado: Map<string, any> = new Map([["name", "Miriam"], ["surname", "Rosado"]]); // Solo para la inicializacion se puede varios valores
let variableMap = new Map();  // implícito Map<any, any>



console.log("mapInicializado: ", mapInicializado.set("age", 30));
console.log("variableMap (sin inicializar): ", variableMap);

//Inserción
variableMap.set("age", 30);
variableMap.set("name", "Carlos");
variableMap.set("surname", "Perez");

mapInicializado.set("age", 30);
mapInicializado.set("address", {
    street: "Calle Mayor",
    number: 1,
    city: "Madrid",
    country: "España"
});

console.log("mapInicializado y con inserción de edad y address: ", mapInicializado.set("age", 30));
console.log("variableMap ya inicializada: ", variableMap);

//Borrado
mapInicializado.delete("surname");

mapInicializado.size;

//Actualizacion
mapInicializado["age"]= 31;

console.log("mapInicializado con actualizacion de edad: ", mapInicializado);

// Claves
const keys: IterableIterator<string> = mapInicializado.keys();

//Ordenacion
//?En este caso no se puede ordenar, está ordenado pororden de inserción...


//!--------------------- Sets -------------------

/** Los objetos Set son colecciones de valores. Puede iterar a través de los elementos de un conjunto en orden 
 * de inserción. Un valor en un Set solo puede ocurrir una vez; es único en la colección del Set.
*/

// creación
let mySet1 = new Set([1,"Carlos", true]);
console.log("mi primer set: ",mySet1);


//Inserción
mySet1.add("Carpintero");
// No se le puede añadir un objeto al set:
/**
 * 
 * This code attempts to add an object additionalValues to the set mySet1. However, since sets in TypeScript only store
 * unique primitive values, adding an object will not work as expected. Instead, it will add the object as a reference,
 * and if the same object is added again, it will be treated as a duplicate and not added to the set. If you want to add 
 * unique key-value pairs to a data structure, you might want to consider using a Map instead
 * 
 * Error de compilación: ------------------------------------
 * const additionalValues = {a:1, b:3};
 * mySet1.add(additionalValues);
 * 
 */
mySet1.add(1); // solo admite valores únicos, como el 1 ya está no lo va a añadir
mySet1.add("Carlos");
console.log("mi set con un nuevo elemento: ",mySet1);

//Borrado
mySet1.delete("Carpintero");
console.log("mi set borrando carpintero: ",mySet1);

//Actualizacion
//? No se pueden actualizar los valores de un Set, solo es válido para almacenar datos únicos

//Ordenacion
//? No se pueden ordenar los set

console.log("Metodo has, para comprobar si existe el elemento dentro del set: ",mySet1.has("carpintero"));
mySet1.has("Carlos");



//!--------------------- Conjuntos -------------------
//!--------------------- Pilas -------------------
//!--------------------- Colas -------------------
//!--------------------- Listas enlazadas -------------------
//!--------------------- Árboles -------------------
//!--------------------- Grafos -------------------