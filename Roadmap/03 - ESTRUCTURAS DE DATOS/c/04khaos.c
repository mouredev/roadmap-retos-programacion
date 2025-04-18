#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Prototipos de funciones para las estructuras de datos
void arrays();
void structs();
void linkedlists();
void queue();
void stacks();

// Definición global de la estructura node
typedef struct node {
    int number;
    struct node* next;
} node;

// Variables globales para las colas (First In, First Out)
node *front = NULL; // Apunta al primer elemento de la cola (First to dequeue)
node *rear = NULL;  // Apunta al último elemento de la cola (Recently enqueue add)

// Variables globales para las pilas (Last In, First Out)
node* top = NULL;   // Apunta al tope de la pila (Last element added)

// Prototipos de funciones para las colas 
void enqueue(int value);
void dequeue();
void displayqueue();

// Prototipos de funciones para las pilas 
void push(int value);
void pop();
void displaystack();


// DIFICULTAD EXTRA

#define MAX_CONTACTS 100
#define MAX_NAME 50
#define MAX_PHONE 12

typedef struct {
    char name[MAX_NAME];
    char phone[MAX_PHONE];
} contacts;

contacts *contact = NULL;
int contactCount = 0;

void displaymenu();
int validatePhone(const char *phone);
void addContact();
void searchContact();
void updateContact();
void deleteContact();
void displayContact();


int main() {

    printf("\n== Basic Structures ==");

    printf("\n1. Arrays\n");
    arrays();

    printf("\n\n2. Structs\n");
    structs();

    printf("\n3. Linked Lists\n");
    linkedlists();

    printf("\n4. Queue\n");
    queue();

    printf("\n5. Stacks\n");
    stacks();

    printf("\n== Extra Difficulty ==\n");

    int option;
    do {
        displaymenu();

        (scanf("%d", &option));
        getchar();
        switch (option) {
            case 1:
                searchContact();
                break;
            case 2:
                addContact();
                while (getchar() != '\n'); // Limpiar buffer
                break;
            case 3:
                updateContact();
                while (getchar() != '\n');
                break;
            case 4:
                deleteContact();
                break;
            case 5:
                displayContact();
                break;
            case 6:
                printf("Exiting the program...\n\n");
                break;
            default:
                printf("Invalid option. Please try again\n\n");
        }
    } while (option != 6);

    free(contact);
    return 0;
}


void arrays() {

    // Creación de un array simple de enteros
    int arr[10] = {10, 4, 3, 6, 1, 8};
    int size = 6;

    printf("Initial array: ");
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }

    // Inserción de un elemento
    if (size < 10) {
        arr[size] = 5;
        size++;
    }

    // Actualización de un elemento
    printf("\nUpdated array: ");
    arr[2] = 0;
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }

    // Eliminación de un elemento
    for (int i = 0; i < size; i++) {
        arr[i] = arr[i + 1];
    }
    size--;

    // Bubble sort
    for (int i = 0; i < size - 1; i++) {
        for (int j = 0; j < size - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }

    printf("\nFinal array: ");
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }

}


void structs() {

    typedef struct {
        char name[20];
        int age;
    } persons;

    persons person[3] = {
        {"Gregory", 45},
        {"Wilson", 38},
        {"Alice", 20},
    };

    for (int i = 0; i < 3; i++) {
        printf("1. Name: %s, %d years old\n", person[i].name, person[i].age);
    }
}


void linkedlists() {

    node *list = NULL;

    // Crear y agregar nodos a la lista
    for (int i = 0; i < 3; i++) {
        node *n = malloc(sizeof(node));
        if (n == NULL) {
            return;
        }

        n->number = i+1;
        n->next = list;
        list = n;
    }

    // Imprimir la lista
    node *ptr = list;
    while (ptr != NULL) {
        printf("%d -> ", ptr->number);
        ptr = ptr->next;
    }
    printf("NULL\n");


    // Liberar memoria
    node *temp;
    while(list != NULL) {
        temp = list;
        list = list->next;
        free(temp);
    }
}


