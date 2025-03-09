//OPERADORES DE ASIGNACIÓN (Los más usados):

// Asigna un valor a su operando izquierdo 
let valor1=5; //(Asignación) Asigna a la variable valor, el valor de 5
console.log(valor1 += 2); //(Adición) Esto es igual a valor1 = valor1 + 2
console.log(valor1 -= 2); //(Resta) Esto es igual a valor1 = valor1 - 2
console.log(valor1 *= 2); //(Multiplicación) Esto es igual a valor1 = valor1 * 2
console.log(valor1 /= 2); //(División) Esto es igual a valor1 = valor1 / 2
console.log(valor1 %= 2); //(Residuo|Resto) Esto es igual a valor1 = valor1 % 2
console.log(valor1 **= 2); //(Exponenciación) Esto es igual a valor1 = valor1 ** 2

//OPERADORES DE COMPARACIÓN (Los más usados) = Compara sus operandos y devuelve un valor lógico 
// Si la comparación es verdadera, devuelve (true) y si es falsa devuelve (false)

let numero1 = 1;
let numero2 = 2;
let numero3 = "1";

//¿ Es igual en cuanto a número ?
console.log(numero1==numero2); //False
console.log(numero1==numero3); //True

//¿ Es igual en cuanto a número y tipo ?
console.log(numero1===numero2); //False
console.log(numero1===numero3); //False //Son el mismo número pero, el tipo, numero1 es integer y numero3 string

//¿ Es distinto en cuanto a número ?
console.log(numero1!=numero2); //True
console.log(numero1!=numero3); //False

//¿ Es distinto en cuanto a número y tipo ?
console.log(numero1!==numero2); //True
console.log(numero1!==numero3); //True

//¿ Es Mayor o Mayor o igual ?
console.log(numero1>numero2); //False
console.log(numero1>=numero3); //False

//¿ Es Menor o Menor o igual ?
console.log(numero1<numero2); //True
console.log(numero1<=numero3); //True

// OPERADORES ARITMÉTICOS (Los más usados):

let numero4 = 4;
let numero5 = 2;

//+ (Suma) Suma dos números
let suma = numero4+numero5;
console.log(suma);

//- (Resta) Resta dos números
let resta = numero4-numero5;
console.log(resta);

//++ (Incremento) Suma 1 al valor de la variable
let incremento = numero4++; // incremento ahora será 5
console.log(incremento);

//-- (Decremento) Resta 1 al valor de la variable
let decremento = numero4--; // decremento ahora será 3
console.log(decremento);

//% (Residuo | Resto) Devuelve el resto de la división de dos operandos
let resto = numero4%2; // (el resto de dividir 4 entre 2 es 0)
console.log(resto);

//** (Exponenciación) Devuelve la base elevada a la potencia del exponente
let exponenciacion = numero4 ** 2; // (4 elevado a la potencia de 2 es 16)
console.log(exponenciacion);

//OPERADORES LÓGICOS (Los más usados):

/* 
&& (AND Lógico)
|| (OR Lógico)
! (NOT Lógico)
Los operadores lógicos funcionan con valores booleanos, pero también con expresiones que devuelven valores booleanos 
a partir de comparaciones o cualquier tipo de expresión que sea evaluada con true false
*/

let numero6 = 6
let numero7 = 4

//&& (AND Lógico)
let resultado1 = (numero6 > numero7) && (numero6>0);
console.log(resultado1); //Equivale a true ya que la variable numero 6 es mayor a la variable numero 7 y la variable numero6 es mayor a 0

//|| (OR Lógico)
let resultado2 = (numero6 < numero7) || (numero6==6);
console.log(resultado2); //La variable numero 6 no es menor a la variable numero 7 (esto es false), pero como la variable numero6 es igual a 6, entonces como se cumple una de las dos, es true

//! (NOT Lógico)
let resultado3 = !(numero7>10)
console.log(resultado3); //La variable resultado3 sería false, pero como le hemos puesto el ! al principio la convertimos a true

//OPERADORES DE CADENA (Los más usados):
/* 
Tenemos + y tenemos `${}`
*/

let saludo="Hola, mi nombre es: ";
let nombre="Pedro";

let juntar1=saludo+nombre; //Concatenamos una variable con otra con un +
let juntar2=`Hola, mi nombre es: ${nombre}`; //Concatenamos una variable un texto con los caracteres especiales ` y la variable dentro de ${}

console.log(juntar1);
console.log(juntar2);

//OPERADORES CONDICIONALES:

//Condicional: Se usa para evaluar si una condición es verdadera o falsa y ejecutar diferentes bloques de código según el resultado.
let numeroCondicional=2;

if(numeroCondicional>10){
    console.log("El numero es mayor a 10"); 
}else{
    console.log("El numero es menor a 10");
}

//Bucle for: Se usa cuando se conoce de antemano cuántas veces se debe ejecutar el bloque de código, normalmente para iterar sobre números o arrays.
let contarHastaCinco=5;
for(let i=0;i<=contarHastaCinco;i++){
    console.log(i);
} 

//Bucle foreach: Se usa para iterar sobre los elementos de un array y ejecutar una función para cada uno de ellos.
let animales=["Perro","Gato","Oso"];
animales.forEach(animal=>console.log(animal));

//Bucle for of: Se usa para iterar sobre los valores de un objeto iterable (como arrays, cadenas, etc).
for(animal of animales){
    console.log(animal);
}

//Bucle while: Ejecuta el bloque de código mientras que la condición sea verdadera. 
// Es útil cuando no se sabe cuántas veces se debe iterar de antemano, tenemos que ir modificando la variable, si no se quedaría en un bucle infinito.
let contarHastaDiez=0;
while(contarHastaDiez<=10){
    console.log(contarHastaDiez);
    contarHastaDiez++;
}

//Bucle do While: Ejecuta el bloque de código al menos una vez antes de evaluar la condición (aunque la condición sea falsa), y continuará ejecutando mientras la condición sea verdadera.
let i=0;
do {
    console.log(i);
    i++;
} while (i>5);

//Switch: Se usa para evaluar varias opciones posibles para una sola variable, de manera más limpia y eficiente que usando múltiples if...else.
let operacion="sumar";
switch (operacion) {
    case "sumar":
        console.log("Vas a sumar");
        break;
    case "restar":
        console.log("Vas a restar");
        break;
    case "multiplicar":
        console.log("Vas a multiplicar");
        break;
    case "dividir":
        console.log("Vas a dividir");
        break;
    default:
        console.log("Esa operación no está disponible");
        break;
}

//OPERADOR CONDICIONAL(TERNARIO):

let edad=18;
let comprobarEdad=edad>=18?"Es mayor de edad":"Es menor de edad";  

console.log(comprobarEdad);

/* 
Si la edad es mayor o igual a 18,
la variable comprobarEdad será igual a "Es mayor de edad" ,
si es menor a 18 la variable comprobarEdad será igual a "Es menor de edad"   
*/

/*
    EJERCICIO EXTRA
    Crea un programa que imprima por consola todos los números comprendidos
    entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
*/

for(let i=10;i<=55;i++){ //Le digo que empiece con el número 10 y que cuente hasta el número 55 incluido
    if(i%2==0 && !(i%3==0) && i!=16){ //Aquí compruebo primero que sean pares, que no sea multiplo de 3 y que no sea = al numero 16
        console.log(i);
    }
}