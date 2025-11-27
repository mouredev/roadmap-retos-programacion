const num1  = 10;
const num2 =5;

//Funcion sin parametros
function suma(){
    console.log("La suma es: " + (num1 + num2));
}
suma();

//Funcion con parametros
function sumaPara(a, b) {
    console.log("La suma con parametros es: " + (a + b));
}
sumaPara(num1, num2);


//Funcion con parametros y retorno
function sumaParaRetorno(a, b) {
    return a + b;
}
let resultado2 = sumaParaRetorno(num1, num2);
console.log("La suma con parametros y retorno es: " + resultado2);

//Funcion Anonima
const resta = function(a, b) {
    return a - b;
};
let resultado3 = resta(num1, num2);
console.log("La resta con funcion anonima es: " + resultado3);

//Funcion Flecha
const multipliacion = (a,b) => a * b;
let resultado4 = multipliacion(num1, num2);
console.log("Resultado de multipliacion: " + resultado4);

//Funcion dentro de otra funcion
function funcionE(a){
    function funcionI(z){
        return z *3 *2;
    }
    return funcionI(a);
}
let resultado5 = funcionE(4);
console.log("Resultado de funcion dentro de otra funcion: " + resultado5); 

//Funciones ya creadas
let nombre = "Leandro";
let longitud = nombre.length;
console.log("La longitud del nombre es: " + longitud);

let fecha = new Date();
console.log("Fecha actual: " + fecha.toDateString());

//Variable Global y Local
let variableGlobal = "Soy una variable global";
function mostrarVariable() {
    let variableLocal = "Soy una variable local";
    console.log(variableLocal);
} 

console.log(variableGlobal);

//Difucultad extra 

function extraDificultad(a, b) {
    let numNormales = 0 ;
    for (let i = 1; i <=100; i++) {
        if (i % 3 === 0 && i%5 === 0)   {
            console.log (a + b);
        } else if (i % 3 === 0) {
            console.log (a);
        } else if (i % 5 === 0) {
            console.log (b);
        } else {
            console.log(i);
            numNormales++; 
        }
    }
    return numNormales;
}

let resultadoExtra = extraDificultad("Hola", "Mundo");
console.log("Cantidad de numeros normales impresos: " + resultadoExtra);