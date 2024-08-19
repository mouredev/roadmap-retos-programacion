/*
 * EXERCISE:
 * Implement the mechanisms of introduction and retrieval of elements typical of
 * stacks (stacks - LIFO) and queues (queue - FIFO) using an array
 * or list (depending on the possibilities of your language).
 */

fn main() {
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

    // CHALLENGE
    challenge();
}

/*
 * EXTRA DIFFICULTY (optional):
 * - Using the stack implementation and text strings, simulate the forward/back
 *   mechanism of a web browser. Create a program in which you can navigate to a page or tell it
 *   that you want to move forward or backward, showing in each case the name of the web.
 *   The words "forward", "backward" trigger this action, the rest is interpreted as
 *   the name of a new web.
 * - Using the queue implementation and text strings, simulate the mechanism of a
 *   shared printer that receives documents and prints them when indicated.
 *   The word "print" prints an element from the queue, the rest of the words are
 *   interpreted as document names.
 */
use std::io::{self};

fn challenge() {
    pub struct Pages<T> {
        elements: Vec<T>,
        position: usize,
    }

    impl<T> Pages<T> {
        // Create Stack
        pub fn new() -> Self {
            Pages {
                elements: Vec::new(),
                position: 0,
            }
        }
        // enqueue
        pub fn enqueue(&mut self, item: T) {
            self.elements.push(item);
            self.position += 1
        }

        pub fn check(&self) -> Option<&T> {
            if self.position > 0 {
                self.elements.get(self.position - 1)
            } else {
                self.elements.get(0)
            }
        }

        pub fn is_empty(&self) -> bool {
            self.elements.is_empty()
        }

        pub fn clear(&mut self) {
            self.elements.clear();
        }

        pub fn position_add(&mut self) {
            if self.position + 1 <= self.elements.len().try_into().unwrap() {
                self.position += 1
            }
        }

        pub fn position_sub(&mut self) {
            if self.position > 1 {
                self.position -= 1
            } else {
                self.position = 0
            }
        }
    }

    let mut pages = Pages::new();

    loop {
        println!(
            "
            ===========================
            What would you like to do?
            1. Add a page
            2. Delete all pages
            3. Forward
            4. Backward
            5. Print
            6. Exit
            ===========================
            "
        );

        let mut input = String::new();
        io::stdin()
            .read_line(&mut input)
            .expect("Failed to read line");

        let choice: u32 = input.trim().parse().expect("Invalid input");

        match choice {
            1 => add_page(&mut pages),
            2 => delete_pages(&mut pages),
            3 => go_forward(&mut pages),
            4 => go_backwards(&mut pages),
            5 => get_page(&mut pages),
            6 => {
                println!("Goodbye!");
                break;
            }
            _ => println!("Invalid choice. Please try again."),
        }

        println!();
    }
    fn add_page(pages: &mut Pages<String>) {
        println!("Enter the URL");
        let mut url: String = String::new();
        io::stdin().read_line(&mut url).expect("Failed to read Url");
        let url: String = url.trim().to_string();

        pages.enqueue(url)
    }

    fn delete_pages(pages: &mut Pages<String>) -> () {
        println!("Deleted all pages");
        pages.clear()
    }

    fn go_forward(pages: &mut Pages<String>) -> () {
        println!("Forward");
        pages.position_add()
    }

    fn go_backwards(pages: &mut Pages<String>) -> () {
        println!("Backward");
        pages.position_sub()
    }

    fn get_page(pages: &mut Pages<String>) -> () {
        println!("You are in:");
        if pages.is_empty() {
            println!("You have no pages in your browser");
            return;
        }

        let page = pages.check().unwrap();
        println!("{}", page);
    }
}
