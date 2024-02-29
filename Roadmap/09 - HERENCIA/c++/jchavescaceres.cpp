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
#include <string>
#include <list>

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
	return "guau";
};

class Cat : public Animal {

	public:
 		virtual const char* sound() const;
};

const char* Cat::sound() const {
	return "miau";
};

class Employee {
	private:
		const unsigned int id;
		const std::string name;
		std::list<Employee*> listSubordinates;
		
	protected:
		Employee (unsigned int inId, std::string inName);
	
	public:
		int getId();
		std::string getName();

		void addSubordinate (Employee* inEmployee);
		std::list<Employee*> getListSubordinates();
};

Employee::Employee (unsigned int inId, std::string inName) :
	id (inId), name (inName), listSubordinates() {

};

int Employee::getId() {
	return id;
};

std::string Employee::getName() {
	return name;
};

void Employee::addSubordinate (Employee* inEmployee) {

	listSubordinates.push_back (inEmployee);

};

std::list<Employee*> Employee::getListSubordinates() {
	return listSubordinates;
};


class GeneralManager : public Employee {
	private:
		const std::string department;
	
	public:
		GeneralManager (unsigned int inId, std::string inName, std::string inDepartment);
		std::string getDepartment();

};

GeneralManager::GeneralManager (unsigned int inId, std::string inName, std::string inDepartment) : 
	Employee (inId, inName), department (inDepartment) {

};

std::string GeneralManager::getDepartment() {
	return department;
}

class ProjectManager : public Employee {
	private:
		const std::string project;
	
	public:
		ProjectManager (unsigned int inId, std::string inName, std::string inProject);
		std::string getProject();

};

ProjectManager::ProjectManager (unsigned int inId, std::string inName, std::string inProject) : 
	Employee (inId, inName), project (inProject) {

};

std::string ProjectManager::getProject() {
	return project;
}

class Developer : public Employee {
	private:
		const std::string project;
	
	public:
		Developer (unsigned int inId, std::string inName, std::string inProject);
		std::string getProject();

};

Developer::Developer (unsigned int inId, std::string inName, std::string inProject) : 
	Employee (inId, inName), project (inProject) {

};

std::string Developer::getProject() {
	return project;
}

/*
 * DIFICULTAD EXTRA (opcional):
 * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 * actividad, y almacenan los empleados a su cargo.
 */

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
};
