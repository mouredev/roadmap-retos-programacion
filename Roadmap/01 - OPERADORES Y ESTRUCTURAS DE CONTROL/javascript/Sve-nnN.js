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
 */

//Declaracion de variables
let a = 1;
const b = 5;
var c = 10;
let num=55;
//Esctructuras de control
while(a<b){
  //Mientras que A sea menor que B, imprime A
  console.log(a);
  a++;
}
for(var i=0;i<=b;i++){
  //Imprime del 0 al 5
  console.log(i);
}
if(b%2==0){
  //Si B es Par, imprime que es par
  console.log("B es par");
}else {
  //Si B es impar, imprime que es impar
  console.log("B es impar");
}
//Dificultad extra
for(var i=10;i<=num;i++){
  if(i%2==0 && i!=16 && i%3!=0){
    console.log(i);
  }
}
