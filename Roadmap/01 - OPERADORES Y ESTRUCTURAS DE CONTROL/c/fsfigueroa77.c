#include <stdio.h>

int main(){
    // Ejemplo de operador de asignacion
    printf("\nOPERADORES DE ASIGNACION\n");
    int variable_entera = 100; // El "=" es el operador de asignacion
    printf("El ejemplo de usar un operador de asignacion en una variable es: %d.\n", variable_entera);
    variable_entera += 5;
    printf("El ejemplo de usar un operador de suma y asignacion en una variable es: %d.\n", variable_entera);
    variable_entera -= 45;
    printf("El ejemplo de usar un operador de resta y asignacion en una variable es: %d.\n", variable_entera);
    variable_entera *= 2;
    printf("El ejemplo de usar un operador de multiplicacion y asignacion en una variable es: %d.\n", variable_entera);
    variable_entera /= 3;
    printf("El ejemplo de usar un operador de division y asignacion en una variable es: %d.\n", variable_entera);
    variable_entera %= 9;
    printf("El ejemplo de usar un operador de modulo y asignacion en una variable es: %d.\n", variable_entera);

    // Ejemplos de operadores aritmeticos
    printf("\nOPERADORES DE ARITMETICOS\n");
    variable_entera = 1;
    printf("Usar el operador unario Signo negativo en la variable da como resultado: %d.\n", -variable_entera);
    printf("Usar el operador unario Incremento en la variable da como resultado: %d.\n", ++variable_entera);
    printf("Usar el operador unario Decremento en la variable da como resultado: %d.\n", --variable_entera);
    printf("Uso del operador binario Suma: 2 + 3 = %d.\n", 2 + 3);
    printf("Uso del operador binario Resta: 3 - 2 = %d.\n", 3 - 2);
    printf("Uso del operador binario Multiplicacion: 10 * 5 = %d.\n", 10 * 5);
    printf("Uso del operador binario Division: 24 / 6 = %d.\n", 24 / 6);
    printf("Uso del operador binario Modulo: 30 % 11 = %d.\n", 30 % 11);

    // Ejemplos de operadores relacionales (C no tiene el tipo de dato booleano. Se representa a True como 1 y False como 0)
    printf("\nOPERADORES DE RELACIONALES\n");
    int resultado;
    resultado = (1 < 3); // Menor que
    printf("El resultado de 1 < 3 es: %d.\n", resultado);
    resultado = (1 > 3); // Mayor que
    printf("El resultado de 1 > 3 es: %d.\n", resultado);
    resultado = (1 <= 3); // Menor o igual que
    printf("El resultado de 1 <= 3 es: %d.\n", resultado);
    resultado = (1 >= 3); // Mayor o igual que
    printf("El resultado de 1 >= 3 es: %d.\n", resultado);
    resultado = (1 == 3); // Igual que 
    printf("El resultado de 1 == 3 es: %d.\n", resultado);
    resultado = (1 != 3); // Distinto que
    printf("El resultado de 1 != 3 es: %d.\n", resultado);

    // Ejemplos de operadores logicos
    printf("\nOPERADORES DE LOGICOS\n");
    resultado = (5 > 3) && (3 != 7);
    printf("El resultado de (5 > 3) && (3 != 7) es: %d.\n", resultado); // Conjuncion
    resultado = (5 == 1) || (4 >= 10);
    printf("El resultado de (5 == 1) || (4 >= 10) es: %d.\n", resultado); // Disyuncion
    resultado = !(5 > 3);
    printf("El resultado de !(5 > 3) es: %d.\n", resultado); // Negacion

    // Ejemplo de operadores con bits
    printf("\nOPERADORES DE BITS\n");
    unsigned char numero1 = 7, numero2 = 2; // 7 = 111, 2 = 10
    unsigned char conjuncion = numero1 & numero2; // 111 & 10
    printf("El resultado de 7 & 2 es: %u.\n", conjuncion); // 10 = 2
    unsigned char disyuncion = numero1 | numero2; // 111 | 10
    printf("El resultado de 7 | 2 es: %u.\n", disyuncion); // 111 = 7
    unsigned char disyuncion_ex = numero1 ^ numero2; // 111 ^ 10
    printf("El resultado de 7 ^ 2 es: %u.\n", disyuncion_ex); // 101 = 5
    unsigned char negacion = ~numero1; // ~0000 0111
    printf("El resultado de ~7 es: %u.\n", negacion); // 1111 1000 = 248 
    unsigned char desp_der = numero1 >> 2;
    printf("El resultado de 7 >> 2 es: %u.\n", desp_der); // 001 = 1
    unsigned char desp_izq = numero1 << 2;
    printf("El resultado de 7 << 2 es: %u.\n", desp_izq); // 11100 = 28

    // Ejemplos de Condicionales 
    int variable1 = 0, variable2 = 0;
    printf("\nIngrese un numero entre 1 y 90: ");
    scanf("%d", &variable1); // Pedir al usuario un numero entre 1 y 90
    if(variable1 > 0 && variable1 <= 30){ // Uso de if
        printf("Tendras suerte en el trabajo.\n");
    }else if(variable1 > 30 && variable1 <= 60){
        printf("Tendras suerte en el amor.\n");
    }else if(variable1 > 60 && variable1 <= 90){
        printf("Tendras suerte en el dinero.\n");
    }else{
        printf("Tendras mala suerte en todo.\n");
    }

    printf("\nIngresa otro numero: ");
    scanf("%d", &variable2);
    printf("El numero maximo es: %d.\n", ((variable1 > variable2) ? variable1 : variable2)); // Uso del operaperador condicional ?

    unsigned char opcion = 0;
    printf("\nConsulta de saldos\n[1] Saldo de minutos.\n[2] Saldo de datos.\n[3] Salir.\nElija una opcion del menu: ");
    scanf("%u", &opcion);
    if(!(opcion < 1 || opcion > 3)){
        switch(opcion){ // Uso de Switch
            case 1:
                printf("Su salgo de minutos es: 50 minutos.\n");
                break;
            case 2:
                printf("Su saldo de datos es: 15 gb.\n");
                break;
            default:
                printf("Gracias por elegir nuestro servicio.\n");
                break;
        }
    }else{
        printf("Opcion incorrecta.\n");
    }
    
    // Ejemplos de iterativas
    unsigned char eleccion = 0;    
    while(eleccion < 1 || eleccion > 3){ // Uso de While
        printf("\nIngresa un numero del 1 al 3: ");
        scanf("%u", &eleccion);
        if(eleccion < 1 || eleccion > 3){
            printf("Opcion incorrecta.\n");
        }
    }

    int i;
    for(i = 1; i < 11; i++){ // Uso de For
        if(i % 2 == 0){
            printf("%d\n", i);
        }
    }

    // Dificultad Extra
    printf("\n=====Dificultad Extra=====\n");    
    for(i = 10; i < 56; i+=2){ // Ciclo para empezar en el 10 y terminar en el 56, haciendo saltos de 2 en 2
        if(!((i % 3) == 0)){ // Condicion para excluir los numeros multiplos de 3
            if(!(i == 16)){ // Condicion para excluir el numero 16
                printf("%d\n", i);
            }
        }
    }

    return(0);
}