/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */
/////////--- aritmeticos ---//////////

//suma 
console.log("la suma de 15 + 10 es: " + (15 + 10));

//resta 
console.log('la resta de 10-10 es: ' + (9 - 1));

//multiplacion 
console.log('la multiplicacion de 5*10 es: ' + (5 * 10));

//division
console.log('la division de 10/2 es: ' + (10 / 2));

//residuo de la division
console.log('el residuo de la division de 10/3 es: ' + (10 % 3));

//exponenciacion 
console.log('la exponenciacion de 2**3 es: ' + (2 ** 3));

//incremento
for (let i = 2; i < 6; i++) {
    console.log('el incremento de 2 es: ' + i);
};

//decremento
for (let i = 11; i > 7; i--) {
    console.log('el decremento de 11 es: ' + i);
};

/////////--- comparacion ---//////////

//igual 
console.log('10 es igual a 10: ' + (10 == 10));

//estrictamente igual
console.log('10 es estrictamente igual a 10: ' + (10 === 10));

//diferente 
console.log('10 es diferente a 11: ' + (10 != 11));

//estrictamente diferente
console.log('10 es estrictamente diferente a 11: ' + (10 !== 11));

//mayor que 
let c = 15;
let d = 8;
console.log('c es mayor que d: ' + (15 > 8));

//menor que 
console.log('c es menor que d: ' + (15 < 8));

//mayor o igual que 
console.log('c es mayor o igual que d: ' + (15 >= 8));

//menor o igual que 
console.log('c es menor o igual que d: ' + (15 <= 8));

/////////--- operadores logicos ---//////////

let numberA = 10;
let numberB = 20;
let numberC = 30;

console.log((numberA > numberB) && (numberA < numberC));

//or
console.log((numberA > numberB) || (numberA < numberC));

//negacion logica   

let esPerro = true;

if (!esPerro){
    console.log('el animal es un perro');
}else{
    console.log('el animal no es un perro'); // esto se imprimira ya que la negacion cambia un valor booleano a un valor contrario
};

/////////--- operadores de asignacion ---//////////

//asignacion simple
let number1 = 20;

//asignacion adicion
number1 += 3

console.log(number1)//number1 es 23 (20 + 3)

//de sustraccion
let number2 = 40;

number2 -= 4;

console.log(number2)//number2 es 36 (40 - 4)

//  asignacion multiplicacion
let number3 = 10;

number3 *= 2;

console.log(number3)//number3 es 20 (10 * 2)

//asignacion division
let number4 = 80;

number4 /= 4;

console.log(number4)//number4 es 20 (80 / 4)

//asignacion de modulo
let number5 = 50;

number5 %= 7;

console.log(number5)//number5 es 1 (50 % 7)

//asignacion de exponenciacion
let number6 = 2;

number6 **= 3;

console.log(number6)//number6 es 8 (2 ** 3)

//asignacion de concatenacion
let texto = "Hola";
texto += " Mundo";
console.log(texto)//texto es "Hola Mundo"

//---------------------operadores de identidad-----------------------------


//igualdad estricta

let igual1 = 15;
let igual2 = 13;

if (igual1 === igual2){
    console.log("son iguales");
}else{
    console.log("no es igual");//no son iguales 
};

//desigualdad estricta

let desigualdad = 15;
let desigualdad1 = 13;

if (igual1 !== igual2){
    console.log("son iguales");//son iguales 
}else{
    console.log("no es igual");
};

//-----------------------------operadores de pertenencia-----------------------------

//in
// se usa para verificar una propiedad en un array u objeto 

const persona = {
nombre: "Samuel",
edad:56
};

if (`nombre` in persona){
    console.log("la propiedad nombre si existe")
}else{
    console.log("la propiedad nombre no existe")
};

//intanceof 

//se usa para verificar si un objeto es una instancia de una clase o contructor especifico 

let fecha = new Date();
let esFecha = fecha instanceof  Date;

console.log(esFecha);

//---------- --------------------------dificultad--------------------------------------------------

/* DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */


for (let i = 10; i < 56 ; i++){//usamos  un  ciclo for creamos la variable indice igualando a 10, si i e menor a 56 , i aumentara hasta 55
    if(i === 16){//si i es igual a 16
        continue;//se salta ese numero 
    }if(i % 3 === 0){//si i es multiplo de 3 
        continue;//se salta el numero
    }
    console.log(i)
};