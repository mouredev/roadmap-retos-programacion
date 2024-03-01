#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// RETO
#define MAX_CONTACTOS 100
#define MAX_NOMBRE 50
#define MAX_TELEFONO 12

typedef struct
{
    char nombre[MAX_NOMBRE];
    char telefono[MAX_TELEFONO];
} Contacto;

Contacto agenda[MAX_CONTACTOS];
int totalContactos = 0;

void insertarContacto()
{
    if (totalContactos >= MAX_CONTACTOS)
    {
        printf("Agenda llena.\n");
        return;
    }

    printf("Introduce el nombre del contacto: ");
    scanf("%s", agenda[totalContactos].nombre);

    char telefono[MAX_TELEFONO];
    printf("Introduce el número de telefono (hasta 11 dígitos): ");
    scanf("%s", telefono);

    // Validar longitud y que sean solo dígitos
    if (strlen(telefono) > 11)
    {
        printf("Numero invalido. Demasiados dígitos.\n");
        return;
    }

    strcpy(agenda[totalContactos].telefono, telefono);
    totalContactos++;
    printf("Contacto añadido.\n");
}

void buscarContacto()
{
    char nombre[MAX_NOMBRE];
    printf("Introduce el nombre del contacto a buscar: ");
    scanf("%s", nombre);

    for (int i = 0; i < totalContactos; i++)
    {
        if (strcmp(agenda[i].nombre, nombre) == 0)
        {
            printf("Contacto encontrado: %s, Telefono: %s\n", agenda[i].nombre, agenda[i].telefono);
            return;
        }
    }
    printf("Contacto no encontrado.\n");
}

void actualizarContacto()
{
    char nombre[MAX_NOMBRE];
    printf("Introduce el nombre del contacto a actualizar: ");
    scanf("%s", nombre);

    for (int i = 0; i < totalContactos; i++)
    {
        if (strcmp(agenda[i].nombre, nombre) == 0)
        {
            printf("Introduce el nuevo número de telefono: ");
            scanf("%s", agenda[i].telefono);
            printf("Contacto actualizado.\n");
            return;
        }
    }
    printf("Contacto no encontrado.\n");
}

void eliminarContacto()
{
    char nombre[MAX_NOMBRE];
    printf("Introduce el nombre del contacto a eliminar: ");
    scanf("%s", nombre);

    for (int i = 0; i < totalContactos; i++)
    {
        if (strcmp(agenda[i].nombre, nombre) == 0)
        {
            for (int j = i; j < totalContactos - 1; j++)
            {
                agenda[j] = agenda[j + 1];
            }
            totalContactos--;
            printf("Contacto eliminado.\n");
            return;
        }
    }
    printf("Contacto no encontrado.\n");
}
// Definición de la estructura Persona
typedef struct
{
    int id;
    char nombre[50];
} Persona;

// Definición de la estructura Nodo para la lista enlazada
typedef struct Nodo
{
    int dato;
    struct Nodo *siguiente;
} Nodo;

// Funciones para la lista enlazada
void insertarInicio(Nodo **cabeza, int nuevoDato)
{
    Nodo *nuevoNodo = (Nodo *)malloc(sizeof(Nodo));
    nuevoNodo->dato = nuevoDato;
    nuevoNodo->siguiente = *cabeza;
    *cabeza = nuevoNodo;
}

void borrarInicio(Nodo **cabeza)
{
    if (*cabeza != NULL)
    {
        Nodo *temp = *cabeza;
        *cabeza = (*cabeza)->siguiente;
        free(temp);
    }
}

void imprimirLista(Nodo *n)
{
    while (n != NULL)
    {
        printf("%d ", n->dato);
        n = n->siguiente;
    }
    printf("\n");
}

int main()
{
    // Arrays
    int numeros[5] = {1, 2, 3, 4, 5};
    numeros[2] = 30; // Actualización
    // Ordenación simplificada
    for (int i = 0; i < 4; i++)
    {
        for (int j = i + 1; j < 5; j++)
        {
            if (numeros[i] > numeros[j])
            {
                int temp = numeros[i];
                numeros[i] = numeros[j];
                numeros[j] = temp;
            }
        }
    }
    for (int i = 0; i < 5; i++)
    {
        printf("%d ", numeros[i]);
    }
    printf("\n");

    // Struct
    Persona persona1;
    persona1.id = 1;
    strcpy(persona1.nombre, "Juan");
    persona1.id = 2; // Actualización
    printf("ID: %d, Nombre: %s\n", persona1.id, persona1.nombre);

    // Lista enlazada
    Nodo *cabeza = NULL;
    insertarInicio(&cabeza, 10);
    insertarInicio(&cabeza, 20);
    imprimirLista(cabeza);
    borrarInicio(&cabeza);
    imprimirLista(cabeza);
    /********************************************RETO*****************************************************/
    int opcion;

    do
    {
        printf("\nAgenda de contactos\n");
        printf("1. Insertar contacto\n");
        printf("2. Buscar contacto\n");
        printf("3. Actualizar contacto\n");
        printf("4. Eliminar contacto\n");
        printf("5. Salir\n");
        printf("Selecciona una opción: ");
        scanf("%d", &opcion);

        switch (opcion)
        {
        case 1:
            insertarContacto();
            break;
        case 2:
            buscarContacto();
            break;
        case 3:
            actualizarContacto();
            break;
        case 4:
            eliminarContacto();
            break;
        case 5:
            printf("Saliendo...\n");
            break;
        default:
            printf("Opción invalida.\n");
        }
    } while (opcion != 5);

    return 0;
}