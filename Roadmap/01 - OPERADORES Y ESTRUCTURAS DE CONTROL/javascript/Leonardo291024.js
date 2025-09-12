// Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...

//Operadores aritmeticos:
const suma = 10 + 5;
const resta = 10 - 5;
const multiplicacion = 10 * 5;
const divicion = 10 / 5;

console.log(suma, resta, multiplicacion, divicion);

//Operadores de comparacion:
const igualdad = 10 == 10;
const desigualdad = 10 !== 10;
const menorQue = 10 < 6;
const menorOIgual = 10 <= 6;
const mayorQue = 10 > 16;
const mayorOIgual = 10 >= 6;


console.log(igualdad, desigualdad, menorQue, menorOIgual, mayorQue, mayorQue);

//Operadores logicos
const and = a && b;
const or = a || b;
const not = !a;

//operador de asignacion
const name = "Leonardo";


//Utilizando las operaciones con operadores que tú quieras, crea ejemplos que representen todos los tipos deestructuras de control que existan en tu lenguaje:Condicionales, iterativas, excepciones...

let a = 18;
let b = 5;

if(a === 10){
    console.log(a + b);
}else{
    console.log("El numero a no es 10");
}

for(let i = 0; i <= 10; i++){
    console.log(i);
}

let num = 0;

while(num <= 10){
    console.log(num);
    num++
}

//Crea un programa que imprima por consola todos los números comprendidos entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.

for(let i = 0; i <= 55; i++){
    if(i %2 === 0 && i !== 16 && i %3 != 0){
        console.log(i);
    }
}