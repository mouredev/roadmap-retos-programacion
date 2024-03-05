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

// Definición de macros

#define MAX_SIZE 2048

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

/* Declaración de funciones de los nodos */

t_node	*create_node(const char *item);
void	destroy_node(t_node **node);

// Manejo de errores

int		error_handler(void *address, int status, t_function name);

// Utils

void	ft_print(t_node *first, t_node *last, t_function name);

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

// Estructura del navegador web

typedef struct s_web
{
	t_stack	*history;
	t_stack	*temp;
	char	input[MAX_SIZE];
	int		flag;
	int		home_counter;
}				t_web;

// Navegador web

int		web_browser(void);
void	web_browser_menu(t_web **web);
int		web_browser_navigate(t_web **web);
int		web_browser_previous(t_web **web);
int		web_browser_forward(t_web **web);

typedef struct s_printer
{
	t_queue	*queue;
	char	input[MAX_SIZE];
}				t_printer;

// Impresora

int		printer(void);
void	printer_menu(void);
int		printer_add(t_printer **printer);
int		printer_remove(t_printer **printer);
int		printer_print(t_printer **printer);

int	main(void)
{
	int	status;

	printf("========== INICIO STACK ==========\n\n");
	status = test_stack();
	if (status) return (status);
	printf("========== FIN STACK ==========\n");
	printf("\n");
	printf("========== INICIO QUEUE ==========\n\n");
	status = test_queue();
	if (status) return (status);
	printf("========== FIN QUEUE ==========\n");
	status = web_browser();
	if (status) return (status);
	status = printer();
	if (status) return (status);
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
 * @param name Nombre de la función.
 *
 * @return - status Devuelve el parámetro status.
 */
int	error_handler(void *address, int status, t_function name)
{
	if (name == POP || name == PEEK_STACK) printf("La pila está vacía\n\n");
	else if (name == DEQUEUE || name == PEEK_QUEUE) printf("La cola está vacía\n\n");
	else if (name == PUSH)
	{
		printf("Error añadiendo el elemento a la pila, llamada %d\n", status);
		destroy_stack((t_stack **) address);
	}
	else if (name == ENQUEUE)
	{
		printf("Error añadiendo el elemento a la cola, llamada %d\n", status);
		destroy_queue((t_queue **) address);
	}
	return (status);
}

/**
 * @brief Mensaje personalizado para pilas y colas
 *
 * @param first Nodo al primer elemento.
 * @param last Nodo al último elemento.
 * @param name Nombre de la función.
 */
void	ft_print(t_node *first, t_node *last, t_function name)
{
	if (!first || !last) return ;
	if (name == PUSH || name == POP)
		printf("Bottom: %s | Top: %s\n\n", first->item, last->item);
	else if (name == ENQUEUE || name == DEQUEUE)
		printf("Front: %s | Back: %s\n\n", first->item, last->item);
}

/**
 * @brief Test de funciones de la pila.
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
	printf("Push:\n");
	if (status) return (error_handler(&stack, status, PUSH));
	if (stack->bottom) ft_print(stack->bottom, stack->top, PUSH);

	status = push(&stack, "Mundo");
	printf("Push:\n");
	if (status) return (error_handler(&stack, status, PUSH));
	if (stack->bottom) ft_print(stack->bottom, stack->top, PUSH);

	status = pop(&stack);
	printf("Pop:\n");
	if (status) error_handler(&stack, status, POP);
	if (stack->bottom) ft_print(stack->bottom, stack->top, POP);

	status = pop(&stack);
	printf("Pop:\n");
	if (status) error_handler(&stack, status, POP);
	if (stack->bottom) ft_print(stack->bottom, stack->top, POP);

	status = pop(&stack);
	printf("Pop:\n");
	if (status) error_handler(&stack, status, POP);
	if (stack->bottom) ft_print(stack->bottom, stack->top, POP);

	status = push(&stack, "La");
	printf("Push:\n");
	if (status) return (error_handler(&stack, status, PUSH));
	if (stack->bottom) ft_print(stack->bottom, stack->top, PUSH);

	status = push(&stack, "Pila");
	printf("Push:\n");
	if (status) return (error_handler(&stack, status, PUSH));
	if (stack->bottom) ft_print(stack->bottom, stack->top, PUSH);

	status = push(&stack, "Funciona");
	printf("Push:\n");
	if (status) return (error_handler(&stack, status, PUSH));
	if (stack->bottom) ft_print(stack->bottom, stack->top, PUSH);

	element = peek_stack(stack);
	printf("Peek_stack:\n");
	if (!element) error_handler(&stack, status, PEEK_STACK);
	else printf("El último elemento de la pila es: %s\n\n", element);

	status = pop(&stack);
	printf("Pop:\n");
	if (status) error_handler(&stack, status, POP);
	if (stack->bottom) ft_print(stack->bottom, stack->top, POP);

	element = peek_stack(stack);
	printf("Peek_stack:\n");
	if (!element) error_handler(&stack, status, PEEK_STACK);
	else printf("El último elemento de la pila es: %s\n\n", element);

	status = pop(&stack);
	printf("Pop:\n");
	if (status) error_handler(&stack, status, POP);
	if (stack->bottom) ft_print(stack->bottom, stack->top, POP);

	element = peek_stack(stack);
	printf("Peek_stack:\n");
	if (!element) error_handler(&stack, status, PEEK_STACK);
	else printf("El último elemento de la pila es: %s\n\n", element);

	status = pop(&stack);
	printf("Pop:\n");
	if (status) error_handler(&stack, status, POP);
	if (stack->bottom) ft_print(stack->bottom, stack->top, POP);

	element = peek_stack(stack);
	printf("Peek_stack:\n");
	if (!element) error_handler(&stack, status, PEEK_STACK);
	else printf("El último elemento de la pila es: %s\n\n", element);

	status = pop(&stack);
	printf("Pop:\n");
	if (status) error_handler(&stack, status, POP);
	if (stack->bottom) ft_print(stack->bottom, stack->top, POP);

	element = peek_stack(stack);
	printf("Peek_stack:\n");
	if (!element) error_handler(&stack, status, PEEK_STACK);
	else printf("El último elemento de la pila es: %s\n\n", element);

	destroy_stack(&stack);
	return (0);
}

/**
 * @brief Test de funciones de la cola.
 *
 * @return - > 0 Si hay algún error grave.
 * @return - 0 Si el test se ejecuta correctamente.
 */
int		test_queue(void)
{
	t_queue	*queue;
	int		status;
	char	*element;

	queue = NULL;

	status = enqueue(&queue, "Hola");
	printf("Enqueue:\n");
	if (status) error_handler(&queue, status, ENQUEUE);
	if (queue->front) ft_print(queue->front, queue->back, ENQUEUE);

	status = enqueue(&queue, "Mundo");
	printf("Enqueue:\n");
	if (status) error_handler(&queue, status, ENQUEUE);
	if (queue->front) ft_print(queue->front, queue->back, ENQUEUE);

	status = dequeue(&queue);
	printf("Dequeue:\n");
	if (status) error_handler(&queue, status, DEQUEUE);
	if (queue->front) ft_print(queue->front, queue->back, DEQUEUE);

	status = dequeue(&queue);
	printf("Dequeue:\n");
	if (status) error_handler(&queue, status, DEQUEUE);
	if (queue->front) ft_print(queue->front, queue->back, DEQUEUE);

	status = dequeue(&queue);
	printf("Dequeue:\n");
	if (status) error_handler(&queue, status, DEQUEUE);
	if (queue->front) ft_print(queue->front, queue->back, DEQUEUE);

	status = enqueue(&queue, "La");
	printf("Enqueue:\n");
	if (status) error_handler(&queue, status, ENQUEUE);
	if (queue->front) ft_print(queue->front, queue->back, ENQUEUE);

	status = enqueue(&queue, "Cola");
	printf("Enqueue:\n");
	if (status) error_handler(&queue, status, ENQUEUE);
	if (queue->front) ft_print(queue->front, queue->back, ENQUEUE);

	status = enqueue(&queue, "Funciona");
	printf("Enqueue:\n");
	if (status) error_handler(&queue, status, ENQUEUE);
	if (queue->front) ft_print(queue->front, queue->back, ENQUEUE);

	element = peek_queue(queue);
	printf("Peek_queue:\n");
	if (!element) error_handler(&queue, status, PEEK_QUEUE);
	else printf("El primer elemento de la cola es: %s\n\n", element);

	status = dequeue(&queue);
	printf("Dequeue:\n");
	if (status) error_handler(&queue, status, DEQUEUE);
	if (queue->front) ft_print(queue->front, queue->back, DEQUEUE);

	element = peek_queue(queue);
	printf("Peek_queue:\n");
	if (!element) error_handler(&queue, status, PEEK_QUEUE);
	else printf("El primer elemento de la cola es: %s\n\n", element);

	status = dequeue(&queue);
	if (status) error_handler(&queue, status, DEQUEUE);
	if (queue->front) ft_print(queue->front, queue->back, DEQUEUE);

	element = peek_queue(queue);
	printf("Peek_queue:\n");
	if (!element) error_handler(&queue, status, PEEK_QUEUE);
	else printf("El primer elemento de la cola es: %s\n\n", element);

	status = dequeue(&queue);
	printf("Dequeue:\n");
	if (status) error_handler(&queue, status, DEQUEUE);
	if (queue->front) ft_print(queue->front, queue->back, DEQUEUE);

	element = peek_queue(queue);
	printf("Peek_queue:\n");
	if (!element) error_handler(&queue, status, PEEK_QUEUE);
	else printf("El primer elemento de la cola es: %s\n\n", element);

	status = dequeue(&queue);
	printf("Dequeue:\n");
	if (status) error_handler(&queue, status, DEQUEUE);
	if (queue->front) ft_print(queue->front, queue->back, DEQUEUE);

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
	queue->back = create_node(item);
	if (!queue->back)
	{
		free(queue);
		return (NULL);
	}
	queue->front = queue->back;
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
	if (!(*queue) || !(*queue)->front) return (calls);
	if (!(*queue)->front->next)
	{
		destroy_node(&(*queue)->back);
		(*queue)->front = NULL;
		return (0);
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
 * @return - El primer elemento de la cola.
 */
char	*peek_queue(t_queue *queue)
{
	if (!queue || !queue->front) return (NULL);
	return (queue->front->item);
}

/* === DIFICULTAD EXTRA === */

/**
 * @brief Simulación de un navegador web.
 *
 * @return - 0 Si se ha ejecutado correctamente.
 * @return - != 0 Si ha habido un error grave.
 */
int	web_browser(void)
{
	int		status;
	t_web	*web;

	status = 0;
	web = (t_web *)malloc(sizeof(t_web));
	if (!web) return (-1);
	web->history = create_stack("Inicio");
	if (!web->history)
	{
		free(web);
		return (-2);
	}
	web->temp = NULL;
	web->flag = -1;
	web->home_counter = 0;
	while (status <= 0)
	{
		web_browser_menu(&web);
		if (!fgets(web->input, MAX_SIZE, stdin))
		{
			status = -3;
			break;
		}
		web->input[strlen(web->input) - 1] = '\0';
		if (!strcmp(web->input, "Atrás") || !strcmp(web->input, "atrás")
				|| !strcmp(web->input, "Atras") || !strcmp(web->input, "atras")
				|| !strcmp(web->input, "<-"))
			status = web_browser_previous(&web);
		else if (!strcmp(web->input, "Adelante") || !strcmp(web->input, "adelante")
				|| !strcmp(web->input, "->"))
			status = web_browser_forward(&web);
		else if (!strcmp(web->input, "Salir") || !strcmp(web->input, "salir")
				|| !strcmp(web->input, "X") || !strcmp(web->input, "x"))
		{
			printf("Has cerrado el navegador\n\n\n");
			status = 0;
			break;
		}
		else
			status = web_browser_navigate(&web);
		printf("\n\n");
	}
	destroy_stack(&web->history);
	destroy_stack(&web->temp);
	free(web);
	return (status);
}

/**
 * @brief Menú del navegador web
 *
 * @param web Dirección de memoria de la web.
 */
void	web_browser_menu(t_web **web)
{
	printf("Buscador Variable    ");
	for (size_t i = 0; i < strlen(peek_stack((*web)->history)); ++i)
		printf(" ");
	printf("- o x\n");
	printf("===========================");
	for (size_t i = 0; i < strlen(peek_stack((*web)->history)); ++i)
		printf("=");
	printf("\n| <-  -> |    %s    |       |\n", (*web)->history->top->item);
	printf("===========================");
	for (size_t i = 0; i < strlen(peek_stack((*web)->history)); ++i)
		printf("=");
	printf("\n");
	printf("Introduce:\n");
	printf("- El enlace una página web, para navegar hacia ella\n");
	printf("- Adelante, para avanzar en el historial\n");
	printf("- Atrás, para retroceder en el historial\n");
	printf("- Salir, para cerrar el navegador\n");
	printf(">> ");
}

/**
 * @brief Navega hacia un enlace.
 *
 * @param web Dirección de memoria
 *
 * @return - 0 Si la navegación es exitosa.
 * @return - > 0 Si ha habido un problema navegando.
 */
int		web_browser_navigate(t_web	**web)
{
	int	status;

	status = push(&(*web)->history, (*web)->input);
	if (status) printf("Error navegando a %s\n", (*web)->input);
	if ((*web)->flag == 1)
		destroy_stack(&(*web)->temp);
	(*web)->flag = 0;
	if (!strcmp(peek_stack((*web)->history), "Inicio"))
		(*web)->home_counter++;
	return (status);
}

/**
 * @brief Navega una página hacia atrás.
 *
 * @param web Dirección de memoria de la web.
 *
 * @return - 0 Si la navegación es exitosa.
 * @return - != 0  Si ha habido un problema navegando.
 */
int		web_browser_previous(t_web **web)
{
	int	status;

	if (!strcmp(peek_stack((*web)->history), "Inicio") && !(*web)->home_counter)
	{
		printf("Has llegado al límite, no puedes retroceder\n");
		return (-1);
	}
	else if (!strcmp(peek_stack((*web)->history), "Inicio"))
		(*web)->home_counter--;
	status = push(&(*web)->temp, peek_stack((*web)->history));
	if (status) printf("Error retrocediendo\n");
	pop(&(*web)->history);
	(*web)->flag = 1;
	return (0);
}

/**
 * @brief Navega una página hacia adelante.
 *
 * @param web Dirección de memoria de la web.
 *
 * @return - 0 Si la navegación es exitosa.
 * @return - != 0  Si ha habido un problema navegando.
 */
int		web_browser_forward(t_web **web)
{
	int		status;
	char	*link;

	if (!(*web)->temp || !(*web)->temp->top)
	{
		printf("Has llegado al límite, no puedes avanzar\n");
		return (-1);
	}
	if (!strcmp(peek_stack((*web)->temp), "Inicio"))
		(*web)->home_counter++;
	link = peek_stack((*web)->temp);
	status = push(&(*web)->history, link);
	pop(&(*web)->temp);
	return (status);
}

/**
 * @brief Simulación del comportamiento de una impresora.
 *
 * @return - 0 Si se ha ejecutado correctamente.
 * @return - != 0 Si ha habido un error grave.
 */
int		printer(void)
{
	int			status;
	t_printer	*printer;

	status = 0;
	printer = (t_printer *) malloc(sizeof(t_printer));
	if (!printer) return (-1);
	printer->queue = NULL;
	while (status <= 0)
	{
		printer_menu();
		if (!fgets(printer->input, sizeof(printer->input), stdin))
		{
			status = -2;
			break;
		}
		printer->input[strlen(printer->input) - 1] = '\0';
		if (!strcmp(printer->input, "Imprimir")
				|| !strcmp(printer->input, "imprimir"))
			status = printer_print(&printer);
		else if (!strcmp(printer->input, "Eliminar")
				|| !strcmp(printer->input, "eliminar"))
			status = printer_remove(&printer);
		else if (!strcmp(printer->input, "Fin")
				|| !strcmp(printer->input, "fin"))
		{
			printf("Apagando impresora...\n");
			status = 0;
			break;
		}
		else
			status = printer_add(&printer);
		printf("\n\n");
	}
	destroy_queue(&printer->queue);
	free(printer);
	return (status);
}

/**
 * @brief Menú de la impresora.
 */
void	printer_menu(void)
{
	printf("========== IMPRESORA ==========\n");
	printf("Introduce:\n");
	printf("- El nombre del documento, para añadirlo a la cola\n");
	printf("- Imprimir, para imprimir el primer documento en la cola\n");
	printf("- Eliminar, para eliminar el primer documento de la cola\n");
	printf("- Fin, para terminar de imprimir\n");
	printf(">> ");
}

/**
 * @brief Añade un documento a la cola.
 *
 * @param printer Dirección de memoria de la impresora.
 *
 * @return - 0 Si se añade correctamente.
 * @return - > 0 Si ha habido un problema.
 */
int	printer_add(t_printer **printer)
{
	int	status;

	status = enqueue(&(*printer)->queue, (*printer)->input);
	if (!status)
		printf("Se ha añadido %s a la cola\n", (*printer)->queue->back->item);
	return (status);
}

/**
 * @brief Imprime el primer elemento en la cola.
 *
 * @param printer Dirección de memoria de la impresora.
 *
 * @return - 0 Si imprime correctamente. 
 * @return - != 0 Si no imprime.
 */
int	printer_print(t_printer **printer)
{
	int		status;
	char	document[MAX_SIZE];

	if (!(*printer)->queue || !(*printer)->queue->front)
	{
		printf("No hay nada que imprimir\n");
		return (-1);
	}
	strcpy(document, (*printer)->queue->front->item);
	status = dequeue(&(*printer)->queue);
	if (status) return (status);
	printf("Se ha imprimido %s correctamente\n", document);
	return (0);
}

/**
 * @brief Elimina el último documento añadido.
 *
 * @param printer Dirección de memoria de la impresora.
 *
 * @return - 0 Si se elimina correctamente.
 * @return - != 0 Si no se elimina.
 */
int	printer_remove(t_printer **printer)
{
	char	document[MAX_SIZE];
	t_node	*temp;

	if (!(*printer)->queue || !(*printer)->queue->front)
	{
		printf("No hay nada en cola\n");
		return (-1);
	}
	strcpy(document, (*printer)->queue->back->item);
	temp = (*printer)->queue->front;
	if (temp == (*printer)->queue->back) destroy_queue(&(*printer)->queue);
	else
	{
		while (temp && temp->next != (*printer)->queue->back)
			temp = temp->next;
		temp->next = NULL;
		destroy_node(&(*printer)->queue->back);
		(*printer)->queue->back = temp;
	}
	printf("Se ha eliminado %s correctamente\n", document);
	return (0);
}
