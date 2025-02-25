// Operadores de asignación 

/**Asignación */
var x = 5; // x = y;
var y = 10;
console.log(x);
/**Asignación de adición */
x += y; // x = x + y;
console.log(x);
/**Asignación de resta */
x -= y; // x = x - y;
console.log(x);
/**Asignación de multiplicación */
x *= y; // x = x * y;
console.log(x);
/**Asignación de división */
x /= y; // x = x / y;
console.log(x);
/**Asignación de residuo */
x %= y; // x = x % y;
console.log(x);
/**Asignación de exponenciación */
x **= y; // x = x ** y;
console.log(x);
/**Asignación de desplazamiento a la izquierda */
x <<= y; // x = x << y;
console.log(x);
/**Asignación de desplazamiento a la derecha */
x >>= y; // x = x >> y;
console.log(x);
/**Asignación de desplazamiento a la derecha sin signo*/
x >>>= y; //x = x >>> y
console.log(x);
/**Asignación AND bit a bit*/
x &= y; // x = x & y;
console.log(x);
/**Asignación XOR bit a bit*/
x ^= y; // x = x ^ y;
console.log(x);
/**Asignación OR bit a bit*/
x |= y; // x = x | y;
console.log(x);
/**Asignación AND lógico*/
x &&= y; // x && (x = y);
console.log(x);
/**Asignación OR lógico*/
x ||= y; // x || (x = y);
console.log(x);
/**Asignación de anulación lógica */
x ??= y; // x ?? (x = y)
console.log(x);

// Operadores de comparación 
var x = 10;
var y = 15;
var var1 = true;
var var2 = false;

/**Igualdad */
var z = var1 == var2;
console.log(z);
/**No es igual */
var z = var1 != var2;
console.log(z);
/**Estrictamente igual */
var z = x === y;
console.log(z);
var a = var1 === var2;
console.log(a);
/**Desigualdad estricta */
var z = var1 !== var2;
console.log(z);
/**Mayor que */
var z = x > y;
console.log(z);
/**Mayor o igual que */
var z = x >= y;
console.log(z);
/**Menor que */
var z = x < y;
console.log(z);
/**Menor o igual que */
var z = x <= y;
console.log(z)

//Operadores aritméticos
var x = 12;
var y = 5;

/**Residuo */
var z = x % y;
console.log(z);
/**Incremento */
var z = x++;
console.log(z);
var b = ++x;
console.log(b);
/**Decremento */
var z = x--;
console.log(z);
var b = --x;
console.log(b);
/**Negación Unitaria */
var z = -x;
console.log(z);
/**Positivo Unitario */
var z = +"3";
console.log(z, typeof(z));
/**Operador de exponenciación */
var z = x ** y;
console.log(z);

//Operadores bit a bit
var a = 1;
var b = 0;

/**AND a nivel de bits */
var z = a & b;
console.log(z);
/**OR a nivel de bits */
var z = a | b;
console.log(z);
/**XOR a nivel de bits */
var z = a ^ b;
console.log(z);
/**NOT a nivel de bits */
var z = ~ a;
console.log(z);
/**Desplazamiento a la izquierda */
var z = a << b;
console.log(z);
/**Desplazamiento a la derecha de propagación de signo */
var z = a >> b;
console.log(z);
/**Desplazamiento a la derecha de relleno cero */
var z = a >>> b;
console.log(z);

//Operador de desplazamiento de bits
var a = 9;
var b = 2;

/**Desplazamiento a la izquierda */
console.log(a << b);
/**Desplazamiento a la derecha de propagación de signo */
console.log(a >> b);
/**Desplazamiento a la derecha de relleno cero */
console.log(a >>> b);

//Operadores Lógicos
let expr1 = true;
let expr2 = false;

/**AND lógico */
console.log(expr1 && expr2);
/**OR Lógico */
console.log(expr1 || expr2);
/**NOT Lógico */
console.log(!expr1);
console.log(!expr2);

//Operador de Cadena
console.log('Hola ' + 'JavaScript' );

let hello = 'Hola ';
console.log(hello += 'JavaScript');

//Operador condicional (ternario)
let val1 = 20;
let val2 = 15;

let isAdult = val2 >= 18 ? 'Adult' : 'Minor';
console.log(isAdult);

//Operador unarios

/**DELETE */
x = 42;
var o = 43;
var myObj = { h:4, }

console.log(delete x);
console.log(delete o);
console.log(delete Math.PI);
console.log(delete myObj.h);

/**typeof */
let myFun = new Function('5 + 2');
let myName = 'Alexander';
let age = 26;
let fruit = ['apple', 'wathermelon', 'Banana'];

console.log(typeof(myFun));
console.log(typeof(myName));
console.log(typeof(age));
console.log(typeof(fruit));
console.log(typeof(true));

