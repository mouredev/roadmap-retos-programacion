#include <stdio.h>
#include <string.h>

int main()
{
//Inicializacion
    
    int a = 20;
    int b = 1;
    int c = 0;
    printf("a=%d b=%d\n",a,b);
//Aritmeticos
    printf("Suma(+) \ta+10=%d\n",a + 10);
    printf("Resta(-)\ta-5=%d\n",a - 5);
    printf("Mult(*) \ta*5=%d\n",a * 5);
    printf("División(/)\ta/5=%d\n",a / 5);
    printf("Resto(%%)\ta%%5=%d\n\n",a % 5);
    
//Incremento
    printf("Incremento(a++)\t%d\n",a++); //Primero evalua y luego incrementa
    printf("Incremento(a)\t%d\n",a);
    printf("Incremento(++a)\t%d\n",++a); //Primero incrementa y luego evaluea
    printf("Incremento(a)\t%d\n",a);
    printf("Decremento(a--)\t%d\n",a--); //Primero evalua y luego incrementa
    printf("Decremento(a)\t%d\n",a);
    printf("Decremento(--a)\t%d\n",--a); //Primero incrementa y luego evaluea
    printf("Decremento(a)\t%d\n\n",a);

//Asignacion
    a -= 5; // a = a - 5
    printf("Resta e igual(-=)\ta-=5 a=%d\n",a);
    a += 10; // a = a + 10
    printf("Suma e igual(+=)\ta+=10 a=%d\n",a);
    a *= b; // a = a * b
    printf("Mult e igual(-=)\ta*=b a=%d\n",a);
    a /= b; // a = a / b
    printf("Div e igual(-=)\t\ta/=b a=%d\n",a);
    a %= b; // a = a % b
    printf("Div_entera e igual(%%=)\ta%%=b a=%d\n",a);
    a = 20;
    printf("Asignacion(=)\t\ta=20 a=%d\n",a);
    b = 18;
    printf("Asignacion(=)\t\tb=18 b=%d\n\n",b);

//Operadores binarios
    printf("And(&)\t\t\ta&b=%d\n",a&b);
    printf("Or(|)\t\t\ta|b=%d\n",a|b);
    printf("Not(~)\t\t\t~a=%d\n",~a);
    printf("Xor(^)\t\t\ta^b=%d\n",a^b);
    printf("Desplazamiento_der(>>)\ta>>2=%d\n",a >> 2);
    printf("Desplazamiento_izq(<<)\ta<<2=%d\n\n",a << 2);

//Operadores logicos
    printf("And(&&)\ta&&b=%d\n",a&&b);
    printf("Or(||)\ta||b=%d\n",a||b);
    printf("Not(!)\ta!b:%d\n\n",!a);

//Operadores de comparacion
    printf("Igualdad(==):\t\ta == b:%d\n",a==b);
    printf("Desigualdad(!=):\ta != b:%d\n",a!=b);
    printf("Mayor que(>):\t\ta > b:%d\n",a>b);
    printf("Menor que(<):\t\ta < b:%d\n",a<b);
    printf("Mayor o igual(>=):\ta >= b:%d\n",a>=b);
    printf("Menor o igual(<=):\ta <= b:%d\n\n",a<=b);

    /*No tiene operadores de pertenencia, ni de identidad*/

    /**
     * Estructuras de control
    */
   char d[]= "HelierCamejo";
    
    //Condicionales
    if (strstr(d,"heliercamejo"))
    {
        printf("No importa si esta en mayuscula\n");
    }
    else if (strstr(d,"helier_camejo"))
    {
        printf("No importa si esta separado\n");
    }
    else 
    {   
        printf("Si importa si esta separado o en mayuscula\n");
    }
    //Con el operador ? tambien se puede realizar una condicional
    (strstr(d,"HelierCamejo"))?printf("Esta es una condicion positiva\n"):printf("Esta es una condicion negativa\n"); 

    //iterativas 
    int i = 0;
    printf("do{}While\n");

    do{
        printf("i=%d\n",i);
        i++;
    }while(i<10);

    printf("While\n");

    while (i<30)
    {
        printf("i=%d\n",i);
        i++;
    }

    printf("For\n");

    for (; i < 50; i++)
    {
        printf("i=%d\n",i);
    }
    
    //Expresiones de seleccion switch case
    i = 3;
    switch (i)
    {
    case 1:
        printf("i=1\n");
        break;
    case 2:
        printf("i=2\n");
        break;
    case 3:
        printf("i=3\n");
        break;
    default:
        printf("Valor por defecto\n");
        break;
    }

    /*C no tiene excepciones*/

    //Extra
    printf("Ejercicio extra\n");
    for(i = 10; i<=55;i++)
    {
        if ((i != 16) && ( i % 3 != 0) && ( i % 2 != 0) )
        {
            printf("i=%d\n",i);
        }
    }

    return 0;
}