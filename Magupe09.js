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




// tipos de operadores

/* ARITMETICOS
    suma,
    resta,
    multiplicacion,
    division,
    modulo,
    incremento,decremento.
    exponenciacion 
  */ 


let suma = 2 + 5; // 7
console.log(suma);
let resta = 2 - 5; // -3
console.log(resta);
let multiplicacion = 2*5; // 10
console.log(multiplicacion);
let division = 2 /5;
console.log(division);
let modulo = 5 % 3; // modulo es 2
console.log(modulo);
let a = 5;
a++; // a es 6
console.log(a);
let b = 5;
b--; // b es 4
console.log(b);
let exponenciacion = 2 ** 3; // exponenciacion es 8
console.log(exponenciacion);




//  Operadores logicos  ------------- AND - OR - NOT LOGICO - NULLISH--

// AND lógico (&&): Devuelve true si ambos operandos son true

let c = true;
let d = false;
let and = c && d; // and es false
console.log(and)
// OR lógico (||): Devuelve true si al menos uno de los operandos es true.

let e = true;
let f = false;
let or = a || b; // or es true
console.log(or)
// NOT lógico (!): Invierte el valor booleano del operando.

let g = true;
let resultado = !a; // resultado es false
console.log(resultado)
// Nullish Coalescing (??): Devuelve el operando de la derecha si el operando de la izquierda es null o undefined, de lo contrario, devuelve el operando de la izquierda.

let h = null;
let i = "valor por defecto";
let resultado2 = a ?? b; // resultado2 es "valor por defecto"
console.log(resultado2)






// A NIVEL DE BITS ------------- AND A NIVEL DE BITS - OR A NIVEL DE BITS---

//AND a nivel de bits (&): Compara cada bit de sus dos operandos. Si ambos bits son 1, el bit resultante es 1. De lo contrario, el bit resultante es 0.

let j = 5;  // (en binario: 0101)
let k = 3;  // (en binario: 0011)
let resultado3 = a & b; // resultado3 es 1 (en binario: 0001)
console.log(resultado3)
// OR a nivel de bits (|): Compara cada bit de sus dos operandos. Si al menos uno de los bits es 1, el bit resultante es 1. De lo contrario, el bit resultante es 0.

let l = 5;  // (en binario: 0101)
let m = 3;  // (en binario: 0011)
let resultado4 = l | m; // resultado4 es 7 (en binario: 0111)
console.log(resultado4)





// operadores de comparacion ----- 
/* 
  igualdad,
  igualdad estricta,
  desigualdad,
  desigualdad estricta,
  mayor que ,
  menor que,
  menor o igual,
  mayor o igual
*/


// Igualdad (==): Compara dos valores para ver si son iguales, realizando conversión de tipos si es necesario.

let n = 5;
let o = "5";
console.log(n == o); // true

// Igualdad estricta (===): Compara dos valores para ver si son iguales en valor y tipo.

let p = 5;
let q = "5";
console.log(p === q); // false

// Desigualdad (!=): Compara dos valores para ver si son diferentes, realizando conversión de tipos si es necesario.

let r = 5;
let s = "5";
console.log(r != s); // false

// Desigualdad estricta (!==): Compara dos valores para ver si son diferentes en valor o tipo.


let t = 5;
let u = "5";
console.log(t !== u); // true

//Mayor que (>): Verifica si el valor de la izquierda es mayor que el de la derecha.

let v = 5;
let w = 3;
console.log(v > w); // true

//Mayor o igual que (>=): Verifica si el valor de la izquierda es mayor o igual que el de la derecha.

let x = 5;
let y = 5;
console.log(x >= y); // true


//Menor que (<): Verifica si el valor de la izquierda es menor que el de la derecha.

let z = 3;
let aa = 5;
console.log(z < aa); // true


//Menor o igual que (<=): Verifica si el valor de la izquierda es menor o igual que el de la derecha.

let bb = 5;
let cc = 5;
console.log(bb <= cc); // true





// Operadores de asignaciòn----
/*
    Asignación simple (=): Asigna el valor del operando de la derecha a la variable de la izquierda.
    Asignación de adición (+=): Suma el valor del operando de la derecha al operando de la izquierda y asigna el resultado a la variable de la izquierda.
    Asignación de sustracción (-=): Resta el valor del operando de la derecha del operando de la izquierda y asigna el resultado a la variable de la izquierda.
    Asignación de multiplicación (*=): Multiplica el valor del operando de la derecha por el operando de la izquierda y asigna el resultado a la variable de la izquierda.
    Asignación de división (/=): Divide el operando de la izquierda por el valor del operando de la derecha y asigna el resultado a la variable de la izquierda.
    Asignación de módulo (%=): Calcula el resto de dividir el operando de la izquierda por el operando de la derecha y asigna el resultado a la variable de la izquierda.
    Asignación de exponenciación (=)**: Eleva el operando de la izquierda a la potencia del operando de la derecha y asigna el resultado a la variable de la izquierda.

*/
// Asignación simple
let x1 = 10;
console.log(x1)

// Asignaciòn de adiciòn 
let x2= 10;
x2 += 5; // x2 ahora es 15
console.log(x2)

//Asignación de sustracción
let x3 = 10;
x3 -= 5; // x3 ahora es 5
console.log(x3)

//Asignación de multiplicación
let x4 = 10;
x4 *= 5; // x4 ahora es 50
console.log(x4)


