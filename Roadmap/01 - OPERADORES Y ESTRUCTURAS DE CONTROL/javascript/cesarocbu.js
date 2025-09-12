//Operadores
console.log("OPERADORES")

console.log("------------------------")

console.log("Aritmeticos:")
let a = 10
let b = 5
let suma = a + b
let resta = a - b
let multiplicacion = a * b
let division = a / b
let modulo = a % b
console.log("Numero 1: " + a, "Numero 2: " + b)
console.log("Suma:" + suma)
console.log("Resta: " + resta)
console.log("Multiplicación: " + multiplicacion)
console.log("Division: " + division)
console.log("Modulo: " + modulo)
a++
b--
console.log("Incremento(10): " + a)
console.log("Decremento(5) : " + b)

console.log("------------------------")

console.log("Lógicos:")

let p = true
let q = false
console.log(p && q)
console.log(p || q)
console.log(!p)
console.log("------------------------")

console.log("Comparación:")

let num1 = 10
let num2 = 5
console.log("Num1: " + num1)
console.log("Num2: " + num2)

console.log('==: ')
console.log(num1 == num2)
console.log("===: ")
console.log(num1 === num2)
console.log("!=: ")
console.log(num1 != num2)
console.log("!==: ")
console.log(num1 !== num2)
console.log(">: ")
console.log(num1 > num2)
console.log("<: ")
console.log(num1 < num2)
console.log(">=: ")
console.log(num1 >= num2)
console.log("<=: ")
console.log(num1 <= num2)

console.log("------------------------")

console.log("Asignación:")

let x = 10;
console.log("x: " + x)
x += 5; // x ahora es 15
console.log("x += 5: " + x)
let y = 20;
console.log("y: " + y)
y -= 3; // y ahora es 17
console.log("y -= 3: " + y)

console.log("------------------------")

console.log("Pertenencia:")

let persona = {nombre: "Juan", edad: 30};
console.log(persona)
console.log('nombre in persona');
console.log("nombre" in persona); //true
console.log('apellido in persona');
console.log("apellido" in persona); //false

console.log("------------------------")

console.log("Bit");
let m = 5; // Representación binaria: 101
let n = 3; // Representación binaria: 011

console.log(m & n); // 1 (AND bit a bit)
console.log(m | n); // 7 (OR bit a bit)
console.log(m ^ n); // 6 (XOR bit a bit)
console.log(m << 1); // 10 (Desplazamiento a la izquierda)
console.log(n >> 1); // 1 (Desplazamiento a la derecha)

console.log("------------------------")

console.log("Estructuras de control:");

console.log("if-else");

let numero = 200
if (numero === 200) {
    console.log("Es el mismo número!")
} else {
    console.log("No es el mismo número :C")
}

console.log("For")
for (let i = 0; i < 5; i++) {
    console.log("Iteración número: " + i);
}

console.log("While")
let i = 0
while (i < 5) {
    console.log("Iteración número: " + i);
    i++;
}

console.log("Switch")
let dia = 2
switch (dia) {
    case 1:
        console.log("Lunes");
        break;
    case 2:
        console.log("Martes");
        break;
    default:
        console.log("Día no válido");
}

console.log("Ejercicio extra:");
console.log("Números entre 10 y 55, pares, y que no son ni el 16 ni múltiplos de 3.");
for (let i = 10; i <= 55; i++) {
    if (i % 2 === 0 && i !== 16 && i % 3 !== 0) {
        console.log(i);
    }
}