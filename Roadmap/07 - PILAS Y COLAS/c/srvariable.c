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
 *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
 * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos.
 */

// Inclusión de librerías

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Enum para las diferentes funciones

typedef enum e_function
{
	PUSH,
	POP,
	PEEK_STACK,
	ENQUEUE,
	DEQUEUE,
	PEEK_QUEUE,
}				t_function;

// Estructura de un nodo

typedef struct s_node
{
	char			*item;
	struct s_node	*next;
}				t_node;

/* Funciones de los nodos */
t_node	*create_node(const char *item);
void	destroy_node(t_node **node);

// Estructura de una pila

typedef struct s_stack
{
	t_node	*bottom;
	t_node	*top;
}				t_stack;

/* Declaración de funciones de la pila */

t_stack	*create_stack(const char *item);
void	destroy_stack(t_stack **stack);
int		push(t_stack **stack, const char *item);
int		pop(t_stack **stack);
char	*peek_stack(t_stack *stack);
int		test_stack(void);

// Estructura de una cola
typedef struct s_queue
{
	t_node	*back;
	t_node	*front;
}				t_queue;

/* Declaración de funciones de la cola */

t_queue	*create_queue(const char *item);
void	destroy_queue(t_queue **queue);
int		enqueue(t_queue **queue, const char *item);
int		dequeue(t_queue **queue);
char	*peek_queue(t_queue *queue);
int		test_queue(void);

// Manejo de errores

int		error_handler(void *address, int status, t_function type);

int	main(void)
{
	int	status;

	printf("=== INICIO STACK ===\n");
	status = test_stack();
	if (status) return (status);
	printf("=== FIN STACK ===\n");
	printf("\n");
	printf("=== INICIO QUEUE ===\n");
	status = test_queue();
	if (status) return (status);
	printf("=== FIN QUEUE ===\n");

	return (0);
}

/**
 * @brief Crea un nodo.
 *
 * @param item Elemento que se añadirá al nodo.
 *
 * @return - El nodo creado.
 * @return - NULL Si falla la creación del nodo.
 */
t_node	*create_node(const char *item)
{
	t_node	*node;

	node = (t_node *) malloc(sizeof(t_node));
	if (!node) return (NULL);
	node->item = strdup(item);
	if (!node->item)
	{
		free(node);
		return (NULL);
	}
	node->next = NULL;
	return (node);
}

/**
 * @brief Destruye el nodo.
 *
 * @param node Dirección de memoria del nodo.
 */
void	destroy_node(t_node **node)
{
	if (!(*node)) return;
	if ((*node)->item)
	{
		free((*node)->item);
		(*node)->item = NULL;
	}
	free(*node);
	*node = NULL;
}

/**
 * @brief Maneja los diferentes posibles errores
 *
 * @param address Dirección de memoria de la pila/cola.
 * @param status Estado que indica en qué llamada ha fallado.
 * @param type 
 *
 * @return - status
 */
int	error_handler(void *address, int status, t_function type)
{
	if (type == POP || type == PEEK_STACK) printf("La pila está vacía\n");
	else if (type == DEQUEUE || type == PEEK_QUEUE) printf("La cola está vacía\n");
	else if (type = PUSH)
	{
		printf("Error añadiendo el elemento a la pila, llamada %d\n", status);
		destroy_stack((t_stack **) address);
	}
	else if (type = ENQUEUE)
	{
		printf("Error añadiendo el elemento a la cola, llamada %d\n", status);
		destroy_queue((t_queue **) address);
	}
	return (status);
}

/**
 * @brief Test de funciones del stack.
 *
 * @return - > 0 Si hay algún error grave.
 * @return - 0 Si el test se ejecuta correctamente.
 */
