// EJERCICIO:
//      Crea ejemplos de funciones básicas que representen las diferentes posibilidades del lenguaje: Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
//  * - Debes hacer print por consola del resultado de todos los ejemplos.

// Sin parámetros ni retorno:
function myFunction(){
    console.log("Función básica");
}
myFunction();


// Varios parámetros y retorno
console.log("---------------------------------------------------------------")
function operacion(a, b, c){
    return `El resultado de (${a}+${b})*${c} es ${(a + b) * c}`;
}
let result = operacion(2,5,7);
console.log(result);

// Valores por defecto en parámetros
console.log("---------------------------------------------------------------")
function saludar(nombre = "Mundo!", saludo = "Hola") {
    return `${saludo}, ${nombre}!`;
}
console.log(saludar());


// Función Flecha
console.log("---------------------------------------------------------------")
let multiplicacion = (a, b) => a * b;
console.log(multiplicacion(5, 4));


// Función Anónima
console.log("---------------------------------------------------------------")
// No tiene nombre, se guarda en una variable
const anonima = function(){
    console.log("Función Anónima");
};
anonima();


//  * - Comprueba si puedes crear funciones dentro de funciones.
console.log("---------------------------------------------------------------")

function externa(nombre){
    function interna(){
        console.log(`Hola ${nombre}`)
    }
    interna();
}
externa("ant000o");


//  * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
console.log("---------------------------------------------------------------")
let fruta = "manzana"
console.log(`Tengo una ${fruta.toUpperCase()}`);


console.log("---------------------------------------------------------------")
//  * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
let global = "global" // se puede usar dentro y fuera de funciones
function newFunction(){
    let local = "local"; //solo se puede usar dentro de la funcion
    console.log(local + " + " + global);
}
newFunction();
console.log("---------------------------------------------------------------")
try{
    console.log(local + global)
}catch(error){
    console.log("Error:", error.message);
}finally{
    console.log("La variable local no se reconoce, ya que fue creada dentro de la funcion 'newFunction'.")
}


console.log("---------------------------------------------------------------")
//  * DIFICULTAD EXTRA (opcional):
//  * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
//  * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
//  *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
//  *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
//  *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
//  *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
//  *
//  * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
//  * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
//  */

function textNumbers(primero = "Hola", segundo = "Mundo!"){
    let contador = 0;
    for (let i = 1; i <= 100; i++){
        if (i % 3 === 0 && i % 5 === 0){
            console.log(`${primero} ${segundo}`)
        }else if(i % 5 === 0){
            console.log(`${segundo}`)
        }else if(i % 3 === 0){
            console.log(`${primero}`)
        }
        else{
            console.log(i)
            contador++
        }
} return contador
}
let resultado = textNumbers();
console.log("Se imprimió un número: " + resultado + " veces");