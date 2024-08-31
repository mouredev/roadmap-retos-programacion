//Tipos de oparadores en javascript

//Arimeticos

let num1 = 5;
let num2 = 2;

console.log('OPERADORES ARITMETICOS');
let suma = (num1 + num2);
console.log('El resultado de la suma es:', suma);//SUMA
let resta = (num1 - num2);
console.log('El resultado de la resta es:', resta);//RESTA
let division = (num1 / num2);
console.log('El resultado de la division es:', division);//DIVISION
let multiplicacion = (num1 * num2);
console.log('El resultado de la multiplicacion es:', multiplicacion);//MULTIPLICACION
let resto = (num1 % num2);
console.log('El resultado del resto es:', resto);//RESTO O MODULO
let potencia = (num1 ** num2);
console.log('El resultado de la potencia es:', potencia);//POTENCIA

//Logicos

let estudiante = true;
let programador = true;

console.log('OPERADORES LOGICOS');
//And 
console.log('Operador and', estudiante && programador); //Ambos deben ser true para que se cumpla 
//Or
console.log('Operador Or', estudiante || programador); //Al menos una variable debe ser true 
//Not
console.log('Operador Not', !estudiante); //Invierte el valor de la variable 

//Comparacion 

let a = 10;
let b = 5

console.log('OPERADORES DE COMPARACION');
console.log(a > b); //Mayor que...
console.log(a < b); //Menor que...
console.log(a >= b); //Mayor o igual que...
console.log(a <= b); //Menor o igual que...
console.log(a == b); //Igual a...
console.log(a != b); //Distinto que...
console.log(a === 'numero'); //Compara con un string
console.log(a !== 'numero'); //Compara con un string distinto 

//Asignacion

a += 5; //Aumenta valor en 5
a -= 3; //Disminuye valor en 3
console.log('OPERADORES DE ASIGNACION');
console.log(a);

//Operadores de control de flujo

console.log('OPERADOR IF');
//IF
if(num1 > num2){
    console.log('Numero1 es mayor a Numero2')
}
console.log('OPERADOR ELSE');
//ELSE
if(num1 > num2){
    console.log('Numero1 es mayor a Numero2');
}else{
    console.log('Numero1 es menor a Numero2');
}
console.log('OPERADOR ELSE IF');
//ELSE IF 
if(num1 > num2){
    console.log('Numero1 es mayor a Numero2');
}else if(num1 < num2){
    console.log('Numero1 es menor a Numero2');
}else{
    console.log('Numero1 es igual a Numero2');
}
console.log('OPERADOR WHILE');
//WHILE
let contador = 1; //Declaracion de variable 

while(contador <= 5){
    console.log(contador);
    contador++;
}
console.log('OPERADOR DO WHILE');
//DO WHILE
let contador2 = 1;
do{
    console.log(contador2);
    contador2++;
}while(contador2 <= 3);
console.log('OPERADOR FOR');
//FOR
let numero = 9;
for(i=1; i <= numero; i++){
    console.log(i);
}

/*DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.*/

console.log('EJERCICIO EXTRA');

for(let j = 10; j <= 55; j++){
    if(j % 2 === 0 && j !== 16 && j % 3 !== 0){
        console.log(j);
    }
}