int	test_stack(void)
{
	t_stack	*stack;
	int		status;
	char	*element;

	stack = NULL;

	status = push(&stack, "Hola");
	if (status) return (error_handler(&stack, status, PUSH));
	if (stack->bottom)
		printf("Bottom: %s | Top: %s\n", stack->bottom->item, stack->top->item);

	status = push(&stack, "Mundo");
	if (status) return (error_handler(&stack, status, PUSH));
	if (stack->bottom)
		printf("Bottom: %s | Top: %s\n", stack->bottom->item, stack->top->item);

	status = pop(&stack);
	if (status) error_handler(&stack, status, POP);
	if (stack->bottom)
		printf("Bottom: %s | Top: %s\n", stack->bottom->item, stack->top->item);

	status = pop(&stack);
	if (status) error_handler(&stack, status, POP);
	if (stack->bottom)
		printf("Bottom: %s | Top: %s\n", stack->bottom->item, stack->top->item);

	status = pop(&stack);
	if (status) error_handler(&stack, status, POP);
	if (stack->bottom)
		printf("Bottom: %s | Top: %s\n", stack->bottom->item, stack->top->item);

	status = push(&stack, "La");
	if (status) return (error_handler(&stack, status, PUSH));
	if (stack->bottom)
		printf("Bottom: %s | Top: %s\n", stack->bottom->item, stack->top->item);

	status = push(&stack, "Pila");
	if (status) return (error_handler(&stack, status, PUSH));
	if (stack->bottom)
		printf("Bottom: %s | Top: %s\n", stack->bottom->item, stack->top->item);

	status = push(&stack, "Funciona");
	if (status) return (error_handler(&stack, status, PUSH));
	if (stack->bottom)
		printf("Bottom: %s | Top: %s\n", stack->bottom->item, stack->top->item);

	element = peek_stack(stack);
	if (!element) error_handler(&stack, status, PEEK_STACK);
	else printf("El último elemento de la pila es: %s\n", element);

	status = pop(&stack);
	if (status) error_handler(&stack, status, POP);
	if (stack->bottom)
		printf("Bottom: %s | Top: %s\n", stack->bottom->item, stack->top->item);

	element = peek_stack(stack);
	if (!element) error_handler(&stack, status, PEEK_STACK);
	else printf("El último elemento de la pila es: %s\n", element);

	status = pop(&stack);
	if (status) error_handler(&stack, status, POP);
	if (stack->bottom)
		printf("Bottom: %s | Top: %s\n", stack->bottom->item, stack->top->item);

	element = peek_stack(stack);
	if (!element) error_handler(&stack, status, PEEK_STACK);
	else printf("El último elemento de la pila es: %s\n", element);

	status = pop(&stack);
	if (status) error_handler(&stack, status, POP);
	if (stack->bottom)
		printf("Bottom: %s | Top: %s\n", stack->bottom->item, stack->top->item);

	element = peek_stack(stack);
	if (!element) error_handler(&stack, status, PEEK_STACK);
	else printf("El último elemento de la pila es: %s\n", element);

	status = pop(&stack);
	if (status) error_handler(&stack, status, POP);
	if (stack->bottom)
		printf("Bottom: %s | Top: %s\n", stack->bottom->item, stack->top->item);

	element = peek_stack(stack);
	if (!element) error_handler(&stack, status, PEEK_STACK);
	else printf("El último elemento de la pila es: %s\n", element);

	destroy_stack(&stack);
	return (0);
}

