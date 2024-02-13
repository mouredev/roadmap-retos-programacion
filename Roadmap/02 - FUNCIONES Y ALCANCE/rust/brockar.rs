const HORA_DE_LOS_DIRECTOS: u8 = 16;
fn main() {
    funcion_basica();

    funcion_con_parametros(1, 2);

    println!("Retorno: {}", funcion_con_retorno());

    println!("Retorno: {}", funcion_con_parametros_y_retorno(1, 2));

    funcion_con_parametros_y_varios_retornos(2, 4);

    let (suma, resta) = funcion_con_parametros_y_varios_retornos_con_nombres(2, 4);
    println!("Esta es la suma retornada: {}", suma);
    println!("Esta es la resta retornada: {}", resta);

    // Funcion dentro de otra
    let x: u8 = 5;
    let lamda_incrementar = |y: u8| y + 1;
    println!(
        "\nRetorno de funcion lamda(dentro de otra): {}",
        lamda_incrementar(x)
    );

    // Uso de constantes
    println!("\nEsta es una constante: {}", HORA_DE_LOS_DIRECTOS);

    // Scope de las variables definidas en una función solo podrán ser utilizadas dentro de esta,
    // excepto que se pase por parámetro a otra función.

    // función ya creada por el lenguaje
    let mut s = String::from("Hola");
    s.push_str(", moure!");

    println!("\nResultado de la función creada por el lenguaje: \n{}", s);

    // EXTRA EXTRA
    println!("\n\n EXTRA EXTRA\n\n");
    let result = extra("Hola", " Mundo!");
    println!(
        "\nLa cantidad de veces que se ha impreso el numero es: {}",
        result
    );
}

fn funcion_basica() {
    let x: u8 = 5;
    println!("Esto es una función básica: {}", x);
}

fn funcion_con_parametros(x: u8, y: u8) {
    println!("Esto es una función con parámetros: {} y {}", x, y);
}

fn funcion_con_retorno() -> u8 {
    let x: u8 = 5;
    println!("Esto es una función con retorno: {}", x);
    x
}

fn funcion_con_parametros_y_retorno(x: u8, y: u8) -> u8 {
    let z = x + y;
    println!(
        "Esto es una función con parámetros y retorno: {} + {} = {}",
        x, y, z
    );
    z
}

fn funcion_con_parametros_y_varios_retornos(x: i8, y: i8) -> (i8, i8) {
    let z = x + y;
    let w = x - y;
    println!(
        "Esto es una función con parámetros y varios retornos: {} + {} = {} y {} - {} = {}",
        x, y, z, x, y, w
    );
    (z, w)
}

fn funcion_con_parametros_y_varios_retornos_con_nombres(x: i8, y: i8) -> (i8, i8) {
    let suma = x + y;
    let resta = x - y;
    println!("Esto es una función con parámetros y varios retornos con nombres: {} + {} = {} y {} - {} = {}", x, y, suma, x, y, resta);
    (suma, resta)
}

fn extra(a: &str, b: &str) -> i32 {
    let mut r = 0;
    for num in 1..=100 {
        if (num % 3) == 0 && (num % 5) == 0 {
            println!("{} {}", a, b);
        } else if (num % 3) == 0 {
            println!("{}", a);
        } else if (num % 5) == 0 {
            println!("{}", b);
        } else {
            println!("{}", num);
            r += 1;
        }
    }

    r
}
