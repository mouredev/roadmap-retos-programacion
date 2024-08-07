/** 
<-------------- Variable por valor -------------->
Cuando se le asignan valores primitivos (boolean, number, string, undefined, null, BigInt, symbol) el valor asignado se va a pasar como 
una copia del valor original.
*/

let a = 'hola'
let b = a // Se asigna el valor de "a" a "b"
a += 'Mundo' // Se cambia el valor de "a" añadiendo "Mundo" al final
console.log(a) // holaMundo
console.log(b) // hola

// En el ejemplo anterior, se puede observar como cada variable guarda su propio valor, o sea que se mantienen independientes.

/** 
<-------------- Variable por referencia -------------->
Cuando se le asignan valores NO primitivos (objetos, arrays y funciones) el valor asignado no se va a pasar como tal, en realidad lo que se
pasa es una referencia a la variable que contiene el valor original, es como si la variable fuera una "casa" y lo que se pasa no es la casa
como tal, sino que lo que se pasa es su "dirección" para poder ubicarla.
*/

let x = [1, 2, 3]
let y = x
x.push(4)
console.log(x) // [ 1, 2, 3, 4 ]
console.log(y) // [ 1, 2, 3, 4 ]

/**
En el ejemplo anterior, se puede observar que a la variable "x" se le está agregando un nuevo valor, sin embargo, tanto el valor de "x" como
de "y" es exactamente el mismo. Esto se debe a que las variables tienen diferente nombre, pero el valor que estamos modificando es el mismo.
*/

/**
<-------------- Variable por valor y referencia en funciones -------------->
La diferencia entre pasar una variable por referencia o por valor es con respecto a lo que pasa dentro y fuera de la función.

<-------------- Variable por valor en funciones -------------->
Cuando pasamos una variable por valor, las acciones que ocurren dentro de esta NO repercuten fuera de ella, o sea que dichas acciones solo viven
dentro de la función y NO alteran el código fuera de la función. Recordemos que el valor que recibe la función es una "copia" del valor original.
*/

let animalPorValor = "perro" // Valor original

function mascotaPorValor(animal) {
	animal = "gato" // Re-asignación
	console.log(`Dentro de la función el animal es: ${animal}`) // Dentro de la función el animal es: gato
}

mascotaPorValor(animalPorValor) 
console.log(`Fuera de la función el animal es: ${animalPorValor}`) // Fuera de la función el animal es: perro

/**
<-------------- Variable por referencia en funciones -------------->
Cuando pasamos una variable por referencia, las acciones que ocurren dentro de esta SÍ repercuten fuera de ella, o sea que dichas acciones viven
tanto dentro como fuera de la función, por ende alteran todo el código. Recordemos que el valor que recibe la función es una referencia o 
dirección que apunta hacia el valor original.
*/

let arrayDeMascotas = ["conejo"] // Valor original

function mascotaPorReferencia(animales) {
	animales[1] = "gato" // Agregar un nuevo elemento
	console.log(`Dentro de función el array tiene: ${animales}`) // Dentro de la función el array tiene: conejo,gato
}

mascotaPorReferencia(arrayDeMascotas)
console.log(`Fuera de la función el array tiene: ${arrayDeMascotas}`) // Fuera de la función el array tiene: conejo,gato