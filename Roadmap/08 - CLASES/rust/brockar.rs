/*
* EJERCICIO:
Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
atributos y una función que los imprima (teniendo en cuenta las posibilidades
de tu lenguaje).
Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
utilizando su función.
*/
use std::fmt;
struct User {
    username: String,
    email: String,
    count: u8,
}

fn init_user(email: String, username: String) -> User {
    User {
        email,
        username,
        count: 0,
    }
}

fn count_user(user: &mut User) {
    user.count += 1;
}
impl fmt::Display for User {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(
            f,
            "User: \n -Username: {}\n -Email: {}\n -Count: {}",
            self.username, self.email, self.count
        )
    }
}

fn main() {
    let mut user = init_user("brockar@mouredev.com".to_string(), "brockar".to_string());
    count_user(&mut user);
    println!("{}", user);

    //Extra Pila
    println!("\n\nEXTRA PILA");

    let mut p: Pila<u32> = init_pila::<u32>();
    println!("{}", p);

    push_pila(&mut p, 1);
    push_pila(&mut p, 2);
    push_pila(&mut p, 3);
    println!("{}", p);
    println!("\nLa pila tiene {} elementos.\n", n_elementos_pila(&p));
    println!("Pop: {:?}", pop_pila(&mut p));
    println!("Pop: {:?}", pop_pila(&mut p));
    println!("Pop: {:?}", pop_pila(&mut p));
    println!("Pop: {:?}", pop_pila(&mut p));
    println!("{}", p);

    println!("\n\nEXTRA COLA");

    let mut c: Cola<u32> = init_cola::<u32>();
    println!("{}", c);

    push_cola(&mut c, 1);
    push_cola(&mut c, 2);
    push_cola(&mut c, 3);

    println!("{}", c);
    println!("\nLa cola tiene {} elementos.\n", n_elementos_cola(&c));
    
    println!("Pop: {:?}", pop_cola(&mut c));
    println!("Pop: {:?}", pop_cola(&mut c));
    println!("Pop: {:?}", pop_cola(&mut c));
    println!("Pop: {:?}", pop_cola(&mut c));
    println!("{}", c);
}

 /*
 * DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido.
 */
//-----------------PILA-----------------
struct Pila<T> {
    contenido: Vec<T>,
}

fn init_pila<T>() -> Pila<T>{
    Pila{
        contenido: vec![]
    }
}

fn push_pila<T>(pila: &mut Pila<T>, valor: T) {
    pila.contenido.push(valor);
}

fn pop_pila<T: Default>(pila: &mut Pila<T>) -> T {
    if !pila.contenido.is_empty() {
        return pila.contenido.pop().unwrap();
    }
    println!("Pila vacia!!!");
    T::default()
}

fn n_elementos_pila <T>(pila: &Pila<T>) -> usize {
    pila.contenido.len()
}

impl<T: std::fmt::Debug> fmt::Display for Pila<T>{
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "Pila: \n -Contenido: {:?}", self.contenido)
    }
}



//-----------------COLA-----------------
struct Cola<T> {
    contenido: Vec<T>,
}

fn init_cola<T>() -> Cola<T>{
    Cola{
        contenido: vec![]
    }
}

fn push_cola<T>(cola: &mut Cola<T>, valor: T) {
    cola.contenido.push(valor);
}

fn pop_cola<T: Default>(cola: &mut Cola<T>) -> T {
    if !cola.contenido.is_empty() {
        return cola.contenido.remove(0);
    }
    println!("Cola vacia!!!");
    T::default()
}

fn n_elementos_cola <T>(cola: &Cola<T>) -> usize {
    cola.contenido.len()
}

impl<T: std::fmt::Debug> fmt::Display for Cola<T>{
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "Cola: \n -Contenido: {:?}", self.contenido)
    }
}