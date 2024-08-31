// OPERADORES EN JAVASCRIPT //

// OPERADOR DE ASIGNACION ( = )

let x = 1;
let y = 2;
let a = y;
let b = x;
console.log(x);
console.log(y);
console.log(a);
console.log(b);
// Asginacion de adicion ( += )

x += y;
y += a;
console.log(x);
console.log(y);

// Asginacion resta ( -= )

x -= y;
a -= b;
console.log(x);
console.log(a);


// Asginacion de multiplicacion ( *= )

x *= x;
b *= a;
console.log(x);
console.log(b);

// Asginacion de division ( /= )

let numDiv1 = 15;
let numDiv2 = 3;
numDiv1 /= numDiv2;

console.log(numDiv1);
// Asignacion Residuo ( %= ) 
let numResiduo = 20;
let numeResiduo2 = 2;
numResiduo %= numeResiduo2;

console.log(numResiduo);

// Asignacion exponenciacion 

let numExpo = 2;
let numExpo2 = 10;
numExpo2 **= numExpo;

console.log(numExpo2);

// OPERADORES DE COMPARACION 

// Operador de igualdad ( == ) 
let numeroComparacion = 5;
let numeroComparacion2 = 7;

let comparacionResultado = numeroComparacion == numeroComparacion2;
console.log(comparacionResultado); //False

// operador de desigualdad ( != )

let numDesigual1 = 15;
let numDesigual2 = 20;

let desigual = numDesigual1 != numDesigual2;
console.log(desigual); // True 

// Estrictamente igual ( === )

let strinEstricto = "Hola Mundo";
let strinEstricto2 = "hola mundo";

let compararEstricto = strinEstricto === strinEstricto2;
console.log(compararEstricto); // False 

// Desigualdad estricta ( !== )

let desEstricta = 5;
let desEstricta2 = "5";

let comDesigEstric = desEstricta !== desEstricta2;
console.log(comDesigEstric);

// Mayor igual ( > )

let numMenor = 5;
let numMayor = 20;

let respMayor = numMayor > numMenor;
console.log(respMayor);

// Menor igual ( < )

let resMenor = numMayor < numMenor;
console.log(resMenor);

// menor igual ( <= )

let menorIgual = numMayor <= numMenor;
console.log(menorIgual);

// Mayor igual ( >= )

let mayorIgual = numMayor >= numMenor;
console.log(mayorIgual);

// OPERADORS ARITMETICOS  SUMA (+) RESTA ( - ) MULTIPLICACION (*) DIVISION (/)

let num1 = 5;
let num2 = 10;

// Suma (+)

let suma = num1 + num2;
console.log(suma);
let resta = num1 - num2;
console.log(resta);
let mult = num1 * num2;
console.log(mult);
let div = num1 / num2;
console.log(div);

// OPERADORES UNARIOS INCREMENTO, DECREMENTO

let numUnario = 15;
numUnario ++;
console.log(numUnario);
numUnario --;
console.log(numUnario);

// OPERADOR UNARIO NEGATIVO
let unarioNeg = 10;
console.log(-unarioNeg);

// UNARIO POSITIVO

let unarioPost = "10";
console.log(+unarioPost);

// POTENCIA UNARIA

let numPot = 15;
let potenciaUnaria = numPot**2;
console.log(potenciaUnaria);


// OPERADORES LOGICOS  AND OR NOT

let numComparacion1 = 10;
let numComparacion2 = 25;
let numComparacion3 = 18;

let and = (numComparacion1 == numComparacion2 && numComparacion3 > numComparacion1);
let or = (numComparacion1 == numComparacion2 || numComparacion3 > numComparacion1);
let not = !or;

console.log(and);
console.log(or);
console.log(not);


// OPERADOR CONCATENACION 

let string1 = "Hola me llamo ";
let string2 = "Juan Fernandez";

console.log(string1 + string2);


// OPERADOR CONDICIONAL TERNARIO

// condition ? val1 : val2

let tern = 50;

let resTern = tern > 18 ? "Es mayor de edad": "Es menor de edad";
console.log(resTern);

//OPERADOR TYPEOF

let cadena = "Hola";
let numero = 1215;
let booleano =  4 < 6;

console.log(typeof(cadena));
console.log(typeof(numero));
console.log(typeof(booleano));

// Operadores logicos BIT a BIT

let bitAnd = 20 & 15;
let bitOR = 25 | 20;
let bitXor = 10 ^ 5;
let bitNot = ~ 15;
console.log(bitAnd);
console.log(bitOR);
console.log(bitXor);
console.log(bitNot);

// Operadores de desplazamiento de BITS

let desplazamientoIzq = 20 << 2;
let desplazamientoDer = 25 >> 5;
console.log(desplazamientoIzq);
console.log(desplazamientoDer);

// Operador In

let array = ["Uva", "Naranja", "Manzana", "Pera"];
let validar = 1 in array
console.log(validar); // Valida si el indice esta en ese array


// Estructuras de control
let numer1If = 2;
let numer2If = 5;
if (numer1If > numer2If) {  // Estructura de control If
    console.log("Si es mayor");
}else{
    console.log("Es menor");
}

// Condicionales if - else - else if

numer1If = 10;
numer2If = 10;

if (numer1If < numer2If) 
{
    console.log("Es menor");

}else if(numer1If > numer2If){
    console.log("Es mayor");
} else {
    console.log("Es igual");
}


// Iteradores 
// while
let iterador = 0;
let contador = 0;
while (iterador < 15) {
    contador += 2;
    iterador++;
    console.log(contador);
}

// For

contador = 0;

for (let i = 0; i < 15; i++) {
    contador += 3;
    console.log(contador);
    
};

// Foreach
let arrayFrutas = ["Manzana","Pera","Naranja","Uva", "Kiwi","Mandarina","Limon"];
contador = 0;
arrayFrutas.forEach(fruta => {
    contador ++
    console.log(`${contador} : ${fruta}`);
});

// For in
for (const indexFruta in arrayFrutas) {
    console.log(indexFruta);
}


// Programa para imprimir por consola los numero del 10 al 55 (incluidos)
// pares, y que no sean nu el 16 ni multiplos de 3

let number = 10;

for (let i = 10; i <= 55; i++) {
    
    if (((number % 3) === 0) || (number === 16)) {
        number++
    }else
    {
        console.log(number);
        number++;
    }
}
