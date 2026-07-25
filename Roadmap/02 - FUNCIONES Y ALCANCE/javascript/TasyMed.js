// ----- 1. Crear funciones básicas -----

// - 1 
function EstoEsUnaFuncion(){

}
// - 2
const Numero = 10
function FucionConParametros(Numero) {
    if (Numero === 10) {
        console.log("Uso del parametro")
    }
}
// - 3
// Declaracion de una fuacion con sus parametros
function FucionVariosParameros(a, b) {
    return a + b
}
// Uso y declaracion
let resultado = FucionVariosParameros(10, 5)
console.log(resultado) //15


// ----- 2. Verificar si puedes hacer funciones dentro de funciones -----

function Prueba(texto){
    function interno(texto){
        console.log(texto)
    }
    interno(texto)
}
Prueba("Funciona")

// Si puedes

// ----- 3. Usar alguna función ya existente en el lenguaje (Ejemplo: Math.max()) -----

let usarFuncionIntegrada = Math.random() //Genera un numeros alatorios
console.log(usarFuncionIntegrada)


// ----- 4. Probar el concepto de variable local y global -----

function Globalsuma(a, b) {
    return a + b
}

function Entorno() {
    // Funcion local
    function Localresta(a, b) {
        return a - b
    }

    let suma = Globalsuma(2,2)
    console.log(suma) // Impreme 4

    let resta = Localresta(2,2) 
    console.log(resta) // Impreme 0
}

// Inicar el Entorno
Entorno()

// Uso de las variables en uso global
let  sumaGlobal = Globalsuma(3,3)
console.log(sumaGlobal) // Impreme 6

let usarRestaLocal = Localresta(3,2)
console.log(usarRestaLocal) // Null


// ----- Dificultad extra -----

/*
* DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
*/

function RETO(letra1, letra2) {
    let cantidad = 0;
    
    for (let i = 1; i <= 100; i++) {
        if (i % 3 === 0 && i % 5 === 0) {
            console.log(letra1 + " " + letra2);
        } else if (i % 3 === 0) {
            console.log(letra1);
        } else if (i % 5 === 0) {
            console.log(letra2);
        } else {
            console.log(i);
            cantidad++;
        }
    }

    console.log("Numbers printed: " + cantidad);
    return cantidad;
}

RETO("Alan", "Andres");