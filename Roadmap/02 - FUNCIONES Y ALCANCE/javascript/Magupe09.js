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



// FUNCIONES SIN PARAMETRO NI RETORNO
function saludar(){
    console.log("Hola soy Mauricio y cada dia soy un mejor programador")
}

saludar();// de esta manera invoco la funcion sin algumentos ni retorno .


function mostrarFecha() {
    let fecha = new Date();
    console.log(`La fecha y hora actual es: ${fecha}`);
}

// Llamada a la función
mostrarFecha();

//------ 

//FUNCIONES CON RETORNO

function sumar(a, b) {
    return a + b;
}

// Llamada a la función
let resultado = sumar(3, 4);
console.log("La suma es:", resultado);  // La suma es: 7


function dobleDelNumero(numero){
    return numero*2;
}

console.log(dobleDelNumero(5));// 10


//--------

//FUNCIONES CON UN PARAMETRO Y VARIOS PARAMETROS


function esMayorDeEdad(edad){
    if(edad < 18){
        console.log("Eres menor de edad No puedes ingresar a este antro");
    }else{
        console.log("Bienvenid@ a este club");
    }

}
esMayorDeEdad(16);

function sumarVariosNumeros(a,b,c){
    return resultado= a+b+c;
}
console.log(sumarVariosNumeros(2,5,6))




// COMPROVAMOS SI PODEMOS CREAR UNA FUNCION DENTRO DE OTRA FUNCION


function funcionExterna(a,b){
    function funcionInterna(){
        console.log("La suma de los valores es :", a+b)
    }

    funcionInterna();   // Esta es la llamada a ejecucion de la funcion interna.
}

funcionExterna(2,2);// Desde fuera la unica funcion que se ejecuta es la externa.


// PONIENDO A PRUEBA EL CONCEPTO DE VARIABLE LOCAL Y VARIABLE GLOBAL

let edad = 20; // Variable de alcanze global

function mayorDeEdad(edad){
    let nombre= "Mauricio"; // variable de alcanze local, quiere decir que solo la puedo utilizar dentro de esta funcion.
    if(edad > 18){ // Aqui justo leo la variable declarada en el scop global 
        console.log("ERES MAYOR DE EDAD",nombre); 
    }

    console.log(nombre,"ESTOY DENTRO")// Aqui si que funcion ESTOY DENTRO DE LA FUNCION

}
mayorDeEdad(edad);
// vamos a comprobar que la variable nombre no puede leerse desde fuera.
console.log(edad)
// console.log(nombre)// Esto ejecuta un error en consola diciendo que no se puede ejecutar por que no esta definida 


/*
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


function numeroDeVecesIngresadoEnLugarDeLosTextos(a,b){
    let contador=0;
    for(let i=1;i <= 100;i++)
        {

          if(i % 3 === 0 && i % 5 === 0)
            {
                console.log(a+b,"soy multiplo de los 2",i)
            
           }else if(i % 5 === 0)
            {
                console.log(b)
            }else if(i % 3 === 0)
                {
                    console.log(a,"soy multiplo de 3",i);
                    
                }else
                {
                    contador= contador+1;
                    
                }
        }
         
       
    
    return console.log(contador);
    
}

numeroDeVecesIngresadoEnLugarDeLosTextos("string1","string2")