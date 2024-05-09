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
