// Operadores 

var numero1 = 10;
var letraNumero = "10";
var numero2 = 20;
var numero3 = 10;

console.log("--- Operadores de comparación e igualdad ---");
console.log("Igualdad (10 == \"10\"): ", numero1 == letraNumero);
console.log("Desigualdad (10 != 20): ", numero1 != numero2);
console.log("Estrictamente igual (10 === \"10\"): ", numero1 === letraNumero);
console.log("Estrictamente desigual (10 !== \"10\"): ", numero1 !== letraNumero);
console.log("Mayor que (20 > 10): ", numero2 > numero1);
console.log("Menor que (10 < 20): ", numero1 < numero2);
console.log("Mayor o igual que (10 >= 10): ", numero1 >= numero3);
console.log("Menor o igual que (10 <= 20): ", numero1 <= numero2);

console.log("\n--- Operadores aritméticos ---");
var x = 2;
console.log("Suma (10 + 20): ", numero1 + numero2);
console.log("Resta (20 - 10): ", numero2 - numero1);
console.log("Multiplicación (10 * 2): ", numero1 * x);
console.log("División (20 / 2): ", numero2 / x);
console.log("Residuo / Módulo (20 % 5): ", 20 % 5);
console.log("Incremento posterior (x = 2; x++): ", x++);
console.log("Decremento posterior (x = 3; x--): ", x--);
console.log("Negación unaria (-x): ", -x);
console.log("Positivo unario (+letraNumero): ", +letraNumero);
console.log("Exponenciación (2 ** 3): ", 2 ** 3);

console.log("\n--- Operadores bit a bit ---");
console.log("AND bit a bit (10 & 20): ", 10 & 20);
console.log("OR bit a bit (10 | 20): ", 10 | 20);
console.log("XOR bit a bit (10 ^ 20): ", 10 ^ 20);
console.log("NOT bit a bit (~10): ", ~10);
console.log("NOT bit a bit (~20): ", ~20);
console.log("Desplazamiento a la izquierda (10 << 2): ", 10 << 2);
console.log("Desplazamiento a la derecha (10 >> 2): ", 10 >> 2);
console.log("Desplazamiento a la derecha con relleno de ceros (10 >>> 2): ", 10 >>> 2);

console.log("\n--- Operadores lógicos ---");
console.log("AND lógico (true && false): ", (10 < 20) && (10 > 50));
console.log("OR lógico (false || true): ", (10 > 20) || (10 === 10));
console.log("NOT lógico (!true): ", !true);
console.log("Nullish Coalescing (null ?? 'valor por defecto'): ", null ?? "valor por defecto");

console.log("\n--- Operador ternario ---");
var edad = 18;
console.log("¿Puedo votar?: ", edad >= 18 ? "Sí puedo votar" : "No puedo votar");

console.log("\n--- Operadores de cadena ---");
console.log("Concatenación (+): ", "Hola " + "Mundo");
var palabra1 = "mi";
palabra1 += "guel";
console.log("Concatenación y asignación (+=): ", palabra1);

console.log("\n--- Operadores de tipo y pertenencia ---");
var numero = 10;
var myFun = new Function("5 + 2");
var lista = [1, 2, 3];
var objeto = { nombre: "Miguel" };
console.log("typeof numero: ", typeof numero);
console.log("typeof myFun: ", typeof myFun);
console.log("instanceof (lista instanceof Array): ", lista instanceof Array);
console.log("in ('nombre' in objeto): ", "nombre" in objeto);

console.log("\n--- Operadores de asignación ---");
var a = 10;
var b = 20;
console.log("Asignación (=): ", a = 10);
console.log("Suma y asignación (+=): ", b += 20);
console.log("Resta y asignación (-=): ", a -= 5);
console.log("Multiplicación y asignación (*=): ", b *= 2);
console.log("División y asignación (/=): ", a /= 5);
console.log("Residuo y asignación (%=): ", b %= 7);
console.log("Exponenciación y asignación (**=): ", a **= 3);
console.log("Desplazamiento a la izquierda y asignación (<<=): ", b <<= 2);
console.log("Desplazamiento a la derecha y asignación (>>=): ", a >>= 1);
console.log("Desplazamiento a la derecha sin signo y asignación (>>>=): ", b >>>= 1);
console.log("AND bit a bit y asignación (&=): ", a &= 3);
console.log("OR bit a bit y asignación (|=): ", b |= 2);
console.log("XOR bit a bit y asignación (^=): ", a ^= 1);


