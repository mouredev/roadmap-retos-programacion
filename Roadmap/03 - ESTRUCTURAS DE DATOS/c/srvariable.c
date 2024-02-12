/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
 */

#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

/*! Declaración de estructuras y funciones !*/
 
/* Lista enlazada simple */

// Estructura

typedef struct s_linked_list
{
    int                     data;
    struct s_linked_list    *next;
}                           t_linked_list;

// Operaciones

t_linked_list   *ll_create_node(int data);
int             ll_insert_node_beginning(t_linked_list **ll, int data);
int             ll_insert_node_end(t_linked_list **ll, int data);
int             ll_insert_node_nth_position(t_linked_list **ll, int data, int position);
void            ll_delete(t_linked_list **ll);
int             ll_delete_first_node(t_linked_list **ll);
int             ll_delete_last_node(t_linked_list **ll);
int             ll_delete_nth_node(t_linked_list **ll, int position);
int             ll_update_node(t_linked_list **ll, int new_data, int position);
t_linked_list   *ll_find_data(t_linked_list *ll, int data);
void            ll_sort(t_linked_list **ll);
void            ll_print(t_linked_list *ll);
int             ll_length(t_linked_list *ll);

/* Lista doblemente enlazada */

// Estructura

typedef struct s_doubly_linked_list
{
    int                         data;
    struct s_doubly_linked_list *previous;
    struct s_doubly_linked_list *next;
}                               t_doubly_linked_list;

// Operaciones

t_doubly_linked_list    *dll_create_node(int data);
int                     dll_insert_node_beginning(t_doubly_linked_list **dll, int data);
int                     dll_insert_node_end(t_doubly_linked_list **ll, int data);
int                     dll_insert_node_nth_position(t_doubly_linked_list **dll, int data, int position);
int                     dll_delete(t_doubly_linked_list **dll);
int                     dll_delete_first_node(t_doubly_linked_list **dll);
int                     dll_delete_last_node(t_doubly_linked_list **dll);
int                     dll_delete_nth_node(t_doubly_linked_list **dll, int position);
int                     dll_update_node(t_doubly_linked_list **dll, int new_data, int position);
t_doubly_linked_list    *dll_find_data(t_doubly_linked_list *dll, int data);
void                    dll_sort(t_doubly_linked_list **dll);
void                    dll_print(t_doubly_linked_list *dll);
int                     dll_length(t_doubly_linked_list *dll);

/* DIFICULTAD EXTRA */

// Estructura

typedef struct s_contact
{
    char                name[50];
    unsigned long long  phone_number;
    struct s_contact    *previous;
    struct s_contact    *next;
}                       t_contact;

// Funciones

int                     contact_list(void);
t_contact               *create_contact_list(void);
void                    display_menu(void);
void                    handle_option(int option, t_contact **contact);
void                    add_contact(t_contact **contact);
void                    update_contact(t_contact **contact);
t_contact               *search_contact(t_contact *contact, unsigned long long phone_number);
void                    delete_contact(t_contact **contact);
void                    display_contacts(t_contact *contact);
void                    delete_contact_list(t_contact **contact);

// Programa principal

