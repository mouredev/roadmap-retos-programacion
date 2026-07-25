// 1. Operadores

// Operadores Aritméticos
let suma = 5 + 5;
let resta = 5 - 5;
let multiplicacion = 5 * 5;
let division = 5 / 5;
let módulo = 5 % 5;
let potencia = 5 ** 6;
console.log("suma; " + suma);
console.log("resta: " + resta);
console.log("multiplicacion: " + multiplicacion);
console.log("division: " + division);
console.log("módulo: " + módulo);
console.log("potencia: " + potencia);

// Operadores Lógicos
let and = true && true;
let or = true || false;
let not = !true;
console.log("and: " + and);
console.log("or: " + or);
console.log("not: " + not);

// Operadores de Comparación
let igual = 5 == 5;
let diferente = 5 != 5;
let mayor = 5 > 5;
let menor = 5 < 5;
let mayorIgual = 5 >= 5;
let menorIgual = 5 <= 5;
console.log("igual: " + igual);
console.log("diferente: " + diferente);
console.log("mayor: " + mayor);
console.log("menor: " + menor);
console.log("mayorIgual: " + mayorIgual);
console.log("menorIgual: " + menorIgual);

// Operadores de Asignación
let asignacion = 5;
let asignacionSuma = asignacion += 5;
let asignacionResta = asignacion -= 5;
let asignacionMultiplicacion = asignacion *= 5;
let asignacionDivision = asignacion /= 5;
let asignacionMódulo = asignacion %= 5;
let asignacionPotencia = asignacion **= 5;
console.log("asignacion: " + asignacion);
console.log("asignacionSuma: " + asignacionSuma);
console.log("asignacionResta: " + asignacionResta);
console.log("asignacionMultiplicacion: " + asignacionMultiplicacion);
console.log("asignacionDivision: " + asignacionDivision);
console.log("asignacionMódulo: " + asignacionMódulo);
console.log("asignacionPotencia: " + asignacionPotencia);

// Operadores de Identidad
let igualDiferente = 5 == "5"; // true: solo compara el valor
let igualIdentidad = 5 === "5"; // false: compara tanto el valor como el tipo de dato
let diferenteIdentidad = 5 !== "5";
console.log("igualIdentidad: " + igualIdentidad);
console.log("diferenteIdentidad: " + diferenteIdentidad);
console.log("igualDiferente: " + igualDiferente);

// Operadores de Pertenencia
let cadena = "Hola Mundo";
let pertenece = cadena.includes("Mundo");
console.log("pertenece: " + pertenece);
console.log("includes: " + cadena.includes("Mundo"));

// Operadores de Bits
let bitAnd = 5 & 3;
let bitOr = 5 | 3;
let bitXor = 5 ^ 3;
let bitNot = ~5;
let bitLeftShift = 5 << 2;
let bitRightShift = 5 >> 2;
let bitUnsignedRightShift = 5 >>> 2;
console.log("bitAnd: " + bitAnd);
console.log("bitOr: " + bitOr);
console.log("bitXor: " + bitXor);
console.log("bitNot: " + bitNot);
console.log("bitLeftShift: " + bitLeftShift);
console.log("bitRightShift: " + bitRightShift);
console.log("bitUnsignedRightShift: " + bitUnsignedRightShift);

// 2. Estructuras de control

// 2.1 Condicionales: Estas estructuras de control permiten ejecutar un bloque de código
// en función de la evaluación de una condición.

// IF/ELSE: Usa if/else para condiciones simples o multiples caminos claros.
let condicion = true;
if (condicion) {
  console.log("Condición verdadera");
} else {
  console.log("Condición falsa");
}

let numero = 10;
if (numero > 0) {
  console.log("El número es positivo");
} else if (numero < 0) {
  console.log("El número es negativo");
} else {
  console.log("El número es cero");
}

// SWITCH: Usa switch para condiciones múltiples en una unica entidad con varios valores posibles.
// siempre usar break para finalizar cada caso de un switch.
// Usar default para cualquier valor no contemplado en los casos. 
let color = "red";
switch(color) {
    case "red":
        console.log("El color es rojo")
        break
    case "blue":
        console.log("El color es azul")
        break
    case "green":
        console.log("El color es verde")
        break
    default:
        console.log("El color no es rojo, azul o verde")
        break
}



// 2.2 Iterativas: Estas estructuras de control permiten ejecutar un bloque de código
// mientras se cumpla una condición.


// Ciclo FOR: Se usa cuando se conoce el número de iteraciones que se van a realizar.
for (let i = 0; i < 5; i++) {
    console.log("Iteración " + i);
}

// Ciclo WHILE: Se usa cuando no se conoce el número de iteraciones que se van a realizar.
let contador = 0;
while (contador < 5) {
    console.log("Iteración " + contador);
    contador++;
}

// Ciclo DO WHILE: Se usa cuando se conoce el número de iteraciones que se van a realizar y es necesario ejecutar la iteracion al menos una vez.
let contador2 = 0;
do {
    console.log("Iteración " + contador2);
    contador2++;
} while (contador2 < 5);

// 2.3 Excepciones: Estas estructuras de control permiten manejar errores en el código.

// DIFICULTAD EXTRA (opcional):
// Crea un programa que imprima por consola todos los números comprendidos
// entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.

for (let i = 10; i <= 55; i++) {
    if (i % 2 === 0 && i !== 16 && i % 3 !== 0) {
        console.log(i)
    }
}