/*
 * OPERADORES Y ESTRUCTURAS DE CONTROL EN JAVASCRIPT
 * https://developer.mozilla.org/es/docs/Web/JavaScript
 */

console.log("=== Operadores en Javascript=====");
// ==========================================
// 1. OPERADORES ARITMÉTICOS
// ==========================================
console.log("----Operadores Arimeticos ------");
let a = 10;
let b = 3;

console.log(`Suma: ${a} + ${b} = ${a + b}`);
console.log(`Resta: ${a} - ${b} = ${a - b}`);
console.log(`Multiplicación: ${a} * ${b} = ${a * b}`);
console.log(`División: ${a} / ${b} = ${a / b}`);
console.log(`Módulo (resto): ${a} % ${b} = ${a % b}`);
console.log(`Exponenciación: ${a} ** ${b} = ${a ** b}`);

let x = 5;
console.log(`incremento x++ = ${x++}, ahora x= ${x}`);
let y = 5;
console.log(`Pre-incremento: ++y = ${++y}, ahora y = ${y}`);
let z = 5;
console.log(`Decremento: z-- = ${z--}, ahora z = ${z}`);

// ==========================================
// 2. OPERADORES DE ASIGNACIÓN
// ==========================================
console.log("\n--- OPERADORES DE ASIGNACIÓN ---");
let num = 10;
console.log(`asignacion simple: num ${num}`);
num += 5;
console.log(`Suma y asigna (+=): num = ${num}`);

num -= 3;
console.log(`Resta y asigna (-=): num = ${num}`);

num *= 2;
console.log(`Multiplica y asigna (*=): num = ${num}`);

num /= 4;
console.log(`Divide y asigna (/=): num = ${num}`);

num %= 5;
console.log(`Módulo y asigna (%=): num = ${num}`);

num **= 2;
console.log(`Exponenciación y asigna (**=): num = ${num}`);

// ==========================================
// 3. OPERADORES DE COMPARACIÓN
// ==========================================

console.log("\n--- OPERADORES DE COMPARACIÓN ---");
let p = 5;
let q = "5";
console.log(`${p} == ${q}:${p == q}(igualdad debil)`);
console.log(`${p} === ${q}:${p === q}(igualdad estricta)`);
console.log(`${p} != ${q}: ${p != q} (desigualdad débil)`);
console.log(`${p} !== ${q}: ${p !== q} (desigualdad estricta)`);
console.log(`${p} > 3:${p > 3}`);
console.log(`${p}< 10 : ${p < 10}`);
console.log(`${p} >= 5: ${p >= 5}`);
console.log(`${p} <= 4: ${p <= 4}`);

// ==========================================
// 4. OPERADORES LÓGICOS
// ==========================================
console.log("\n --- Operadores Logicos ---");
let Verdaderos = true;
let falso = false;
console.log(`true && false : ${Verdaderos && falso} (AND logico)`);
console.log(`true || false : ${Verdaderos || falso} (OR logico)`);
console.log(`!true: ${!Verdaderos} (NOT logico)`);

// Cortocircuito
console.log(`Cortocircuito &&: ${0 && "no se evalúa"}`);
console.log(`Cortocircuito ||: ${0 || "se evalúa"}`);

// ==========================================
// 5. OPERADORES DE BITS (BITWISE)
// ==========================================
console.log("\n--- OPERADORES DE BITS ---");
let bit1 = 5; // 0101 en binario
let bit2 = 3; // 0011 en binario

console.log(`${bit1} & ${bit2} = ${bit1 & bit2} (AND bit a bit)`);
console.log(`${bit1} | ${bit2} = ${bit1 | bit2} (OR bit a bit)`);
console.log(`${bit1} ^ ${bit2} = ${bit1 ^ bit2} (XOR bit a bit)`);
console.log(`~${bit1} = ${~bit1} (NOT bit a bit)`);
console.log(`${bit1} << 1 = ${bit1 << 1} (desplazamiento izquierda)`);
console.log(`${bit1} >> 1 = ${bit1 >> 1} (desplazamiento derecha)`);
console.log(`-${bit1} >>> 1 = ${-bit1 >>> 1} (desplazamiento sin signo)`);

