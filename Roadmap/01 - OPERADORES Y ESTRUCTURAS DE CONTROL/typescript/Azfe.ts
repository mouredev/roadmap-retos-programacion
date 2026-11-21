/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 */

// OPERADORES EN TYPESCRIPT
// Operadores Aritméticos
let a: number = 10;
let b: number = 5;
console.log("Suma:", a + b); // 15
console.log("Resta:", a - b); // 5
console.log("Multiplicación:", a * b); // 50
console.log("División:", a / b); // 2
console.log("Módulo:", a % b); // 0
console.log("Potencia:", a ** b); // 100000 (10^5)
console.log("Incremento:", a++); // 10 (post-incremento: devuelve el valor ANTERIOR)
console.log("Valor de a después del post-incremento:", a); // 11
console.log("Decremento:", b--); // 5 (post-decremento: devuelve el valor ANTERIOR)
console.log("Valor de b después del post-decremento:", b); // 4

// Operadores de Asignación
let c: number = 20;
c += 10; // c = c + 10
console.log("Asignación suma:", c); // 30
c -= 5; // c = c - 5
console.log("Asignación resta:", c); // 25
c *= 2; // c = c * 2
console.log("Asignación multiplicación:", c); // 50
c /= 5; // c = c / 5
console.log("Asignación división:", c); // 10
c %= 3; // c = c % 3
console.log("Asignación módulo:", c); // 1
c **= 2; // c = c ** 2
console.log("Asignación potencia:", c); // 1
c <<= 1; // Desplazamiento izquierda
console.log("Asignación desplazamiento izquierda:", c); // 2
c >>= 1; // Desplazamiento derecha
console.log("Asignación desplazamiento derecha:", c); // 1
c &= 3; // AND bit a bit
console.log("Asignación AND bit a bit:", c); // 1
c |= 2; // OR bit a bit
console.log("Asignación OR bit a bit:", c); // 3
c ^= 1; // XOR bit a bit
console.log("Asignación XOR bit a bit:", c); // 2

// Operadores de Comparación
console.log("Igualdad:", a == b); // false
console.log("Igualdad estricta:", a === b); // false
console.log("Desigualdad:", a != b); // true
console.log("Desigualdad estricta:", a !== b); // true
console.log("Mayor que:", a > b); // true
console.log("Menor que:", a < b); // false
console.log("Mayor o igual que:", a >= b); // true
console.log("Menor o igual que:", a <= b); // false

// Operadores Lógicos
let verdadero: boolean = true;
let falso: boolean = false;
console.log("AND:", verdadero && falso); // false
console.log("OR:", verdadero || falso); // true
console.log("NOT verdadero:", !verdadero); // false
console.log("NOT falso:", !falso); // true
console.log("Doble negación verdadero:", !!verdadero); // true
console.log("Doble negación falso:", !!falso); // false

// Operadores Bit a Bit
let m: number = 5; // 0101 en binario
let n: number = 3; // 0011 en binario
console.log("AND bit a bit:", m & n); // 1 (0001 en binario)
console.log("OR bit a bit:", m | n); // 7 (0111 en binario)
console.log("XOR bit a bit:", m ^ n); // 6 (0110 en binario)
console.log("NOT bit a bit m:", ~m); // -6 (1111...1010 en binario)
console.log("NOT bit a bit n:", ~n); // -4 (1111...1100 en binario)
console.log("Desplazamiento izquierda m:", m << 1); // 10 (1010 en binario)
console.log("Desplazamiento derecha m:", m >> 1); // 2 (0010 en binario)
console.log("Desplazamiento derecha sin signo m:", m >>> 1); // 2 (0010 en binario)

// Operadores de Cadena
let str1: string = "Hola";
let str2: string = "Mundo";
console.log("Concatenación:", str1 + " " + str2); // "Hola Mundo"

// Operadores Ternarios/Condicionales
let resultado: string = a > b ? "a es mayor que b" : "a no es mayor que b";
console.log("Operador ternario:", resultado); // "a es mayor que b"

// Operadores de Pertenencia
/* .includes() -> Comprueba si un array o una cadena de texto contiene un valor específico*/
let array: number[] = [1, 2, 3, 4, 5];
console.log("Pertenencia en array (3):", array.includes(3)); // true
console.log("Pertenencia en array (6):", array.includes(6)); // false

// Operadores de Tipo (TypeScript específicos)
let valor: any = "Hola";
let tipo = typeof valor; // Comprueba el tipo de dato primitivo
console.log("typeof valor:", tipo); // "string"
let esString: boolean = valor instanceof String; // Comprueba si es una instancia de String, no un string primitivo
console.log("valor instanceof String:", esString); // false
let esArray: boolean = [1, 2, 3] instanceof Array; // Comprueba si es una instancia de Array
console.log("[1,2,3] instanceof Array:", esArray); // true

// Operadores de TypeScript
interface Persona {
    nombre: string;
    edad: number;
}

let usuario: Persona = { nombre: "Ana", edad: 25 };
let tieneNombre = "nombre" in usuario; // operador 'in'
console.log("Operador 'in' (nombre):", tieneNombre); // true
console.log("Operador 'in' (email):", "email" in usuario); // false

// Type assertion
let longitud = (valor as string).length; // Aserción de tipo
console.log("Aserción de tipo 'as':", longitud); // 4
let longitud2 = (<string>valor).length; // Forma alternativa
console.log("Aserción de tipo '<>':", longitud2); // 4

// Operador 'as const'
let colores = ['rojo', 'verde', 'azul'] as const; // readonly tuple
console.log("as const:", colores); // [ 'rojo', 'verde', 'azul' ]

