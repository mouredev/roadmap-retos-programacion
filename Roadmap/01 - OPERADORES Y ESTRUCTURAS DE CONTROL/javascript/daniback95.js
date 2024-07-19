/* 
Operadores
*/

/* 
Binarios: El operador es aplicado a dos operandos
*/
// Aritméticos
console.log(`Suma 3 + 2 = ${3 + 2}`);
console.log(`Resta 3 - 2 = ${3 - 2}`);
console.log(`Multiplicación 3 * 2 = ${3 * 2}`);
console.log(`División 3 / 2 = ${3 / 2}`);
console.log(`Módulo o resto 3 % 2 = ${3 % 2}`);
console.log(`Exponenciación 3 ** 2 = ${3 ** 2}`);

/* 
Operador de concatenación +
Cuando se aplica el oprador + a dos operandos de 
tipo string los une.
*/
let text = 'My' + 'string';
console.log(text);
/* 
Si uno de los operandos es una cadena, el otro operando
también es convertido en una cadena
*/
console.log(1 + '2'); // '12'
console.log('2' + 1); // '21'
console.log(1 + 2 + '3'); // primero: 1 + 2 = 3 luego: 3 + '3' = '33'
console.log('1' + 2 + 3); // primero '1' + 2 = '12' luego '12' + 3 = '123'
/* 
Para tener en cuenta:
El operador binario + es el unico que soporta cadenas 
como las anteriormente vistas, otros operadores como la resta
la multiplicación, división... trabajan sólo con números
y convierte sus operandos a números
*/
console.log(3 - '1'); // 2
console.log('3' * 2); // 6
console.log(3 ** '2'); // 9
console.log('9' / '3'); //3

/* 
Unarios: El operador es aplcado a un solo operando
*/
/* 
Unario +: este operador no hace nada cuando se aplica a números, pero 
cuando se palica a operandos que son número, los convierte en números
*/
let a = '9';
console.log(+a); // 9
let b = '';
console.log(+b); // 0
let c = true;
console.log(+c); // 1
let d = false;
console.log(+d); // 0
let f = true;
console.log(-f); // -1
/* 
Lo que se hizo anteriormente con el operador 
unario + hace lo mismo que la función Number()
*/
let apples = '2';
let oranges = '5';
console.log(apples + oranges); // '25'
console.log(+apples + +oranges); // 7
console.log(+apples + -oranges); // -3

/* 
Operadores de incremento/decremento
Es una manera de incrementar o decrementar valores de manera acortada
*/
let counter = 0;
// incremento usando la forma tradicional
counter = counter + 1; 
console.log(counter); // 1
// incremento de manera acortada
counter++;
console.log(counter); // 2
counter--;
console.log(counter); // 1
/* 
Existe dos formas de usar el incremento/decremento
Como prefijo: devuelve inmendiatamente el nuevo valor
Como sufijo: develve el valor anterior antes de realizar el
incremento/decremento.
Importante: Ambas formas hacen los mismo, incrementar/decrementar,
para poder ver su sutil diferencia debemos usar inmediatamente su
valor
*/
// Prefijo
let counter2 = 1;
++counter; // 2
console.log(counter);
// Sufijo
counter++;
console.log(counter); // 3
/* 
Lo anterior hace lo mismo, ahora veamos su sutil
diferencia
*/
let counter3 = 1;
console.log(++counter3); // nuevo valor: 2
let counter4 = 0;
console.log(counter4++); // devueve su valor anterior: 0 
console.log(counter4); // tenemos el nuevo valor: 1

/* 
Operadores de asignación:
son operadores cortos que modifican y asignan al mismo tiempo, 
son aplicables a todos los operadores aritméticos
*/
let x = 1;
x += 2;
console.log(x); // 3
x *= 3;
console.log(x); // 9
x -= 2;
console.log(x); // 7
x **= 2;
console.log(x); // 49
x /= 7;
console.log(x); // 7

