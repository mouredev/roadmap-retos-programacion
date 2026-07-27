// EJERCICIO 04 - CADENAS DE CARACTERES
// Autor: TTATTIN

#include <iostream>
#include <string>
#include <algorithm>
#include <sstream>
#include <format>

//FUNCIONES PRIMERA PARTE DEL EJERCICIO

void recorrido_y_acceso_a_caracteres(const std::string& cadena) {
    std::cout << "Recorrido y acceso a caracteres:" << std::endl;
    for (size_t i = 0; i < cadena.size(); i++) {
        std::cout << cadena[i] << std::endl;
    }
    std::cout << std::endl;
}

void subcadena(const std::string& cadena) {
    std::cout << "Subcadena: recorte de una parte intermedia de la cadena:" << std::endl;
    std::string subcadena = cadena.substr(3, 7);
    std::cout << subcadena << std::endl << std::endl;
}

void longitud_de_cadena(const std::string& cadena1, const std::string& cadena2) {
    std::cout << "Longitud de cadenas:" << std::endl;
    std::cout << "Cadena 1: " << cadena1.size() << std::endl;
    std::cout << "Cadena 2: " << cadena2.size() << std::endl;
    std::cout << std::endl;
}

void concatenacion(const std::string& cadena1, const std::string& cadena2) {
    std::cout << "Concatenacion de cadenas:" << std::endl;
    std::string cadena_concatenada = cadena1 + cadena2;
    std::cout << cadena_concatenada << std::endl << std::endl;
}

void conversion_a_mayusculas(std::string& cadena) {
    std::cout << "Conversion a mayusculas:" << std::endl;
    std::transform(cadena.begin(), cadena.end(), cadena.begin(), ::toupper);
    std::cout << cadena << std::endl << std::endl;
}

void conversion_a_minusculas(std::string& cadena) {
    std::cout << "Conversion a minusculas:" << std::endl;
    std::transform(cadena.begin(), cadena.end(), cadena.begin(), ::tolower);
    std::cout << cadena << std::endl << std::endl;
}

void reemplazo(std::string& cadena) {
    std::cout << "Reemplazo de caracteres:" << std::endl;
    cadena.replace(0, 4, "Adios");
    std::cout << cadena << std::endl << std::endl;
}

void division(std::string& cadena) {
    std::cout << "Division de cadenas:" << std::endl;
    std::stringstream ss(cadena);
    std::string palabra;
    while (std::getline(ss, palabra, ' ')) {
        std::cout << palabra << std::endl;
    }
    std::cout << std::endl;
}

void union_de_cadenas(const std::string& cadena1, const std::string& cadena2) {
    std::cout << "Union de cadenas:" << std::endl;
    std::string cadena_unida = cadena1 + " " + cadena2;
    std::cout << cadena_unida << std::endl << std::endl;
}

void interpolacion(const std::string& cadena1, const std::string& cadena2) {
    std::cout << "Interpolacion de cadenas:" << std::endl;
    std::string cadena_interpolata = std::format("{} {} {}", cadena1, cadena2, cadena1);
    std::cout << cadena_interpolata << std::endl << std::endl;
}

void eliminacion_selectiva_de_caracteres(std::string& cadena) {
    std::cout << "Eliminacion selectiva de caracteres:" << std::endl;
    cadena.erase(7, 3);
    std::cout << cadena << std::endl << std::endl;
}

void repeticion(const std::string& cadena) {
    std::cout << "Repeticion de cadenas:" << std::endl;
    for (int i = 0; i<5; i++) {
        std::cout << cadena << " ";
    }
    std::cout << std::endl << std::endl;
}

void verificacion_de_cadena(const std::string& cadena) {
    std::cout << "Verificacion de cadenas:" << std::endl;
    if (!cadena.empty()) {
        std::cout << "La cadena no esta vacia" << std::endl;
    }
    if (cadena.find("mundo") != std::string::npos) {
        std::cout << "La cadena contiene la palabra 'mundo'" << std::endl;
    }
    std::cout << std::endl << std::endl;
}

//FUNCIONES DIFICULTAD EXTRA

