/*
 * EJERCICIO:
 * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
 * implemente una superclase Animal y un par de subclases Perro y Gato,
 * junto con una función que sirva para imprimir el sonido que emite cada Animal.
 *
 * DIFICULTAD EXTRA (opcional):
 * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 * actividad, y almacenan los empleados a su cargo.
 */

#include <iostream>

 class Animal {

	public:

 		virtual const char* sound() const = 0;
		virtual void printSound () const ;
 };

void Animal::printSound()  const {
	
	std::cout << sound() << "\n";

};

class Dog : public Animal {

	public:
 		virtual const char* sound() const;
};


const char* Dog::sound() const {
	return "guau guau";
};

class Cat : public Animal {

	public:
 		virtual const char* sound() const;
};

const char* Cat::sound() const {
	return "miau miau";
};

int main() {

	const Animal* C_ARRAY_ANIMALS [] = {
		new Dog(),
		new Cat(),
		new Cat(),
		new Dog(),
		new Cat()};

	for (int i = 0; i < sizeof (C_ARRAY_ANIMALS) / sizeof (Animal*); i++) {
		C_ARRAY_ANIMALS [i]->printSound();
	};

	//Free memory
	for (int i = 0; i < sizeof (C_ARRAY_ANIMALS) / sizeof (Animal*); i++) {
		delete C_ARRAY_ANIMALS [i];
	};

	return 0;
}
