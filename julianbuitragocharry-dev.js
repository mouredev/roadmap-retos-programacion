//✔️OPERADORES
//✔️OPERADORES ARITMETICOS
let a = 5;

//1️⃣=============================== PRE INCREMENTO
let preIncremento = ++a;
console.log(preIncremento); // 6
console.log(a); // 6

//2️⃣=============================== POST INCREMENTO
let postIncremento = a++;
console.log(postIncremento); // 6
console.log(a); // 7

//3️⃣=============================== PRE DECREMENTO                              
let preDecremento = --a;
console.log(preDecremento); // 6
console.log(a); // 6

//4️⃣=============================== POST DECREMENTO
let postDecremento = a--;
console.log(postDecremento); // 6
console.log(a); // 5

//✔️OPERADORES DE ASIGNACIÓN
let x = 7;
let y = 12; 

//1️⃣=============================== ASIGNACIÓN BÁSICA
x = y;
console.log(x); // 12

//2️⃣=============================== ASIGNACIÓN DE ADICIÓN
x += y; //x = x + y
console.log(x); // 24 

//3️⃣=============================== ASIGNACIÓN DE RESTA
x -= y; //x = x - y
console.log(x); // 12

//4️⃣=============================== ASIGNACIÓN DE MULTIPLICACIÓN
x *= y; //x = x * y
console.log(x); // 144

//5️⃣=============================== ASIGNACIÓN DE DIVISIÓN
x /= y; //x = x / y
console.log(x); // 12

//6️⃣=============================== ASIGNACIÓN DE RESIDUO
x %= y; //x = x % y
console.log(x); // 0

//7️⃣=============================== ASIGNACIÓN DE EXPONENTE
x = 2;
y = 3;
x **= y; //x = x ** y;
console.log(x); // 8

//8️⃣=============================== ASIGNACIÓN DE DESPLAZAMIENTO A LA IZQUIERDA
x <<= y; //x = x << y
console.log(x); // 64 

//9️⃣=============================== ASIGNACIÓN DE DESPLAZAMIENTO A LA DERECHA
x >>= y; //x = x >> y
console.log(x); // 8 

//🔟=============================== ASIGNACIÓN DE DESPLAZAMIENTO A LA DERECHA SIN SIGNO
x >>>= y; //x = x >>> y
console.log(x); // 1 

//1️⃣1️⃣=============================== ASIGNACIÓN AND BIT A BIT
x &= y; //x = x & y
console.log(x); // 1

//1️⃣2️⃣=============================== ASIGNACIÓN XOR BIT A BIT
x ^= y; //x = x ^ y
console.log(x); // 2

//1️⃣3️⃣=============================== ASIGNACIÓN OR BIT A BIT
x |= y; //x = x | y
console.log(x); // 3

//1️⃣4️⃣=============================== ASIGNACIÓN AND LÓGICO
let z = null;
x &&= z; //x = x && z
console.log(x); // null (La asignación no se realiza porque la condición es falsa)

//1️⃣5️⃣=============================== ASIGNACIÓN OR LÓGICO
let w = "Valor";
x ||= w; //x = x || w
console.log(x); // Valor (La asignación se realiza porque la condición es falsa)

//1️⃣6️⃣=============================== ASIGNACIÓN DE ANULACIÓN
let u;
x ??= u; // Equivalente a: x = x ?? u
console.log(x); // Valor (La asignación se realiza porque x es null o undefined)


//✔️OPERADORES DE COMPARACIÓN

//1️⃣=============================== IGUAL
console.log(6 == '6'); // true
console.log(2 == '3'); // false

//2️⃣=============================== NO ES IGUAL 
console.log(6 != '2'); // true
console.log(2 != '2'); // false

//3️⃣=============================== ESTRICTAMENTE IGUAL
console.log(6 == '6'); // true
console.log(2 == '3'); // false

//4️⃣=============================== DESIGUALDAD ESTRICTA 
console.log(6 != '2'); // true
console.log(2 != '2'); // false

//5️⃣=============================== MAYOR QUE
console.log(6 > 3); // true
console.log(3 > 6); // false

//6️⃣=============================== MAYOR O IGUAL QUE
console.log(4 >= 4); // true
console.log(7 >= 0); // false