void verificacion_de_palindromo(const std::string& palabra_palindroma, const std::string& palabra_anagrama1) {
    std::cout << "Verificacion de palindromo:" << std::endl;
    std::string palabra_inversa = palabra_palindroma;
    std::reverse(palabra_inversa.begin(), palabra_inversa.end());
    if (palabra_palindroma == palabra_inversa) {
        std::cout << "La palabra " << palabra_palindroma << " es un palindromo." << std::endl;
    }
    else {
        std::cout << "La palabra " << palabra_palindroma << " no es un palindromo." << std::endl;
    }

    palabra_inversa = palabra_anagrama1;
    std::reverse(palabra_inversa.begin(), palabra_inversa.end());
    if (palabra_anagrama1 == palabra_inversa) {
        std::cout << "La palabra " << palabra_anagrama1 << " es un palindromo." << std::endl;
    }
    else {
        std::cout << "La palabra " << palabra_anagrama1 << " no es palindromo." << std::endl;
    }
    std::cout << std::endl;
}

void verificacion_de_anagrama(const std::string& palabra_anagrama1, const std::string& palabra_anagrama2, const std::string& palabra_isograma) {
    std::cout << "Verificacion de anagrama:" << std::endl;
    std::string s1 = palabra_anagrama1;
    std::string s2 = palabra_anagrama2;
    std::string s3 = palabra_isograma;

    std::sort(s1.begin(), s1.end());
    std::sort(s2.begin(), s2.end());
    std::sort(s3.begin(), s3.end());

    if (s1 == s2) {
        std::cout << "Las palabras " << palabra_anagrama1 << " y " << palabra_anagrama2 << " son anagramas." << std::endl;
    } else {
        std::cout << "Las palabras " << palabra_anagrama1 << " y " << palabra_anagrama2 << " no son anagramas." << std::endl;
    }

    if (s1 == s3) {
        std::cout << "Las palabras " << palabra_anagrama1 << " y " << palabra_isograma << " son anagramas." << std::endl;
    } else {
        std::cout << "Las palabras " << palabra_anagrama1 << " y " << palabra_isograma << " no son anagramas." << std::endl;
    }

    std::cout << std::endl;
}

void verificacion_de_isograma(const std::string& palabra) {
    std::cout << "Verificacion de isograma:" << std::endl;
    std::string s1 = palabra;
    std::sort(s1.begin(), s1.end());

    for (size_t i = 1; i < s1.size(); i++) {
        if (s1[i] == s1[i-1]) {
            std::cout << "La palabra " << palabra << " no es un isograma." << std::endl;
            return;
        }
    }
    std::cout << "La palabra " << palabra << " es un isograma." << std::endl;

}

int main() {
    std::string cadena1 = "Hola Mundo";
    std::string cadena2 = "Cadena de prueba";

    recorrido_y_acceso_a_caracteres(cadena1);
    subcadena(cadena2);
    longitud_de_cadena(cadena1, cadena2);
    concatenacion(cadena1, cadena2);
    conversion_a_mayusculas(cadena1);
    conversion_a_minusculas(cadena1);
    reemplazo(cadena1);
    division(cadena2);
    union_de_cadenas(cadena1, cadena2);
    interpolacion(cadena1, cadena2);
    eliminacion_selectiva_de_caracteres(cadena2);
    repeticion(cadena1);
    verificacion_de_cadena(cadena1);

    std::cout << "--------------------------------------" << std::endl;
    std::cout << "---------- DIFICULTAD EXTRA ----------" << std::endl;
    std::cout << "--------------------------------------" << std::endl;
    std::cout << std::endl;

    std::string palabra_palindroma = "radar";
    std::string palabra_anagrama1 = "roma";
    std::string palabra_anagrama2 = "mora";
    std::string palabra_isograma = "retazo";

    verificacion_de_palindromo(palabra_palindroma, palabra_anagrama1);
    verificacion_de_anagrama(palabra_anagrama1, palabra_anagrama2, palabra_isograma);
    verificacion_de_isograma(palabra_isograma);
    verificacion_de_isograma(palabra_palindroma);

    std::cout << std::endl << std::endl;

    return 0;
}