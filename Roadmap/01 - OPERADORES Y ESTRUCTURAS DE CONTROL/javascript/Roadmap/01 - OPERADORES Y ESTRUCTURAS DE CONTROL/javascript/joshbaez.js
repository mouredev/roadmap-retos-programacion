// OPERADORES 

// OPERADORES ARITMETICOS 

let number1 = 15 
let number2 = 10

//  SUMA (+) RESTA (-) MULTIPLICACION (*) DIVISION (/) MODULO (%)

let suma = number1 + number2; 
console.log(suma);
let resta = number1 - number2;
console.log(resta);
let multi = number1 * number2;
console.log(multi);
let divi = number1 / number2;
console.log(divi);
let modu = number1 % number2;
console.log(modu);
let expo = number1 ** number2;
console.log(expo);

// INCREMENTO (++)

let x = 5; 
console.log(x); // valor inicial de x: 5

x++;
console.log(x); // despues de incremento valor de x: 6

// DECREMENTO (--) 

let a = 10; 
console.log(a); // valor inicial de a: 10

a--;
console.log(a); // despues de decremento valor de a: 9

// INCREMENTO Y DECREMNETO CON OPERADORES PREFIJO Y SUFIJO

let c = 5; 
console.log(c); // valor inicial de c: 5 

console.log(++c); // prefijo (++c) Incrementa c a 6 y devuelve 6
console.log(c++); // sufijo (c++) Devuelve 6 y luego incrementa c a 7

let z = 10;
console.log(z);

console.log(--z); // Decrementa d a 9 y devuelve 9
console.log(z--); // Devuelve 9 y luego decrementa d a 8

// OPERADORES DE ASIGNACION 

let ope = 10;
console.log(ope); // 10 

// Asignación de Suma (+=)

ope += 3; 
console.log(ope);

// Asignación de Resta (-=)

ope -=  4;
console.log(ope);

// Asignación de Multiplicación (*=) 

ope *= 20;
console.log(ope);

// Asignación de División (/=)

ope /= 7;
console.log(ope);

// Asignación de Módulo (%=)

ope %= 14;
console.log(ope);

// Asignación de Exponenciación (**=) 

ope **= 50;
console.log(ope);

// OPERADORES DE COMPARACION 

// Igualdad ('==')

console.log(5 == '5'); // true 
console.log(5 == 5); // true
console.log(5 ==  6); // false 

// Desigualdad (!=)

console.log(5 != '5'); // false debido a tipos diferentes
console.log(5 != 6); // true 

// Identidad (===)

console.log(5 === '5'); // false, no hay conversión de tipo
console.log(5 === 5); // true 

// No identidad (!==)

console.log(5 !== 5); // true 
console.log(5 !== 5); // false 

// Mayor que (>)

console.log(10 > 5); // true 
console.log(5 > 10); // false 

// Mayor o igual que (>=)

console.log(10 >= 5); // true 
console.log(5 >= 5); // false
console.log(10 >= 10); // true 

// Menor que (<)

console.log(5 < 10); // true
console.log(10 < 5); // false 

// Menor o igual que (<=)

console.log(5 <= 10); //true
console.log(10 <= 5); // false
console.log(5 <= 5); // ture 

// Operadores logicos

// and logico 

console.log(true && true); // true
console.log(true && false); // false 
console.log(false && true); // false
console.log(false && false); // false 

// or logico 

console.log(true || true); // true
console.log(true || false); // true 
console.log(false || true); // true 
console.log(false || false); // false

// not logico 

console.log(!true); // false
console.log(!false); // true 

// Operadores Bit a Bit

// and bit a bit (&) 

let j = 5;  // 0101 en binario
let b = 3;  // 0011 en binario

console.log(a & b);  // 1 (0001 en binario)

// OR bit a bit (|)

let g = 5;  // 0101 en binario
let t = 3;  // 0011 en binario

console.log(a | b);  // 7 (0111 en binario)

// XOR bit a bit (^)

let w = 5;  // 0101 en binario
let u = 3;  // 0011 en binario

console.log(a ^ b);  // 6 (0110 en binario)

// Operadores de cadena 

// concatenacion (+)

let nombre = "josh";
let apellido = "baez";
let nombreCompleto = nombre + " " +  apellido;

console.log(nombreCompleto); // "josh baez"

// asignacion (+=) 

let mensaje = "hola"; 
mensaje += "como estas";

console.log(mensaje); // "hola como estas"

// plantillas literales 

let apoodo = "yandel";
let edad = 22;

let saludo = `Hola, mi apodo es ${apoodo} y tengo ${edad} años.`;
console.log(saludo); // hola mi apodo es yandel y tengo 22 anos 

// metodo concat()

let str1 = "hola";
let str2 = "mundo";
let resultado = str1.concat(" ", str2 );

console.log(resultado); // hola mundo

// metodo slice() 

let texto = "me gusta javascript";
let parte = texto.slice(0, 10);

console.log(parte); // javascript

// metodo toUpperCase() y toLowerCase()

let str = "hola mundo";

console.log(str.toUpperCase()); // HOLA MUNDO 
console.log(str.toLowerCase()); // hola mundo

// metodo replace() 

let frase = "me gusta mucho javascript";
let nuevafrase = frase.replace("javascript", "programar");

console.log(nuevafrase); // me gusta programar 

// operadores tipo 

// typeof devuelve el tipo 

console.log(typeof 42);          // "number"
console.log(typeof 'hello');     // "string"
console.log(typeof true);        // "boolean"
console.log(typeof undefined);   // "undefined"
console.log(typeof {a: 1});      // "object"
console.log(typeof [1, 2, 3]);   // "object" (en JavaScript, los arrays son objetos)
console.log(typeof function(){});// "function"
console.log(typeof null);        // "object" (esto es un error histórico en JavaScript)

// instanceof 

function Person(name) {
    this.name = name;
}

let john = new Person('John');

console.log(john instanceof Person); // true
console.log(john instanceof Object); // true (en JavaScript, todos los objetos son instancias de Object)
console.log([] instanceof Array);    // true
console.log([] instanceof Object);   // true

// operador condicional ternario 

let edad1 = 18;
let mensaje1 = (edad >= 18) ? "Es mayor de edad" : "Es menor de edad";
console.log(mensaje1);  // "Es mayor de edad"

// dificulta extra: 

for (let i = 10; i <= 55; i++) {
    if (i % 2 === 0 && i !== 16 && i % 3 !== 0) {
        console.log(i);
    }
}

