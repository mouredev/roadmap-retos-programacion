#include <iostream>
#include <string>
#include <regex>

void regExpr(std::string cadena) {
    std::regex patron(R"-(-?\d+(\.\d+)?)-");
    std::smatch numeros;

    std::cout << "Números encontrados:" << std::endl;
    while (std::regex_search(cadena, numeros, patron)) {
        std::cout << numeros.str() << std::endl;
        cadena = numeros.suffix();
    }
    std::cout << std::endl;
}

void emailValidation(const std::string& email) {
    std::regex patron(R"-([a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4})-");
    if (std::regex_match(email, patron)) {
        std::cout << "El email " << email << " es válido." << std::endl;
    } else {
        std::cout << "El email " << email << " no es válido." << std::endl;
    }
}

void phoneValidation(const std::string& phone) {
    std::regex patron(R"-((\+?\d{2,3})?[-. ]?\d{9})-");
    if (std::regex_match(phone, patron)) {
        std::cout << "El teléfono " << phone << " es válido." << std::endl;
    } else {
        std::cout << "El teléfono " << phone << " no es válido." << std::endl;
    }
}

void urlValidation(const std::string& url) {
    std::regex patron(R"-((http|https):\/\/[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4})-");
    if (std::regex_match(url, patron)) {
        std::cout << "La URL " << url << " es válida." << std::endl;
    } else {
        std::cout << "La URL " << url << " no es válida." << std::endl;
    }
}

int main() {
    std::string texto = "Este es un texto con números como 123, 45.6, -7 y 1000.";
    std::cout << "Vamos a analizar el siguiente texto:" << std::endl;
    std::cout << "'" << texto << "'\n\n";
    regExpr(texto);

    texto = "123Erase una vez un número 1234567890 y otro 0987654321. Y para terminar456";
    std::cout << "Vamos a analizar el siguiente texto:" << std::endl;
    std::cout << "'" << texto << "'\n\n";
    regExpr(texto);

    emailValidation("correo@correo.com");
    emailValidation("correo@correo");

    phoneValidation("+34 123456789");
    phoneValidation("123456789");

    urlValidation("http://www.google.com");
    urlValidation("www.google.com");

    return 0;
}
