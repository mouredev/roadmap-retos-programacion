/*
 * IMPORTANT: You should only upload the code file as part of the exercise.
 *
 * EXERCISE:
 * Develop a program capable of creating a file named after
 * your GitHub username and has the .txt extension.
 * Add several lines to that file:
 * - Your name.
 * - Age.
 * - Favorite programming language.
 * Print the content.
 * Delete the file.
 */

use std::fs::{File, OpenOptions};
use std::io::{self, Error, ErrorKind, Read, Write};

fn create_file(filename: &str) -> Result<(), Error> {
    let file_name = format!("{}.txt", filename);

    if !file_name.is_empty() {
        let _ = File::create(file_name);
        Ok(())
    } else {
        Err(Error::new(
            ErrorKind::InvalidInput,
            "You must provide a file name",
        ))
    }
}

fn write_file(filename: &str, contents: &str) -> Result<(), Error> {
    let file_name = format!("{}.txt", filename);
    let mut file = OpenOptions::new()
        .write(true)
        .append(true)
        .open(file_name)?;

    file.write_all(contents.as_bytes())?;
    Ok(())
}

fn read_file(filename: &str) -> Result<String, Error> {
    let file_name = format!("{}.txt", filename);
    let mut file = File::open(file_name)?;
    let mut contents = String::new();
    file.read_to_string(&mut contents)?;
    Ok(contents)
}

fn delete_file(filename: &str) -> Result<(), Error> {
    let file_name = format!("{}.txt", filename);
    std::fs::remove_file(file_name)?;
    Ok(())
}

/* EXTRA DIFFICULTY (optional):
 * Develop a sales management program that stores its data in a
 * .txt file.
 * - Each product is saved on a line of the file in the following way:
 *   [product_name], [quantity_sold], [price].
 * - Following that format, and through terminal, it should allow adding, consulting,
 *   updating, deleting products and exiting.
 * - It should also have options to calculate the total sale and by product.
 * - The exit option deletes the .txt.
 */

fn main() {
    match create_file("gabrielcmoris") {
        Ok(()) => println!("File Created sucessfully"),
        Err(err) => println!("There was an error: {}", err),
    }

    match write_file(
        "gabrielcmoris",
        "Name: Gabriel\nAge: 34\nFavorite programming language: Assembly",
    ) {
        Ok(()) => println!("File writted sucessfully"),
        Err(err) => println!("There was an error: {}", err),
    }

    match read_file("gabrielcmoris") {
        Ok(file) => println!("File contents {:?}", file),
        Err(err) => println!("There was an error: {}", err),
    }

    match delete_file("gabrielcmoris") {
        Ok(()) => println!("File deleted sucessfully"),
        Err(err) => println!("There was an error: {}", err),
    }

    sales_manager();
}

fn sales_manager() {
    loop {
        println!(
            "
            ===========================
            What would you like to do?
            1. Add a file
            2. Delete a file
            3. Read a file
            4. Edit a file
            5. Exit
            ===========================
            "
        );

        let mut input = String::new();
        io::stdin()
            .read_line(&mut input)
            .expect("Failed to read line");

        let choice: u32 = input.trim().parse().expect("Invalid input");

        match choice {
            1 => add_doc(),
            2 => delete_doc(),
            3 => read_doc(),
            4 => edit_doc(),
            5 => {
                println!("📁 Goodbye! 📁");
                break;
            }
            _ => println!("Invalid choice. Please try again."),
        }

        println!();
    }
}

fn add_doc() {
    println!("Enter the document Name");
    let mut doc_name: String = String::new();
    io::stdin()
        .read_line(&mut doc_name)
        .expect("Failed to read name");
    let doc_name: String = doc_name.trim().to_string();
    match create_file(&doc_name) {
        Ok(()) => println!("File Created sucessfully"),
        Err(err) => println!("There was an error: {}", err),
    }

    println!("Enter the product Name");
    let mut product_name: String = String::new();
    io::stdin()
        .read_line(&mut product_name)
        .expect("Failed to read name");
    let product_name: String = product_name.trim().to_string();

    println!("Enter the sold product amount");
    let mut product_amount: String = String::new();
    io::stdin()
        .read_line(&mut product_amount)
        .expect("Failed to read amount");
    let product_amount: String = product_amount.trim().to_string();

    println!("Enter the sold product price");
    let mut product_price: String = String::new();
    io::stdin()
        .read_line(&mut product_price)
        .expect("Failed to read price");
    let product_price: String = product_price.trim().to_string();

    let content = format!(
        "Product: {}\nUnits sold: {}\nPrice: {}",
        product_name, product_amount, product_price
    );

    match write_file(&doc_name, &content) {
        Ok(()) => println!("File writted sucessfully"),
        Err(err) => println!("There was an error: {}", err),
    }
}

fn delete_doc() {
    println!("Enter the document Name");
    let mut doc_name: String = String::new();
    io::stdin()
        .read_line(&mut doc_name)
        .expect("Failed to read name");
    let doc_name: String = doc_name.trim().to_string();

    match delete_file(&doc_name) {
        Ok(()) => println!("File deleted sucessfully"),
        Err(err) => println!("There was an error: {}", err),
    }
}

fn read_doc() {
    println!("Enter the document Name");
    let mut product_name: String = String::new();
    io::stdin()
        .read_line(&mut product_name)
        .expect("Failed to read name");
    let product_name: String = product_name.trim().to_string();

    match read_file(&product_name) {
        Ok(file) => println!("File contents {:?}", file),
        Err(err) => println!("There was an error: {}", err),
    }
}

fn edit_doc() {
    println!("Enter the document Name");
    let mut doc_name: String = String::new();
    io::stdin()
        .read_line(&mut doc_name)
        .expect("Failed to read name");
    let doc_name: String = doc_name.trim().to_string();

    println!("Enter the product Name.");
    let mut product_name: String = String::new();
    io::stdin()
        .read_line(&mut product_name)
        .expect("Failed to read name");
    let product_name: String = product_name.trim().to_string();

    println!("Enter the sold product amount.");
    let mut product_amount: String = String::new();
    io::stdin()
        .read_line(&mut product_amount)
        .expect("Failed to read amount");
    let product_amount: String = product_amount.trim().to_string();

    println!("Enter the sold product price.");
    let mut product_price: String = String::new();
    io::stdin()
        .read_line(&mut product_price)
        .expect("Failed to read price");
    let product_price: String = product_price.trim().to_string();

    let content = format!(
        "Product: {}\nUnits sold: {}\nPrice: {}",
        product_name, product_amount, product_price
    );

    match delete_file(&doc_name) {
        Ok(()) => println!("File deleted sucessfully"),
        Err(err) => println!("There was an error: {}", err),
    }
    match create_file(&doc_name) {
        Ok(()) => println!("File Created sucessfully"),
        Err(err) => println!("There was an error: {}", err),
    }

    match write_file(&doc_name, &content) {
        Ok(()) => println!("File writted sucessfully"),
        Err(err) => println!("There was an error: {}", err),
    }
}
