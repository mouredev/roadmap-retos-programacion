#include <stddef.h>
#include <string.h>
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

/*
//---------------- Array
int numbers[] = {0, 1, 2, 3, 4, 5};

// Acceder a un elemento
printf("%d\n", numbers[2]);

// Cambiar un elemento
numbers[2] = 7;
printf("%d\n", numbers[2]);

// Iterar
printf("{");
for (int i = 0; i < 6; i++) {
    printf("%d, ", numbers[i]);
}
printf("}\n");

// Iniciar con tamaño fijo
int fourNumbers[4];
fourNumbers[0] = 0;
fourNumbers[1] = 1;
fourNumbers[2] = 2;
fourNumbers[3] = 3;

// Tamaño del array
int length = sizeof(fourNumbers) / sizeof(fourNumbers[0]);
printf("%d\n", length);

//Multidimensional
int matrix[3][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};

for (int i = 0; i < 3; i++) {

    for (int j = 0; j < 3; j++) {
        printf("%d, ", matrix[i][j]);
    }
    printf("\n");
}

//------------------ Structs
struct myStructure {
    int number;
    char character;
};

struct myStructure s1;
s1.character = 'A';
s1.number = 10;
printf("%c\n", s1.character);
printf("%d\n", s1.number);

//------------- Enumeration
enum Level {
    LOW,
    MEDIUM,
    HIGH
};


enum Level {
    LOW = 25,
    MEDIUM = 50,
    HIGH = 75
};

enum Level myLevel1 = LOW;
enum Level myLevel2 = MEDIUM;
enum Level myLevel3 = HIGH;
printf("%d\n", myLevel1);
printf("%d\n", myLevel2);
printf("%d\n", myLevel3);
*/

#define MAX_CONTACTS 100
#define MAX_NAME_LENGTH 100

struct Contact {
    int number;
    char name[MAX_NAME_LENGTH];
};

struct Contact contacts[MAX_CONTACTS];
int contactCount = 0;

void clearInputBuffer() {
    int c;
    while ((c = getchar()) != '\n' && c != EOF);
}

void removeElement(struct Contact arr[], int index) {
       if (index < 0 || index >= MAX_CONTACTS) {
           printf("Índice fuera de rango\n");
           return;
       }

       // Desplazar los elementos posteriores hacia adelante
       for (int i = index; i < MAX_CONTACTS - 1; i++) {
           arr[i] = arr[i + 1];
       }

       // Inicializar el último elemento a valores predeterminados
       arr[contactCount - 1].number = 0;
       arr[contactCount - 1].name[0] = '\0';

       contactCount--;
   }

struct Contact search() {
    char contactName[MAX_NAME_LENGTH];
    struct Contact contact = {0, ""};

    clearInputBuffer();

    printf("\nIntroduce el nombre del contacto: ");
    if (fgets(contactName, sizeof(contactName), stdin) == NULL) {
        fprintf(stderr, "\nError al leer el nombre\n");
    }

    // Eliminar el carácter de nueva línea al final de la cadena
    size_t len = strlen(contactName);
    if (len > 0 && contactName[len - 1] == '\n') {
        contactName[len - 1] = '\0';
    }

    for (int i = 0; i < MAX_CONTACTS; i++) {
        if (strcmp(contacts[i].name, contactName) == 0) {
            contact = contacts[i];
            break;
        }
    }

    return contact;
}

int addContact() {
    if (contactCount >= MAX_CONTACTS) {
        fprintf(stderr, "\nNo se pueden añadir más contactos\n");
        return 1;
    }

    struct Contact contact;
    char contactName[MAX_NAME_LENGTH];
    int contactNumber;

    clearInputBuffer();

    printf("\nIntroduce el nombre del contacto: ");
    if (fgets(contactName, sizeof(contactName), stdin) == NULL) {
        fprintf(stderr, "\nError al leer el nombre\n");
        return 1;
    }

    // Eliminar el carácter de nueva línea al final de la cadena
    size_t len = strlen(contactName);
    if (len > 0 && contactName[len - 1] == '\n') {
        contactName[len - 1] = '\0';
    }

    // Solicitar el número del contacto
    printf("Introduce el número del contacto: ");
    if (scanf("%d", &contactNumber) != 1) {
        fprintf(stderr, "\nError al leer el número\n");
        clearInputBuffer();
        return 1;
    }

    strcpy(contact.name, contactName);
    contact.number = contactNumber;

    contacts[contactCount++] = contact;
    printf("Contacto añadido correctamente\n");

    return 0;
}

int update() {
    int contactNumber;
    struct Contact contact = search();

    // Solicitar el nuevo número del contacto
    printf("Introduce el nuevo número del contacto: ");
    if (scanf("%d", &contactNumber) != 1) {
        fprintf(stderr, "\nError al leer el número\n");
        clearInputBuffer();
        return 1;
    }

    if (contact.number) {
        for (int i = 0; i < MAX_CONTACTS; i++) {
            if (strcmp(contacts[i].name, contact.name) == 0) {
                contacts[i].number = contactNumber;
                printf("Contacto actualizado\n");
                break;
            }
        }
    } else {
        printf("El contacto no existe\n");
    }

    return 0;
}

int removeContact() {
    struct Contact contact = search();

    if (contact.number) {
        for (int i = 0; i < MAX_CONTACTS; i++) {
            if (strcmp(contacts[i].name, contact.name) == 0) {
                removeElement(contacts, i);
                printf("Contacto eliminado\n");
                break;
            }
        }
    } else {
        printf("El contacto no existe\n");
    }

    return 0;
}

int main() {

    int choice;
    bool finish = false;
    struct Contact contact;

    while (!finish) {
        printf("\nQué dese hacer?:\n");
        printf("1- Buscar\n");
        printf("2- Añadir\n");
        printf("3- Actualizar\n");
        printf("4- Eliminar\n");
        printf("5- Salir\n");

        if (scanf("%d", &choice) != 1) {
            fprintf(stderr, "\n⚠️ Opción incorrecta\n");
        }

        switch (choice) {
            case 1:
                contact = search();
                if (contact.number) {
                    printf("%s - %d\n", contact.name, contact.number);
                } else {
                    printf("No existe el contacto\n");
                }
                break;
            case 2:
                addContact();
                break;
            case 3:
                update();
                break;
            case 4:
                removeContact();
                break;
            case 5:
                finish = true;
                printf("👋 Hasta pronto");
                break;
            default:
                printf("\n⚠️ Opción incorrecta\n");
        }
    }


    return 0;
}
