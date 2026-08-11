/* ----- Crea ejemplos de funciones básicas que representen las diferentes
   posibilidades del lenguaje:
   Sin parámetros ni retorno, con uno o varios parámetros, con retorno */

   
// funcion sin parametros ni retornos
function saludar(){
    console.log("Holaaaaa!")
}
saludar();

// funcion con uno o varios parametros
const nombre = "Walter";
const apellido = "Valladares";
function nombre(nombre, apellido){
    console.log(`Mi nombre es ${nombre} ${apellido}`)
}

//Funcion con parametros y retorno
const number1 = 4;
const number2 = 2;
function numero(number1, number2){
    return number1 + number2;
}

//---- Comprueba si puedes crear funciones dentro de funciones.
function fun1(){
    console.log('--- Iniciando fun1 ---');
    console.log('Esta es la funcion numero 1');

    function fun2(){
        console.log('Esta es la funcion numero 2');
        function fun3(){
            console.log('Esta es la funcion numero 3');
        }
        fun3();
    }
    fun2();
    console.log('--- finaliza la fun2 ---');
}
console.log('Llamando a la fun1()');
fun1();

//---- Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
const texto = "Hola mundo, como estan?";
const mayusculas = texto.toUpperCase();// toUpperCase() convierte todo a mayusculas
const minusculas = texto.toLowerCase();// toLowerCase() convierte toto a minisculas

//---- Pon a prueba el concepto de variable LOCAL y GLOBAL.
let variableGloval = "Juan";// las variable globales son las que se declaran fuera de cualquier funcion
function Mynombre(){
    console.log(`Mi nombre es: ${variableGloval}`);
}

function calcularArea(base, altura){
    let variableLocal = base * altura;
    return variableLocal;
}
Mynombre();
calcularArea(5,10);



//  * DIFICULTAD EXTRA (opcional):
// Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
// Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
// - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
//   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
//   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
//   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
//   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
//
// Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
// Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.

functionExtra();
function functionExtra(cadtex1, cadtex2) {
    let contador = 0;

    for (let i = 1; i <= 100; i++) {
        if (i % 3 === 0 && i % 5 === 0) {
            console.log(cadtex1 + cadtex2);
        } else if (i % 3 === 0) {
            console.log(cadtex1);
        } else if (i % 5 === 0) {
            console.log(cadtex2);
        } else {
            console.log(i);
            contador++;
        }
    }

    return contador;
}

// Llamada con los parámetros
let vecesNumero = functionExtra("Hola", "Mundo");
console.log("Se imprimió el número " + vecesNumero + " veces");