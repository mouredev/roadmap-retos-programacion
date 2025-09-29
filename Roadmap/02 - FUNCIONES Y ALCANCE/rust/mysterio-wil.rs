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

// --- Variable Global ---
// Modificar variables estáticas mutables es inseguro en Rust y requiere un bloque `unsafe`.
// La forma segura y recomendada de tener estado global mutable es usando primitivas de concurrencia como Mutex.
static mut GLOBAL_VAR: &str = "Soy una variable global";

fn main() {
    println!("===> Funciones básicas <===");

    // Sin parámetros ni retorno
    greet();

    // Con un parámetro (&str es un "string slice", la forma idiomática de pasar texto)
    greet_person("Wilmer");

    // Con varios parámetros
    add(5, 3);

    // Con retorno (el retorno sin `return` es implícito si no hay punto y coma)
    let result = multiply(5, 3);
    println!("El resultado de la multiplicación es {}", result);

    // Rust no soporta parámetros por defecto.
    println!("Rust no soporta parámetros por defecto.");

    // Para argumentos variables, la forma idiomática es usar slices (o macros para casos más complejos).
    println!("Argumentos variables (pasando un slice):");
    print_args(&[1, 2, 3, 4]);


    println!("\n===> Funciones dentro de funciones <===");
    outer_function();


    println!("\n===> Funciones de la Librería Estándar de Rust <===");
    let my_list = [1, 2, 3, 4, 5];
    println!("Usando el método .len() de un array/slice: El array tiene {} elementos.", my_list.len());
    // .iter().max() devuelve un Option, por eso usamos unwrap() para obtener el valor.
    println!("Usando .iter().max(): El valor máximo es {}.\n", my_list.iter().max().unwrap());


    println!("\n===> Variable LOCAL y GLOBAL <===");
    my_function_scope();

    // Modificar o leer una variable `static mut` es una operación `unsafe`.
    unsafe {
        println!("Antes de modificar: {}", GLOBAL_VAR);
        modify_global();
        println!("Después de modificar: {}", GLOBAL_VAR);
    }


    /*
     * DIFICULTAD EXTRA (opcional):
     */
    println!("\n====> DIFICULTAD EXTRA <====");
    let times_printed_number = fizz_buzz_extra("Fizz", "Buzz");
    println!("\nEl número se imprimió un total de {} veces.", times_printed_number);
}

// --- Definiciones de funciones ---

fn greet() {
    println!("Hola, Rust!");
}

fn greet_person(name: &str) {
    println!("Hola, {}!", name);
}

fn add(a: i32, b: i32) {
    println!("La suma de {} y {} es {}", a, b, a + b);
}

fn multiply(a: i32, b: i32) -> i32 {
    a * b // Retorno implícito
}

fn print_args(args: &[i32]) {
    for arg in args {
        println!("- {}", arg);
    }
}

fn outer_function() {
    println!("Esta es la función externa.");
    fn inner_function() {
        println!("Esta es la función interna.");
    }
    inner_function();
}

fn my_function_scope() {
    let local_var = "Soy una variable local";
    // Leer una `static mut` también es `unsafe`.
    unsafe {
        println!("{}", GLOBAL_VAR);
    }
    println!("{}", local_var);
}

unsafe fn modify_global() {
    GLOBAL_VAR = "He modificado la variable global";
}

fn fizz_buzz_extra(text1: &str, text2: &str) -> i32 {
    let mut count = 0;
    for i in 1..=100 { // El rango ..= es inclusivo
        let is_multiple_of_3 = i % 3 == 0;
        let is_multiple_of_5 = i % 5 == 0;

        if is_multiple_of_3 && is_multiple_of_5 {
            println!("{}{}", text1, text2);
        } else if is_multiple_of_3 {
            println!("{}", text1);
        } else if is_multiple_of_5 {
            println!("{}", text2);
        } else {
            println!("{}", i);
            count += 1;
        }
    }
    count
}
