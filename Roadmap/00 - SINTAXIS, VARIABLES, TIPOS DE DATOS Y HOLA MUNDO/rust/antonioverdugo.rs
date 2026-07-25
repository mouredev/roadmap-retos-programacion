fn main() {
    // https://rust-lang.org/es/
    // Comentario de una sola linea
    /*
     * Comentario de
     * varias lineas
     */
    /// Comentario de una linea Outer doc para el siguiente elemento
    /**
     * Comentario de varias lineas
     * Outer doc para el siguiente elemento
     */
    // //! Comentario de una linea Inner doc para el elemento padre
    // /*!
    //  * Comentario de varias lineas Inner doc
    //  * para el elemento padre
    //  */

    //- Crea una variable (y una constante si el lenguaje lo soporta).
    let variable = "hola que tal";
    const CONSTANTE: f32 = 3.1416;

    //- Crea variables representando todos los tipos de datos primitivos
    let ok = true;
    let character = 'b';
    let paragraph = "Viva er betis manque pierda";
    let slice = &paragraph[0..4]; // Tipo de dato slice
    let num_8: i8 = 127;
    let num_16: i16 = 1000;
    let num_32: i32 = 120000;
    let num_64: i64 = 100000000;
    let num_128: i128 = 100000000;
    let num_unsigned_8: u8 = 120;
    let num_unsigned_16: u16 = 1000;
    let num_unsigned_32: u32 = 100000;
    let num_unsigned_64: u64 = 10000000;
    let num_unsigned_128: u128 = 10000000000000;
    let num_float_32: f32 = 100.47;
    let num_float_64: f64 = 3589090.987;
    let tuple = ("hola", 78, true);
    let array: [&str; 5] = ["viva", "er", "betis", "manque", "pierda"];

    // - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
    let name = "Rust";
    println!("\"¡Hola, {}!\"", name);
}
