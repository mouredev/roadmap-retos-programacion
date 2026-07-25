#include <iostream>

using std::cout;
using std::cin;

//Numeros del 100 al 0

int contador(int cont = 100) //en el mandato pide 100 asi que simplemente lo defino
{
    if(cont < 0)
    {
        return 0;
    }
    cout << cont << std::endl;
    return contador(cont-1);

}

int factorial(int n)
{
    if(n == 1 ) return 1;
    return n * factorial(n-1);
}
int main()
{
    contador();

    //Dificultad Opcional ::  Factorial de un numero
    int nFactorial;
    cout << "Ingresa un numero: ";
    cin >> nFactorial; cout << "El Factorial de " << nFactorial << " Es " << factorial(nFactorial);
    return 0;
}