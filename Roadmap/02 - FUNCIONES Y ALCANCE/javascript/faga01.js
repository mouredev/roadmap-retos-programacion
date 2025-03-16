/* Funciones. Una función es un bloque de código diseñado para realizar una tarea en particular.
 Una función de javascript se ejecuta cuando algo la invoca o la llama.
 con funciones puedes reutilizar código, puedo utilizar el mismo código con diferentes argumentos para diferentes resultados. */

// Función sin parametros ni retorno


function myFunction1(){
    let rta1 = 5 + 8;
}

// Función con parametros

function myFunction2(a, b){
    let rta2 = a - b;
}

var i = 35;
var j = 10;

function myFunction2a(i, j){
    let rta2a = i - j;
    return rta2a;
}

function myfunction3(item1, item2) {
    return item1*item2;
}

let x = myFunction4(5, 8, 2);

function myFunction4(par1, par2, par3) {
    return (par1 * par2) / par3;
}

function myFunction5(c, d) {
    return c * d;
}

function myFunction6 (s, t) {
    return myFunction5(s, t);
}

function myFunction7() {
    return function myFunction8 () {
        return 40 + 30;
    }
}


/* console.log(myFunction1);
console.log(myFunction2);
console.log(myfunction3(2,5));
console.log(x); 
console.log(myFunction6(5,8)); 
console.log(myFunction7()());
console.log(myFunction2a(i,j));
console.log(rta2);*/


/* Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda. */


/*
function miPruebaExtra(parametroA, parametroB) {
        let contadorVeces = 0;

    for (let i=1; i <= 100; i++) {
        
        if (parametroA % 3 == 0 && parametroB % 5 == 0) {
            contadorVeces++
            console.log(parametroA + " " + parametroB);
        } else if ( parametroA % 3 == 0) {
            
            console.log(parametroA);
            contadorVeces++
        } else if ( parametroB % 5 == 0) {
            contadorVeces++
            console.log(parametroB);
        } else {
            console.log(i);
        }

} 
    return contadorVeces;

}
*/



function miPruebaExtra2 (parametroC, parametroD) {
    
    let contadorTexto = 0

    if (parametroC % 3 == 0 && parametroD % 5 == 0) {
        console.log(parametroC + " " + parametroD);
        for (let index = 1; index <= 100; index++) {
                
            if(index % 3 == 0 || index % 5 == 0) {
                contadorTexto++
            }
        }
    } else if (parametroC % 3 == 0){
        console.log(parametroC);
        for (let index = 1; index <= 100; index++) {
            if(index % 3 == 0) {
                contadorTexto++
            }
        }
    } else if (parametroD % 5 == 0){
        console.log(parametroD);
        for (let index = 1; index <= 100; index++) {
            if(index % 5 == 0) {
                contadorTexto++
            }
        }
    } else {
        for(let index = 1; index <= 100; index++)
        console.log(index);
    }

    return "numero de veces que se imprime el número" + ": " + contadorTexto;

}

//console.log(miPruebaExtra("21", "30"));

console.log(miPruebaExtra2("9", "25"));




