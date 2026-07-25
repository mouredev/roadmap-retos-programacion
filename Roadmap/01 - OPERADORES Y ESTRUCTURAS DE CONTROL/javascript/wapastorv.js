/*
# #01 OPERADORES Y ESTRUCTURAS DE CONTROL
> #### Dificultad: Fácil | Publicación: 02/01/24 | Corrección: 08/01/24

## Ejercicio  
*
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

// Tipo de Operadores en JavaScript

// Operador Aritméticos
console.log(2 + 2); // Suma
console.log(2 - 2); // Resta
console.log(2 * 2); // Multiplicación
console.log(2 / 2); // División
console.log(2 % 2); // Módulo, que es el resto de la división
console.log(2 ** 2); // Exponenciación
let x = 5;
console.log(x++); // Incremento
console.log(x--); // Decremento


// Operador Lógicos
console.log(true && true); // AND, devuelve true si ambos son true; ejemplos (5 > 2 && 2 > 1) // true
console.log(true || false); // OR, devuelve true si uno de los dos es true; ejemplos (5 > 2 || 2 > 5) // true
console.log(!true); // NOT, invierte el valor; ejemplos (!true) o !(5 > 3)// false

// Operador de comparación
console.log(2 > 2); // Mayor que
console.log(2 < 2); // Menor que
console.log(2 >= 2); // Mayor o igual que
console.log(2 <= 2); // Menor o igual que
console.log(2 == 2); // Igualdad que (no estricto)
console.log(2 != 2); // Desigualdad que (no estricto)
console,log(2 !== 2); // Desigualdad que (estricto)
console.log(2 === 2); // Igualdad (estricto)

// Operador de asignación
let a = 2; // Asignación un valor a una variable
console.log(a); // 2
a += 2; // Suma y asignación
console.log(a); // 4
a -= 2; // Resta y asignación
console.log(a); // 2
a *= 2; // Multiplicación y asignación
console.log(a); // 4
a /= 2; // División y asignación
console.log(a);// 2
a %= 2; // Módulo y asignación
console.log(a); // 0
a **= 2; // Exponenciación y asignación
console.log(a); // 0


//Operador de identidad
console.log(2 === 2); // Igual que y mismo tipo (true)
console.log(2 === '2'); // Igual que y mismo tipo (false)

// Operador de pertenencia
let b = [1, 2, 3];
console.log(2 in b); // Existe en el array (true) 
console.log(4 in b); // Existe en el array (false)

// Operador de bits
console.log(2 & 2); // AND
console.log(2 | 2); // OR
console.log(2 ^ 2); // XOR
console.log(~2); // NOT
console.log(2 << 2); // Desplazamiento a la izquierda
console.log(2 >> 2); // Desplazamiento a la derecha 
console.log(2 >>> 2); // Desplazamiento a la derecha sin signo, ejemplos con números negativos

// Operador de tipo
console.log(typeof 2); // Number, devuelve el tipo de una variable


let c = new String('Hola');
console.log(c instanceof String); //instanceof, devuelve true si un objeto es una instancia de un tipo de objeto. // true

// Operador de agrupación
console.log(5 + 3) * 2; // Agrupación de operaciones

// Operador de acceso a propiedad (objeto y array)
let d = {nombre: 'Juan'};
console.log(d.nombre); // Juan, el punto se utiliza para acceder a las propiedades de un objeto

let e = [1, 2, 3];
console.log(e[0]); // 1, el corchete se utiliza para acceder a los elementos de un array

// Operador de encadenamiento opcional
let f = {nombre: 'Juan'};
console.log(f.nombre?.apellido); // undefined, si la propiedad no existe no lanza un error


// Operador de Coalescencia nula
let g = null;
console.log(g ?? 'Valor por defecto'); // Valor por defecto, si el valor es null o undefined devuelve el valor por defecto o valor de la derecha

// Operador de propagación y rest
let h = [1, 2, 3];
let i = [4, 5, 6];
console.log([...h, ...i]); // [1, 2, 3, 4, 5, 6], propagación de arrays (spread operator)

let j = [1, 2, 3];
let [k, ...l] = j;
console.log(k); // 1, rest operator (desestructuración de arrays)
console.log(l); // [2, 3], rest operator (desestructuración de arrays)


// Estructuras de control en JavaScript

// Condicionales 

    //if ; if else y if else if
    let edad = 18;
    if (edad >= 18) {
        console.log('Eres mayor de edad');
    }
    else {
        console.log('Eres menor de edad');
    }


    let dia = "lunes";
    if (dia === "lunes") {
        console.log("Hoy es lunes");
    }
    else if (dia === "martes") {
        console.log("Hoy es martes");
    }
    else {
        console.log("Hoy es otro día");
    }

    // Switch
    let fruta = "manzana";
    switch(fruta) {
      case "manzana":
        console.log("Es una manzana");
        break;
      case "pera":
        console.log("Es una pera");
        break;
      default:
        console.log("Es otra fruta");
    }

    //Ternario
    let alto = 180;
    let esAlto = alto >= 180 ? 'Eres alto' : 'No eres alto';
    console.log(esAlto); // Eres alto


    // Bucles (loops)

    // For
    for (let i = 0; i < 5; i++) {
        console.log(i); // 0, 1 
    }

    // for .. of, recorre las propiedades de un objeto iterando, como arrays o string
    let personas = ["juan", "maria", "pedro"];
    for (let persona of personas) {
        console.log(persona);  // Muestra los elementos del array, juan, maria, pedro
    }

    let saludoEspecial = "Hola Mundo, soy un saludo especial";
    for (let letra of saludoEspecial) {
        console.log(letra); // Muestra cada letra del string Hola Mundo, soy un saludo especial 
    }

    // for .. in, itera sobre las propiedades de un objeto(propiedades enumerables)
    let carro = {marca: "Toyota", modelo: "Corolla"};
    for (let propiedad in carro) {
        console.log(`${propiedad}: ${carro[propiedad]}`); // Muestra las propiedades del objeto, marca: Toyota, modelo: Corolla
    }

    /* While:
     Se ejecuta un bloque de código mientras la condición sea verdadera. Es util cuando no se sabe cuantas veces se va a ejecutar el bloque de código.
    */
    let contador = 0;
    while (contador < 5) {
        console.log(contador);   
        contador++;
    }
    /* Do While:
        Se ejecuta un bloque de código al menos una vez y luego se ejecuta mientras la condición sea verdadera.
    */
    let nuemro = 5;
    do {
        console.log(nuemro); // 5, 4, 3, 2, 1
        nuemro--;
    } while(nuemro > 0);


    // Excepciones
    
    /* Try ... Catch: 
        Se utiliza para capturar errores en un bloque de código. Si se produce un error en el bloque de código dentro del bloque try, se ejecuta el bloque catch.
    */
    try {
        let resultado = 10 / 0;
        console.log(resultado);
    } catch (error) {
        console.log("Ocurrió un error: ", error.message); // Ocurrió un error:  Cannot divide by zero
    }

    /* Finally: 
        Se ejecuta un bloque de código después de que se haya intentado ejecutar el bloque try y el bloque catch. Independientemente de si se produce un error o no.
    */
    try {
        let resultado = 10 / 2;
        console.log(resultado); // 5
    } catch (error) {
        console.log("Ocurrió un error: ", error.message);
    } finally {
        console.log("Bloque finally"); // Bloque finally
    }

    /* Throw:
        Permite lanzar una error manualmente. Se puede crear errores personalizados.
    */
    try {
        throw new Error("Error personalizado");
    } catch (error) {
        console.log("Ocurrió un error: ", error.message); // Ocurrió un error:  Error personalizado
    }


    // EJECICIO DIFICULTAD EXTRA
    for (let i = 10; i <= 55; i++) {
        if (i % 2 === 0 && i !== 16 && i % 3 !== 0) {
            console.log(i); 
        }
    }




