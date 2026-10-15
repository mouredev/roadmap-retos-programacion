fn func_extra1(msg1: String, msg2: String) -> [String; 2] {
    let ret1 = msg2;
    let ret2 = msg1;

    return [ret1, ret2];
}

fn func_extra2(msg1: &mut String, msg2: &mut String) -> [String; 2] {
    let ret1 = msg2.clone();
    let ret2 = msg1.clone();

    return [ret1, ret2];
}

fn func_by_value_string(msg: String) {
    println!("func_by_value_string: {msg}");
}

fn func_by_reference_string(msg: &String) {
    println!("func_by_reference_string: {msg}");
}

fn func_by_reference_string_mut(msg: &mut String) {
    println!("func_by_reference_string_mut: {msg}");
    *msg = msg.clone() + " added.";
}

fn func_by_value_primitive(n: u8, f: f32) {
    println!("func_by_value_primitive: {n} {f}");
}

fn func_by_reference_primitive(n: &u8, f: &f32) {
    println!("func_by_reference_primitive: {n} {f}");
}

fn func_by_reference_primitive_mut(n: &mut u8, f: &mut f32) {
    println!("func_by_reference_primitive_mut: {n} {f}");
    *n = 11;
    *f = 55.5;
}

fn func_by_value_vect(v: Vec<u8>) {
    println!("func_by_value_vect: {v:?}");
}

fn func_by_reference_vect(v: &Vec<u8>) {
    println!("func_by_reference_vect: {v:?}");
}

fn func_by_reference_vect_mut(v: &mut Vec<u8>) {
    println!("func_by_value_vect_mut: {v:?}");
    v[3] = 222;
}

fn main() {
    let string1 = String::from("Hello world");
    let mut string2 = String::from("Bye Bye");

    // The objects passed by value are moved and can not be used
    // after the function call because it free the data.
    func_by_value_string(string1);
    // The following line provoke a compilation error due to the
    //previous function call.
    //println!("{string1}");

    func_by_reference_string(&string2);
    println!("Main: {string2}");
    func_by_reference_string_mut(&mut string2);
    println!("Main: {string2}");

    let vec1 = vec![1, 3, 4, 6, 8, 9];
    let mut vec2 = vec![11, 33, 44, 66, 88, 99];
    println!("Main: {vec1:?}");
    func_by_value_vect(vec1);
    // The following line provoke a compilation error due to the previous

    //println!("Main: {vec1:?}");
    func_by_reference_vect(&vec2);
    println!("Main: {vec2:?}");
    func_by_reference_vect_mut(&mut vec2);
    println!("Main: {vec2:?}");

    // Primitive types are copied when they are passed by value (not moved)
    // And can be used after the function calls.
    let mut num1: u8 = 10;
    let mut float1: f32 = 44.3;
    println!("Main: num1: {num1}, float1: {float1}");
    func_by_value_primitive(num1, float1);
    println!("Main: num1: {num1}, float1: {float1}");
    func_by_reference_primitive(&num1, &float1);
    println!("Main: num1: {num1}, float1: {float1}");
    func_by_reference_primitive_mut(&mut num1, &mut float1);
    println!("Main: num1: {num1}, float1: {float1}");

    // Extra task
    let p1 = String::from("John");
    let p2 = String::from("Mary");
    let mut p3 = String::from("Edward");
    let mut p4 = String::from("Peter");

    println!("Old vars: p1: {p1} | p2: {p2} | p3: {p3} | p4: {p4}");

    let [s1, s2] = func_extra1(p1, p2);
    let [s3, s4] = func_extra2(&mut p3, &mut p4);

    println!("Old vars: p3: {p3} | p4: {p4}");
    println!("New vars: s1: {s1} | s2: {s2} | s3: {s3} | s4: {s4}");
}
