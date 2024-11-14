// <------- Operadores aritmeticos ---------->

/**
 * suma (+),
 * resta (-).
 * multiplicación(*),
 * división (/),
 * módulo (%),
 * incrementos o decrementos (++ , ++) ==> Aunmenta o disminuye en una unidad.
 */

let a = 5;
let b = 10;

console.log(a + b);
console.log(a - b);
console.log(a * b);
console.log(a / b);
console.log(a % b);

// <-------- Operadores Lógicos ---------->

/**
 * || (or) ===> Evalúa si por lo menos una de las condiciones se cumplen.
 * En caso de que eso suceda, devolverá TRUE
 * && (AND) ===> Evaluá si las dos condiciones se cumplen, en caso de ser así devolverá TRUE.
 * ! (Not) ===> EStablece una negación logica de una expresión, es decir, hará que una expreción que da como resultado TRUE, devuelva False
 */

// EJEMPLO
/** Determina si una persona es mayor de edad y tiene boleto de entrada. Si no es mayor de edad pero tiene acompañante, puede ingresar */

function puedeIngresar(edad, entrada, acompañante) {
    if (edad >= 18 && entrada === true) {
         console.log('Puede ingresar')
    } else if (edad < 18 && acompañante === true && entrada === true ) {
        console.log('Puede ingresar con acompañante');
    } else {
        console.log('No puede ingresar');
    }
}

puedeIngresar(20, true); // Puede ingresar
puedeIngresar(12, true, true); // Puede ingresar con acompañante
puedeIngresar(15, true,false); // No puede ingresar

// <------ Operadores de Comparación ---------->
 /**
  * == (igaul a)
  * === (igualdad estricta) ===> ESto quiere decir que el tipo de dato y el valor deben ser iguales
  * != (no es igual a)
  * !== (no igualdad estricta)
  * > (mayor que)
  * < (Menor que)
  * >= (mayor o igual)
  * >= (menor o igual)
  */

let y = 4;
let z = 5;
let w = 1;
console.log(y == '4'); // Comprobación de igualdad de valores sin verificar el tipo de dato
console.log(y != 3); // Comprobación de la diferencia de lavalores sin verificar el tipo de dato
console.log(y === 4); // Comprobación de igualdad de valores y tipo de dato
console.log(y !== 3); // Comprobación de la diferencia de valores o tipo de dato
console.log(z > y); // Comprobación si el valor de z es estrictamente mayor al de y
console.log(z >= y); // Comprobación si el valor de z es mayor o igual al de y
console.log(w < y); // Comprobación si el valor de w es estrictamente menor al de y
console.log(w <= y); // Comprobación si el valor de w es menor o igual al de y


 // <------------- Operadores de asignación --------------->

let x = 2; //operador de asignación
x += 1; // operador de adición, simboliza x = x + 1
x -= 1; // operador de resta, simboliza x = x - 1
x *= 1; // operador de multiplicación, simboliza x = x * 1
x /= 2; // operador de división, simboliza x = x / 2
x %= 2; // operador de resto, simboliza x = x % 2 y a x se le adigna el resto de la división
x **= 2; // operador de exponenciación, simboliza x = x ** 2 (x a la potencia de 2)

// <------ Operadores atipicos ----------->
/**
 * typeof ===> NOs indica el tipo de dato contenido en una variable,
 * void ===>  SE limita a impedir que todo funciones normalmente, es decir,
 *  que una vez evaluadas las instrucciones, sus efectos o presentación de 
 * resultados serán anulados. En principio podemos dudar de su utilidad,
 *  pero puede resultar muy util en las ocasiones en que, dependiendo de
 *  una evaluación previa, haya que deshabilitar algun objeto o impedir una
 *  alguna acción.
 */


// <------------ Estructuras de control ----------->

/** En javascript podemos dividir estas estructuras de control en don grandes grupos:
 * Condicionales, y
 * ciclos.
 */

// <-------- Condicionales ----------->

// if - else
/** Nos permite ejecutar un determinado bloque de código dependiendo de si una condición es verdadera o falsa. */

if(condicion){
    //Bloque de código
        // Código que se ejecutará si la condición es cierta
} else {
    //Bloque de código
        // Código que se ejecutará si la condición es falsa.
}