//7️⃣=============================== MENOR QUE
console.log(2 <= 10); // true
console.log(10 <= 2); // false

//8️⃣=============================== MENOR O IGUAL QUE
console.log(8 <= 8); // true
console.log(7 <= 2); // false


//✔️OPERADORES LOGICOS
//Son utilizados para obtener booleanos, son equivalentes a las tablas de verdad.

//1️⃣=============================== AND LOGICO
console.log (true && true); // true
console.log (false && true); // false
console.log (true && false); // false
console.log (false && false); // false

//2️⃣=============================== OR LOGICO
console.log (true || true); // true
console.log (false || true); // true
console.log (true || false); // true
console.log (false || false); // false

//3️⃣=============================== NOT LOGICO
console.log(!false); // true
console.log(!true); // false

//✔️OPERADOR TERNIARIO
// Se evalua como una condicion equivalente a un if {} else {}.
const age = 18;
var status = age >= 18 ? "adult" : "minor";
console.log(`Operador Terniario ?: ${status}`); // adult

//✔️OPERADOR UNITARIO DELETE
//Elimina propiedades de objetos.

let persona = {nombre: "Juan", edad: 30, ciudad: "Argentina"};
console.log(`Objeto original: ${persona}`); // { nombre : 'Juan', edad: 30 , ciudad : 'Argentina' }

//=============================== Eliminando la propiedad 'ciudad' del objeto
let deleteSuccess = delete persona.ciudad;
console.log(`Después de eliminar 'ciudad': ${persona}`); // { nombre : 'Juan', edad: 30 }
console.log(`Operación 'delete' exitosa: ${deleteSuccess}`); // true

//✔️OPERADOR DE RELACIÓN IN
// Verificando si 'nombre' y 'apellido' son propiedades del objeto 'persona'
console.log("¿'nombre' en persona?", "nombre" in persona); // true
console.log("¿'apellido' en persona?", "apellido" in persona); // false


//✔️ESTRUCTURAS DE CONTROL
//✔️WHILE
let contadorWhile = 0;
while (contadorWhile < 5) {
    console.log(`Iteración: ${contadorWhile}`);
    contadorWhile++;
}

//✔️DO WHILE
let contadorDoWhile = 0;

do {
    console.log(`Iteración: ${contadorDoWhile}`);
    contadorDoWhile++;
} while (contadorDoWhile < 5);

//✔️FOR
for (let i = 0; i < 5; i++) {
    console.log(`Iteración: ${i}`);
}

//✔️FOR OF
let arrayForOf = [10, 20, 30];

for (let valor of arrayForOf) {
    console.log(`Valor elemento arrayForOf: ${valor}`);
}

//✔️FOR IN
let objetoForIn = { a: 1, b: 2, c: 3 };

for (let propiedad in objetoForIn) {
    console.log(`Propiedad ${propiedad} = ${objetoForIn[propiedad]}`);
}

//✔️FOR EACH
let arrayForEach = [1, 2, 3];

arrayForEach.forEach(function (elemento) {
    console.log(`Elemento: ${elemento}`);
});

//✔️SWITCH
let opcion = 2;

switch (opcion) {
    case 1:
        console.log("Opción 1");
        break;
    case 2:
        console.log("Opción 2");
        break;
    default:
        console.log("Opción por defecto");
}


//✔️IF ELSE
let numero = 7;

if (numero > 0) {
    console.log("Número positivo");
} else if (numero < 0) {
    console.log("Número negativo");
} else {
    console.log("Número es cero");
}

//✔️TRY CATCH
function dividirNumeros(a, b) {
    try {
        if (b === 0) {
            throw new Error("¡División por cero no permitida!");
        }

        let resultado = a / b;
        console.log(`Resultado de la división: ${resultado}`);
    } catch (error) {
        console.error(`Error: ${error.message}`);
    }
}

dividirNumeros(10, 2);  // 5
dividirNumeros(8, 0);   // Error: ¡División por cero no permitida!
dividirNumeros(12, 3);  // 4

/*🧑‍💻DIFICULTAD EXTRA:
 Crea un programa que imprima por consola todos los números comprendidos
 entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
*/

for (let number = 10; number <= 55; number += 2) {
    if (number == 16){
        continue;
    } else if (number % 3 == 0) {
        continue;
    } else {
        console.log(number);
    }
}