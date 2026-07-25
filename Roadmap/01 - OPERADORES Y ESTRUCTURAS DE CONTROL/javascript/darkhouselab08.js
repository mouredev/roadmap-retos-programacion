
console.log("--- OPERADORES ---");

// 1. Aritméticos
console.log("Aritméticos:");
let a = 10;
let b = 5;
console.log("Suma: 10 + 5 =", a + b);
console.log("Resta: 10 - 5 =", a - b);
console.log("Multiplicación: 10 * 5 =", a * b);
console.log("División: 10 / 5 =", a / b);
console.log("Módulo (Resto): 10 % 3 =", 10 % 3);
console.log("Exponenciación: 10 ** 2 =", a ** 2);

// 2. Lógicos
console.log("\nLógicos:");
let esVerdadero = true;
let esFalso = false;
console.log("AND (&&): true && false =", esVerdadero && esFalso); // false
console.log("OR (||): true || false =", esVerdadero || esFalso);   // true
console.log("NOT (!): !true =", !esVerdadero);                    // false

// 3. De Comparación
console.log("\nDe Comparación:");
console.log("Mayor que (>): 10 > 5 =", a > b);
console.log("Menor que (<): 10 < 5 =", a < b);
console.log("Mayor o igual (>=): 10 >= 10 =", a >= 10);
console.log("Menor o igual (<=): 5 <= 10 =", b <= a);

// 4. De Asignación
console.log("\nDe Asignación:");
let c = 10; // Asignación básica
c += 5;     // c = c + 5
console.log("Asignación de suma (+= 5):", c); // 15
c -= 3;     // c = c - 3
console.log("Asignación de resta (-= 3):", c); // 12
c *= 2;     // c = c * 2
console.log("Asignación de multiplicación (*= 2):", c); // 24

// 5. De Identidad (Comparación Estricta vs. Abstracta)
console.log("\nDe Identidad (Estricta vs. Abstracta):");
let numCinco = 5;
let strCinco = "5";
// Abstracta (==): Compara solo el valor, no el tipo. (NO RECOMENDADO)
console.log("Abstracta (==): 5 == '5' es", numCinco == strCinco); // true
// Estricta (===): Compara valor Y tipo. (RECOMENDADO)
console.log("Estricta (===): 5 === '5' es", numCinco === strCinco); // false

// 6. De Pertenencia (in)
console.log("\nDe Pertenencia (in / .includes()):");
let miArray = [1, 2, 3, 4];
let miObjeto = { nombre: "Franco", pais: "Colombia" };
console.log("¿Está el 3 en el array? (.includes()):", miArray.includes(3)); // true
console.log("¿Está 'nombre' en el objeto? (in):", "nombre" in miObjeto); // true

// 7. De Bits (Avanzado)
console.log("\nDe Bits:");
console.log("AND a nivel de bits (5 & 1):", 5 & 1); // 1
console.log("OR a nivel de bits (5 | 1):", 5 | 1);  // 5

console.log("\n--- ESTRUCTURAS DE CONTROL ---");

// 1. Condicionales (if, else if, else)
console.log("\nCondicional (if):");
let edad = 18;
if (edad > 18) {
  console.log("Es mayor de 18");
} else if (edad === 18) {
  console.log("Tiene 18 años");
} else {
  console.log("Es menor de 18");
}

// Condicional (switch)
console.log("\nCondicional (switch):");
let dia = "Lunes";
switch (dia) {
  case "Lunes":
    console.log("¡Ánimo, es Lunes!");
    break;
  case "Viernes":
    console.log("¡Hoy es Viernes!");
    break;
  default:
    console.log("Es un día de la semana.");
}

// 2. Iterativas (Bucles)
console.log("\nIterativa (for):");
// El bucle 'for' es el clásico: (inicio; condición; incremento)
for (let i = 0; i < 3; i++) {
  console.log("Número de bucle 'for':", i);
}

console.log("\nIterativa (while):");
let contador = 0;
while (contador < 3) {
  console.log("Número de bucle 'while':", contador);
  contador++; // ¡Importante incrementar para no hacer un bucle infinito!
}

console.log("\nIterativa (forEach):");
// 'forEach' es la forma moderna de recorrer un array
miArray.forEach(function(numero) {
  console.log("Número en miArray:", numero);
});

// 3. Excepciones (try, catch)
console.log("\nExcepciones (try...catch):");
try {
  // Intentamos ejecutar un código que fallará
  let resultado = 10 / variableInexistente;
} catch (error) {
  // Si falla, "atrapamos" el error aquí y el programa no se detiene
  console.log("¡Ups, ocurrió un error!");
  console.log("Mensaje de error:", error.message);
} finally {
  console.log("El bloque 'try...catch' ha finalizado.");
}