int main(void)
{

    /* === 1 === */
    /* Array */
    int array[10] = {8, 5, 2, 1, 9, 125, 3892, -1, 12893, -9592};

    /* Lista enlazada simple */
    t_linked_list *ll = ll_create_node(array[0]);
    if (!ll)
        return (1);

    /* Lista doblemente enlazada */
    t_doubly_linked_list *dll = dll_create_node(array[0]);
    if (!dll)
        return (2);

    /* === 2 === */
    /* Array */
    // Obtener el tamaño
    int size = sizeof(array) / sizeof(array[0]);

    // Modificar el valor
    array[5] = 82319;

    /* Lista enlazada simple*/
    int i = 1;
    for (i; i < 4; i++)
        // Inserta un nodo al principio
        ll_insert_node_beginning(&ll, array[i]);

    for (i; i < size; i++)
        // Inserta un nodo al final
        ll_insert_node_end(&ll, array[i]);

    // Insertar nodo en una posición en concreto
    ll_insert_node_nth_position(&ll, array[3], 3);

    // Elimina el primer nodo
    ll_delete_first_node(&ll);

    // Elimina el último nodo
    ll_delete_last_node(&ll);

    // Elimina un nodo
    ll_delete_nth_node(&ll, 4);

    // Actualiza un elemento
    ll_update_node(&ll, 2024, 7);

    // Busca un elemento
    if (ll_find_data(ll, 2024))
        printf("Lo he encontrado\n");
    else
        printf("No lo he encontrado\n");

    // Imprime el número de nodos
    printf("Hay %d nodos en la lista enlazada simple\n", ll_length(ll));

    // Imprime la lista enlazada
    printf("*****************\n");
    printf("Sin ordenar\n");
    ll_print(ll);
    printf("*****************\n");

    // Ordena la lista enlazada
    ll_sort(&ll);
    printf("*****************\n");
    printf("Ordenado\n");
    ll_print(ll);
    printf("*****************\n");

    // Elimina completamente la lista enlazada simple
    ll_delete(&ll);

    /* Lista doblemente enlazada */
    i = 1;
    for (i; i < 4; i++)
        // Insertar un nodo al principio
        dll_insert_node_beginning(&dll, array[i]);

    for (i; i < size; i++)
        // Inserta un nodo al final
        dll_insert_node_end(&dll, array[i]);

    // Inserta un nodo en una posición en concreto
    dll_insert_node_nth_position(&dll, array[9], 9);

    // Elimina el primer nodo
    dll_delete_first_node(&dll);

    // Elimina el último nodo
    dll_delete_last_node(&dll);

    // Elimina un nodo
    dll_delete_nth_node(&dll, 1);

    // Actualiza un elemento
    dll_update_node(&dll, 213498, 0);

    // Busca un elemento
    if (dll_find_data(dll, 21474836))
        printf("Lo he encontrado\n");
    else
        printf("No lo he encontrado\n");
    printf("Hay %d nodos en la lista doblemente enlazada\n", dll_length(dll));

    // Imprime la lista doblemente enlazada
    printf("*****************\n");
    printf("Sin ordenar\n");
    dll_print(dll);
    printf("*****************\n");

    // Ordena la lista doblemente enlazada
    dll_sort(&dll);
    printf("*****************\n");
    printf("Ordenado\n");
    dll_print(dll);
    printf("*****************\n");

    // Elimina completamente la lista doblemente enlazada
    dll_delete(&dll);
    /* DIFICULTAD EXTRA */
    if (contact_list() < 0)
        return (-1);
    return (0);
}

/*! Definición de funciones !*/

/* Lista enlazada simple */

t_linked_list   *ll_create_node(int data)
{
    t_linked_list   *ll;

    ll = (t_linked_list *)malloc(sizeof(t_linked_list));
    if (!ll)
    {
        fprintf(stderr, "Error: creando lista enlazada\n");
        return (NULL);
    }
    ll->data = data;
    ll->next = NULL;
    return (ll);
}

int ll_insert_node_beginning(t_linked_list **ll, int data)
{
    t_linked_list   *node;

    if (!(*ll))
    {
        fprintf(stderr, "Error: lista enlazada nula\n");
        return (-1);
    }
    node = (t_linked_list *)malloc(sizeof(t_linked_list));
    if (!node)
    {
        fprintf(stderr, "Error: añadiendo nodo al principio de la lista enlazada\n");
        return (-1);
    }
    node->data = data;
    node->next = *ll;
    *ll = node;
    return (0);
}

int ll_insert_node_end(t_linked_list **ll, int data)
{
    t_linked_list   *node;
    t_linked_list   *temp;

    if (!(*ll))
    {
        fprintf(stderr, "Error: lista enlazada nula\n");
        return (-1);
    }
    node = (t_linked_list *)malloc(sizeof(t_linked_list));
    if (!node)
    {
        fprintf(stderr, "Error: añadiendo nodo al final de la lista enlazada\n");
        return (-1);
    }
    node->data = data;
    node->next = NULL;
    temp = *ll;
    while (temp->next)
        temp = temp->next;
    temp->next = node;
    return (0);
}

