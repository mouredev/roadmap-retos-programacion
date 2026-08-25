/*OPERADORES*/
//Asignación
const a = 10;
const b = 20;
const c = 30;
let d = 40;
let e = 50;
let f = "60";
//--------------------
let x = 10;
x += 5; // x = 15
x -= 2; // x = 13
x *= 3; // x = 39
x /= 2; // x = 19.5
x %= 4; // x = 3.5

//Aritmeticos
console.log(`Suma: ${a} + ${b} = ${a + b}`);
console.log(`Resta: ${a} - ${b} = ${a - b}`);
console.log(`Multiplicación: ${a} * ${b} = ${a * b}`);
console.log(`División: ${a} / ${b} = ${a / b}`);
console.log(`Resto: ${a} % ${b} = ${a % b}`);
console.log(`Incremento: ${++d}, ${e++}, e se establece despues: e = ${e}`);
console.log(`Incremento: ${--d}, ${e--}, e se establece despues: e = ${e}`);
console.log(`Negación unaria: Devuelve la negación de su operando: ${-e}`);
console.log(`Unario más: Convierte el operando a un número si es que aún no lo es: ${+f} o ${+e}`);
console.log(`Operador de exponenciación: calcula "base^exponent": ${2 ** 2}`);

//Lógicos
// &&
if(11 && 11 > 10){
    console.log(true)
} else {
    console.log(false)
}
// ||
if(11 || 5 > 10){
    console.log(true)
} else {
    console.log(false)
}
// !
if(9 >! 10){
    console.log(true)
} else {
    console.log(false)
}
// ?? (Si el primer valor es null, retorna el segundo valor, pero si el primer valor no es null retorna el primer valor.)
let nombre1 = "Dario";
let texto = "invitado";
let resultado = nombre1 ?? texto;
console.log(resultado);

//Comparación
const var1 = 3;
const var2 = 4;
// ==
console.log(3 == var1);
console.log(3 == var2);
// !=
console.log(3 != var1);
console.log(3 != var2);
// ===
console.log(3 === var1);
console.log("3" === var1);
// !==
console.log(3 !== var1);
console.log("3" !== var1);
// >, <, >=, <=
console.log(4 > var1);
console.log(3 < var2);
console.log(3 >= var1);
console.log(4 <= var2);

//Identidad
let numero1 = 5;
let numero2 = 5;
let numero3 = "5";

if(numero1 === numero2){
    console.log(true);
}
if(numero1 === numero3){
    console.log(true);
} else {
    console.log(false);
}

//Relacionales
const lista = ["a", "b", "c"];
console.log(0 in lista); // true
console.log(3 in lista); // false

//Bits
console.log(1 | 2); // OR a nivel de bits: 3
console.log(1 & 2); // AND a nivel de bits: 0
console.log(1 ^ 2); // XOR a nivel de bits: 3
console.log(~1); // NOT a nivel de bits: -2

//Ternario
const age = 18;
const status = age >= 18 ? "adult" : "minor";
console.log(status);

/*ESTRUCTURAS DE CONTROL*/
//Condicionales
const nombre = "Francoo";
if(nombre == "Dario"){
    console.log(`Mi nombre es: ${nombre}`);
} else if (nombre == "Franco") {
    console.log(`Mi nombre es: ${nombre}`);
} else {
    console.log("Mi nombre no es ese");
}

switch (nombre) {
    case "Dario":
        console.log(`Mi nombre es ${nombre}`);
        break;
    case "Franco":
        console.log(`Mi nombre es ${nombre}`);
        break;
    default:
        console.log("Mi nombre no es ese");
}

//Iterativas
for (let step = 1; step <= 5; step++) {
  // Runs 5 times, with values of step 0 through 4.
  console.log("Walking east one step");
  console.log(step)
}

let i = 0;
do {
  i += 1;
  console.log(i);
} while (i < 5);

let n = 0;
let x2 = 0;
while (n < 3) {
  n++;
  x2 += n;
  console.log(x2);
}

//Try y catch

let divisor = 1;

try {
    if (divisor === 0) {
        throw new Error("No se puede dividir por cero");
    }
    console.log(10 / divisor);
} catch (error) {
    console.log("Se ha producido un error: " + error.message);
} finally {
    // Este bloque se ejecuta SIEMPRE
    console.log("Operación finalizada. Limpieza realizada.");
}
 
/*DIFICULTAD EXTRA*/

for(i = 10; i <= 55; i++){
    if(i % 2 == 0 && i != 16 && i % 3 != 0){
        console.log(i);
    }
}




