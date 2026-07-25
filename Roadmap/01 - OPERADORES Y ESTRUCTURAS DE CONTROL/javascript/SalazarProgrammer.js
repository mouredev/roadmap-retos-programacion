// #01 OPERADORES Y ESTRUCTURAS DE CONTROL
// Dificultad: Fácil | Publicación: 02/01/24 | Corrección: 08/01/24

/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */

/*
 * RESPUESTAS:
 * - Operadores y estructuras de control
 */

console.log('=== OPERADORES EN JAVASCRIPT ===');

// 1. OPERADORES ARITMÉTICOS
console.log('\n1. OPERADORES ARITMÉTICOS:');
let a = 15;
let b = 4;

console.log('a =', a, ', b =', b);
console.log('Suma (a + b):', a + b);
console.log('Resta (a - b):', a - b);
console.log('Multiplicación (a * b):', a * b);
console.log('División (a / b):', a / b);
console.log('Módulo (a % b):', a % b);
console.log('Exponenciación (a ** b):', a ** b);
console.log('Incremento (a++):', a++); // Post-incremento
console.log('Decremento (--b):', --b); // Pre-decremento

// 2. OPERADORES DE COMPARACIÓN
console.log('\n2. OPERADORES DE COMPARACIÓN:');
console.log('Igualdad (a == 15):', a == 15);
console.log("Igualdad estricta (a === '15'):", a === '15');
console.log('Desigualdad (a != 15):', a != 15);
console.log('Desigualdad estricta (a !== 15):', a !== 15);
console.log('Mayor que (a > 10):', a > 10);
console.log('Menor que (a < 20):', a < 20);
console.log('Mayor o igual (a >= 15):', a >= 15);
console.log('Menor o igual (a <= 15):', a <= 15);

// 3. OPERADORES LÓGICOS
console.log('\n3. OPERADORES LÓGICOS:');
let x = true;
let y = false;

console.log('AND (x && y):', x && y);
console.log('OR (x || y):', x || y);
console.log('NOT (!x):', !x);
console.log("Nullish Coalescing (null ?? 'default'):", null ?? 'default');
console.log('Optional Chaining (obj?.prop):', {}.prop?.nested);

// 4. OPERADORES DE ASIGNACIÓN
console.log('\n4. OPERADORES DE ASIGNACIÓN:');
let c = 10;
console.log('Asignación (=): c =', c);
c += 5;
console.log('Suma y asignación (+=):', c);
c -= 3;
console.log('Resta y asignación (-=):', c);
c *= 2;
console.log('Multiplicación y asignación (*=):', c);
c /= 4;
console.log('División y asignación (/=):', c);
c %= 3;
console.log('Módulo y asignación (%=):', c);

// 5. OPERADORES DE BITS
console.log('\n5. OPERADORES DE BITS:');
let num1 = 5; // 0101 en binario
let num2 = 3; // 0011 en binario

console.log('AND (&):', num1 & num2); // 0001 = 1
console.log('OR (|):', num1 | num2); // 0111 = 7
console.log('XOR (^):', num1 ^ num2); // 0110 = 6
console.log('NOT (~num1):', ~num1); // Complemento a 2
console.log('Desplazamiento izquierda (num1 << 1):', num1 << 1); // 1010 = 10
console.log('Desplazamiento derecha (num1 >> 1):', num1 >> 1); // 0010 = 2

// 6. OPERADORES DE IDENTIDAD/TIPO
console.log('\n6. OPERADORES DE IDENTIDAD/TIPO:');
console.log('typeof 42:', typeof 42);
console.log("typeof 'hello':", typeof 'hello');
console.log('instanceof ([] instanceof Array):', [] instanceof Array);
console.log("in ('length' in []):", 'length' in []);

// 7. OPERADORES DE PERTENENCIA (para arrays y objetos)
console.log('\n7. OPERADORES DE PERTENENCIA:');
const array = [1, 2, 3, 4, 5];
const objeto = { nombre: 'Juan', edad: 30 };

console.log("in operator ('edad' in objeto):", 'edad' in objeto);
console.log('Array includes (array.includes(3)):', array.includes(3));

console.log('\n=== ESTRUCTURAS DE CONTROL ===');

// 1. CONDICIONALES
console.log('\n1. ESTRUCTURAS CONDICIONALES:');

// if-else
if (a > 10) {
	console.log('if: a es mayor que 10');
} else {
	console.log('if: a no es mayor que 10');
}

// if-else if-else
if (a > 20) {
	console.log('a > 20');
} else if (a > 15) {
	console.log('15 < a <= 20');
} else {
	console.log('a <= 15');
}

// switch
let dia = 3;
switch (dia) {
	case 1:
		console.log('switch: Lunes');
		break;
	case 2:
		console.log('switch: Martes');
		break;
	case 3:
		console.log('switch: Miércoles');
		break;
	default:
		console.log('switch: Otro día');
}

// Operador ternario
let resultado = a > 10 ? 'Mayor que 10' : 'Menor o igual a 10';
console.log('Ternario:', resultado);

// 2. ESTRUCTURAS ITERATIVAS
console.log('\n2. ESTRUCTURAS ITERATIVAS:');

// for
console.log('For loop:');
for (let i = 0; i < 5; i++) {
	console.log('  Iteración:', i);
}

// while
console.log('While loop:');
let contador = 0;
while (contador < 3) {
	console.log('  Contador:', contador);
	contador++;
}

// do-while
console.log('Do-while loop:');
contador = 0;
do {
	console.log('  Contador:', contador);
	contador++;
} while (contador < 3);

// for...of (arrays)
console.log('For...of (arrays):');
for (const elemento of array) {
	console.log('  Elemento:', elemento);
}

// for...in (objetos)
console.log('For...in (objetos):');
for (const clave in objeto) {
	console.log(`  ${clave}: ${objeto[clave]}`);
}

// 3. MANEJO DE EXCEPCIONES
console.log('\n3. MANEJO DE EXCEPCIONES:');

try {
	console.log('Intentando operación...');
	let division = 10 / 0;
	if (!isFinite(division)) {
		throw new Error('División por cero o resultado infinito');
	}
	console.log('Resultado:', division);
} catch (error) {
	console.log('Error capturado:', error.message);
} finally {
	console.log('Bloque finally ejecutado');
}

// 4. CONTROL DE FLUJO
console.log('\n4. CONTROL DE FLUJO:');

// break
console.log('Break en loop:');
for (let i = 0; i < 10; i++) {
	if (i === 5) break;
	console.log('  i =', i);
}

// continue
console.log('Continue en loop:');
for (let i = 0; i < 5; i++) {
	if (i === 2) continue;
	console.log('  i =', i);
}

// return (en función)
function ejemploReturn() {
	console.log('Esta línea se ejecuta');
	return 'Valor retornado';
}
console.log('Return:', ejemploReturn());

/*
 * DIFICULTAD EXTRA (opcional):
 * Números entre 10 y 55, pares, que no son 16 ni múltiplos de 3
 */
console.log('\n=== DIFICULTAD EXTRA ===');

function numerosEspeciales() {
	let count = 0;

	for (let i = 10; i <= 55; i++) {
		if (i % 2 === 0 && i !== 16 && i % 3 !== 0) {
			console.log(i);
			count++;
		}
	}

	return count;
}

const total = numerosEspeciales();
console.log(`\nTotal de números encontrados: ${total}`);
