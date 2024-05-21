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
//Operadores en JS
//Aritméticos: son los operadores básicos para realizar cualquier operación aritmética
//Incremento
const incremento = 1 + 2;
//Decremento
const decremento = 8 -1;
//Multiplicación 
const multiplicacion = 2 * 18;
//Divición 
const division = 9 / 3;
//Substracción 
const substracion = 10 % 2;
//Potenciasión
const potenciacion = 3**2;
//Operadores de asiganción: estos operadores asignan un valor en una operación de manera consistente
//un uso muy frecuente de este tipo de opereadorees es de uttilizarlos como acumuladores
let x = 1;
//asiganamiento de incremento
x= x+3;
//asiganamiento de decremento
x = x-2;
//asiganamiento de multiplicación
x = x*2;
//asiganamiento de divicón
x = x/2;

//Operadores lógicos: efectuán operaciones lógicas donde el resultado es una valor booleano ("true" o "false")
//Estrita igualdad
const igualdad = 5 === 2 + 4;
//Desigualdad
const desigualdad = 5 !== 2 + 3 ;
//menor que
const menor = 10 < 6;
//mayor que
const mayor = 10 > 20;
//menor o igual que
const menorIgual = 3 <= 2;
//MayorIgual
const mayourIgual = 5 >= 4;

//Estructuras de control: permiten alterar e flujo de  control del programa

//selectivas: permiten ejeecutar una sentencia o un bloque de sentencia dependiendo del resultado de una condición
//if
if(10>5){
  console.log("10 es mayor a cinco");
}
//if-else
if(10>20){
    console.log("10 es mayor a 20");
}
else{
    console.log("10 no es mayor a 20");
}
//switch: permite ejecutar una sentencia(s) en base al valor que una variable/expresión pueda tomar
const expre = "Naranja";
switch(expre){
 case "azul":
    console.log("azul");
    break;
case "rosa":
    console.log("rosa");
    break;
case "verde":
    console.log("verde");
    break;
default:
    console.log("color no encotrado");
    break;

}
//repetitivas
let i = 1;
//ciclo while: ejecuta un sentencia(s) mientras se cumpla una determinada condición
while( i < 10){
    console.log(i);
    i+=1;
}
//do while: permite ejecutar al menos una vez el ciclo while
let j = 1;
do{
    console.log(j);
    j+=1;
}while(j<10)
//for: ejecuta un código un número predeterminado de veces
for(let k = 0; k<10;k++){
    console.log(k);
}
const colores= ["verde","naranja", "azul", "rojo"];
//for of loop: perimite iterar sonbre los valores de un objeto
for(const color of colores){
    console.log(color);
}
const coloresObj = {
    verde: "color verde",
    rojo: "color rojo",
    azul: "color azul",
    naranja: "color naranja"
}
//for in loop: permite iterar sobre las keys de un objeto en lugar de los valores.
for(const key in coloresObj){
    console.log(key);
}
//De manejo de exepciones
 function dividir(dividendo, divisor) {
    if (divisor === 0) {
      
      throw new Error("No se puede dividir por cero");
    }
    return dividendo / divisor;
  }
  //Try-catch: señala un bloque de intrucciones a intenter y especifica una respuesta si se produce un expción.
try {
 
    let resultado = dividir(10, 0); 
    console.log("El resultado es: " + resultado); 
  } catch (error) {
   
    console.log("Ha ocurrido un error: " + error.message);
  }
 //Try-catch-finally
 try {
 
    let resultado = dividir(10, 0); 
    console.log("El resultado es: " + resultado); 
  } catch (error) {
   
    console.log("Ha ocurrido un error: " + error.message);
  }
  finally{
    console.log("Finalizando el proceso.");
  }
  //Dificultat extra
 for(let z = 10; z <= 55; z++) {
    if(z === 10 || z === 55 || (z % 2 === 0 && z !== 16 && z % 3 !== 0)) {
        console.log(z);
    }
}
