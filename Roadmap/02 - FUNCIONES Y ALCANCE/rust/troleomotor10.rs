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

// Main function
fn main(){
    hello_world();

    let resultado: i32 = suma(10, 5);
    println!("{resultado}");

    let (string1, string2) = multiple_return();
    println!("{} {}", string1, string2);

    let names: [&str; 3] = ["Juan", "Manolo", "Luis"];
    more_than_1_parameter(&names);

    function_out();

    builtin_functions();
    
    hello_rust1();

    exercice_extra("Zipi", "Zape");
}

/*
    FUNCIONES BÁSICAS DEL LENGUAJE
*/

// Function without return and parameters
fn hello_world() {
    println!("Hello World!")
}

//  Function with parameters and return
fn suma(a: i32, b: i32) -> i32{
    a + b
}

// Function with parameters and return of many values
fn multiple_return() -> (&'static str, &'static str){
    ("Hola", "Troleomotor10")
}


// Function with more than 1 parameter
fn more_than_1_parameter(names: &[&str]) {
    for name in names {
        println!("{name}");
    }
}

/*
    FUNCIONES DENTRO DE FUNCIONES
*/

fn function_out() {
    fn function_in_function(){
        println!("Hello, Rust 2!")
    }
    function_in_function();
}

/*
    FUNCIONES DEL LENGUAJE (built-in)
*/

fn builtin_functions(){
    let variable: &str = "github";
    println!("{}", variable.len());
    
}

/*
    VARIABLES LOCALES Y GLOBALES
*/

fn hello_rust1() {
    let global_var: i32 = 33;
    fn hello_rust2(){
        let local_var: i32 = 55;
        //println!("{}", global_var); -> No va a funcionar
        println!("{}", local_var);
    }
    hello_rust2();
    println!("{}",  global_var);
    //println!("{}", local_var); -> No va a funcionar
}

/*
    EJERCICIO EXTRA
*/

fn exercice_extra(text1: &str, text2: &str) {
    let mut contador: i32 = 0;
    for x in 1..101 {
        if x % 3 == 0 && x % 5 == 0{
            println!("{} {}", text1, text2);
        } else if x % 3 == 0 {
            println!("{text1}");
        } else if x % 5 == 0 {
            println!("{text2}");
        } else {
            println!("{x}");
            contador += 1;
        }
    }
    println!("Los numeros en lugar de los textos han salido: {contador} veces");
}