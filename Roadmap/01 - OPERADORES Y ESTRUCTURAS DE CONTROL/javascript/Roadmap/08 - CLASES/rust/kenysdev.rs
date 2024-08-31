/*
╔═══════════════════════════════════════╗
║ Autor:  Kenys Alvarado                ║
║ GitHub: https://github.com/Kenysdev   ║
║ 2024 -  Rust                          ║
╚═══════════════════════════════════════╝
-----------------------------------------
* CLASES
-----------------------------------------
- En Rust no existen clases.
- Rust usa estructuras y enumeraciones para crear tipos personalizados y 
  bloques impl para definir métodos en esos tipos.
*/
struct Person {
    name: String,
    age: u32,
}
  
impl Person {
    // Constructor
    fn new(name: String, age: u32) -> Self {
        Person { name, age }
    }
  
    // Método
    fn print(&self) {
        println!("Nombre: {} - Edad: {}", self.name, self.age);
    }
}
  
/* ----------------------------------------
 * Ejercicio:
   ----------------------------------------
 - Implementa dos clases que representen las estructuras de Pila y Cola 
   (estudiadas en el ejercicio número 7 de la ruta de estudio)
 - Deben poder inicializarse y disponer de operaciones para añadir, 
   eliminar, retornar el número de elementos e imprimir todo su contenido.
  _________________________________________
 * Pilas(stack - LIFO): 
*/
use std::fmt::Display;

struct MyStack<T> {
    stack: Vec<T>,
}

impl<T> MyStack<T> {
    fn new() -> Self {
        MyStack {
            stack: Vec::new(),
        }
    }

    fn push(&mut self, item: T) {
        self.stack.push(item);
    }

    fn pop(&mut self) -> Option<T> {
        self.stack.pop()
    }

    fn count(&self) -> usize {
        self.stack.len()
    }

    fn print(&self)
        where
            T: std::fmt::Display,
        {
            for item in self.stack.iter().rev() {
                println!("{}", item);
            }
        }
}

// _________________________________________
// Colas (Queue - FIFO):
use std::collections::VecDeque;

struct MyQueue<T> {
    queue: VecDeque<T>,
}

impl<T> MyQueue<T> {
    fn new() -> Self {
        MyQueue {
            queue: VecDeque::new(),
        }
    }

    fn enqueue(&mut self, item: T) {
        self.queue.push_back(item);
    }

    fn dequeue(&mut self) -> Option<T> {
        self.queue.pop_front()
    }

    fn count(&self) -> usize {
        self.queue.len()
    }

    fn print(&self)
        where
            T: Display,
        {

            for item in &self.queue {
                println!("{}", item);
            }
        }
}

fn main() {
    // ______________
    let person = Person::new(String::from("Ben"), 21);
    person.print();

    // ______________
    println!("\nUso de pila:");
    let mut stack = MyStack::<i32>::new();
    stack.push(1);
    stack.push(2);
    stack.push(3);

    println!("Count: {}", stack.count());
    stack.print();

    stack.pop();
    println!("Count: {}", stack.count());
    stack.print();

    // ______________
    println!("\nUso de cola:");
    let mut queue = MyQueue::<i32>::new();
    queue.enqueue(1);
    queue.enqueue(2);
    queue.enqueue(3);

    println!("Count: {}", queue.count());
    queue.print();

    queue.dequeue();
    println!("Count: {}", queue.count());
    queue.print();

}
