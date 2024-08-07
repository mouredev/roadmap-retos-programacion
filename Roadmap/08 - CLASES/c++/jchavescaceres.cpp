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
#include <stdlib.h>
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
		//Element *previousElement;
		//Element *nextElement;

	protected:
		Element ();
	public:
		//virtual Element* getPreviousElement();
		//virtual Element* getNextElement();

		//virtual void setPreviousElement(Element *inElement);
		//virtual void setNextElement(Element *inElement);

		virtual void print() = 0;
};

Element::Element () {
};

//Generic Storage
class Storage {

	protected:
		class InnerElement {
			public:

				InnerElement() :
					element (NULL), previousElement (NULL),
					nextElement (NULL) {
				};
				Element *element;
				InnerElement *previousElement;
				InnerElement *nextElement;
		};

		InnerElement *firstElement;
		InnerElement *lastElement;

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

	InnerElement *currentElement = firstElement;
	unsigned long totalElements = 0;

	while (currentElement != NULL) {
		totalElements++;
		currentElement = currentElement->nextElement;
	};
	return totalElements;
};

void Storage::push (Element *newElement) {
	/* Add new element at the end of the list*/

	InnerElement *innerElement = new InnerElement();

	innerElement->previousElement = lastElement;
	innerElement->nextElement = NULL;
	innerElement->element = newElement;

	if (firstElement == NULL) {
		firstElement = innerElement;
	};

	if (lastElement == NULL) {
		lastElement = innerElement;
	} else {
		lastElement->nextElement = innerElement;
		lastElement = innerElement;
	};

};

void Storage::print() {
	InnerElement *currentElement = firstElement;

	while (currentElement != NULL) {
		currentElement->element->print();
		currentElement = currentElement->nextElement;
	};
};


//Queue Storage
class Queue : public Storage {

	public:
		Queue();
		virtual Element* pop ();
};

Queue::Queue() : Storage() {
};

//FIFO
Element* Queue::pop () {
	Element *element = NULL;
	InnerElement *nextElement = NULL;

	if (firstElement != NULL) {
		element = firstElement->element;

		nextElement = firstElement->nextElement;
		delete firstElement;

		if (nextElement != NULL) { 
			firstElement = nextElement;
			firstElement->previousElement = NULL;
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
		virtual Element* pop ();
};

Stack::Stack() : Storage() {
};

//LIFO
Element* Stack::pop () {
	Element *element = NULL;
	InnerElement *previousElement = NULL;

	if (lastElement != NULL) {
		element = lastElement->element;

		previousElement = lastElement->previousElement;
		delete lastElement;

		if (previousElement != NULL) { 
			lastElement = previousElement;
			lastElement->nextElement = NULL;
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
		char* document;
	public:
		Document (const char* inPage);
		Document (const Document& inDocument);
		~Document ();
		virtual void print();
};

Document::Document (const char* inPage) : document (NULL) {
	if (inPage != NULL) {
		document = (char*)malloc (strlen (inPage)+1);
		strcpy (document, inPage);
	};
};

Document::Document (const Document& inDocument) : document (NULL) {
	if (inDocument.document != NULL) {
		document = (char*)malloc (strlen (inDocument.document)+1);
		strcpy (document, inDocument.document);
	};
};

Document::~Document () {
	free (document);
};

void Document::print() {
	std::cout << "Document " << document << "\n";
};

int main () {

 	MyClass myObject (1, 2);

	myObject.setArg1 (3);
	myObject.setArg2 (4);
	myObject.print();

//Dificultad extra
	//Queue  example
	Queue queue;
	Stack stack;
	Document d1 ("1");
	Document d2 ("2");
	Document d3 ("3");
	Document d4 ("4");
	Document d5 ("5");

	std::cout << "\nEjemplo cola\n";
	queue.push (&d1);
	std::cout << "Push "; 
	d1.print();
	queue.push (&d2);
	std::cout << "Push ";
	d2.print();
	queue.push (&d3);
	std::cout << "Push ";
	d3.print();

	std::cout << "Número elementos en cola " << queue.getElementsCount() << "\n";
	std::cout << "Contenido cola: \n";
	queue.print();

	std::cout << "\n";

	//print 1
	std::cout << "pop ";
	queue.pop()->print();

	queue.push (&d4);
	std::cout << "Push "; 
	d4.print();

	//print 2
	std::cout << "pop ";
	queue.pop()->print();

	queue.push (&d5);
	std::cout << "Push "; 
	d5.print();

	//print 3
	std::cout << "pop ";
	queue.pop()->print();

	//print 4
	std::cout << "pop ";
	queue.pop()->print();

	//print 5
	std::cout << "pop ";
	queue.pop()->print();

	std::cout << "Número elementos en cola " << queue.getElementsCount() << "\n";
	queue.print();


	//Stack  example
	std::cout << "\nEjemplo pila\n";
	stack.push (&d1);
	std::cout << "Push "; 
	d1.print();
	stack.push (&d2);
	std::cout << "Push ";
	d2.print();
	stack.push (&d3);
	std::cout << "Push ";
	d3.print();

	std::cout << "Número elementos en pila " << stack.getElementsCount() << "\n";
	std::cout << "Contenido pila: \n";
	stack.print();

	std::cout << "\n";

	//print 3
	std::cout << "pop ";
	stack.pop()->print();

	stack.push (&d4);
	std::cout << "Push "; 
	d4.print();

	//print 4
	std::cout << "pop ";
	stack.pop()->print();

	stack.push (&d5);
	std::cout << "Push "; 
	d5.print();

	//print 5
	std::cout << "pop ";
	stack.pop()->print();

	//print 2
	std::cout << "pop ";
	stack.pop()->print();

	//print 1
	std::cout << "pop ";
	stack.pop()->print();

	std::cout << "Número elementos en pila " << stack.getElementsCount() << "\n";
	stack.print();

	return 0;
};
