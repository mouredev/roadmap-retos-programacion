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


//funciones sin parametros , ni retornos 

function saludar(){
console.log("hola mundo");
};

saludar();


//varios parametros 
function calculadoraBasica(a,b,operador){

    switch(operador){
        case`suma`:
            console.log(`la suma es:` + (a + b));
        break;
        case`resta`:
            console.log(`la suma es:` + (a - b));
        break;
        case`multiplicacion`:
            console.log(`la suma es:` + (a * b));
        break;
        case`division`:
            console.log(`la suma es:` + (a / b));
        break;
        case`elevacion`:
            console.log(`la suma es:` + (a ** b));
        break;
        case`residuo`:
            console.log(`la suma es:` + (a % b));
        break;
        default:
            console.log("por favor ingresa un operador valido")
            break;
    }   
}

//resultados de la funcion con varios parametros demostrado en una calculadora basica
calculadoraBasica(7,10,"suma");//la suma es:17
calculadoraBasica(7,10,"resta");//la suma es:-3
calculadoraBasica(7,10,"multiplicacion");//la suma es:70
calculadoraBasica(7,10,"division");//la suma es:0.7
calculadoraBasica(7,10,"elevacion");//la suma es:282475249
calculadoraBasica(7,10,"residuo");//la suma es:7
calculadoraBasica(7,10,"ninguno");//la suma es:por favor ingresa un operador valido


//con retorno

const calcularRectangulo = (largo, ancho) => {

    const area = largo * ancho;
    return area;
};

console.log(calcularRectangulo(9,5));


//funciones dentro de funciones

//vamos a crear una funcion con ejemplo de motos

function caracteristicasDeMoto(marca,modelo){
    console.log(`${marca} ${modelo}`);

function detallesDeMoto(año,color){
    console.log(`Detalles: año ${año} color ${color}`);
    return `la marca de la moto es ${marca} de color ${color} , modelo ${modelo} del año ${año}`
};
    const res = detallesDeMoto(2024,`rojo`);
    console.log(`descripcion completa:`,res)
};

caracteristicasDeMoto(`yamaha`,`r1`);

// Utiliza algún ejemplo de funciones ya creadas en el lenguaje.

const numeros = [1,2,3,4,5,6,7,8];

const numerosMultiplicados = numeros.map(function(numero){
return numero * 4
});

console.log("numeros multiplicados:", numerosMultiplicados);// numeros multiplicados: 4,  8, 12, 16,20, 24, 28, 32


//variable local y global

let mensajeGlobal = "este es una varaible global";


function pruebaVariable(){
    //variable local
    let mensajeLocal = "esta es una variable local";


    console.log(mensajeGlobal);
    console.log(mensajeLocal);

    //se puede modificar la variable global desde la funcion
    mensajeGlobal = "soy la variable global modificada desde la funcion"
};

pruebaVariable();
console.log(mensajeGlobal);


/* DIFICULTAD EXTRA (opcional):
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


const string1 = "soy la cadena 1 ,";
const string2 = " soy la cadena 2";

function pasarDeTextoANumero (string1,string2){

    const resultado = string1 + string2;
    const numbers   = [];

    for(let i = 0; i <= 100; i++ ){
        if(i % 3 === 0 && i % 5 === 0){
            console.log(`multiplo de 3 y  5: ${resultado}`,);
        }else if (i % 3 === 0){
            console.log(`multiplo de 5: ${string2}`,);
            
        }else if (i % 5 === 0){
            console.log(`multiplo de 3 : ${string1}`, );
        }else{
            numbers.push(i);
        }
    };
    
    return numbers;

};

console.log(pasarDeTextoANumero(string1,string2));