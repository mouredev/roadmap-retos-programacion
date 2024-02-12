
//ESTRUCTURAS DE DATOS EN JS

/*
ALgunas de las estructuras soportadas en javascript son:

1. Arrays
2. Objects
3. Strings
4. Sets
5. Maps
6. Colas (Queues) y Pilas (Stacks):

*/

//*  1 ARRAYS ----- 

/*
un array (también conocido como arreglo o matriz) 
es una estructura de datos que almacena elementos del 
mismo tipo en una secuencia ordenada. Cada elemento en 
un array ocupa una posición específica, y se puede acceder 
a ellos mediante un índice o posición.
En el contexto de JavaScript, un array puede contener 
elementos de cualquier tipo, ya sean números, cadenas de texto, 
objetos u otros arrays.

Los arrays son muy utilizados en programación debido a su 
capacidad para almacenar y organizar datos de manera eficiente. 
Pueden ser utilizados en una variedad de situaciones, como la 
implementación de listas, colas, pilas y muchas otras estructuras 
de datos. Además, los arrays proporcionan métodos y propiedades 
útiles que facilitan la manipulación y gestión de los datos 
almacenados en ellos.

SINTAXIS:

indice        0 1 2 3     el indice siempre empieza en 0
Let array = [ a,b,c,d ];  cuerpo de array

*/

// INSERCIÓN EN UN ARRAY
// Al final del array
let miArray = [1, 2, 3];
miArray.push(4);
// Resultado: miArray = [1, 2, 3, 4]

// Al principio del array
let miArray2 = [2, 3, 4];
miArray.unshift(1);
// Resultado: miArray = [1, 2, 3, 4]

//En una posicion Específica
let miArray3 = [1, 2, 4];
miArray.splice(2, 0, 3);
// Resultado: miArray = [1, 2, 3, 4]

/*

Explicacion de Splice -----

El primer argumento (2) es el índice en el cual comenzará la modificación. 
En este caso, se empieza en el índice 2, que es la posición después de 2 en el array.

El segundo argumento (0) indica cuántos elementos se deben eliminar desde 
el índice especificado. En este caso, 0 significa que no se eliminará ningún elemento.

Los argumentos restantes (3) son los elementos que se agregarán al array a partir 
del índice especificado. En este caso, se agrega el elemento 3 en el índice 2.

*/

// BORRADO EN UN ARRAY
//Al final de array
let miArray4 = [1, 2, 3, 4];
miArray.pop();
// Resultado: miArray = [1, 2, 3]

//Al inicio del array
let miArray5 = [1, 2, 3];
miArray.shift();
// Resultado: miArray = [2, 3]

//En una posición específica
let miArray6 = [1, 2, 3, 4];
miArray.splice(1, 1);
// Resultado: miArray = [1, 3, 4]


// ACTUALIZACION  EN UN ARRAY
//Reasignando valores
let miArray7 = [1, 2, 3];
miArray[1] = 4;
// Resultado: miArray = [1, 4, 3]

//En una posicion específica
let miArray8 = [1, 2, 4];
miArray.splice(1, 1, 10);
// Resultado: miArray = [1, 10, 4]

//En una posicion especifica
let miArray9 = [1, 2, 4];
miArray.fill(10, 1, 2);
// Resultado: miArray = [1, 10, 4]

//Creando un nuevo array
let miArray10 = [1, 2, 4];
let nuevoArray1 = miArray.map((elemento, indice) => (indice === 1 ? 10 : elemento));
// Resultado: miArray = [1, 10, 4]

/*
map crea un nuevo array aplicando una función a cada elemento del array original. 
En este caso, se verifica si el índice es 1 y se actualiza ese elemento a 10.
*/

// Operador de propagacion
let miArray11 = [1, 2, 4];
let nuevoArray2 = [...miArray.slice(0, 1), 10, ...miArray.slice(2)];
// Resultado: miArray = [1, 10, 4]

/*

Explicacion operador de propagacion

miArray es el array original que contiene los elementos [1, 2, 4].

miArray.slice(0, 1) devuelve una porción del array desde el índice 0 (inclusive) 
hasta el índice 1 (exclusive). En este caso, devuelve [1].

...miArray.slice(0, 1) utiliza el operador de propagación para descomponer los 
elementos de la porción obtenida. Esto es necesario para incluir los elementos 
individualmente en el nuevo array.

10 es el valor que queremos insertar o actualizar en el array.

...miArray.slice(2) realiza una operación similar a la primera parte, obteniendo 
los elementos desde el índice 2 hasta el final del array. En este caso, devuelve [4].

Finalmente, todos estos fragmentos se combinan en un nuevo array llamado nuevoArray 
utilizando el operador de propagación. El resultado es [1, 10, 4].

*/

