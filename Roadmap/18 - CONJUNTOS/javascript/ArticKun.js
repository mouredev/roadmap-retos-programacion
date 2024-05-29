
// ⚡ Conjuntos

// Creamos un conjunto de datos inicial
let conjuntoDatos = ["dato1", "dato2", "dato3"];

// Añadir un elemento al final
conjuntoDatos.push("dato4");

// Añadir un elemento al principio
conjuntoDatos.unshift("dato0");

// Añadir varios elementos en bloque al final
conjuntoDatos = conjuntoDatos.concat(["dato5", "dato6"]);

// Añadir varios elementos en bloque en una posición concreta
conjuntoDatos.splice(3, 0, "datoA", "datoB");

// Eliminar un elemento en una posición concreta
conjuntoDatos.splice(2, 1);

// Actualizar el valor de un elemento en una posición concreta
conjuntoDatos[1] = "datoX";

// Comprobar si un elemento está en el conjunto
const elementoBuscado = "datoX";
const estaEnConjunto = conjuntoDatos.includes(elementoBuscado);

// Eliminar todo el contenido del conjunto
conjuntoDatos = [];

/*

DIFICULTAD EXTRA (opcional):

  Muestra ejemplos de las siguientes operaciones con conjuntos:
  - Unión.
  - Intersección.
  - Diferencia.
  - Diferencia simétrica.

*/

// Union
const conjuntoA = new Set([1, 2, 3]);
const conjuntoB = new Set([3, 4, 5]);
// Unión de conjuntoA y conjuntoB
const union = new Set( [...conjuntoA, ...conjuntoB] );
console.log("Unión:", union); // Output: Set { 1, 2, 3, 4, 5 }


// Intersección
const conjuntoC = new Set([1, 2, 3]);
const conjuntoD = new Set([3, 4, 5]);
// Intersección de conjuntoC y conjuntoD
const interseccion = new Set( [...conjuntoC].filter(x => conjuntoD.has(x)) );
console.log("Intersección:", interseccion); // Output: Set { 3 }


// Diferencia
const conjuntoE = new Set( [1, 2, 3] );
const conjuntoF = new Set( [3, 4, 5] );
// Diferencia de conjuntoE y conjuntoF
const diferencia = new Set( [...conjuntoE].filter(x => !conjuntoF.has(x)) );
console.log("Diferencia:", diferencia); // Output: Set { 1, 2 }


// Diferencia simétrica
const conjuntoG = new Set([1, 2, 3]);
const conjuntoH = new Set([3, 4, 5]);
// Diferencia simétrica (G - H) U (H - G)
const diferenciaSimetrica = new Set([
  ...[...conjuntoG].filter(x => !conjuntoH.has(x)),
  ...[...conjuntoH].filter(x => !conjuntoG.has(x))
]);
console.log("Diferencia Simétrica:", diferenciaSimetrica); // Output: Set { 1, 2, 4, 5 }
