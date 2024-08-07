// Arrays: son colecciones de datos que tienen un identificador (numérico) y un valor (de cualquier tipo)

let array1 = new Array() // Forma 1 para declarar un array
let array2 = []          // Forma 2 para declarar un array

let frutas = ["piña", "fresa", "mango",] // Los elementos están numerados partiendo desde el 0

console.log(frutas[1]) // Acceder al elemento en la posición 1: fresa

frutas[2] = "uva" // Reemplazar el elemento "mango" por "uva"
console.log(frutas) // [ 'piña', 'fresa', 'uva' ]

frutas[3] = "naranja" // Agregar un nuevo elemento en la posición 3
console.log(frutas) // [ 'piña', 'fresa', 'uva', 'naranja' ]

console.log(frutas.at(-1)) // Obtener el último elemento del array: naranja

frutas.push("manzana") // Agregar un nuevo elemento al final del array
console.log(frutas) // [ 'piña', 'fresa', 'uva', 'naranja', 'manzana' ]

frutas.pop() // Eliminar el último elemento del array: manzana
console.log(frutas) // [ 'piña', 'fresa', 'uva', 'naranja' ]

frutas.shift() // Extraer el primer elemento del array: piña
console.log(frutas) // [ 'fresa', 'uva', 'naranja' ]

frutas.unshift("pera") // Agregar el elemento al principio del array: pera
console.log(frutas) // [ 'pera', 'fresa', 'uva', 'naranja' ]

frutas.sort() // Ordenar los elementos, en este caso en orden alfabético
console.log(frutas) // [ 'fresa', 'naranja', 'pera', 'uva' ]

//------------------------------------------------------------------------

// Objeto: son colecciones de datos que tienen una clave y un valor (de cualquier tipo)

let objeto1 = new Object() // Forma 1 para declarar un objeto
let objeto2 = {}          // Forma 2 para declarar un objeto

let persona = {
    nombre:"Marisol",
    edad: 24,
    "comida favorita": "pastas", // Para obtener este valor se deben utilizar: []
}

console.log(persona.nombre) // Obtener el nombre: Marisol
console.log(persona["comida favorita"]) // Obtener la comida favorita: pastas 

persona["comida favorita"] = "pizza" // Actualizar su comida favorita de pastas a: pizza
persona.sabeBailar = false // Insertar si sabe bailar con el valor: false

console.log(persona) // { nombre: 'Marisol', edad: 24, 'comida favorita': 'pizza', sabeBailar: false }

delete persona.edad // Borrar la propiedad: edad: 24
delete persona["comida favorita"] // Borrar la propiedad: "comidad favorita": "pizza"

console.log(persona) // { nombre: 'Marisol', sabeBailar: false }