int ll_insert_node_nth_position(t_linked_list **ll, int data, int position)
{
    t_linked_list   *node;
    t_linked_list   *temp;

    if (!(*ll))
    {
        fprintf(stderr, "Error: lista enlazada nula\n");
        return (-1);
    }
    if (position < 0 || position > ll_length(*ll))
    {
        fprintf(stderr, "Error: posición inválida\n");
        return (-1);
    }
    if (position == 0)
        ll_insert_node_beginning(ll, data);
    else if (position == ll_length(*ll))
        ll_insert_node_end(ll, data);
    else
    {
        node = (t_linked_list *)malloc(sizeof(t_linked_list));
        if (!node)
        {
            fprintf(stderr, "Error: añadiendo nodo en la posición %d de la lista enlazada\n", position);
            return (-1);
        }
        temp = *ll;
        while (position-- > 1)
            temp = temp->next;
        node->data = data;
        node->next = temp->next;
        temp->next = node;
    }
    return (0);
}

void    ll_delete(t_linked_list **ll)
{
    t_linked_list   *temp;

    while (*ll)
    {
        temp = (*ll)->next;
        free(*ll);
        *ll = temp;
    }
    *ll = NULL;
}

int ll_delete_first_node(t_linked_list **ll)
{
    t_linked_list   *temp;

    if (!(*ll))
    {
        fprintf(stderr, "Error: lista enlazada nula\n");
        return (-1);
    }
    temp = (*ll)->next;
    free(*ll);
    *ll = temp;
    return (0);
}

int ll_delete_last_node(t_linked_list **ll)
{
    t_linked_list   *temp;
    t_linked_list   *penultimate;

    if (!(*ll))
    {
        fprintf(stderr, "Error: lista enlazada nula\n");
        return (-1);
    }
    temp = *ll;
    penultimate = NULL;
    while (temp->next)
    {
        penultimate = temp;
        temp = temp->next;
    }
    if (!penultimate)
    {
        free(*ll);
        *ll = NULL;
    }
    else
    {
        free(temp);
        penultimate->next = NULL;
    }
    return (0);
}

int ll_delete_nth_node(t_linked_list **ll, int position)
{
    t_linked_list   *temp;
    t_linked_list   *previous;

    if (!(*ll))
    {
        fprintf(stderr, "Error: lista enlazada nula\n");
        return (-1);
    }
    if (position < 0 || position >= ll_length(*ll))
    {
        fprintf(stderr, "Error: posición inválida\n");
        return (-1);
    }
    if (position == 0)
        ll_delete_first_node(ll);
    else if (position == ll_length(*ll))
        ll_delete_last_node(ll);
    else
    {
        temp = *ll;
        while (position-- > 0)
        {
            previous = temp;
            temp = temp->next;
        }
        previous->next = temp->next;
        free(temp);
    }
    return (0);
}

int ll_update_node(t_linked_list **ll, int new_data, int position)
{
    t_linked_list   *temp;

    if (!(*ll))
    {
        fprintf(stderr, "Error: lista enlazada nula\n");
        return (-1);
    }
    if (position < 0 || position >= ll_length(*ll))
    {
        fprintf(stderr, "Error: posición inválida\n");
        return (-1);
    }
    temp = *ll;
    while (position-- > 0)
        temp = temp->next;
    temp->data = new_data;
    return (0);
}

void    ll_print(t_linked_list *ll)
{
    if (!ll)
    {
        fprintf(stderr, "Error: lista enlazada nula\n");
        return ;
    }
    while (ll)
    {
        printf("%d\n", ll->data);
        ll = ll->next;
    }
}

t_linked_list   *ll_find_data(t_linked_list *ll, int data)
{
    t_linked_list   *temp;

    if (!ll)
    {
        fprintf(stderr, "Error: lista enlazada nula\n");
        return (NULL);
    }
    temp = ll;
    while (temp)
    {
        if (temp->data == data)
            return (temp);
        temp = temp->next;
    }
    return (NULL);
}

void    ll_sort(t_linked_list **ll)
{
    int             temp_data;
    bool            is_swapped;
    t_linked_list   *temp;

    if (!(*ll))
    {
        fprintf(stderr, "Error: lista enlazada nula\n");
        return ;
    }
    is_swapped = false;
    while (!is_swapped)
    {
        is_swapped = true;
        temp = *ll;
        while (temp->next != NULL)
        {
            if (temp->data > temp->next->data)
            {
                temp_data = temp->data;
                temp->data = temp->next->data;
                temp->next->data = temp_data;
                is_swapped = false;
            }
            temp = temp->next;
        }
    }
}

