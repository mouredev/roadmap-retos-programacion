fn printer_action(doc_op: &str, printer: &mut Vec<String>) {
    if doc_op == "imprimir" {
        let job = fifo_dequeue(printer);
        if let Some(j) = job {
            println!("Printing {}", j);
        } else {
            println!("Printer queue empty");
        }
    } else {
        fifo_enqueue(printer, String::from(doc_op));
    }
}

fn printer_fifo_test() {
    let mut printer = Vec::new();

    printer_action("imprimir", &mut printer);
    printer_action("my_doc.docx", &mut printer);
    printer_action("my_pdf.pdf", &mut printer);
    printer_action("my_ppt.ppt", &mut printer);
    printer_action("imprimir", &mut printer);
    printer_action("imprimir", &mut printer);
    printer_action("imprimir", &mut printer);
    printer_action("imprimir", &mut printer);
}

fn print_url(stack: &Vec<String>) {
    let mut path = String::from("/");

    for folder in stack.iter().rev() {
        path.push_str(folder);
        path.push_str("/");
    }

    if path != "/" {
        path.pop();
    }

    println!("Current path: {path}");
}

fn web_browser_action(operation: &str, stack: &mut Vec<String>) {
    if operation.contains("adelante") {
        let arg: Vec<&str> = operation.split(' ').collect();
        if arg.len() != 2 {
            println!("Error: path not specified with adelante command");
        }
        lifo_push(stack, String::from(arg[1]));
    } else if operation.contains("atras") {
        lifo_pop(stack);
    }
}

fn web_browser_lifo_test() {
    let mut path_stack = Vec::from([String::from("home")]);

    web_browser_action("adelante test", &mut path_stack);
    print_url(&path_stack);
    web_browser_action("adelante resource", &mut path_stack);
    print_url(&path_stack);
    web_browser_action("atras", &mut path_stack);
    print_url(&path_stack);
    web_browser_action("atras", &mut path_stack);
    print_url(&path_stack);
    web_browser_action("atras", &mut path_stack);
    print_url(&path_stack);
    web_browser_action("atras", &mut path_stack);
    print_url(&path_stack);
}

fn fifo_enqueue<T: Clone>(fifo: &mut Vec<T>, elem: T) {
    fifo.insert(fifo.len(), elem.clone());
}

fn fifo_dequeue<T: Clone>(fifo: &mut Vec<T>) -> Option<T> {
    if fifo.len() == 0 {
        return None;
    } else {
        let elem: T = fifo.remove(0);
        return Some(elem);
    }
}

fn fifo_peek<T: Clone>(fifo: &Vec<T>) -> Option<T> {
    if fifo.len() == 0 {
        return None;
    } else {
        let elem: T = fifo[0].clone();
        return Some(elem);
    }
}

fn lifo_push<T: Clone>(lifo: &mut Vec<T>, elem: T) {
    lifo.insert(0, elem.clone());
}

fn lifo_pop<T: Clone>(lifo: &mut Vec<T>) -> Option<T> {
    if lifo.len() == 0 {
        return None;
    } else {
        let elem: T = lifo.remove(0);
        return Some(elem);
    }
}

fn lifo_peek<T: Clone>(lifo: &Vec<T>) -> Option<T> {
    if lifo.len() == 0 {
        return None;
    } else {
        let elem: T = lifo[0].clone();
        return Some(elem);
    }
}

fn main() {
    let mut fifo: Vec<u8> = vec![1, 2, 3, 4, 5];
    let mut elem;

    println!("FIFO test");
    println!("{:?}", fifo);
    println!("peek: {}", fifo_peek(&fifo).unwrap());
    elem = fifo_dequeue(&mut fifo);
    println!("elem: {} -> {:?}", elem.unwrap(), fifo);
    elem = fifo_dequeue(&mut fifo);
    println!("elem: {} -> {:?}", elem.unwrap(), fifo);
    elem = fifo_dequeue(&mut fifo);
    println!("elem: {} -> {:?}", elem.unwrap(), fifo);
    elem = fifo_dequeue(&mut fifo);
    println!("elem: {} -> {:?}", elem.unwrap(), fifo);
    elem = fifo_dequeue(&mut fifo);
    println!("elem: {} -> {:?}", elem.unwrap(), fifo);
    fifo_enqueue(&mut fifo, 10);
    println!("{:?}", fifo);
    fifo_enqueue(&mut fifo, 20);
    println!("{:?}", fifo);
    fifo_enqueue(&mut fifo, 30);
    println!("{:?}", fifo);
    fifo_enqueue(&mut fifo, 40);
    println!("{:?}", fifo);
    fifo_enqueue(&mut fifo, 50);
    println!("{:?}", fifo);
    println!("peek: {}", fifo_peek(&fifo).unwrap());
    elem = fifo_dequeue(&mut fifo);
    println!("elem: {} -> {:?}", elem.unwrap(), fifo);
    elem = fifo_dequeue(&mut fifo);
    println!("elem: {} -> {:?}", elem.unwrap(), fifo);
    elem = fifo_dequeue(&mut fifo);
    println!("elem: {} -> {:?}", elem.unwrap(), fifo);
    elem = fifo_dequeue(&mut fifo);
    println!("elem: {} -> {:?}", elem.unwrap(), fifo);
    elem = fifo_dequeue(&mut fifo);
    println!("elem: {} -> {:?}", elem.unwrap(), fifo);

    println!("LIFO test");
    let mut lifo: Vec<u8> = vec![1, 2, 3, 4, 5];
    println!("{:?}", lifo);
    println!("peek: {}", lifo_peek(&lifo).unwrap());
    elem = lifo_pop(&mut lifo);
    println!("elem: {} -> {:?}", elem.unwrap(), lifo);
    elem = lifo_pop(&mut lifo);
    println!("elem: {} -> {:?}", elem.unwrap(), lifo);
    elem = lifo_pop(&mut lifo);
    println!("elem: {} -> {:?}", elem.unwrap(), lifo);
    elem = lifo_pop(&mut lifo);
    println!("elem: {} -> {:?}", elem.unwrap(), lifo);
    elem = lifo_pop(&mut lifo);
    println!("elem: {} -> {:?}", elem.unwrap(), lifo);
    lifo_push(&mut lifo, 10);
    println!("{:?}", lifo);
    lifo_push(&mut lifo, 20);
    println!("{:?}", lifo);
    lifo_push(&mut lifo, 30);
    println!("{:?}", lifo);
    lifo_push(&mut lifo, 40);
    println!("{:?}", lifo);
    lifo_push(&mut lifo, 50);
    println!("{:?}", lifo);
    println!("peek: {}", lifo_peek(&lifo).unwrap());
    elem = lifo_pop(&mut lifo);
    println!("elem: {} -> {:?}", elem.unwrap(), lifo);
    elem = lifo_pop(&mut lifo);
    println!("elem: {} -> {:?}", elem.unwrap(), lifo);
    elem = lifo_pop(&mut lifo);
    println!("elem: {} -> {:?}", elem.unwrap(), lifo);
    elem = lifo_pop(&mut lifo);
    println!("elem: {} -> {:?}", elem.unwrap(), lifo);
    elem = lifo_pop(&mut lifo);
    println!("elem: {} -> {:?}", elem.unwrap(), lifo);

    println!("Web browser test");
    web_browser_lifo_test();

    println!("Printer test");
    printer_fifo_test();
}
