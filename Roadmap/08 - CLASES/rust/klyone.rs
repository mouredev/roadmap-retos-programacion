use std::fmt::Debug;

pub struct Fifo<T: Clone + Debug> {
    list: Vec<T>,
}

impl<T: Clone + Debug> Fifo<T> {
    fn print(&self) {
        println!("{:?}", self.list);
    }

    fn enqueue(&mut self, item: T) {
        self.list.insert(self.list.len(), item.clone());
    }

    fn dequeue(&mut self) -> Option<T> {
        if self.list.len() == 0 {
            return None;
        } else {
            return Some(self.list.remove(0));
        }
    }

    fn peek(&self) -> Option<T> {
        if self.list.len() == 0 {
            return None;
        } else {
            return Some(self.list[0].clone());
        }
    }
}

fn run_fifo() {
    let mut fifo1: Fifo<u8> = Fifo { list: Vec::new() };

    fifo1.print();
    fifo1.enqueue(9);
    fifo1.enqueue(19);
    fifo1.enqueue(29);
    fifo1.enqueue(39);
    fifo1.print();
    println!("peek: {}", fifo1.peek().unwrap());
    fifo1.dequeue();
    fifo1.print();
    fifo1.dequeue();
    fifo1.print();
    fifo1.dequeue();
    fifo1.print();
    fifo1.dequeue();
    fifo1.print();
}

pub struct Lifo<T: Clone + Debug> {
    list: Vec<T>,
}

impl<T: Clone + Debug> Lifo<T> {
    fn print(&self) {
        println!("{:?}", self.list);
    }

    fn push(&mut self, item: T) {
        self.list.insert(0, item.clone());
    }

    fn pop(&mut self) -> Option<T> {
        if self.list.len() == 0 {
            return None;
        } else {
            return Some(self.list.remove(0));
        }
    }

    fn peek(&self) -> Option<T> {
        if self.list.len() == 0 {
            return None;
        } else {
            return Some(self.list[0].clone());
        }
    }
}

fn run_lifo() {
    let mut lifo1: Lifo<&str> = Lifo { list: Vec::new() };

    lifo1.print();
    lifo1.push("hello");
    lifo1.push("bryan");
    lifo1.push("mary");
    lifo1.push("bye");
    lifo1.print();
    println!("peek: {}", lifo1.peek().unwrap());
    lifo1.pop();
    lifo1.print();
    lifo1.pop();
    lifo1.print();
    lifo1.pop();
    lifo1.print();
    lifo1.pop();
    lifo1.print();
}

pub struct MyClass<'a> {
    list: Vec<&'a str>,
    valid: bool,
    prio: u8,
}

impl<'a> MyClass<'a> {
    fn set_prio(&mut self, p: u8) {
        self.prio = p;
    }

    fn get_prio(&self) -> u8 {
        return self.prio;
    }

    fn set_valid(&mut self, v: bool) {
        self.valid = v;
    }

    fn get_valid(&self) -> bool {
        return self.valid;
    }

    fn set_list(&mut self, l: Vec<&'a str>) {
        self.list = l;
    }

    fn get_list(&self) -> Vec<&'a str> {
        return self.list.clone();
    }
    fn print(&self) {
        println!("####################");
        println!("Dump MyClass");
        println!("####################");
        println!("list: {:?}", self.list);
        println!("valid: {}", self.valid);
        println!("prio: {}", self.prio);
        println!("####################");
    }
}

fn main() {
    let mut c1 = MyClass {
        list: Vec::new(),
        valid: false,
        prio: 130,
    };

    c1.print();
    println!("List: {:?}", c1.get_list());
    c1.set_list(["hello", "world"].to_vec());
    println!("List: {:?}", c1.get_list());
    println!("Valid: {}", c1.get_valid());
    c1.set_valid(true);
    println!("Valid: {}", c1.get_valid());
    println!("Prio: {}", c1.get_prio());
    c1.set_prio(121);
    println!("Prio: {}", c1.get_prio());
    c1.print();

    println!("FIFO test");
    run_fifo();

    println!("LIFO test");
    run_lifo();
}