int ll_length(t_linked_list *ll)
{
    t_linked_list   *temp;
    int             counter;

    if (!ll)
    {
        fprintf(stderr, "Error: lista enlazada nula\n");
        return (0);
    }
    temp = ll;
    counter = 0;
    while (temp)
    {
        counter++;
        temp = temp->next;
    }
    return (counter);
}

/* Lista doblemente enlazada */

t_doubly_linked_list    *dll_create_node(int data)
{
    t_doubly_linked_list    *dll;

    dll = (t_doubly_linked_list *)malloc(sizeof(t_doubly_linked_list));
    if (!dll)
    {
        fprintf(stderr, "Error: creando lista doblemente enlazada\n");
        return (NULL);
    }
    dll->data = data;
    dll->previous = NULL;
    dll->next = NULL;
    return (dll);
}

int dll_insert_node_beginning(t_doubly_linked_list **dll, int data)
{
    t_doubly_linked_list    *node;
    t_doubly_linked_list    *temp;

    if (!(*dll))
    {
        fprintf(stderr, "Error: lista doblemente enlazada nula\n");
        return (-1);
    }
    node = (t_doubly_linked_list *)malloc(sizeof(t_doubly_linked_list));
    if (!node)
    {
        fprintf(stderr, "Error: añadiendo nodo al principio de la lista doblemente enlazada\n");
        return (-1);
    }
    temp = *dll;
    while (temp->previous)
        temp = temp->previous;
    node->data = data;
    node->previous = NULL;
    node->next = temp;
    temp->previous = node;
    *dll = node;
    return (0);
}

int dll_insert_node_end(t_doubly_linked_list **dll, int data)
{
    t_doubly_linked_list    *node;
    t_doubly_linked_list    *temp;

    if (!(*dll))
    {
        fprintf(stderr, "Error: lista doblemente enlazada nula\n");
        return (-1);
    }
    node = (t_doubly_linked_list *)malloc(sizeof(t_doubly_linked_list));
    if (!node)
    {
        fprintf(stderr, "Error: añadiendo nodo al final de la lista doblemente enlazada\n");
        return (-1);
    }
    node->data = data;
    node->next = NULL;
    temp = *dll;
    while (temp->next)
        temp = temp->next;
    node->previous = temp;
    temp->next = node;
    return (0);
}

int dll_insert_node_nth_position(t_doubly_linked_list **dll, int data, int position)
{
    t_doubly_linked_list    *node;
    t_doubly_linked_list    *temp;

    if (!(*dll))
    {
        fprintf(stderr, "Error: lista doblemente enlazada nula\n");
        return (-1);
    }
    if (position < 0 || position > dll_length(*dll))
    {
        fprintf(stderr, "Error: posición inválida\n");
        return (-1);
    }
    if (position == 0)
        dll_insert_node_beginning(dll, data);
    else if (position == dll_length(*dll))
        dll_insert_node_end(dll, data);
    else
    {
        node = (t_doubly_linked_list *)malloc(sizeof(t_doubly_linked_list));
        if (!node)
        {
            fprintf(stderr, "Error: añadiendo nodo en la posición %d de la lista doblemente enlazada\n", position);
            return (-1);
        }
        temp = *dll;
        while (position-- > 1)
            temp = temp->next;
        node->data = data;
        node->previous = temp;
        node->next = temp->next;
        temp->next->previous = node;
        temp->next = node;
    }
    return (0);
}

int dll_delete(t_doubly_linked_list **dll)
{
    t_doubly_linked_list    *temp;
    t_doubly_linked_list    *temp2;

    if (!(*dll))
    {
        fprintf(stderr, "Error: lista doblemente enlazada nula\n");
        return (-1);
    }
    temp2 = (*dll)->next;
    while (*dll)
    {
        temp = (*dll)->previous;
        free(*dll);
        *dll = temp;
    }
    while (temp2)
    {
        *dll = temp2;
        temp2 = temp2->next;
        free(*dll);
    }
    *dll = NULL;
    return (0);
}

