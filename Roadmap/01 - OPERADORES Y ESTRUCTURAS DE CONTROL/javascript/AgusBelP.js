/* 

#01  OPERADORES Y ESTRUCTURAS DE CONTROL

Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje: Aritméticos, lógicos, de comparación asignación, identidad, pertenencia, bits...(Ten en cuenta que cada lenguaje puede poseer unos diferentes).
Utilizando las operaciones con operadores que tú quieras, crea ejemplos que representen todos los tipos de estructuras de control que existan en tu lenguaje: Condicionales, iterativas, excepciones...
Debes hacer print por consola del resultado de todos los ejemplos.
 
DIFICULTAD EXTRA (opcional):
Crea un programa que imprima por consola todos los números comprendidos entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 
Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo. */

// --------------------------------------- RESOLUCIÓN --------------------------------------- //

// <<<---------------------->>> Tipos de operadores <<<---------------------->>>

/* En Javascript existen 10 tipos de operadores */

// ---------------> 1. Operadores aritméticos <---------------

let suma = 1 + 1;
let resta = 5 - 2;
let multiplicación = 2 * 3;
let división = 4 / 2;
let modulo = 4 % 2; // Devuelve el resto de la división de 4 entre 2
let exponenciacion = 2 ** 3; // eleva 2 a la potencia de 3

// ---------------> 2. Operadores de asignación <---------------

let x = 2; //operador de asignación
x += 1; // operador de adición, simboliza x = x + 1
x -= 1; // operador de resta, simboliza x = x - 1
x *= 1; // operador de multiplicación, simboliza x = x * 1
x /= 2; // operador de división, simboliza x = x / 2
x %= 2; // operador de resto, simboliza x = x % 2 y a x se le adigna el resto de la división
x **= 2; // operador de exponenciación, simboliza x = x ** 2 (x a la potencia de 2)

// ---------------> 3. Operadores de comparación <---------------
// Se mostrarán ejemplos que proporcionen un resultado true

let y = 4;
let z = 5;
let w = 1;
console.log(y == '4'); // Comprobación de igualdad de valores sin verificar el tipo de dato
console.log(y != 3); // Comprobación de la diferencia de lavalores sin verificar el tipo de dato
console.log(y === 4); // Comprobación de igualdad de valores y tipo de dato
console.log(y !== 3); // Comprobación de la diferencia de valores o tipo de dato
console.log(z > y); // Comprobación si el valor de z es estrictamente mayor al de y
console.log(z >= y); // Comprobación si el valor de z es mayor o igual al de y
console.log(w < y); // Comprobación si el valor de w es estrictamente menor al de y
console.log(w <= y); // Comprobación si el valor de w es menor o igual al de y

// ---------------> 4. Operadores de cadena <---------------

let nombre = 'My' + 'GitHub';
console.log(nombre);

// ---------------> 5. Operadores lógicos <---------------

// Operador condicional(ternario)

let edad = 15;

edad > 18 ? console.log('Soy mayor de edad') : console.log('No soy mayor de edad');

// AND (&&)

console.log(true && true); // Cuando se usa con valores booleanos, && devuelve verdadero si ambos operandos son verdaderos; de lo contrario, devuelve falso.
console.log(0 && true); // Considerando la forma "expr1 && expr2" el operador && devuelve expr1 si se puede convertir a false; de lo contrario, devuelve expr2. Ejemplos de expresiones que se pueden convertir a false son aquellos que se evalúan como null, 0, NaN, la cadena vacía ("") o undefined. En el ejemplo el log imprime 0

// OR (||)

// El operador lógico OR establece una condición donde devolverá el primer valor si es true, o el segundo valor si el primero es false. Esto se puede leer de forma que «devuelve a (si es verdadero), o si no, b».

console.log(false || false); // devuelve false
console.log(true || false); // devuelve true
console.log(false || true); // devuelve true
console.log(true || true); // devuelve true

// Considerando que cualquier valor superior a 0 es considerado como true y que cualquier valor que sea 0 o falsy se considera false:

