<?php
/**
 * Ejercicio de Expresiones Regulares en PHP
 * 
 * Este script demuestra el uso de expresiones regulares en PHP para:
 * 1. Extraer números de un texto
 * 2. Validar direcciones de email
 * 3. Validar números de teléfono
 * 4. Validar URLs
 */

// Texto de ejemplo para probar las expresiones regulares
$textoEjemplo = "Hola, tengo 25 años y mi número es 123-456-789. " .
                "Puedes contactarme al +34 611 222 333 o por email a usuario@dominio.com. " .
                "Visita mi web https://www.ejemplo.com para más información. " .
                "Hay 42 razones para usar expresiones regulares y 100 formas de aplicarlas.";

/**
 * 1. Función para encontrar y extraer todos los números de un texto
 * 
 * La expresión regular \b\d+\b significa:
 * \b  - límite de palabra
 * \d+ - uno o más dígitos
 * \b  - otro límite de palabra
 * 
 * @param string $texto El texto del que extraer los números
 * @return array Array con todos los números encontrados
 */
function extraerNumeros($texto) {
    $patron = '/\b\d+\b/';
    preg_match_all($patron, $texto, $coincidencias);
    return $coincidencias[0];
}

/**
 * 2. Función para validar un email
 * 
 * La expresión regular verifica:
 * ^ - inicio de la cadena
 * [\w\.-]+ - uno o más caracteres de palabra, puntos o guiones
 * @ - símbolo @
 * [\w\.-]+ - uno o más caracteres de palabra, puntos o guiones
 * \. - un punto literal
 * [\w\.-]+ - dominio de nivel superior
 * $ - fin de la cadena
 * 
 * @param string $email El email a validar
 * @return bool true si el email es válido, false si no
 */
function validarEmail($email) {
    $patron = '/^[\w\.-]+@[\w\.-]+\.\w+$/';
    return preg_match($patron, $email) === 1;
}

/**
 * 3. Función para validar un número de teléfono
 * 
 * Acepta formatos:
 * - 123-456-789
 * - +34 611 222 333
 * 
 * @param string $telefono El número de teléfono a validar
 * @return bool true si el teléfono es válido, false si no
 */
function validarTelefono($telefono) {
    $patron = '/^(\+\d{1,3}\s?)?(\d{3}[-\s]?){2}\d{3}$/';
    return preg_match($patron, $telefono) === 1;
}

/**
 * 4. Función para validar una URL
 * 
 * Verifica URLs que:
 * - Comienzan con http:// o https://
 * - Pueden tener www. (opcional)
 * - Tienen un dominio y una extensión válida
 * 
 * @param string $url La URL a validar
 * @return bool true si la URL es válida, false si no
 */
function validarURL($url) {
    $patron = '/^https?:\/\/(www\.)?[\w\.-]+\.\w{2,}$/';
    return preg_match($patron, $url) === 1;
}

// PRUEBAS

echo "=== PRUEBAS DE EXPRESIONES REGULARES ===\n\n";

// 1. Extraer números
echo "1. Números encontrados:\n";
$numeros = extraerNumeros($textoEjemplo);
foreach ($numeros as $numero) {
    echo "- $numero\n";
}

// 2. Validar emails
echo "\n2. Validación de emails:\n";
$emails = ['usuario@dominio.com', 'email_invalido.com', 'test@test.co.uk'];
foreach ($emails as $email) {
    $esValido = validarEmail($email) ? 'válido' : 'inválido';
    echo "- $email es $esValido\n";
}

// 3. Validar números de teléfono
echo "\n3. Validación de números de teléfono:\n";
$telefonos = ['123-456-789', '+34 611 222 333', '1234', '999-999-999'];
foreach ($telefonos as $telefono) {
    $esValido = validarTelefono($telefono) ? 'válido' : 'inválido';
    echo "- $telefono es $esValido\n";
}

// 4. Validar URLs
echo "\n4. Validación de URLs:\n";
$urls = ['https://www.ejemplo.com', 'http://ejemplo', 'https://dominio.es'];
foreach ($urls as $url) {
    $esValido = validarURL($url) ? 'válida' : 'inválida';
    echo "- $url es $esValido\n";
}

?>