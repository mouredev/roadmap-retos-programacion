/*
_____________________________________
https://github.com/kenysdev
2024 - Rust
_____________________________________
41 CAMISETA RAR
-------------------------------------
* EJERCICIO:
* ¿Has visto la camiseta.rar?
 * https://x.com/MoureDev/status/1841531938961592740
 *
 * Crea un programa capaz de comprimir un archivo
 * en formato .zip (o el que tú quieras).
 * - No subas el archivo o el zip.

[dependencies]
zip = "2.2.1"
*/

use std::fs::File;
use std::io::{self, Write};
use std::path::Path;
use zip::{write::FileOptions, CompressionMethod, ZipWriter};

pub fn compress_file<P: AsRef<Path>>(source_file: P, zip_file: P) -> io::Result<()> {
    if !source_file.as_ref().exists() {
        return Err(io::Error::new(
            io::ErrorKind::NotFound,
            format!(
                "El archivo fuente '{}' no existe.",
                source_file.as_ref().display()
            ),
        ));
    }

    if let Some(zip_dir) = zip_file.as_ref().parent() {
        if !zip_dir.exists() {
            return Err(io::Error::new(
                io::ErrorKind::NotFound,
                format!("El directorio '{}' no existe.", zip_dir.display()),
            ));
        }
    }

    if zip_file.as_ref().exists() {
        return Err(io::Error::new(
            io::ErrorKind::AlreadyExists,
            format!(
                "El archivo zip '{}' ya existe.",
                zip_file.as_ref().display()
            ),
        ));
    }

    let file = File::create(zip_file.as_ref())?;
    let mut zip = ZipWriter::new(file);

    let file_name = source_file
        .as_ref()
        .file_name()
        .and_then(|n| n.to_str())
        .ok_or_else(|| {
            io::Error::new(
                io::ErrorKind::InvalidInput,
                "No se pudo obtener el nombre del archivo",
            )
        })?;

    let options = FileOptions::default().compression_method(CompressionMethod::Deflated)
        as FileOptions<'_, ()>;

    zip.start_file(file_name, options)?;

    let source_content = std::fs::read(source_file.as_ref())?;
    zip.write_all(&source_content)?;
    zip.finish()?;
    
    Ok(())
}

fn main() {
    match compress_file("D:\\dev\\tmp\\users.csv", "D:\\dev\\tmp\\file.zip") {
        Ok(_) => println!("Compresión completada exitosamente"),
        Err(e) => eprintln!("Error al comprimir: {}", e),
    }
}
