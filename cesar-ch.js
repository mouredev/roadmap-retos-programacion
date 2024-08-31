// Operadores Aritméticos
let a = 5;
let b = 2;
console.log("Suma:", a + b);
console.log("Resta:", a - b);
console.log("Multiplicación:", a * b);
console.log("División:", a / b);
console.log("Módulo:", a % b);
console.log("Incremento:", ++a);
console.log("Decremento:", --b);

// Operadores de Comparación
let x = 10;
let y = "10";
console.log("Igualdad:", x == y);
console.log("Igualdad estricta:", x === y);
console.log("Desigualdad:", a !== b);
console.log("Mayor que:", a > b);
console.log("Menor que o igual:", a <= b);

// Operadores Lógicos
let p = true;
let q = false;
console.log("AND lógico:", p && q);
console.log("OR lógico:", p || q);
console.log("NOT lógico:", !p);

// Operadores de Asignación
let c = 3;
c += 2;
console.log("Asignación con adición:", c);

// Operadores de Identidad
console.log("Identidad:", x === 10);
console.log("No identidad:", y !== 10);

// Operadores de Pertenencia
let arreglo = [1, 2, 3];
console.log("Pertenece al arreglo:", 2 in arreglo);

// Operadores de Bits
let num1 = 5; // Representación binaria: 0101
let num2 = 3; // Representación binaria: 0011
console.log("AND a nivel de bits:", num1 & num2); // Resultado: 0001 (1 en binario)
console.log("OR a nivel de bits:", num1 | num2); // Resultado: 0111 (7 en binario)
console.log("Desplazamiento a la izquierda:", num1 << 1); // Resultado: 1010 (10 en binario)
console.log("Desplazamiento a la derecha:", num1 >> 1); // Resultado: 0010 (2 en binario)

// Estructuras de Control
// Condicionales
let edad = 18;
if (edad >= 18 && edad <= 125) {
    console.log("Eres mayor de edad");
} else if (edad < 18) {
    console.log("Eres menor de edad");
} else {
    console.log("Edad no valida");

}

// Excepciones
try {
    let resultado = 10 / 0;
    console.log("Resultado:", resultado);
} catch (error) {
    console.log("Error:", error.message);
} finally {
    console.log("Finalizado el bloque try-catch");
}

// Programa
for (let i = 10; i <= 55; i++) {
    if (i % 2 === 0 && i !== 16 && i % 3 !== 0) {
        console.log(i);
    }
}

