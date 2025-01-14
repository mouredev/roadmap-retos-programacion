// Operadores ----------------------------------------

// Operadores Aritméticos
let a = 10, b = 3;
console.log("Suma:", a + b);
console.log("Resta:", a - b);
console.log("Multiplicación:", a * b);
console.log("División:", a / b);
console.log("Módulo:", a % b);
console.log("Potenciación:", a ** b);

// Operadores de Comparación
console.log("Mayor que:", a > b);
console.log("Menor o igual:", a <= b);
console.log("Igualdad estricta:", a === b);
console.log("Desigualdad estricta:", a !== b);

// Operadores Lógicos
let x = true, y = false;
console.log("AND:", x && y);
console.log("OR:", x || y);
console.log("NOT:", !x);

// Operadores de Asignación
let c = 5;
c += 2; // c = c + 2
console.log("Asignación Suma:", c);
c *= 3; // c = c * 3
console.log("Asignación Multiplicación:", c);

// Operadores de Identidad (strict equality)
let d = "10";
console.log("Igualdad estricta:", a === d); // Compara valor y tipo
console.log("Igualdad no estricta:", a == d); // Compara solo valor

// Operadores de Pertenencia
let arr = [1, 2, 3];
console.log("Elemento en array (2):", arr.includes(2));

// Operadores a Nivel de Bits
let e = 5, f = 1; // e = 0101, f = 0001 en binario
console.log("AND a nivel de bits:", e & f); // 0001
console.log("OR a nivel de bits:", e | f); // 0101
console.log("XOR a nivel de bits:", e ^ f); // 0100
console.log("Desplazamiento a la izquierda:", e << 1); // 1010
console.log("Desplazamiento a la derecha:", e >> 1); // 0010


// Estructuras de control ----------------------------------------

// Condicionales
let age = 18;
if (age >= 18) {
    console.log("Eres mayor de edad.");
} else {
    console.log("Eres menor de edad.");
}

// Iterativas (for, while, do-while)
console.log("Bucle for:");
for (let i = 0; i < 5; i++) {
    console.log("i =", i);
}

console.log("Bucle while:");
let count = 3;
while (count > 0) {
    console.log("count =", count);
    count--;
}

console.log("Bucle do-while:");
let num = 0;
do {
    console.log("num =", num);
    num++;
} while (num < 3);

// Excepciones
try {
    console.log("Intentando dividir por cero...");
    let result = 10 / 0;
    if (!isFinite(result)) throw new Error("División por cero no permitida.");
    console.log("Resultado:", result);
} catch (error) {
    console.log("Error:", error.message);
} finally {
    console.log("Bloque finally ejecutado.");
}

// Ejercicio Extra --------------------------------------------------------
for (let i = 10; i < 56; i++) {
    if (i % 2 == 0 && i != 16 && i % 3 != 0) {
        console.log(i);
    }
}