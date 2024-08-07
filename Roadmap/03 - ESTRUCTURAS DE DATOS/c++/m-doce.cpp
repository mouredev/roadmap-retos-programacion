#include <iostream>
#include <algorithm>
#include <vector>
#include <list>
#include <map>
#include <tuple>
#include <string.h>
using namespace std;

#define MAX_SIZE 50

// - - - Funciones y estructuras para el ejercicio extra - - -

struct Contacto
{
    char nombre[MAX_SIZE];
    int numero;
};

void Continuar()
{
    printf("Presione 'Enter' para continuar...\n");
    cin.get();
    cin.ignore();

    return;
}

void ListarContactos(vector <Contacto> agenda, int &option)
{
    for(int i=0; i<agenda.size(); i++)
    {
        printf("[%d] %s\n", (i+1), agenda[i].nombre);
    }

    scanf("%d", &option);

    return;
}

void BuscarContacto(vector <Contacto> agenda)
{
    int option = 0;
    printf("\nSeleccione el contacto para ver su numero:\n");
    ListarContactos(agenda, option);

    int i = 0;
    while(i < option)
    {
        if(i == (option - 1))
        {
            printf("%s: %d\n", agenda[i].nombre, agenda[i].numero);
        }

        i++;
    }

    Continuar();

    return;
}

void AgregarContacto(vector <Contacto> &agenda)
{
    Contacto newContact;
    
    printf("Ingrese el nombre del contacto: ");
    scanf("%s", &newContact.nombre);
    printf("Ingrese el numero del contacto: ");
    scanf("%d", &newContact.numero);

    agenda.push_back(newContact);
    printf("\nSe agrego a %s de forma exitosa!\n", newContact.nombre);
    Continuar();

    return;
}

void ActualizarContacto(vector <Contacto> &agenda)
{
    int option = 0;
    printf("\nSeleccione el contacto que desea actualizar:\n");
    ListarContactos(agenda, option);

    int i = 0;
    while(i < option)
    {
        if(i == (option - 1))
        {
            printf("Actualice el nombre del contacto: ");
            scanf("%s", &agenda[i].nombre);
            printf("Actualice el numero del contacto: ");
            scanf("%d", &agenda[i].numero);
        }

        i++;
    }

    printf("\nContacto actualizado de forma exitosa!\n");
    Continuar();

    return;
}

void EliminarContacto(vector <Contacto> &agenda)
{
    int option = 0;
    char user[MAX_SIZE];
    printf("\nSeleccione el contacto que desea eliminar:\n");
    ListarContactos(agenda, option);

    int i = 0;
    while(i < option)
    {
        if(i == (option - 1))
        {
            strcpy(user, agenda[i].nombre);
            agenda.erase(agenda.begin()+i);
        }

        i++;
    }

    printf("\nSe elimino a %s de forma exitosa!\n", user);
    Continuar();

    return;
}

void Salir()
{
    printf("\nGracias por utilizar nuestra agenda! Que tenga un buen dia :)\n");
    exit(0);

    return;
}

void MenuPrincipal(vector <Contacto> agenda)
{
    int firstOption = 0;
    printf("\nSeleccione la accion a realizar:\n [1] Buscar\n [2] Agregar\n [3] Actualizar\n [4] Eliminar\n [5] Salir\n\n");
    scanf("%d", &firstOption);

    switch(firstOption)
    {
        case 1:
        BuscarContacto(agenda);
        MenuPrincipal(agenda);
        break;

        case 2:
        AgregarContacto(agenda);
        MenuPrincipal(agenda);
        break;

        case 3:
        ActualizarContacto(agenda);
        MenuPrincipal(agenda);
        break;

        case 4:
        EliminarContacto(agenda);
        MenuPrincipal(agenda);
        break;

        case 5:
        Salir();
        break;

        default:
        printf("\nError de ingreso. Por favor ingrese una opcion valida\n");
        MenuPrincipal(agenda);
        break;
    }
}



int main()
{
    // - - - Ejercicio extra - - -
    printf("Bienvenido/a a su agenda!\n");
    vector <Contacto> agenda = {{"m-doce", 1212}, {"mouredev", 1000}, {"gitHubUser", 9999}};
    MenuPrincipal(agenda);

    return 0;
}

/* USO Y DEFINICIÓN DE DISTINTOS TIPOS DE ESTRUCTURAS DE DATOS

//Arrays
    //Su tamaño y tipo de dato deben definirse al momento de crearlos, y no pueden modificarse luego. Es decir, no se pueden agregar o quitar elementos
    int arrayEnteros[5] = {1, 3, 5, 7, 11}; //Creación
    printf("%d\n",arrayEnteros[3]); //Acceso
    arrayEnteros[4] = 13; //Modificación
    //Para listar todos sus elementos es necesario utilizar un bucle de repetición
    for(int i=0; i<5; i++)
    {
        printf("%d, ", arrayEnteros[i]);
    }
    printf("\n");


    //Vectores
    //Debemos definir el tipo de datos que contendrá nuestro vector, pero no es necesario definir su tamaño. El mismo es flexible y puede variar durante la ejecución del código
    vector <int> vectorEnteros; //Creación
    vectorEnteros.push_back(12); //Agregar un elemento al final
    vectorEnteros.push_back(9);
    vectorEnteros.push_back(2);
    vectorEnteros.push_back(92);
    vectorEnteros.push_back(19);
    vectorEnteros[3] = 29; //Modificar un elemento
    printf("%d\n\n\n", vectorEnteros[0]); //Acceso a elementos
    vectorEnteros.pop_back(); //Eliminar el último elemento
    sort(vectorEnteros.begin(), vectorEnteros.end()); //Ordenar de menor a mayor


    //Listas
    list <int> listaEnteros;
    listaEnteros.push_back(10); //Agregar un elemento al final
    listaEnteros.push_back(20);
    listaEnteros.push_front(15); //Agregar un elemento al principio
    listaEnteros.push_front(5);
    listaEnteros.pop_back(); //Quitar el último elemento
    listaEnteros.pop_front(); //Quitar el primer elemento

    //Diccionarios
    map <string, string> diccionario;
    diccionario["User"] = "m-doce";
    diccionario["Language"] = "C++";


*/