void queue() {

    // Estado inicial de la cola
    printf("Initial state: ");
    displayqueue();

    // Añadir elementos a la cola
    printf("Enqueue all: ");
    enqueue(10);
    enqueue(20);
    enqueue(30);
    displayqueue();

    // Eliminar un elemento de la cola
    printf("Dequeue one: ");
    dequeue();
    displayqueue();

    // Añadir un elemento a la cola
    printf("Enqueue one: ");
    enqueue(40);
    displayqueue();

    // Eliminar todos los elementos de la cola
    printf("Dequeue all: ");
    while (front != NULL) {
        dequeue();
    }
    displayqueue();
}

void enqueue(int value) {
    node* newNode = malloc(sizeof(node));
    if (newNode == NULL) {
        printf("Memory allocation failed\n");
        return;
    }

    newNode->number = value;      // Asignar el valor al nuevo nodo
    newNode->next = NULL;         // El nuevo nodo no tiene siguiente

    if (rear == NULL) {
        front = rear = newNode;   // Si la cola esta vacia, el nuevo nodo es el primero y el último
    } else {
        rear->next = newNode;     // El último nodo apunta al nuevo
        rear = newNode;           // El nuevo nodo ahora es el último 
    }
}

void dequeue() {
    if (front == NULL) {
        printf("Error: The queue is empty\n");
    }

    node *temp = front;           // Guardar el nodo que se eliminará (el primero, o sea 10)

    front = front->next;          // Mover al frente el siguiente nodo (el siguiente, o sea 20)
    if (front == NULL) {
        rear = NULL;              // Si la cola quedó vacía, también actualizamos rear
    }

    free(temp);                   // Liberar la memoria del nodo eliminado
}

void displayqueue() {
    if (front == NULL) {
        printf("The queue is empty\n");
        return;
    }

    node *ptr = front;            // Puntero temporal para recorrer la cola
    while (ptr != NULL) {         // Recorrer la cola y mostrar el valor actual 
        printf("%d -> ", ptr->number);
        ptr = ptr->next;          // Mover al siguiente nodo
    }
    printf("NULL\n");
}


void stacks() {

    printf("Initial state: ");
    displaystack();

    printf("Push elements: ");
    push(100);
    push(200);
    push(300);
    displaystack();

    printf("Pop one element: ");
    pop();
    displaystack();

    printf("Pop all elements: ");
    while (top != NULL) {
        pop();
    }
    displaystack();
}

void push(int value) {
    node *newNode = malloc(sizeof(node));
    if (newNode == NULL) {
        printf("Memory allocation failed\n");
        return;
    }

    newNode->number = value;            // Asignar el valor al nuevo nodo
    newNode->next = top;                // El nuevo nodo apunta al tope actual
    top = newNode;                      // El nuevo nodo es ahora el tope
}

void pop() {
    if (top == NULL) {
        printf("Error: The stacks is empty\n");
        return;
    }

    node *temp = top;                   // Guardar el nodo que se eliminará
    top = top->next;                    // Mover el tope al siguiente nodo

    free(temp);                         // Liberar la memoria del nodo eliminado
}

void displaystack() {
    if (top == NULL) {
        printf("The stacks is empty\n");
        return;
    }

    node *ptr = top;
    while(ptr != NULL) {
        printf("%d -> ", ptr->number);
        ptr = ptr->next;
    }   
    printf("NULL\n");
}


// FUNCIONES DE LA DIFICULTAD EXTRA 

void displaymenu() {

    printf("\n1. Search contact\n");
    printf("2. Add contact\n");
    printf("3. Update contact\n");
    printf("4. Delete contact\n");
    printf("5. Display contacts\n");
    printf("6. Exit\n");
    printf("Option: ");
}

int validatePhone(const char *phone) {

    if (strlen(phone) != 11) {
        return 0;
    }

    for (int i = 0; i < 11; i++) {
        if(!isdigit(phone[i])) {
            return 0;
        }
    }

    return 1;
}


