#include <string.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>


/*
char name[] = "Diego";
char hello[20] = {'H', 'e', 'l', 'l', 'o', ' ', '\0'};
char saludo[] = "\tHola \"amigo\"";
printf("%s\n", name);
printf("%s\n", hello);
printf("%s\n", saludo);

// Acceso
printf("%c\n", name[0]);

//Modificar
name[0] = 'd';
printf("%s\n", name);

//Interar
int length = sizeof(name) / sizeof(name[0]);

for (int i = 0; i < length; i++) {
    printf("%c\n", name[i]);
}

// Tamaño
int size = strlen(saludo);
printf("%d\n", size);

//Concatenar
strcat(hello, name);
printf("%s\n", hello);

//Copiar
char str[20];
strcpy(str, hello);
printf("%s\n", str);

//Comparar
printf("%d\n", strcmp(hello, str));
*/


bool isPalindrome(const char *str) {
    int len = strlen(str);
    char backwards[len + 1];

    for (int i = 0; i < len; i++) {
        backwards[i] = str[len - 1 - i];
    }
    backwards[len] = '\0';

    if (strcmp(str, backwards) == 0) {
        return true;
    }

    return false;
}

bool areAnagrams(char *str1, char *str2) {
    int count[256] = {0}; // Asumiendo ASCII

    // Si las longitudes son diferentes, no pueden ser anagramas
    if (strlen(str1) != strlen(str2)) {
        return false;
    }

    // Incrementar el conteo de caracteres para str1
    // y decrementar el conteo de caracteres para str2
    for (int i = 0; str1[i] && str2[i]; i++) {
        count[(unsigned char)str1[i]]++;
        count[(unsigned char)str2[i]]--;
    }

    // Verificar si todos los conteos son cero
    for (int i = 0; i < 256; i++) {
        if (count[i] != 0) {
            return false;
        }
    }

    return true;
}

bool isIsogram(char str[]) {
    int len = strlen(str);
    int frequency[256] = {0};

    for (int i = 0; i < len; i++) {
        char ch = tolower((unsigned char)str[i]);

        if (frequency[(unsigned char)ch] > 0) {
            return false;
        }
        frequency[(unsigned char)ch]++;
    }

    return true;
}

int main() {

    char firstWord[30];
    char secondWord[30];

    printf("Escribe la primera palabra\n > ");
    scanf("%s", firstWord);
    printf("Escribe la segunda palabra\n > ");
    scanf("%s", secondWord);

    if (isPalindrome(firstWord)) {
        printf("%s es un palíndromo\n", firstWord);
    }
    if (isPalindrome(secondWord)) {
        printf("%s es un palíndromo\n", secondWord);
    }

    if (areAnagrams(firstWord, secondWord)) {
        printf("%s y %s son anagramas\n", firstWord, secondWord);
    }

    if (isIsogram(firstWord)) {
        printf("%s es un isograma\n", firstWord);
    }
    if (isIsogram(secondWord)) {
        printf("%s es un isograma\n", secondWord);
    }

    return 0;
}
