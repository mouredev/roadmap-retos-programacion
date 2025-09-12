// @Roni

#include<iostream>
#include<tuple>

void porValor(int a, int b);
void porReferencia(int& a, int& b);
std::tuple<int,int> intercambioPorValor(int a, int b);
std::tuple<int,int> intercambioPorReferencia(int& a, int& b);
int main(){

	//Asignación de variables por valor

	int original=5;
	int copia=original;
	std::cout<<"El valor de original: "<<original<<std::endl;
	std::cout<<"El valor de la copia: "<<copia<<std::endl;
	copia=10;
	std::cout<<"El valor de original al modificar la copia: "<<original<<std::endl;
	std::cout<<"El nuevo valor de la copia: "<<copia<<std::endl;

	//Asignación de variables por referencia

	int x=5;
	int &ref=x;
	std::cout<<"El valor de x: "<<x<<std::endl;
	std::cout<<"El valor de la referencia: "<<ref<<std::endl;
	ref=10;
	std::cout<<"El valor de x al modificar la referencia: "<<x<<std::endl;
	std::cout<<"El nuevo valor de la referencia: "<<ref<<std::endl;

	//Llamadas a funciones
	int a=5; int b=10;
	std::cout<<"Valores antes de llamar a la funcion porValor\n"
			"a: "<<a<<".\tb: "<<b<<std::endl;
	porValor(a, b);
	std::cout<<"Valores despues de llamar a la funcion porValor\n"
				"a: "<<a<<"\tb: "<<b<<std::endl;
	std::cout<<"Valores antes de llamar a la funcion porReferencia\n"
			"a: "<<a<<".\tb: "<<b<<std::endl;
	porReferencia(a, b);
	std::cout<<"Valores despues de llamar a la funcion porReferencia\n"
				"a: "<<a<<"\tb: "<<b<<std::endl;

   /* DIFICULTAD EXTRA (opcional):
	* Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
	* - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
	*   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
	*   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
	*   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
	*   Comprueba también que se ha conservado el valor original en las primeras.
	*/

	int numA=5;		int numB=10;
	std::cout<<"\nValor de numA: "<<numA<<".\tValor de numB: "<<numB<<std::endl;
	int numC;		int numD;
	std::tie(numC,numD)=intercambioPorValor(numA, numB);
	std::cout<<"Valor de numA: "<<numA<<".\tValor de numB: "<<numB<<std::endl;
	std::cout<<"Valor de numC: "<<numC<<".\tValor de numD: "<<numD<<"\n"<<std::endl;

	int&refA=numA;		int&refB=numB;
	std::cout<<"\nValor de refA: "<<refA<<".\tValor de refB: "<<refB<<std::endl;
	int valorC;int&refC=valorC;		int valorD;int&refD=valorD;
	std::tie(refC,refD)=intercambioPorReferencia(refA, refB);
	std::cout<<"Valor de refA: "<<refA<<".\tValor de refB: "<<refB<<std::endl;
	std::cout<<"Valor de refC: "<<refC<<".\tValor de refD: "<<refD<<"\n"<<std::endl;

	return 0;
}
//Funciones con variables por valor
void porValor(int a, int b){
	std::cout<<"\nEntramos en la funcion porValor"<<std::endl;
	a=45;	b=95;
	std::cout<<"Valor de la variable a: "<<a<<"\nnValor de la variable b: "<<b<<std::endl;
	std::cout<<"Salimos de la funcino porValor\n"<<std::endl;
}
//Funciones con variables por referencia
void porReferencia(int& a, int& b){
	std::cout<<"\nEntramos en la funcion porReferencia"<<std::endl;
	a=45;	b=95;
	std::cout<<"Valor de la variable a: "<<a<<"\nnValor de la variable b: "<<b<<std::endl;
	std::cout<<"Salimos de la funcino porReferencia\n"<<std::endl;
}
std::tuple<int,int> intercambioPorValor(int a, int b){
	std::cout<<"Entramos en la funcion intercambioPorValor"<<std::endl;
	int temp=a;
	a=b;
	b=temp;
	std::cout<<"Salimos de la funcion intercambioPorValor"<<std::endl;
	return std::make_tuple(a, b);
}
std::tuple<int,int> intercambioPorReferencia(int& a, int& b){
	/*Al pasarle los parametros por Referencia hay que tener en cuenta que
	 *cualquier modificación realizada dentro de la funcion cambiara el valor
	 *de la posicion de memoria que le pasemos
	 */
	std::cout<<"Entramos en la funcion intercambioPorReferencia"<<std::endl;
	/*Creamos dos variables temporales para poder intercambiar los valores sin
	 *modificar sus valores originales
	 */
	int tempA=a;
	int tempB=b;
	std::cout<<"Salimos de la funcion intercambioPorReferencia"<<std::endl;
	return std::make_tuple(tempB, tempA);
}
