/*
 * EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 */

/*FUNCIONES*/
//Sin parametros:
console.log(`==========`);
console.log(`Funcion sin marametros:`);
function parameterLess (){
    let upshot = 6+3;
    console.log(`Esta funcion no tiene nigun parametro,
en su interior realiza la suma de dos numeros prestablecidos,
'6+3', cuyo resultado es ${upshot}`);
}
parameterLess()
console.log(`==========`);

//Con un parametro:
console.log(`==========`);
console.log(`Funcion con un marametro: numero`);
function oneParameter(number){
    let upshot= number*number;
    console.log(`Esta funcion tiene un parametro,
en su interior realizamos la multiplicacion de el parametro por si mismo (cuadrado),
en su llamada establecemos en valor del parametro en este caso ${number}.
'${number}*${number}', cuyo resultado es ${upshot}`);
}
console.log(`==========`);
oneParameter(5)
console.log(`==========`);
oneParameter(10)
console.log(`==========`);
oneParameter(20)
console.log(`==========`);

console.log(`==========`);
console.log(`Funcion con un marametro: string`);
function oneParameter(name){
    let upshot= `Hola, Bienvenido ${name}`;
    console.log(`Esta funcion tiene un parametro,
en su interior realizamos concatenacion de el nombre pasado por parametor ${name},
y el mensaje de bienbenida 'Hola, Biembenido', cuyo resultado es ${upshot}`);
}
console.log(`==========`);
oneParameter("Alberto")
console.log(`==========`);
oneParameter("Juan")
console.log(`==========`);
oneParameter("Fernando")
console.log(`==========`);

//Con varios parametros:
console.log(`==========`);
console.log(`Funcion mas de un parametro:`);
function moreThanOneParameter(number1,number2){
    let upshot= number1**number2;
    console.log(`Esta funcion tiene mas de un parametro,
en su interior realizamos la exponeiciación de number1 elevado a number2,
en su llamada establecemos en valor del los parametros en este caso ${number1}, ${number2}.
'${number1}*${number2}', cuyo resultado es ${upshot}`);
}
console.log(`==========`);
moreThanOneParameter(5,3)
console.log(`==========`);
moreThanOneParameter(2,8)
console.log(`==========`);
moreThanOneParameter(20,3)
console.log(`==========`);

//Con retorno:
console.log(`==========`);
console.log(`Funcion con un marametro y retorno: string`);
function oneParameterAndReturn(name){
    let upshot= `Hola, Bienvenido ${name}`;
    console.log(`Esta funcion tiene un parametro y retorno,
en su interior realizamos concatenacion de el nombre pasado por parametor ${name},
y el mensaje de bienbenida 'Hola, Biembenido', cuyo resultado es ${upshot},
y lo devolvemos por return, retorno para poder utilizarlo fuera de la a nuestro antojo.`);
    return upshot;
}
console.log(`==========`);
console.log(`Retorno: ${oneParameterAndReturn("Brais")}`)
console.log(`==========`);
console.log(`Retorno: ${oneParameterAndReturn("Jorge")}`)
console.log(`==========`);
console.log(`Retorno: ${oneParameterAndReturn("Jaime")}`)
console.log(`==========`);

console.log(`==========`);
console.log(`Funcion mas de un parametro y retorno:`);
function moreThanOneParameterAndReturn(number1,number2){
    let upshot= number1**number2;
    console.log(`Esta funcion tiene mas de un parametro y retorno,
en su interior realizamos la exponeiciación de number1 elevado a number2,
en su llamada establecemos en valor del los parametros en este caso ${number1}, ${number2}.
'${number1}*${number2}', cuyo resultado es ${upshot},
y lo devolvemos por return, retorno, para poder utilizarlo fuera de la a nuestro antojo.`);
    return upshot
}
console.log(`==========`);
console.log(`Retorno: ${moreThanOneParameterAndReturn(6,2)}`)//imprimimos directamente por consola el retorno.
console.log(`==========`);
console.log(`Retorno: ${moreThanOneParameterAndReturn(8,16)}`)
console.log(`==========`);
let retorno = moreThanOneParameterAndReturn(2,30);//almacenamos en una varialbe el retorno.
console.log(`Retorno: ${retorno}`)//imprimimos la variable que contiene el valor de retorno.
//console.log(upshot) //upshot no exixte fuera de la funcio.
console.log(`==========`);

//Funciones a alas que pasamos objetos o arrays como parametros:
console.log(`==========`);
console.log(`Funcion con objeto como argumento/parametro:`);
function myFunc(theObject) {
    theObject.make = 'Volkswagen';//Cambia el valor con clave make del objeto
    theObject.model = 'Golf';//cambia el valor con clave model del objeto
    theObject.year = 1992;//Cambia el valor con clave year del objeto
}
let mycar = { make: 'Honda', model: 'Civic', year: 2000 };//definimos objeto.
console.log(`El objeto inicial es: mycar = ${JSON.stringify(mycar)}`);//utilizamos el motodo JSON.stringify() para poder visualizar el objeto.
console.log(`==========`);
myFunc(mycar)
console.log(`function myFunc(theObject) {
    theObject.make = 'Volkswagen';//Cambia el valor con clave make del objeto
    theObject.model = 'Golf';//cambia el valor con clave model del objeto
    theObject.year = 1992;//Cambia el valor con clave year del objeto
}
myfunc(mycar)`)
console.log(`El objeto tras ejecutar la funcion es: mycar = ${JSON.stringify(mycar)}`);//utilizamos el motodo JSON.stringify() para poder visualizar el objeto.
console.log(`==========`);