/*
Explicacion metodo fill

10 es el valor con el que se llenarán los elementos.
1 es el índice de inicio (inclusive) desde el cual comenzará a llenarse.
2 es el índice de fin (exclusive) hasta el cual se llenarán los elementos.
En este caso, fill llenará los elementos desde el índice 1 (inclusive) hasta el 
índice 2 (exclusive) con el valor 10.

Como resultado, el array miArray se modifica, y ahora contiene los elementos [1, 10, 4].

*/


// ORDENACIÓN DE UN ARRAY 
//Ascendente
let miArray = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5];
miArray.sort((a, b) => a - b);
// Resultado: miArray = [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

//Descendente
let miArray = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5];
miArray.sort((a, b) => b - a);
// Resultado: miArray = [9, 6, 5, 5, 5, 4, 3, 3, 2, 1, 1]



//* 2 OBJECTS -----

/*

En JavaScript, un objeto es una estructura de datos que permite almacenar 
y organizar datos mediante pares clave : valor. Cada valor almacenado en un 
objeto está asociado a una clave única, lo que facilita el acceso y la 
manipulación de los datos. Los objetos en JavaScript son una de las características 
fundamentales del lenguaje y se utilizan extensamente.

SINTAXIS

let miObjeto = {
  clave1: "valor1",
  clave2: 42,
  clave3: true
};

Acceso a valores mediante claves

console.log( miObjeto.clave1 ); // Imprime "valor1"
console.log( miObjeto.clave2 ); // Imprime 42
console.log( miObjeto.clave3 ); // Imprime true

*/

// INSERCIÓN EN UN OBJETO
//Para insertar una nueva propiedad en un objeto, simplemente 
// se asigna un valor a una nueva clave:
let miObjeto = {
  clave1: "valor1",
  clave2: 42
};

// Inserción de una nueva propiedad
miObjeto.nuevaClave = "nuevoValor";
console.log(miObjeto);

// Resultado: { clave1: "valor1", clave2: 42, nuevaClave: "nuevoValor" }


// BORRADO EN UN OBJETO
//Para eliminar una propiedad de un objeto, puedes utilizar el operador delete:
let miObjeto2 = {
  clave1: "valor1",
  clave2: 42,
  nuevaClave: "nuevoValor"
};

// Borrado de una propiedad
delete miObjeto.nuevaClave;
console.log(miObjeto2);
// Resultado: { clave1: "valor1", clave2: 42 }


//ACTUALIZACION DE UN OBJETO
//La actualización de un valor en un objeto se realiza simplemente asignando 
//un nuevo valor a la clave correspondiente:
let miObjeto3 = {
  clave1: "valor1",
  clave2: 42
};

// Actualización de un valor
miObjeto.clave2 = 100;
console.log(miObjeto3);
// Resultado: { clave1: "valor1", clave2: 100 }


//ORDENACION DE UN OBJETO
//A diferencia de los arrays, los objetos en JavaScript no tienen un orden 
//específico para sus propiedades. Sin embargo, se puede simular un cierto orden 
//utilizando arrays o mapas si el orden es importante para la aplicación.
let miObjeto4 = {
  clave2: 42,
  clave1: "valor1",
  clave3: true
};

// Crear un array de las claves y ordenarlas
let clavesOrdenadas = Object.keys(miObjeto4).sort();

// Crear un nuevo objeto con las claves ordenadas
let objetoOrdenado = {};
for (let clave of clavesOrdenadas) {
  objetoOrdenado[clave] = miObjeto4[clave];
};

console.log(objetoOrdenado);
// Resultado: { clave1: "valor1", clave2: 42, clave3: true }

/*
Explicacion de método objext.keys() y el método .short()

Object.keys(miObjeto4): El método Object.keys() es una función 
incorporada en JavaScript que toma un objeto como argumento y devuelve 
un array con las claves (o propiedades) de ese objeto. En este caso, 
miObjeto4 es el objeto del cual queremos obtener las claves.

.sort(): Después de obtener las claves del objeto usando Object.keys(), 
se aplica el método sort() al array resultante. El método sort() ordena 
los elementos de un array alfabéticamente (por defecto, en orden lexicográfico).

*/



//*  3 SETS ----- 

