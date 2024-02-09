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

//**Tipos de operadores en javascript */

//*Operadores aritméticos */
// Suma
let suma = 5 + 4;
console.log({ suma });

// Resta
let resta = 10 - 7;
console.log({ resta });

// Multiplicación
let multiplicacion = 6 * 4;
console.log({ multiplicacion });

// División
let division = 20 / 5;
console.log({ division });

// Módulo
let modulo = 17 % 4; // Proporciona el resto de dividir el primero número con el segundo.
console.log({ modulo });

// Incremento
let numInc = 6;
numInc++; // Incrementa numero en 1.
console.log({ numInc });

// Decremento
let numDec = 6;
numDec--; // Decrementa numero en 1.
console.log({ numDec });

//**Operadores lógicos */

// Operador AND (&&)
let opAND = 5 > 2 && 2 < 10; // Devuelve true en caso de que ambas condiciones sean verdaderas, sino devuelve false.
console.log({ opAND });

// Operador OR (||)
let opOR = 8 == 4 || 7 < 10; // Devuelve true si al menos una de las condiciones es verdadera, solo devuelve false cuando todas las condiciones son falsas.
console.log({ opOR });

let opNOT = !(6 > 1); // Si la expresión orginal es verdadera, ! la convierte en falsa y viceversa.
console.log({ opNOT });

//**Operadores de comparación */
let a = 4;
let b = 9;

// Igualdad
let igualdad = a == b;
console.log({ igualdad });
let igualdadEstricta = a === b; // Tambien es un operador de identidad
console.log({ igualdadEstricta });

// Desigualdad
let desigualdad = a != b;
console.log({ desigualdad });
let desigualdadEstricta = a !== b; // Tambien es un operador de identidad
console.log({ desigualdadEstricta });

// Mayor que y menor que
let mayor = a > b;
console.log({ mayor });
let menor = a < b;
console.log({ menor });

// Mayor o igual que y menor o igual que
let mayorIgual = a >= b;
console.log({ mayorIgual });
let menorIgual = a <= b;
console.log({ menorIgual });

//**Operadores de asignación */
// Asignación basica =
let basica = 3;
console.log({ basica });

// Asignación con adición *=
let adicion = 6;
adicion += 9; // Equivale a adicion = adicion + 9
console.log({ adicion });

// Asignación con sustracción -=
let sustraccion = 6;
sustraccion -= 9; // Equivale a sustraccion = sustraccion - 9
console.log({ sustraccion });

// Asignación con multiplicación *=
let multiplicacionAsig = 6;
multiplicacionAsig *= 9; // Equivale a multiplicacionAsig = multiplicacionAsig * 9
console.log({ multiplicacionAsig });

// Asignación con multiplicación /=
let divisionAsig = 6;
divisionAsig /= 9; // Equivale a divisionAsig = divisionAsig / 9
console.log({ divisionAsig });

//**Operadores de pertenencia */

// Operador de pertenencia en array
let arr = [1, 2, 3, 4, 5];

console.log('Operador de pertencia arr 1: ' + arr.includes(3)); // Devuelve true, ya que 3 se encuentra en el array
console.log('Operador de pertencia arr 2: ' + arr.includes(8)); // Devuelve false, ya que 8 no se encuentra en el array

// Operador de pertencia en string
let cadena = '!Hola, mundo';

console.log('Operador de pertencia string 1: ' + cadena.includes('Hola'));
console.log('Operador de pertencia string 2: ' + cadena.includes('javascript'));

// Operador de pertencia in para verificar si una propiedad esta presente en un objeto
let persona = {
	name: 'José',
	edad: 24,
	ciudad: 'Sevilla',
};

console.log('Operador de pertencia objeto 1: ' + ('name' in persona));
console.log('Operador de pertencia objeto 2: ' + ('trabajo' in persona));

//**Operador de concatenación */
let msg1 = 'Hola';
let msg2 = 'mundo';

console.log('¡' + msg1 + ', ' + msg2 + '!'); // Para concatenar se hace uso de +

//**Operador de tipos de datos */

let td1 = 5;
let td2 = 'Hola';
let td3 = true;
let obj1 = { name: 'Ejemplo' };

console.log('Operador de tipos de datos');
console.log(typeof td1); // Devuelve "number"
console.log(typeof td2); // Devuelve "string"
console.log(typeof td3); // Devuelve "boolean"
console.log(typeof obj1); // Devuelve "object"
console.log('-----------------------');

//**Operadores de instancia */

class Persona {
	constructor(nombre) {
		this.nombre = nombre;
	}
}

let persona1 = new Persona('Juan');

console.log('Operador de instancia');
console.log(persona1 instanceof Persona); // Devuelve true, persona1 es una instancia de la clase Persona
console.log(persona1 instanceof Object); // Devuelve true, todas las instancias son también objetos
console.log(persona1 instanceof Array); // Devuelve false, persona1 no es una instancia de Array
console.log('-----------------------');

//**Tipos de esctructura en javascript */

//**Estructura de control de flujo */
// Operador ternario
10 === 10 ? console.log('Ternaria respuesta 1') : console.log('Ternaria respuesta 2'); // Si la condicion es verdadera se ejecuta la primera expresión sino se ejecuta la segunda

// if...else, es como el operador ternario, pero se ve de manera diferente, depende de para que se vaya a usar se recomienda usar uno o el otro
if (10 === 10) {
	console.log('if respuesta');
} else {
	console.log('else respuesta');
}

// switch

let diaSemana = 'Lunes';

switch (diaSemana) {
	case 'Lunes':
		console.log('Es Lunes');
		break;
	case 'Martes':
		console.log('Es Martes');
		break;
	case 'Miercoles':
		console.log('Es Miercoles');
		break;
	case 'Jueves':
		console.log('Es Jueves');
		break;
	case 'Viernes':
		console.log('Es Viernes');
		break;
	case 'Sabado':
		console.log('Es Sabado');
		break;
	case 'Domingo':
		console.log('Es Domingo');
		break;

	default:
		console.log('El dia de la semana introducido no existe');
		break;
}

//**Bucles */
//for
console.log('Ciclo for');
for (let i = 0; i < 5; i++) {
	console.log(i);
}

//while
let num = 0;
console.log('Ciclo while');
while (num < 5) {
  console.log(num);
  num++;
}

//do...while
let count = 0;
console.log('Ciclo do...while');
do {
  console.log(count);
  count++;
} while (count < 5);

//for...of
const array = [1, 2, 3, 4, 5];
console.log('Ciclo for...of');
for (let elemento of array) {
  console.log(elemento);
}

//for...in
const objeto = { a: 1, b: 2, c: 3 };
console.log('Ciclo for...in');
for (let propiedad in objeto) {
  console.log(propiedad + ": " + objeto[propiedad]);
}

/*
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 */
console.log('Números comprendidos entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3');
for (let i = 10; i < 55; i++) {
   if(i % 2 == 0){
      if (i != 16){
         if (i % 3 != 0) {
            console.log(i);
         }
      }
   }
   
}