int dll_delete_first_node(t_doubly_linked_list **dll)
{
    t_doubly_linked_list    *temp;

    if (!(*dll))
    {
        fprintf(stderr, "Error: lista doblemente enlazada nula\n");
        return (-1);
    }
    temp = (*dll)->next;
    free(*dll);
    if (temp)
        temp->previous = NULL;
    *dll = temp;
}

int dll_delete_last_node(t_doubly_linked_list **dll)
{
    t_doubly_linked_list    *temp;
    t_doubly_linked_list    *penultimate;

    if (!(*dll))
    {
        fprintf(stderr, "Error: lista doblemente enlazada nula\n");
        return (-1);
    }
    temp = *dll;
    penultimate = NULL;
    while (temp->next)
    {
        penultimate = temp;
        temp = temp->next;
    }
    if (!penultimate)
    {
        free(*dll);
        *dll = NULL;
    }
    else
    {
        free(temp);
        penultimate->next = NULL;
    }
    return (0);
}

int dll_delete_nth_node(t_doubly_linked_list **dll, int position)
{
    t_doubly_linked_list    *temp;
    t_doubly_linked_list    *previous;

    if (!(*dll))
    {
        fprintf(stderr, "Error: lista doblemente enlazada nula\n");
        return (-1);
    }
    if (position < 0 || position >= dll_length(*dll))
    {
        fprintf(stderr, "Error: posición inválida\n");
        return (-1);
    }
    if (position == 0)
        dll_delete_first_node(dll);
    else if (position == dll_length(*dll))
        dll_delete_last_node(dll);
    else
    {
        temp = *dll;
        while (position-- > 0)
        {
            previous = temp;
            temp = temp->next;
        }
        previous->next = temp->next;
        temp->next = previous;
        free(temp);
    }
    return (0);
}

int dll_update_node(t_doubly_linked_list **dll, int new_data, int position)
{
    t_doubly_linked_list    *temp;

    if (!(*dll))
    {
        fprintf(stderr, "Error: lista doblemente enlazada nula\n");
        return (-1);
    }
    if (position < 0 || position >= dll_length(*dll))
    {
        fprintf(stderr, "Error: posición invalida\n");
        return (-1);
    }
    temp = *dll;
    while (position-- > 0)
        temp = temp->next;
    temp->data = new_data;
    return (0);
}

int dll_length(t_doubly_linked_list *dll)
{
    t_doubly_linked_list    *temp;
    int                     counter;

    if (!dll)
    {
        fprintf(stderr, "Error: lista doblemente enlazada nula\n");
        return (0);
    }
    temp = dll;
    counter = 0;
    while (temp)
    {
        counter++;
        temp = temp->next;
    }
    temp = dll->previous;
    while (temp)
    {
        counter++;
        temp = temp->next;
    }
    return (counter);
}

t_doubly_linked_list    *dll_find_data(t_doubly_linked_list *dll, int data)
{
    t_doubly_linked_list    *temp;

    if (!dll)
    {
        fprintf(stderr, "Error: lista doblemente enlazada nula\n");
        return (NULL);
    }
    temp = dll;
    while (temp)
    {
        if (temp->data == data)
            return (temp);
        temp = temp->next;
    }
    temp = dll->previous;
    while (temp)
    {
        if (temp->data == data)
            return (temp);
        temp = temp->previous;
    }
    return (NULL);
}

void    dll_sort(t_doubly_linked_list **dll)
{
    int                     temp_data;
    bool                    is_swapped;
    t_doubly_linked_list    *temp;

    if (!(*dll))
    {
        fprintf(stderr, "Error: lista doblemente enlazada nula\n");
        return ;
    }
    is_swapped = false;
    while (!is_swapped)
    {
        is_swapped = true;
        temp = *dll;
        while (temp->next != NULL)
        {
            if (temp->data > temp->next->data)
            {
                temp_data = temp->data;
                temp->data = temp->next->data;
                temp->next->data = temp_data;
                is_swapped = false;
            }
            temp = temp->next;
        }
    }
}

void    dll_print(t_doubly_linked_list *dll)
{
    t_doubly_linked_list    *temp;

    if (!dll)
    {
        fprintf(stderr, "Error: lista doblemente enlazada nula\n");
        return ;
    }
    temp = dll;
    while (temp->previous)
        temp = temp->previous;
    while (temp)
    {
        printf("%d\n", temp->data);
        temp = temp->next;
    }
}

