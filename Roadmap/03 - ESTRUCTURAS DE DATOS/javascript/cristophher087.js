/**
 * Estructuras soportadas por JavaScript
 * 
 * Tipado dinámico
 * 
 * JS es un Lenguaje de prigramacion debilmente tipado y dinámico.
 */

let foo = 42;   // foo ahora es un número
foo = "bar";    // foo ahora es un string
foo = true;     // foo ahora es un booleano

/**
 * Estructuras y tipso de datos
 * El último estándar ECMAScript define nueve tipos:
*/

// Seis tipos de datos primitivos, controlados por el operador typeof

typeof isntance === "undefined"
typeof isntance === "boolean"
typeof instance === "number"
typeof instance === "string"
typeof instance === "bigint"
typeof instance === "symbol"

typeof instance === "object" //Tipo primitivo especial que tiene un uso adicional para su valor: si el objeto no se hereda, se muestra null

typeof instance === "object" //Tipo estructural especial que no es de datos pero para cualquier instancia de objeto construido que también se utiliza como estructuras de datos: new Object, new Array, new Map, new Set, new WeakMap, new WeakSet, new Date y casi todo lo hecho con la palabra clave new;

typeof instance === "function" //Esta simplemente es una forma abreviada para funciones, aunque cada constructor de funciones se deriva del constructor Object.

/**
 * Estructuras de Datos
 */

// Set: Conjunto de valores únicos
let conjunto = new Set([1, 2, 3, 3]);
console.log(conjunto);  // {1, 2, 3}
/**
 * Set define valores como se muestra en el ejemplo
 */

// Map: Estructura clave-valor
let mapa = new Map();
mapa.set("nombre", "Carlos");
mapa.set("edad", 25);
console.log(mapa.get("nombre"));  // Carlos
/**
 * Map Genera una estructura en donde s egenera una clave con su rsepectivo valor de este
 */

// WeakSet y WeakMap: Estructuras que contienen referencias débiles
let weakSet = new WeakSet();
let objeto1 = { clave: 123 };
weakSet.add(objeto1);

// No se puede iterar directamente un WeakSet
console.log(weakSet.has(objeto1));  // true


/**
 * Vectores (Arrays) en JavaScript
 *      Un Array es una lista ordenada de elementos. En JavaScript, los arrays pueden contener cualquier tipo de dato (números, strings, objetos, etc.).
 */

let numeros = [1, 2, 3, 4, 5];  // Array de números
let mezclado = [42, "texto", true, { id: 1 }];  // Elementos de distintos tipos

/**
 * Inserciones
 */

// Inserción al final del array
numeros.push(6);  // [1, 2, 3, 4, 5, 6]

// Inserción al inicio del array
numeros.unshift(0);  // [0, 1, 2, 3, 4, 5, 6]

// Inserción en una posición específica (índice)
numeros.splice(3, 0, 99);  // [0, 1, 2, 99, 3, 4, 5, 6]

/**
 * Eliminación de Elementos
 */

// Eliminar el último elemento
numeros.pop();  // [0, 1, 2, 99, 3, 4, 5]

// Eliminar el primer elemento
numeros.shift();  // [1, 2, 99, 3, 4, 5]

// Eliminar en una posición específica
numeros.splice(2, 1);  // [1, 2, 3, 4, 5] (elimina el valor en el índice 2)

/**
 * Búsquedas en Arrays
 */

// Buscar el índice de un elemento
let indice = numeros.indexOf(3);  // 2

// Verificar si un elemento existe
let existe = numeros.includes(4);  // true

// Búsqueda con función de condición
let mayorQueTres = numeros.find(num => num > 3);  // 4

/**
 * Recorrer un Array
 */

// Usando for
for (let i = 0; i < numeros.length; i++) {
  console.log(numeros[i]);
}

// Usando for...of
for (let num of numeros) {
  console.log(num);
}

// Usando forEach
numeros.forEach((num, index) => {
  console.log(`Elemento en ${index}: ${num}`);
});

/**
 * Matrices (Arrays Multidimensionales)
 *  Una matriz es un array de arrays. Esto se usa para representar estructuras como tablas o grillas.
 */

let matriz = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
];

/**
 * Acceso a Elementos
 */

let elemento = matriz[1][2];  // 6 (Fila 1, Columna 2)

/**
 * Modificación de Elementos
 */

