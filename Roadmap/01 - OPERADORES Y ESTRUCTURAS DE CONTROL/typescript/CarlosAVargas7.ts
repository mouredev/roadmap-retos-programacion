/* EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje: Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 */

//! 1. Tipos de Operadores

//* a) Operadores Aritméticos
// Los operadores aritméticos realizan cálculos matemáticos como suma, resta, multiplicación, etc.
let a: number = 10;
let b: number = 5;
console.log("Suma:", a + b); // 15
console.log("Resta:", a - b); // 5
console.log("Multiplicación:", a * b); // 50
console.log("División:", a / b); // 2
console.log("Módulo:", a % b); // 0
console.log("Potencia:", a ** b); // 100000
console.log("Incremento:", ++a); // 11 (pre-incremento, muestra el valor actualizado)
console.log("Decremento:", --b); // 4 (pre-decremento, muestra el valor actualizado)

//* b) Operadores de Comparación
// Los operadores de comparación evalúan si una condición es verdadera o falsa, comparando valores.
a = 10; // Reiniciar
b = 5; // Reiniciar
console.log("Igualdad:", a == b); // false
console.log("Desigualdad:", a != b); // true
console.log("Igualdad estricta:", a === b); // false
console.log("Desigualdad estricta:", a !== b); // true
console.log("Mayor que:", a > b); // true
console.log("Menor que:", a < b); // false
console.log("Mayor o igual que:", a >= b); // true
console.log("Menor o igual que:", a <= b); // false

//* c) Operadores Lógicos
// Los operadores lógicos combinan condiciones booleanas para tomar decisiones.
let e: boolean = true;
let f: boolean = false;
console.log("AND lógico:", e && f); // false
console.log("OR lógico:", e || f); // true
console.log("NOT lógico:", !e); // false

//* d) Operadores de Asignación
// Los operadores de asignación asignan valores a variables, a menudo combinando operaciones aritméticas.
let g: number = 10;
let h: number = 5;
console.log("Asignación simple:", (g = h)); // 5
g = 10; // Reiniciar
console.log("Suma y asignación:", (g += h)); // 15
g = 10; // Reiniciar
console.log("Resta y asignación:", (g -= h)); // 5
g = 10; // Reiniciar
console.log("Multiplicación y asignación:", (g *= h)); // 50
g = 50; // Reiniciar
console.log("División y asignación:", (g /= h)); // 10
g = 10; // Reiniciar
console.log("Módulo y asignación:", (g %= h)); // 0
g = 10; // Reiniciar
console.log("Potencia y asignación:", (g **= h)); // 100000

//* e) Operadores Bit a Bit
// Los operadores bit a bit operan sobre los bits de números enteros, útiles para operaciones a bajo nivel.
let i: number = 5; // 0101 en binario
let j: number = 3; // 0011 en binario
console.log("AND bit a bit:", i & j); // 1 (0101 & 0011 = 0001)
console.log("OR bit a bit:", i | j); // 7 (0101 | 0011 = 0111)
console.log("XOR bit a bit:", i ^ j); // 6 (0101 ^ 0011 = 0110)
console.log("NOT bit a bit:", ~i); // -6 (invierte los bits de 0101)
console.log("Desplazamiento a la izquierda:", i << j); // 40 (0101 << 3 = 101000)
console.log("Desplazamiento a la derecha:", i >> j); // 0 (0101 >> 3 = 0000)
console.log("Desplazamiento a la derecha sin signo:", i >>> j); // 0 (similar a >> para números positivos)

//* f) Operadores de Tipo
// Los operadores de tipo son específicos de TypeScript y ayudan a manejar el sistema de tipos.
class Animal {
    nombre: string;
    constructor(nombre: string) {
        this.nombre = nombre;
    }
}
class Perro extends Animal {
    ladra: boolean;
    constructor(nombre: string, ladra: boolean) {
        super(nombre);
        this.ladra = ladra;
    }
}
// `as` (Type Assertion): Fuerza un tipo específico cuando sabemos que es seguro
let valor: string = "Hola TypeScript";
let texto: string = valor as string;
console.log("Type Assertion (as):", texto); // Hola TypeScript

// `is` (Type Guard): Verifica si un objeto pertenece a un tipo específico
function esPerro(animal: Animal): animal is Perro {
    return (animal as Perro).ladra !== undefined;
}
let miMascota: Animal = new Perro("Firulais", true);
console.log("Type Guard (is):", esPerro(miMascota)); // true

// `!` (Non-null Assertion): Indica que una variable no es null ni undefined
let elemento: string | null = "texto";
let seguroElemento: string = elemento!;
console.log("Non-null Assertion (!):", seguroElemento); // texto