//  Asignación de división 
let x5 = 10;
x5 /= 5; // x5 ahora es 2
console.log(x5)



// Asignación de módulo
let x6 = 10;
x6 %= 3; // x6 ahora es 1
console.log(x6)


//Asignación de exponenciación
let x7 = 2;
x7 **= 3; // x7 ahora es 8
console.log(x7)


// Operadores de identidad -
/* En JavaScript, los operadores de identidad se refieren principalmente a los operadores que comparan tanto el valor como el tipo de los operandos. Estos son:

   Igualdad estricta (===):
   Desigualdad estricta (!==): 
*/



// igualdad estricta
let a1 = 5;
let b1 = 5;
let c1 = "5";
console.log(a1 === b1); // true
console.log(a1 === c1); // false


//desigualdad estricta
let a2 = 5;
let b2 = 5;
let c2= "5";
console.log(a2 !== b2); // false
console.log(a2 !== c2); // true




//En JavaScript, los operadores de pertenencia se utilizan para comprobar si una propiedad o un elemento existe dentro de un objeto o una estructura de datos. Los operadores de pertenencia más comunes son:
/*
   Operador in: Este operador se utiliza para verificar si una propiedad existe en un objeto. Devuelve true si la propiedad está en el objeto especificado.
   Método hasOwnProperty: Este método se utiliza para verificar si una propiedad es una propiedad directa del objeto (no heredada). Devuelve true si la propiedad es una propiedad directa del objeto.
   Operador instanceof: Este operador se utiliza para verificar si un objeto es una instancia de una clase o de una función constructora específica. Devuelve true si el objeto es una instancia de la clase especificada.




 */

// operador in
let obj = { name: "Alice", age: 25 };
console.log("name" in obj); // true
console.log("address" in obj); // false

//Método hasOwnProperty
let obj1 = { name: "Alice", age: 25 };
console.log(obj1.hasOwnProperty("name")); // true
console.log(obj1.hasOwnProperty("toString")); // false (heredado del prototipo)

// Operador instanceof:

function Person(name) {
    this.name = name;
  }
  
  let alice = new Person("Alice");
  console.log(alice instanceof Person); // true
  console.log(alice instanceof Object); // true
  


//Estructuras de Control Condicionales
/* 
   if: Ejecuta un bloque de código si la condición especificada es verdadera.
   if...else: Ejecuta un bloque de código si la condición es verdadera y otro bloque si la condición es falsa.
   else if: Permite comprobar múltiples condiciones.
   switch: Ejecuta uno de varios bloques de código según el valor de una expresión.

 */

//if
let xy = 10;
if (xy > 5) {
  console.log("xy es mayor que 5");
}

// if...else:
let xa = 10;
if (xa > 5) {
  console.log("xa es mayor que 5");
} else {
  console.log("xa no es mayor que 5");
}


//else if: 
let xb = 10;
if (xb > 10) {
  console.log("xb es mayor que 10");
} else if (xb == 10) {
  console.log("xb es igual a 10");
} else {
  console.log("xb es menor que 10");
}

//switch:
let color = "rojo";
switch (color) {
  case "rojo":
    console.log("El color es rojo");
    break;
  case "azul":
    console.log("El color es azul");
    break;
  default:
    console.log("Color no reconocido");
}

// Estructuras de Control de Bucles
/* for: Repite un bloque de código un número específico de veces.
   while: Repite un bloque de código mientras una condición especificada sea verdadera.
   do...while: Similar a while, pero garantiza que el bloque de código se ejecute al menos una vez.
   for...in: Itera sobre las propiedades enumerables de un objeto.
   for...of: Itera sobre objetos iterables (como arrays, cadenas de texto, mapas, conjuntos, etc.).






 */

// for:
for (let ii = 0; ii < 5; ii++) {
    console.log(ii);
  }
  

//while
let i2 = 0;
while (i2 < 5) {
  console.log(i2);
  i2++;
}

//do...while:
let i3 = 0;
do {
  console.log(i3);
  i3++;
} while (i3 < 5);


//for...in: 
let obj5 = { a: 1, b: 2, c: 3 };
for (let key in obj5) {
  console.log(key + ": " + obj5[key]);
}

// for of
let arr = [1, 2, 3, 4, 5];
for (let value of arr) {
  console.log(value);
}


//Estructuras de Control de Salto
/* break: Termina el bucle actual o la declaración switch.
   continue: Salta a la siguiente iteración del bucle.
   return: Finaliza la ejecución de una función y opcionalmente devuelve un valor.
   throw: Lanza una excepción definida por el usuario.





 */

//break:
for (let i = 0; i < 10; i++) {
    if (i === 5) {
      break;
    }
    console.log(i);
  }
  

// continue
for (let i = 0; i < 10; i++) {
    if (i === 5) {
      continue;
    }
    console.log(i);
  }
  

// return
function sumaf(a, b) {
    return a + b;
  }
  console.log(sumaf(5, 3)); // 8
  
//  throw:
function verificaEdad(edad) {
    if (edad < 18) {
      throw new Error("No permitido para menores de edad");
    }
    return "Acceso permitido";
  }
  
  try {
    console.log(verificaEdad(15));
  } catch (error) {
    console.log(error.message); // No permitido para menores de edad
  }


//  ---------------------- Plus 

/*
  DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
*/

for(let i=10 ; i<=55;i++){
    if(i % 2 === 0 && i !== 16 && i % 3 !==0 ){
        console.log(i);
    }
}