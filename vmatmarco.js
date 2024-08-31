/* Tipos de operadores en JavaScript */

// Operadores aritméticos
let suma = 1 + 2;
let resta = 3 - 1;
let multiplicacion = 2 * 4;
let division = 10 / 2;
let modulo = 10 % 3;

// Operadores de asignación
let x = 5;
x += 2; // x = x + 2;
x -= 3; // x = x - 3;
x *= 4; // x = x * 4;
x /= 2; // x = x / 2;
x %= 3; // x = x % 3;

// Operadores de comparación
let a = 5;
let b = 10;
console.log(a == b); // false
console.log(a != b); // true
console.log(a > b); // false
console.log(a < b); // true
console.log(a >= b); // false
console.log(a <= b); // true

// Operadores lógicos
let c = true;
let d = false;
console.log(c && d); // false
console.log(c || d); // true
console.log(!c); // false

// Operadores de concatenación
let nombre = "John";
let apellido = "Doe";
let nombreCompleto = nombre + " " + apellido;
console.log(nombreCompleto); // "John Doe"

// Operador ternario
let edad = 18;
let mensaje = (edad >= 18) ? "Eres mayor de edad" : "Eres menor de edad";
console.log(mensaje); // "Eres mayor de edad"

// Operador de tipo
let numero = 10;
console.log(typeof numero); // "number"


/* Estructuras de control */

// Estructuras condicionales
let numero1 = 5;  // numero1 = 5
let numero2 = 10; // numero2 = 10
if (numero1 > numero2) {
    console.log("numero1 es mayor que numero2");
} else if (numero1 < numero2) {
    console.log("numero1 es menor que numero2");
} else {
    console.log("numero1 es igual a numero2");
}


/* Estructuras de repetición */

// Bucle FOR
for (let i = 0; i < 10; i++) {
    console.log("El valor de i es: " + i);
}

// Bucle WHILE
let i = 0;
while (i < 10) {
    console.log("El valor de i es: " + i);
    i++;
}

// Bucle DO-WHILE
let j = 0;
do {
    console.log("El valor de j es: " + j);
    j++;
} while (j < 10);

// Estructura de control SWITCH
let dia = "Miércoles";  // Cambia este valor para probar diferentes casos

switch (dia) {
    case "Lunes":
        console.log("Hoy es Lunes");
        break;
    case "Martes":
        console.log("Hoy es Martes");
        break;
    case "Miércoles":
        console.log("Hoy es Miércoles");
        break;
    case "Jueves":
        console.log("Hoy es Jueves");
        break;
    case "Viernes":
        console.log("Hoy es Viernes")
        break;
    case "Sábado":
        console.log("Hoy es Sábado")
        break;
    case "Domingo":
        console.log("Hoy es Domingo")
        break;
    default:
        console.log("El valor no corresponde a un día de la semana")
}

// Estructura de control de errores TRY/CATCH
try
{
document.write(10/variable1) ; //Variable insegura del usuario (puede introducir un 0)
}catch(e)
{
alert(e.message); // Mensaje en caso de error
}



/* DIFICULTAD EXTRA */

for(i = 1; i<56; i++){
    if(i % 2 === 0 && i !== 16 && i%3 !== 0){
        console.log(i);
    }
}