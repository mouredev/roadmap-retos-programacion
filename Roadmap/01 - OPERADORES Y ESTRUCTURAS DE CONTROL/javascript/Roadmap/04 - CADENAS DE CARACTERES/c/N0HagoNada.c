#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

#define MAX_LEN 100

// Función para comprobar si una palabra es un palíndromo
int esPalindromo(char *palabra)
{
    int longitud = strlen(palabra);
    for (int i = 0; i < longitud / 2; i++)
    {
        if (tolower(palabra[i]) != tolower(palabra[longitud - i - 1]))
        {
            return 0; // No es palíndromo
        }
    }
    return 1; // Es palíndromo
}

// Función para comprobar si dos palabras son anagramas
int sonAnagramas(char *palabra1, char *palabra2)
{
    int count[256] = {0};
    int i;

    for (i = 0; palabra1[i] && palabra2[i]; i++)
    {
        count[(int)tolower(palabra1[i])]++;
        count[(int)tolower(palabra2[i])]--;
    }

    if (palabra1[i] || palabra2[i])
    { // Si las palabras son de diferente longitud
        return 0;
    }

    for (i = 0; i < 256; i++)
    {
        if (count[i])
        {
            return 0; // No son anagramas
        }
    }
    return 1; // Son anagramas
}

// Función para comprobar si una palabra es un isograma
int esIsograma(char *palabra)
{
    int count[256] = {0};

    for (int i = 0; palabra[i]; i++)
    {
        if (count[(int)tolower(palabra[i])])
        {
            return 0; // No es isograma
        }
        count[(int)tolower(palabra[i])]++;
    }
    return 1; // Es isograma
}
int main()
{
    // Definición de la cadena original
    char str[] = "Hola mundo";
    char copia[20]; // Para operaciones que necesitan una copia

    // Acceso a caracteres específicos
    printf("Primer caracter: %c\n", str[0]);

    // Subcadenas
    strncpy(copia, str + 5, 5); // Copia "mundo" en copia
    copia[5] = '\0';            // Añade manualmente el carácter nulo
    printf("Subcadena: %s\n", copia);

    // Longitud
    printf("Longitud: %lu\n", strlen(str));

    // Concatenación
    char saludo[20] = "Hola";
    strcat(saludo, ", mundo");
    printf("Concatenación: %s\n", saludo);

    // Conversión a mayúsculas
    for (int i = 0; str[i]; i++)
    {
        str[i] = toupper(str[i]);
    }
    printf("A mayúsculas: %s\n", str);

    // Conversión a minúsculas
    for (int i = 0; str[i]; i++)
    {
        str[i] = tolower(str[i]);
    }
    printf("A minúsculas: %s\n", str);

    // Recorrido
    printf("Recorrido: ");
    for (int i = 0; str[i]; i++)
    {
        printf("%c", str[i]);
    }
    printf("\n");

    // División (Tokenización)
    char str2[] = "Hola mundo, prueba"; // Nueva cadena para evitar modificar la original en la tokenización
    printf("División:\n");
    char *token = strtok(str2, " ,");
    while (token != NULL)
    {
        printf("%s\n", token);
        token = strtok(NULL, " ,");
    }

    // Verificación (Buscar Subcadena)
    strcpy(copia, "Hola mundo"); // Restablecer copia a un valor conocido
    if (strstr(copia, "mundo") != NULL)
    {
        printf("Subcadena encontrada.\n");
    }
    else
    {
        printf("Subcadena no encontrada.\n");
    }

    char palabra1[MAX_LEN], palabra2[MAX_LEN];

    printf("Introduce la primera palabra: ");
    scanf("%99s", palabra1);
    printf("Introduce la segunda palabra: ");
    scanf("%99s", palabra2);

    // Comprobar si las palabras son palíndromos
    printf("'%s' es un palíndromo? %s\n", palabra1, esPalindromo(palabra1) ? "Sí" : "No");
    printf("'%s' es un palíndromo? %s\n", palabra2, esPalindromo(palabra2) ? "Sí" : "No");

    // Comprobar si las palabras son anagramas
    printf("'%s' y '%s' son anagramas? %s\n", palabra1, palabra2, sonAnagramas(palabra1, palabra2) ? "Sí" : "No");

    // Comprobar si las palabras son isogramas
    printf("'%s' es un isograma? %s\n", palabra1, esIsograma(palabra1) ? "Sí" : "No");
    printf("'%s' es un isograma? %s\n", palabra2, esIsograma(palabra2) ? "Sí" : "No");

    return 0;
}