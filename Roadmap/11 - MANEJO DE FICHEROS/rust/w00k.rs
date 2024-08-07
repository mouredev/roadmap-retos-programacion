use std::fs::File;
use std::io::Write;
use std::fs;

fn main() {
    // Data you want to write to the file
    let data = "Name: w00k.\nAge: 41 años.\nFavorite programming language: Java";
    let file_name = "w00k.txt";

    // Open the file in write mode, creating it if it doesn't exist
    let mut file = File::create(file_name).expect("Error creating file");

    // Write the data to the file
    file.write_all(data.as_bytes()).expect("Error writing to the file");

    println!("Successfully wrote data to {}", file_name);

    let contents = fs::read_to_string(file_name)
        .expect("Should have been able to read the file");

    println!("\nWith text:\n{contents}\n");

    fs::remove_file(file_name).expect("File not found");

    println!("Delete file");

}