//#O1 Roadmap de programación "Operadores y Estructuras de Control".

/*
Operadores 
*/

//Operadores Aritmetricos.
console.log("Suma -->" + (2+2));
console.log("Resta -->" + (2-2));
console.log("Multiplicacion -->" + (2*2));
console.log("Division -->" + (2/2));
console.log("Porcentajes -->" + (2%2));
console.log("Exponenetes -->" + (2**6));

//Operadores de asignacion.
let x = 2;
x = 5;
console.log("Asignacion --> " + x);
//Operadores de incremento y decremento.
let num1 = 4;
num1++;
num1;
console.log("Incrementeo --> " + num1);
let num2 = 6;
num2--;
num2;
console.log("Decremento --> " + num2);

//Operadores de Comparación.
/*
A veces querremos ejecutar pruebas 
de verdadero/falso, y luego actuaremos 
de acuerdo con el resultado de esa prueba. 
Para ello, utilizamos operadores de comparación.
*/
/*
Son los Siguientes: 
- Igual Estricto "===" (Comprueba si los valores izquierdo y derecho son idénticos entre sí)
- Desigual Estricto "!==" (Comprueba si los valores izquierdo y derecho no son idénticos entre sí)
- Mayor que ">" (Comprueba si el valor izquierdo es mayor que el derecho.)
- Menor que "<" (Comprueba si el valor izquierdo es menor que el derecho.)
- Mayor o igual que ">=" (Comprueba si el valor izquierdo es mayor o igual que el derecho..)
- Menor o igual que "<=" (Comprueba si el valor izquierdo es menor o igual que el derecho.)
*/
console.log("Igual Estricto --> " + (2=== 2));
console.log("Desigual Estricto --> " + (2!= 2));
console.log("Mayor que --> " + (2> 2));
console.log("Menor que --> " + (2< 2));
console.log("Mayor o igual que --> " + (2>= 2));
console.log("Menor o igual que --> " + (2<= 2));

//Operadores Logicos.
// Operador Y lógico (`&&`)
let a = true;
let b = true;

if (a && b) {
  console.log("Ambos operandos son verdaderos");
} else {
  console.log("Al menos uno de los operandos es falso");
}

// Operador O lógico (`||`)
let c = false;
let d = true;

if (c || d) {
  console.log("Al menos uno de los operandos es verdadero");
} else {
  console.log("Ambos operandos son falsos");
}

// Operador NO lógico (`!`)
let e = true;

if (!e) {
  console.log("El operando es falso");
} else {
  console.log("El operando es verdadero");
}
//Operadores de Bit.
let bitUno = 10;
let = bitDos = 5;

console.log("AND --> " + (bitUno & bitDos));
console.log("OR --> " + (bitUno | bitDos));
console.log("XOR --> " + (bitUno ^ bitDos));
console.log("NOT --> " + (~bitUno));
console.log("NOT --> " + (~bitDos));
console.log("Se mueve a la drecha --> " + (bitUno >> 2));
console.log("Se mueve a la izquierda --> " + (bitUno << 2));

/* 
Estructuras de Control. JavaScript.
*/
//- Estructuras Condicionales. 
//if, else if, else.
//Estas estruturas nos permiten ejecutar un bloque de codigo simepre y cuando se cumpla una condición.

let string = "Hola Mundo";

if (string == "Hola Mundo") { //Lo que nos permite If es ejecutar si la condición es verdadera.
  console.log("Bien y tu?");
} else {
  console.log("No te entiendo TwT") //En este caso else, nos permite ejecutar si la condición es falsa.
}
//Al final estas Dos tambien forman una estrutura if-else.

/*
En JavaScript.
Tenemos tambien las interativas, que son blucles al final. 
Como for, while y hasta Swich. 
*/

for (let i = 0; i < 10; i++) {
  console.log(i);
}

let casa = 10;
while (casa < 20) {
  console.log(casa);
  casa++;
}

let Componentes = "Pantalla";
switch (Componentes) {
  case "CPU":
    console.log("Procesador");
    break;
  case "Pantalla": 
    console.log("Pantalla");
    break;
  case "Teclado":
    console.log("Teclado");
    break;
  default:
    console.log("No existe");
}

//Fin del Reto Semanal. :D.

//**DESARROLLO DE LA DICICULTAD EXTRA. */
/* Crea un programa que imprima por consola todos los números comprendidos
* entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.*/

for (let i=10; i<=55; i++) {
  if (i%2==0 && i!=16 && i%3!=0) {
    console.log("Solución " +i) 
  }
}
