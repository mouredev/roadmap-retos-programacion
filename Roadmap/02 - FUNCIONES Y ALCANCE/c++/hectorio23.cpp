#include <iostream>
#include <string>

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

// Ejemplo de función sin parámetros ni retorno
void saludar() {
    std::cout << "¡Hola, mundo!" << std::endl;
}

// Ejemplo de función con parámetros y retorno
int suma(int a, int b) {
    return a + b;
}

// Ejemplo de función con función anidada
std::pair<int, int> operaciones(int a, int b) {
    // Función lambda anidada
    auto multiplicar = [&]() {
        return a * b;
    };

    int resultado_multiplicacion = multiplicar();
    int resultado_suma = suma(a, b);

    return std::make_pair(resultado_multiplicacion, resultado_suma);
}

// Variable global
int variable_global = 10;

// Ejemplo de función que utiliza variable global
void usar_variable_global() {
    variable_global += 5;
}

int  ejercicioExtra(std::string, std::string); 

int main() {

    int resultado_suma = suma(3, 7);
    std::cout << "Resultado de la suma: " << resultado_suma << std::endl;

    auto resultado_operaciones = operaciones(2, 4);
    std::cout << "Resultado de la multiplicación y suma: " << resultado_operaciones.first << ", " << resultado_operaciones.second << std::endl;

    std::cout << "Valor inicial de la variable global: " << variable_global << std::endl;
    usar_variable_global();
    std::cout << "Valor de la variable global después de usar_variable_global: " << variable_global << std::endl;


    int data = ejercicioExtra("Hola", "Mundo");
    std::cout << "Se imprimio un numero que no cumple con las condiciones: " << data << " veces\n";
    return 0;
}

// funcion  que cumple con el ejercicio extra
int  ejercicioExtra(std::string cadenaTexto1, std::string cadenaTexto2) {
    // El siguiente contador almacenara las veces que se imprimira en terminal
    // el numero que no cumpla con las condiciones
    int counter = 0;

    // El siguente codigo hace todo el trabajo
    for (int i = 1; i <= 100; i++) {
        if (i % 5 == 0 && i % 3 == 0) std::cout << i << " => " << cadenaTexto1 << " " << cadenaTexto2 << "\n";
        else if (i % 3 == 0) std::cout << i << " => "<< cadenaTexto1 << "\n";
        else if (i % 5 == 0) std::cout << i << " => "<< cadenaTexto2 << "\n";
        else {
            std::cout << i << "\n";
            counter++;
        }
    }

    return counter;
}