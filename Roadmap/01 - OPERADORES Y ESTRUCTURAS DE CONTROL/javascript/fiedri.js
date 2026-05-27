// Tipos de operadores
/*
=========================
 operadores de asignacion
=========================
*/
let x = 10// (=) asignacion
x += 10 //20, (+=) asignacion de adicion
x -= 5 //15, (-=) asignacion de resta
x *= 2 //30, (*=) asignacion multplicacion
x /= 2 //15, (/=) asignacion de division
x **= 2//225, (**=) asignacion de exponenciacion
x %= 2//1, (%=) asignacion de resto


x <<= 6//64, desplazamiento a la izquierda
// x <<= n  es lo mismo que  x = x << n
// 1. Convierte x a binario (32 bits).
// 2. Mueve los bits 'n' posiciones a la izquierda.
// 3. Rellena los huecos de la derecha con CEROS.
// 4. Equivale a multiplicar x por 2 elevado a n.
console.log(x)

x >>= 6// desplazamiento a la derecha con signo
// 2. mueve 'n' posiciones a la derecha
// 3. Si el numero es positivo rellena con 0, si es negativo con 1
// Equivale a dividir x entre 2^n y redondea hacia abajo
console.log(x)

// Asinacion bit a bit
x &= 10//(AND)
// 1 &= 1, es igual a 1
//Si en la misma posición ambos tienen un 1 el resultado es 1 Si no es 0
x  ^= 10 //(XOR)
// devuelve 1 si los bits en esa posicion son distintos
x |= 10 // (OR)
// devuelve 1 si x o y (o ambos) son 1
console.log(x)

// asignacion logica
// &&= (AND), Solo asigna el valor de la derecha si el de la izquierda ya es verdadero
let usuario = true
usuario &&= "Juan"

let invitado = false
invitado &&= "Pedro"
console.log(usuario, invitado)// "Juan" false

// ||= (OR), asigna el valor de la derecha si el de la izquierda es falso
let nickname = ""; 
nickname ||= "Anónimo"; 
console.log(nickname);// "Anonimo"

let puntos = 10;
puntos ||= 100;
console.log(puntos);// 10

// ??= (anulacion) asigna si el valor de la izquierda es estrictamente null o undefined
let nombre;
nombre ??= "Sin nombre";
console.log(nombre); // "Sin nombre"


/*
=========================
 operadores de comparacion
=========================
*/
console.log(10 == "10");// true (igualdad debil)
console.log(10 === "10");// false (igualdad fuerte, tambien compara tipo)
console.log(10 != 5)// true (desigualdad)
console.log(10 !== "10"); // true (Desigualdad fuerte)
console.log(10 > 5, 10 < 20, 10 >= 10, 10 <= 10);
/*
=========================
 operadores aritmeticos
=========================
*/
console.log(10+5) // suma
console.log(10-5)// resta
console.log(10*5)// multiplicacion
console.log(10/2)// division
console.log(10 % 3)// Módulo
console.log(2**3)// potencia
let i=1; i++; i--; //incremento y decremento 

/*
=========================
 operadores logicos bit a bit
=========================
*/
// AND (&): Devuelve 1 si ambos bits son 1.
console.log(5 & 1); // 0101 & 0001 = 0001 (1)

// OR (|): Devuelve 1 si al menos uno de los bits es 1.
console.log(5 | 1); // 0101 | 0001 = 0101 (5)

// XOR (^): Devuelve 1 si los bits son diferentes.
console.log(5 ^ 1); // 0101 ^ 0001 = 0100 (4)

// NOT (~): Invierte todos los bits (operador unario).
console.log(~5);    // ~0101 = ...1010 (-6 en complemento a dos)


/*
=========================
operadores de desplazamiento bit a bit
=========================
*/
// Desplazamiento a la izquierda (<<): Mueve bits a la izquierda y rellena con ceros.
console.log(5 << 1); // 0101 -> 1010 (10)

// Desplazamiento a la derecha con signo (>>): Mueve bits a la derecha manteniendo el signo.
console.log(5 >> 1); // 0101 -> 0010 (2)

// Desplazamiento a la derecha sin signo (>>>): Rellena con ceros sin importar el signo.
console.log(-5 >>> 1); // Un número muy grande (32-bit unsigned)

/*
=========================
 operadores logicos
=========================
*/
console.log(true && false);// AND
console.log(true || false);// OR
console.log(!true);// NOT
/*
=========================
 operadores de cadena
=========================
*/
console.log("Hola " + "JavaScript");// Concatenación
/*
=========================
 operadores de ternario
=========================
*/
let resultado = (10 > 5) ? "Es mayor" : "Es menor";
console.log(resultado);
/*
=========================
 operadores de relacionales
=========================
*/
console.log("name" in {name: "Friedrich"}); // in: comprueba propiedad en objeto
console.log([1, 2] instanceof Array);      // instanceof: comprueba tipo de objeto



/*
=====================
Estructura de control
=====================
*/
//condicionales
if(true){} else if(false){} else{}
switch(1){case 1: break; default: break;}

// iterativas
while(false){}
do{} while(false)
for(let i = 1; i!=1; i++){}
for (let item of [1,2]) {} // for ... of
for (let key in {a:1}) {} // for in

// Excepciones (Manejo de errores)
try { throw new Error("Error de sistema"); } 
catch (e) { console.log(e.message); } 
finally { console.log("Finalizado"); }

//DIFICULTAD EXTRA
console.log('DIFICULTAD EXTRA')
for(let i = 10; i<=55; i+=2){
    if(i != 16 && i%3 !=0){
        console.log(i)
    }
}