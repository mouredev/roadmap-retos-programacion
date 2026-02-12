/**
 * FUNCIONES DEFINIDAS POR EL USUARIO
 */

//A. Función sin parámetros ni retorno
function greet(){
    console.log("¡Esto es una funcion básica!");
}

greet();

//B. Función con parámetros y sin retorno
function suma(a, b){
    console.log(a + b);
}

suma(100, 60);

//C. Función sin parámetros y con retorno
function square(){
    let side = 5;
    return side * side;
}

formula = square();

//D. Función con parámetros y con retorno
function calcularIVA(precio){
    const baseIva = 0.19;
    return precio * baseIva;
}

calcularIVA(5200);

//E. Función Expresiva
const calcularArea = function(base, altura){
    return base * altura;
}

calcularArea(5, 10);

//F. Función de Flecha
const saludar = name => `Hola ${name}!`; //Un solo parámetro
const mensaje = saludar("Mundo");
console.log(mensaje);

const despedir = () => "Adiós"; //Sin parámetros
despedir();

const module = (a, b) => a % b; //Una línea
module(9, 3);

const multiplicar = (x, y) => {
    let operacion = x * y;
    return operacion;
}
multiplicar(5, 8);

//G. Función con Parámetros Predeterminados
function configPuerto(puerto = 3000){
    return `Puerto utilizado: ${puerto}`;
}

configPuerto();         //3000
configPuerto(5000);     //5000

//H. Función con Parámetros Rest
function consecutivo (...numeros){
    let total = "";

    for(const numero of numeros){
        total += `Número ${numero} \n`;
    };

    return total;
};

const menssage = consecutivo (1, 2, 3, 4, 5);
console.log(menssage);

//Funciones Anidadas
function outerFunction(name){
    //variable externa
    const output_message = "Hola";

    //Declaración funcion interna
    function innerFunction(){
        console.log(output_message + ", " + name);
    }

    //invocación de la funcion interna dentro de la externa
    innerFunction();
}

outerFunction("Diego");

/**
 * BUILT-IN OBJECTS
 */
parseInt('1010', 2); //10
parseFloat('3.1416'); //3.1416
isNaN('A'); //True
isNaN(1); //False
isFinite(Math.PI); //true
eval('2 + 2'); //4
let builtInObhects; //undefinied
Math.sqrt(16); //4
encodeURI("https://eltiempo noticias.co/"); //'https://eltiempo%20noticias.co/'
decodeURI("https://eltiempo%20noticias.co/"); //'https://eltiempo noticias.co/'

/**
 * DIFICULTAD EXTRA
 */
function printNumber(str1, str2){
    let contador = 0;

    for(let i = 1; i <= 100; i++){
        if(i % 3 === 0 && i % 5 === 0){
            console.log(str1 + str2);
        } else if(i % 3 === 0){
            console.log(str1);
        } else if(i % 5 === 0){
            console.log(str2);
        } else{
            console.log(i);
            contador += 1;
        }
    }

    return contador;
}

console.log(printNumber('Fizz', 'Buzz'));
