/*
╔═══════════════════════════════════════╗
║ Autor:  Kenys Alvarado                ║
║ GitHub: https://github.com/Kenysdev   ║
║ 2024 -  Rust                          ║
╚═══════════════════════════════════════╝
-----------------------------------------------------
* SOLID: PRINCIPIO DE SEGREGACIÓN DE INTERFACES (ISP)
-----------------------------------------------------
- Una estructura no debería estar obligada a implementar interfaces que no utiliza.
'   Evitando crear grandes clases monolíticas.

_______________
' NOTA: Este ejemplo muestra el uso CORRECTO. Para suponer un ejemplo que viole el principio, sería. 
'       Imaginar todos los métodos siguientes, en una sola interfaz, entonces algunos dispositivos
'       implementarían una interfaz que no necesitan.
*/

//____________________________________
// Interfaces
trait Playable {
    fn play(&self);
}

trait Displayable {
    fn display(&self);
}

//____________________________________
// Implementación

struct Speaker;

impl Playable for Speaker {
    fn play(&self) {
        println!("El altavoz está reproduciendo música.");
    }
}

//____________________________________
struct Phone;

impl Playable for Phone {
    fn play(&self) {
        println!("El teléfono está reproduciendo una canción.");
    }
}

impl Displayable for Phone {
    fn display(&self) {
        println!("El teléfono está mostrando la pantalla de reproducción.");
    }
}

/*
//____________________________________
* EJERCICIO #2:
'* Crea un gestor de impresoras.
'* Requisitos:
'* 1. Algunas impresoras sólo imprimen en blanco y negro.
'* 2. Otras sólo a color.
'* 3. Otras son multifunción, pueden imprimir, escanear y enviar fax.
'* Instrucciones:
'* 1. Implementa el sistema, con los diferentes tipos de impresoras y funciones.
'* 2. Aplica el ISP a la implementación.
'* 3. Desarrolla un código que compruebe que se cumple el principio.
*/

//____________________________________
// Interfaces
trait IPrinter {
    fn print_file(&self, file: &str);
}

trait IScanner {
    fn to_scan(&self, path_save: &str);
}

trait IFax {
    fn send_file(&self, file: &str, phone_number: i32);
}

//____________________________________
// Implementación

struct MonoPrinter;

impl IPrinter for MonoPrinter {
    fn print_file(&self, file: &str) {
        println!("\nImpresora blanco y negro:");
        println!("{} se imprimió.", file);
    }
}

//____________________________________
struct ColorPrinter;

impl IPrinter for ColorPrinter {
    fn print_file(&self, file: &str) {
        println!("\nImpresora a color:");
        println!("{} se imprimió.", file);
    }
}

//____________________________________
struct Scanner;

impl IScanner for Scanner {
    fn to_scan(&self, path_save: &str) {
        println!("\nEscaneo realizado, guardado en: {}", path_save);
    }
}

//____________________________________
struct Fax;

impl IFax for Fax {
    fn send_file(&self, file: &str, phone_number: i32) {
        println!("\n{} fue enviado a: {}", file, phone_number);
    }
}

//____________________________________
struct MultiFunctionPrinter {
    mono_printer: MonoPrinter,
    color_printer: ColorPrinter,
    scanner: Scanner,
    fax: Fax,
}

impl MultiFunctionPrinter {
    fn new() -> Self {
        MultiFunctionPrinter {
            mono_printer: MonoPrinter,
            color_printer: ColorPrinter,
            scanner: Scanner,
            fax: Fax,
        }
    }
}

//____________________________________
fn main() {
    // exs 1
    let speaker = Speaker;
    speaker.play();

    let phone = Phone;
    phone.play();
    phone.display();

    //____________________________________
    // exs 2
    println!("\nExs #2");

    // Individuales
    let mono_printer = MonoPrinter;
    mono_printer.print_file("filex.pdf");

    let color_printer = ColorPrinter;
    color_printer.print_file("filex.pdf");

    let scanner = Scanner;
    scanner.to_scan("c:\\docs");

    let fax = Fax;
    fax.send_file("filex.pdf", 12345678);

    //____________________________________
    println!("\n__________\nMultifunción");
    let mfp = MultiFunctionPrinter::new();

    mfp.mono_printer.print_file("filex.pdf");
    mfp.color_printer.print_file("filex.pdf");
    mfp.scanner.to_scan("c:\\docs");
    mfp.fax.send_file("filex.pdF", 123456789);

}
