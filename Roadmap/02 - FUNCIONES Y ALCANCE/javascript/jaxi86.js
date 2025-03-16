// funciones basicas

function recuperar(){
    console.log('recuperando...');
};
recuperar();

function multiplicacion(a, b){
    return a * b;
};
console.log(multiplicacion(2, 4));

function numero(numero) {
    console.log("cien" + " "  + numero + "!!" );
}

numero(100);
 
//Comprueba si puedes crear funciones dentro de funciones.

function funcion(){
    return function(){
        console.log('Hola mundo');
    }
}

let saludar = funcion();
saludar()

//Utiliza algún ejemplo de funciones ya creadas en el lenguaje.

function obtenerLongitud(palabra) {
    return palabra.length;
}
console.log( obtenerLongitud('jaxi'));


let cadenaNumero = "588";
let numero1 = parseInt(cadenaNumero);//Esta linea convierte la cadena "123" a un numero(integer) entero utilizando parseInt.

console.log(numero1);

//Pon a prueba el concepto de variable LOCAL y GLOBAL.

let var_glob = 'esta es una variable global';
function pruebasVariables(){
    let var_loc ='esta es una variable local';
    console.log(var_loc);
    console.log(var_glob);
}
pruebasVariables();

// console.log(1,var_loc);// esta la tuve que comentar porque me saltaba error porque esta variable solo existe dentro de la funcion
console.log(2,var_glob);

// DIFICULTAD EXTRA (opcional):
//  * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
//  * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
//  *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
//  *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
//  *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
//  *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.

function para( pala1, pala2 ){
    let numeros = 0;
    for (let i = 1; i <= 100; i++){
        if (i % 3 == 0){
            console.log (pala1);
        }
        if (i % 5 == 0){
            console.log (pala2);
        }
        if (i % 3 == 0 && i % 5 ==0){
            console.log(pala1 + pala2);
        }if (i % 3 != 0 && i % 5 !=0){
            numeros++;
            console.log(i)
        }
    }
    return numeros;
}

let resultado = para("multiplo3", "multiplo5");
console.log(resultado);