console.log(0 || null); // devuelve false, se considera como false || false
console.log(44 || undefined); // devuelve true, se considera como true || false
console.log(0 || 17); // devuelve true, se considera como false || true
console.log(4 || 10); // devuelve true, se considera como true || true

// Nullish coalescing (??)

// el operador a ?? b devuelve b sólo cuando a es undefined o null. Al contrario que el operador OR, con valores como false, 0 o "", no devuelve b.

console.log(42 || 50); // devulve 42
console.log(42 ?? 50); // devulve 42
console.log(false || 50); // devulve 50
console.log(false ?? 50); // devulve false
console.log(0 || 50); // devulve 50
console.log(0 ?? 50); // devulve 0
console.log(null || 50); // devulve 50
console.log(null ?? 50); // devulve 50
console.log(undefined || 50); // devulve 50
console.log(undefined ?? 50); // devulve 50

// Operador de asignación lógica nula (??=)

// Especialmente útil en los casos en que una variable tiene el valor null o undefined y se desea cambiar su valor

// Sin asignación lógica nula
let t = null;
if (t === null || t === undefined) {
    t = 120;
}

// Con asignación lógica nula
t ??= 120;

// Encadenamiento opcional (?)

// Este operador permite acceder a propiedades aunque su elemento padre no exista de forma de evitar un error.

//Ejemplo: Suponiendo que se tiene un objeto usuario:

const user = {
    name: 'Moure',
    role: 'streamer',
    attributes: {
        life: 100,
        power: 25,
    },
};

// Si intento acceder a sus propiedades:

user.attributes.life;
user.attributes.power;

// Suponiendo que la propiedad attributes del objeto user aún no exite (pero existirá), si se intenta acceder a las propiedades sin que attributes exista ocurrirá un error. Para evitar eos se puede utilizar el optional chainig:

user.attributes?.life;
user.attributes?.power;

// En el caso de que la propiedad attribte del objeto user aún no exista el optionan chainig devuelve "undefined" pero no salta un error

// Operador NOT (!)

// Se trata de un operador utilziado para negar el valor (invertir) de una variable. Si una variable vale true, al negarla valdrá false y si una variable vale false, al negarla, valdrá false.

console.log(!true); // devuelve false
console.log(!false); // devuelve true
console.log(!!true); // devuelve true
console.log(!44); // devuelve false
console.log(!0); // devuelve true (el 0 se evalua como false)
console.log(!(10 || 23)); // devuelve false

// ---------------> 6. Operadores de bits <---------------

// Se trata de una serie de operadores que nos permiten realizar operaciones básicas trabajando a nivel binario, donde los operandos solo pueden tomar valores de 0 o 1:

// x & y	Realiza una operación AND binaria. Devuelve 1 en las posiciones de bit dónde las posiciones de los dos operadores tienen un 1.
// x | y	Realiza una operación OR binaria. Devuelve un cero en las posiciones de bit dónde las posiciones de los dos operadores tienen un 0.
// x ^ y	Realiza una operación XOR binaria. Devuelve un cero en las posiciones dónde el bit es el mismo y un 1 dónde las posiciones son diferentes.
// ~ x	Realiza una operación NOT binaria.
// x << y	Realiza un desplazamiento de bits a la izquierda.
// x >> y	Realiza un desplazamiento de bits a la derecha.
// x >>> y	Realiza un desplazamiento de bits a la derecha rellenando con ceros. */

let a = 9; // en bits: 1001
let b = 12; // en bits: 1100

console.log(a & b); // Devuelve 1000 - 8
console.log(a | b); // Devuelve 1101 - 13
console.log(a ^ b); // Devuelve 0101 - 5

// Para ver las operaciones de desplazamiento de bits se npuede calcular las potencias de 2:

let c = 2; // en bits: 000010

console.log(c << 1); // Devuelve 000100 - 4
console.log(c << 2); // Devuelve 001000 - 8
console.log(c << 3); // Devuelve 010000 - 16
console.log(c << 4); // Devuelve 100000 - 32

// <<<---------------------->>> Estructuras de control <<<---------------------->>>

// ---------------> Condicionales if/else <---------------