matriz[2][1] = 88;  // Modifica el valor en la fila 2, columna 1
console.log(matriz);
// Resultado: [ [1, 2, 3], [4, 5, 6], [7, 88, 9] ]

/**
 * Recorrer una Matriz
 */

for (let fila of matriz) {
  for (let valor of fila) {
    console.log(valor);
  }
}

// Usando forEach
matriz.forEach(fila => {
  fila.forEach(valor => console.log(valor));
});

/**
 * Operaciones Funcionales en Arrays (map, filter, reduce)
 */

/**
 * map: Crear un nuevo array transformando los elementos.
 */

let duplicados = numeros.map(num => num * 2);  // [2, 4, 6, 8, 10]

/**
 * reduce: Reducir el array a un solo valor.
 */

let suma = numeros.reduce((acumulador, actual) => acumulador + actual, 0);  // 15

/**
 * Ejemplo
 */

// Crear una matriz 3x3
let matriz = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
];

// Insertar un valor en una posición específica (fila 1, columna 1)
matriz[1][1] = 99;

// Sumar todos los elementos de la matriz
let sumaTotal = matriz.flat().reduce((acc, val) => acc + val, 0);
console.log(`Suma total: ${sumaTotal}`);  // 144

// Filtrar todos los valores mayores que 5
let mayores = matriz.flat().filter(num => num > 5);
console.log(`Mayores que 5: ${mayores}`);  // [6, 7, 8, 9]


let contactos = [
  { nombre: "Carlos", telefono: "5558765123" },
  { nombre: "María", telefono: "5512345678" },
  { nombre: "Juan", telefono: "5578943210" },
  { nombre: "Ana", telefono: "5587654321" },
  { nombre: "Luis", telefono: "5612345678" },
  { nombre: "Sofía", telefono: "5545678912" },
  { nombre: "Pedro", telefono: "5556781234" },
  { nombre: "Laura", telefono: "5598765432" },
  { nombre: "Roberto", telefono: "5587123456" },
  { nombre: "Daniela", telefono: "5567894321" }
];

// Mostrar contactos iniciales
mostrarContactos();

// Ciclo principal del programa
while (true) {
  console.log("\nAgenda de contactos");
  console.log("Digita la opción que quieres realizar:");
  console.log("[b] - Búsqueda");
  console.log("[i] - Inserción");
  console.log("[a] - Actualización");
  console.log("[e] - Eliminación");
  console.log("[q] - Salir");

  let opcion = prompt("¿Qué acción deseas realizar?").toLowerCase().trim();

  switch (opcion) {
    case "b":
      consultaContacto();
      break;
    case "i":
      ingresaContacto();
      break;
    case "a":
      actualizaContacto();
      break;
    case "e":
      eliminaContacto();
      break;
    case "q":
      console.log("Saliendo de la agenda...");
      process.exit();  // Solo en Node.js; en navegador, usar 'break' y finalizar el ciclo.
    default:
      console.log("Opción no válida. Inténtalo de nuevo.");
  }
}

// Función para mostrar todos los contactos
function mostrarContactos() {
  console.log("\nContactos actuales:");
  contactos.forEach((contacto, index) =>
    console.log(`${index + 1}. Nombre: ${contacto.nombre}, Teléfono: ${contacto.telefono}`)
  );
}

// Función para buscar un contacto por nombre
function consultaContacto() {
  let nombreConsulta = prompt("Ingresa el nombre del contacto a buscar:").trim().toLowerCase();
  let contacto = contactos.find(c => c.nombre.toLowerCase() === nombreConsulta);

  if (contacto) {
    console.log(`\nNombre: ${contacto.nombre}, Teléfono: ${contacto.telefono}`);
  } else {
    console.log(`No se encontró un contacto con el nombre "${nombreConsulta}".`);
  }
}

