#include <iostream>
#include <string>
#include <vector>
#include <algorithm> 
#include <initializer_list>

/*
 * EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 */

// --- Declaraciones de funciones ---

void greet();
void greet_person(const std::string& name);
void add(int a, int b);
int multiply(int a, int b);
void greet_default(const std::string& name, const std::string& greeting = "Hola");
void print_args(std::initializer_list<const char*> args);
void outer_function();
void my_function_scope();
void modify_global();
int fizz_buzz_extra(const std::string& text1, const std::string& text2);

// --- Variable Global ---
std::string global_var = "Soy una variable global";

// --- Función Principal ---
int main() {
    std::cout << "===> Funciones básicas <===\n";

    greet();
    greet_person("Wilmer");
    add(5, 3);
    int result = multiply(5, 3);
    std::cout << "El resultado de la multiplicación es " << result << std::endl;
    
    greet_default("MoureDev");
    greet_default("Wilmer", "Hello");

    std::cout << "Argumentos variables (initializer_list):\n";
    print_args({"uno", "dos", "tres"});

    std::cout << "\n===> Funciones dentro de funciones (Lambdas) <===\n";
    outer_function();

    std::cout << "\n===> Funciones de la Librería Estándar (STL) <===\n";
    std::vector<int> my_list = {1, 2, 3, 4, 5};
    std::cout << "Usando el método size() de un vector: El vector tiene " << my_list.size() << " elementos." << std::endl;
    auto max_it = std::max_element(my_list.begin(), my_list.end());
    std::cout << "Usando std::max_element: El valor máximo es " << *max_it << std::endl;

    std::cout << "\n===> Variable LOCAL y GLOBAL <===\n";
    my_function_scope();
    
    std::cout << "Antes de modificar: " << global_var << std::endl;
    modify_global();
    std::cout << "Después de modificar: " << global_var << std::endl;

    std::cout << "\n====> DIFICULTAD EXTRA <====\n";
    int times_printed_number = fizz_buzz_extra("Fizz", "Buzz");
    std::cout << "\nEl número se imprimió un total de " << times_printed_number << " veces." << std::endl;

    return 0;
}

// --- Definiciones de funciones ---

void greet() {
    std::cout << "Hola, C++!\n";
}

void greet_person(const std::string& name) {
    std::cout << "Hola, " << name << "!\n";
}

void add(int a, int b) {
    std::cout << "La suma de " << a << " y " << b << " es " << a + b << std::endl;
}

int multiply(int a, int b) {
    return a * b;
}

void greet_default(const std::string& name, const std::string& greeting) {
    std::cout << greeting << ", " << name << "!\n";
}

void print_args(std::initializer_list<const char*> args) {
    for (const auto& arg : args) {
        std::cout << "- " << arg << "\n";
    }
}

void outer_function() {
    std::cout << "Esta es la función externa.\n";
    // C++ usa lambdas para funciones anónimas locales.
    auto inner_function = []() {
        std::cout << "Esta es una función lambda (interna).\n";
    };
    inner_function();
}

void my_function_scope() {
    std::string local_var = "Soy una variable local";
    std::cout << global_var << std::endl;
    std::cout << local_var << std::endl;
}

void modify_global() {
    global_var = "He modificado la variable global";
}

int fizz_buzz_extra(const std::string& text1, const std::string& text2) {
    int count = 0;
    for (int i = 1; i <= 100; ++i) {
        std::string output = "";
        if (i % 3 == 0) {
            output += text1;
        }
        if (i % 5 == 0) {
            output += text2;
        }
        if (!output.empty()) {
            std::cout << output << "\n";
        } else {
            std::cout << i << "\n";
            count++;
        }
    }
    return count;
}
