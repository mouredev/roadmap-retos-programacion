// Operadores en JavaScript

// Operadores Básicos (Operadores aritméticos, de asignación y unarios.)

// Operadores de asignación. Permiten asignar el resultado de una operación a una variable: 
/* 
+= Adición asignación 
-= Resta asignación 
*= Multiplicación asignación
/= División asignación 
*/

let number1 = 3;
let number2 = 6;

// Operadores de comparación
//El operador de comparacion (==) comprueba si sus dos operandos son iguales y devuelve un resultado booleano. A diferencia del operador de igualdad estricta (===), es que este convierte y compara operandos que son de diferentes tipos.

// Sintaxis: x == y

console.log(3 == number1); // Igual
console.log(number1 != 4); // No es igual
console.log("3" === number1); // Estrictamente igual
console.log(number1 !== "3"); // Desigualdad estricta
console.log(number1 > n2); // Mayor que
console.log(number1 >= number1); // Mayor o igual que
console.log(number1 > n2); // Menor que
console.log(number1 <= n2); // Menor o igual que

// Operadores aritméticos. Permiten realizar operaciones matemáticas como sumas, restas, multiplicaciones y divisiones:
/* 
* Multiplicación 
/ División 
% Módulo de división (resto) 
+ Suma 
- Resta 
 */

console.log(number1 + n2); // Suma
console.log(number1 - n2); // Resta
console.log(number1 * n2); // Multiplicación
console.log(number1 / n2); // División
console.log(number1 % n2); // Residuo
console.log(number1++); // Incremento
console.log(number1--); // Decremento

// Operadores bit a bit (bitwise) permiten realizar operaciones que se hacen más «cerca de la máquina», por lo que son más eficientes. Esto es ideal si necesitamos realizar operaciones intensivas de forma masiva, ya que al llamarlas gran cantidad de veces, una mejora de rendimiento se vuelve notable.
/* 
AND: Devuelve un 1 en cada posición de bit para la que los bits correspondientes en ambos operandos es un 1. 
OR: Devuelve un 1 en. 
XOR: Manipula bits directamente. 
NOT: Manipula bits directamente. 
Desplazamientos: Manipula bits directamente. 
 */
let a = 6; // 0110 en binario
let b = 3; // 0011 en binario

console.log(a & b); // AND bit a bit: 0010 (salida: 2)
console.log(a | b); // OR bit a bit: 0111 (salida: 7)
console.log(a ^ b); // XOR bit a bit: 0101 (salida: 5)
console.log(~a); // NOT bit a bit: 1001 (en complemento a dos, salida: -7)
console.log(a << 1); // Desplazamiento a la izquierda: 1100 (salida: 12)
console.log(a >> 1); // Desplazamiento a la derecha con signo: 0011 (salida: 3)
console.log(a >>> 1); // Desplazamiento a la derecha sin signo: 0011 (salida: 3)

// Operadores lógicos. Hay cuatro operadores lógicos en JavaScript: || (O), && (Y), ! (NO), ?? (Fusión de nulos). El operador ?? Aunque sean llamados lógicos, pueden ser aplicados a valores de cualquier tipo, no solo booleanos. El resultado también puede ser de cualquier tipo.

let p = 8;
let q = 3;

let resultado1 = p > q && q > 0; // true && true => true
console.log(resultado1); // Salida: true

let resultado2 = p < q || q > 0; // false || true => true
console.log(resultado2); // Salida: true

let resultado3 = !(p < q); // !false => true
console.log(resultado3); // Salida: true

let m = false;
let n = true;
let o = false;

let resultado4 = m || (n && o); // false || true && false => false || false => false
console.log(resultado4); // Salida: false

let resultado5 = !(m || (n && o)); // !(false || (true && false)) => !(false || false) => !false => true
console.log(resultado5); // Salida: true

// Operadores de cadena
let r = "JavaScript";
console.log("Hola mundo desde " + r); // Operador de concatenación

let s = "Java";
s += "Script"; // Operador de concatenación abreviada
console.log(s);

