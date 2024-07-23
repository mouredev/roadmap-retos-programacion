//funciones basicas
//una funcion es un bloque de codigo para reutilizar algun accion 
//def por el usuario

//simple
function greet(){
    console.log("hola javascipt")
}
greet();
// Funcion sin parametro ni retorno
function saludar() {
    console.log("Hola, Javascript!")
}

saludar();

// Funcion con un parametro y sin retorno

function saludo(nombre){
    console.log(`hola, ${nombre} bienvenido`)
}
saludo("quique")

function ejemplo(nombre){
    console.log(`hola, ${nombre} bienvenido`)
}
ejemplo();


// Funcion con varios parametros y con retorno
function sumar(a, b) {
    return a + b;
}

let resultado = sumar(5, 10);
console.log("El resultado es:", resultado);

//Funcion con varios parametros
function variosParametros(...args){
    for(let i = 0; i<args.length;i++){
        console.log(args[i])
    }
}

//ejercicio con varios parametros 
function varpar(...args){
    for(i=0;i<args.length;i++){
        console.log(args[i])
    }
}
variosParametros(1, 2, 3, 4)
varpar(2,3,4,5);

//Funciones anidadas
function funcionUno(){
    console.log("Hola desde funcionUno");

    function funcionDos(){
        console.log("Hola desde funcionDos")
    }

    funcionDos(); //Estamos llamando la funcion dos dentro de funcionUno por lo que si funciona
}
funcionUno();

//dificultad extra

function padre(a, b) {
    let contador = 0;
    for (let i = 1; i <= 100; i++) {
        if (i % 3 === 0 && i % 5 === 0) {
            console.log(`${a}, ${b}`);
        } else if (i % 3 === 0) {
            console.log(a);
        } else if (i % 5 === 0) {
            console.log(b);
        } else {
            console.log(i);
            contador++;
        }
    }
    console.log("Numeros en lugar de texto :");
    return contador;
}

console.log(padre('fizz', 'buzz'));
