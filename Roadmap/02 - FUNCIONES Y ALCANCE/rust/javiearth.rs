//=========================
// 02 - FUNCIONES Y ALCANCE
//=========================
use rand::Rng; // A partir de ahora mejor usar el gestor de paquetes cargo ;)

// Crea funciones basicas que que representen las diferentes posibilidades del lenguaje

fn main(){

sin_param();

println!("La siguiente es una funcion a la que se le da un radio como paramentro:");

con_param(5.0);

println!("La siguiente expresion llama a una funcion que retorna un valor");

let suma: u32 = con_return();

println!("La suma de todos los pares en los primeros cien numeros naturales es {}", suma);


// Comprueba si puedes crear una funcion dentro de otra funcion:

funciones_anidadas();

// Utiliza algunejemplo de funciones ya creadas en el lenguaje
// Voy a utilizar una funcion para generar un numero aleatorio (para eso se importa la libreria rand al principio del archivo

let num = rand::thread_rng().gen_range(1..=100);
println!("Numero aleatorio usando una funcion ya creada en Rust: {}", num);

// DIFICULTAD EXTRA

// Funcion que recibe dos strings y devuelve un numero

let mi_num = cadena_numero ("primero", "segundo");

println!("Dos strings a un numero: {}", mi_num);


}
// FIN DE FUNCION MAIN

// FUNCION SIN PARAMETROS
fn sin_param(){
    println!("Esta es una funcion sin parametros ni retorno");
}

//FUNCION CON PARAMETROS
fn con_param(radio: f32){
    let area = 3.1415926 * radio * radio;
    println!("El area del circulo es {}", area);
}

//FUNCION CON RETURN
fn con_return() -> u32 {
    //let la_guia: u8 = 42; ESTO SERIA UNA VARIABLE LOCAL QUE NO PUEDO LLAMAR DESDE LA FUNCION MAIN
    let mut suma: u32 = 0;
    let mut counter: u32 = 1;
    while counter <= 100 {
        if counter % 2 == 0 {
            suma = suma + counter;
        }
        counter += 1;
    }
    return suma;
}

//FUNCION DENTRO DE UNA FUNCION
fn funciones_anidadas(){
    println!("Esta es la funcion de primer nivel");
    funcion_interna();
    fn funcion_interna(){
         println!("Y esta es una funcion dentro de una funcion");
    }
}

//DIFICULTAD EXTRA
fn cadena_numero(uno: &str, dos: &str) -> i32 {
/*    let longitud: usize = uno.len() + dos.len();
    longitud
*/
    let mut num_count: i32 = 0;
    for mi_numero in 1..100 {
        if mi_numero %3 == 0 && mi_numero %5 == 0 { println!("{}{}", uno, dos);
        } else if mi_numero %3 == 0 {println!("{}", uno);
        } else if mi_numero %5 == 0 {println!("{}", dos);
        } else {
            println!("{}", mi_numero);
            num_count +=1;
        }
    }
    num_count
}