// Condicional if
let nota1 = 7;
console.log('He realizado mi examen.');

// Condición (si la nota es mayor o igual a 5)
if (nota1 >= 5) {
    console.log('¡Estoy aprobado!');
}

// Condicional if-else

let nota2 = 7;
console.log('He realizado mi examen. Mi resultado es el siguiente:');

if (nota2 < 5) {
    // Acción A: nota es menor que 5
    calificacion = 'suspendido';
} else {
    // Acción B: Cualquier otro caso diferente a A (nota es mayor o igual que 5)
    calificacion = 'aprobado';
}

console.log('Estoy', calificacion);

// ---------------> Condicional switch <---------------

// La estructura de control switch permite definir casos específicos a realizar cuando la variable expuesta como condición sea igual a los valores que se especifican a continuación mediante cada case. En el caso de que no se encuentre una coincidencia entre las opciones el resultado del switch será lo establecido en el case default

let instrumento = 'oboe';

switch (instrumento) {
    case 'trompeta':
        console.log('Toco la trompeta');
        break;
    case 'flauta':
        console.log('Toco la flauta');
        break;
    case 'oboe':
        console.log('Toco el oboe');
        break;
    default:
        console.log('No toco un instrumento. Lo siento');
        break;
}

// ---------------> Ciclos, bucles o loops <---------------

// Ciclo for

//  El bucle FOR se utiliza para repetir una o más instrucciones un determinado número de veces. De entre todos los bucles, el FOR se suele utilizar cuando sabemos seguro el número de veces que queremos que se ejecute. La sintaxis del bucle for se muestra a continuación:

/* for (inicialización; condición; actualización) {
    //sentencias a ejecutar en cada iteración
} */

// Ejemplo:

for (var i = 0; i < 5; i++) {
    console.log(i);
}

console.log(' Final del bucle for');

// Ciclo for...of

// La sentencia sentencia for...of ejecuta un bloque de código para cada elemento de un objeto iterable, como lo son: String, Array, objetos similares a array,TypedArray, Map (en-US), Set e iterables definidos por el usuario. Su sintaxis es:

/* for (variable of iterable) {
    statement;
} */

//Ejemplo:

let iterable = ['trenes', 'camiones', 'tractores'];

for (let value of iterable) {
    console.log(value);
}

console.log(' Final del bucle for...of');

// Ciclo for...in

// La instrucción for-in itera sobre todas las propiedades enumerables de un objeto que está codificado por cadenas (ignorando los codificados por Símbolos, incluidas las propiedades enumerables heredadas). Su sintaxis es:

/* for (variable in objeto) instrucción; */

// Ejemplo:

const object = { auto: 'mercedes', deporte: 'natacion', trabajo: 'backend' };

for (const property in object) {
    console.log(`${property}: ${object[property]}`);
}

console.log(' Final del bucle for...in');

// Ciclo while

// El bucle while empieza por evaluar la condición. Si la condición es verdadera (devuelve true), entonces las sentencias son ejecutadas. Si la condición es falsa (devuelve false), entonces las sentencias no son ejecutadas. Luego el bucle finaliza. Su sintaxis es:

/* while (condicion) {
    sentencia(s);
} */

// Ejemplo:

var i = 1;
while (i < 5) {
    console.log(i);
    i++; // i=i+1 esto sería lo mismo
}

console.log(' Final del bucle while');

// Ciclo do-while

// El bucle  do...while está cercanamente relacionado al bucle while . En el bucle  do...while , la condición se evalúa al final. La sintaxis para este bucle es:

/*  do {

   *Sentencias;*

} while (*condicion*); */

// Ejemplo:

var i = 0;
do {
    i = i + 1;
    console.log(i);
} while (i < 5);

console.log(' Final del bucle do-while');

// <<<---------------------->>> Ejercicio extra <<<---------------------->>>

for (let m = 10; m < 56; m++) {
    if (m % 2 == 0 && m != 16 && m % 3 !== 0) {
        console.log(m);
    }
}

/*El resultado del ejercicio es:
10
14
20
22
26
28
32
34
38
40
44
46
50
52 
*/