// Operador condicional (Ternario) El operador ternario es una alternativa al condicional if/else de una forma mucho más compacta y breve, que en muchos casos resulta más legible. Sin embargo, hay que tener cuidado, porque su sobreutilización puede ser contraproducente y producir un código más difícil de leer.
//Sintaxis
//condición ? valor verdadero : valor falso;

let nota = 7;
console.log("He realizado mi examen. Mi resultado es el siguiente:");

if (nota < 5) {
  // Acción A: nota es menor que 5
    calificacion = "suspendido";
} else {
  // Acción B: Cualquier otro caso diferente a A (nota es mayor o igual que 5)
    calificacion = "aprobado";
}

console.log("Estoy", calificacion);

/* Utilizando las operaciones con operadores que tú quieras, crea ejemplos que representen todos los tipos de estructuras de control que existan en tu lenguaje: Condicionales, iterativas, excepciones... */

// Condicional
if (edad >= 18) {
    console.log("Eres mayor de edad.");
} else {
    console.log("Eres menor de edad.");
}

// Bucle for
let mult = 5;
for (let n = 1; n <= 12; n++) {
  console.log(`${mult} x ${n} = ${mult * n}`);
}

// Bucle for. El bucle for es quizás uno de los más utilizados en el mundo de la programación. En Javascript se utiliza exactamente igual que en otros lenguajes como Java o C/C++. 
// for (inicialización; condición; incremento)
for (let i = 0; i < 5; i++) {
    console.log("Valor de i:", i);
}

// Bucle for...in La declaración for...in itera sobre todas las propiedades de cadena enumerables de un objeto (ignorando las propiedades codificadas por símbolos), incluidas las propiedades enumerables heredadas.

//Sintaxis:
/* 
for (variable in object)
    statement
*/

// Bucle for...of La instrucción for...of ejecuta un bucle que opera sobre una secuencia de valores provenientes de un objeto iterable. Los objetos iterables incluyen instancias de funciones integradas como Array, String, TypedArray, Map, Set, NodeList (y otras colecciones DOM), así como el objeto de argumentos, los generadores producidos por funciones generadoras y los iterables definidos por el usuario.

const array1 = ['a', 'b', 'c'];

for (const element of array1) {
    console.log(element);
}

// Expected output: "a"
// Expected output: "b"
// Expected output: "c"



// Bucle while Crea un bucle que ejecuta una sentencia especificada mientras cierta condición se evalúe como verdadera. Dicha condición es evaluada antes de ejecutar la sentencia

//Sintaxis:
/* 
while (condition) {
    código
    llamado "cuerpo del bucle"
}
 */
let i = 0;
while (i < 3) {
  // muestra 0, luego 1, luego 2
    alert(i);
    i++;
}

// Bucle Do While La sentencia (hacer mientras) crea un bucle que ejecuta una sentencia especificada, hasta que la condición de comprobación se evalúa como falsa. La condición se evalúa después de ejecutar la sentencia, dando como resultado que la sentencia especificada se ejecute al menos una vez.
let result = '';
let i = 0;

do {
    i = i + 1;
    result = result + i;
} while (i < 5);

console.log(result);
// Expected output: "12345"



// Switch La declaración switch evalúa una expresión, comparando el valor de esa expresión con una instancia case, y ejecuta declaraciones asociadas a ese case, así como las declaraciones en los case que siguen.
switch (expr) {
    case "Naranjas":
        console.log("El kilogramo de naranjas cuesta $0.59.");
        break;
    case "Manzanas":
        console.log("El kilogramo de manzanas cuesta $0.32.");
        break;
    case "Platanos":
        console.log("El kilogramo de platanos cuesta $0.48.");
        break;
    case "Cerezas":
        console.log("El kilogramo de cerezas cuesta $3.00.");
        break;
    case "Mangos":
    case "Papayas":
        console.log("El kilogramo de mangos y papayas cuesta $2.79.");
        break;
    default:
    console.log("Lo lamentamos, por el momento no disponemos de " + expr + ".");
}

console.log("¿Hay algo más que te quisiera consultar?");

/* Crea un programa que imprima por consola todos los números comprendidos entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3. */

for (let n = 10; n <= 55; n++) {
    if (n % 2 === 0 && n !== 16 && n % 3 !== 0) {
        onsole.log(n);
    }
}
