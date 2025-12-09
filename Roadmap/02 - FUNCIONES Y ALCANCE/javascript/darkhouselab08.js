/*
 * EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 * posibilidades del lenguaje:
 * Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 */

// -----------------------------------------------------------------
// RESPUESTAS
// -----------------------------------------------------------------

// 1. FUNCIONES BÁSICAS

// A. Sin parámetros ni retorno 
// ejecuta una acción.
function saludar() {
    console.log("Hola! Soy una función básica.");
}
saludar(); // Llamada a la función

// B. Con parámetros
// Recibe datos ("input") para trabajar con ellos.
function saludarPersona(nombre, apellido) {
    console.log("Hola, " + nombre + " " + apellido + "!");
}
saludarPersona("Jorge", "Franco");

// C. Con retorno (Return)
// Devuelve un resultado ("output") que podemos guardar en una variable.
function sumar(a, b) {
    return a + b;
}
let resultadoSuma = sumar(5, 10);
console.log("El resultado de la suma es: " + resultadoSuma);


// 2. FUNCIONES DENTRO DE FUNCIONES (Nested Functions)

function funcionExterna() {
    console.log("Iniciando función externa...");
    
    function funcionInterna() {
        console.log(" -> Ejecutando función interna.");
    }
    
    funcionInterna(); // La externa llama a la interna
}
funcionExterna();


// 3. FUNCIONES YA CREADAS EN EL LENGUAJE (Built-in)
// JavaScript.

// Ejemplo: Math (Matemáticas)
let numeroAleatorio = Math.random(); // Genera un número entre 0 y 1
console.log("Número aleatorio generado: " + numeroAleatorio);

// Ejemplo: String (Texto)
let texto = "hola mundo";
console.log("Texto en mayúsculas: " + texto.toUpperCase());


// 4. VARIABLE LOCAL Y GLOBAL (El Alcance/Scope)

// Variable GLOBAL: Accesible desde cualquier parte del código.
let variableGlobal = "Soy GLOBAL (accesible por todos)";

function pruebaDeScope() {
    // Variable LOCAL: Solo existe DENTRO de esta función.
    let variableLocal = "Soy LOCAL (solo existo aquí)";
    
    console.log("Dentro de la función:");
    console.log("- " + variableGlobal); // Funciona
    console.log("- " + variableLocal);  // Funciona
}

pruebaDeScope();

console.log("Fuera de la función:");
console.log("- " + variableGlobal); // Funciona

// INTENTO DE ERROR (Para demostración):
try {
    console.log("- " + variableLocal); // ¡Esto fallará!
} catch (error) {
    console.log("ERROR: No puedo acceder a 'variableLocal' desde fuera. " + error.message);
}

// 5. BONUS: Funciones Flecha (Arrow Functions)
// Una forma moderna.
const multiplicar = (x, y) => {
    return x * y;
};
console.log("Multiplicación con Arrow Function: " + multiplicar(2, 3));