/*
 * EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 */

/**************************IMPORTANTE*********************************/
//Para probar las funciones se deben desconmentar en el main .


#include <stdio.h>
#include <stdlib.h>
#include <string.h>

    int num;//EJEMPLO DE VARIABLE GLOBAL 

    /***********************printf() y  scanf()********* */
    //printf(): imprime en pantalla .
    //scanf(): lee datos de entrada (normalmente datos introducidos dese el teclado) .
void ft_pritf_and_sacnf()
{
    // Solicita al usuario que ingrese un número .
    printf("Enter a number: ");
    scanf("%d", &num);

    // Muestra el número ingresado .
    printf("You entered: %d\n", num);
};
    


    /*********************malloc y free**********************/
    //malloc: es otra funcion reprensantativa de C que se utiliza para asignar memoria .
    //free : con free liberamos esa memoria .


void ft_malloc_and_free(){
    int *ptr = (int*) malloc(sizeof(int));

    if (ptr == NULL) {
        printf("¡ERROR! no se pudo asignar memoria");
       
    }

    *ptr = 42;//usamos la memoria asignada
    printf("Valor almacenado es : %d\n" ,num);

    free(ptr);
    
}
/**************************strcpy, strlen y strcmp*******************/

void ft_strcpy(){

    char src[]= "hola";//EJEMPLO DE VARIABLES LOCALES
    char dest[5];

    strcpy(dest, src);

    printf("Hemos copiado la cadena src : %s , en dest: %s\n", src ,dest);


}

void ft_strlen(){

    char src[] = "esto es un ejemplo";

    int src_lenght = strlen(src);
    printf("El numero de caracteres de src es : %d \n", src_lenght);
}


void ft_strcmp(){
    char string_1[]= "Hola";
    char string_2[]= "hola";

    int res = strcmp(string_1, string_2);
    if(res == 0){
        printf("las cadenas comparadas son iguales\n");
    } else if (res < 0){
        printf("string_1 es menor que estring_2\n");
    } else {
        printf("string_1 es mayor que string_2\n");
    }
}

/****************Crear funciones dentro de funciones **************** */

// En C, no es posible definir una función dentro de otra. Intentarlo resultará en un error de compilación.



/***************************dificultad extra********************/

int ft_my_function(char str_1[], char str_2[])
{
    int num;
    num = 1;
    int count = 0;
   
    while(num <= 100){
        if (num % 3 == 0 && num %5 == 0)
        {
            printf("%s , %s\n", str_1, str_2);
            

        } else if (num % 3 == 0) {

              printf("%s\n", str_1) ;
            

        } else if (num % 5 == 0){

            printf("%s \n", str_2);
            
        } else {
            
         printf("%d\n", num);
         count++;
        }
       
        num++;
    }
    printf ("count of numbers = %d\n", count);

    return (count);

}




    
int main() {

    char *str_1= "hola";
    char *str_2= "adios"; 
    //printf("ft_print_and_scanf:\n\n");
    //ft_pritf_and_sacnf();
    //printf("***************************\n");
    //printf("ft_malloc_and_free:\n\n");
    //ft_malloc_and_free();
    //ft_strcpy();
    //ft_strlen();
    //ft_strcmp();
    ft_my_function(str_1,str_2);
    return 0;
}
   



