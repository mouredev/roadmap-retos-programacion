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


function saludar(): void {
    console.log("Hola mundo");
}


function sumar(valor1:number, valor2:number): number {
    return valor1+valor2;
  }
  
  console.log(sumar(10, 5));

  // Función dentro de otra función
function operacionesMatematicas(): void {
    const restar = (x: number, y: number): number => {
        return x - y;
    }

    console.log("Suma: ", sumar(5, 3));
}

// Uso de una función incorporada: Math.max()
function maximoDeDosNumeros(a: number, b: number): number {
    return Math.max(a, b);
}


// Demostración de variable LOCAL y GLOBAL
let variableGlobal = "Soy global";

function probarScope(): void {
    let variableLocal = "Soy local";
    console.log(variableGlobal); // Accede a la variable global
    console.log(variableLocal);  // Accede a la variable local
}

// Función con dificultad extra
function extra(texto1: string, texto2: string): number {
    let contadorNumeros :number=0

    for (let index = 0; index < 100; index++) {
        if(index%3===0) {
            console.log(texto1)
        }
       else if(index%5===0) {
            console.log(texto2)
        }
        else if(index%5===0 && index%3===0 ) {
            console.log(texto1+texto2)
        }   
        else{
            console.log(index)
            contadorNumeros++
        } 
    }
    return contadorNumeros
}
console.log("Número de veces que se imprimió un número:", extra("Fizz", "Buzz"));