int		test_queue(void)
{
	t_queue	*queue;
	int		status;
	char	*element;

	queue = NULL;

	status = enqueue(&queue, "Hola");
	if (status) error_handler(&queue, status, ENQUEUE);
	if (queue->front)
		printf("Front: %s | Back: %s\n", queue->front->item, queue->back->item);

	status = enqueue(&queue, "Mundo");
	if (status) error_handler(&queue, status, ENQUEUE);
	if (queue->front)
		printf("Front: %s | Back: %s\n", queue->front->item, queue->back->item);

	status = dequeue(&queue);
	if (status) error_handler(&queue, status, DEQUEUE);
	if (queue->front)
		printf("Front: %s | Back: %s\n", queue->front->item, queue->back->item);

	status = dequeue(&queue);
	if (status) error_handler(&queue, status, DEQUEUE);
	if (queue->front)
		printf("Front: %s | Back: %s\n", queue->front->item, queue->back->item);

	status = dequeue(&queue);
	if (status) error_handler(&queue, status, DEQUEUE);
	if (queue->front)
		printf("Front: %s | Back: %s\n", queue->front->item, queue->back->item);

	status = enqueue(&queue, "La");
	if (status) error_handler(&queue, status, ENQUEUE);
	if (queue->front)
		printf("Front: %s | Back: %s\n", queue->front->item, queue->back->item);

	status = enqueue(&queue, "Cola");
	if (status) error_handler(&queue, status, ENQUEUE);
	if (queue->front)
		printf("Front: %s | Back: %s\n", queue->front->item, queue->back->item);

	status = enqueue(&queue, "Funciona");
	if (status) error_handler(&queue, status, ENQUEUE);
	if (queue->front)
		printf("Front: %s | Back: %s\n", queue->front->item, queue->back->item);

	element = peek_queue(queue);
	if (!element) error_handler(&queue, status, PEEK_QUEUE);
	else printf("El primer elemento de la cola es: %s\n", element);

	status = dequeue(&queue);
	if (status) error_handler(&queue, status, DEQUEUE);
	if (queue->front)
		printf("Front: %s | Back: %s\n", queue->front->item, queue->back->item);

	element = peek_queue(queue);
	if (!element) error_handler(&queue, status, PEEK_QUEUE);
	else printf("El primer elemento de la cola es: %s\n", element);

	status = dequeue(&queue);
	if (status) error_handler(&queue, status, DEQUEUE);
	if (queue->front)
		printf("Front: %s | Back: %s\n", queue->front->item, queue->back->item);

	element = peek_queue(queue);
	if (!element) error_handler(&queue, status, PEEK_QUEUE);
	else printf("El primer elemento de la cola es: %s\n", element);

	status = dequeue(&queue);
	if (status) error_handler(&queue, status, DEQUEUE);
	if (queue->front)
		printf("Front: %s | Back: %s\n", queue->front->item, queue->back->item);

	element = peek_queue(queue);
	if (!element) error_handler(&queue, status, PEEK_QUEUE);
	else printf("El primer elemento de la cola es: %s\n", element);

	status = dequeue(&queue);
	if (status) error_handler(&queue, status, DEQUEUE);
	if (queue->front)
		printf("Front: %s | Back: %s\n", queue->front->item, queue->back->item);

	destroy_queue(&queue);
	return (0);
}

/* === 1 === */

/**
 * @brief Crea la pila
 *
 * @param item Elemento que se añadirá al nodo de la pila.
 * 
 * @return La pila creada.
 * @return NULL Si la falla la creación de la pila.
 *
 * @warning Utilizar la función destroy_stack al terminar de usar
 * la pila para evitar fugas de memoria.
 */
t_stack	*create_stack(const char *item)
{
	t_stack	*stack;

	stack = (t_stack *) malloc(sizeof(t_stack));
	if (!stack) return (NULL);
	stack->bottom = create_node(item);
	if (!stack->bottom)
	{
		free(stack);
		return (NULL);
	}
	stack->top = stack->bottom;
	return (stack);
}

/**
 * @brief Destruye la pila.
 *
 * @param stack Dirección de memoria de la pila.
 */
void	destroy_stack(t_stack **stack)
{
	t_node	*temp;

	if (!(*stack)) return;
	while ((*stack)->bottom)
	{
		temp = (*stack)->bottom->next;
		destroy_node(&(*stack)->bottom);
		(*stack)->bottom = temp;
	}
	free(*stack);
	*stack = NULL;
}

/**
 * @brief Añade un elemento al final de la pila.
 *
 * @param stack Dirección de memoria de la pila.
 * @param item El elemento que va a ser añadido.
 *
 * @return - 0 Si el elemento es añadido correctamente.
 * @return - > 0 Si falla el añadir un elemento.
 *
 * @attention El stack tiene que estar previamente inicializado,
 * ya sea a NULL o usando la función create_stack.
 *
 * @warning Utilizar la función destroy_stack al terminar de usar
 * la pila para evitar fugas de memoria.
 */
int	push(t_stack **stack, const char *item)
{
	static int	calls;

	++calls;
	printf("Push:		");
	if (!(*stack))
	{
		*stack = create_stack(item);
		if (!(*stack)) return (calls);
	}
	else if (!(*stack)->top)
	{
		(*stack)->top = create_node(item);
		if (!(*stack)) return (calls);
		(*stack)->bottom = (*stack)->top;
	}
	else
	{
		(*stack)->top->next = create_node(item);
		if (!(*stack)->top->next) return (calls);
		(*stack)->top = (*stack)->top->next;
	}
	return (0);
}

/**
 * @brief Elimina el último elemento de la pila.
 *
 * @param stack Dirección de memoria de la pila.
 *
 * @return - 0 Si el elemento es eliminado correctamente.
 * @return - > 0 Si no hay elemento que eliminar.
 */