/* DIFICULTAD EXTRA */

int contact_list(void)
{
    int         option;
    t_contact   *contact;

    option = 0;
    contact = create_contact_list();
    if (!contact)
    {
        fprintf(stderr, "Error: creando lista de contactos\n");
        return (-1);
    }
    while (option != 6)
    {
        if (!contact)
        {
            contact = create_contact_list();
            if (!contact)
            {
                fprintf(stderr, "Error: creando lista de contactos\n");
                return (-1);
            }
        }
        display_menu();
        printf("Elige una opción: ");
        if (scanf("%d", &option) != 1)
        {
            fprintf(stderr, "Error: leyendo la opción\n");
            break ;
        }
        handle_option(option, &contact);
    }
    delete_contact_list(&contact);
    return (0);
}

void    display_menu(void)
{
    printf("========================================\n");
    printf("\t   Lista de contactos\n");
    printf("========================================\n");
    printf("\t1. Añadir contacto\n");
    printf("\t2. Actualizar contacto\n");
    printf("\t3. Buscar contacto\n");
    printf("\t4. Eliminar contacto\n");
    printf("\t5. Mostrar contactos\n");
    printf("\t6. Salir\n");
    printf("=========================================\n");
}

void    handle_option(int option, t_contact **contact)
{
    t_contact   *temp;
    printf("\n");
    switch (option)
    {
        case 1:
            add_contact(contact);
            break;
        case 2:
            update_contact(contact);
            break;
        case 3:
            temp = search_contact(*contact, 0);
            if (temp)
            {
                printf("Nombre: %s\n", temp->name);
                printf("Número de teléfono: %llu\n", temp->phone_number);
            }
            else
                fprintf(stderr, "Error: el contacto no existe\n");
            break;
        case 4:
            delete_contact(contact);
            break;
        case 5:
            display_contacts(*contact);
            break;
        case 6:
            printf("Saliendo...\n");
            break;
        default:
            fprintf(stderr, "Error: Opción inválida\n");
            break;
    }
}

void    add_contact(t_contact **contact)
{
    t_contact   *new_contact;
    t_contact   *temp;

    if (!(*contact))
    {
        fprintf(stderr, "Error: lista de contactos vacía\n");
        return ;
    }
    if (!(*contact)->name[0])
    {
        printf("Introduce el nombre del contacto: ");
        if (scanf("%49s", (*contact)->name) != 1)
        {
            fprintf(stderr, "Error: añadiendo nuevo contacto\n");
            return ;
        }
        printf("Introduce el número de %s: ", (*contact)->name);
        if (scanf("%llu", &((*contact)->phone_number)) != 1)
        {
            fprintf(stderr, "Error: añadiendo nuevo contacto\n");
            return ;
        }
    }
    else
    {
        new_contact = (t_contact *)malloc(sizeof(t_contact));
        if (!new_contact)
        {
            fprintf(stderr, "Error: añadiendo nuevo contacto\n");
            return ;
        }
        printf("Introduce el nombre del contacto: ");
        if (scanf("%49s", new_contact->name) != 1)
        {
            fprintf(stderr, "Error: añadiendo nuevo contacto\n");
            free(new_contact);
            return ;
        }
        printf("Introduce el número de %s: ", new_contact->name);
        if (scanf("%llu", &(new_contact->phone_number)) != 1)
        {
            fprintf(stderr, "Error: añadiendo nuevo contacto\n");
            free(new_contact);
            return ;
        }
        if (search_contact(*contact, new_contact->phone_number))
        {
            fprintf(stderr, "Error: el número ya existe\n");
            free(new_contact);
            return ;
        }
        temp = *contact;
        while (temp->next)
            temp = temp->next;
        temp->next = new_contact;
        new_contact->previous = temp;
        new_contact->next = NULL;
    }
}