/*

En JavaScript, un Set es un objeto que te permite almacenar valores 
únicos de cualquier tipo, ya sea valores primitivos o referencias a objetos. 
La principal característica de un Set es que no permite duplicados, por lo 
que cada elemento debe ser único en el conjunto.

SINTAXIS:

Creacion del set
let miSet = new Set();

Insercion de datos en el set

miSet.add(1);
miSet.add("Hola");
miSet.add(true);
miSet.add(1); 

Este ultimo valor 1 no se añadirá, ya que los Sets no permiten duplicados

console.log(miSet);
Resultado: Set { 1, 'Hola', true }


*/

/*

Características

Valores Únicos: Los Sets no pueden contener elementos duplicados. 
Si intentas añadir un elemento que ya está presente en el conjunto, no 
se realizará ninguna acción.

No Ordenados: A diferencia de los arrays, los Sets no mantienen un orden 
específico de los elementos. No puedes acceder a los elementos de un Set 
por índice.

Operaciones Básicas: Los Sets proporcionan métodos como add para añadir 
elementos, delete para eliminar elementos, y has para verificar si un elemento 
está presente en el conjunto.

*/


// INSERCION EN UN SET
//Para insertar elementos en un Set, puedes utilizar el método add:
let miSet = new Set();

miSet.add(1);
miSet.add("Hola");
miSet.add(true);

console.log(miSet);
// Resultado: Set { 1, 'Hola', true }


//BORRADO EN UN SET
//Para eliminar elementos de un Set, puedes utilizar el método delete:
let miSet2 = new Set([1, 2, 3, 4, 5]);

miSet.delete(3);

console.log(miSet2);
// Resultado: Set { 1, 2, 4, 5 }


//ACTUALIZACION DE UN SET
//No hay un método específico para actualizar un elemento en un Set porque, 
//por diseño, los elementos en un Set son únicos y no se permiten duplicados. 
//Si se necesitara actualizar un valor, se puede eliminar el antiguo y añadir 
//el nuevo.
let miSet3 = new Set([1, 2, 3]);

miSet.delete(2);
miSet.add(4);

console.log(miSet3);
// Resultado: Set { 1, 3, 4 }


//ORDENACION DE UN SET
//Los Sets en JavaScript no tienen un método sort porque, a diferencia de los 
//arrays, los Sets no mantienen un orden específico. Sin embargo, si SE necesita
//obtener un array ordenado a partir de un Set, Se puede convertir en un array y 
//luego usar el método sort de los arrays.
let miSet4 = new Set([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]);

let arrayOrdenado = Array.from(miSet4).sort((a, b) => a - b);

console.log(arrayOrdenado);
// Resultado: [1, 2, 3, 4, 5, 6, 9]

//En este ejemplo, Array.from(miSet) convierte el Set en un array, y luego sort 
//ordena ese array numéricamente.


//*  4 MAPS ----- 

/*

En JavaScript, un Map es una estructura de datos que te permite almacenar pares clave-valor, 
donde cada clave y cada valor pueden ser de cualquier tipo. A diferencia de los Sets, que solo 
almacenan valores únicos, los Mapas permiten asociar valores específicos a claves y proporcionan
métodos para la inserción, borrado, actualización y recuperación de estos pares clave-valor.

*/

// SINTAXIS:

// Creacion del map
let miMapa = new Map();

// Inserción de pares clave-valor

miMapa.set("clave1", "valor1");
miMapa.set(42, "Hola");
miMapa.set(true, [1, 2, 3]);

console.log(miMapa);

// Resultado: Map { 'clave1' => 'valor1', 42 => 'Hola', true => [ 1, 2, 3 ] }

/*

Caracteristicas

Claves Únicas: Cada clave en un Map es única, lo que significa que no puede haber duplicados.
Iteración: Puedes iterar sobre los pares clave-valor de un Map utilizando bucles o métodos como forEach.

*/

miMapa.forEach((valor, clave) => {
  console.log(`${clave} : ${valor}`);
});

// Resultado:
// clave1 : valor1
// 42 : Hola
// true : 1,2,3

/*

Operaciones Básicas: Los Mapas proporcionan métodos como set para añadir pares clave-valor, 
delete para eliminar pares, get para obtener el valor asociado a una clave, y más.

*/

console.log(miMapa.get("clave1")); // Imprime 'valor1'
miMapa.delete(42);
console.log(miMapa.has(true));     // Imprime true


//Tamaño Dinámico: Los Mapas pueden cambiar de tamaño dinámicamente a medida que se añaden 
//o eliminan pares clave-valor.

console.log(miMapa.size); // Imprime 2 (después de la eliminación del par con clave 42)

/*

Los Mapas son especialmente útiles cuando necesitas almacenar y recuperar datos asociados 
a claves específicas y proporcionan una alternativa a los objetos cuando las claves no 
necesariamente son cadenas de texto y se requiere un comportamiento más predecible en términos 
de orden y manipulación de datos.

*/

