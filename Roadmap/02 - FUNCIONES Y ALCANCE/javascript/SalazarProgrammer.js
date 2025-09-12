// #02 FUNCIONES Y ALCANCE
// Dificultad: Fácil | Publicación: 08/01/24 | Corrección: 15/01/24

/*
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

/*
 * RESPUESTAS:
 * - Crea ejemplos de funciones básicas
 */

// 1. Función sin parámetros ni retorno
function saludar() {
	console.log('¡Hola desde función sin parámetros!');
}

// 2. Función con un parámetro
function saludarPersona(nombre) {
	console.log(`¡Hola, ${nombre}!`);
}

// 3. Función con varios parámetros
function sumar(a, b) {
	return a + b;
}

// 4. Función con retorno
function multiplicar(a, b) {
	return a * b;
}

// 5. Función flecha (arrow function) - ES6
const dividir = (a, b) => a / b;

// 6. Función con parámetros por defecto
function potencia(base, exponente = 2) {
	return Math.pow(base, exponente);
}

// 7. Comprobar funciones dentro de funciones
function funcionExterna() {
	console.log('Función externa ejecutada');

	function funcionInterna() {
		console.log('Función interna ejecutada');
		return 'Retorno desde función interna';
	}

	const resultado = funcionInterna();
	console.log(resultado);

	// También podemos retornar una función
	return function () {
		console.log('Función retornada ejecutada');
	};
}

// 8. Funciones ya creadas en el lenguaje
// Math.random(), console.log(), parseInt(), etc.

// 9. Variables locales y globales
let variableGlobal = 'Soy global';

function probarVariables() {
	let variableLocal = 'Soy local';
	console.log('Dentro de la función:');
	console.log('Variable global:', variableGlobal);
	console.log('Variable local:', variableLocal);

	// Podemos modificar la variable global
	variableGlobal = 'Global modificada';
}

// Ejecutamos todas las funciones
console.log('=== FUNCIONES BÁSICAS ===');
saludar();
saludarPersona('Ana');
console.log('Suma:', sumar(5, 3));
console.log('Multiplicación:', multiplicar(4, 6));
console.log('División:', dividir(10, 2));
console.log('Potencia:', potencia(3));
console.log('Potencia con exponente:', potencia(2, 4));

console.log('\n=== FUNCIONES DENTRO DE FUNCIONES ===');
const funcionRetornada = funcionExterna();
funcionRetornada();

console.log('\n=== VARIABLES LOCALES Y GLOBALES ===');
console.log('Variable global antes:', variableGlobal);
probarVariables();
console.log('Variable global después:', variableGlobal);

// Intentar acceder a variable local fuera de su scope causaría error
// console.log(variableLocal); // ReferenceError

console.log('\n=== FUNCIONES DEL LENGUAJE ===');
console.log('Número aleatorio:', Math.random());
console.log('Redondeo:', Math.round(3.7));
console.log('Máximo:', Math.max(1, 5, 3, 8));
console.log('Parseo a entero:', parseInt('42'));

/*
 * DIFICULTAD EXTRA (opcional):
 */
function desafioExtra(texto1, texto2) {
	let contadorNumeros = 0;

	for (let i = 1; i <= 100; i++) {
		if (i % 3 === 0 && i % 5 === 0) {
			console.log(texto1 + texto2);
		} else if (i % 3 === 0) {
			console.log(texto1);
		} else if (i % 5 === 0) {
			console.log(texto2);
		} else {
			console.log(i);
			contadorNumeros++;
		}
	}

	return contadorNumeros;
}

console.log('\n=== DESAFÍO EXTRA ===');
const resultado = desafioExtra('Fizz', 'Buzz');
console.log(`\nNúmeros impresos en lugar de textos: ${resultado}`);

/*
 * FIN DEL DESAFÍO
 */
