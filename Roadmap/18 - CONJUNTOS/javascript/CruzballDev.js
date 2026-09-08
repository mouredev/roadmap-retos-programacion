/*
 * EJERCICIO:
 * Utilizando tu lenguaje crea un conjunto de datos y realiza las siguientes
 * operaciones (debes utilizar una estructura que las soporte):
 * - Añade un elemento al final.
 * - Añade un elemento al principio.
 * - Añade varios elementos en bloque al final.
 * - Añade varios elementos en bloque en una posición concreta.
 * - Elimina un elemento en una posición concreta.
 * - Actualiza el valor de un elemento en una posición concreta.
 * - Comprueba si un elemento está en un conjunto.
 * - Elimina todo el contenido del conjunto.
*/

let datos = [1, 2, 3, 4, 5]
console.log(`Datos iniciales: ${datos}`)

datos.push(6)
console.log(`Añadido elemento al final: ${datos}`)

datos.unshift(7)
console.log(`Añadido elemento al principio: ${datos}`)

datos.push(8, 9)
console.log(`Añadido varios elementos al final: ${datos}`)

datos.splice(3,1)
console.log(`Elimino elemento en la posición 3 en una posición concreta: ${datos}`)

datos.splice(3, 1, 18)
console.log(`Actualizo elemento en la posición 3 por el númeor 18: ${datos}`)

datos.includes(7)
console.log(`Compruebo si el número 7 está en el conjunto: ${datos.includes(7)}`)

datos.splice(4, 2, 23, 24)
console.log(`Añado varios elementos,los números 23 y 24 en las posiciones 4 y 5: ${datos}`)

datos.length = 0
console.log (`Elimino todos los datos del conjunto, ${datos}`)

/*
 * DIFICULTAD EXTRA (opcional):
 * Muestra ejemplos de las siguientes operaciones con conjuntos:
 * - Unión.
 * - Intersección.
 * - Diferencia.
 * - Diferencia simétrica.
*/

// Unión
let datos2 = new Set (["coche1", "coche2", "coche3", "coche4", "coche8"])
let datos3 = new Set (["coche5", "coche1",  "coche6", "coche7", "coche8"])
console.log(datos2)
console.log(datos3)

let union = new Set([...datos2, ...datos3])
console.log(union)

// Intersección

/*
Convierte el Set en un array.
Después:
Pregunta:
"¿Este coche también está en datos3?"
Si la respuesta es true, se conserva.
Si es false, se elimina.
Con el resultado sería:
Set(2) { 'coche1', 'coche8' }
*/

const interseccion = new Set(
    [...datos2].filter(coche => datos3.has(coche))
)
console.log(interseccion)

// Diferencia

const diferencia2a3 = new Set(
    [...datos2].filter(coche => !datos3.has(coche))
)
console.log(diferencia2a3)
console.log(`Diferencia entre conjunto 2 y 3 es:  ${[...diferencia2a3].join(", ")}`) // Para mostrarlo por un console.log() lo convertirmos en un Array y con .join(", ") le añadimos un espacio y coma pera que sea más legible.

const diferencia3a2 = new Set(
    [...datos3].filter(coche => !datos2.has(coche))
)
console.log(diferencia3a2)
console.log(`Diferencia entre conjunto 3 y 2 es: ${[...diferencia3a2].join(", ")}`)

// Diferencia simétrica

const diferenciaSimetrica = new Set([
    ...[...datos2].filter(coche => !datos3.has(coche)),
    ...[...datos3].filter(coche => !datos2.has(coche))
])
console.log(diferenciaSimetrica)