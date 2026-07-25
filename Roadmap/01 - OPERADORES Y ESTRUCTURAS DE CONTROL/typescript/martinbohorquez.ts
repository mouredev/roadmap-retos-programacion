/*
    Operadores aritméticos: actúan sobre números enteros y en punto flotante (decimales).
    Hay dos tipos:
        -- Operadores binarios.
        -- Operadores unarios.
    */

/*
    * Operadores unarios: aplican a un operando.
    * Tipos:
    *      -- Mantiene el signo del operando (+)
    *      -- Cambia el signo del operando (-)
    *      -- Autoincremento (++)
    *      -- Autodecremento (--)
    */

let a: number = 10;

console.log("Operadores unarios: aplican a un operando.");

console.log("Mantiene el signo: " + (+a));
console.log("Cambia el signo: " + (-a));
console.log("Autoincremento e impresión: " + (++a)); //Se incrementa y se imprime
console.log("Impresión y autoincremento: " + (a++)); //Se imprime y se incrementa
console.log("Autodecremento e impresión: " + (--a)); //Se decrementa y se imprime
console.log("Impresión y autodecremento: " + (a--)); //Se imprime y se decrementa

console.log("");

/*
    * Operadores binarios: aplican sobre dos operandos.
    * Tipos:
    *       -- Suma (+)
    *       -- Resta (-)
    *       -- Multiplicación (*)
    *       -- División (/)
    *       -- Módulo (%)
    */

const b: number = 5;
const c: number = 2;

console.log("Operadores binarios: aplican sobre dos operandos: ");

console.log("Suma: " + b + " + " +  c + " = " + (b + c));
console.log("Resta: " + b + " - " +  c + " = " + (b - c));
console.log("Multiplicación: " + b + " * " +  c + " = " + (b * c));
console.log("División: " + b + " / " +  c + " = " + (b / c));
console.log("Módulo: " + b + " % " +  c + " = " + (b % c));

console.log("");

/*
    * Operadores relacionales: para hacer comparaciones.
    * Tipos:
    *      -- Mayor que (>)
    *      -- Mayor o igual que (>=)
    *      -- Menor que (<)
    *      -- Menor o igual que (<=)
    *      -- Igual que (==)
    *      -- Distinto de (!=)
    */

const d: number = 20;
const e: number = 50;

console.log("Operadores relacionales: para hacer comparaciones.");

console.log("¿20 es mayor que 50? : " + (d > e));
console.log("¿20 es mayor o igual que 50? : " + (d >= e));
console.log("¿20 es menor que 50? : " + (d < e));
console.log("¿20 es menor o igual que 50? : " + (d <= e));
console.log("¿20 es igual que 50? : " + (d == e));
console.log("¿20 es distinto de 50? : " + (d != e));

console.log("");

/*
    * Operadores lógicos: Operan con valores lógicos para devolver nuevos valores lógicos.
    * Tipos:
    *      -- AND (&&): Evalúa si las dos expresiones son verdaderas.
    *      -- OR (||): Evalúa si alguna de las expresiones es verdadera.
    *      -- NOT (!): Cambia el valor de la variable lógica.
    */

const v: boolean = true;
const f: boolean = false;

console.log("Operadores lógicos: Operan con valores lógicos para devolver nuevos valores lógicos.");

console.log("¿true es igual a false? : " + (v && f));
console.log("¿true o false son verdaderas? : " + (v || f));
console.log("Cambiamos el valor de true : " + (!v));

console.log("");

/*
    * Operador sobre cadenas de caracteres (+): Para concatenar cadenas de caracteres.
    */

const text1: string = "¡Hola, "
const text2: string = "TypeScript!"

console.log("Operador sobre cadenas de caracteres:");

console.log(text1 + text2);

console.log("");

/*
    * Operadores de asignación: Para asignar un valor a una variable.
    * Tipos:
    *      -- +=: Suma a la variable y sobrescribe el valor de la variable con el resultado.
    *      -- -=: Resta a la variable y sobrescribe el valor de la variable con el resultado.
    *      -- *=: Multiplica a la variable y sobrescribe el valor de la variable con el resultado.
    *      -- /=: Divide a la variable y sobrescribe el valor de la variable con el resultado.
    *      -- %=: Realiza el módulo a la variable y sobrescribe el valor de la variable con el resultado.
    *      -- *=: Potencia a la variable y sobrescribe el valor de la variable con el resultado.
    *      -- &&=: Realiza un AND lógico a la variable y sobrescribe el valor de la variable con el resultado.
    *      -- ||=: Realiza un OR lógico a la variable y sobrescribe el valor de la variable con el resultado.
    */

let i: number;
let t: boolean = true;

console.log("Operadores de asignación: Para asignar un valor a una variable.");

console.log("Asignamos valor a la variable i = " + (i = 2));
console.log("Suma y asigna: " + (i += 4));
console.log("Resta y asigna: " + (i -= 3));
console.log("Multiplica y asigna: " + (i *= 5));
console.log("Divide y asigna: " + (i /= 3));
console.log("Módulo y asigna: " + (i %= 3));
console.log("Potencia y asigna: " + (i **= 3));
console.log("AND lógico y asigna: " + (t &&= true));
console.log("OR lógico y asigna: " + (t ||= false));

console.log("");

/*
    * Operadores a nivel de bits: operan con cada bit del operando, ofreciendo un control más granular sobre los datos.
    * Tipos:
    *      -- AND (&): Operador AND a nivel de bits (1 y 1 = 1).
    *      -- OR (|): Operador OR a nivel de bits (1 o 1 = 1).
    *      -- XOR (^): Operador XOR a nivel de bits (1 y 1 = 0).
    *      -- Complemento (~): Invierte el valor de cada bit.
    *      -- >> : Desplaza bits a la derecha.
    *      -- << : Desplaza bits a la izquierda.
    *      -- >>> : Desplaza bits a la derecha sin signo.
    */

const x: number = 10; // 1010
const y: number = 7; // 0111

console.info("Operadores a nivel de bits: operan con cada bit del operando, ofreciendo un control más granular sobre los datos.");

console.log("x AND y : " + (x & y));
console.log("x OR y : " + (x | y));
console.log("x XOR y : " + (x ^ y));
console.log("Complemento de x = " +  + ~x);
console.log("Complemento de y = " +  + ~y);
console.log("Desplazamiento de bits de x a la izquierda de 2: " + (x << 2)); 
console.log("Desplazamiento de bits de y a la derecha de 1: " + (y >> 1)); 
console.log("Desplazamiento de bits de y a la derecha de 1 (sin signo): " + (y >>> 1));

console.log("");

/*
    * Excepciones
    * uso del try - catch
    */ 
try {
throw new Error('Este es un ejemplo de excepción.');
} catch (error) {
console.error('Excepción:', (error as Error).message);
}

console.log("");


/*
    * Crea un programa que imprima por consola todos los números comprendidos
    * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
    */

console.log("DIFICULTAD EXTRA \n");

console.log("Los números son: ");

for (let j: number = 10; j <= 55; j++) {
    //Compruebo si son pares, distintos de 16 y no son múltiplos de 3
    if (j % 2 == 0 && j != 16 && j % 3 != 0) {
        console.log(j);
    }
}