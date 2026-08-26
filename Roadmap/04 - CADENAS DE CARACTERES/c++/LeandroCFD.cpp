#include <iostream>
#include <string>
#include <cctype>
#include <algorithm>

int main() {

    std::string cadena1 = "Hola"; // Declaración e inicialización de la primera cadena
    std::string cadena2 = "Mundo"; // Declaración e inicialización de la segunda cadena

    std::cout << "Cadena 1: " << cadena1 << std::endl;
    std::cout << "Cadena 2: " << cadena2 << std::endl;

    // Acceso a caracteres individuales
    cadena1.operator[](0) = 'h'; // Cambia el primer carácter de cadena1 a 'h'
    cadena2[0] = 'm'; // Cambia el primer carácter de cadena2 a 'm'

    // Subcadenas
    std::string subcadena1 = cadena1.substr(0, 2); // Obtiene los primeros 2 caracteres de cadena1
    std::cout << "Subcadena 1: " << subcadena1 << std::endl;
    std::string subcadena2 = cadena2.substr(1, 3); // Obtiene los 3 caracteres a partir del segundo carácter de cadena2
    std::cout << "Subcadena 2: " << subcadena2 << std::endl;

    // Longitud de cadenas
    std::cout << "Longitud de cadena1: " << cadena1.length() << std::endl;

    // Concatenación de cadenas
    std::string concatenacion = cadena1 + " " + cadena2;
    std::cout << "Concatenacion: " << concatenacion << std::endl;

    // Reemplazo de subcadenas
    std::string reemplazo = cadena1.replace(0, 2, "Adios"); // Reemplaza los primeros 2 caracteres de cadena1 por "Adiós"
    std::cout << "Reemplazo: " << reemplazo << std::endl;

    // Conversión de cadenas a mayúsculas y minúsculas
    std::transform(cadena1.begin(), cadena1.end(), cadena1.begin(), ::toupper); // Convierte cadena1 a mayúsculas
    std::cout << "Cadena 1 en mayusculas: " << cadena1 << std::endl;
    std::transform(cadena2.begin(), cadena2.end(), cadena2.begin(), ::tolower); // Convierte cadena2 a minúsculas
    std::cout << "Cadena 2 en minusculas: " << cadena2 << std::endl;


    // Dificultad extra
    std::string palabra1, palabra2; // Declaración de dos cadenas dadas por el usuario
    std::cout << "Ingrese la primera palabra: ";
    std::cin >> palabra1; // Entrada de la primera palabra
    std::cout << "Ingrese la segunda palabra: ";
    std::cin >> palabra2; // Entrada de la segunda palabra

    std::string palabra1_minus = palabra1; // Crea una copia de palabra1 para convertirla a minúsculas
    std::string palabra2_minus = palabra2; // Crea una copia de palabra2 para convertirla a minúsculas
    std::transform(palabra1_minus.begin(), palabra1_minus.end(), palabra1_minus.begin(), ::tolower);
    std::transform(palabra2_minus.begin(), palabra2_minus.end(), palabra2_minus.begin(), ::tolower);

    int i = 0; // Inicialización del índice para iterar sobre los caracteres

    for (auto it = palabra1_minus.end() - 1; it >= palabra1_minus.begin(); --it) { // Itera desde el último carácter hasta el primero de palabra1
        if (*it != palabra1_minus[i] ){
            std::cout << "La palabra " << palabra1 << " NO es palindroma." << std::endl; // Si algún carácter no coincide, la palabra no es palíndroma
            break;  
        }
        i++;
    }

    if (i == palabra1.length()) { // Si todos los caracteres coinciden, la palabra es palíndroma
        std::cout << "La palabra " << palabra1 << " es palindroma." << std::endl;
    }

    i = 0; // Reinicia el índice para la verificación de la segunda palabra

    for (auto it = palabra2_minus.end() - 1; it >= palabra2_minus.begin(); --it) { // Itera desde el último carácter hasta el primero de palabra2
        if (*it != palabra2_minus[i] ){
            std::cout << "La palabra " << palabra2 << " NO es palindroma." << std::endl; // Si algún carácter no coincide, la palabra no es palíndroma
            break;  
        }
        i++;
    }

    if (i == palabra2.length()) { // Si todos los caracteres coinciden, la palabra es palíndroma
        std::cout << "La palabra " << palabra2 << " es palindroma." << std::endl;
    }

    if (palabra1.length() != palabra2.length()) { // Si las longitudes de las palabras son diferentes, no son anagramas
        std::cout << "Las palabras " << palabra1 << " y " << palabra2 << " NO son anagramas." << std::endl;
    } else {
        std::string sorted_palabra1 = palabra1_minus; // Crea una copia de palabra1 para ordenar
        std::string sorted_palabra2 = palabra2_minus; // Crea una copia de palabra2 para ordenar

        std::sort(sorted_palabra1.begin(), sorted_palabra1.end()); // Ordena los caracteres de la primera palabra
        std::sort(sorted_palabra2.begin(), sorted_palabra2.end()); // Ordena los caracteres de la segunda palabra

        if (sorted_palabra1 == sorted_palabra2) { // Compara las palabras ordenadas
            std::cout << "Las palabras " << palabra1 << " y " << palabra2 << " son anagramas." << std::endl;
        } else {
            std::cout << "Las palabras " << palabra1 << " y " << palabra2 << " NO son anagramas." << std::endl;
        }
    }

    i = 1; // Reinicia el índice para la verificación de isogramas

    for (auto it = palabra1_minus.begin(); it !=palabra1_minus.end(); ++it){
        if (*it == palabra1_minus[i]) { // Si el carácter se encuentra en la palabra
            std::cout << "la palabra " << palabra1 << " NO es un Isograma." << std::endl;
            break;
        }
        i++;
    }

    if (i == palabra1.length() + 1) { // Si todos los caracteres son únicos, la palabra es un isograma
        std::cout << "la palabra " << palabra1 << " es un Isograma." << std::endl;
    }

    i = 1; // Reinicia el índice para la verificación de isogramas en la segunda palabra

    for (auto it = palabra2_minus.begin(); it !=palabra2_minus.end(); ++it){
        if (*it == palabra2_minus[i]) { // Si el carácter se encuentra en la palabra
            std::cout << "la palabra " << palabra2 << " NO es un Isograma." << std::endl;
            break;
        }
        i++;
    }

    if (i == palabra2.length() + 1) { // Si todos los caracteres son únicos, la palabra es un isograma
        std::cout << "la palabra " << palabra2 << " es un Isograma." << std::endl;
    }

    return 0;
}