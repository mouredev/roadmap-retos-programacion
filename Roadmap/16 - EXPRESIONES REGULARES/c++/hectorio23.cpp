// Author: Hector Adán
// GitHub: https://github.com/hectorio23 
#include <iostream>
#include <regex>
#include <string>

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

/*************************************************
**************  Prototipo de funcion *************
*************************************************/
std::string verify(std::string, std::string, std::regex);
std::string extract(std::string);


 int main() {
    /*************************************************
    *******************  REGEX ZONE ******************
    *************************************************/
    std::regex email_regex (R"(^\w+@\w{3,}\.\w{2,})");
    std::regex phone_number_regex (R"(^\+\d{2,3}\s\d{3}\s\d{3}\s\d{2}\s\d{2})");
    std::regex url_regex ("^https?://w{0,3}?[a-z]+\\.[a-z]{3}");

    std::string texto_legible = "E5n e6l si5g7ui8e956nte tex8to s9e 0t4ien4e que3 extr3aer to3dos lo0s nume3ro0s pa2ra q4ue s8e7a l9e0gi9b0le";

    // IMPRESION DEL LA SALIDA DEL EJERCICIO 1
    std::cout << "***** EJERCICIO *****\n";
    std::cout << "[-] Cadena a extraer los numeros: " << texto_legible << "\n";
    std::cout << "[+] Cadena limpia sin numeros: " << extract(texto_legible) << "\n\n";


    // IMPRESION DEL LA SALIDA DEL EXTRA 1
    std::cout << "********* EJERCICIO EXTRA *********\n";
    std::cout << "*********************** EMAIL CHECK *********************************\n";
    std::cout << verify("hectorino2789@gmail.com", "e-mail", email_regex) << "\n";
    std::cout << verify("quesobadas@outlook.es", "e-mail", email_regex) << "\n";
    std::cout << verify("nocorresponde a unema%il@gmaildjfj.completo", "e-mail", email_regex) << "\n";


    std::cout << "\n*********************** PHONE CHECK *********************************\n";
    std::cout << "Para que un numero sea valido, tiene que estar escrito de la siguiente forma: +52 449 369 52 34\n";
    std::cout << verify("+52 449-369-52-34", "numero de telefono", phone_number_regex) << "\n";
    std::cout << verify("+52 449 369 52 34", "numero de telefono", phone_number_regex) << "\n";
    std::cout << verify("449 369 52 34", "numero de telefono", phone_number_regex) << "\n";


    std::cout << "\n*********************** URL CHECK *********************************\n";
    std::cout << verify("https://github.com/hectorio23", "url", url_regex) << "\n";
    std::cout << verify("outlook:///github.com\\hectorio23", "url", url_regex) << "\n";
    std::cout << verify("127.0.0.1:89/path/otherpath", "url", url_regex) << "\n";
    std::cout << verify("https://apple.com", "url", url_regex) << "\n";


    return EXIT_SUCCESS;
}

// LA funcion verify solo compara la cadena de caracteres previamente especificada en el 
// parametro sValue con el pattern.
std::string verify(std::string sValue, std::string tipo, std::regex pattern) {

    if (!std::regex_search(sValue, pattern)) return "[-] El valor [ " +  sValue  + " ] no corresponde a un  " + tipo;

    return "[+] El valor [ " +  sValue  + " ] corresponde a un  " + tipo;
}
// Esta funcion extrae los numeros de una cadena de caracteres
// y retorna la misma cadena sin los numeros.
std::string extract(std::string sValue) {
    std::regex pattern("\\d");

    return std::regex_replace(sValue, pattern, "");
 }

// OUTPUT
//  ***** EJERCICIO *****
// [-] Cadena a extraer los numeros: E5n e6l si5g7ui8e956nte tex8to s9e 0t4ien4e que3 extr3aer to3dos lo0s nume3ro0s pa2ra q4ue s8e7a l9e0gi9b0le
// [+] Cadena limpia sin numeros: En el siguiente texto se tiene que extraer todos los numeros para que sea legible

// ********* EJERCICIO EXTRA *********
// *********************** EMAIL CHECK *********************************
// [+] El valor [ hectorino2789@gmail.com ] corresponde a un  e-mail
// [+] El valor [ quesobadas@outlook.es ] corresponde a un  e-mail
// [-] El valor [ nocorresponde a unema%il@gmaildjfj.completo ] no corresponde a un  e-mail

// *********************** PHONE CHECK *********************************
// Para que un numero sea valido, tiene que estar escrito de la siguiente forma: +52 449 369 52 34
// [-] El valor [ +52 449-369-52-34 ] no corresponde a un  numero de telefono
// [+] El valor [ +52 449 369 52 34 ] corresponde a un  numero de telefono
// [-] El valor [ 449 369 52 34 ] no corresponde a un  numero de telefono

// *********************** URL CHECK *********************************
// [+] El valor [ https://github.com/hectorio23 ] corresponde a un  url
// [-] El valor [ outlook:///github.com\hectorio23 ] no corresponde a un  url
// [-] El valor [ 127.0.0.1:89/path/otherpath ] no corresponde a un  url
// [+] El valor [ https://apple.com ] corresponde a un  url