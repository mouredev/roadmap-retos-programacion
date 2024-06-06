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

 // Función sin parámetros ni retorno
fn funcion_simple() {
    println!("¡Hola desde la función simple!");
}

// Con retorno y sin parametros
fn funcion_con_retorno_y_sin_parametros() -> i32 {
    // Realiza alguna operación
    let resultado = 42;

    // Retorna un valor
    resultado
}

// Función con un parámetro y retorno
fn cuadrado(numero: i32) -> i32 {
    numero * numero
}

// Función con varios parámetros y retorno
fn suma_y_producto(a: i32, b: i32) -> (i32, i32) {
    (a + b, a * b)
}


// Función que retorna múltiples valores usando una tupla
fn funcion_con_retorno_multiple(input: i32) -> (i32, i32, i32) {
    let cuadrado = input * input;
    let cubo = input * input * input;
    let cuadruple = input * 4;

    // Retorna una tupla con los valores calculados
    (cuadrado, cubo, cuadruple)
}

// Función con un número variable de argumentos usando slices
fn funcion_con_varios_argumentos(args: &[i32]) -> i32 {
    let mut suma = 0;

    for &numero in args {
        suma += numero;
    }

    suma
}

fn funcion_exterior() {
    println!("Comienzo de la función exterior.");

    // Definición de una función interna
    fn funcion_interior() {
        println!("¡Hola desde la función interior!");
    }

    // Llamada a la función interna
    funcion_interior();

    println!("Fin de la función exterior.");
}


// Función que imprime todos los números del 1 al 100 con condiciones especiales
fn procesar_numeros(texto1: &str, texto2: &str) -> u32 {
    let mut contador = 0;

    for num in 1..=100 {
        if num % 3 == 0 && num % 5 == 0 {
            println!("{}{}", texto1, texto2);
        } else if num % 3 == 0 {
            println!("{}", texto1);
        } else if num % 5 == 0 {
            println!("{}", texto2);
        } else {
            println!("{}", num);
            contador += 1;
        }

        
    }

    contador
}

const CONSTANTE_GLOBAL: i32 = 100;

// Función principal
fn main() {
    // Uso de funciones simples
    funcion_simple();

    // Uso de función con un parámetro y retorno
    let resultado_cuadrado = cuadrado(5);
    println!("Cuadrado: {}", resultado_cuadrado);

     // Llama a la función y almacena el resultado
     let resultado_funcion = funcion_con_retorno_y_sin_parametros();
     println!("Resultado de la función: {}", resultado_funcion);

    // Uso de función con varios parámetros y retorno
    let (suma, producto) = suma_y_producto(3, 4);
    println!("Suma: {}, Producto: {}", suma, producto);

    // Llama a la función y almacena los resultados en una tupla
    let (resultado_cuadrado, resultado_cubo, resultado_cuadruple) = funcion_con_retorno_multiple(3);

    // Imprime los resultados
    println!("Cuadrado: {}", resultado_cuadrado);
    println!("Cubo: {}", resultado_cubo);
    println!("Cuádruple: {}", resultado_cuadruple);

    // Llama a la función con diferentes números de argumentos
    let resultado1 = funcion_con_varios_argumentos(&[1, 2, 3]);
    let resultado2 = funcion_con_varios_argumentos(&[10, 20, 30, 40]);

    // Imprime los resultados
    println!("Resultado 1: {}", resultado1);
    println!("Resultado 2: {}", resultado2);

    // Llamada a la función exterior
    funcion_exterior();

    // Funciones estándar
    // print! y println!
    print!("Hola, ");
    println!("Mundo!");
    // format!:
    let mensaje = format!("{} {}", "Hola", "Mundo");
    println!("{}", mensaje);

    // Variable local en la función main
    let variable_local = 42;
    println!("Variable local en main: {}", variable_local);

    // Constante global
    println!("Constante global: {}", CONSTANTE_GLOBAL);

    // Uso de función que imprime números con condiciones especiales
    let veces_impreso = procesar_numeros("Fizz", "Buzz");
    println!("Número de veces impreso: {}", veces_impreso);
}
