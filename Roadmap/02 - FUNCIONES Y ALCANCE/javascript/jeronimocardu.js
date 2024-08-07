// Funcion vacia
function vacio(){
    console.log('Hola soy una funcion sin parametros ni retorno');
}
vacio()

// Funcion con parametros y return
function completa(a, b){
    return `Hola soy una function y estoy retornando el parametro A: ${a} y B: ${b}`;
}
completa()

// funcion dentro de otra funcion
function funcion(){
    function segundaFuncion(){
        return 'Se puede crear funciones dentro de funciones';
    }
    console.log(segundaFuncion());
}
funcion();

// funcion ya creadas de JS 
function isNumber(a){
    if(!isNaN(a)){
        console.log('Es un numero!');
    } else{
        console.log('No es un numero!');
    }
}
isNumber(2);

// Variables locales y globales
let variableGlobal = 'Puedo ser usado de forma global';
function local(){
    let variableLocal = 'Soy una variable local';
    console.log(variableGlobal); // Funciona porque es global
    console.log(variableLocal); // Funciona porque está dentro de la funcion donde fue creada
}
// console.log(variableLocal) // No funciona porque es LOCAL
local();

// EXTRA
function extra(str1, str2){
    let veces = 0;
    for(let i = 1; i <= 100; i++){
        if(i%3 === 0 && i%5 === 0){
            console.log(i, str1,'y', str2);
            veces += 2;
        }else if(i%5 === 0){
            console.log(i, str2);
            veces++;
        }else if(i%3 === 0){
            console.log(i, str1);
            veces++;
        } else{
            console.log(i);
        }
    }
    return veces;
}
console.log(`Hay ${extra('Multiplo de 3', 'Multiplo de 5')} numeros multiplo de 3 y/o 5`);

