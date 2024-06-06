// ##########################################################################
// ##################### Librerias requeridas ###############################
// ##########################################################################
#include <algorithm>
#include <iostream>
#include <string>

/*
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
 *   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
 */

// Declaracion de la funcion la cual retornara una caadena de carateres 
// distinra en caso de ser polidromo, anagrama o isograma respectivamente
std::string  discoverType(std::string&, std::string&);
bool anagrama(std::string, std::string);
bool isograma(std::string);


int main() {
    // Las siguientes variables almacenan las palabras
    //insertadas por el usuario 
    std::string value1, value2;

    std::cout << "Inserta la primera palabra: ";
    std::cin >> value1;

    std::cout <<  "Ahora inserta la segunda palabra: ";
    std::cin >> value2;


    std::string cadena1 = "Hola";
    std::string cadena2 = "Mundo";

    // Modifican la variable original transformando sus caracteres en minusculas
    transform(value1.begin(), value1.end(), value1.begin(), ::tolower);
    transform(value2.begin(), value2.end(), value2.begin(), ::tolower);


    // Se llama a la función discoverType, la cual devuelve una cadena dependiendo de 
    // si las palabras ingresadas por el usuario forman parte de un palíndromo, anagrama o isograma.
    // Para lograr esto, se invocan otras funciones cuyo único propósito es verificar 
    // si las palabras cumplen con las especificaciones dadas.
    std::cout << discoverType(value1, value2);

    // Concatenación de dos cadenas
    std::string concatenacion = cadena1 + " " + cadena2;
    std::cout << "Concatenación: " << concatenacion << "\n";

    // Se elimina cualquier espacio de la cadena de caracteres
    std::string cadenaPrueba = concatenacion;
    cadenaPrueba.erase(std::remove_if(cadenaPrueba.begin(), cadenaPrueba.end(), ::isspace), cadenaPrueba.end());
    std::cout << "Cadena sin espacios en blanco " << cadenaPrueba << "\n";

    // Obtencion de la longitud de dos cadenas
    std::cout << "Longitud de la cadena 1: " << cadena1.length() << "\n";
    std::cout << "Longitud de la cadena 2: " << cadena2.size() << "\n";

    // Acceso a caracteres individuales
    std::cout << "Primer caracter de la cadena 1: " << cadena1[0] << "\n";
    std::cout << "Último caracter de la cadena 2: " << cadena2.back() << "\n";

    // Comparación
    if (cadena1 == cadena2) {
        std::cout << "Las cadenas son iguales" << "\n";
    } else {
        std::cout << "Las cadenas son diferentes" << "\n";
    }

    // Subcadena H o l a   M u n d o
    //           1 2 3 4 5 6 7 8 9 
    std::string subcadena = concatenacion.substr(5, 9); // Extrae "Mundo"
    std::cout << "Subcadena: " << subcadena << "\n";

    // Búsqueda 
    std::string buscar = "Mundo";
    size_t posicion = concatenacion.find(buscar);
    if (posicion != std::string::npos) {
        std::cout << "La cadena '" << buscar << "' fue encontrada en la posición " << posicion << "\n";
    } else {
        std::cout << "La cadena '" << buscar << "' no fue encontrada" << "\n";
    }

    // Modificación
    concatenacion.replace(5, 10, "Universo");
    std::cout << "Después de reemplazar 'Mundo' por 'Universo': " << concatenacion << "\n";

    return 0;
}


// ##########################################################################
// ##################### ZONA DE FUNCIONES ##################################
// ##########################################################################


// Esta es la funcion encargada de realizar el 
// ejercicio extra
std::string  discoverType(std::string& value1, std::string& value2) {
    
    // Se guarda una variable local la cual sera modificada
    // para posteriormente ser comparada con la segunda palabra.
    // Se puede observar que se ordena de manera contraria <reverse> 
    std::string valueReverse  = value1;
    reverse(valueReverse.begin(), valueReverse.end());

    if (valueReverse == (value2)) return "\nLas palabras anteriormente insertadas forman en realidad son un polidromo\n\n";
    else if (isograma(value1) && isograma(value2)) return "\nAmbas palabras son isogramas\n\n";
    else if (isograma(value1) || isograma(value2)) return "\nUna de las palabras es un isograma\n\n";
    else if (anagrama(value1, value2)) return "\nEs un anagrama\n\n";

    return "\nLas palabras proporcionadas no cumplen con las condiciones para ser un polidromo, isograma, anagrama\n";
}

// Funcion que comprueba que la palabra dada sea un isograma
// comprueba que las letras sean unicas dentro de la cadena
// de caracteres, en caso de encontrarse alguna coincidencia
// inmediatamente saldra de la funcion retornando un valor booleano
// falso y no seguira mas con la comprobacion,
bool isograma(std::string palabra) {
    std::string _tmp_ = "";

    for (auto item: palabra) {

        for (auto element: _tmp_)  if (item == element) return false;

        _tmp_ += item;
    }

    return true;
}

// Comprueaba que realmente las palabras dadas sean anagramas.
// Primero comprueba que las palabras tengan la misma longitud
// Segundo ordena de manera alfabetica las palabras dadas, ejemplo: cerebro -> bceeorr
// Lo hace con ambas palabras, finalmente, en caso de ser un anagrama, lel
// producto resultante sera dos palabras identicas
bool anagrama(std::string palabra1, std::string palabra2) {

    sort(palabra1.begin(), palabra1.end());
    sort(palabra2.begin(), palabra2.end());

    if (palabra1.length() != palabra2.length() || palabra1 != palabra2) return false;
    return true;
}