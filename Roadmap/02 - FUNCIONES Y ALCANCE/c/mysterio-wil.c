#include <stdio.h>
#include <string.h>
#include <stdarg.h> // For variable arguments

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

// --- Declarations of functions ---

// Basic functions
void greet(void);
void greet_person(const char* name);
void add(int a, int b);
int multiply(int a, int b);
// No default parameters in C, so we define a standard function.
void greet_default(const char* name, const char* greeting);
// Variable arguments
int sum_all(int count, ...);

// Nested functions are not supported in standard C.

// Scope
void my_function_scope(void);
void modify_global(void);

// Extra difficulty
int fizz_buzz_extra(const char* text1, const char* text2);


// --- Global variable ---
// Usamos un array de char para que la cadena sea modificable
char global_var_buffer[50] = "Soy una variable global";
char* global_var = global_var_buffer;


// --- Main function ---
int main() {
    printf("===> Funciones básicas <===\n");

    // Sin parámetros ni retorno
    greet();

    // Con un parámetro
    greet_person("Wilmer");

    // Con varios parámetros
    add(5, 3);

    // Con retorno
    int result = multiply(5, 3);
    printf("El resultado de la multiplicación es %d\n", result);

    // Simulating default parameters
    printf("No hay parámetros por defecto en C.\n");
    greet_default("MoureDev", "Hola");
    greet_default("Wilmer", "Hello");

    // Con parámetros de longitud variable
    int total = sum_all(4, 10, 20, 30, 5);
    printf("Suma variable: %d\n", total);


    printf("\n===> Funciones dentro de funciones <===\n");
    printf("Standard C no soporta funciones anidadas.\n");


    printf("\n===> Funciones de la librería estándar <===\n");
    const char* my_text = "Hola Mundo";
    printf("Usando la función strlen() de <string.h>:\n");
    printf("El texto \"%s\" tiene %zu caracteres.\n", my_text, strlen(my_text));


    printf("\n===> Variable LOCAL y GLOBAL <===\n");
    my_function_scope();

    // Modificar una variable global
    printf("Antes de modificar: %s\n", global_var);
    modify_global();
    printf("Después de modificar: %s\n", global_var);


    /*
     * DIFICULTAD EXTRA (opcional):
     */
    printf("\n====> DIFICULTAD EXTRA <====\n");
    int times_printed_number = fizz_buzz_extra("Fizz", "Buzz");
    printf("\nEl número se imprimió un total de %d veces.\n", times_printed_number);

    return 0;
}


// --- Definitions of functions ---

void greet(void) {
    printf("Hola, C!\n");
}

void greet_person(const char* name) {
    printf("Hola, %s!\n", name);
}

void add(int a, int b) {
    printf("La suma de %d y %d es %d\n", a, b, a + b);
}

int multiply(int a, int b) {
    return a * b;
}

void greet_default(const char* name, const char* greeting) {
    printf("%s, %s!\n", greeting, name);
}

int sum_all(int count, ...) {
    int total = 0;
    va_list args;
    va_start(args, count);
    for (int i = 0; i < count; i++) {
        total += va_arg(args, int);
    }
    va_end(args);
    return total;
}

void my_function_scope(void) {
    const char* local_var = "Soy una variable local";
    printf("%s\n", global_var); // Podemos acceder a la variable global
    printf("%s\n", local_var);
}

void modify_global(void) {
    // Copiamos la nueva cadena en el buffer global para modificarla de forma segura
    strcpy(global_var_buffer, "He modificado la variable global");
}

int fizz_buzz_extra(const char* text1, const char* text2) {
    int count = 0;
    for (int i = 1; i <= 100; i++) {
        int is_multiple_of_3 = (i % 3 == 0);
        int is_multiple_of_5 = (i % 5 == 0);

        if (is_multiple_of_3 && is_multiple_of_5) {
            printf("%s%s\n", text1, text2);
        } else if (is_multiple_of_3) {
            printf("%s\n", text1);
        } else if (is_multiple_of_5) {
            printf("%s\n", text2);
        } else {
            printf("%d\n", i);
            count++;
        }
    }
    return count;
}
