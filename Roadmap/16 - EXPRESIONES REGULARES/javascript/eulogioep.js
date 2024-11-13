// Ejercicio de Expresiones Regulares en JavaScript

// Texto de ejemplo para probar todas las expresiones regulares
const textoEjemplo = `Hola, tengo 25 años y mi número de teléfono es 123-456-789. 
También puedes contactarme al +34 611 222 333 o por email a usuario@dominio.com. 
Visita mi página web en https://www.ejemplo.com para más información. 
Hay 42 razones para usar expresiones regulares y 100 formas de aplicarlas.`;

/**
 * 1. Función para encontrar y extraer todos los números de un texto
 * Utiliza la expresión regular \b\d+\b que significa:
 * \b  - límite de palabra
 * \d+ - uno o más dígitos
 * \b  - otro límite de palabra
 */
function extraerNumeros(texto) {
    const patron = /\b\d+\b/g;
    const numerosEncontrados = texto.match(patron);
    
    console.log('1. Números encontrados:');
    numerosEncontrados.forEach(numero => console.log(numero));
}

/**
 * 2. Función para validar un email
 * Utiliza una expresión regular que verifica:
 * ^             - inicio de la cadena
 * [\w.-]+       - uno o más caracteres de palabra, puntos o guiones
 * @             - símbolo @
 * [\w-]+        - uno o más caracteres de palabra o guiones
 * \.            - un punto literal
 * [\w-]+        - dominio de nivel superior
 * (\.[a-zA-Z]{2,})?$ - opcional: punto seguido de 2 o más letras, fin de cadena
 */
function validarEmail(email) {
    const patronEmail = /^[\w.-]+@[\w-]+\.[\w-]+(\.[a-zA-Z]{2,})?$/;
    return patronEmail.test(email);
}

/**
 * 3. Función para validar un número de teléfono
 * Acepta formatos:
 * - 123-456-789
 * - +34 611 222 333
 */
function validarTelefono(telefono) {
    const patronTelefono = /^(\+\d{1,3}\s?)?(\d{3}[-\s]?){2}\d{3}$/;
    return patronTelefono.test(telefono);
}

/**
 * 4. Función para validar una URL
 * Acepta URLs que:
 * - Comienzan con http:// o https://
 * - Pueden tener www. (opcional)
 * - Tienen un dominio y una extensión válida
 */
function validarURL(url) {
    const patronURL = /^(https?:\/\/)(www\.)?[\w-]+(\.[a-zA-Z]{2,})+$/;
    return patronURL.test(url);
}

// Pruebas
console.log('\n=== PRUEBAS DE EXPRESIONES REGULARES ===');

// 1. Extraer números
extraerNumeros(textoEjemplo);

// 2. Validar emails
console.log('\n2. Validación de emails:');
const emails = ['usuario@dominio.com', 'email_invalido.com', 'test@test.co.uk'];
emails.forEach(email => {
    console.log(`${email} es válido:`, validarEmail(email));
});

// 3. Validar números de teléfono
console.log('\n3. Validación de números de teléfono:');
const telefonos = ['123-456-789', '+34 611 222 333', '1234', '999-999-999'];
telefonos.forEach(telefono => {
    console.log(`${telefono} es válido:`, validarTelefono(telefono));
});

// 4. Validar URLs
console.log('\n4. Validación de URLs:');
const urls = ['https://www.ejemplo.com', 'http://ejemplo', 'https://dominio.es'];
urls.forEach(url => {
    console.log(`${url} es válida:`, validarURL(url));
});