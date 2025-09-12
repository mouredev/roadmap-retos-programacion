
//Operadores aritmeticos

console.log("La suma de 10 + 5 es: ", 10 + 5);


console.log("La resta de 10 - 5 es: ", 10 - 5);


console.log("La multip de 10 * 5 es: " + 10 * 5);


console.log("La div de 10 entre 5 es: " + 10 / 5);

let mod = 10 % 3;
console.log(`El residuo de 10 % 3 es: ${mod}`);

console.log("El exponente de 2**2 es: ", 2 ** 2);

console.log("<br>");


//Unarios

let inc = 5;
console.log("Operador unario de incremento devolviendo 5 + 1", ++inc);
console.log("Operador unario de incremento que devuelve el valor de inc y luego suma", inc++);
console.log(`${inc}`);

let dec = 5;
console.log("Operador unario de decremento devolviendo 5 -1 ", --dec);
console.log("Operador unario de decremento que devuelve el valor de dec y luego resta", dec--);
console.log(`${dec}`);

let unNeg = 4
console.log("la negación unaria negativa es: ", -unNeg);
console.log(`el positivo unario es: ${+unNeg}`);
console.log(+"3");
console.log(+true);

console.log("<br>");


//Operadores comparación

console.log("Es 2 = a 10 ? ", 2 == 10);

console.log("Es 2 = a 2 ? ", 2 == 2);

console.log("Es 2 diferente de 10 ? ", 2 != 10);

console.log("Es 2 < a 10 ? ", 2 < 10);

console.log("Es 2 > a 10 ? ", 2 > 10);

console.log("Es 2 < o = a 10 ? ", 2 <= 10);

console.log("Es 2 < o = a 10 ? ", 2 >= 10);

//con objetos === !== se comportan como en Python
console.log("Es 2 diferente de `2` ? ", 2 === "2");

console.log("Es 2 diferente de `2` ? ", 2 !== "2");

console.log("<br>");


//Operadores logicos

// && and
console.log("Es 2 + 2 = 4 y(&&) 2 - 2 = a 0? ", (2 + 2 == 4) && (2 - 2 == 0));

// || or
console.log("Es 2 + 2 = 4 o(||) 2 - 2 = a 0? ", (2 + 2 == 4) || (2 - 2 == 2)); 
//una cond es true = true

console.log("Es 2 + 2 = 4 y(&&) 2 - 2 = a 0? ", (2 + 2 == 2) || (2 - 2 == 2));

// Not
console.log("No es 2 + 2 = 3? ", !(2 + 2 == 3)); //true

console.log("<br>");


//Operadores de asignación

let myVar = 20;
console.log(myVar);

console.log(myVar += 1);

console.log(myVar -= 1);

console.log(myVar *= 2);

console.log(myVar /= 2);

console.log(myVar %= 3);

console.log(myVar **= 3);

console.log("<br>");


//Operadores relacionales (pertenencia)

//con arrays
console.log([1,2,3] .includes (3));
console.log([1,2,3] .includes (4));

//con strings
console.log("abc" .includes ("a"));

//con objetos
let obj = {a : 1, b : 2};
console.log("a" in obj);
console.log("c" in obj);

console.log("<br>");


//Operadores de bits
console.log(5 & 3); // 0101 & 0011 = 0001  (1)
console.log(5 | 3);  //0101 | 0011 = 0111  (7)
console.log(5 ^ 3);  //0101 ^ 0011 = 0110  (6) 
console.log(~5);    // -0101 = 1010 = -6
console.log(5 << 1); // 0101 << 1 = 1010 = 10
console.log(5 >> 1); // 0101 >> 1 = 0010 = 2
console.log(-5 >>> 1);

console.log("<br>");


//Operador ternario

let age = 18;
var status = age >= 18 ? "adulto" : "menor";

console.log(status);


console.log("<br>");
console.log("<br>");
console.log("<br>");


//ESTRUCTURAS DE CONTROL

//Condicionales

let edad = 18;

if(edad > 18) {
  console.log("Eres mayor de edad");
} else if (edad = 18) {
  console.log("Tienes justo 18 años");
} else {
  console.log("Eres menor de edad")
}


let food = "meat";
let menu;

switch (food) {
  case "meat":
    menu = "La carne está en su punto";
    break;
  case "fish":
    menu = "El pescado es de hoy";
    break;
  case "fruit":
    menu = "La fruta es de temporada";
    break;
  default:
    menu = "Lo siento, no tenemos";
    
}
console.log(menu);


let total = 0;
while (total <= 10) {
  console.log(total);
  total++;
}


let numero = 10;
do {
  console.log(`tenemos un ${numero}`);
  numero--;
} while (numero > 0);


for(let num = 0; num <= 7; num++) {
  console.log(`Hola ${num}`);
}


myArra = [1, 2, 3, 4, 5];
for(val of myArra) {
  console.log(val);
}


let frase = "Hello Mouredev!";
for(let l in frase) {
  console.log(l);
}

let frase2 = "Hello Mouredev!";
for(let l in frase2) {
  console.log(frase2[l]);
}


//Dificultad EXTRA

/*
for(let number = 10; number <= 55; number ++) {
  if(number == 16) {
    continue;
  }else if(number % 3 == 0) {
    continue;
  }else if(number % 2 != 0) {
    continue;
  }
  console.log(`${number}`);
}
console.log("55");
*/

for (let number = 10; number <= 55; number++) {
  if (((number % 2 == 0 && number != 16) && number % 3 != 0) || number == 55) {
    console.log(`${number}`);
  }
}
















