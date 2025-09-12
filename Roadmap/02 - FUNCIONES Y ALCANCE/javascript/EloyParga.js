// FUNCIONES BÁSICAS EN JAVASCRIPT

// 1. Funcion sin parametros ni retorno
function saludoSimple(){
    console.log("Hola, JS");
}


// 2. Función con un parametro
function saludarNombre(nombre) {
    console.log(`Hola ${nombre}, buenos días`);
}


// 3. Función con varios parametros
function sumar (a , b){
    console.log(`La suma de ${a} + ${b} = ${a+b}`);
}


/** 4. Función con @return */
function restar (a , b){
    return a-b;
}
let resultado = restar(10,5);
console.log(`El resultado de 10 - 5 = ${resultado}`);


// 5. Función dentro de otra función
function calculadora(a , b){
    function multiplicar (x , y) {
        return x * y;
    }
    const suma = a+b;
    const multiplicacion = multiplicar(a, b); // llamada a la subfuncion
    console.log(`Suma : ${suma} , Multiplicación : ${multiplicacion}`);
}
calculadora(10,5);


// 6. Funciones prefinidas
let numeros = [1,2,3,4,5,];
console.log("Lista de numeros: ", numeros);
let numerosCuadrados =numeros.map((n) => n**2);
console.log("Numeros Cuadradosa ", numerosCuadrados);


//VARIABLES LOCALES Y GLOBALES
let variableGlobal = "Soy una variable global";

function alcance(){
    let variableLocal = "Soy una variable Local";
    console.log("VARIABLE: ", variableLocal);
    console.log("VARIABLE: ", variableGlobal);
}
alcance();
/** Esto da error : Porque @param variableLocal 
 *  no existe fuera del @method alcance() 
 */
// console.log(variableLocal);


// DIFICULTAD EXTRA : FUNCION MULTIPLOS

function fizzBuzz(fizz , buzz) {
    let cont = 0; // Contador que evalua cuantas veces se imprime números en vez de texto

    for (let i = 1; i<=100 ; i++){
        if (i % 3 === 0 && i % 5 === 0) {
            console.log(fizz,buzz); //Multiplo 3 y 5
        }else if(i % 3 === 0){
            console.log(fizz,)      //Multiplo 3
        }else if (i % 5 === 0) {
            console.log(buzz);      //Multiplo 5
        }else{
            console.log(i);         //No multiplo
            cont++; // Incrementa el contador
        }
    }

    return cont; //Retorna el total de numeros impresos
}

const impresos = fizzBuzz("Fizz", "Buzz");
console.log(`Total de numeros impresos en lugar de Texto ${impresos}`);
