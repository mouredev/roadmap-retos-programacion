// @RoniPG

#include <iostream>
#include <set>
#include <string>
#include <cstring>
#include <algorithm>

void Palindromo(std::string);
void Anagrama(std::string,std::string);
void Isograma(std::string);

int main(){

	std::string ejemplo="Hola Mundo";
	std::string ejemplo2("Hello World");
	std::string vacio="";
	std::basic_string <char> alias_string; //std::basic_string es la superclase de la clase std::string


	size_t encontrar = ejemplo.find("Mundo");
	(encontrar!=std::string::npos) // --> std::string::npos Se utiliza para verificar si la subcadena fue encontrada o no.
	? std::cout << "Valor encontrado" << std::endl : std::cout << "Valor encontrado"<<std::endl;
	std::cout << ejemplo.append ("\tAñadido") // --> Añade al final de la cadena de carateres otra cadena de caracteres que le pasemos
	<<	std::endl;
	std::cout << ejemplo.assign (ejemplo2) // --> Sobrescribe el valor que le pasamos como parametro
	<< std::endl;
	ejemplo="Hola Mundo";
	std::cout << ejemplo.at(1) // --> Devuelve el valor en la poscion que le indiquemos
	<< std::endl;
	std::cout << ejemplo.back() // --> Devuelve el ultimo valor de la cadena de caracteres
	<< std::endl;
	char * c_str = new char [ejemplo.length()+1];
	std::string::iterator begin =ejemplo.begin(); // --> Devuelve un iterador que apunta al primer carácter de la cadena
	std::strcpy(c_str,ejemplo.c_str()); // --> Devuelve un puntero a una cadena de caracteres estilo C(terminada en NULL(\0))
	std::cout<< c_str << std::endl;
	std::cout << ejemplo.capacity() // --> Devuelve el numero maximo de caracteres que puede contener sin necesidad de asignar mas memoria
	<< std::endl;
	std::string::const_iterator iter = ejemplo.cbegin(); // --> Devuelve un iterador constante que apunta a la primera posicion de la cadena de caracteres
	for( /*no hace falta iniciar el iterador*/;
	iter != ejemplo.cend(); // --> Devuelve un iterador constante que apunta a la ultima posicion de la cadena de caracteres
	iter++){std::cout<<*iter<<std::endl;}
	std::cout << "antes del clear: "<<ejemplo<<std::endl; ejemplo.clear(); // --> Vacia la cadena y libera el espacio en memoria asociada a su almacenamiento
	std::cout << " Despues del clear: "<<ejemplo<<std::endl;
	ejemplo.append("Hola Mundo");
	std::cout << ejemplo.compare("Hola Mundo") // -->Compara dos cadenas de caracteres y devuelve un numero con la diferencia lexicografica
	<< std::endl;														//		entre las dos cadenas
	char buffer[ejemplo.length()]; size_t copy = ejemplo.copy(buffer, 6, 0); // --> Copiar una parte de una cadena en otro array o buffer
	buffer[copy]='\0'; std::cout << buffer << std::endl; //
	std::string::const_reverse_iterator crbegin=ejemplo.crbegin();// --> Devuelve un iterador constante que apunta a la primera posicion de la cadena de caracteres
																  //	 en orden inverso
	for( /*no hace falta iniciar el iterador*/;
	crbegin != ejemplo.crend(); // --> Devuelve un iterador constante que apunta a la ultima posicion de la cadena de caracteres contando en orden inverso
	crbegin++){std::cout<<*crbegin;}
	std::cout << std::endl;
	const char * const_data = ejemplo.data(); // --> Obtener un puntero al array de caracteres internos de una cadena(para lectura)
	std::cout << const_data << std::endl;
	char * no_const_data = const_cast<char *>(ejemplo.data()); // --> Obtener un puntero al array de caracteres internos de una cadena(para lectura/escritura)
	no_const_data[0]='h'; std::cout << no_const_data << std::endl;
 	std::cout << std::boolalpha << ejemplo.empty() // --> Verifica si la cadena esta vacia, si esta vacia devuelve True sino False.
	<< std::endl;
 	std::string::iterator end = ejemplo.end(); // --> Devuelve un iterador que apunta justo despues del ultimo caracter de la cadena
 	std::cout << ejemplo.erase(6) // --> Se utiliza para eliminar datos dentro de una cadena ya sea por posicion o por rango
 	<< std::endl;
 	ejemplo= "Hola Mundo";
	std::cout << ejemplo.find("ola") // --> Se utiliza para buscar un caracter o una cadena de caracteres especifica, devuelve la posicion de la cadena/caracter
	<< std::endl;
	std::cout << "first not of: "<< ejemplo.find_first_not_of("ola") // -->Se utiliza para buscar cualquier caracter de una cadena de caracteres dada, devuelve la primera posicion que no coincida con la cadena de caracteres dada
	<< std::endl;
	std::cout << "first of: "<< ejemplo.find_first_of("ola") // --> Se utiliza para buscar cualquier caracter de una cadena de caracteres dada, devuelve la primera coincidencia encontrada
	<< std::endl;
	std::cout << "last not of: "<<ejemplo.find_last_not_of("ola") // --> Se utiliza para buscar cualquier caracter de una cadena de caracteres dada, devuelve la ultima posicion que no coincida con la cadena de caracteres dada
	<< std::endl;
	std::cout << "last of: "<<ejemplo.find_last_of("ola") // --> Se utiliza para buscar cualquier caracter de una cadena de caracteres dada, devuelve la ultima coincidencia encontrada
	<< std::endl;
	char& front = ejemplo.front(); // --> Devuelve una referencia al primer carácter de la cadena
	std::cout << front	<< std::endl;
	std::allocator<std::string> myAllocator = ejemplo.get_allocator(); // --> Devuelve el objeto allocator asociado con la cadena
	std:: string* my_string = myAllocator.allocate(1);
	new (my_string) std::string(ejemplo, myAllocator);
	std::cout << "Valor del string construido: " << *my_string << std::endl;
	my_string->~basic_string(); myAllocator.deallocate(my_string, 1);
	ejemplo.insert(ejemplo.end(),{' ','N','u','e','v','o'}); // --> Inserta elementos dentro de la cadena
	std::cout << ejemplo << std::endl;
	std::cout << ejemplo.length() // --> Se utiliza para obtener la longitud (número de caracteres) de la cadena de caracteres
	<< std::endl;
	std::cout << ejemplo.max_size() // --> Devuelve el tamaño máximo posible que puede tener la cadena de caracteres
	<< std::endl;
	std::cout << ejemplo.operator +=('o') << std::endl; // -->  Invocar explícitamente el operadorX como un metodo()
	ejemplo.pop_back(); // --> Se utiliza para eliminar el último carácter de una cadena
	std::cout << std::endl;
	ejemplo.push_back('.'); // --> Se utiliza para añadir un caracter en la ultima posicion de una cadena
	std::cout << ejemplo << std::endl;
	std::string::reverse_iterator rbegin = ejemplo.rbegin(); // --> Se utiliza para obtener un iterador que apunta al último elemento de una cadena ya que la 'r' se refiere a reversa.
	std::string::reverse_iterator rend = ejemplo.rend(); // --> Se utiliza para obtener un iterador que apunta al primer elemento de una cadena ya que la 'r' se refiere a reversa..
	for (;rbegin != rend; ++rbegin) { std::cout << *rbegin;	} std::cout<<std::endl;
	std::cout << ejemplo.replace(2, 4, "123") // --> Se utiliza para reemplazar subcadenas en una cadena dada
	<< std::endl;
	std::cout << ejemplo.rfind('o') // --> Es utilizada para buscar la última ocurrencia de una subcadena dentro de una cadena.
	<<std::endl;
	std::cout << "Tamaño antes del reserve: " << ejemplo.capacity() << std::endl;
	ejemplo.reserve(20); // --> Se utiliza para reservar espacio en la memoria para una cadena de caracteres
	std::cout << "Tamaño despues del reserve: "<< ejemplo.capacity() << std::endl;
	std::cout << "Tamaño antes del resize: " << ejemplo.length() << " cadena: " << ejemplo << std::endl;
	ejemplo.resize(20,'*'); // --> Se utiliza para cambiar el Tamaño de la cadena
	std::cout << "Tamaño despues del resize: "<< ejemplo.length() << " cadena: " << ejemplo << std::endl;
	std::cout << "Tamaño antes del shrink_to_fit: " << ejemplo.capacity() << std::endl;
	ejemplo.shrink_to_fit(); // --> Se utiliza para reducir la capacidad de la cadena al mínimo necesario para almacenar su contenido actual
	std::cout << "Tamaño despues del shrink_to_fit: "<< ejemplo.capacity() << std::endl;
	std::cout << ejemplo.size() << std::endl; // --> Se utiliza para obtener el número de caracteres en la cadena
	std::cout << ejemplo.substr(4) << std::endl; // --> Se utiliza para extraer una subcadena de la cadena original
	std::cout << "Ejemplo antes del intercambio: " << ejemplo << std::endl;
    std::cout << "Ejemplo 2 antes del intercambio: " << ejemplo2 << std::endl;
	ejemplo.swap(ejemplo2); // --> Se utiliza para intercambiar el contenido de dos cadenas.
	std::cout << "Ejemplo despues del intercambio: " << ejemplo << std::endl;
	std::cout << "Ejemplo 2 despues del intercambio: " << ejemplo2 << std::endl;

	/* DIFICULTAD EXTRA (opcional):
	 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
	 * para descubrir si son:
	 * - Palíndromos
	 * - Anagramas
	 * - Isogramas
	 */

	Palindromo("Anilina");
	Anagrama("Amor", "Roma");
	Isograma("Centrifugado");

	return 0;
}
void Palindromo(std::string a){
	/* Palindromo:
	 * Palabra o frase cuyas letras están dispuestas de tal manera que resulta la misma leída de izquierda a derecha que de derecha a izquierda.
	 * Por ejemplo: anilina
	 */
	std::string subA=a;
	std::string aux="";
	std::transform(subA.begin(), subA.end(), subA.begin(), ::tolower);
	std::string::reverse_iterator aReverse= subA.rbegin();
	std::string::reverse_iterator rend= subA.rend();
	for(;aReverse != rend;aReverse++){
		aux += *aReverse;
	}
	if (subA.compare(aux)==0) {
		std::cout << "La palabra: "<<a<<".Es Palindromo" << std::endl;
	}else {
		std::cout << "La palabra: "<<a<<".No es Palindromo"<< std::endl;
	}
}
void Anagrama(std::string a,std::string b){
	/* Anagrama:
	 * Cambio en el orden de las letras de una palabra o frase que da lugar a otra palabra o frase distinta.
	 * Por ejemplo: Amor --> Roma
	 */
	std::string a1=a;
	std::string b1=b;
	std::transform(a1.begin(), a1.end(), a1.begin(), ::tolower);
	std::transform(b1.begin(), b1.end(), b1.begin(), ::tolower);
	std::sort(a1.begin(), a1.end());
	std::sort(b1.begin(), b1.end());
	if (a1.compare(b1)==0) {
		std::cout << a << " y " << b << " son Anagramas" << std::endl;
	} else {
		std::cout << a << " y " << b << " no son Anagramas" << std::endl;
	}
}
void Isograma(std::string a){
	/* Un isograma es una palabra o frase en la que cada letra aparece el mismo número de veces.
	 * Si cada letra aparece solo una vez será un heterograma, si aparece dos, un isogroma de segundo orden y así sucesivamente.
	 * Por ejemplo:
	 * Heterogramas: yuxtaponer, centrifugado, luteranismo.
	 * Isogramas con una repetición o de segundo orden: acondicionar, escritura, intestinos.
	 */
	bool flag=false;
	int count=0;
	std::transform(a.begin(), a.end(), a.begin(), ::tolower);
	std::set<char> subA;
	for ( int i = 0; i < a.length(); i++) {
		subA.insert(a.at(i));
	}
	for(char character: subA){
		for (int i = 0; i < a.length(); i++) {
			if (character == a.at(i)) {
				count++;
			}
		}
		std::cout << "La letra: \""<<character<<"\" esta repetida: " << count << " veces."<<std::endl;
		if(count>1){
			flag=true;
		}
		count=0;
	}
	if (flag) {
		std::cout<<"Es un isograma"<<std::endl;
	}else {
		std::cout<<"Es un heterograma"<<std::endl;
	}
}
