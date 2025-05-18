// ! #01 OPERADORES Y ESTRUCTURAS DE CONTROL //

// EJERCICIO

let numero1 = 20; // Asignacion simple con "=".
let numero2 = 2;

/*- Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
    Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
    (Ten en cuenta que cada lenguaje puede poseer unos diferentes) */

//Operadores Aritméticos:
console.log(numero1 + numero2); // Suma.
console.log(numero1 - numero2); // Resta.
console.log(numero1 / numero2); // División.
console.log(numero1 * numero2); // Multiplicación.
console.log(numero1 % numero2); // Resto entero.
console.log(numero1++); // Incremento.
console.log(numero1--); // Decremento.

//Operadores de Comparación:
console.log(numero1 == 20); //true (Igualdad) Valida dato pero no su tipo.
console.log(numero1 === "20"); //false (Igualdad Estricta) Valida dato y tipo del mismo.
console.log(numero1 != 20); //false (Desigualdad) Valida dato pero no su tipo.
console.log(numero1 !== "20"); //true (Desigualdad Estricta) Valida dato y tipo del mismo.
//Funciones flechas:
console.log(numero1 > numero2); //true (Mayor que)
console.log(numero1 < 20); //false (Menor que)
console.log(numero1 >= 20); //true (Mayor o igual)
console.log(numero1 >= 20); //true (Mayor o igual)

//Operadores de Asignación:
console.log((numero1 += numero2)); //Suma y asigna
console.log((numero1 -= numero2)); //Resta y asigna
console.log((numero1 *= numero2)); //Multiplica y asigna
console.log((numero1 /= numero2)); //Divide y asigna
console.log((numero1 %= numero2)); //Modula (resto entero) y asigna
console.log((numero1 **= numero2)); //Exponencia y asigna

//Operadores Lógicos:
console.log(20 > 10 && 10 > 5); //"&&" devuelve true si ambos operandos son true.
console.log(true && true);
console.log(true && false); //de lo contrario, devuelve false.
console.log(false && false);

console.log(30 >= 10 || 10 > 30); //"||" devuelve true si al menos uno de los operandos es true.
console.log(true || true);
console.log(false || false);
console.log(true || false);

console.log(!true); //Operador "!" para negar un valor booleano.
console.log(!false);
console.log(!(40 > 30));
console.log(!(40 < 30));

//Operador Ternario (Condicional):

let edad = 12;
let GrupoEtario = edad >= 18 ? "Mayor de Edad" : "Menor de edad";
console.log(GrupoEtario);

/*- Utilizando las operaciones con operadores que tú quieras, crea ejemplos
    que representen todos los tipos de estructuras de control que existan
    en tu lenguaje:
    Condicionales, iterativas, excepciones... */
/*- Debes hacer print por consola del resultado de todos los ejemplos.*/

//Expresiones condicionales:
//if.
if (edad >= 18) {
  console.log("Mayor de edad");
}

//if else.
if (edad >= 18) {
  console.log("Mayor de edad");
} else {
  console.log("Menor de edad");
}

//else if.
if (edad >= 12 && edad < 18) {
  console.log("Púber");
} else if (edad >= 18 && edad <= 21) {
  console.log("Adolescente");
} else if (edad > 21 && edad <= 30) {
  console.log("Adulto joven");
} else if (edad > 30 && edad <= 50) {
  console.log("Adulto");
} else {
  console.log("Adulto Mayor");
}

  //Switch Statement:
  switch (edad) {
    case edad >= 1 && edad <= 11:
      console.log("Niño/a");
      break;
    case edad >= 12 && edad < 18:
      console.log("Púber");
      break;
    case edad >= 18 && edad < 21:
      console.log("Adolescente");
      break;
    case edad >= 21 && edad < 30:
      console.log("Adulto joven");
      break;
    case edad >= 30 && edad <= 50:
      console.log("Adulto");
      break;
    default:
      console.log("Adulto mayor");
      break;
  }

/*-    DIFICULTAD EXTRA (opcional):
   Crea un programa que imprima por consola todos los números comprendidos
   entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
  
   Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.*/


for (let i = 10; i <=55; i++) {
  if (i % 2 === 0 && i !== 16 && i % 3 !== 0) {
    console.log(i)
  }
  
}