console.log("\n==========================================");
console.log("         ESTRUCTURAS DE CONTROL           ");
console.log("==========================================");

// 1. Condicionales 
console.log("\n--- Condicionales: if, else if, else ---");
var puntuacion = 85;
if (puntuacion >= 90) {
    console.log("Excelente");
} else if (puntuacion >= 70) {
    console.log("Aprobado");
} else {
    console.log("Reprobado");
}

console.log("\n--- Condicional: switch ---");
var dia = "viernes";
switch (dia.toLowerCase()) {
    case "lunes":
        console.log("Es lunes");
        break;
    case "martes":
        console.log("Es martes");
        break;
    case "miercoles":
    case "miércoles":
        console.log("Es miércoles");
        break;
    case "jueves":
        console.log("Es jueves");
        break;
    case "viernes":
        console.log("Es viernes");
        break;
    case "sabado":
    case "sábado":
        console.log("Es sábado");
        break;
    case "domingo":
        console.log("Es domingo");
        break;
    default:
        console.log("No es un día válido");
}

// 2. Iterativas (Bucles)
console.log("\n--- Bucle: for ---");
for (var i = 1; i <= 3; i++) {
    console.log("Iteración for: " + i);
}

console.log("\n--- Bucle: while ---");
var miEdad = 27;
var meta = 30;
while (miEdad < meta) {
    miEdad++;
    console.log("Cumpliendo año: " + miEdad);
}

console.log("\n--- Bucle: do while ---");
var contadorDo = 0;
do {
    console.log("Ejecutando do...while, contador: " + contadorDo);
    contadorDo++;
} while (contadorDo < 2);

console.log("\n--- Bucle: for...in (propiedades de un objeto) ---");
var persona = { nombre: "Miguel", rol: "Desarrollador" };
for (var propiedad in persona) {
    console.log(propiedad + ": " + persona[propiedad]);
}

console.log("\n--- Bucle: for...of (elementos iterables) ---");
var lenguajes = ["JavaScript", "Python", "TypeScript"];
for (var lenguaje of lenguajes) {
    console.log("Lenguaje: " + lenguaje);
}

// 3. Control de salto: break y continue
console.log("\n--- Control de salto: break ---");
for (var j = 1; j <= 5; j++) {
    if (j === 3) {
        console.log("Rompiendo bucle en j = " + j);
        break;
    }
    console.log("j = " + j);
}

console.log("\n--- Control de salto: continue ---");
for (var k = 1; k <= 5; k++) {
    if (k === 3) {
        console.log("Saltando iteración k = " + k);
        continue;
    }
    console.log("k = " + k);
}

// 4. Manejo de Excepciones
console.log("\n--- Manejo de excepciones: try...catch...finally ---");
try {
    console.log("Intentando ejecutar código...");
    var resultado = 10 / 2;
    console.log("Resultado: " + resultado);
    // Provocar error controlado
    throw new Error("Este es un error personalizado de prueba");
} catch (error) {
    console.log("Error capturado: " + error.message);
} finally {
    console.log("Bloque finally ejecutado siempre al terminar");
}


// DIFICULTAD EXTRA
console.log("\n==========================================");
console.log("            DIFICULTAD EXTRA              ");
console.log("==========================================");
console.log("Números comprendidos entre 10 y 55 (incluidos), pares, que no son ni el 16 ni múltiplos de 3:");

for (var num = 10; num <= 55; num++) {
    if (num === 16 || num % 3 === 0) {
        continue;
    }

    if (num % 2 === 0) {
        console.log(num);
    }
}