/*
 * EJERCICIO:
 * Implementa los mecanismos de introducción y recuperación de elementos propios de las
 * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
 * o lista (dependiendo de las posibilidades de tu lenguaje).
 *
 * DIFICULTAD EXTRA (opcional):
 * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
 *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
 *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
 *   Las palabras "adelante", "atras" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
 * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos.
 */

#include <stdio.h>
#include <stdlib.h>

#define ELEMENT_TYPE const char*
const ELEMENT_TYPE NULL_ELEMENT_TYPE = NULL;


/*
Queue element type
*/
typedef struct t_struct_queue_element {
	ELEMENT_TYPE element;
	struct t_struct_queue_element *previous_element;
	struct t_struct_queue_element *next_element;
} t_queue_element;

/*
Queue type
*/
typedef struct {
	t_queue_element* firstElement;
	t_queue_element* lastElement;
} t_queue;


/*
Initialize queue
*/
void initialize_queue (t_queue* inOutQueue) {
	inOutQueue->firstElement = NULL;
	inOutQueue->lastElement = NULL;
}

/*
Return 0 if queue is not empty
*/
int isQueueEmpty (t_queue* inOutQueue) {
	return (inOutQueue->firstElement == NULL);
}

/*
Add element at the end of the list
*/
void push (t_queue* inOutQueue, ELEMENT_TYPE inElement) {

	t_queue_element* newQueElement = malloc (sizeof (t_queue_element));

	newQueElement->element = inElement;

	/* Add new element at the end of the list*/
	newQueElement->previous_element = inOutQueue->lastElement;
	newQueElement->next_element = NULL;

	if (inOutQueue->firstElement == NULL ) {
		inOutQueue->firstElement = newQueElement;
	}

	if (inOutQueue->lastElement == NULL ) {
		inOutQueue->lastElement = newQueElement;
	} else {
		inOutQueue->lastElement->next_element = newQueElement;
		inOutQueue->lastElement = newQueElement;
	}
}

/*
Get element from queue applying LIFO policy
*/
ELEMENT_TYPE pop_lifo (t_queue* inOutQueue) {

	ELEMENT_TYPE element = NULL_ELEMENT_TYPE;
	t_queue_element* lastElement = inOutQueue->lastElement;

	if (lastElement != NULL) {
		element = lastElement->element;

		if (lastElement->previous_element != NULL) {

			inOutQueue->lastElement = lastElement->previous_element;
			lastElement->previous_element->next_element = NULL;

		} else {

			inOutQueue->firstElement = NULL;
			inOutQueue->lastElement = NULL;

		};
		free (lastElement);
	}
	return element;

};

/*
Get element from queue applying FIFO policy
*/
ELEMENT_TYPE pop_fifo (t_queue* inOutQueue) {

	ELEMENT_TYPE element = NULL_ELEMENT_TYPE;
	t_queue_element* firstElement = inOutQueue->firstElement;

	if (firstElement != NULL) {
		element = firstElement->element;

		if (firstElement->next_element != NULL) {

			inOutQueue->firstElement = firstElement->next_element;
			firstElement->next_element->previous_element = NULL;

		} else {

			inOutQueue->firstElement = NULL;
			inOutQueue->lastElement = NULL;

		};
		free (firstElement);
	}
	return element;

};


void main () {
	
	const char* C_A = "Elemento A";
	const char* C_B = "Elemento B";
	const char* C_C = "Elemento C";
	const char* C_D = "Elemento D";
	t_queue queue;

	initialize_queue (&queue);

	printf ("Ejemplo LIFO:\n");
	push (&queue, C_A);
	printf ("push %s\n", C_A);
	push (&queue, C_B);
	printf ("push %s\n", C_B);
	push (&queue, C_C);
	printf ("push %s\n", C_C);

	printf ("pop %s\n", pop_lifo (&queue));
	push (&queue, C_D);
	printf ("push %s\n", C_D);
	printf ("pop %s\n", pop_lifo (&queue));
	printf ("pop %s\n", pop_lifo (&queue));
	printf ("pop %s\n", pop_lifo (&queue));

	printf ("Ejemplo FIFO:\n");
	push (&queue, C_A);
	printf ("push %s\n", C_A);
	push (&queue, C_B);
	printf ("push %s\n", C_B);
	push (&queue, C_C);
	printf ("push %s\n", C_C);

	printf ("pop %s\n", pop_fifo (&queue));
	push (&queue, C_D);
	printf ("push %s\n", C_D);
	printf ("pop %s\n", pop_fifo (&queue));
	printf ("pop %s\n", pop_fifo (&queue));
	printf ("pop %s\n", pop_fifo (&queue));

};

