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
 * LAURA ORTEGA - 02/01/2024
 */

/***************************************************************************/
/* 1-OPERADORES DEL LENGUAJE */

console.log('OPERADORES DE ASIGNACIÓN');
console.log('Para asignar un valor a una variable, se utiliza el signo de igual (=)');
let numero = 10; //Asignación

numero +=2; //Asignación de adición
console.log('Existe la asignación de adición, donde se suma el valor de una variable con otro. El signo utilizado es (+=). Por ejemplo, si el valor de la variable es 10, el resultado de (10+2) es ' + numero);

numero-=2; //Asignación de resta
console.log('Opuesto a ella está la asignación de resta, donde se resta el valor de una variable con otro. El signo utilizado es (-=). Por ejemplo, si el valor de la variable es 12, el resultado de (12-2) es ' + numero);

numero*=3; //Asignación de multiplicación
console.log('Tenemos también la asignación de multiplicación, donde se multiplica el valor de una variable con otro. El signo utilizado es (*=). Por ejemplo, si el valor de la variable es 10, el resultado de (10*3) es ' + numero);

numero/=3; //Asignación de división
console.log('Y  asignación de división, donde se divide el valor de una variable con otro. El signo utilizado es (/=). Por ejemplo, si el valor de la variable es 30, el resultado de (30/3) es ' + numero);
let resto = numero;

resto %=3; //Asignación de residuo
console.log('Contamos además con la asignación de residuo (o resto), donde se obtiene el residuo de una división. El signo utilizado es (%=). Por ejemplo, si el valor de la variable es 30, el resultado de (30%3) es ' + resto);

numero**=2; //Asignación de potencia
console.log('La asignación de potencia, donde se obtiene la potencia de un número. El signo utilizado es (**=). Por ejemplo, si el valor de la variable es 10, el resultado de (10**2) es ' + numero);

numero = 10;
numero>>=2; //Asignación de desplazamiento a la derecha - 10/(2*2) = 2  
console.log('La asignación de desplazamiento, donde se desplaza un número. El signo utilizado es (>>=). Esto equevale a dividir por 2^n. Por ejemplo, si el valor de la variable es 10, el resultado de (10>>2) es ' + numero);

numero = 10;

numero<<=2; //Asignación de desplazamiento a la izquierda - 10*(2*2) = 40
console.log('Funciona igual que la anterior, pero se desplaza a la izquierda. El signo utilizado es (<<=). Esto equevale a multiplicar por 2^n. Por ejemplo, si el valor de la variable es 10, el resultado de (10<<2) es ' + numero);

numero = 10;

numero >>>=2; //Asignación de desplazamiento a la derecha sin signo - 10/(2*2) = 2

console.log('Igual a la anterior, pero sin mantener el signo. El signo utilizado es (>>>=). Esto equevale a dividir por 2^n. Por ejemplo, si el valor de la variable es 10, el resultado de (10>>>2) es ' + numero);

numero = 1;

numero&='soy un string'; //Asignación de AND
console.log("AND: "+numero); // El operador AND bit a bit compara cada bit de su primer operando con el bit correspondiente de su segundo operando. Si ambos bits son 1, el bit del resultado correspondiente se establece en 1. De lo contrario, el bit del resultado correspondiente se establece en 0.

numero = 1;

numero^=1; //Asignación de XOR
console.log("XOR: "+numero); //El operador XOR compara los bits de ambos operandos. Si ambos bits son iguales, el bit del resultado es 0. Si uno de los dos bits es 1, el bit del resultado es 1.

numero = 1;

numero |= 1; //Asignación de OR
console.log("OR: "+numero); //El operador OR compara los bits de ambos operandos. Si ambos bits son 0, el bit del resultado es 0. Si uno de los dos bits es 1, el bit del resultado es 1.

numero = 1;

numero &&= '1';
console.log("AND: "+numero); //El operador AND compara los bits de ambos operandos. Si ambos bits son 1, el bit del resultado es 1. Si uno de los dos bits es 0, el bit del resultado es 0.

numero = 1;

numero ||= '1'; //Asignación de OR
console.log("OR: "+numero); //El operador OR compara los bits de ambos operandos. Si ambos bits son 0, el bit del resultado es 0. Si uno de los dos bits es 1, el bit del resultado es 1.


numero = 1;

numero ??= '1'; //Asignación de OR
console.log("OR: "+numero); //El operador OR compara los bits de ambos operandos. Si ambos bits son 0, el bit del resultado es 0. Si uno de los dos bits es 1, el bit del resultado es 1.

console.log('OPERADORES DE COMPARACIÓN');

