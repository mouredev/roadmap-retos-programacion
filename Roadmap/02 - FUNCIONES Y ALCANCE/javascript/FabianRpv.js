// Funciones y alcance


function saludar() {   // Funcion sin parametros ni retorno
    console.log('Hola, Soy Fabian Petit');
}

saludar();



function saludar2(nombre, apellido) {   // Funcion con parametros
    console.log(`Hola, Soy ${nombre} ${apellido}`);
}

let nombre = 'Fabian';
let apellido = 'Petit';

saludar2(nombre, apellido);



function saludar3(nombre, apellido) {   // Funcion con parametros y retorno
    return `Hola, Soy ${nombre} ${apellido}`;
}

console.log(saludar3(nombre, apellido));



const functionAnom = function() {  // Funcion anonima
    console.log('Hola, Soy Fabian Petit');
}

functionAnom();  



const functionArrow = (nombre, apellido) => console.log(`Hola, Soy ${nombre} ${apellido}`) // Funcion arrow

functionArrow(nombre, apellido);



function saludar4(nombre, apellido, saludo = "Hola") {  // Funcion con parametros por defecto
    console.log(`${saludo}, Soy ${nombre} ${apellido}`);
}

saludar4(nombre, apellido);
saludar4(nombre, apellido, "Buenos dias");



// Funcion dentro de otra funcion

function saludar5(nombre, apellido) {

    function getNombreCompleto() {
        return `${nombre} ${apellido}`;
    }

    console.log(`Hola, Soy ${getNombreCompleto()}`);
}

saludar5(nombre, apellido);


function saludar6(myFunction, parametro1, parametro2){
    myFunction(parametro1, parametro2);
}

saludar6(saludar5, 'Fabian', 'Petit');



// Funciones ya definidas en el lenguaje

let numero = 10.456789;
console.log(numero.toFixed(2));



// Variables locales y globales

let variableGlobal = 'Soy una variable global';

function mostrarVariables(){
    let variableLocal = 'Soy una variable local';
    console.log(variableGlobal);
    console.log(variableLocal);
}

mostrarVariables();

console.log(variableGlobal);
// console.log(variableLocal);  // Error



/* Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
- La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
- Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
- Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
- Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
- La función retorna el número de veces que se ha impreso el número en lugar de los textos.
*/

function imprimir(text1, text2){

    let contador = 0;

    for(let i = 1; i <= 100; i++){


        if (i % 3 == 0 && i % 5 == 0){
            console.log(`${text1} ${text2}`);
        }

        else if(i % 3 == 0){
            console.log(text1);
        }

        else if (i % 5 == 0){
            console.log(text2);
        }

        else {
            console.log(i);
            contador++;
        }

    }

    return `El numero de veces que se imprimio un numero fue de ${contador}`;

}

console.log(imprimir('Hola', 'Mundo'));