// Non-null assertion operator
let posibleNulo: string | null = "texto";
console.log("Non-null assertion:", posibleNulo!.length); // 5 (afirmamos que no es null)

// Operadores de Conjuntos
// Spread operator
let array1: number[] = [1, 2, 3];
let array2: number[] = [...array1, 4, 5];
console.log("Spread en array:", array2); // [ 1, 2, 3, 4, 5 ]

let obj1: { a: number; b: number } = { a: 1, b: 2 };
let obj2: { a: number; b: number; c: number } = { ...obj1, c: 3 };
console.log("Spread en objeto:", obj2); // { a: 1, b: 2, c: 3 }

// Rest operator
let [primero, ...resto]: [number, ...number[]] = [1, 2, 3, 4];
console.log("Rest (primero):", primero); // 1
console.log("Rest (resto):", resto); // [ 2, 3, 4 ]

// Operadores Especiales
// delete
let persona: { nombre: string; edad?: number } = { nombre: "Ana", edad: 25 };
console.log("Antes del delete:", persona); // { nombre: 'Ana', edad: 25 }
delete persona.edad; // Elimina la propiedad
console.log("Después del delete:", persona); // { nombre: 'Ana' }

// void
void function() {
    console.log("Esto no retorna nada");
}();

// typeof (ya visto en operadores de tipo)
let numero: number = 42;
console.log("typeof numero:", typeof numero); // "number"

// instanceof
class Perro {}
let mascota: Perro = new Perro();
console.log("mascota instanceof Perro:", mascota instanceof Perro); // true

// Nullish coalescing (??)
// Devuelve el valor de la derecha SOLO si el de la izquierda es null o undefined
let nulo: string | null = null;
console.log("Nullish coalescing:", nulo ?? "valor por defecto"); // "valor por defecto"
let cero: number | null = 0;
console.log("Diferencia con OR (0 || x):", cero || "por defecto"); // "por defecto" (0 es falsy)
console.log("Diferencia con ?? (0 ?? x):", cero ?? "por defecto"); // 0 (0 no es null ni undefined)

// Optional chaining (?.)
// Corta la evaluación y devuelve undefined si el valor es null o undefined
let cliente: { nombre: string; direccion?: { ciudad: string } } = { nombre: "Ana" };
console.log("Optional chaining:", cliente.direccion?.ciudad); // undefined (no lanza error)
console.log("Optional chaining con ??:", cliente.direccion?.ciudad ?? "Sin ciudad"); // "Sin ciudad"

// Operadores de Asignación Lógica
let x: number | null = null;
x ??= 10; // Asigna solo si el valor actual es null o undefined
console.log("Asignación nullish (??=):", x); // 10
let activo: boolean = true;
activo &&= false; // Asigna solo si el valor actual es truthy
console.log("Asignación AND (&&=):", activo); // false
let nombre: string = "";
nombre ||= "Anónimo"; // Asigna solo si el valor actual es falsy
console.log("Asignación OR (||=):", nombre); // "Anónimo"

// ESTRUCTURAS DE CONTROL EN TYPESCRIPT
// Condicionales
if (a > b) {
  console.log("a es mayor que b");
} else if (a < b) {
  console.log("a es menor que b");
} else {
  console.log("a es igual a b");
}

let dia: string = "Lunes";
switch (dia) {
  case "Lunes":
    console.log("Hoy es lunes");
    break;
  case "Martes":
    console.log("Hoy es martes");
    break;
  default:
    console.log("Hoy no es ni lunes ni martes");
}

// switch con enums
enum Color {
  Rojo = 0,
  Verde = 1,
  Azul = 2
}

let color = Color.Rojo as Color;

switch (color) {
  case Color.Rojo:
    console.log("El color es rojo");
    break;
  case Color.Verde:
    console.log("El color es verde");
    break;
  case Color.Azul:
    console.log("El color es azul");
    break;
}

// Iterativas
console.log("Bucle for:");
for (let i = 0; i < 5; i++) {
  console.log("Iteración:", i);
}

console.log("Bucle while:");
let j: number = 0;
while (j < 5) {
  console.log("Iteración:", j);
  j++;
}

// do...while comprueba la condición AL FINAL, así que siempre se ejecuta al menos una vez
console.log("Bucle do...while:");
let k: number = 10;
do {
  console.log("Iteración:", k); // se ejecuta aunque 10 < 3 sea false
  k++;
} while (k < 3);

// for...of recorre los VALORES de un iterable
console.log("Bucle for...of:");
for (const item of array) {
  console.log("Valor:", item);
}

// for...in recorre las CLAVES de un objeto
console.log("Bucle for...in:");
for (const clave in usuario) {
  console.log("Clave:", clave);
}

// break y continue
console.log("break y continue:");
for (let i = 0; i < 10; i++) {
  if (i % 2 === 0) {
    continue; // salta al siguiente ciclo sin ejecutar lo que queda
  }
  if (i > 6) {
    break; // sale del bucle por completo
  }
  console.log("Impar:", i);
}

// Excepciones
function dividir(a: number, b: number): number {
  if (b === 0) {
    throw new Error("No se puede dividir por cero"); // throw interrumpe el flujo
  }
  return a / b;
}

try {
  console.log("Resultado:", dividir(10, 2));
  console.log("Resultado:", dividir(10, 0)); // Lanza la excepción
  console.log("Esta línea nunca se ejecuta");
} catch (error) {
  // En modo strict la variable del catch es 'unknown', hay que comprobar el tipo
  if (error instanceof Error) {
    console.error("Error:", error.message);
  }
} finally {
  console.log("Bloque finally ejecutado"); // Se ejecuta siempre, haya error o no
}

export {};
