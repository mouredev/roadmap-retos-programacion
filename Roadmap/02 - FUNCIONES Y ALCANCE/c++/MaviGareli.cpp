#include <iostream>
#include <string>

/*!
*Funcion: printHIMsg()\n
*Brief: Imprime un mensaje de bienvenida\n
*@param none \n
*@return none\n
*/
void printHiMsg();


/*!
*Funcion: print()\n
*Brief: Imprime un mensaje dado\n
*@param string \n
*@return none\n
*/
void print(std::string message);


/*!
*Funcion: print()\n
*Brief: Imprime un numero entero dado\n
*@param int \n
*@return none\n
*/
void print(int number);


/*!
*Funcion:printNumberList()\n
*Brief: La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
*   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
*   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
*   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
*   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.\n
*@param string, string\n
*@return int\n
*/
int printNumberList(std::string message1, std::string message2);


//Variable global
int counterGlobal = 0;

int main()
{
    //Variables locales
    std::string message1 = "Soy un multiplo de 3 ";
    std::string message2 = "Soy un multiplo de 5";
    printHiMsg();
    printNumberList(message1, message2);
    
    counterGlobal = 0;  //Se resetea el contador, para que no se acumulen los valores al llamar nuevamente la funcion
    int result = printNumberList(message1, message2);
    
    print("El numero de veces que se ha impreso un numero es: ");
    print(result);
    return 0;
 
}

void printHiMsg()
{
    std::cout << "Bienvenido!" << std::endl;
}

void print(std::string message)
{
    std::cout << message;
}


void print(int number)
{
    std::cout << number;
}


int printNumberList(std::string message1, std::string message2)
{   
    /*Aqui seria mejor poner la variable counter, para evitar resetearla cada vez que se llama a la funcion. 
    Se hizo global con fines de demostracion
    */
    for(int i = 1; i <= 100; i++)
    {
        print(i);
        if(i % 3 == 0 && i % 5 == 0)
        {
            print(" " + message1 + message2);
            
        }
        else if( i% 3 == 0)
        {
            print(" " + message1);
        }
        else if( i% 5 == 0)
        {
            print(" " + message2);
        }
        else
        {
            counterGlobal++;
        }
        std::cout << std::endl;
    }
    return counterGlobal; 

}