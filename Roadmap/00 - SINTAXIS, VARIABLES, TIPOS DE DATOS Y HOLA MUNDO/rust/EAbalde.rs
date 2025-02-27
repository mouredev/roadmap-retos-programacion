/*
Comentario en bloque con el enunciado del ejercicio:

¿Preparad@ para aprender o repasar el lenguaje de programación que tú quieras?
- Recuerda que todas las instrucciones de participación están en el
repositorio de GitHub.

Lo primero... ¿Ya has elegido un lenguaje?
- No todos son iguales, pero sus fundamentos suelen ser comunes.
- Este primer reto te servirá para familiarizarte con la forma de participar
enviando tus propias soluciones.

EJERCICIO:
- Crea un comentario en el código y coloca la URL del sitio web oficial del
lenguaje de programación que has seleccionado.
- Representa las diferentes sintaxis que existen de crear comentarios
en el lenguaje (en una línea, varias...).
- Crea una variable (y una constante si el lenguaje lo soporta).
- Crea variables representando todos los tipos de datos primitivos
del lenguaje (cadenas de texto, enteros, booleanos...).
- Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"

¿Fácil? No te preocupes, recuerda que esta es una ruta de estudio y
debemos comenzar por el principio.
 */

// Comentario de una sola línea con la URL oficial:  https://www.rust-lang.org

fn main() {
/*
Rust no permite declarar variables que no sean usadas.
Para evitar que marque warnings en esas variables
es necesario iniciarlas con un guión bajo.
*/	
	// VARIABLES Y CONSTANTES:
	let _x = 1; // Esta es una variable inmutable.
	let mut _y = 2; // Esta es una variable mutable.

	const _YEAR: i32 = 365; // Esta es una constante.

	// DATOS PRIMITIVOS ESCALARES:
	let _a: i32 = -50; // Enteros con signo. Pueden ser i8, i16, i32, i64, i128 o isize.
	let _b: u32 = 100; // Enteros sin signo. Pueden ser u8, u16, u32, u64, u128 o usize.
	let _c: f32 = 1.0; // Decimales o de coma flotante. Pueden ser f32 o f64.
	let _d = true; // Datos booleanos. Pueden ser true o false.
	let _e: char = 'A'; // Caracteres Unicode. Pueden ser letras, números o símbolos.
	let _f: &str = "¡Hola Mundo!"; // Cadenas de texto.

	// DATOS PRIMITIVOS COMPUESTOS:

	// Arreglo o array. Colección de elementos del mismo tipo con longitud fija.
	let _g: [i32; 5] = [1, 2, 3, 4, 5];
	// Tuplas. Colecciones de elementos que pueden ser de distinto tipo.
	let _h: (i32, f64, char) = (-50, 3.1416927, '');

	// HOLA RUST:
	println!("¡Hola, Rust!");
}