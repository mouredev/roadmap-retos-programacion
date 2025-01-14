#include <stdio.h>


char language = 'C';

void sayHello() {
    printf("Hello %c!\n", language);
}

int suma() {
    return 2 + 5;
}

void saluda(char nombre[]) {
    printf("Hola %s\n", nombre);
}

int sumaADos(int number) {
    int dos = 2;
    return dos + number;
}

int exercise(char string1[], char string2[]) {
    int times = 0;

    for (int i = 0; i <= 100; i++) {
        if((i % 3 == 0) && (i % 5 == 0)) {
            printf("%s %s\n", string1, string2);
        } else if(i % 5 == 0) {
            printf("%s\n", string2);
        } else if (i % 3 == 0) {
            printf("%s\n", string1);
        } else {
            printf("%d\n", i);
            times++;
        }
    }

    return times;
}

int main()  {
    sayHello();
    printf("%d\n", suma());
    saluda("Diego");
    printf("%d\n", sumaADos(5));
    printf("%d", exercise("Hola", "Mundo"));
    return 0;
}
