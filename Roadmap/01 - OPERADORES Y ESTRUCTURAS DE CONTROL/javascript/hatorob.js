const { error } = require("console");

//! Operadores aritmeticos
let number = 1;

let sum = 2 + 2;
console.log(`sum - ${sum}`);
let res = 5 - 2;
console.log(`res - ${res}`);
let mult = 5 * 2;
console.log(`mult - ${mult}`);
let div = 9 / 2;
console.log(`div - ${div}`);
let exp = 2 ** 2;
console.log(`exp - ${exp}`);
let resid = 21 % 2;
console.log(`resid - ${resid}`);
let incrementOptionOne = number++;
console.log(`increment - ${incrementOptionOne}`);
let incrementOptionTwo = ++number;
console.log(`increment - ${incrementOptionTwo}`);
let decrementOptionOne = number--;
console.log(`decrement - ${decrementOptionOne}`);
let decrementOptionTwo = --number;
console.log(`decrement - ${decrementOptionTwo}`);

//! Operadores lógicos

//!AND
if( true && true ) console.log("si cumple ambas condiciones entro aquí");
//!OR
if( false || true ) console.log("si cumple al menos una condicion entro aquí");
//! Negation
if(!false) console.log("niego un boolean, si es falso estoy entrando");


//! comparación
if( 20 < 30) console.log(`Si el num1 es menor a num2`);
if( 20 <= 30) console.log(`Si el num1 es menor o igual a num2`);
if( 20 > 10) console.log(`Si el num1 es mayor a num2`);
if( 10 >= 10) console.log(`Si el num1 es mayor o igual a num2`);
if( 10 == "10") console.log(`Si el num1 es igual a num2`);
if( 10 === 10) console.log(`Si el num1 es identico a num2`);
if( "20" != 10) console.log(`Si el num1 es diferent a num2`);
if( "20" !== 20) console.log(`Si el num1 es diferente estricto a num2`);

//! asignacion
//! suma
let asig1 = 1;
asig1 += 1
console.log(asig1);
//! resta
let asig2 = 1;
asig2 -= 1
console.log(asig2);
//! multiplicacion
let asig3 = 1;
asig3 *= 2
console.log(asig3);
//! division
let asig4 = 8;
asig4 /= 2
console.log(asig4);
//! residuo
let asig5 = 8;
asig5 %= 2
console.log(asig5);
//! Concatena string
let asig6 = "hola";
asig6 += " Mundo"
console.log(asig6);


//! Estrcutura de control
//! if
if(2 == "2") {
    // if con llavers
}
//! if de una sola linea
if(2 == "2") console.log("entro al if de una sola linea");
//! if else
if(2 > 10 ) {
    close.log("entro al if 2");
} else {
    console.log("entro al else");
}

//! if, if else, else

if(2 > 10) {
    //! si cumple entro aqui
} else if(4 == 4) {
    console.log("entro al else if");
} else if( 6 == 7 ) {
    //! otro else if
} else {
    //! else
}

//! if ternario
("spiderman" == "spiderman") ? console.log("user active") : console.log("user inactive");;

//! switch
let search = "hulk";
switch (search) {
    case "hulk":
        console.log(`welcome hero ${search}`);
        break;
    case "spiderman":
        console.log(`welcome hero ${search}`);
    default:
        console.log(`welcome to hero`);
}


//! iterativas

//? for
for(let i = 0; i < 4; i++) {
    console.log(`recorriendo un for ${i}`);
}

//! while
let j = 0;
while( j <= 2 ) {
    console.log("recorriendo un while, hasta que se cumpla una condicion"); 
    j++;   
}
j = 0;
do {
    console.log("recorriendo un do while, se ejecuta al menos una primera vez");
    j++;
} while(j < 0)

//! excepciones
//* Dejo comentando throw new Error para que no saque el código
let brand = "nike";
try {
    if( brand != "adidas" ) //throw new Error(`the brand ${brand} is not exists`)
    //! si pasa el if sigo mi lógica
    console.log(`the brand ${brand} is ok`);
} catch (error) {
    console.log(error);
}



//! EJERCICIO OPCIONAL
/*
* Crea un programa que imprima por consola todos los números comprendidos
* entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
*/

let start = 10;
let limit = 55;
for( let i = start; i <= limit; i++ ){
    if( (i % 2 == 0) && (i != 16) && (i % 3 != 0) ) console.log(i);
}







