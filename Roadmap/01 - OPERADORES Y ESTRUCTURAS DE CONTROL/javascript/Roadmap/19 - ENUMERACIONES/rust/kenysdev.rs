/*
╔═══════════════════════════════════════╗
║ Autor:  Kenys Alvarado                ║
║ GitHub: https://github.com/Kenysdev   ║
║ 2024 -  Rust                          ║
╚═══════════════════════════════════════╝
-----------------------------------------
* ENUMERACIONES
-----------------------------------------
https://www.rustlang-es.org/rust-book-es/ch06-00-enums.html

* EJERCICIO 1:
* Empleando tu lenguaje, explora la definición del tipo de dato
* que sirva para definir enumeraciones (Enum).
* Crea un Enum que represente los días de la semana del lunes
* al domingo, en ese orden. Con ese enumerado, crea una operación
* que muestre el nombre del día de la semana dependiendo del número entero
* utilizado (del 1 al 7).
*/

#[derive(Debug, PartialEq)]
enum Weekday {
    Monday = 1,
    Tuesday = 2,
    Wednesday = 3,
    Thursday = 4,
    Friday = 5,
    Saturday = 6,
    Sunday = 7,
}

impl Weekday {
    fn from_i32(num: i32) -> Option<Weekday> {
        match num {
            1 => Some(Weekday::Monday),
            2 => Some(Weekday::Tuesday),
            3 => Some(Weekday::Wednesday),
            4 => Some(Weekday::Thursday),
            5 => Some(Weekday::Friday),
            6 => Some(Weekday::Saturday),
            7 => Some(Weekday::Sunday),
            _ => None,
        }
    }

    fn get_day(num: i32) -> String {
        if let Some(weekday) = Weekday::from_i32(num) {
            format!("{:?}", weekday)
        } else {
            String::from("'o'")
        }
    }
}

/*
* EJERCICIO 2:
* Crea un pequeño sistema de gestión del estado de pedidos.
* Implementa una clase que defina un pedido con las siguientes características:
* - El pedido tiene un identificador y un estado.
* - El estado es un Enum con estos valores: PENDIENTE, ENVIADO, ENTREGADO y CANCELADO.
* - Implementa las funciones que sirvan para modificar el estado:
*   - Pedido enviado
*   - Pedido cancelado
*   - Pedido entregado
*   (Establece una lógica, por ejemplo, no se puede entregar si no se ha enviado, etc...)
* - Implementa una función para mostrar un texto descriptivo según el estado actual.
* - Crea diferentes pedidos y muestra cómo se interactúa con ellos. 
*/

#[derive(Debug, PartialEq)] 
enum Status {
    PENDING,
    SHIPPED,
    DELIVERED,
    CANCELED,
}

struct Order {
    identifier: String,
    status: Status,
}

impl Order {
    fn new(identifier: &str) -> Self {
        Order {
            identifier: identifier.to_string(),
            status: Status::PENDING,
        }
    }

    fn send(&mut self) {
        println!("\nEnviar:");
        if self.status == Status::PENDING {
            self.status = Status::SHIPPED;
            println!("{}", self.info());
        } else {
            self.invalid();
        }
    }

    fn cancel(&mut self) {
        println!("\nCancelar:");
        if self.status == Status::PENDING {
            self.status = Status::CANCELED;
            println!("{}", self.info());
        } else {
            self.invalid();
        }
    }

    fn deliver(&mut self) {
        println!("\nEntregar:");
        if self.status == Status::SHIPPED {
            self.status = Status::DELIVERED;
            println!("{}", self.info());
        } else {
            self.invalid();
        }
    }

    fn info(&self) -> String {
        format!("{} is {:?}", self.identifier, self.status)
    }

    fn invalid(&self) {
        println!("Invalid operation, {}", self.info());
    }
}

fn main() {
    println!("{}", Weekday::get_day(7));
    println!("{}", Weekday::get_day(3));
    println!("{}", Weekday::get_day(9));

     // Creación de pedidos
     let mut libro1 = Order::new("libro1");
     let mut libro2 = Order::new("libro2");
     let mut libro3 = Order::new("libro3");
 
     // Positivas
     println!("\n-----\nOperaciones exitosas:\n-----");
     libro1.send();
     libro1.deliver();
     libro2.cancel();
 
     // Negativas
     println!("\n-----\nOperaciones inválidas:\n-----");
     libro3.deliver();
     libro2.cancel();
     libro1.send();
 
     // Info
     println!("\n-----\nEstado de órdenes\n-----");
     println!("{}", libro1.info());
     println!("{}", libro2.info());
     println!("{}", libro3.info());

}
