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


      var intercambioDeValor = (valor1,valor2) => {

          if(!isNaN(parseFloat(valor1)) && !isNaN(parseFloat(valor2))) { 
             let inter = parseFloat(valor1);
             (valor1) = parseFloat(valor2);
             (valor2)= inter;
             return[valor1,valor2];

          } else {
               let inter = valor1;
               valor1 = valor2;
               valor2 = inter;
               return[valor1,valor2];
              
            }
      }
      let x = valor1;
      let y = valor2;
       

      let [nuevoValor1,nuevoValor2] = intercambioDeValor(x,y);
x

   

      console.log(`Valor Original 1 : ${x}, Valor Original 2: ${y}`);
      console.log(`Nuevo Valor Original 1: ${nuevoValor1}, Nuevo Valor Original 2: ${nuevoValor2}`);
      

    
   
    // Cierra la interfaz de readline
   
// SEGUNDO PROGRAMA  Pregunta al usuario por el valor por referencia 


    rl.question('¿Ingresa el elemento número 1 por Referencia: ', (referencia1) => {
        rl.question('Ingresa el elemento número 2 por Referencia',(referencia2 )=>{
            
          let intercambioPorReferencia = (ref) => {
            let inter = ref[0];
            ref[0] = ref[1];
            ref[1] = inter;
        }

        let variableR = [referencia1, referencia2];
        let variableRO = [...variableR]; // Crea una copia de variableR

        intercambioPorReferencia(variableRO);

        console.log(`Variable original 1: ${variableR[0]}, Variable original 2: ${variableR[1]}`);
        console.log(`Nuevo valor 1: ${variableRO[0]}, Nuevo valor 2: ${variableRO[1]}`);
      // Cierra la interfaz de readline
      rl.close();
      })
    });
  });
});
