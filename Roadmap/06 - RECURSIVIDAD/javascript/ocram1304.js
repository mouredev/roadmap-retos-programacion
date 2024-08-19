/*Recursividad Es aquella propiedad que posee una función para llamarse así misma, funciona como una alternativa a la iteración. 
Los subprogramas recursivos -funciones- son aquellos que pueden llamarse así mismos de manera indirecta o directa.

Tipos de recursión
La recursión puede darse de dos maneras: directa e indirecta. En el código de una recursión directa el subprograma recursivo
F tiene una sentencia que invoca a F, mientras que una recursión indirecta el subprograma F  invoca al subprograma G y este a su 
vez invoca a P así sucesivamente hasta que se invoca de nuevo a F.

Condición de terminación 
Para que un algoritmo recursivo sea correcto este no debe de  generar una secuencia infinita de llamadas sobre sí mismo, pues cualquier 
algoritmo que ejecute esto no terminará nunca. Por ello la definición recursiva debe de tener un componente base (una condición de salida) en 
el que una función f(n) se define directamente (es decir no recursiva) para un o más valores de n
*/

//Generar numeros del 1 al 100 de manera recursiva
function genera(num){
    
    num+=1;
    console.log(num)
    if(num === 100){ //Caso base (condición de terminación)
        return "Se ha terminado de imprimir";
    }

    return genera(num);//LLamada recursiva

}
console.log(genera(0))

//Dificultad extra
function factorial (n){
    //Verifiacar que el argumento es valido. Quea sea un número entero
    if (typeof n !== 'number' || n < 0 || !Number.isInteger(n)) {
        return "Entrada inválida. El número debe ser un entero no negativo.";
    } 

    if(n === 0){ //Caso base, si "n" es igual a cero, se concluye la llamada recursiva y se regreesa el caso base
                 //El factorial de 0 es 1, es de dónde se empieza a calcular el factorial
        return 1;
    }
    return n*factorial(n-1)

}
confirm.log(factorial(4));
function fibonacci(posicion) {
    if (posicion === 0 || posicion === 1) { //Caso base
      return posicion;
    } else {
      return fibonacci(posicion - 1) + fibonacci(posicion - 2);//Suma valores en las posicio-1 y piscion-2
    }
  }
  
  console.log(fibonacci(25)); // Debería imprimir el 25º valor en la secuencia Fibonacci
  


