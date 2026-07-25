/*
 * EJERCICIO:
 * Utilizando tu lenguaje, explora el concepto de expresiones regulares,
 * creando una que sea capaz de encontrar y extraer todos los números
 * de un texto.
 * 
 * DIFICULTAD EXTRA (opcional):
 * Crea 3 expresiones regulares (a tu criterio) capaces de:
 * - Validar un email.
 * - Validar un número de teléfono.
 * - Validar una url.
 */
 

// Expresiones regulares en JavaScript
/*
Una expresión regular es una secuencia de caracteres que forma un patrón de búsqueda. Este patrón se puede usar para:

    * Buscar texto dentro de una cadena.
    * Validar si una cadena cumple con un formato específico (por ejemplo, un correo electrónico o un número de teléfono).
    * Reemplazar partes de una cadena.
    *Extraer información específica de un texto.
*/
// Creación de una expresión regular en JavaScript
/* 
    1. Usando el constructor RegExp
    Ejemplo:
    var regex = new RegExp('pattern');
    var regex = new RegExp('pattern', 'flags');
    var regex = new RegExp(/pattern/);
    var regex = new RegExp(/pattern/, 'flags');
*/
/* 
    2. Usando la notación literal
    Ejemplo:
    var regex = /pattern/;
    var regex = /pattern/flags;

    Donde:
    - pattern es el patrón de búsqueda.
    - flags son los modificadores que se pueden aplicar a la expresión regular.

    Las barras diagonales (/) se utilizan para delimitar la expresión regular, y los modificadores se colocan al final de la expresión regular.
    Pero las barras invertidas (\) se utilizan para escapar caracteres especiales dentro de la expresión regular.

    Ejemplo:
    var regex = /pattern\./;
    var regex = /pattern\./i;
*/

// Métodos de las expresiones regulares en JavaScript
/*
    - test(): Comprueba si una cadena cumple con el patrón de la expresión regular.
    - exec(): Devuelve la primera coincidencia de la expresión regular en una cadena.
    - match(): Devuelve un array con todas las coincidencias de la expresión regular en una cadena.
    - matchAll(): Devuelve un iterador con todas las coincidencias de la expresión regular en una cadena.
    - search(): Devuelve la posición de la primera coincidencia de la expresión regular en una cadena.
    - replace(): Reemplaza las coincidencias de la expresión regular en una cadena.
    - replaceAll(): Reemplaza todas las coincidencias de la expresión regular en una cadena.
    - split(): Divide una cadena en un array de subcadenas utilizando la expresión regular como separador.
    
*/
// las banderas o flags que se pueden utilizar en una expresión regular en JavaScript son:
/*
    - i: Realiza una búsqueda sin distinguir entre mayúsculas y minúsculas.
    - g: Realiza una búsqueda global en toda la cadena.
    - m: Realiza una búsqueda multilinea.
    - u: Habilita el modo Unicode.
    - y: Realiza una búsqueda pegajosa (sticky).
    - s: Habilita el modo dotall.
    - x: Ignora los espacios en blanco y permite comentarios en la expresión regular.
    - U: Deshabilita el modo Unicode.
    - A: Realiza una búsqueda en la cadena completa.
    - D: Realiza una búsqueda en la cadena completa, pero excluye el último carácter.
    - J: Realiza una búsqueda en la cadena completa, incluyendo el último carácter.
*/
// Caracteres especiales en las expresiones regulares en JavaScript

/*
    - \d: Representa cualquier dígito (0-9).
    - \D: Representa cualquier carácter que no sea un dígito.
    - \w: Representa cualquier carácter alfanumérico (incluyendo el guion bajo _).
    - \W: Representa cualquier carácter que no sea alfanumérico.
    - \s: Representa cualquier carácter de espacio en blanco.
    - \S: Representa cualquier carácter que no sea un espacio en blanco.
    - \b: Representa un límite de palabra.
    - \B: Representa un límite que no sea de palabra.
    - \n: Representa un salto de línea.
    - \t: Representa un tabulador.
    - \r: Representa un retorno de carro.
    - \f: Representa un salto de página.
    - \v: Representa un tabulador vertical.
    - \0: Representa el carácter nulo.
    - \xhh: Representa el carácter ASCII especificado por los dos dígitos hexadecimales hh.
    - \uhhhh: Representa el carácter Unicode especificado por los cuatro dígitos hexadecimales hhhh.
    - \cX: Representa un control ASCII, donde X es una letra en mayúscula.
    - \: Escapa un carácter especial.
    - .: Representa cualquier carácter, excepto un salto de línea.
    - ^: Representa el inicio de una cadena.
    - $: Representa el final de una cadena.
    - *: Representa cero o más repeticiones del elemento anterior.
    - +: Representa una o más repeticiones del elemento anterior.
    - ?: Representa cero o una repetición del elemento anterior.
    - {n}: Representa exactamente n repeticiones del elemento anterior.
    - {n,}: Representa n o más repeticiones del elemento anterior.
    - {n,m}: Representa entre n y m repeticiones del elemento anterior.
    - (x): Representa un grupo de captura.
    - [xyz]: Representa un conjunto de caracteres.
    - ` `: Representa un conjunto de caracteres que no están en el rango especificado.
*/

// Ejercicio: Encontrar y extraer todos los números de un texto en JavaScript
// Crear una expresión regular que encuentre y extraiga todos los números de un texto en JavaScript.

// Ejemplo:
var text = 'En el año 2021, el precio del producto es $25.50 y el descuento es del 10%.';
var regex = /\d+/g; // Expresión regular para encontrar números
var numbers = text.match(regex);
console.log(numbers);// Output: ['2021', '25', '50', '10']

// Explicación:
// - La expresión regular /\d+/g busca uno o más dígitos en el texto.
// - El modificador g se utiliza para realizar una búsqueda global en todo el texto.
// - El método match() devuelve un array con todas las coincidencias encontradas.

// Ejercicio extra: Validar un email, un número de teléfono y una URL en JavaScript
// Crear expresiones regulares que validen un email, un número de teléfono y una URL en JavaScript.

// Ejemplo:
var emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
var phoneRegex = /^\+\d{1,3}\s?\(\d{1,3}\)\s?\d{3}-\d{4}$/;
var urlRegex = /^(https?:\/\/)?(www\.)?[a-zA-Z0-9-]+\.[a-zA-Z]{2,}\/?$/;

var email = 'peito_qwq12.12@gmail.com';
var phone = '+57 (32) 353-7890';
var url = 'https://www.example.com';

console.log(emailRegex.test(email)); // Output: true    
console.log(phoneRegex.test(phone)); // Output: true
console.log(urlRegex.test(url)); // Output: true

// Explicación:
// - La expresión regular /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/ valida un email.
// - La expresión regular /^\+\d{1,3}\s?\(\d{1,3}\)\s?\d{3}-\d{4}$/ valida un número de teléfono.
// - La expresión regular /^(https?:\/\/)?(www\.)?[a-zA-Z0-9-]+\.[a-zA-Z]{2,}\/?$/ valida una URL.


