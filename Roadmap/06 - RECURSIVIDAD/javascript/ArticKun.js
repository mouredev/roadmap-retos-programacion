

// ⚡ RECURSIVIDAD
/*
En JavaScript, la recursividad es un 
concepto en el que una función que:

1. Se llama a sí misma durante su ejecución. 
2. Debe tener una condicion donde deje de llamarse asi misma

Esto puede ser útil para resolver problemas que pueden 
dividirse en subproblemas más pequeños y similares al 
problema original.

*/

//* 1. IMPRIMIR NUMEROS DEL 0 al 100 CON RECURSIVIDAD

function numerosRecursivos( numero ) {
// Caso base: detener la recursión cuando se alcanza el 100
    if ( numero > 100 ) {
      return;
    }
// Imprimir el número actual
    console.log( numero );
// Llamada recursiva con el siguiente número
    numerosRecursivos( numero + 1 );
}


// Llamada inicial con el número inicial
numerosRecursivos( 0 );


//* 2. DIFICULTAD EXTRA (opcional):

// Utiliza el concepto de recursividad para:
// - Calcular el factorial de un número concreto (la función recibe ese número).
// - Calcular el valor de un elemento concreto (según su posición) en la 
//   sucesión de Fibonacci (la función recibe la posición).

// ⚡ 1. FACTORIAL DE UN NUMERO CON RECURSIVIDAD:
function numeroFactorial( n ){
    if (  n === 0 ){
        return 1;
    }else{
        return n * numeroFactorial( n - 1 );
    }
};

// 5! = 5 x 4 x 3 x 2 x 1
numeroFactorial( 5 ); // output : 120 

// ⚡ 2. SECUENCIA FIBONACCI CON RECURSIVIDAD:



function numeroFibonacci( num ){
    
    if( num <= 0 ){
        print('Numeros negativos no válidos');
        return 0;
    }
    else if( num === 1 ){
        return 0;
    }
    else if( num === 2 ){
        return 1;
    }
    else{
        console.log(num);
        return numeroFibonacci( num - 1 ) + numeroFibonacci ( num - 2 );
    }

};

numeroFibonacci( 3 );