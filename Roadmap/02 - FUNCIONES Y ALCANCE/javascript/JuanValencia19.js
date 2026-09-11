//Tipos de funciones y sus alcances

/*Funcion sin parametros ni retorno
funciona como un interruptor que enciende un bombillo, cumple con hacer una acción y ya
*/

// Declaración
function saludar() {
    console.log("¡Hola! Bienvenido a JavaScript.")
}

// Llamada a la función
saludar() // Muestra: ¡Hola! Bienvenido a JavaScript.
saludar() 

//Funcion con parametros (sin retorno)
function presentarPersona(nombre, edad) {
    console.log("Me llamo " + nombre + " y tengo " + edad + " años.")
}

presentarPersona("Ana", 25);  // Me llamo Ana y tengo 25 años.
presentarPersona("Carlos", 30); // Me llamo Carlos y tengo 30 años.

//Función con retorno
function sumar(a, b) {
    const resultado = a + b
    return resultado;  // Devuelve el valor
}

const miSuma = sumar(5, 3) // Guardamos lo que devuelve
console.log(miSuma)        // 8
console.log(sumar(10, 20))   // 30 (también podemos usarlo directamente)

//Importante: Todo lo que se ejecute despues del return no entra dentro de la función
function ejemplo() {
    console.log("Esto sí se ve")
    return "Resultado"
    console.log("Esto NUNCA se verá") // Código inalcanzable
}

//Funciones con parametros y con retorno(con todo)
function calcularAreaRectangulo(base, altura) {
    return base * altura
}

const area = calcularAreaRectangulo(5, 3);
console.log("El área es: " + area) // 15

//Valores por defecto en los parametros
function crearSaludo(nombre, saludo = "Hola") {
    return saludo + ", " + nombre + "!"
}

console.log(crearSaludo("Ana"))          // Hola, Ana! (usa valor por defecto)
console.log(crearSaludo("Carlos", "Buenos días")); // Buenos días, Carlos!

//Funcion dentro de funcion
function calculadoraAvanzada(a, b) {
    // Función interna (solo visible dentro de calculadoraAvanzada)
    function elevarAlCuadrado(x) {
        return x * x
    }
    
    const suma = a + b
    const sumaAlCuadrado = elevarAlCuadrado(suma); // Usamos la función interna
    
    console.log("Suma: " + suma);
    console.log("Suma al cuadrado: " + sumaAlCuadrado);
}

calculadoraAvanzada(3, 4)
// Suma: 7
// Suma al cuadrado: 49

// elevarAlCuadrado(5); // ❌ Error: no existe fuera de su función padre


//Scope: Variables globales y variables locales
// Variable GLOBAL (accesible desde cualquier parte)
const mensajeGlobal = "Soy visible en todo el programa";

function probarAlcance() {
    // Variable LOCAL (solo existe dentro de esta función)
    const mensajeLocal = "Solo existo dentro de esta función";
    
    console.log(mensajeGlobal)// ✅ Funciona: "Soy visible en todo el programa"
    console.log(mensajeLocal)  // ✅ Funciona: "Solo existo dentro de esta función"
}

probarAlcance();

console.log(mensajeGlobal) // ✅ Funciona
// console.log(mensajeLocal);   ❌ Error: mensajeLocal no está definida fuera de la función

//Funciones creadas por el lenguaje
// parseInt y parseFloat (convertir texto a número)
console.log(parseInt("42"))       // 42
console.log(parseFloat("3.14"))  // 3.14

// isNaN (¿no es un número?)
console.log(isNaN("Hola"))      // true
console.log(isNaN(42))           // false

// Math (objeto con funciones matemáticas)
console.log(Math.random())       // Número aleatorio entre 0 y 1
console.log(Math.floor(3.9))     // 3 (redondear hacia abajo)
console.log(Math.ceil(3.1))       // 4 (redondear hacia arriba)
console.log(Math.round(3.5))     // 4 (redondear al más cercano)
console.log(Math.max(10, 20, 5))  // 20 (el mayor)
console.log(Math.min(10, 20, 5))  // 5 (el menor)

// String (métodos de cadenas, ya vimos algunos)
console.log("javascript".toUpperCase()); // "JAVASCRIPT"
console.log("Hola".length);              // 4

//Ejercicio de practica
let saldo = 1000
console.log("Saldo inicial: "+ saldo)

function consultarSaldo(){
    return "El saldo actual es:"+ saldo
}

function depositar(cantidad){
     saldo += cantidad
     console.log("Depositando... " + cantidad)
     console.log(consultarSaldo())
}

function retirar(cantidad){
    // Mejor validación: primero ver si hay saldo (no solo si es <= 0)
    if (cantidad > saldo){
        console.log("No se puede retirar " + cantidad + " porque excede el saldo disponible")
        return false
    }
    else if (saldo <= 0){
        console.log("No hay saldo disponible")
        return false
    }
    else {
        saldo -= cantidad
        console.log("Retirando... " + cantidad)
        console.log(consultarSaldo())
        return true
    }
}

consultarSaldo()
depositar(500)
retirar(200)
retirar(2000)

//Dificultad extra
function retoExtra(cadena1 = "", cadena2 = ""){
    let contadorNumero = 0
    for(let i=1;i <=100; i++){
        if(i % 3 === 0 && i % 5 === 0){
            console.log(cadena1 + cadena2)
        }
        else if(i % 3 === 0){
            console.log(cadena1)
        }
        else if(i % 5 === 0){
            console.log(cadena2)
        }
        else {
            contadorNumero++
        }
    }
    return contadorNumero
}

console.log("Número de veces que se imprimió el número:", retoExtra("texto1", "texto2"))
