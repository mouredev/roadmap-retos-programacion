/*
    * #18 CONJUNTOS 
*/

let conjunto = new Set()

// añade un elemento
conjunto.add("elemento 1")

// añade un elemento al inicio
const array = Array.from(conjunto)
array.splice(0, 0, "elemento 0")
conjunto = new Set(array)

// añade varios elementos en bloque al final
conjunto.add("elemento 2")
conjunto.add("elemento 3")

// añade varios elementos en bloque en una posicion concreta
const array2 = Array.from(conjunto)
array2.splice(1, 0, "elemento 0.25", "elemento 0.5", "elemento 0.75")
conjunto = new Set(array2)

// elimina un elemento en la posicion concreta
const posicion = Array.from(conjunto).indexOf("elemento 0.25")
conjunto.delete(Array.from(conjunto)[posicion])

// actualiza el valor de un elemento en una pocicion concreta
const array3 = Array.from(conjunto)
const posicion2 = array3.indexOf("elemento 0.5")
array3[posicion2] = "elemento 0.4"
conjunto = new Set(array3)

// comprueba si un elemento existe
console.log(conjunto.has("elemento 1"))

// elimina todo el contenido del conjunto
conjunto.clear()

console.log(conjunto)

/*
    * DIFICULTAD EXTRA 
*/

// UNION
const conjuntoA = new Set(["a", "b", "c"]);
const conjuntoB = new Set(["b", "c", "d"]);
const union = new Set([...conjuntoA, ...conjuntoB]);
console.log(union);

// INTERSECCION

const interseccion = new Set([...conjuntoA].filter(x => conjuntoB.has(x)));
console.log(interseccion);

// DIFERENCIA

const diferencia = new Set([...conjuntoA].filter(x => !conjuntoB.has(x)));
console.log(diferencia);

// DIFERENCIA SIMETRICA

const diferencia2 = new Set([...conjuntoB].filter(x => !conjuntoA.has(x)));
const diferenciaSimetrica = new Set([...diferencia, ...diferencia2]);

console.log(diferenciaSimetrica);