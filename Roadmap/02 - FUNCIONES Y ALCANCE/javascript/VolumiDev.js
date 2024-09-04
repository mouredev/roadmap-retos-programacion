/**
 * EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 */

//  ✳️ Funcion si parametros y sin retorno
function greetins() {
  console.log('Bienvenidos a JavaScript')
}

greetins()

//  ✳️ Funcion con parametro y sin retorno
function paramFunction(lang, lang1) {
	console.log('Este lenguaje se lo hemos pasado por parametro:', lang, '\ny lo mostramos en la practica de', lang1)
}

var lang = 'python'
var lang1 = 'javascript'
paramFunction(lang, lang1)

//  ✳️ Funcion con parametros y con retorno, en esta funcion tambien cramos una nueva funcion 
function paramYReturn(a, b) {
	console.log('En esta funcion vamos a cambiar la variable \na= '+a+'\nb= '+b+'\ny vamos a retornar el valor de la suma de los dos parametros que le hemos pasado')
	function sum (a, b){
		return a+b
	}

	return sum(a, b)
}

console.log(paramYReturn(4, 3), 'esta es el valor que retorno')

// ✳️ Funciones propias del lenguaje

console.log('esta es una funcion propia del lenguaje')
var cadena = 'las hemos pasado a mayusculas con otra funcion propia del lenguaje JS llamada touppercase()'
console.log(cadena.toUpperCase())

// ✳️ Local y Gobal
const constante = 'esta es una constante que no podemos modificar.'
var esGlobal = 'local'
function mostrar(){
	console.log(constante)
	let esDeBloque = 'solo de bloque'
	console.log(esGlobal)
	esGlobal = 'modificado dentro de la funcion'
	console.log(esDeBloque)
}

mostrar()
console.log(esGlobal)

// ✳️✳️ DIFICULTAD EXTRA

function printNumbers(cad1, cad2) {
	var n = 1
	var cont = 0
	while (n <= 100){
		if(n % 3 === 0 && n % 5 === 0){
			console.log('es',cad1,'y',cad2)
		}else if(n % 5 === 0){
			console.log('es',cad2)
		}else if(n % 3 === 0 ){
			console.log('es',cad1)
		} else {
			console.log(n)
			cont++
		}
		n++
	}
	return cont
}

console.log('Se han impreso: ',printNumbers('multiplo de 3','multiplo de 5'), 'numeros')