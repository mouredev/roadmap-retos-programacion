// En C++, no se pueden crear funciones dentro de otras funciones.

#include <iostream>

// VARIABLE GLOBAL
char globalVar[] = "global";


// FUNCION SIN PARAMETROS NI RETORNO
void voidFunc()
{

}
int intFunc()
{
	return 1;
}
char charFunc(const char *str)
{
	std::cout << "Tu caracter seleccionado: " << str << std::endl;
	return *str;
}

void ft_fizzbuzz(char *str1, char *str2)
{
	int i = 1;
	while (i < 101)
	{
		if (i % 3 == 0 && i % 5 == 0)
		{
			std::cout << str1 << str2 << std::endl;
		}
		if (i % 3 == 0 && i % 5 != 0)
		{
			std::cout << str1 << std::endl;
		}
		if (i % 5 == 0 && i % 3 != 0)
		{
			std::cout << str2 << std::endl;
		}
		if (i % 3 != 0 && i % 5 != 0)
		{
			std::cout << i << std::endl;
		}
		i++;
	}
}

int main()
{
	std::cout << "IMPRIMIR UN CARACTER DESDE OTRA FUNCION ENVIANDOLE UN PARAMETRO" << std::endl;
	char a[1];
	std::cin >> a;
	charFunc(a);

	std::cout << "\nUtiliza algún ejemplo de funciones ya creadas en el lenguaje." << std::endl;
	char z = 'z';
	char y = toupper(z); // Uso de la funcion toupper() para convertir el caracter de minuscula a mayuscula
	std::cout << y << std::endl;

	std::cout << "\nPon a prueba el concepto de variable LOCAL y GLOBAL." << std::endl;
	char localVar[] = "local";
	std::cout << localVar << std::endl;
	std::cout << globalVar << std::endl;

	std::cout << "\nDIFICULTAD EXTRA(opcional) :" << std::endl;
	char str1[20];
	char str2[20];
	std::cout << "Selecciona una palabra que no supere los 19 caracteres:" << std::endl;
	std::cin >> str1;
	std::cout << "Selecciona otra palabra que no supere los 19 caracteres:" << std::endl;
	std::cin >> str2;
	ft_fizzbuzz(str1, str2);

	return 0;
}