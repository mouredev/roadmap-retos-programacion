fn main() {
    // Crea ejemplos de funciones básicas que representen las diferentes
    // posibilidades del lenguaje:
    // Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
    fn no_return() {
        println!("Esto es una funcion sin parametros y sin retorno");
    }
    no_return();

    fn return_i32() -> i32 {
        10
    }
    let number = return_i32() + 5;
    println!("La funcion devuelve un numero y le sumamos 5, resultado = {number}");

    fn with_one_parameter(num: i32) -> i32 {
        num + 10
    }
    println!("{}", with_one_parameter(7));

    fn with_two_parameter(num: i32, text: &str) -> String {
        format!(
            "El numero introducido es {} y el texto introducido es {}",
            num, text
        )
    }
    let return_function = with_two_parameter(45, "Viva er Betis");
    println!("{return_function}");

    //- Comprueba si puedes crear funciones dentro de funciones.

    fn functions_into_functions() -> i32 {
        fn sum(a: i32, b: i32) -> i32 {
            a + b
        }
        sum(4, 5)
    }
    let result = functions_into_functions();
    println!("El resultado es {result}");

    // Otra forma con closures (funciones anonimas)
    fn funtions_into_closures() -> i32 {
        let sum = |a, b| a + b;
        sum(7, 3)
    }
    println!("El resultado es {}", funtions_into_closures());

    //* - Pon a prueba el concepto de variable LOCAL y GLOBAL.
    let var_global = 9;
    fn var_local() -> i32 {
        let num1 = 3;
        let num2 = 8;
        let var_global = num1 + num2;
        var_global
    }

    println!("El valor de la variable global {var_global}");
    println!("El resultado de la variable local {}", var_local());

    // Concepto de ownership cuando se pasa la variable a una
    // funcion está tiene ahora la propiedad de la variable
    let global = String::from("hola que tal");

    fn propietary_global(global: String) -> String {
        global
    }
    println!(
        "El valor de la variable al pasar por la funcion {}",
        propietary_global(global)
    );
    // Lo siguiente da error por que ahora la funcion propietary_global es
    // el propietario de la variable global habria que pasarla como referencia
    //println!("El valor de la variable global = {}", global);

    // * DIFICULTAD EXTRA (opcional):
    // * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
    // * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
    // *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
    // *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
    // *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
    // *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.

    fn extra(first: &str, second: &str) -> i8 {
        let mut count: i8 = 0;
        for num in 1..=100 {
            if num % 3 == 0 {
                println!("{first}");
            } else if num % 5 == 0 {
                println!("{second}");
            } else if num % 3 == 0 && num % 5 == 0 {
                println!("{first} y {second}");
            } else {
                println!("{num}");
                count += 1;
            }
        }
        count
    }
    let count_num = extra("Es multiplo de 3", "Es multiplo de 5");
    println!("El número de veces que se ha imprimido el número es: {count_num}");
}
