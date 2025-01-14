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

//------------------------------- aritmeticos --------------------------------------
///////////////////////////////////////////////////////////
//suma
console.log("la suma de 15 + 10 es :"+(15 + 10));

//resta 
console.log("la resta de 15 - 10 es :"+(15 - 10));

//multiplicacion 
console.log("la multiplicacion de 15 * 10 es :"+(15 * 10));

//division
console.log("la division de 15 / 10 es :"+(15 / 10));

//modulo o residuo de la division
console.log("el modulo de 15 % 10 es :"+(15 % 10));

//Exponenciacion 
console.log("la Exponenciacion de 15 ** 10 es :"+(2 ** 4));

//incremento 

for (let i = 0 ; i < 4 ; i++ ){
    console.log(i)
};

//decremento 

for (let i = 5 ; i > 0  ; i-- ){
    console.log(i)
};

//------------------------------operadores de compracion---------------------------------

//igual 

let igual = 10 

if (igual == 10){
console.log("el numero dado es igual a :" + igual)
};

//estrictamente igual

let estrictamenteIgual = 10 

if (estrictamenteIgual === 10){
console.log("el numero dado es igual a :" + estrictamenteIgual)
};

//No es igual 

let noEsIgual = 5;

if (noEsIgual != 10){
console.log("el numero dado no es igual " );
};

//estrictamenteNoEsIgual

let estrictamenteNoEsIgual = 5;

if (estrictamenteNoEsIgual !== 10){
console.log("el numero dado no es igual " );
};

//mayor que 

let a = 20;
let b = 70;

console.log(a > b);

//menor que 

console.log(a < b);

//mayor o igual 
console.log(a >= b);

//menor o igual 
console.log(a <= b);

//--------------------------operadores logicos----------------------------------------- 

//and 

let numero = 20;
let numero1 = 30;
let numero2 = 30;


console.log((numero > numero1) && (numero < numero2));//false

//(OR)

console.log((numero > numero1) || (numero < numero2));//true 

//negacion logica !

let esHombre = true;

if (!esHombre){
    console.log("el ususario es hombre");
}else{
    console.log("el usuario es mujer");//imprimira el usuario es mujer ya que la negacion cambia un valor booleano a un valor contrario
};

//-----------------------operadores de asignacion---------------------------------

//asignacion simple

let asignacionSimple = 20;

//asignacion adicion

asignacionSimple += 5;

console.log(asignacionSimple)//asignacionSimple es 25 (20 + 5)

//de sustraccion

let sustracion = 10;

sustracion -= 4;

console.log(sustracion)//asignacionSimple es 25 (20 + 5)

//multiplicacion

let multiplicacion = 10;

multiplicacion *= 4;

console.log(multiplicacion)//asignacionSimple es 25 (20 + 5)


//asignacion de division 

let division = 10;

division /= 4;

console.log(division)//asignacionSimple es 25 (20 + 5)

//asignacion de modulo 

let modulo = 10;

modulo %= 4;

console.log(modulo)//asignacionSimple es 25 (20 + 5)

//asignacion de exponenciacion

let exponenciacion = 10;

exponenciacion **= 4;

console.log(exponenciacion)//asignacionSimple es 25 (20 + 5)


//asignacion de  desplazamiento a la izquierda 

let x = 5;

x <<= 1;

console.log(x)

//asignacion de  desplazamiento a la derecha

let y = 5;

y >>= 1;

console.log(y);

//asignacion de  desplazamiento a la derecha con relleno cero 


let y1 = 5;

y1 >>>= 1;

console.log(y1);

//asignacion and a nivel de bits


let y2 = 5;

y2 &= 1;

console.log(y2);

//asignacion OR a nivel de bits


let y3 = 5;

y3 |= 6;

console.log(y3);

//asignacion XOR a nivel de bits


let y4 = 5;

y4 ^= 6;

console.log(y4);

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
nombre: "juan carlos",
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

//------------------------------operadores de bits---------------------------------------------------------------


let a2 = 5;  // 0101 en binario
let b2 = 3;  // 0011 en binario

let andBits = a2 & b2;  // AND de bits (0001 -> 1)
let orBits = a2 | b2;   // OR de bits (0111 -> 7)
let xorBits = a2 ^ b2;  // XOR de bits (0110 -> 6)
let notBits = ~a2;     // NOT de bits (complemento de 2, 1010 -> -6)
let desplazaIzquierda = a2 << 1; // Desplazamiento a2 la izquierda (1010 -> 10)
let desplazaDerecha = a2 >> 1;   // Desplazamiento a la derecha (0010 -> 2)



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

//gracias por su atencion
