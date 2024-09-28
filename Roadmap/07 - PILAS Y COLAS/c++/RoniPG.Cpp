//@ Roni
#include <iostream>
#include <string>
#include <stack>
#include <queue>
#include <algorithm>

void Programa1();
void Programa2();
bool Contains(std::stack<std::string> pila, std::string texto);
int IndexOf(std::stack<std::string> pila, std::string texto);
std::string GetPos(std::stack<std::string> pila, int pos);
std::string ToLower(std::string texto);

int main() {
	/*
	 * EJERCICIO: Implementa los mecanismos de introducción y recuperación de
	 * elementos propios de las pilas (stacks - LIFO) y las colas (queue - FIFO)
	 * utilizando una estructura de array o lista (dependiendo de las posibilidades
	 * de tu lenguaje).
	 */

	//PILA (STACK)
	// Declarar un Stack de strings
	std::stack<std::string> pila;

	// Insertar elementos en el Stack
	pila.push("Hola");
	pila.push("Mundo");
	pila.push("!");

	// Mostrar el tamaño del Stack
	std::cout << "Tamaño del Stack: " << pila.size() << std::endl;

	// Acceder al elemento en la cima del Stack
	std::cout << "Elemento en la cima del Stack: " << pila.top() << std::endl;

	// Eliminar elementos del Stack
	pila.pop();
	std::cout << "Tamaño del Stack después de eliminar un elemento: "
			<< pila.size() << std::endl;

	// COLA(QUEUE)
	// Crear una cola de strings
	std::queue<std::string> cola;

	// Agregar elementos a la cola
	cola.push("Hola");
	cola.push("Mundo");
	cola.push("!");

	// Mostrar el primer elemento de la cola
	std::cout << "Primer elemento de la cola: " << cola.front() << std::endl;

	// Eliminar el primer elemento de la cola
	cola.pop();

	// Mostrar el nuevo primer elemento de la cola
	std::cout << "Nuevo primer elemento de la cola: " << cola.front()
			<< std::endl;

	// Mostrar el tamaño de la cola
	std::cout << "Tamaño de la cola: " << cola.size() << std::endl;
	/*
	 * DIFICULTAD EXTRA (opcional): - Utilizando la implementación de pila y cadenas
	 * de texto, simula el mecanismo adelante/atrás de un navegador web. Crea un
	 * programa en el que puedas navegar a una página o indicarle que te quieres
	 * desplazar adelante o atrás, mostrando en cada caso el nombre de la web. Las
	 * palabras "adelante", "atras" desencadenan esta acción, el resto se interpreta
	 * como el nombre de una nueva web.
	 */
	Programa1();
	/*
	 * - Utilizando la implementación de cola y cadenas de texto, simula el
	 * mecanismo de una impresora compartida que recibe documentos y los imprime
	 * cuando así se le indica. La palabra "imprimir" imprime un elemento de la
	 * cola, el resto de palabras se interpretan como nombres de documentos.
	 */
	Programa2();

	return 0;
}
void Programa1() {
	std::stack<std::string> url;
	url.push("www.google.com");
	url.push("www.twitter.com");
	url.push("www.gmail.com");
	std::string texto = "";
	int pos = 0;
	do {
		std::cout << "\n*******Navegación web*******\n" << std::endl;
		std::cout << "Escribe la url de la página web para dirigirte a ella."
				<< std::endl;
		std::cout << "Si la url no existe se creara una nueva web" << std::endl;
		std::cout << "Escribe 'adelante' para ir a la siguiente web."
				<< std::endl;
		std::cout << "Escribe 'atras' para ir a la web anterior." << std::endl;
		std::cout << "Escribe 'salir' para cerrar el programa." << std::endl;
		std::cout << "Escribe aquí: " << std::endl;
		getline(std::cin, texto);
		if (ToLower(texto) == "adelante") {	// -->Implementamos un metodo que convierte el texto a minusculas sin modificar su contenido original
			if (pos + 1 >= url.size()) {
				std::cout << "Ya te encuentras en la url del final"
						<< std::endl;
				std::cout << url.top() << std::endl;
				pos = url.size() - 1;
			} else {
				std::cout << "Avanzamos" << std::endl;
				std::cout << GetPos(url, pos + 1) << std::endl;
				pos += 1;
			}
		} else if (ToLower(texto) == "atras") {
			if (pos <= 0) {
				std::cout << "Ya te encuentras en la url del principio"
						<< std::endl;
				std::cout << GetPos(url, pos) << std::endl;
				pos = 0;
			} else {
				std::cout << "Retrocedemos" << std::endl;
				std::cout << GetPos(url, pos - 1) << std::endl;
				pos -= 1;
			}
		} else if (ToLower(texto) == "salir") {
			std::cout << "Vuelva pronto" << std::endl;
		} else if (Contains(url, texto)) { //--> Implementamos un metodo que compruebe la pila
			std::cout << "Encotramos la url en la posición: ";
			pos = IndexOf(url, texto); //--> Implementamos un metodo que devuelve la posicion en donde se ha encontrado la coincidencia
			std::cout << pos << std::endl;
			pos -= 1;
		} else {
			std::cout << "Añadimos nueva url" << std::endl;
			url.push(texto);
		}

	} while (texto != "salir");

}
bool Contains(std::stack<std::string> pila, std::string texto) {
	while (!pila.empty()) {
		if (pila.top() == texto) {
			return true;
		}
		pila.pop();
	}
	return false;
}
std::string ToLower(std::string texto) {
	std::transform(texto.begin(), texto.end(), texto.begin(), ::tolower);
	return texto;
}
int IndexOf(std::stack<std::string> pila, std::string texto) {
	int count = pila.size();
	while (!pila.empty()) {
		if (pila.top() == texto) {
			return count;
		}
		pila.pop();
		count--;
	}
	return count;
}
std::string GetPos(std::stack<std::string> pila, int pos) {
	int count = pila.size() - pos;
	std::string aux = "";
	for (int i = 0; i < count; ++i) {
		aux = pila.top();
		pila.pop();
	}
	return aux;
}
void Programa2() {
	std::queue<std::string> doc;
	doc.push("Documento 1");
	doc.push("Documento 2");
	doc.push("Documento 2");
	std::string texto = "";

	do {
		std::cout << "\n*******Mecanismo de una impresora*******\n"
				<< std::endl;
		std::cout
				<< "Escribe 'imprimir' para ir a la imprimir el primer documento de la cola."
				<< std::endl;
		std::cout
				<< "Si no, introduce el nombre del nuevo documento a imprimir y se añaadira a la cola"
				<< std::endl;
		std::cout << "Escribe 'salir' para cerrar el programa." << std::endl;
		std::cout << "Escribe aquí: " << std::endl;
		std::getline(std::cin, texto);
		if (ToLower(texto) == "imprimir") {
			std::cout << "Procedemos a imprimir el documento: " << doc.front()
					<< std::endl;
			doc.pop();
		} else if (ToLower(texto) == "salir") {
			std::cout << "Vuelva pronto" << std::endl;
		} else {
			std::cout << "Introducimos el nuevo documento" << std::endl;
			doc.push(texto);
		}
	} while (ToLower(texto) != "salir");
}
