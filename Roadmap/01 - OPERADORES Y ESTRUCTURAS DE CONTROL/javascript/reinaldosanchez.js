//operadores

//aritmeticos
//suma
console.log(2 + 2);
//resta
console.log(2 - 2);
//multiplicacion
console.log(2 * 2);
//division
console.log(2 / 2);
//asignacion
let x = 2; console.log(x);
x += 2; console.log(x);
x -= 2; console.log(x);
x *= 2; console.log(x);
x /= 2; console.log(x);
x %= 2; console.log(x);
x **= 2; console.log(x);
//comparacion
console.log(2 == 2);
console.log(2 === 2);
console.log(2 != 2);
console.log(2 !== 2);
console.log(2 > 2);
console.log(2 < 2);
console.log(2 >= 2);
console.log(2 <= 2);
//lógicos
console.log(true && true);  //verdadero
console.log(true && false); //falso
console.log(false && true); //falso
console.log(false && false); //falso
console.log(true || true);  //verdadero
console.log(true || false); //verdadero
console.log(false || true); //verdadero
console.log(false || false); //falso
console.log(!true); //falso
console.log(!false); //verdadero

//operadores de cadena
console.log("Hola" + " " + "Mundo");
//operador condicional
let edad = 18;
let mensaje = edad >= 18 ? "Mayor de edad" : "Menor de edad";
console.log(mensaje);
//operador coma
let a = 1, b = 2, c = 3;
console.log(a, b, c);
//operador de incremento
let d = 1;
console.log(d++);
//operador de decremento
let e = 1;
console.log(e--);
//operador de negacion
let f = 1;
console.log(-f);
//operador bit a bit
let g = 1;
console.log(g & 1);
console.log(g | 1);
console.log(g ^ 1);
console.log(~g);
console.log(g << 1);
console.log(g >> 1);
console.log(g >>> 1);
// operador identidad
let h = 1;
console.log(h === 1);

//estructuras de control

//condicionales
if (2 > 2) {
    console.log("2 es mayor que 2");
} else if (2 < 2) {
    console.log("2 es menor que 2");
} else {
    console.log("2 es igual que 2");
}
//iterativas
for (let i = 0; i < 2; i++) {
    console.log(i);
}
//excepciones
try {
    console.log("Intentando acceder a una variable que no existe");
    console.log(x);
} catch (error) {
    console.log(error);
}
//switch
let numero2 = 2;
switch (numero) {
    case 1:
        console.log("1");
        break;
    case 2:
        console.log("2");
        break;
    default:
        console.log(" Otro");
}
// while
let numero3 = 2;
while (numero < 2) {
    console.log(numero);
    numero++;
}
// do while
let numero = 2;
do {
    console.log(numero);
    numero++;
} while (numero < 2);
// for
for (let i = 0; i < 2; i++) {
    console.log(i);
}

//reto
console.log("--- DIFICULTAD EXTRA ---");

for (let i = 10; i <= 55; i++) {
    if (i % 2 === 0 && i !== 16 && i % 3 !== 0) {
        console.log(i);
    }
}