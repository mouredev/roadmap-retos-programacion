// Funciones 
/*Las funciones son uno de los bloques de construcción fundamentales en JavaScript.
Una función en JavaScript es similar a un procedimiento — un conjunto de instrucciones que realiza 
una tarea o calcula un valor, pero para que un procedimiento 
califique como función, debe tomar alguna entrada y devolver una salida donde hay
alguna relación obvia entre la entrada y la salida */

// Declaracion de una Funcion
/*
Se Define con la palabra reservada function mas el nombre, recibe una lista de parametros entre parentesis.
Dentro de corchetes se escribe el codigo a ejecutar
 */

function name(nombre){
    return nombre;
}

console.log('\n--Definición de una función--');
console.log(name("ricardo"));

//funciones anonimas

const miNombre = function(){
    return  "Mi nombre es Ricardo";
}
console.log(miNombre());

//funciones flechas 
const decirNombre = () =>{
    console.log("Mi nombre es Ricardo Oyola")
}


//funciones autoejecutables
(function() {
    // Código que se ejecutará automáticamente
    console.log("Esta función se ejecuta automáticamente.");
})();

//Funciones Flecha autoejecutables
(() => {
    // Código que se ejecutará automáticamente
    console.log("Esta función de flecha se ejecuta automáticamente.");
})();

//Funciones Anidadas
console.log('\n--Funciones Anidadas--');
function masRaizCuadrada(a, b){
    function raizCuadrada (c){
        return c * c;
    }

    console.log(raizCuadrada(a) + raizCuadrada(b));
}

masRaizCuadrada(2, 5);

//Ámbito de function

/*No se puede acceder a las variables definidas dentro de una función desde cualquier 
lugar fuera de la función, porque la variable se define solo en el ámbito de la función. 
Sin embargo, una función puede acceder a todas las variables y funciones definidas dentro del 
ámbito en el que está definida. */

//Ámbito Global
console.log('\n--Funciones Ámbito Global--');
let numeroUno = 1;
let numeroDos = 2;

function suma(){
    return numeroUno + numeroDos;
}

console.log(suma())

//Ámbito Local
console.log('\n--Funciones Ámbito local--');

function imprimirNumero(elNumero){
    let numero = elNumero;

    if(numero > 2 ){
        for(i = numero; i < 10; i++){
            console.log(i);
        }
    }else {
        console.log("El numero debe ser positivo");
    }
}

imprimirNumero(4);

/*
* DIFICULTAD EXTRA (opcional):
* Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
* - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
*   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
*   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
*   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
*   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
*/

function imprimirResultados(a = "textoUno", b = "textoDos") {
    let control = 0;

    for (let i = 1; i <= 100; i++) {
        let multiploDeTres = i % 3 === 0;
        let multiploDeCinco = i % 5 === 0;

        if (multiploDeTres && multiploDeCinco) {
            console.log(a + b);
        } else if (multiploDeTres) {
            console.log(a);
        } else if (multiploDeCinco) {
            console.log(b);
        } else {
            console.log(i);
            control++;
        }
    }
    return control;
}

imprimirResultados();

