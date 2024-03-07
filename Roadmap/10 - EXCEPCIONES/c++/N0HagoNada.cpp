#include <iostream>
#include <vector>
#include <stdexcept>

double division(double a, double b)
{
    if (b == 0)
    {
        throw std::runtime_error("Error: División por cero");
    }
    return a / b;
}

int obtenerValorIndice(const std::vector<int> &numeros, int indice)
{
    if (indice < 0 || indice >= static_cast<int>(numeros.size()))
    {
        throw std::out_of_range("Error: Índice fuera de rango");
    }
    return numeros[indice];
}

int main()
{
    try
    {
        double resultado = division(10, 0);
        std::cout << "Resultado: " << resultado << std::endl;
    }
    catch (const std::runtime_error &e)
    {
        std::cerr << e.what() << std::endl;
    }

    try
    {
        std::vector<int> numeros = {1, 2, 3};
        int valor = obtenerValorIndice(numeros, 5);
        std::cout << "Valor: " << valor << std::endl;
    }
    catch (const std::out_of_range &e)
    {
        std::cerr << e.what() << std::endl;
    }

    std::cout << "Fin del programa" << std::endl;
    return 0;
}