//Expresiones function:
/*
Si bien la declaración de función anterior sintácticamente es una declaración, las funciones también se pueden crear mediante una expresión function.
Esta función puede ser anónima; no tiene por qué tener un nombre.
Sin embargo, puedes proporcionar un nombre con una expresión function. 
Proporcionar un nombre permite que la función se refiera a sí misma y también facilita la identificación de la función en el seguimiento de la pila de un depurador
*/ 
//Expresion function anonima:
console.log(`==========`);
console.log(`Exprecion Function anonima:`);
const square = function (number){
    return number * number
}

let upshot1 = square(5);
let upshot2 = square(10);
let upshot3 = square(90);
console.log(`La fucnion: 
const square = function (number){
    return number * number
}
es anonima, y la llamamos refiriendonos al nombre de la constante que la contiene.
square(5) = ${upshot1}.
square(10) = ${upshot2}.
square(90) = ${upshot3}.`)
console.log(`==========`);
console.log(`==========`);
console.log(`Exprecion Function con Nombre: permite referise a si misma, y asi usarse como funcion recursiva,
ya que se pueden anidar funciones dentro de funciones.`);
const factorial = function fac(n) {
    return n < 2 ? 1 : n * fac(n - 1);
};
upshot1 = factorial(3);
upshot2 = factorial(8);
upshot3 = factorial(31);
console.log(`
const factorial = function fac(n) {
    return n < 2 ? 1 : n * fac(n - 1);
};
factorial(3) = ${upshot1};
factorial(8) = ${upshot2};
factorial(31) = ${upshot3};
`);
console.log(`==========`);

//Alcande: Global o Local.
console.log(`==========`);
var globalVar = "esta es una variable global"
function globalScope (typevar){
    let localVAr = typevar + globalVar
    return localVAr
}
console.log(globalScope("Puedo usar dentro la variable poque "))
//console.log(localVAr)//descomentar para ver error.
console.log(`pero no podemos acceder a la variable localVar, porque esta definida en ambito local.`)
console.log(`==========`);

// Las siguientes variables se definen en el ámbito global
console.log(`==========`);
var num1 = 20,
num2 = 3,
name = "alberto";

// Esta función está definida en el ámbito global
function multiply() {
    return num1 * num2;
}

console.log(`Las variables glovales pueden usarse en funciones definidas en ambito gloval,
/ Las siguientes variables se definen en el ámbito global
var num1 = 20,
num2 = 3,
name = "alberto";

// Esta función está definida en el ámbito global
function multiply() {
    return num1 * num2;
}
por eso devuelve ${multiply()}`); // Devuelve 60
console.log(`==========`);

// Un ejemplo de función anidada
console.log(`==========`);
function getScore() {
    var num1 = 2,
    num2 = 3;
    
    function add() {
        return name + " Marco " + (num1 + num2);
    }
    
    return add();
}

console.log(`En este caso:
function getScore() {
    var num1 = 2,
    num2 = 3;
    
    function add() {
        return name + " Marco " + (num1 + num2);
    }
    
    return add();
}
podemos redeclarar las variables anteriores en ambito local, 
la funcion anidada, solo puede acceder a las variable de ambito gloval 
de su funcion madre,
por eso devuelve ${getScore()}`); // Devuelve "Chamahk anotó 5"
console.log(`==========`);

//Funciones predefinidas:
/*
* Existen funciones predefinidas en el leguaje que son llamadas metodos, las cuales posemos usar para resolver problemas concretos. 
* Como combersiones de tipo: parseInt() que combierte un valor a entero.
* Como representacion de objetos en str: JSON.stringify() que permite representar un objeto como cadena de texto, visto en algun ejemploanterior.
* y muchos mas.
*/
//ejemplo parseInt() y typeof():
console.log(`==========`);
console.log(`Funciones o Metodos predefinidos del leguaje:`);
let str1 = "2";
console.log(`Ahora la variable es ${str1} de tipo ${typeof(str1)}, usando el metodo typeof() que nos muestra el tipo de dato que contiene la variable.`);
str1=parseInt(str1);
console.log(`tras usar parseInt(str1) ahora la variable es ${str1} de tipo ${typeof(str1)}`);
console.log(`==========`);

//extra:
/*
* DIFICULTAD EXTRA (opcional):
* Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
* - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
*   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
*   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
*   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
*   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
*/
console.log(`==========`);
console.log(`DIFICULTAD EXTRA:`);
function difExtra(str1, str2){
    let counter=0;
    for (let num = 1; num<=100; num++){
        if (((num%3) === 0) && ((num%5) ===0)){
            console.log(str1+" "+str2);
        }else if ((num%5)===0){
            console.log(str2);
        }else if ((num%3)===0){
            console.log(str1);
        }else{
            console.log(num);
            counter++;
        }
    }
    return counter;
}
console.log(`El numero se ha impreso ${difExtra("Chanchito","Feliz")} veces.`)
console.log(`==========`);