// `typeof`: Devuelve el tipo de datos de una variable
console.log("typeof:", typeof texto); // string

// `instanceof`: Verifica si un objeto es instancia de una clase específica
console.log("instanceof Perro:", miMascota instanceof Perro); // true
console.log("instanceof Animal:", miMascota instanceof Animal); // true

//* g) Operadores Ternarios
// El operador ternario ofrece una forma compacta de tomar decisiones condicionales.
let m: number = 10;
let n: number = 5;
console.log("Ternario:", m > n ? "m es mayor que n" : "m no es mayor que n"); // m es mayor que n

//* h) Operadores Opcionales
// Los operadores opcionales manejan valores que podrían ser null o undefined de forma segura.
let o: { name: string; age?: number } = { name: "Carlos" };
console.log("Optional Chaining (?.):", o?.name); // Carlos
console.log("Optional Chaining (?.):", o?.age); // undefined
console.log("Nullish Coalescing (??):", o?.age ?? 0); // 0

//! 2. Estructuras de Control

//* 1. Condicionales
// Las estructuras condicionales ejecutan código según el cumplimiento de una condición.
let age: number = 18;
console.log("If:");
if (age >= 18) {
    console.log("Eres mayor de edad"); // Eres mayor de edad
} else if (age >= 13) {
    console.log("Eres adolescente");
} else {
    console.log("Eres menor de edad");
}
console.log("Switch:");
switch (age) {
    case 18:
        console.log("Eres mayor de edad"); // Eres mayor de edad
        break;
    case 13:
        console.log("Eres adolescente");
        break;
    default:
        console.log("Edad no clasificada");
        break;
}

//* 2. Estructuras de Bucles
// Los bucles permiten repetir un bloque de código múltiples veces según una condición.
console.log("for:");
for (let i: number = 0; i < 5; i++) {
    console.log("Iteración:", i); // 0, 1, 2, 3, 4
}
console.log("for...of:");
let array: number[] = [1, 2, 3, 4, 5];
for (let i of array) {
    console.log("Elemento:", i); // 1, 2, 3, 4, 5
}
console.log("for...in:");
let object: { [key: string]: any } = { name: "Carlos", age: 18 };
for (let i in object) {
    console.log("Propiedad:", i, "Valor:", object[i]); // name Carlos, age 18
}
console.log("while:");
age = 15; // Reiniciar para mostrar el bucle
while (age < 18) {
    console.log("Eres menor de edad"); // Imprime 3 veces
    age++;
}
console.log("do...while:");
let x: number = 0;
do {
    console.log("Iteración:", x); // 0, 1, 2, 3, 4
    x++;
} while (x < 5);

//* 3. Excepciones
// Las estructuras de excepciones manejan errores para evitar que el programa falle.
console.log("try...catch:");
try {
    let valor: string | null = "hola";
    if (typeof valor !== "string") {
        throw new Error("El valor no es un string");
    }
    console.log("Resultado:", valor.toUpperCase()); // HOLA
} catch (error: any) {
    console.log("Error capturado:", error.message);
}
console.log("try...catch...finally:");
try {
    let num: number | undefined = undefined;
    if (num === undefined) {
        throw new Error("Número no definido");
    }
    console.log("Dividiendo:", num / 0);
} catch (error: any) {
    console.log("Error capturado:", error.message); // Número no definido
} finally {
    console.log("Esto se ejecuta siempre"); // Esto se ejecuta siempre
}

//* 4. Control de Flujo
// Los mecanismos de control de flujo modifican la ejecución dentro de bucles o funciones.
console.log("break:");
for (let i: number = 0; i < 10; i++) {
    if (i === 5) {
        console.log("Bucle terminado en i =", i); // Bucle terminado en i = 5
        break;
    }
    console.log("Iteración:", i); // 0, 1, 2, 3, 4
}
console.log("continue:");
for (let i: number = 0; i < 10; i++) {
    if (i === 5) {
        console.log("Saltando i =", i); // Saltando i = 5
        continue;
    }
    console.log("Iteración:", i); // 0, 1, 2, 3, 4, 6, 7, 8, 9
}
console.log("return:");
function suma(a: number, b: number): number {
    if (a < 0 || b < 0) {
        console.log("Números negativos no permitidos");
        return 0;
    }
    return a + b;
}
console.log("Suma válida:", suma(1, 2)); // 3
console.log("Suma con negativo:", suma(-1, 2)); // Números negativos no permitidos, 0


/* DIFICULTAD EXTRA (opcional):
 *-Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 *-Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
*/

let z: number = 10
while (z <= 55) {
    if (z % 2 === 0)
        if (z !== 16)

            console.log(z)
    z++
}