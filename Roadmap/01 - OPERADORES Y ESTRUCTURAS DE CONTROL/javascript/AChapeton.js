// *** OPERADORES DE ASIGNACION ***
//Asignacion
var x = 5;
var y = 10;
console.log('Asignacion:', x, y);

//Asignacion de Adicion
x = x + y;
console.log('Adicion 1:', x);

x += y;
console.log('Adicion 2:', x);

//Asignacion de Resta
x = x - y;
console.log('Resta 1:', x);

x -= y;
console.log('Resta 2:', x);

//Asignacion de Multiplicacion
x = x * y;
console.log('Multiplicacion 1:', x);
x *= y;
console.log('Multiplicacion 2:', x);

//Asignacion de Division
x = x / y;
console.log('Division 1:', x);
x /= y;
console.log('Division 2:', x);

//Asignacion de Residuo
x = x % y;
console.log('Residuo 1:', x);
x %= y;
console.log('Residuo 2:', x);

//Asignacion de Exponente
x = Math.pow(x, y);
console.log('Exponente 1:', x);
x = Math.pow(x, y);
console.log('Exponente 2:', x);

//Asignacion AND logico
x = x && (x = y);
console.log('AND logico 1:', x);
x && (x = y);
console.log('AND logico 2:', x);

//Asignacion OR logico
x = x || (x = y);
console.log('OR logico 1:', x);
x || (x = y);
console.log('OR logico 2:', x);

//Asignacion Anulacion logico
x = x !== null && x !== void 0 ? x : (x = y);
console.log('Anulacion logico 1:', x);
x !== null && x !== void 0 ? x : (x = y);
console.log('Anulacion logico 2:', x);


// *** OPERADORES DE COMPARACION ***
var a = 4;
var b = 8;
//Igual
console.log('Igual: ', a == b);

//No es igual
console.log('No es igual: ', a != b);

//Igualdad estricta
console.log('Igualdad estricta: ', a === b);

//Desigualdad estricta
console.log('Desigualdad estricta: ', a !== b);

//Mayor que
console.log('Mayor que: ', a > b);

//Mayor o igual que
console.log('Mayor o igual que: ', a >= b);

//Menor que
console.log('Menor que: ', a < b);

//Menor o igual que
console.log('Menor o igual que: ', a <= b);


// *** OPERADORES ARITMETICOS ***
var num1 = 10;
var num2 = 4;
//Residuo
console.log('Residuo: ', num1 % num2);

//Incremento
console.log('Incremento antes de imprimir: ', ++num1);
console.log('Incremento despues de imprimir: ', num1++); //Se vuelve 12 luego de imprimir

//Decremento
console.log('Decremento antes de imprimir: ', --num1);
console.log('Decremento despues de imprimir: ', num1--); //Se vuelve 10 luego de imprimir

//Negacion unitaria
console.log('Negacion unitaria: ', -num1);

//Positivo unitaria
console.log('Negacion unitaria: ', +num1);
//Exponenciacion

console.log('Exponenciacion: ', Math.pow(num1, num2));


// *** OPERADORES BIT A BIT ***
var bit1 = 6;
var bit2 = 8;

//Desplazamiento a la izquierda
console.log('Desplazamiento a la izquierda:', bit1 << bit2);

//Desplazamiento a la derecha
console.log('Desplazamiento a la derecha:', bit1 >> bit2);

//AND
console.log('AND bit a bit:', bit1 & bit2);

//OR
console.log('AND bit a bit:', bit1 | bit2);

//XOR
console.log('AND bit a bit:', bit1 ^ bit2);

//NOT
console.log('AND bit a bit:', bit1, ~bit2);


// *** OPERADORES LOGICOS ***
var exp1 = true;
var exp2 = false;

//AND logico
console.log('AND Logico: ', exp1 && exp2);

//OR logico
console.log('OR Logico: ', exp1 || exp2);

//NOT logico
console.log('NOT Logico: ', !exp1);


// *** OPERADORES DE CADENA ***
console.log("mi " + "cadena");


// *** OPERADOR CONDDICIONAL TERNARIO ***

var result = true ? true : false;
console.log(result);
var user = {
    id: '1',
    name: 'Andres',
    age: 86
};

console.log('Existe "age" en el objeto user?: ', 'age' in user);
console.log('Existe "country" en el objeto user?: ', 'country' in user);


// *** ESTRUCTURAS DE CONTROL ***

// * CONDICIONAL *

var num = 25;
// IF-ELSE
if (num > 18) {
    console.log('Es mayor de edad');
}
else {
    console.log('Es menor de edad');
}

//SWITCH
switch (num) {
    case 20:
        console.log('Es 20');
        break;
    case 25:
        console.log('Es 25');
        break;
    case 30:
        console.log('Es 30');
        break;
    default:
        console.log('Default');
        break;
}


// * BUCLES *
var i = 10;
var w = 15;

//WHILE
while (i < w) {
    i++;
    console.log('Nuevo valor de i:', i);
}

//DO-WHILE
i = 10;
do {
    i++;
    console.log('Nuevo valor de i:', i);
} while (i < w);

//FOR
for (var i_1 = 0; i_1 < 10; i_1++) {
    console.log('Nuevo valor de i:', i_1);
}


// *** EJERCICIO EXTRA ***
console.log('EJERCICIO EXTRA');

for (var i_2 = 10; i_2 <= 55; i_2++) {
    if (i_2 % 2 === 0) {
        if (i_2 === 16) {
            console.log('Ignorar');
        }
        else if (i_2 % 3 === 0) {
            console.log('Multiplo de 3');
        }
        else {
            console.log(i_2);
        }
    }
    else {
        console.log('No es par');
    }
}
