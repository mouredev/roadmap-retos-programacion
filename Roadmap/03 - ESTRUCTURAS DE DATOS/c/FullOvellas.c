/*
 * La biblioteca estándar de C no nos proporciona ninguna implementación de estructuras de datos.
 * La única estructura de la que disponemos es el array, que forma parte del lenguaje.
 * Si queremos estructuras de datos tendremos que programarlas nosotros mismos o utilizar una
 * biblioteca de terceros.
 */

#include <stddef.h>
#include <stdint.h>
#include <stdio.h>

// Ejemplo de estructura de datos propia
struct IntNode {
    int32_t val;
    struct IntNode* next;
};
typedef struct IntNode IntNode;

struct IntLinkedList {
    IntNode* head;
    IntNode* (*get)(struct IntLinkedList* this, int32_t index);
};
typedef struct IntLinkedList IntLinkedList;

IntNode* get(IntLinkedList* this, int32_t index) {
    IntNode* result = this->head;
    int32_t i = 0;
    for (int32_t i = 0; i < index; i++) {
        if (result == NULL) {
            return result;
        }
        result = result->next;
    }
    return result;
}

int main() {
    // Array
    int32_t nums[] = {1, 2, 3};
    for (size_t i = 0; i < sizeof(nums) / sizeof(int32_t); i++) {
        printf("%i\n", nums[i]);
    }

    IntNode in;
    IntNode in2;
    in.val = 1;
    in2.val = 2;
    in.next = &in2;
    IntLinkedList ll;
    ll.head = &in;
    ll.get = get;

    printf("Valor del primer elemento de la lista: %i\n", ll.get(&ll, 0)->val);
    printf("Valor del segundo elemento de la lista: %i\n", ll.get(&ll, 1)->val);

    return 0;
}
