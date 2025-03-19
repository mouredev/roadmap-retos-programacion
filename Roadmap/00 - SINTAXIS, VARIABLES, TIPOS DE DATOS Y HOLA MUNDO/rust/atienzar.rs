/*
 * ¿Preparad@ para aprender o repasar el lenguaje de programación que tú quieras?
 * - Recuerda que todas las instrucciones de participación están en el
 *   repositorio de GitHub.
 *
 * Lo primero... ¿Ya has elegido un lenguaje?
 * - No todos son iguales, pero sus fundamentos suelen ser comunes.
 * - Este primer reto te servirá para familiarizarte con la forma de participar
 *   enviando tus propias soluciones.
 *
 * EJERCICIO:
 * - Crea un comentario en el código y coloca la URL del sitio web oficial del
 *   lenguaje de programación que has seleccionado.
 * - Representa las diferentes sintaxis que existen de crear comentarios
 *   en el lenguaje (en una línea, varias...).
 * - Crea una variable (y una constante si el lenguaje lo soporta).
 * - Crea variables representando todos los tipos de datos primitivos
 *   del lenguaje (cadenas de texto, enteros, booleanos...).
 * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
 *
 * ¿Fácil? No te preocupes, recuerda que esta es una ruta de estudio y
 * debemos comenzar por el principio.
 */

 // Comentario de 1 línea => https://www.rust-lang.org/es

 /*
 *  Comentario en bloque
 *  
 */
use std::{vec, collections::HashSet, collections::HashMap};


fn main(){

    // 1 cte y vble
    let mut mivar = 8;
    let miconst = 10;
    println!("{mivar}  {miconst}");

    let mibool:bool = false;
    let miint:i32 = 4;
    let mut micad: &str = "Mi primera cadena";

    // print 
    println!("Hola Rust!");
    println!("{mibool}  {miint} {micad}");



    //Lista 

    let mut my_list = vec!("atienzar", "pedro", "juan", "52", "atienzar");
    my_list.push("atienzar");
    println!("{:?}", my_list);
    println!("{}", my_list[2]);


    // Sets
    // es como el vector pero SIN duplicados y desordenado
    let mut my_set: HashSet<&str> = vec!("atienzar", "pedro", "juan", "52", "atienzar").into_iter().collect();
    println!("{:?}", my_set);
    my_set.insert("Pedro");
    println!("{:?}", my_set);


    //Mapa KEY: VALUE
    let mut my_map: HashMap<&str,i32> = vec![("atienzar",52),("pedro",42),("pedrop",15)].into_iter().collect();
    println!("{:?}", my_set);
    my_map.insert("atienzaj", 26);
    println!("{:?}", my_map);
    
    

}