// ==========================================
// 6. OPERADORES DE CADENA (STRING)
// ==========================================
console.log("\n--- OPERADORES DE CADENA ---");
let str1 = "Hola";
let str2 = "Mundo";
console.log(
  `Concatenación: "${str1}" + " " + "${str2}" = "${str1 + " " + str2}"`
);

// ==========================================
// 7. OPERADOR TERNARIO (CONDICIONAL)
// ==========================================
console.log("\n--- OPERADOR TERNARIO ---");
let edad = 18;
let mensaje = edad >= 18 ? "Mayor de edad" : "Menor de edad";
console.log(`Edad ${edad}: ${mensaje}`);

// ==========================================
// 8. OPERADORES DE TIPO
// ==========================================
console.log("\n -- operadores de tipo --");
let variable = "texto";
console.log(`typeof "${variable}": ${typeof variable}`);
console.log(`typeof 42: ${typeof 42}`);
console.log(`typeof true: ${typeof true}`);

let arr = [1, 2, 3];
console.log(`[1,2,3] instanceof Array: ${arr instanceof Array}`);

// ==========================================
// 9. OPERADOR IN (PERTENENCIA)
// ==========================================
console.log("\n--- OPERADOR IN (PERTENENCIA) ---");
let objeto = { nombre: "Juan", edad: 30 };
console.log(`"nombre" in objeto: ${"nombre" in objeto}`);
console.log(`"apellido" in objeto: ${"apellido" in objeto}`);

let lista = ["a", "b", "c"];
console.log(`1 in abcd : ${1 in lista}(indice existe)`);
console.log(`5 in  abcd : ${5 in lista}(indice no existe)`);

// ==========================================
// 10. OPERADOR DELETE
// ==========================================
console.log("\n--- OPERADOR DELETE ---");
let obj = { prop1: "valor1", prop2: "valor2" };
console.log("Antes de delete:", obj);
delete obj.prop1;
console.log("Después de delete obj.prop1:", obj);

// ==========================================
// 11. OPERADORES DE COALESCENCIA Y OPCIONALES
// ==========================================
console.log("\n--- OPERADORES MODERNOS ---");
let valor = null;
console.log(
  `null ?? "predeterminado": ${valor ?? "predeterminado"} (Nullish coalescing)`
);

let usuario = { nombre: "Ana", direccion: { ciudad: "Madrid" } };
console.log(`Optional chaining: ${usuario?.direccion?.ciudad}`);
console.log(`Optional chaining (no existe): ${usuario?.telefono?.numero}`);

// ==========================================
// 12. OPERADOR SPREAD Y REST
// ==========================================
console.log("\n--- OPERADORES SPREAD Y REST ---");
let arr1 = [1, 2, 3];
let arr2 = [...arr1, 4, 5];
console.log(`Spread en array: [1,2,3] -> [...arr, 4, 5] = [${arr2}]`);

function sumar(...numeros) {
  return numeros.reduce((acc, n) => acc + n, 0);
}
console.log(`Rest en función: sumar(1,2,3,4,5) = ${sumar(1, 2, 3, 4, 5)}`);

console.log("\n\n=== ESTRUCTURAS DE CONTROL ===\n");

// ==========================================
// 1. CONDICIONALES
// ==========================================
console.log("--- CONDICIONALES ---");

// IF / ELSE IF / ELSE
console.log("\nIF / ELSE IF / ELSE:");
let nota = 85;
if (nota >= 90) {
  console.log(`Nota ${nota}: Excelente`);
} else if (nota >= 70) {
  console.log(`Nota ${nota}: Aprobado`);
} else {
  console.log(`Nota ${nota}: Reprobado`);
}

