#include <stdio.h>
#include <time.h>
#include <stdbool.h>
#include <windows.h>
#include <unistd.h>

int main(){

   // Tipos de datos primitivos
   short Int16 = 10;
   int Int32 = 100;
   long Int64 = 1000;

   // Podemos realizar operaciones matematicas usanod
   printf("Suma: %ld\n", Int16 + Int32);
   printf("Resta: %i\n", Int32 - Int16);
   printf("Division: %i\n", Int64 / Int32);
   printf("Multiplicacion: %ld\n", Int16 * Int32);
   printf("Modulo: %i", Int32 % Int16);

   // Tambien tenemos los deplazamiento unitarios
   printf("Desplazamiento derecha: %i", 3 >> 2);
   printf("Desplazamiento izquierda: %i", 3 >> 2);

   // Podemos realizar sentencias de control selectiva
   if(Int16 < Int32){
      printf("True\n");
   }
   else{
      printf("False\n");
   }
   // Tambien podemos realizar multiples caso con Switch ; case
   const int option = 1;

   switch (option) {
      case 1: {
         printf("Realizar el registro de n usuarios\n");
         // procesoo...
         break;
      }
      case 2: {
         printf("Buscar usuario mediante su ID\n");
         // procesoo...
         break;
      }
      default:{
         printf("Este caso no existe!\n");
         // procesoo...
         break;
      }
   }
   // cada caso es detenido con break o return

   // Uso de for: puedes usar for para realizar tareas repetitivas, como imprimir números o bien
   // Rellenar el registro de muchos usuarios
   for(int i = 1; i <= 10; i++){
      printf("%i, ", i);
   }
   printf("\n");
   // Tambien tenemos do while
   int response;

   do{
      // proceso..
      printf("Ingrese 1 para salir del ciclo\n");
      scanf("%i", &response);
   }while(response != 1);


   // solucion del reto extra

   for(int i = 10; i <= 55; i++){
      if(i != 16 && i % 2 == 0 && i % 3 != 0){
         printf("%i, ", i);
      }
   }

   time_t tiempo_actual;
   struct tm* info_tiempo;

   printf("Para finalizar presentar un reloj en tiempo real\n");
   system("pause");
   
   while(true){
      time(&tiempo_actual);
      info_tiempo = localtime(&tiempo_actual);
      printf("La hora actual es: %02d:%02d:%02d\n", info_tiempo->tm_hour, info_tiempo->tm_min, info_tiempo->tm_sec);
      sleep(1);

      system("cls");
   }
   return 0;
}