// Función para ingresar un nuevo contacto
function ingresaContacto() {
  let nuevoNombre = prompt("Ingresa el nombre del nuevo contacto:").trim();
  let nuevoNumero = prompt("Ingresa el número de teléfono (10 dígitos):").trim();

  if (!/^\d{10}$/.test(nuevoNumero)) {
    console.log("Número inválido. Debe contener exactamente 10 dígitos.");
    return;
  }
  /**
   * "/^\d{10}$/" es una expresión regular (regex) que valida que la entrada nuevoNumero contenga exactamente 10 dígitos numéricos.
   * "^" y "$" aseguran que la cadena completa debe cumplir con el patrón (no puede haber otros caracteres).
   * "\d{10}" indica que deben ser exactamente 10 dígitos consecutivos.
   * El operador NOT (!) invierte el resultado de la expresión regular. Si el número no coincide con la regex (es decir, no tiene exactamente 10 dígitos), la condición se cumple.
   * .test(nuevoNumero): Este método prueba si el contenido de nuevoNumero coincide con la expresión regular.
   */

  if (contactos.some(c => c.nombre.toLowerCase() === nuevoNombre.toLowerCase())) {
    console.log("El contacto ya existe. No se puede duplicar.");
    return;
  }
  /**
   * c => c.nombre.toLowerCase() === nuevoNombre.toLowerCase() es una función flecha (arrow function) que actúa como callback. Por cada elemento del array contactos, ejecuta el código dentro de esa función flecha.
   * La c no está definida antes porque es solo un parámetro temporal de la función flecha.
   * some() es un método de los arrays que retorna true si al menos un elemento del array cumple con la condición que se le pasa.
   * Se compara el nombre del contacto existente (c.nombre) con el nuevo nombre ingresado (nuevoNombre).
   * Ambos nombres se convierten a minúsculas con toLowerCase() para evitar errores por mayúsculas o minúsculas (por ejemplo, "Carlos" y "carlos" se tratarían como iguales).
   */

  contactos.push({ nombre: nuevoNombre, telefono: nuevoNumero });
  console.log("Contacto agregado exitosamente.");
  mostrarContactos();
}

// Función para actualizar un contacto
function actualizaContacto() {
  let nombreConsulta = prompt("Ingresa el nombre del contacto a actualizar:").trim().toLowerCase();
  let contacto = contactos.find(c => c.nombre.toLowerCase() === nombreConsulta);

  if (contacto) {
    let nuevoNombre = prompt(`Ingresa el nuevo nombre (actual: ${contacto.nombre}):`).trim() || contacto.nombre;
    let nuevoNumero = prompt(`Ingresa el nuevo número (actual: ${contacto.telefono}):`).trim() || contacto.telefono;

    if (!/^\d{10}$/.test(nuevoNumero)) {
      console.log("Número inválido. Debe contener exactamente 10 dígitos.");
      return;
    }

    contacto.nombre = nuevoNombre;
    contacto.telefono = nuevoNumero;
    console.log("Contacto actualizado exitosamente.");
    mostrarContactos();
  } else {
    console.log(`No se encontró un contacto con el nombre "${nombreConsulta}".`);
  }
}

// Función para eliminar un contacto
function eliminaContacto() {
  let nombreConsulta = prompt("Ingresa el nombre del contacto a eliminar:").trim().toLowerCase();
  let index = contactos.findIndex(c => c.nombre.toLowerCase() === nombreConsulta);

  if (index !== -1) {
    contactos.splice(index, 1);
    console.log("Contacto eliminado exitosamente.");
    mostrarContactos();
  } else {
    console.log(`No se encontró un contacto con el nombre "${nombreConsulta}".`);
  }
}

/**
 ¿Qué es una expresión regular?

Es una secuencia de caracteres que define un patrón de búsqueda. Por ejemplo, /\d{10}/ es una expresión regular que busca 10 dígitos consecutivos.

Las expresiones regulares se delimitan entre barras /.../ (en JavaScript), y pueden incluir caracteres literales, metacaracteres (como . o \d), y modificadores para ampliar su funcionalidad.

Componentes básicos de una regex
Metacaracteres (símbolos especiales):

    . (punto): Representa cualquier carácter, excepto saltos de línea.
        Ejemplo: /c.t/ coincide con cat, cot, o cut.

    \d: Representa cualquier dígito (equivale a [0-9]).
        Ejemplo: /\d/ encuentra cualquier número en la cadena "Tel: 123".

    \w: Representa cualquier carácter alfanumérico (letras, números o guion bajo).
        Ejemplo: /\w+/ encuentra palabras como "hola123".

    \s: Coincide con espacios en blanco (incluye tabulaciones y saltos de línea).

    ^ y $: Marcan el inicio y fin de la cadena, respectivamente.
        Ejemplo: /^Hola/ verifica que la cadena empiece con "Hola".
        Ejemplo: /mundo$/ verifica que termine con "mundo".

    
 */
