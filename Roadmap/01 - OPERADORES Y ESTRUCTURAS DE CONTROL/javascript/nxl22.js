// Operadores en JavaScript

// Operadores aritméticos
let a = 10;
let b = 3;
console.log("Operadores aritméticos:");
console.log("Suma:", a + b);               // Suma: 10 + 3 = 13
console.log("Resta:", a - b);              // Resta: 10 - 3 = 7
console.log("Multiplicación:", a * b);      // Multiplicación: 10 * 3 = 30
console.log("División:", a / b);           // División: 10 / 3 = 3.333...
console.log("Módulo:", a % b);             // Módulo: 10 % 3 = 1
console.log("Potencia:", a ** b);          // Potencia: 10 ** 3 = 1000


// Operadores de comparación
let x = 5;
let y = 10;
console.log("Operadores de comparación:");
console.log("x == y?", x == y);            // x == y? false
console.log("x != y?", x != y);            // x != y? true
console.log("x > y?", x > y);              // x > y? false
console.log("x < y?", x < y);              // x < y? true
console.log("x >= y?", x >= y);            // x >= y? false
console.log("x <= y?", x <= y);            // x <= y? true


// Operadores lógicos
console.log("Operadores lógicos:");
// AND lógico (&&)
console.log("5 && 10?", 5 && 10);       // 5 && 10? 10 (Ambos operandos son verdaderos, devuelve el segundo valor)
// OR lógico (||)
console.log("0 || 20?", 0 || 20);       // 0 || 20? 20 (Uno de los operandos es verdadero, devuelve el primer valor verdadero)
// NOT lógico (!)
console.log("!5?", !5);                 // !5? false (Niega un valor verdadero, devuelve false)
console.log("!0?", !0);                 // !0? true (Niega un valor falso, devuelve true)


// Operadores de asignación
let z = 5;
z += 3;  // Equivalente a z = z + 3
console.log("Operadores de asignación:");
console.log("z:", z);                      // z: 8

// Operadores de identidad
let str1 = "hello";
let str2 = "hello";
console.log("Operadores de identidad:");
console.log("str1 === str2?", str1 === str2);   // str1 === str2? true
console.log("str1 !== str2?", str1 !== str2);   // str1 !== str2? false

// Operadores de pertenencia
let fruits = ["apple", "banana", "orange"];
console.log("Operadores de pertenencia:");
console.log("'banana' in fruits?", 'banana' in fruits);       // 'banana' in fruits? true
console.log("'grape' not in fruits?", !('grape' in fruits));   // 'grape' not in fruits? true


// Estructuras de control

// Condicionales
let num = 15;
if (num % 2 === 0) {
    console.log("Es par.");
} else {
    console.log("Es impar.");
}

// Iterativas
console.log("Bucle while:");
let i = 10;
while (i <= 40) {
    if (i !== 16 && i % 3 !== 0) {
        console.log(i);
    }
    i++;
}

// Manejo de error
console.log("Manejo de error:");
try {
    let result = 10 / 0;
} catch (error) {
    console.log("Error: División por cero.");
}
