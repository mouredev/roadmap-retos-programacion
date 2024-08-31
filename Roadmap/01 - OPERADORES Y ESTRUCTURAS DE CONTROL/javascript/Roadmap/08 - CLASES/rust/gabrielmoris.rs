/*
 * EXERCISE:
 * Explore the concept of a class and create an example that implements an initializer,
 * attributes, and a function that prints them (taking into account the possibilities
 * of your language).
 * Once implemented, create it, set its parameters, modify them, and print them
 * using its function.
 */

fn main() {
    // Creation. The where specifies that Items can be displayed
    pub struct Class<T>
    where
        T: std::fmt::Display,
    {
        elements: Vec<T>,
    }

    // Initialization
    impl<T> Class<T>
    where
        T: std::fmt::Display,
    {
        // Create Stack
        pub fn new() -> Self {
            Class {
                elements: Vec::new(),
            }
        }

        pub fn print(&mut self) {
            for n in &self.elements {
                println!("{}", n);
            }
        }

        pub fn push(&mut self, item: T) {
            self.elements.push(item);
        }

        pub fn clear(&mut self) {
            self.elements.clear();
        }
    }

    let mut class_example: Class<i32> = Class::new();
    class_example.push(1);
    class_example.push(1);
    class_example.push(3);
    class_example.push(7);
    class_example.push(12);
    class_example.print();
    class_example.clear();

    /* EXTRA DIFFICULTY (optional):
     * Implement two classes that represent the Stack and Queue structures (studied
     * in exercise number 7 of the study path)
     * - They must be able to initialize and have operations to add, remove,
     *   return the number of elements, and print all their contents.
     */

    // STACK
    pub struct Stack<T> {
        elements: Vec<T>,
    }

    impl<T> Stack<T> {
        // Create Stack
        pub fn new() -> Self {
            Stack {
                elements: Vec::new(),
            }
        }
        // Push Item
        pub fn push(&mut self, item: T) {
            self.elements.push(item);
        }
        // Pop Item
        pub fn pop(&mut self) -> Option<T> {
            self.elements.pop()
        }

        // Check Item
        pub fn check(&self) -> Option<&T> {
            self.elements.last()
        }
        // Is Empty
        pub fn is_empty(&self) -> bool {
            self.elements.is_empty()
        }

        pub fn clear(&mut self) {
            self.elements.clear();
        }

        pub fn length(&self) -> usize {
            self.elements.len()
        }
    }
    println!(" ======== STACK ======== ");
    let mut stack = Stack::new();
    stack.push(1);
    stack.push(1);
    println!("{:?}", stack.length()); // Prints: 2
    stack.clear();
    println!("{:?}", stack.length()); // Prints: 0
    stack.push(1);
    stack.push(2);
    println!("{:?}", stack.pop()); // Prints: Some(2)
    println!("{:?}", stack.check().unwrap()); // Prints: 1
    println!("{:?}", stack.is_empty()); // Prints: false
    println!("{:?}", stack.pop().unwrap()); // Prints: 1
    println!("{:?}", stack.is_empty()); // Prints: true

    // QUEUE
    pub struct Queue<T> {
        elements: Vec<T>,
    }

    impl<T> Queue<T> {
        // Create Stack
        pub fn new() -> Self {
            Queue {
                elements: Vec::new(),
            }
        }
        // enqueue
        pub fn enqueue(&mut self, item: T) {
            self.elements.push(item);
        }

        pub fn dequeue(&mut self) -> T {
            self.elements.remove(0)
        }

        pub fn check(&self) -> Option<&T> {
            self.elements.first()
        }

        pub fn length(&self) -> usize {
            self.elements.len()
        }

        pub fn is_empty(&self) -> bool {
            self.elements.is_empty()
        }

        pub fn clear(&mut self) {
            self.elements.clear();
        }
    }
    println!(" ======== QUEUE ======== ");
    let mut queue = Queue::new();
    queue.enqueue(1);
    queue.enqueue(1);
    println!("{:?}", queue.length()); // Prints: 2
    queue.clear();
    println!("{:?}", queue.length()); // Prints: 0
    queue.enqueue(1);
    queue.enqueue(2);
    println!("{:?}", queue.dequeue()); // Prints: 1
    println!("{:?}", queue.check().unwrap()); // Prints: 2
    println!("{:?}", queue.is_empty()); // Prints: false
    println!("{:?}", queue.dequeue()); // Prints: 2
    println!("{:?}", queue.is_empty()); // Prints: true
}
