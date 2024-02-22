/*
 * EJERCICIO:
 * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
 * atributos y una función que los imprima (teniendo en cuenta las posibilidades
 * de tu lenguaje).
 * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
 * utilizando su función.
 *
 * DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido.
 * 
 */

#include <iostream>
#include <stdio.h>
#include <string.h>

class MyClass {

	private:

		int arg1;
		long arg2;

	public:

		MyClass (int inArg1, int inArg2);

		int getArg1 ();
		long getArg2 ();

		void setArg1 (int inArg1);
		void setArg2 (long inArg2);

		void print ();
};

MyClass::MyClass (int inArg1, int inArg2) :
	arg1 (inArg1), arg2 (inArg2) {
};

int MyClass::getArg1 () {
	return arg1;
};

long MyClass::getArg2 () {
	return arg2;
};


void MyClass::setArg1 (int inArg1) {
	arg1 = inArg1;

};

void MyClass::setArg2 (long inArg2) {
	arg2 = inArg2;
};

void MyClass::print () {
	std::cout << "MyClass : arg1:" << arg1 << ", arg2:" << arg2 << "\n";
};

//Element abstract class, setPrint must be overwrite
class Element {
	private:
		Element *previousElement;
		Element *nextElement;

	protected:
		Element ();
	public:
		virtual Element* getPreviousElement();
		virtual Element* getNextElement();

		virtual void setPreviousElement(Element *inElement);
		virtual void setNextElement(Element *inElement);

		virtual void print() = 0;
};

Element::Element () : previousElement (NULL), nextElement (NULL) {
};

Element* Element::getPreviousElement() {
	return previousElement;
};

Element* Element::getNextElement() {
	return nextElement;
};


void Element::setPreviousElement(Element *inElement) {
	previousElement = inElement;
};

void Element::setNextElement(Element *inElement) {
	nextElement = inElement;
};


//Generic Storage
class Storage {

	protected:
		Element *firstElement;
		Element *lastElement;

		Storage ();

	public:
		virtual int isStorageEmpty();
		virtual unsigned long getElementsCount();
		virtual void push (Element *inElement);
		virtual Element* pop () =0;

		virtual void print();
};

Storage::Storage () : firstElement (NULL), lastElement (NULL) {
};

int Storage::isStorageEmpty() {

	return firstElement == NULL;
};

unsigned long Storage::getElementsCount() {

	Element *currentElement = firstElement;
	unsigned long totalElements = 0;

	while (currentElement != NULL) {
		totalElements++;
		currentElement = currentElement->getNextElement();
	};
	return totalElements;
};

void Storage::push (Element *newElement) {
	/* Add new element at the end of the list*/

	newElement->setPreviousElement (lastElement);
	newElement->setNextElement (NULL);
	
	if (firstElement == NULL) {
		firstElement = newElement;
	};

	if (lastElement == NULL) {
		lastElement = newElement;
	} else {
		lastElement->setNextElement (newElement);
		lastElement = newElement;
	};

};

void Storage::print() {
	Element *currentElement = firstElement;
	unsigned long totalElements = 0;

	while (currentElement != NULL) {
		currentElement->print();
	};
};


//Queue Storage
class Queue : public Storage {

	public:
		Queue();
		virtual Element* pop () =0;
};

Queue::Queue() : Storage() {
};

//FIFO
Element* Queue::pop () {
	Element *element = NULL;
	Element *nextElement = NULL;

	if (firstElement != NULL) {
		element = firstElement;

		nextElement = firstElement->getNextElement();

		if (nextElement != NULL) { 
			firstElement = nextElement;
			firstElement->setPreviousElement (NULL);
		} else {
			firstElement = NULL;
			lastElement = NULL;
		};
	};

	return element;
};

//Stack Storage
class Stack : public Storage {

	public:
		Stack();
		virtual Element* pop () =0;
};

Stack::Stack() : Storage() {
};