void addContact() {

    if (contactCount >= MAX_CONTACTS) {
        printf("The contact list is full");
        return;
    }

    contacts newContact;

    printf("Enter contact name: ");
    fgets(newContact.name, sizeof(newContact.name), stdin);
    newContact.name[strcspn(newContact.name, "\n")] = '\0';

    if (strlen(newContact.name) == 0) {
        printf("Error: The contact name cannot be empty\n");
        return;
    }

    printf("Enter phone number (11 digits): ");
    fgets(newContact.phone, sizeof(newContact.phone), stdin);
    newContact.phone[strcspn(newContact.phone, "\n")] = '\0';

    if (!validatePhone(newContact.phone)) {
        printf("Error: Invalid phone number\n");
        return;
    }

    contact = realloc(contact, (contactCount + 1) * sizeof(contacts));
    if (contact == NULL) {
        printf("Memory allocation failed\n");
        return;
    }

    contact[contactCount] = newContact;
    contactCount++;

    printf("Contact added successfully\n");
}

void searchContact() {
    char query[MAX_NAME];
    printf("Contact name or phone to search: ");
    fgets(query, sizeof(query), stdin);
    query[strcspn(query, "\n")] = '\0';

    for (int i = 0; i < contactCount; i++) {
        if (strcmp(query, contact[i].name) == 0 || strcmp(query, contact[i].phone) == 0) {
            printf("Contact found: (%d) %s, +%s\n", i+1, contact[i].name, contact[i].phone);
            return;
        }
    }

    printf("Contact not found\n\n");
}

void updateContact() {
    char query[MAX_NAME];
    printf("Enter a name or phone to update contact: ");
    fgets(query, sizeof(query), stdin);
    query[strcspn(query, "\n")] = '\0';

    for (int i = 0; i < contactCount; i++) {
        if (strcmp(contact[i].name, query) == 0 || strcmp(contact[i].phone, query) == 0) {
            printf("-> Leave blank to make no changes <-\n");

            // Actualizar nombre o dejar en blanco
            printf("New name: ");
            char newName[MAX_NAME];
            fgets(newName, sizeof(newName), stdin);
            newName[strcspn(newName, "\n")] = '\0';

            if (strlen(newName) > 0) {
                strcpy(contact[i].name, newName);
            }

            // Actualizar número o dejar en blanco
            printf("New phone: ");
            char newPhone[MAX_PHONE];
            fgets(newPhone, sizeof(newPhone), stdin);
            newPhone[strcspn(newPhone, "\n")] = '\0';

            if (strlen(newPhone) > 0) {
                if (!validatePhone(newPhone)) {
                    printf("Error: Invalid phone number.\n");
                    return;
                }
                strcpy(contact[i].phone, newPhone);
            }

            printf("Contact update successfully\n");
            return;
        }
    }

    printf("Contact not found\n");
}

void deleteContact() {
    if (contactCount == 0) {
        printf("No contacts to delete\n");
        return;
    }

    char query[MAX_NAME];
    printf("Contact name or phone to delete: ");
    fgets(query, sizeof(query), stdin);
    query[strcspn(query, "\n")] = '\0';

    int found = 0;

    for (int i = 0; i < contactCount; i++) {
        if (strcmp(contact[i].name, query) == 0 || strcmp(contact[i].phone, query) == 0) {
            for (int j = i; j < contactCount - 1; j++) {
                contact[j] = contact[j+1];
            }
            found = 1;
            contactCount--;
            break;
        } 
    }

    if (!found) {
        printf("Contact not found\n");
        return;
    }

    // Si ya no hay contactos, liberar la memoria
    if (contactCount == 0) {
        free(contact);
        contact = NULL;
    } else {
        contacts *temp = realloc(contact, contactCount * sizeof(contacts)); // Redimensionar la memoria reservada para contact de acuerdo con el nuevo contactCount
        if (temp == NULL) {
            printf("Memory allocation failed\n");
            return;
        }
        contact = temp;
    } 

    printf("Contact delete successful\n");
}

void displayContact() {
    if (contactCount == 0) {
        printf("No contacts found (Press enter)\n");
        return;
    }

    printf("\n------ Contact list ------\n");
    for(int i = 0; i < contactCount; i++) {
        printf("(%d) %s, +%s\n", i+1, contact[i].name, contact[i].phone);
    }
    printf("-------- (%d/%d) --------\n", contactCount, MAX_CONTACTS);
}