//ejemplo
let i = 10;
if(1 > 5) {
    console.log('EL valor de i es mayor a 5');
} else {
    console.log('El valor de i es menor a 5');
}

// <-------- Operador ternario --------->

/** Utiliza 3 operandos y en algunas ocasiones puede utlizarse como una abreviación de la estructura if else */

condicion ? expresion1 : expresion2

// Ejemplo
let i2 = (15 % 3 == 0) ? 'Si es múltiplo' : 'No es múltiplo'; // i = 'Si es múltiplo'


// <--------- Switch --------->

/**Surge de un concepto conocido como "caza de patrones" la idea es que
 *  dada una expresión esta se evalúe y se ejecute el código correspondiente
 *  a ese "caso". Si no encontramos un caso que coincida con la expresión,
 *  se ejecutará el bloque de código definido es default, aunque no es obligatorio 
 * definir este caso */

switch (expresion) {
    case x:
        //Bloque de código
        break;
    case y:
        //Bloque de código
        break;
    default:
        //Bloque de código
        break;    
}

// Ejemplo

let = 10;

switch(n) {
    case 10:
        console.log('Es 10')
    case 20: 
        console.log('Es 20')
        break;
    default:
        console.log('No se cumplió ningún caso');
        break;
}

// <----------- Ciclos ----------->

/**Un clico es una estructura de control que nos
 * permite ejecutar un mismo bloque de código varias
 *  veces hasta que cierta condición no sea cierta.
 */

// While

/** Verifica una condición y ejecuta el bloque de
 * código siempre que está sea cierta; en cuanto la
 * condición sea falsa, el ciclo dejará de ejecutarse.
 */

while (condición) {
    //Bloque de código
}

/** Un cliclo while se caracteriza por el manejo
 * manual de los iteradores. Un iterador es un valor
 * que utilizamos para controlar las repeticiones del
 * ciclo y evitar quedarnos estancados en un solo
 * valor; esto ocasionariá que el ciclo se ejecutará
 * infinitamente, pues al no cambiar el valor en la 
 * condición no llegariamos nunca a un punto en 
 * donde la condición seria falsa. Para lograr esto
 * debemos modificar el valor de dicho iterador en 
 * cada ejecución del bloque de código.
 */

// Ejemplo

let i3 = 0;
while (i3 <= 20) {
    if(i3 % 2 == 0) {
        console.log(i3);
        i3++;
    }
}

// <------- Do while ---------->
/** Do while funciona de manera similar a while
 * la diferencia es que en while primero se evalúa
 * la condición y luego se ejecuta el codigo. 
 * En do while, primero se ejecuta el código y luego
 *  se evalúa la condición. Pueden haber casos en
 * que la condición no se evalúa nunca.
 */

do {
    //Bloque de código
} while (condicion)

//Ejemplo
let i4 = 15;
while (i4 < 10) {
    console.log('Se ejecuta el while');
}

do{
    console.log('Se ejecutó el do-while');
} while (i4 < 10);

// el while no se ejecuta porque la condición es falsa
// El do- while se ejecuta una vez, y es hasta que esa ejecución termina que se revisa la condición de pemanencia y el ciclo termina.

// <--------- For ----------->
/**La sintaxis del for se compone de tres elementos principales:
 * iterador ===> Para controlar el número de veces que se ejecuta un ciclo
 * condición ===> Si la condición se evalúa como true el ciclo se ejecuta por otra iteración, si la condición se evalúa como false, la ejecución termina.
 * incremento ===> Es la modificación del valor del iterador.
 */ 

for (iterador; condición; incremento) {
    //BLoque de código
}

// Ejemplo

for (let i5 = 0; i5 <= 20; i5++) {
    if(i5 % 2 == 0){
        console.log(i5);
    }
}

// <--------- Try-Catch ------------>

/** Nos permite definir un bloque de código para 
 * intentar ejecutar (try), y una respuesta si es que
 * se prodice una excepción en dicha ejecución (catch).
 */

try {
    //Bloque de código
} catch (excepción) {
    // Bloque de código
}

// Ejemplo

try{
    ejemplo();
} catch (e) {
    console.log('Ha ocurrido el error:' + e);
}


// <----------- Dificultad extra ------------->

/*** Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3. */

for (let num = 10; num < 56; num++){
    if (num % 2 == 0 && num != 16 && num % 3 != 0) {
        console.log(num);
    }
}