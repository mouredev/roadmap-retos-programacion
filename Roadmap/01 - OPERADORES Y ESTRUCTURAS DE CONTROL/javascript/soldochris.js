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

//Operadores Aritméticos
let suma = 2 + 8;
let reste = 7 - 2;
let mulplicacion = 3 * 4;
let potencia = 2 ** 3;
let division = 10 / 5;
let residuo = 9 / 2;

//Operadores de comparación
let igualdad = 2 == 4;
let igualdadEstricta = 2 === 2;
let diferencia = 5 != 4;
let diferenciaEstricta = 3 !== 8;
let menor = 3 < 5;
let menorIgual = 1 <= 6;
let mayor = 9 > 2;
let mayorIgual = 8 <= 4;

//Operadores de lógicos
let y = true && true;
let o = true || false;
let negacion = !false;

//Operadores de Asignacion
let variable = 2;

variable += 2; //primero se realiza la suma y luego se hace la asignacion
variable =+ 2; //primero se realiza la asignacion y luego se hace la suma
variable -= 2; //primero se realiza la resta y luego se hace la asignacion
variable =- 2; //primero se realiza la asignacion y luego se hace la resta

//Operador de Incremento
variable++;

//Operador de Decremento
variable--;

/* Estructuras de control */

//IF
if(true){
  console.log("Se ejecutara si la condición se cumple o es verdadera");
}else{
  console.log("Se ejecutara en casi la primera condición no se cumpla o se falsa");
}

//while
let iterador = 0;

while(iterador < 5){
  console.log("Se ejecutara mientras iterador sea menor que 5");
  console.log(`El valor actual de iterador es: ${iterador}`);
  iterador++;
}

//For
for(let i = 0; i < 5 ; i++){
  console.log("Se ejecutara mientras i sea menor que 5");
  console.log(`El valor actual de i es: ${i}`);
}

//Try - Catch - Finally
try{
  console.log("Primero intentara ejecutarse este bloque de código");
}catch{
  console.log("Este bloque de código se ejecutara al ocurrir un error en el primer bloque");
}finally{
  console.log("Finalmente se ejecutara este bloque de código");
}

/* DIFICULTAD EXTRA */
for(let i = 10 ; i <= 55; i++){
  if( i % 2 == 0 && i != 16 && i % 3 != 0){
    console.log(i);
  }
}