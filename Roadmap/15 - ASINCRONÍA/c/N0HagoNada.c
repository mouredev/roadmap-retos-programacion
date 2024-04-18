#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>

typedef struct
{
    const char *nombre;
    int duracion;
} FuncionInfo;

void *funcionAsincrona(void *arg)
{
    FuncionInfo *info = (FuncionInfo *)arg;
    printf("%s comenzó\n", info->nombre);
    printf("%s tardará %d segundos en finalizar\n", info->nombre, info->duracion);
    sleep(info->duracion);
    printf("%s finalizó\n", info->nombre);
    free(info);
    return NULL;
}

int main()
{
    pthread_t hilos[3];
    FuncionInfo *info;

    // Ejecutar las funciones C, B y A en paralelo
    info = malloc(sizeof(FuncionInfo));
    info->nombre = "Función C";
    info->duracion = 3;
    pthread_create(&hilos[0], NULL, funcionAsincrona, info);

    info = malloc(sizeof(FuncionInfo));
    info->nombre = "Función B";
    info->duracion = 2;
    pthread_create(&hilos[1], NULL, funcionAsincrona, info);

    info = malloc(sizeof(FuncionInfo));
    info->nombre = "Función A";
    info->duracion = 1;
    pthread_create(&hilos[2], NULL, funcionAsincrona, info);

    // Esperar a que las funciones C, B y A finalicen
    for (int i = 0; i < 3; i++)
    {
        pthread_join(hilos[i], NULL);
    }

    // Ejecutar la función D
    info = malloc(sizeof(FuncionInfo));
    info->nombre = "Función D";
    info->duracion = 1;
    funcionAsincrona(info);

    printf("Programa finalizado\n");

    return 0;
}