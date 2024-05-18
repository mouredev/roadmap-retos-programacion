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
// use std::io::prelude::*;
use std::io::{Error, Read, Write};

fn create_file(filename: &str) -> Result<(), Error> {
    let file_name = format!("{}.txt", filename);
    let _ = File::create(file_name);
    Ok(())
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
}

// std::fs::remove_file("filename.txt")?;
