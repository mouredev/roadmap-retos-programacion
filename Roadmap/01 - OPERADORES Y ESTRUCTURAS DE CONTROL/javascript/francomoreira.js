// ejemplos con los operadores

/*
Operadores Aritmeticos
Operadores Logicos
Operadores de comparacion
Operador de asignacion abreviada
 */
let a = 5;
let b = 10;

// Operadores Aritmeticos
let suma = a + b;
let resta = a - b;
let multiplicacion = a * b;
let division = a / b;
let resto = a % b;
let exponenciacion = a ** b;

// Operadores Logicos
let operadorAND = a && b;
let operadorOR = a || b;
let operadorNOT = !a;

//Operador de comparacion
let mayorQue = a > b;
let menorQue = a < b;
let mayorOIgualQue = a >= b;
let menorOIgualQue = a <= b;

// Operador de igualdad 
let igualdadNoEstricta = a == b; // se evalua solo el valor.
let igualdadEstricta = a === b; // se evalua valor y tipo de dato

// Operador de asignacion
let asignando = 'este valor' // el operador es el "="
a += 5; 
a -= 5;
a *= 5;
a /= 5;
a %= 5;
a **= 5;

/* estructuras de control
    |
    |_ Condicionales
    |   |_ If / Else
    |   |_ Switch
    |
    |_ Ciclos
        |_ For
        |_ While
        |_ Do... while
*/

// If / Else
let edad = 20;

if (edad >= 18) {
	console.log('acceso confirmado');
} else {
	console.log('acceso denegado');
}

// Switch

let semaforo = 'verde';

switch (semaforo) {
    case 'rojo':
      console.log('Detente por favor!');
      break;
    case 'amarillo':
      console.log('el semaforo esta en amarillo')
      break;
    case 'verde':
      console.log('el semaforo esta en verde puedes avanzar tranca!')
      break;
    default:
      console.log("¡No entiendo! :(")
}

// for
for(i=0;i<10;i++){
    console.log(i)
}

// while
a = 1;
while (a <= 10) {
  console.log(a++);
}

// do...while
a = 1;
do  {
    console.log(a++); 
} while (a <= 10)


// dificultad extra

function programa(a,b){
    for (var i = a; i <= b; i++) {
      if (i % 2 === 0) {
          if (i === 16 || i % 3 === 0) {
            continue;
          }
          else {
              console.log(i);
          }
      }
    }
  }
  
  programa(10,55);