//Asignaciones
let a = 200
let b = 40

//Operadores aritméticos
suma = a + b
console.log("Suma a + b: " + suma)
resta = a - b
console.log("Resta a - b: " + resta)
multiplicacion = a * b
console.log("Multiplicación a * b: " + multiplicacion)
division = a / b
console.log("División a / b: " + division)
resto = a % b
console.log("Resto a % b: " + resto)

//Asignación compuesta
suma += a 
console.log("suma = suma + a: " + suma)
resta -= a 
console.log("resta = resta - a: " + resta)
multiplicacion *= a 
console.log("multiplicacion = multiplicacion * a: " + multiplicacion)
division /= a 
console.log("division = division / a: " + division)
resto %= a 
console.log("resto = resto % a: " + resto)

//Operadores lógicos
AND = (a < b) && (b === 0)
console.log("¿Es a menor que b, Y b igual a 0?: " + AND)
OR = (a > b) || (b === 0)
console.log("¿Es a mayor que b, O b igual a 0?: " + OR)
NOT = !(a < b)
console.log("Negación a menor que b: " + NOT)

//Operadores de comparación 
igual = (a === b)
console.log("Es igual: " + igual)
distinto = (a !== b)
console.log("Es distinto: " + distinto)
mayor = (a > b)
console.log("Es mayor: " + mayor)
mayorIgual = (a >= b)
console.log("Es mayor o igual: " + mayorIgual)
menor = (a < b)
console.log("Es menor: " + menor)
menorIgual = (a <= b)
console.log("Es menor o igual: " + menorIgual)

//Estructuras condicionales
//IF - ELSE 
let edad = 18

if (edad >= 18) {
  console.log("Eres mayor de edad")
} else {
  console.log("Eres menor de edad")
}

// IF ELSE 
if (edad > 18) {
  console.log("Eres mayor de edad")
} else if (edad === 18) { 
  console.log("Tienes la edad justa")
} else {
  console.log("Eres menor de edad")
}

//SWITCH 
let comision = "A"
switch (comision) {
  case 'A':
    console.log("Eres de la comisión A")
    break;
  case "B":
    console.log("Eres de la comisión B")
    break;
  case "C":
    console.log("Eres de la comisión C")
    break;
  default:
    console.log("Comisión inválida")
}

//Estructuras iterativas
let num = 200

// FOR
for (i = 1; i <= 5; i++) {
    num+=2
    console.log(num)
}

//WHILE
while (num < 300) {
    num+=5
    console.log(num)
}

// DO WHILE
do {
    num+=10
    console.log(num)
} while (num < 350);

// Try catch
try {
    let divError = 5 / 0;
    console.log("Resultado: ", divError);
} catch (error) {
    console.log("Error: ", error.message);
} finally {
    console.log("Se finalizó la ejecución, con error o no");
}

/* DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */

for (i = 10; i <= 55; i++) {
    if ((i % 2 == 0) && (i !== 16) &&(i % 3 !== 0)) {
        console.log(i)
    }
}