/*
Funciones 
*/

//Función Simple 
//No tiene parametros ni retorno.
function primero () {
    console.log("Hola Mundo");
}
primero(); //Se llama la Función

function sumar(num1, num2) {
    var resultado = num1 + num2;
    console.log("La suma es: " + resultado);
}

sumar(5, 3); // Llamada a la función


//Funciones con parámetros y valor de retorno.

function areaCasa (largo, ancho) {
    let area = largo * ancho;
    return area;
}
let resultado = areaCasa(200, 250); //Aca llamamos a la función y lo guardamos dentro de una variable let.
console.log("El area de la casa es de: " + resultado + " metros cuadrados"); //Imprimimos el resultado.

//Con argumento

function agr_name (name) {
    console.log("Que tal" + name)
}
agr_name(" Jose");

function agr_name2 (greet, name) {
    console.log(greet + name);
}
agr_name2("Hola ", " Samuel");
//Pasarlos en orden inverso
agr_name2(greet="Hola ", name="Samuel");

//argumento predeterminado

function arg_predeterminado (name="No se sabe") {
    console.log("Hola " + name);
}
arg_predeterminado("Jose");
arg_predeterminado();

//Argumento y Retorno.
function return_arg (greet, name) {
    return greet + name;
}
console.log(return_arg("Hola ", "Carlos"))

// Retorno con varios valores.
function multiple_returns () {
    return "Como", "Vas"
}
greet, name = multiple_returns()
console.log(name)
console.log(greet)

//Con un numero variable de argumentos.
function argumentosVariables (...names) {
    for (name in names) {
        console.log("Hola " + names[name]);
    }
}
argumentosVariables("Jose", "Carlos", "Maria");

//Un numero Variable de argumentos con claves

function imprimirDatos(...datos) {
    for (let dato of datos) {
    console.log(`Nombre: ${dato.nombre}, Edad: ${dato.edad}`);
    }
}
imprimirDatos({ nombre: 'Juan', edad: 20 });
imprimirDatos({ nombre: 'María', edad: 25 }, { nombre: 'Pedro', edad: 30 });

/* 
Funciones dentro de Funciones.
- Comprueba si puedes crear funciones dentro de funciones.
*/

function externa () {
    function interna () {
        console.log("Hola Mundo");
    }
    interna();
}
externa();

/* 
Variables locales y globales.
- Comprueba si puedes crear variables locales y globales.

Una Varaible global es que tiene un ambito por fuera donde lo queremos ejecutar, es decir, se puede llamar desde
cualquier lado del codigo y poder usarlo, se hace como un orden jerardico, ya que esta global se encuentra por 
fuera / encima de donde queremos usarlo (Funcion).

Una Variable local funciona solo dentro del ambito de la funciónde donde se ha creado. Y solo existe dentro de esta misma.
Si la llamamos por fuera, no lo podremos hacer por que aparece como que no existe.

Tanto locales como Globales son sus propios mundos en estos sentidos.
*/
let global_var = "Carne";

function carneDeMercado (){
    let local_var = "Pollo";
    console.log(global_var);//Aca se llama eta variable que se encuentra por fuera de la función (Global).
    console.log(local_var);//Aca se llama esta variable que se encuentra dentro de la función y solo existe ahi (Local)
}
carneDeMercado();//Intentar restringir al maximo el codigo.

/*
DIFICULTAD EXTRA
 DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
*/
function extra (texto1, texto2) { 
    for (let i=1; i<=100; i++ ) {
        if (i%3==0 && i%5==0) { //Multiplo de 3 y 5
            console.log(i + " Es " + texto1 + " y " + texto2);
        }
        else if (i%3==0) { //Sera multiplo si se divide entre 3 
            console.log(i + " Es " + texto1);
        } else if (i%5==0) { //Sera multiplo si se divide entre 5   
            console.log(i + " Es " + texto2);
        } else {
            console.log(i); //Para los numeros que estan por fuera de esas condiciones.
        }
    }
}
extra("Multiplo de 3 ", "Multiplo de 5 ")

//Reto Completado :D
