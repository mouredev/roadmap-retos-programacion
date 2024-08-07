#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX 100

// Estructura para una cola
typedef struct
{
    char *items[MAX];
    int front, rear;
} Queue;

// Función para inicializar la cola
void initQueue(Queue *queue)
{
    queue->front = -1;
    queue->rear = -1;
}

// Función para añadir elemento a la cola
void enqueue(Queue *queue, char *item)
{
    if (queue->rear == MAX - 1)
    {
        printf("Queue full\n");
        return;
    }
    if (queue->front == -1)
        queue->front = 0;
    queue->items[++queue->rear] = strdup(item); // Duplica el item y guarda el puntero
}

// Función para quitar elemento de la cola
char *dequeue(Queue *queue)
{
    if (queue->front == -1 || queue->front > queue->rear)
    {
        printf("Queue empty\n");
        return NULL;
    }
    char *item = queue->items[queue->front];
    queue->items[queue->front++] = NULL; // Evita fugas de memoria
    if (queue->front > queue->rear)
    { // Resetea la cola si está vacía
        queue->front = queue->rear = -1;
    }
    return item;
}

int main()
{
    Queue printQueue;
    initQueue(&printQueue);

    // Simulación de la cola de impresión
    enqueue(&printQueue, "Documento1.pdf");
    enqueue(&printQueue, "Imagen.png");
    enqueue(&printQueue, "Tarea.docx");

    printf("Printing: %s\n", dequeue(&printQueue)); // Imprime Documento1.pdf
    printf("Printing: %s\n", dequeue(&printQueue)); // Imprime Imagen.png

    return 0;
}
