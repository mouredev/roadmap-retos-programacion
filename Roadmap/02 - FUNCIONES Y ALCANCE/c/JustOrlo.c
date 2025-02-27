#include <stdio.h>
#include <math.h> //Para hacer uso de la Funcion Pow
#include <stdbool.h>
#include <string.h>

/*Declaracioin de Funciones*/
void Introduccion(); //Funcion de Tipo Void, Sin Parametro y sin retorno
int Bit_Convert(int); //Funcion con retorno y con Parametros de entrada
void Mostrar(int); //Funcion sin retorno y con parametros de entrada
void Funcion_en_Funcion(); //Funcion para probar si es posible Crear Funcione dentro de Funciones
int Desafio(char[] , char[] );

/*Declaracion de Variables Globales*/
int arr[7] = {0,0,0,0,0,0,0}; 

int main(){

    /*Declaracion de variables locales*/
    char txt1[] = "MultiploX3";
    char txt2[] = "MultiploX5";
    int a, b, c;
    a = 27;
    b = 114;
    c = 38;

    /*Uso de la Funcion Introducion*/
    Introduccion(); 
    
    /*Funcion Main*/
    printf("---->Funcion Main<----\n\n");
    printf("NOTA: La Funcion main, es la fncion principal de todo Programa en C...\n\n\n");

    /*Uso de la Funcion Mostrar*/
    printf("\t-->Ejemplo de Funcion Con parametro de Entrada y sin retorno<--\n\n");
    printf("\t NOTA: Esta Funcion toma tres numero (0 - 127) y lo escribe en binario y ademas muestra su segunda potencia.\n\n");
    printf("Numero\t\t\t Bits\t\t\t Potencia\n\n");
    
    Mostrar(a);    
    Mostrar(b);
    Mostrar(c);

    /*Uso de la Funcion Funcion_en_Funcion*/
    printf("\t-->Es Posible Crear funciones detro de Funciones?<--\n\n\n");
    Funcion_en_Funcion();

    /*Desafio*/
    printf("\t-->Desafio!!!<--\n\n");
    printf("\n La cantidad de numeros no divisibles entre 3 y/o 5 es: %d\n\n\n", Desafio(txt1,txt2));
    

}

void Introduccion(){
    
    printf("\t\t---->Funciones<----\n\n");

    /*Sintaxis de una Funcion*/

    /*Declaracion*/
    printf("-->Declaracion<--\n\n");
    printf("Typ_Return Nombre_Funcion(Typ_param Var, etc){\n");
    printf("\t /*Sentencias de La Funcion*/;\n");
    printf("\t return retorno;\n");
    printf("}\n\n\n");
    printf("Typ_Return:\t\t Tipo de Parametro a Retornar.\n");
    printf("Nombre_Funcion:\t\t Nombre de la Funcion.\n");
    printf("Typ_param:\t\t Tipo de Paramtetro de Entrada.\n");
    printf("Var:\t\t\t Variable de entrada de la Funcion.\n\n");

    /*Llamada*/
    printf("-->Llamada<--\n\n");
    printf("Nomre_Funcion(var1);\n");
    printf("var1:\t\t\t Variable cuyo valor se pasa al parametrode entrada de la Funcion\n\n");
    printf("NOTA: Existen Funciones de Tipo Void, que no retornan valor...\n\n\n");
}

int Bit_Convert(int var){

    /*Declaracion de Variables Locales*/
    int point = 0;    

    do
    {
        arr[point] = var % 2;
        var = var / 2;
        point++;

    } while (var != 0);
    
    return point;
}

void Mostrar(int var){

    /*Declaracion de Variables Locales*/
    int iteraciones;

    /*Uso de la Fucion Bit Converter*/
    iteraciones = Bit_Convert(var); //La variable iteracioes toma el valor que retorna la Funcion Bit_Converter
    
    
    printf("%d\t\t\t", var);
    /*Haciendo uso de la sentencia for para mostrar la cadena de bits correspondiente*/
    for (int  i = (iteraciones - 1);  i >= 0;  i--)
    {
        printf("%d", arr[i]);
    }
    printf("\t\t\t%.0f\n\n", pow(var, 2)); //Se hace uso de la funcion predefinida pow(x,y)
    
}

void Funcion_en_Funcion()
{
    /*Declaracion de variables locales*/
    bool prueba = false;
    /*Declaracion de Funcion*/
    void Probar(){
        prueba = true; //Cambiamos el valor de la variable prueba, de esta forma, sabremos si funiono la funcion
    }
        /*Llamamos a la funcion anidada Probar(), para probar si es posible*/
        Probar();
        if (prueba)
        {
            printf("Si es posible crear Funciones dentro de funciones\n\n\n");
        }
        else printf("No es posible crear funcione dentro de funciones\n\n\n");

}

int Desafio(char a[], char b[]){
/*Declaracion de Variables Locales*/
int retorno = 0; //para Retornar la cantidad de numeros imprimidos
char txt_Retorno[100] = "\0"; 
for (int i = 1; i <= 100; i++)
{   
    strcpy (txt_Retorno, "\0");

    if(i % 3 == 0) //Si el numero es divisible entre tres se concatena el texto a la cadena que se va a mostrar
    {

        strcat(txt_Retorno, a); 
        printf("%s\n", txt_Retorno);
    }
    if((i % 5) == 0) //Si el numero es divisible entre cinco se concatena el texto a la cadena que se va a mostrar
    {
        strcat(txt_Retorno, b); 
        printf("%s\n", txt_Retorno);
    }
   if(((i % 3) != 0) && ((i % 5) != 0)) //Si no es divisible se muestra un numero 
   {
        printf("%d\n", i);
        retorno++;
   }

}

return retorno;

}