// SWITCH
console.log("\nSWITCH:");
let dia = 3;
switch (dia) {
  case 1:
    console.log("Lunes");
    break;
  case 2:
    console.log("Martes");
    break;
  case 3:
    console.log("Miércoles");
    break;
  default:
    console.log("Otro día");
}

// ==========================================
// 2. BUCLES (ITERATIVAS)
// ==========================================
console.log("\n--- ESTRUCTURAS ITERATIVAS ---");

// FOR
console.log("\nFOR:");
for (let i = 0; i < 5; i++) {
  console.log(`Iteración ${i}`);
}

// WHILE
console.log("\nWHILE:");
let contador = 0;
while (contador < 3) {
  console.log(`Contador: ${contador}`);
  contador++;
}

// DO WHILE
console.log("\nDO WHILE:");
let num2 = 0;
do {
  console.log(`Número: ${num2}`);
  num2++;
} while (num2 < 3);

// FOR...OF (itera sobre valores)
console.log("\nFOR...OF (valores):");
let frutas = ["manzana", "pera", "uva"];
for (let fruta of frutas) {
  console.log(`Fruta: ${fruta}`);
}

// FOR...IN (itera sobre propiedades/índices)
console.log("\nFOR...IN (propiedades):");
let persona = { nombre: "Carlos", edad: 25, ciudad: "Lima" };
for (let propiedad in persona) {
  console.log(`${propiedad}: ${persona[propiedad]}`);
}

// FOREACH (método de arrays)
console.log("\nFOREACH:");
let numeros = [10, 20, 30];
numeros.forEach((num, index) => {
  console.log(`Índice ${index}: ${num}`);
});

// ==========================================
// 3. CONTROL DE FLUJO
// ==========================================
console.log("\n--- CONTROL DE FLUJO ---");

// BREAK
console.log("\nBREAK:");
for (let i = 0; i < 10; i++) {
  if (i === 5) {
    console.log("Break en i = 5");
    break;
  }
  console.log(`i = ${i}`);
}

// CONTINUE
console.log("\nCONTINUE:");
for (let i = 0; i < 5; i++) {
  if (i === 2) {
    console.log("Continue salta i = 2");
    continue;
  }
  console.log(`i = ${i}`);
}

// LABEL (etiquetas)
console.log("\nLABEL:");
bucleExterno: for (let i = 0; i < 3; i++) {
  for (let j = 0; j < 3; j++) {
    if (i === 1 && j === 1) {
      console.log(`Break externo en i=${i}, j=${j}`);
      break bucleExterno;
    }
    console.log(`i=${i}, j=${j}`);
  }
}

// ==========================================
// 4. MANEJO DE EXCEPCIONES
// ==========================================
console.log("\n--- MANEJO DE EXCEPCIONES ---");

// TRY / CATCH / FINALLY
console.log("\nTRY / CATCH / FINALLY:");
try {
  console.log("Intentando ejecutar código...");
  let resultado = 10 / 0;
  console.log(`Resultado: ${resultado}`);

  // Forzar un error
  throw new Error("Error intencional");
} catch (error) {
  console.log(`Error capturado: ${error.message}`);
} finally {
  console.log("Bloque finally siempre se ejecuta");
}

// TRY / CATCH con tipos de error
console.log("\nDiferentes tipos de errores:");
try {
  JSON.parse("json inválido");
} catch (error) {
  if (error instanceof SyntaxError) {
    console.log(`SyntaxError: ${error.message}`);
  }
}

console.log("\n\n=== DIFICULTAD EXTRA ===\n");

/*
 * Números entre 10 y 55 (incluidos)
 * que sean PARES
 * y que NO sean 16
 * y que NO sean múltiplos de 3
 */

console.log(
  "Números entre 10 y 55 (incluidos), pares, sin 16 y sin múltiplos de 3:\n"
);

for (let i = 10; i <= 55; i++) {
  // Verificar todas las condiciones
  if (i % 2 === 0 && i !== 16 && i % 3 !== 0) {
    console.log(i);
  }
}

console.log("\n¡Reto completado! 🎉");
