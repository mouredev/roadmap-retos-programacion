/*
  * EJERCICIO:
  * Entiende el concepto de recursividad creando una función recursiva que imprima
  * números del 100 al 0.
*/

const countDownBOOM = ( value ) => {
    for( let i = value; i>=0; i-- ){
        console.log(`Countdown => ${i}`);
        if( i === 0 ){
          console.log("BOOOOOOOM");
        }
    }
}
countDownBOOM(100);

/*
  * DIFICULTAD EXTRA (opcional):
  * Utiliza el concepto de recursividad para:
  * - Calcular el factorial de un número concreto (la función recibe ese número).
  * - Calcular el valor de un elemento concreto (según su posición) en la
  *   sucesión de Fibonacci (la función recibe la posición).
*/

// Calcular el factorial de un numero concreto (Se recibe como parametro)
const factorial = ( value ) => {
    let aux = [];

    for( let i = 1; i <= value; i++ ){
      aux.push(i);
    }
  
  // console.log( aux );
  let result = aux.reduce( ( valueA, valueB ) => valueA * valueB );
  console.log( result );
}
factorial( 6 );

// Fibonacci:
const fibonacci = (value) => {

  let numbers = [0, 1];
  for (let i = 2; i < value; i++) {
    numbers[i] = numbers[i - 1] + numbers[i - 2];
  }

  return numbers;

};

// 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89...
console.log( fibonacci( 10 ) );
