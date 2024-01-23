/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
 */

use std::{vec, collections::HashSet, collections::HashMap};
use std::io::{stdin,stdout,Write};

fn cortar_numero(s :&String)->String{
    let mut end = 11
    s.chars().into_iter().take(6).for_each(|x| end += x.len_utf8());
    //println!("Numero  es {}",s[..end] );

    return s[..end].to_string();

}
fn get_respuesta()->String{

    let mut answer=String::new();
    let _=stdout().flush();

    stdin().read_line(&mut answer).expect("No has introducido un número correcto.");
    if let Some('\n')=answer.chars().next_back() {
        answer.pop();
    }
    if let Some('\r')=answer.chars().next_back() {
        answer.pop();
    }            
    return answer.to_lowercase();
}

fn agenda(){

    let mut agenda:Vec<(String,String)> =  Vec::new();
    let mut accion=String::new();
    let mut max_chars:usize = 11;

    println!("¡Bienvenido a tu agenda en Rust!");

    loop{
        print!("¿Que deseas hacer? (buscar / insertar / modificar / eliminar o salir): ");
        accion = get_respuesta();

        println!("Has escogido {}", accion);

        match accion.as_str() {
            "buscar" => {
                println!("¿Qué desea buscar? : ");
                let aguja = get_respuesta();

                let mut encontrado = false;
                let mut cont = 0;

                while !encontrado && cont < agenda.len(){
                    //println!("elemento: {:?} ", agenda[cont]);
                    if agenda[cont].0 == aguja || agenda[cont].1 == aguja{
                        println!("Está en la lista {:?}", agenda[cont]);
                        encontrado = true
                    }
                    cont = cont + 1
                }
                println!("Lo sentimos lo que busca no está en la agenda.");

            }
            "insertar" => {

                let mut name = String::new();
                let mut number = String::new();

                println!("Introduzca el nombre del contacto: ");
                name = get_respuesta();
                
                println!("Introduzca el número del contacto(max 11): ");
                number = get_respuesta();
                
                if number.len() >= max_chars {
                    println!("solo almacenaremos los primero 11 números.");
                    number = cortar_numero(&number);
                    println!("Numero ahora es {}", number);
                } 
                agenda.push((name, number));
                println!("Estado de la Agenda: {:?}", agenda);


                accion="".to_string();

            }
            "modificar" => {

                let mut name = String::new();
                let mut number = String::new();

                println!("Introduzca el nombre o el numero del contacto abuscar: ");
                let name_or_number = get_respuesta();
                let mut encontrado = false;
                let mut cont = 0;

                while !encontrado && cont < agenda.len(){
                    // println!("elemento: {:?} ", agenda[cont]);
                    if agenda[cont].0 == name_or_number || agenda[cont].1 == name_or_number{
                        println!("Contacto encontrado: {:?}",agenda[cont]);
                        println!("Introduzca el nuevo nombre (enter si no quiere cambios):  ");
                        name = get_respuesta();
                        if name.len() >= 1{
                            agenda[cont].0 = name;
                        }
                        println!("Introduzca el nuevo número (enter si no quiere cambios):  ");
                        number = get_respuesta();
                        if number.len() >= 1{
                            agenda[cont].1 = number;
                        }
                        encontrado = true;
                        println!("Agenda: {:?}", agenda);
                    }
                    cont = cont + 1;
                }
            }
            "eliminar" => {

                let mut name = String::new();

                println!("Introduzca el nombre a eliminar:");
                name = get_respuesta();
                println!("Vamos a eliminar {}", name);

                let mut encontrado = false;
                let mut cont = 0;

                while !encontrado && cont < agenda.len(){
                    println!("elemento: {:?} ", agenda[cont]);
                    if agenda[cont].0 == name{
                        println!("Lo hemos encontrado!! y lo eliminamos");
                        agenda.remove(cont);
                        encontrado = true;
                        println!("Agenda: {:?}", agenda);
                    
                    }
                    // let elemento:(<String>,<String>) = agenda[cont];
                    //println!("elemento: {:?} ", elemento);

                    cont = cont + 1;

                }
            } 
            "salir" => { return; }
            _ => println!("Opción inválida."),
        }
    }

}

fn main(){


    //Lista 
    let mut my_list = vec!("rosa", "pedro", "atienzar", "52", "juan");
    println!("Vec inicial: {:?}", my_list);

    my_list.push("atienzar");
    println!("Vec add 1 elemento: {:?}", my_list);
    
    //imprimimos 1 elemento
    println!("Vec elemento 3: {}", my_list[2]);

    //ordenamos la lista
    my_list.sort();
    println!("Vec ordenado: {:?}", my_list);
    
    //elimina elemntos del final 
    my_list.pop();
    println!("Vec eliminamos el ultimo: {:?}", my_list);

    // eliminamos el primero
    my_list.remove(0);
    println!("Vec eliminamos 1 elemento: {:?}", my_list);

    // eliminamos el 3
    my_list.remove(2);
    println!("Vec eliminamos 3 elemento: {:?}", my_list);


    // Sets
    // es como el vector pero SIN duplicados y desordenado
    let mut my_set: HashSet<&str> = vec!("atienzar", "pedro", "juan", "52", "atienzar").into_iter().collect();
    println!("Set: {:?}", my_set);

    //add
    my_set.insert("pedro");
    println!("Set add Pedro: {:?}", my_set);
    
    //remove por valor
    my_set.remove("Pedro");
    println!("Set remove Pedro: {:?}", my_set);

    //comprobamos is existe juan
    if my_set.contains("juan") {
        println!("Set : Juan esta en la lista");
        
    }

    //obtenemos 1 elemento y lo borramos
    let elemento = "juan";
    my_set.take(elemento);
    println!("Set remove juan: {:?}", my_set);

    //ordenar => tenemos que sacar la lista de valores y ordenar.
    // al hacer esto, perdemos my_set. 
    let mut valores = my_set.into_iter().collect::<Vec<_>>();
    valores.sort();
    println!("Set valores ordenados: {:?}", valores);



    //Mapa KEY: VALUE
    let mut my_map: HashMap<&str,i32> = vec![("atienzar",52),("pedro",42),("pedrop",15)].into_iter().collect();
    println!("{:?}", my_map);
    my_map.insert("atienzaj", 26);
    println!("{:?}", my_map);

    println!("");
    agenda()


}