void    update_contact(t_contact **contact)
{
    int                 option;
    t_contact           *temp;
    unsigned long long  temp_phone_number;

    if (!(*contact))
    {
        fprintf(stderr, "Error: lista de contactos vacía\n");
        return ;
    }
    printf("Introduce el número de teléfono: ");
    if (scanf("%lld", &temp_phone_number) != 1)
    {
        fprintf(stderr, "Error: leyendo el número de teléfono\n");
        return ;
    }
    temp = search_contact(*contact, temp_phone_number);
    if (!temp)
    {
        fprintf(stderr, "Error: el contacto no existe\n");
        return ;
    }
    printf("Introduce 1 si quieres actualizar el nombre o 2 si quieres actualizar el número: ");
    if (scanf("%d", &option) != 1)
    {
        fprintf(stderr, "Error: leyendo la opción\n");
        return ;
    }
    if (option == 1)
    {
        printf("El nombre actual es %s\n", temp->name);
        memset(temp->name, 0, 50);
        printf("Introduce el nuevo nombre: ");
        if (scanf("%49s", temp->name) != 1)
        {
            fprintf(stderr, "Error: leyendo el nombre\n");
            return ;
        }
    }
    else if (option == 2)
    {
        printf("El número actual es %llu\n", temp->phone_number);
        printf("Introduce el nuevo número de teléfono: ");
        if (scanf("%llu", &temp->phone_number) != 1)
        {
            fprintf(stderr, "Error: leyendo el número de teléfono\n");
            return ;
        }
    }
    else
        fprintf(stderr, "Error: opción inválida\n");
}

t_contact   *search_contact(t_contact *contact, unsigned long long phone_number)
{
    t_contact           *temp;
    unsigned long long  temp_phone_number;

    if (!contact)
    {
        fprintf(stderr, "Error: lista de contactos vacía\n");
        return (NULL);
    }
    temp_phone_number = phone_number;
    if (temp_phone_number == 0)
    {
        printf("Introduce el número de teléfono que quieres buscar: ");
        if (scanf("%llu", &temp_phone_number) != 1)
        {
            fprintf(stderr, "Error: leyendo el número de teléfono\n");
            return (NULL);
        }
    }
    temp = contact;
    while (temp)
    {
        if (temp->phone_number == temp_phone_number)
            return (temp);
        temp = temp->previous;
    }
    temp = contact->next;
    while (temp)
    {
        if (temp->phone_number == temp_phone_number)
            return (temp);
        temp = temp->next;
    }
    return (NULL);
}

void    delete_contact(t_contact **contact)
{
    t_contact           *temp;
    unsigned long long  temp_phone_number;

    if (!(*contact))
    {
        fprintf(stderr, "Error: lista de contactos vacía\n");
        return ;
    }
    printf("Introduce el número de teléfono del contacto que quieres eliminar: ");
    if (scanf("%llu", &temp_phone_number) != 1)
    {
        fprintf(stderr, "Error: leyendo el número de teléfono\n");
        return ;
    }
    temp = search_contact(*contact, temp_phone_number);
    if (!temp)
    {
        fprintf(stderr, "Error: el contacto no existe\n");
        return ;
    }
    if (temp->previous)
        temp->previous->next = temp->next;
    else
    {
        *contact = temp->next;
        if (*contact)
            (*contact)->previous = NULL;
    }
    if (temp->next)
        temp->next->previous = temp->previous;
    free(temp);
}

void    display_contacts(t_contact *contact)
{
    t_contact   *temp;

    if (!contact || !contact->name[0])
    {
        fprintf(stderr, "Error: lista de contactos vacía\n");
        return ;
    }
    temp = contact;
    while (temp->previous)
        temp = temp->previous;
    while (temp)
    {
        printf("Nombre: %s\n", temp->name);
        printf("Teléfono: %llu\n", temp->phone_number);
        temp = temp->next;
    }
}

t_contact   *create_contact_list(void)
{
    t_contact   *contact;

    contact = (t_contact *)malloc(sizeof(t_contact));
    if (!contact)
    {
        fprintf(stderr, "Error: creando la lista de contactos\n");
        return (NULL);
    }
    memset(contact->name, 0, 50);
    contact->phone_number = 0;
    contact->previous = NULL;
    contact->next = NULL;
    return (contact);
}

void    delete_contact_list(t_contact **contact)
{
    t_contact   *temp;

    if (!(*contact)) 
    {
        fprintf(stderr, "Error: lista de contactos vacía\n");
        return ;
    }
    temp = *contact;
    while (temp->previous)
        temp = temp->previous;
    while (temp)
    {
        *contact = temp;
        temp = temp->next;
        free(*contact);
    }
    *contact = NULL;
}