//INSERCION EN MAPS
//Para insertar pares clave-valor en un Map, puedes utilizar el método set:
let miMapa2 = new Map();

// Inserción de pares clave-valor
miMapa2.set("clave1", "valor1");
miMapa2.set(42, "Hola");
miMapa2.set(true, [1, 2, 3]);

console.log(miMapa2);
// Resultado: Map { 'clave1' => 'valor1', 42 => 'Hola', true => [ 1, 2, 3 ] }


//BORRADO EN MAPAS
//Para eliminar pares clave-valor de un Map, puedes utilizar el método delete:
miMapa2.delete(42);

console.log(miMapa2);
// Resultado: Map { 'clave1' => 'valor1', true => [ 1, 2, 3 ] }



//ACTUALIZACION EN MAPS
//Para actualizar el valor asociado a una clave específica, simplemente vuelves a utilizar 
//el método set con la misma clave:
miMapa2.set("clave1", "nuevoValor");

console.log(miMapa2);
// Resultado: Map { 'clave1' => 'nuevoValor', true => [ 1, 2, 3 ] }


// ORDENACION O RECORRIDO ORDENADO
//Aunque los Mapas en JavaScript mantienen el orden de inserción, si queremos recorrer 
//los pares clave-valor en un orden específico, se puede hacer utilizando el método 
//entries() y, por ejemplo, ordenar el array resultante.
let miMapa3 = new Map([
  ['z', 1],
  ['a', 2],
  ['c', 3]
]);

// Recorrer los pares clave-valor en orden alfabético
let paresOrdenados = Array.from(miMapa3.entries()).sort((a, b) => a[0].localeCompare(b[0]));

console.log(paresOrdenados);
// Resultado: [ [ 'a', 2 ], [ 'c', 3 ], [ 'z', 1 ] ]

/*
En este ejemplo, Array.from(miMapa.entries()) convierte los pares clave-valor en un array, y 
luego el método sort se utiliza para ordenar el array alfabéticamente según las claves.
este enfoque proporcionará un array ordenado, pero los Mapas en sí 
mismos mantendrán el orden de inserción original.
*/


//*  5 COLAS(QUEQUES) Y PILAS(STACKS) ----- 

/*

En JavaScript, las colas (queues) y pilas (stacks) son estructuras 
de datos comúnmente implementadas utilizando arrays o linked lists. Estas estructuras se 
utilizan para organizar y gestionar datos de manera específica.

*/

//PILAS(STACKS)

/*
Una pila es una estructura de datos en la que los elementos se añaden y eliminan siguiendo 
el principio de Last In, First Out (LIFO), es decir, el último elemento que se añade es el 
primero en ser eliminado.
En JavaScript, se puede implementar una pila utilizando un array y utilizando los métodos push 
para añadir elementos al final y pop para eliminar el último elemento añadido.

*/
let pila = [];

// Añadir elementos a la pila
pila.push(1);
pila.push(2);
pila.push(3);

console.log(pila);  // Resultado: [1, 2, 3]

// Eliminar el último elemento añadido (LIFO)
let elementoEliminado = pila.pop();
console.log(elementoEliminado);  // Resultado: 3
console.log(pila);  // Resultado: [1, 2]

//COLAS (QUEQUE)

/*

Una cola es una estructura de datos en la que los elementos se añaden al final y se eliminan 
desde el principio, siguiendo el principio de First In, First Out (FIFO), es decir, el 
primer elemento que se añade es el primero en ser eliminado.
En JavaScript, se puede implementar una cola utilizando un array y utilizando los métodos push 
para añadir elementos al final y shift para eliminar el primer elemento añadido.

*/

let cola = [];

// Añadir elementos a la cola
cola.push(1);
cola.push(2);
cola.push(3);

console.log(cola);  // Resultado: [1, 2, 3]

// Eliminar el primer elemento añadido (FIFO)
let elementoFuera = cola.shift();
console.log(elementoFuera);  // Resultado: 1
console.log(cola);  // Resultado: [2, 3]



//*  6 STRINGS ----- 

/*

En JavaScript, un String es una estructura de datos que representa una secuencia de caracteres. 
Los strings son utilizados para almacenar y manipular texto en el lenguaje. Cada carácter en un 
string tiene un índice numérico, comenzando desde 0 para el primer carácter.

*/

let miString = "Hola, mundo!";

// Acceder a caracteres por índice
console.log(miString[0]); // Resultado: "H"

// Longitud de un string
console.log(miString.length); // Resultado: 13

