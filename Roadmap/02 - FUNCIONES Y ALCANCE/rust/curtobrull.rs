// Crear funciones con o sin parámetros, con o sin retorno, etc...

fn saludar() {
    println!("Hola, mundo!");
}

fn despedir_nombre(nombre: &str) {
    println!("Adiós, {}!", nombre);
}

fn multiples_parametros(nombre: &str, apellidos: &str) {
    println!("Hola, {} {}!", nombre, apellidos);
}

fn con_retorno() -> i32 {
    44
}

fn con_retorno_multiple() -> (i32, i32) {
    (44, 10)
}

fn con_retorno_y_parametros(parametro: i32) -> i32 {
    parametro
}

fn funcion_con_funcion() {
    fn funcion_anidada() {
        println!("Función anidada");
    }
    funcion_anidada();
}

fn suma_fn_recursiva(num: u32) -> u32 {
    if num == 0 {
        println!("Iteración {}, Suma parcial = {}", num, 0);
        0
    } else {
        let suma_parcial = num + suma_fn_recursiva(num - 1);
        println!("Iteración {}, Suma parcial = {}", num, suma_parcial);
        suma_parcial
    }
}

const VARIABLE_GLOBAL: u32 = 10;

fn variable_local() {
    let variable_local: u32 = 111;
    println!("La variable local es: {} y la global es: {}", variable_local, VARIABLE_GLOBAL);
}

fn ejercicio_extra(texto: &str, texto_2: &str) -> i32 {

    let mut count: i32 = 0;

    for i in 0..101 {
        if i % 3 == 0 && i % 5 == 0 {
            println!("{} {}", texto, texto_2);
        } else if i % 3 == 0 {
            println!("{}", texto);
        } else if i % 5 == 0 {
            println!("{}", texto_2);
        } else {
            println!("{}", i);
            count += 1;
        }
    }

    count
}

fn main() {
    println!("Función sin parámetros");
    saludar();
    println!("Función con parámetros");
    despedir_nombre("Javier");
    println!("Función con múltiples parámetros");
    multiples_parametros("Javier", "Curto");
    println!("Función con retorno");
    println!("Tengo {} años.", con_retorno());
    println!("Función con retorno multiple");
    println!("Tengo {} y {} meses.", con_retorno_multiple().0, con_retorno_multiple().1);
    println!("Función con retorno y parámetro");
    println!("Sigo teniendo {} años.", con_retorno_y_parametros(44));
    println!("-----------------------");
    println!("Función con funciones");
    funcion_con_funcion();
    println!("-----------------------");
    println!("Función recursiva, suma de la iteración acumulada");
    let num: u32 = 10;
    println!("La suma de {} iteraciones es: {}", num, suma_fn_recursiva(num));
    println!("-----------------------");
    variable_local();
    println!("Podemos acceder a la variable global: {} desde cualquier lugar pero \
    la variable local solo es accesible desde la función variable_local()", VARIABLE_GLOBAL);
    println!("-----------------------");
    println!("Ejercicio extra");
    let texto = "Boom";
    let texto_2 = "Zapp";
    println!("Cantidad de veces que han salido números: {}", ejercicio_extra(texto, texto_2));
}
