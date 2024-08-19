/*
╔═══════════════════════════════════════╗
║ Autor:  Kenys Alvarado                ║
║ GitHub: https://github.com/Kenysdev   ║
║ 2024 -  Rust                          ║
╚═══════════════════════════════════════╝
-----------------------------------------
* DECORADORES
-----------------------------------------

* EJERCICIO #1:
* Explora el concepto de "decorador" y muestra cómo crearlo
* con un ejemplo genérico.
*/

// Rasgo Componente
trait Component {
    fn operation(&self, first_name: &str, last_name: &str);
}

// Implementar este rasgo
struct ConcreteComponent;

impl Component for ConcreteComponent {
    fn operation(&self, first_name: &str, last_name: &str) {
        println!("Hola, {} {}!", first_name, last_name);
    }
}

// Definir una estructura Decorator con su implementación:
struct MyDecorator<T: Component> {
    component: T,
}

impl<T: Component> MyDecorator<T> {
    fn new(component: T) -> Self {
        MyDecorator { component }
    }
}

impl<T: Component> Component for MyDecorator<T> {
    fn operation(&self, first_name: &str, last_name: &str) {
        println!("Antes de llamar a la función.");
        self.component.operation(first_name, last_name);
        println!("Después de llamarla.");
    }
}

/*
* EJERCICIO #2:
* Crea un decorador que sea capaz de contabilizar cuántas veces
* se ha llamado a una función y aplícalo a una función de tu elección.
*/

trait FunctionTrait {
    fn call(&mut self, func_name: &str);
}

struct Function {
    calls: usize,
}

impl Function {
    fn new() -> Self {
        Function { calls: 0 }
    }
}

impl FunctionTrait for Function {
    fn call(&mut self, func_name: &str) {
        self.calls += 1;
        println!("\nLa función '{}' ha sido llamada {} veces", func_name, self.calls);
    }
}
struct CountCalls<T: FunctionTrait> {
    wrapped_function: T,
}

impl<T: FunctionTrait> CountCalls<T> {
    fn new(wrapped_function: T) -> Self {
        CountCalls { wrapped_function }
    }
}

impl<T: FunctionTrait> FunctionTrait for CountCalls<T> {
    fn call(&mut self, func_name: &str) {
        self.wrapped_function.call(func_name);
    }
}

//____________________________________
fn main() {
    println!("EJERCICIO #1");

    let component = ConcreteComponent;
    let decorated_component = MyDecorator::new(component);

    decorated_component.operation("Zoe", "Roy");

    //____________________________________
    println!("EJERCICIO #2");

    let function_a = Function::new();
    let mut function_a = CountCalls::new(function_a);

    function_a.call("A");
    function_a.call("A");
    function_a.call("A");

    let function_b = Function::new();
    let mut function_b = CountCalls::new(function_b);

    function_b.call("B");
    function_b.call("B");
    
}