/* 
Operadores de comparación
El resultado de este tipo de operaciones es un valor booleno 
*/
console.log(`Mayor que: 5 > 3 es ${5 > 3}`); // true
console.log(`Menor que: 5 < 3 es ${5 < 3}`); // false
console.log(`Mayor o igal que: 5 >= 5 es ${5 >= 3}`); // true
console.log(`Menor o igaual que: 5 <= 3 es ${5 <= 3}`); // false
console.log(`Igual que: 3 == 3 es ${3 == 3}`); // true
console.log(`Diferente que: 5 != 3 ${5 != 3}`); //true
/* 
Igualdad regular:
Este operador corresponde al de doble igual ==
Este operador realiza primero una coerción de tipo si los valores
son diferentes, convertirlos a un tipo común antes de realizar
la comparción.
Esto también aplica para la diferencia regular !=
*/
console.log(1 == false); // convierte false a 0 
console.log(1 == true); // convierte true a 1
console.log('' == false); // true, cadena vacía la pasa a 0 y false a 0
console.log(null == undefined) // true, se consideran iguales
console.log(1 != true); // false
/* 
Igualda estricta:
Compara los operandos tanto en valor como en tipo, 
no realiza ninguna coerción de tipo
Esto también aplica para la diferencia estricta !==
*/
console.log(null === undefined); // false
console.log(1 === '1'); // false
console.log(1 === true) // false
console.log(1 !== true) // true

// Operadores lógicos
// OR
console.log(`OR ||: 3 > 5 || 3 + 2 == 5 es ${3 > 5 || 3 + 2 == 5}`);
console.log(`1 || 0 es ${ 1 || 0 }`);
console.log(`null || 1 es ${ null || 1 }`);
console.log(`null || 0 || 3 es ${ null || 0 || 3 }`);
console.log(`undefined || 0 || null es ${ undefined || 0 || null}`);
let firstName = '';
let lastName = '';
let nickName = 'SuperCoder';
console.log(firstName || lastName || nickName || 'Anonymous');
nickName || console.log('Esto no se ejecuta');
firstName || console.log(`Ejecutando nickname: ${ nickName }`);

//AND
console.log(`AND &&: 3 < 5 && 3 + 2 == 5 es ${ 3 < 5 && 3 + 2 == 5 }`);
console.log(`1 && 0 es ${ 1 && 0 }`);
console.log(`true && true es ${ true && true }`);
console.log(`null && 1 && '' es ${ null && 1 && '' }`);
console.log(`1 && undefined && null es ${ 1 && undefined && null }`);
console.log(`1 && 0 && null es ${ 1 && 0 && null }`);
console.log(`1 && '0' && null es ${ 1 && '0' && null }`);
console.log(`1 && '' && null es ${ 1 && '' && null }`);
console.log(`1 && 2 && null es ${ 1 && 2 && null }`);
console.log(`0 && 1 && 3 es ${ 0 && 1 && 3 }`);
console.log(`1 && 2 && 3 es ${ 1 && 2 && 3 }`);
1 > 0 && console.log('1 es mayor que cero');

// !NOT
console.log(`NOT !: !true es ${ !true }`);
console.log(`!false es ${ !false }`);
console.log(`!null es ${ !null }`);
console.log(`!!null es ${ !!null }`);

// Operadores Bit
console.log("AND: ", 9 & 7);
console.log("OR: ", 9 | 7);
console.log("XOR: ", 9 ^ 7);
console.log("NOT: ", ~9);
console.log("Left shift: ", 9 << 7);
console.log("Right shift: ", 9 >> 7);
console.log("Zero-fill right shift: ", 9 >>> 3);

/* 
Operador nullish coalescing
*/
let nombre;
let apellido;
let nombrePorDefecto = 'Anónimo';
let user = nombre ?? apellido ?? nombrePorDefecto;
console.log(`Saludando a user: ${user}`);
console.log(nombre ?? apellido ?? nickName);
let heigth = 0
console.log('heitg es: ', heigth || 100); // 100
console.log('heitg es: ', heigth ?? 100); // 0 
/* 
Condicionales
*/

// if / else
let ageUser = 23;
let minimunAge = 18;
if(ageUser >= 18) {
  console.log('Es mayor de edad, puede ingresar');
} else {
  console.log('Es menor de edad, no puede ingresar');
}

let num = -2;
if(num > 0) {
  console.log(1);
} else if(num < 0) {
  console.log(-1);
} else {
  console.log(0);
}

// Ternario
let age = 25;
let message = (age < 18) ? 'Hola niño' : 
  (age < 25) ? '!Hola¡' :
  (age < 50) ? '!Qué tal¡' : 'Saludos';

console.log(message);

/* 
Condicionales
*/
// while
let i = 0;
while(i < 3) {
  console.log(i);
  i++;
}
while(i != 0) {
  console.log(i);
  i--;
}
// do while
do {
  console.log(i);
  i++
} while(i < 3)

// for
for (let j = 0; j<=5; j++) {
  console.log('el valor de j es', j)
}
let k = 0;
for (k; k <= 10; k++) {
  let result = 3 * k;
  console.log(`3 * ${k} = ${result}`);
}

for (num = 10; num <= 55; num++) {
  if(num % 2 == 0 && num != 16 && num % 3 != 0) {
    console.log(num);
  }
}