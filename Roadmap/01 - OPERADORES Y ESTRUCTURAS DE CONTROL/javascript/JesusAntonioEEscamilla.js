/** #01 - JavaScript ->Jesus Antonio Escamilla */
/**
 * -----TIPOS DE OPERADORES-----
 * Dentro operadores empezaremos con
 * Aritméticos
 * Lógicos
 * Asignación
 * Comparación
 */

/**
 * ---ARITMÉTICOS---
 * Dentro de estos hay están las operaciones básicas
 * de las cuales derivan la suma, resta, division o multiplicación.
*/
    console.log(2 + 3); // La suma el resultado es 5
    console.log(5 - 3); // La resta en la cual el resultado es 2
    console.log(16 / 4); // La division en donde el resultado es 4
    console.log(5 * 7); // La multiplicación por el cual el resultado es 35


/**
 * ---LÓGICOS---
 * Los cuales dan solo una respuesta si VERDADERO o FALSO.
 */

// El && es una comparación que solo vuelve si los dos son TRUE
    console.log(true && true); //TRUE
    console.log(false && true); //FALSE
    console.log(false && false); //FALSE

// El || hace una comparación solo cuando los dos sean FALSE
    console.log(true || true); //TRUE
    console.log(false || true); //TRUE
    console.log(false || false); //FALSE

// El ! es lo contrario de uno ya sea TRUE o FALSE
    console.log(!true);  //FALSE
    console.log(!false); //TRUE


/**
 * ---ASIGNACIÓN---
 * Son operadores que se asignan a valores
 * que ya existen en las variables,
 * también la sintaxis en como se escribe.
*/
// El = es para asignar un valor a la variable
var x = 10;
console.log(x); // 10

// El += es una asignación con una adicción
var num1 = 6
console.log(num1 += 5); // 11

// El -= es de restar a la asignación
var num2 = 4;
console.log(num2 -= 3); // 1

// El *= es para multiplicar la asignación
var z = 4;
console.log(z *= 7); // 28

// El /= es la división la asignación
var y = 64;
console.log(y /= 2); // 32

// El %= es el residuo de la asignación
var residuo = 100;
console.log(residuo %= 11); // 11

// El **= es el exponente de una asignación 
var expo = 4;
console.log(expo **= 2); // 16

// Estos operadores no se utilizan ya que todo el proceso es a nivel bit

// El <<= es decir que los bits de una asignación se recorran los bits del segundo valor y se convierte en el bit existente a decimal
var izquierda = 2;
console.log(izquierda <<= 1); // 4

// El >>= es decir que los bits de una asignación se recorran los bits del segundo valor y se convierte en el bit existente a decimal
var derecha = 2;
console.log(derecha >>= 1); // 1



/**
 * ---COMPARACIÓN---
 * Estos sirven para comprar diferentes fuentes
 * o variables en las cuales se utilizan,
 * sirven también si un proceso se realiza o no.
*/
var variable1 = 3;
var variable2 = 4;

//El == vuelve true si son iguales
console.log(variable1 == "3"); //true
console.log(variable1 == 3); //true

//El != vuelve true no son iguales
console.log(variable2 != "3"); //true
console.log(variable1 != 4); //true

//El === vuelve true si son iguales y son del mismo tipo
console.log(variable1 === 3); //true

//El < vuelve true si  es menor que
console.log(variable1 < variable2); //true

//El <= vuelve true si  es menor que o igual que
console.log(variable1 <= 3); //true

//El > vuelve true si es mayor que
console.log(variable1 > variable2); //false

//El >= vuelve true si  es menor que o igual que
console.log(variable1 >= 4); //false




/**
 * -----TIPO DE ESTRUCTURA DE CONTROL-----
 * Dentro de las estructuras de control existen estos:
 * If-Else
 * Switch
 * While
 * Do while
 * For
 * Try Catch
 */

//---IF - ELSE---
var edad = 19;
if (edad >= 18) {
    console.log("Es mayor de edad, puede votar");
} else {
    console.log("No es mayor de edad, regrese cuando tenga 18 años cumplidos");
}

//---SWITCH---
var hoy = new Date();
var nombreMes;
var mes=hoy.getMonth();
switch (mes) {
    case 0 :
        nombreMes = "Enero";
        break;
    case 1 :
        nombreMes = "Febrero";
        break;
    case 2 :
        nombreMes = "Marzo";
        break;
    case 3 :
        nombreMes = "Abril";
        break;
    case 4 :
        nombreMes = "Mayo";
        break;
    case 5 :
        nombreMes = "Junio";
        break;
    case 6 :
        nombreMes = "Julio";
        break;
    case 7 :
        nombreMes = "Agosto";
        break;
    case 8 :
        nombreMes = "Septiembre";
        break;
    case 9 :
        nombreMes = "Octubre";
        break;
    case 10 :
        nombreMes = "Noviembre";
        break;
    case 11 :
        nombreMes = "Diciembre";
        break;
    default:
        nombreMes = "No existe el mes"
        break;
}
console.log("El mes es " + nombreMes);

//---WHILE---
var i = 0;
while (i <= 9) {
    console.log(i);
    i++;
}
/* Entro imprime en la consola
0
1
2
3
4
5
6
7
8
9
 */

//---DO WHILE---
var numero = 1;
var resultado = 2;
do {
    numero++;
    resultado = resultado * numero;
    console.log(resultado);
} while (numero < 5);
/* Entro imprime en la consola
4
12
48
240
*/

//---FOR---
for (let i = 0; i <= 10; i++) {
    console.log(i);
}
/* Entro imprime en la consola
0
1
2
3
4
5
6
7
8
9
10*/

//---TRY - CATCH---
try {
    throw new Error('Si funciona');
} catch (error) {
    console.error(error.message);
}
/**
 * En este caso cuando se ejecuta si es
 * correcto la operación pasara por el try-catch,
 * en dado caso de causar conflicto se ira directo al error
*/ 



/**-----DIFICULTAD EXTRA-----*/
for (let i = 10; i < 55; i++) {
    if((i % 2 == 0) && (i !== 16) && (i % 3 !== 0)){
        console.log(i);
    }
}
/**-----DIFICULTAD EXTRA-----*/