int	pop(t_stack **stack)
{
	static int	calls;
	t_node		*temp;

	++calls;
	printf("Pop:		");
	if (!(*stack) || !(*stack)->top) return (calls);
	if (!(*stack)->bottom->next)
	{
		destroy_node(&(*stack)->bottom);
		(*stack)->top = NULL;
		return (0);
	}
	temp = (*stack)->bottom;
	while(temp->next && temp->next->next)
		temp = temp->next;
	(*stack)->top = temp;
	destroy_node(&temp->next);
	return (0);
}

/**
 * @brief Devuelve el último elemento de la pila.
 *
 * @param stack La pila.
 *
 * @return - NULL si no hay ningún elemento.
 * @return - El último elemento de la pila.
 */
char	*peek_stack(t_stack *stack)
{
	printf("Peek:		");
	if (!stack || !stack->top) return (NULL);
	return (stack->top->item);
}

/**
 * @brief Crea la cola 
 *
 * @param item Elemento que se añadirá al nodo de la cola.
 * 
 * @return La cola creada.
 * @return NULL Si la falla la creación de la cola.
 *
 * @warning Utilizar la función destroy_queue al terminar de usar
 * la pila para evitar fugas de memoria.
 */
t_queue	*create_queue(const char *item)
{
	t_queue	*queue;

	queue = (t_queue *) malloc(sizeof(t_queue));
	if (!queue) return (NULL);
	queue->back= create_node(item);
	if (!queue->back)
	{
		free(queue);
		return (NULL);
	}
	queue->front= queue->back;
	return (queue);
}

/**
 * @brief Destruye la cola.
 *
 * @param stack Dirección de memoria de la cola.
 */
void	destroy_queue(t_queue **queue)
{
	t_node	*temp;

	if (!(*queue)) return;
	while ((*queue)->front)
	{
		temp = (*queue)->front->next;
		destroy_node(&(*queue)->front);
		(*queue)->front = temp;
	}
	free(*queue);
	*queue = NULL;
}

/**
 * @brief Añade un elemento al inicio de la cola.
 *
 * @param queue Dirección de memoria de la cola.
 * @param item El elemento que va a ser añadido.
 *
 * @return - 0 Si el elemento es añadido correctamente.
 * @return - > 0 Si falla el añadir un elemento.
 *
 * @attention El stack tiene que estar previamente inicializado,
 * ya sea a NULL o usando la función create_queue.
 *
 * @warning Utilizar la función destroy_queue al terminar de usar
 * la pila para evitar fugas de memoria.
 */
int		enqueue(t_queue **queue, const char *item)
{
	static int	calls;

	++calls;
	printf("Enqueue:	");
	if (!(*queue))
	{
		*queue = create_queue(item);
		if (!(*queue)) return (calls);
	}
	else if (!(*queue)->front)
	{
		(*queue)->front = create_node(item);
		if (!(*queue)->front ) return (calls);
		(*queue)->back = (*queue)->front;
	}
	else
	{
		(*queue)->back->next = create_node(item);
		if (!(*queue)->back->next) return (calls);
		(*queue)->back = (*queue)->back->next;
	}
	return (0);
}

/**
 * @brief Elimina el primer elemento de la cola.
 *
 * @param queue Dirección de memoria de la cola.
 *
 * @return - 0 Si el elemento es eliminado correctamente.
 * @return - > 0 Si no hay elemento que eliminar.
 *
 */
int		dequeue(t_queue **queue)
{
	static int	calls;
	t_node		*temp;

	++calls;
	printf("Dequeue:	");
	if (!(*queue) || !(*queue)->front) return (calls);
	if (!(*queue)->front->next)
	{
		destroy_node(&(*queue)->back);
		(*queue)->front = NULL;
		return (calls);
	}
	temp = (*queue)->back;
	while(temp->next && temp->next->next)
		temp = temp->next;
	(*queue)->back = temp;
	temp = (*queue)->front;
	(*queue)->front = (*queue)->front->next;
	destroy_node(&temp);
	return (0);
}

/**
 * @brief Devuelve el primer elemento de la cola.
 *
 * @param queue La pila.
 *
 * @return - NULL si no hay ningún elemento.
 * @return - El último elemento de la cola.
 */
char	*peek_queue(t_queue *queue)
{
	printf("Peek:		");
	if (!queue || !queue->front) return (NULL);
	return (queue->front->item);
}
