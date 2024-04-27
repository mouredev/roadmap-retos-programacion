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

static _GLOBAL: i32 = 1;
fn main() {
    print!("\n No parameters no return \n");
    do_it_simple();

    print!("\n Recursive and not value \n");
    let mut i = 1;

    recursive(&mut i);

    print!("\n Return and method \n");
    let value = dramatize("Hello, String");
    print!("{}\n", value);

    print!("\n 2 Params + return \n");

    let result = sum(3, 5);
    print!("{}\n", result);

    print!("\n Create function here \n");

    fn call_me_here() -> String {
        return "I'm here, yes".to_owned();
    }
    print!("{}", call_me_here());

    print!("\n Local, Global variable \n");

    fn _local_fn() {
        let _local = 1;
    }
    // print!("{}", _local) // Cannot find _local in this scope
    print!("Can be logged: {} ", _GLOBAL);

    print!("\n Challenge \n");
    let num = fizz_what("fizz", "buzz");
    print!("Solution: {}\n", num)
}

fn do_it_simple() {
    return;
}

fn recursive(i: &mut i32) {
    print!("{},", i);
    *i += 1;
    if *i < 4 {
        recursive(i)
    }
}

fn dramatize(a: &str) -> String {
    // I need to convert ir in a owned string
    return a.to_uppercase() + "!";
}

fn sum(first: i32, second: i32) -> i32 {
    // Instead of return I just can put the value here without semicolon.
    first + second
}

fn fizz_what(str1: &str, str2: &str) -> i32 {
    let mut number_of_numnbers_printed = 0;

    for n in 0..=100 {
        if n % 3 == 0 && n % 5 == 0 {
            print!("{}{},", str1, str2);
        } else if n % 5 == 0 {
            print!("{},", str2);
        } else if n % 3 == 0 {
            print!("{},", str1);
        } else {
            print!("{},", n);
            number_of_numnbers_printed += 1;
        }
    }
    return number_of_numnbers_printed;
}
