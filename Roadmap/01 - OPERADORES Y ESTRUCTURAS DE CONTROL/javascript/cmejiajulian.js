/*
* #01 OPERADORES Y ESTRUCTURAS DE CONTROL
*/

/*
 *   Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
*/ 

//OPERADORES ARITMETICOS 

let num1 = 8;
let num2 = 2;
//Suma: +
console.log(num1+num2);
//Resta: -
console.log(num1-num2);
//Multiplicacion: *
console.log(num1*num2);
//Division: /
console.log(num1/num2);
//Modulo: %
console.log(num1%num2);
//Exponenciación: **
console.log(num1**num2);
//Incremento: ++
console.log(num1++);
console.log(num1);
//Decremento: --
console.log(num2--);
console.log(num2);


//OPERADORES DE ASIGNACION 

let a = 9;

// Asignación: =
console.log (a);
// Asignación de adición: +=
a+=2;
console.log(a);
// Asignación de sustracción: -=
a-=2;
console.log (a);
// Asignación de multiplicación: *=
a*=2;
console.log (a);
// Asignación de módulo: %=
a%=2;
console.log(a);
//Asignación de exponenciación: **=
a**=2;
console.log(a);

// OPERADORES DE COMPARACION 

let x = 1
let y = 1 
// Igualdad: ==
console.log( x == y );
// Desigualdad: !=
console.log( x != y );
// Desigualdad estricta: !==
console.log( x !== y );
// Mayor que: >
console.log(5>3);
// Mayor o igual que: >=
console.log(5>=9);
// Menor que: <
console.log(7<3);
// Menor o igual que: <=
console.log(2<=2);

// OPERADORES LOGICOS 
 let ope1 = true;
 let ope2 = false;

// AND lógico: &&

console.log(ope1 && ope1);
console.log(ope1 && ope2);
console.log(ope2 && ope2);
console.log(ope2 && ope1);
  
// OR lógico: ||

console.log(ope2 || ope2);
console.log(ope1 || ope2);
console.log(ope1 || ope1);
console.log(ope2 || ope1);

// NOT lógico: !

console.log(!ope1);
console.log(!ope2);

//OPERADORES DE CADENA 

//Concatenación: (+)

let name1 = 'Peter';
let lastName = ' Parker';

console.log( name1 +""+ lastName);

// OPERADORES RELACIONALES

// En: in (verifica si una propiedad está en un objeto)

let marvel = { superHero : 'Spiderman', power:'Escalar' };

console.log( 'superHero' in marvel);
console.log( 'Villano' in marvel);


// OPERADORES DE BIT
let first = 11;
let second = 5;

// AND bit a bit: &
console.log( first & second);

// OR bit a bit: |
console.log( first|second);

// XOR bit a bit: ^
console.log( first ^ second);

// NOT bit a bit: ~
console.log( ~first);

// Desplazamiento a la izquierda: <<
console.log(first <<2);

// Desplazamiento a la derecha: >>
console.log(second >>2);

// Desplazamiento a la derecha sin signo: >>>
console.log(second >>>1);

/*
*   Utilizando las operaciones con operadores que tú quieras, crea ejemplos
*   que representen todos los tipos de estructuras de control que existan
*   en tu lenguaje:
*   Condicionales, iterativas, excepciones...
*/


//CONDICIONALES

// if y else

//*
let book = 'EL DIOS DE LA GUERRA';

if (book == 'EL DIOS DE LA GUERRA') 
    
    {console.log( 'Si, es el libro recomendado')}

else
    {console.log('Es el libro para estar mejor')}

//else if 

//*
let personaje = 'SuperMan'

if (personaje === 'Tanos')
    {console.log('Es el Dios de la destruccion')}

else if (personaje === 'SuperMan')
    {console.log('Es el salvador')}

else
    {console.log('Es una farsa')};

//for 

for (let i = 0; i<=10; i++) {
    console.log(i);
  }

let j = 0 

//while

while (j<=10){
    console.log(j);
    j++
}

//Control de excepciones

//try, catch, finally

try {
    console.log(50/0);
  } catch (error)  {
    console.log('Ocurrió un error:',error.mesage);
  } finally {
    console.log('Esta sección se ejecuta siempre');
  };
  

try {
    let resultado = 50/0;
    console.log(resultado);
  } catch (error) {
    console.log('Ocurrió un error:', error.message);
  } finally {
    console.log('Esta sección se ejecuta siempre');
  }

  
/*
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 */

//Primero creamos una ciclo for que inicia en i = 10 y termina en i<=5 con un incremento de i++ 

for (let i = 10; i<=55; i++ )

/*luego usamos la condicion if para determinar los pares y sacar el numero 16 y los multiplos de 3 
  como lo hacemos 
  1) Usamos el operador de asignacion del modulo, teniendo en cuenta que si el modulo es 0 es multiplo
  de 2,  cabe resaltar que hacemos la igualdad == a 0 para que sea multiplo valga la redundancia 

  2) luego usamos el operador logico and (&&) para asignar otra condicion 

  3) usamos el operador de COMPARACION de Desigualdad estricta: !== para extraer el numero 16 de la lista

  4) continuando con la secuencia de operadores logicos colocamos el modulo de 3 para que sea distinto de cero
  y asi determinar los que no son multiplos de tres
  */

    if(i%2==0 && i!==16 && i%3!=0 )
    {
    console.log(i);
}