console.log('El operador de igualdad (==) compara el valor de dos operandos. El signo utilizado es (==). Por ejemplo, si el valor de la variable es 10, el resultado de (10==10) es ' + (10==10));
console.log('El operador de desigualdad (!=) compara el valor de dos operandos. El signo utilizado es (!=). Por ejemplo, si el valor de la variable es 10, el resultado de (10!=10) es ' + (10!=10));
console.log('El operador de igualdad estricta (===) compara el valor y el tipo de dos operandos. El signo utilizado es (===). Por ejemplo, si el valor de la variable es 10, el resultado de (10===10) es ' + (10===10) + ' y (10==="10") es ' + (10==="10"));
console.log('El operador de desigualdad estricta (!==) devuelve true si los operandos son del mismo tipo pero no iguales, o son de diferente tipo. El signo utilizado es (!==). Por ejemplo, si el valor de la variable es 10, el resultado de (10!==10) es ' + (10!==10) + ' y (10!=="10") es ' + (10!=="10"));
console.log('El operador de mayor que (>) compara el valor de dos operandos. El signo utilizado es (>). Por ejemplo, si el valor de la variable es 10, el resultado de (10>10) es ' + (10>10));
console.log('El operador de menor que (<) compara el valor de dos operandos. El signo utilizado es (<). Por ejemplo, si el valor de la variable es 10, el resultado de (10<10) es ' + (10<10));
console.log('El operador de mayor o igual que (>=) compara el valor de dos operandos. El signo utilizado es (>=). Por ejemplo, si el valor de la variable es 10, el resultado de (10>=10) es ' + (10>=10));
console.log('El operador de menor o igual que (<=) compara el valor de dos operandos. El signo utilizado es (<=). Por ejemplo, si el valor de la variable es 10, el resultado de (10<=10) es ' + (10<=10));

console.log('OPERADORES ARITMETICOS');

console.log('El operador de suma (+) compara el valor de dos operandos. El signo utilizado es (+). Por ejemplo, si el valor de la variable es 10, el resultado de (10+10) es ' + (10+10));
console.log('El operador de resta (-) compara el valor de dos operandos. El signo utilizado es (-). Por ejemplo, si el valor de la variable es 10, el resultado de (10-10) es ' + (10-10));
console.log('El operador de multiplicación (*) compara el valor de dos operandos. El signo utilizado es (*). Por ejemplo, si el valor de la variable es 10, el resultado de (10*10) es ' + (10*10));
console.log('El operador de división (/) compara el valor de dos operandos. El signo utilizado es (/). Por ejemplo, si el valor de la variable es 10, el resultado de (10/10) es ' + (10/10));
console.log('El operador de residuo (%) compara el valor de dos operandos. El signo utilizado es (%). Por ejemplo, si el valor de la variable es 10, el resultado de (10%10) es ' + (10%10));
console.log('El operador de potencia (**) compara el valor de dos operandos. El signo utilizado es (**). Por ejemplo, si el valor de la variable es 10, el resultado de (10**10) es ' + (10**10));

numero = 10;
numero++;
console.log('El operador de incremento (++). El signo utilizado es (++). Por ejemplo, si el valor de la variable es 10, el resultado de (++10) es ' + numero);

numero = 10;
numero--;
console.log('El operador de decremento (--). El signo utilizado es (--). Por ejemplo, si el valor de la variable es 10, el resultado de (--10) es ' + numero);

console.log('El operador de negación unitaria (~). El signo utilizado es (~). Por ejemplo, si el valor de la variable es 10, el resultado de (~10) es ' + (~10));
console.log('El operador de negación unaria (!). El signo utilizado es (!). Por ejemplo, si el valor de la variable es 10, el resultado de (!10) es ' + (!10));


console.log('OPERADORES LÓGICOS');

console.log('El operador de conjuncio (&&) compara el valor de dos operandos. El signo utilizado es (&&). Por ejemplo, si el valor de la variable es 10, el resultado de (10&&10) es ' + (10&&10));
console.log('El operador de disyuncio (||) compara el valor de dos operandos. El signo utilizado es (||). Por ejemplo, si el valor de la variable es 10, el resultado de (10||10) es ' + (10||10));
console.log('El operador de XOR (XOR) compara el valor de dos operandos. El signo utilizado es (XOR). Por ejemplo, si el valor de la variable es 10, el resultado de (10^10) es ' + (10^10));
console.log('El operador de NOT lógico (!) compara el valor de dos operandos. El signo utilizado es (!). Por ejemplo, si el valor de la variable es 10, el resultado de (!10) es ' + (!10));

/**Por la extensa cantidad de operadores, se anexa el link para leer más sobre ellos: https://developer.mozilla.org/es/docs/Web/JavaScript/Guide/Expressions_and_Operators**/
/***************************************************************************/
/* 2-ESTRUCTURAS DE CONTROL */

let index = 1;

while(index <= 10) { //Ciclo while. Puede no ser ejecutado.
    console.log(index);
    index++;
}

do{ //Ciclo do while. Se ejecuta al menos una vez.
    index--;
    console.log(index);
}while(index > 1);

const edad = 19;

if(edad <18){ // If. Revisa las condiciones
    console.log("No eres mayor de edad");
}else{ // Else. Si no se cumple la condición del if, se ejecuta
    console.log("Eres mayor de edad");
}

const opcion = 2;

switch(opcion){ // Switch. Revisa las opciones y ejecuta la correspondiente al caso
    case 1:
        console.log("Opcion 1");
        break;
    case 2:
        console.log("Opcion 2");
        break;
    case 3:
        console.log("Opcion 3");
        break;
    default:
        console.log("Opcion no encontrada");
        break;
}

for(let i = 1; i <= 10; i++){ // For. Se ejecuta hasta que no se cumpla la condición
    console.log(i);
}
const constante = 10;
try{ // Try. Intenta ejecutar el bloque de código
    constante = 20;
}catch(error){ // Catch. Se ejecuta si hay un error sin interrupir la ejecución del programa
    console.log(error);
}


/***************************************************************************/
/* 3-EXTRA */

/*Crea un programa que imprima por consola todos los números comprendidos entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.*/

let n = 10;

while(n <= 55){
    if(n!==16 && (n%3!==0 && n%2===0)){
        console.log(n);
    }
    n++;
}

/***************************************************************************/