//LIFO
Element* Stack::pop () {
	Element *element = NULL;
	Element *previousElement = NULL;

	if (lastElement != NULL) {
		element = lastElement;

		previousElement = lastElement->getPreviousElement();

		if (previousElement != NULL) { 
			lastElement = previousElement;
			lastElement->setNextElement (NULL);
		} else {
			firstElement = NULL;
			lastElement = NULL;
		};
	};

	return element;
};

//Document element
class Document : public Element {
	private:
		char* page;
	public:
		Document (const char* inPage);
		~Document ();
		virtual void print();
};

Document::Document (const char* inPage) : page (NULL) {
	if (inPage != NULL) {
		page = (char*)malloc (strlen (inPage)+1);
		strcpy (page, inPage);
	};
};

Document::~Document () {
	free (page);
};

void Document::print() {
	std::cout << "Page " << page << "\n";
};

//WebPage element, same as Document
class WebPage : public Document {
	public:
		WebPage (const char* inPage);
};

WebPage::WebPage (const char* inPage) : Document (inPage) {
};

 /*
 * DIFICULTAD EXTRA (opcional):
 * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
 *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
 *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
 *   Las palabras "adelante", "atras" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
 */
//void webBrowserSimulator() {
//
//	const char* C_ADELANTE = "adelante";
//	const char* C_ATRAS = "atras";
//	const char* C_SALIR = "salir";
//	const unsigned int C_SIZE_BUFFER = 200;
//
//	char myBuffer [C_SIZE_BUFFER];
//	memset (myBuffer, 0, sizeof (myBuffer));
//
//	char myExit = 0;
//	char *page = NULL;
//
//	Queue queueBack, queueNext;
//
//	/*
//	A: 
//	B: push back (old page), empty queue_next
//	C: push back (old page), empty queue_next
//	atras: pop lifo back -> str, push str
//	atras: pop lifo back -> str, push str
//	delante: pop lifo next -> str, push back
//
//
//	A B C
//	atras
//	B 
//	atras
//	A
//	delante
//	B
//	D
//	E
//	atras
//	E
//	atras
//	D
//	atras
//	B
//	*/
//
//	while (!myExit) {
//
//		printf ("Página? %s? %s? o %s?: ", C_ADELANTE, C_ATRAS, C_SALIR);
//		fgets (myBuffer, C_SIZE_BUFFER, stdin);
//		myBuffer [strlen (myBuffer)-1] = '\0'; /* remove \n */
//
//		if (!strcmp (myBuffer, C_SALIR)) {
//			myExit = 1;
//		} else if (!strcmp (myBuffer, C_ATRAS)) {
//			/* save previous page */
//			if (page != NULL) {
//				push (&queueNext, page);
//			}
//			page = (char*) pop_lifo (&queueBack);
//			
//		} else if (!strcmp (myBuffer, C_ADELANTE)) {
//			/* save previous page */
//			if (page != NULL) {
//				push (&queueBack, page);
//			}
//			page = (char*) pop_lifo (&queueNext);
//		} else {
//
//			/* save previous page */
//			if (page != C_NULL_ELEMENT_TYPE) {
//				push (&queueBack, page);
//			}
//
//			/* empty queue next */
//			while ( (page=(char*)pop_lifo (&queueNext)) != NULL) {
//				free (page);
//			}
//
//			page = malloc (strlen (myBuffer)+1);
//			strcpy (page, myBuffer);
//		};
//
//		if (page != C_NULL_ELEMENT_TYPE) {
//			printf ("Display %s\n", page);
//		} else {
//			printf ("No hay más páginas \n");
//		}
//
//	};
//
//	free (page);
//
//	while ( (page=(char*)pop_lifo (&queueNext)) != NULL) {
//		free (page);
//	}
//	while ( (page=(char*)pop_lifo (&queueBack)) != NULL) {
//		free (page);
//	}
//
//
//}

int main () {

 	MyClass myObject (1, 2);

	myObject.setArg1 (3);
	myObject.setArg2 (4);
	myObject.print();

	return 0;
};
