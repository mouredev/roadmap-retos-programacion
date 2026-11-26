use std::fs::File;

#[derive(Debug)]
enum MyError {
    ERROR1,
    ERROR2,
    ERROR3,
}

fn process_with_error2(arg: i32) -> Result<i32, MyError> {
    let a = process_with_error(arg)?;
    Ok(a * 2)
}

fn process_with_error(arg: i32) -> Result<i32, MyError> {
    if arg > 0 {
        return Ok(arg + 1);
    } else if arg == -1 {
        return Err(MyError::ERROR1);
    } else if arg == -2 {
        return Err(MyError::ERROR2);
    } else {
        return Err(MyError::ERROR3);
    }
}

fn throw_panic_error() {
    panic!("Critical error");
}

fn div_by_zero(arg: i32) {
    let v = 10 / arg;
    println!("{v}");
}

fn access_oob_vector() {
    let v = vec![55, 66, 99];

    v[10];
}

fn read_nonexistent_file() {
    let file = File::open("file-noexistent.log");

    match file {
        Ok(f) => println!("File {f:?} opened :)"),
        Err(e) => println!("Error opening file: {e:?}"),
    };
}

fn main() {
    read_nonexistent_file();

    match process_with_error(3) {
        Ok(a) => println!("process_with_error SUCCESS {a}"),
        Err(e) => println!("process_with_error ERROR {e:?}"),
    }

    match process_with_error(-1) {
        Ok(a) => println!("process_with_error SUCCESS {a}"),
        Err(e) => println!("process_with_error ERROR {e:?}"),
    }

    match process_with_error(-2) {
        Ok(a) => println!("process_with_error SUCCESS {a}"),
        Err(e) => println!("process_with_error ERROR {e:?}"),
    }

    match process_with_error(-3) {
        Ok(a) => println!("process_with_error SUCCESS {a}"),
        Err(e) => println!("process_with_error ERROR {e:?}"),
    }

    match process_with_error2(3) {
        Ok(a) => println!("process_with_error2 SUCCESS {a}"),
        Err(e) => println!("process_with_error2 ERROR {e:?}"),
    }

    match process_with_error2(-1) {
        Ok(a) => println!("process_with_error2 SUCCESS {a}"),
        Err(e) => println!("process_with_error2 ERROR {e:?}"),
    }

    match process_with_error2(-2) {
        Ok(a) => println!("process_with_error2 SUCCESS {a}"),
        Err(e) => println!("process_with_error2 ERROR {e:?}"),
    }

    match process_with_error2(-3) {
        Ok(a) => println!("process_with_error2 SUCCESS {a}"),
        Err(e) => println!("process_with_error2 ERROR {e:?}"),
    }

    div_by_zero(0);
    access_oob_vector();
    throw_panic_error();
}
