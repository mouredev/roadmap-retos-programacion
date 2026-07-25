/*
# #02 FUNCIONES Y ALCANCE
> #### Dificultad: Fácil | Publicación: 08/01/24 | Corrección: 15/01/24

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

 #include <iostream>
#include <string>
using namespace std;

// Variables globales
int globalVar = 10;

// Función sin parámetros ni retorno
void saludar() {
    cout << "Hola, esta es una función sin parámetros ni retorno." << endl;
}

// Función con parámetros pero sin retorno
void mostrarSuma(int a, int b) {
    cout << "La suma de " << a << " y " << b << " es: " << a + b << endl;
}

// Función con retorno
int multiplicar(int a, int b) {
    return a * b;
}

// Prueba de variable local y global
void modificarVariables() {
    int localVar = 5;
    cout << "Variable local: " << localVar << endl;
    cout << "Variable global: " << globalVar << endl;
    globalVar = 20; // Modificamos la variable global
}

// Función que imprime todos los números del 1 al 100 siguiendo las reglas descritas
int imprimirMultiples(string cadena1, string cadena2) {
    int contadorNumeros = 0;
    for (int i = 1; i <= 100; i++) {
        if (i % 3 == 0 && i % 5 == 0) {         // Si el número es múltiplo de 3 y de 5
            cout << cadena1 + cadena2 << endl;  // Imprime las dos cadenas de texto concatenadas
        } else if (i % 3 == 0) {                // Si el número es múltiplo de 3 y no de 5
            cout << cadena1 << endl;            // Imprime la cadena de texto del primer parámetro
        } else if (i % 5 == 0) {                // Si el número es múltiplo de 5 y no de 3
            cout << cadena2 << endl;            // Imprime la cadena de texto del segundo parámetro
        } else {                                // Si el número no es múltiplo de 3 ni de 5
            cout << i << endl;                  // Imprime el número
            contadorNumeros++;                  // Incrementa el contador
        }
    }
    return contadorNumeros;                     // Retorna el contador
}

int main() {
    // Ejemplo de uso de las funciones
    saludar();

    mostrarSuma(5, 7);

    int resultado = multiplicar(3, 4);
    cout << "El resultado de la multiplicación es: " << resultado << endl;

    // Prueba de variable local y global
    modificarVariables();
    cout << "Variable global después de modificarla: " << globalVar << endl;

    // DIFICULTAD EXTRA: Función con dos cadenas de texto que imprime los múltiplos
    string palabra1 = "Carlos";
    string palabra2 = "Guariglia";
    int vecesNumeros = imprimirMultiples(palabra1, palabra2);
    cout << "Número de veces que se imprimió un número: " << vecesNumeros << endl;

    return 0;
}
