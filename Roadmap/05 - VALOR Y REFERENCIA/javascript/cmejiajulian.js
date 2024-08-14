/*
 * EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 */

//tipos de datos por valor 

//Number

let = 10;
let = 209.1;

//string 

let magoDeOz = 'El Lago';
let aerosmith = 'Jaded ';

//Bolean

let isIntelligent = true;
let isBoring = false;

//null --> Representa la ausencia intencional de un valor.

let valorReal = null;

//undefined --> Indica que una variable ha sido declarada pero no se le ha asignado un valor 

let notAssigned;

//Symbol --> Representa un valor unico y anonimo 

let sym1 = Symbol('Suma');
let sym2 = Symbol('another description');

// BigInt 

let numValue = 2921129241294129439493949394n;

//EJEMPLO DE COMPORTAMIENTO POR VALOR 


let x = 10; 
let y = x;

y = 20; 

console.log(x);
console.log(y);


//tipos de datos por referencia 

//objecto 

let cars =  {
    name:'Mercedes',
    model: 98,
    kilometraje:1000

}

let anotherCar = cars

anotherCar.model = 2000

console.log(cars.model);
console.log(anotherCar.model);


//array 

let numbers = [1,2,3,4,5,6]
let numbersDiferent = numbers;

numbersDiferent.push(12);

console.log(numbers);
console.log(numbersDiferent);


//function 

let time =()=>{
    console.log('Sunday');
}

let othertime = time 

othertime()



/* DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
 */


// Importa el módulo readline
const readline = require('readline');

// Configura readline para que lea desde la terminal
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

// PRIMER PROGRAMA Pregunta al usuario por el elemento 
rl.question('¿ingresa el elemento numero 1 por valor ? ', (valor1) => {
    rl.question('¿ingresa el elemento numero 2 por valor ? ', (valor2) => {
     
    if ( (!isNaN(valor1) && !isNaN(valor2))  ){
     let x = parseFloat (valor1) ; 
     let y = x
     
     y = parseFloat(valor2)

     
           console.log('Valor numero 1: ', x);
           console.log('Valor numero 2: ', y);
        }
        else{
            let x = (valor1) ; 
            let y = x
     
            y = (valor2)

     
           console.log('Valor numero 1: ', x);
           console.log('Valor numero 2: ', y);
       
        }
    // Cierra la interfaz de readline
   
// SEGUNDO PROGRAMA  Pregunta al usuario por el valor por referencia 


    rl.question('¿Ingresa el elemento número 1 por Referencia: ', (referencia1) => {
        rl.question('Ingresa el elemento número 2 por Referencia',(referencia2 )=>{
            
        let codigo = [referencia1]
        let llave = codigo 

        llave.push(referencia2);

        console.log(codigo);
        console.log(llave)

      // Cierra la interfaz de readline
      rl.close();
      })
    });
  });
});