// Algunos Métodos de string
console.log(miString.toUpperCase());    // Resultado: "HOLA, MUNDO!"
console.log(miString.indexOf("mundo")); // Resultado: 6
console.log(miString.split(", "));      // Resultado: ["Hola", "mundo!"]

/*

Caracteristicas

Inmutabilidad: Los strings en JavaScript son inmutables, lo que significa que no 
pueden ser modificados directamente una vez creados. Cualquier operación que parezca 
modificar un string, en realidad crea uno nuevo.

Concatenación: Puedes concatenar strings utilizando el operador + o el método concat().

Interpolación de cadenas (Template literals): Puedes utilizar template literals para 
crear strings de manera más legible e incluir expresiones dentro del string.

Métodos de manipulación: JavaScript proporciona diversos métodos para manipular y trabajar con strings

*/

//INSERCION EN STRINGS
//Para "insertar" caracteres en un string, puedes utilizar la concatenación de strings o 
//la interpolación de cadenas (template literals):
let original = "Hola";
let insertado = original + ", mundo!";
console.log(insertado); // Resultado: "Hola, mundo!"

// O usando template literals
let insertadoTemplate = `${original}, mundo!`;
console.log(insertadoTemplate); // Resultado: "Hola, mundo!"


//BORRADO DE STRINGS
//Para "borrar" caracteres de un string, puedes utilizar el método slice para crear un nuevo 
//string excluyendo ciertos caracteres:
let original2 = "Hola, mundo!";
let borrado = original2.slice(0, 5); // Elimina los caracteres desde el índice 5 en adelante
console.log(borrado); // Resultado: "Hola"

//ACTUALIZACION DE STRINGS
//Para "actualizar" caracteres en un string, también puedes utilizar el método slice para 
//dividir el string en partes, modificar la parte deseada y luego concatenarlas de nuevo:
let original3 = "Hola, mundo!";
let actualizado = original3.slice(0, 5) + " JavaScript!";
console.log(actualizado); // Resultado: "Hola JavaScript!"

//ORDENACION DE STRINGS
//Para "ordenar" caracteres en un string, puedes convertir el string en un array, ordenar 
//el array y luego convertirlo de nuevo a un string:
let original4 = "javascript";
let ordenado = original4.split('').sort().join('');
console.log(ordenado); // Resultado: "aaccijprstv"



//* 7. DIFICULTAD EXTRA -----

/*

Crea una agenda de contactos por terminal.
  - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
  - Cada contacto debe tener un nombre y un número de teléfono.
  - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
    los datos necesarios para llevarla a cabo.
  - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
    (o el número de dígitos que quieras)
  - También se debe proponer una operación de finalización del programa.

*/

// NOTA: 

//Se puede hacer con prompt, para capturar una entrada dinámica
//del usuario, pero tocaria vincular html a este documento, y solo estamos usando
//archivos Js, asi que se resolverá con código duro y sin ciclo while, pues no 
//existirá entrada de datos dinámica, y aun no se como hacerlo por terminal con Js

const miAgenda = () => {

  let agenda = new Map();

  //Datos en código duro 
  let option  = 3;  // Menú de opciones del 1 al 5
  let name    = 'Fabian';
  let number  = 3188473006;
  let name2   = 'Luisa';
  let number2 = 3188294406;
 
  console.log('1. Buscar');
  console.log('2. Insertar');
  console.log('3. Actualizar');
  console.log('4. Eliminar');
  console.log('5. Salir');

  if( option >= 1 && option <= 5 ){

      switch (option) {
        case 1:
          console.log('Insertando datos...');
          if (name !== '' && !isNaN(number) && number.toString().length <= 11) {
            agenda.set(name, number);
            console.log( agenda );
          } else {
            console.log('Inserte datos válidos');
          }
          break;
        case 2:
          console.log('Realizando la búsqueda...');
          if (name !== '' && !isNaN(number) && number.toString().length <= 11){
            agenda.set(name, number);
          }
          if( agenda.has(name) ){
            console.log( `El numero de ${name} es : ${agenda.get(name)}` );
          }else{
            console.log('El contacto no esta registrado');
          }
          break;
        case 3:
          console.log('Actualizando información...');
          agenda.set(name2,number2);
          console.log( `El numero de ${name2} es : ${agenda.get(name2)}` );
          break;
        case 4:
          console.log('Eliminando datos...');
          agenda.delete(name);
          console.log( agenda );
          break;
        case 5:
          console.log('Saliendo de la agenda ...');
          break;
        default:
          break;
    }

  } else {
    console.log('Opción no válida');
    console.log('Digite opciones del 1 al 5');
  }

};

// Llamada a la función
miAgenda();
