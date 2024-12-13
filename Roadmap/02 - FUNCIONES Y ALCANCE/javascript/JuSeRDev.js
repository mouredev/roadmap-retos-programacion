
//  * - Crea ejemplos de funciones básicas que representen las diferentes posibilidades del lenguaje: Sin parámetros ni retorno, con uno o varios parámetros, con retorno... 



//funcion sin retorno y sin parametros

function saludar() {
    let saludo = "hola"
}

console.log(saludar());


// Funcion con 2 parametros y retorno
function suma(a, b) {
    let resultado = a + b
    return resultado
}

console.log(suma(1, 2));

//  * - Comprueba si puedes crear funciones dentro de funciones.

function multiplicar(resultado) {
    function num1(a,b) {
        let resultado = a + b
        return resultado
    }
    num1(12,10)
    function num2(a,b) {
        let resultado = a-b
        return resultado
    }
    num2(10,5)
    let resultado1 = num1(10,15)
    let resultado2 = num2(10,5)
    resultado = resultado1 * resultado2
    return resultado
}

console.log(multiplicar());


//  * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.

let fechaActual = new Date()
console.log("la fecha de hoy es: ", fechaActual);

let numeromayor = Math.max(3, 5, 10, 12)
console.log(numeromayor);


//  * - Pon a prueba el concepto de variable LOCAL y GLOBAL.

let global = "soy una variable global"

let myFunc = ()=>{
    let local = "Soy una valriable local"
    let global = "soy una varia local definida dentro de una funcion con el nombre de una variable global"
    return `la variable "local": ${local} y la variable "global" dentro de una fucnion: ${global}`
}

//  * - Debes hacer print por consola del resultado de todos los ejemplos. (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)

console.log(global);
console.log(myFunc());

//  * DIFICULTAD EXTRA (opcional):
//  * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
//  * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
//  *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
//  *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
//  *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
//  *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.

let extra = (string1, string2) => {
    let contador = 0;
    for (let i = 1; i <= 100; i++) {
        switch (true) {
            case i % 3 === 0 && i % 5 === 0:
                console.log(string1 + string2)
                break;
            case i % 3 === 0:
                console.log(string1);
                break;
            case i % 5 === 0:
                console.log(string2);
                break;
            default:
                console.log(i);
                contador++;
                break;
            }
        }
    return contador
}


console.log(extra("cadena(1)", "cadena(2)"));


let extra2 = (texto1, texto2)=>{
    let contador = 0
    for (let i = 1; i <= 100; i++) {
        const numero = i;
        if (numero % 3 === 0 && numero % 5 === 0) {
            let string3= texto1 + texto2
            console.log(string3);
        }else if(numero % 3 === 0){
            let string1 = texto1
            console.log(string1);
        } else if(numero % 5 === 0){
            let string2 = texto2
            console.log(string2);
        }else{
            console.log(i)
            contador++
        }
    }
    return contador
}
console.log(extra2("multiplo de 3","multiplo de 5"));



//  * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
//  * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.