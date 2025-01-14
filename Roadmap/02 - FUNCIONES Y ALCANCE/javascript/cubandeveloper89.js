//   ***   FUNCIONES    ***
// funciones sin parámetros ni retorno
function myFunct() {
    console.log("myFunt es una función que no requiere parámetros");
}
myFunct(); //invoco la funcion
// funciones con parámetros pero sin retorno
function my2Funct(name) {
    console.log("Hola, " + name + ", my2Funct si que requiere un parámetro, tu nombre");
}
my2Funct("John");
// Funciones flecha
var my3Funct = function () {
    console.log("my3Funct es una funcion flecha, simplemente otrra manera de denominar una funcion");
};
my3Funct();
// Dos o mas parámetros en una funcion, el tercero es opcinal
var my4Funct = function (a, b, c) {
    var result = 0;
    if (c) {
        result = a + b + c;
    }
    else {
        result = a + b;
    }
    console.log("my4Funct toma 2 parametros y los suma: " + result);
};
my4Funct(10, 5, 7);
// Función con return
var my5Funct = function () {
    return "my5Funct es una función con RETURN";
};
console.log(my5Funct());
// Función dentro de funciones
var my6Funct = function () {
    function innerFunct() {
        console.log("Esta función se ejecuta dentro de my6Funct");
    }
    innerFunct();
};
my6Funct();
// Funciones propias del lenguaje
console.log("1- El mismo console.log() es una funcion del lenguaje");
var words = "2- We all can work together and make this world a better place";
console.log(words.toUpperCase());
// Variable global y local
var global = "global";
var my7Funct = function () {
    var local = "local";
    return "la variable ".concat(global, " esta fuera del scope de la funcion mientras que ").concat(local, " solo existe aqui dentro");
};
console.log(my7Funct());
//  *** Ejercicio EXTRA ***
console.log("     *** Ejercicio Extra ***");
var extraFunct = function (param1, param2) {
    var count = 0;
    for (var index = 1; index <= 100; index++) {
        if (index % 3 == 0 && index % 5 == 0) {
            console.log(param1 + " y " + param2);
            count++;
            continue;
        }
        else if (index % 3 == 0) {
            console.log(param1);
            count++;
            continue;
        }
        else if (index % 5 == 0) {
            console.log(param2);
            count++;
            continue;
        }
        console.log(index);
    }
    console.log("Se cambio por letras " + count + " veces");
    return count;
};
extraFunct("hola", "adios");
