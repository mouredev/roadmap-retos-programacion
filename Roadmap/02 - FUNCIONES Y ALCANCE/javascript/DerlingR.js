function bienvenida() {
    console.log("Bienvenidos al ejercicio 02 de Lógica de Programación");
}

bienvenida();

function bienvenida2(especificacion) {
    console.log("Bienvenido al ejercicio 02 de Lógica de Programación, " + especificacion);
}

bienvenida2("Curso 02"); // Bienvenido al ejercicio 02 de Lógica de Programación, Curso 02

function sumar(a, b) {
    console.log(a +b);
}

sumar(5, 3); // El resultado será 8

function multiplicar(a, b) {
    return a * b;
}

let resultado = multiplicar(4, 7);
console.log(resultado); // El resultado será 28

function operacion(a, b) {
    function sumar(x, y) {
        return x + y;
    }
    function restar(x, y) {
        return x - y;
    }

    console.log("sumar:", sumar(a, b));
    console.log("restar:", restar(a, b));
}

operacion(10, 5);
//Muestra lo siguiente:
// sumar: 15
// restar: 5

let texto = "Javascript es un lenguaje de programación";
let longitud = texto.length;
console.log("Longitud del texto:", longitud); // Longitud del texto: 39

let numero = 9.5678
let numeroRedondeado = Math.round(numero);
console.log("Número redondeado:", numeroRedondeado); // Número redondeado: 10

let global = "Variable global";

function mostrarVariable() {
    let local = "Es una variable local";
    console.log(global); //Para acceder a la variable global
    console.log(local); //Para acceder a la variable local
}

mostrarVariable();
//Muestra:
//Par acceder a la variable global
//Es una variable local
