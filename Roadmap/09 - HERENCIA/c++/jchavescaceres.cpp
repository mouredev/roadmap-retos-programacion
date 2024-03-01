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

		virtual void print();
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

void Employee::print() {
	std::cout << "id: " << id << " nombre: " << name << " , empleados a su cargo: \n" ;
	for (std::list<Employee*>::iterator it=listSubordinates.begin(); it != listSubordinates.end(); ++it) {
	      (*it)->print();
	}
}

class GeneralManager : public Employee {
	private:
		const std::string department;
	
	public:
		GeneralManager (unsigned int inId, std::string inName, std::string inDepartment);
		std::string getDepartment();

		virtual void print();
};

GeneralManager::GeneralManager (unsigned int inId, std::string inName, std::string inDepartment) : 
	Employee (inId, inName), department (inDepartment) {

};

std::string GeneralManager::getDepartment() {
	return department;
}

void GeneralManager::print() {
	std::cout << "Gerente - departamento : " << department << " ";
	Employee::print();
}

class ProjectManager : public Employee {
	private:
		const std::string project;
	
	public:
		ProjectManager (unsigned int inId, std::string inName, std::string inProject);
		std::string getProject();

		virtual void print();
};

ProjectManager::ProjectManager (unsigned int inId, std::string inName, std::string inProject) : 
	Employee (inId, inName), project (inProject) {

};

std::string ProjectManager::getProject() {
	return project;
}

void ProjectManager::print() {
	std::cout << "  Jefe de proyecto - proyecto : " << project << " ";
	Employee::print();
}

class Developer : public Employee {
	private:
		const std::string mainProgrammingLanguage;
	
	public:
		Developer (unsigned int inId, std::string inName, std::string inMainProgrammingLanguage);
		std::string getMainProgrammingLanguage();

		virtual void print();
};

Developer::Developer (unsigned int inId, std::string inName, std::string inMainProgrammingLanguage) : 
	Employee (inId, inName), mainProgrammingLanguage (inMainProgrammingLanguage) {

};

std::string Developer::getMainProgrammingLanguage() {
	return mainProgrammingLanguage;
}

void Developer::print() {
	std::cout << "    Desarrollador - Lenguaje principal : " << mainProgrammingLanguage << " ";
	Employee::print();
}

int main() {

	unsigned int identificador = 1;

	const Animal* C_ARRAY_ANIMALS [] = {
		new Dog(),
		new Cat(),
		new Cat(),
		new Dog(),
		new Cat()};

	for (int i = 0; i < sizeof (C_ARRAY_ANIMALS) / sizeof (Animal*); i++) {
		C_ARRAY_ANIMALS [i]->printSound();
	};

	//Dificultad extra
	GeneralManager manager (identificador++, "Gerente" , "Departamento");
	ProjectManager projectManager1 (identificador++, "Jefe proyecto1" , "Proyecto1");
	ProjectManager projectManager2 (identificador++, "Jefe proyecto1" , "Proyecto1");
	Developer developer1 (identificador++, "Desarrollador1", "Java");
	Developer developer2 (identificador++, "Desarrollador2", "Html");
	Developer developer3 (identificador++, "Desarrollador3", "Java");

	Developer developer4 (identificador++, "Desarrollador4", "C++");
	Developer developer5 (identificador++, "Desarrollador5", "Java");

	manager.addSubordinate (&projectManager1);
	manager.addSubordinate (&projectManager2);
	projectManager1.addSubordinate (&developer1);
	projectManager1.addSubordinate (&developer2);
	projectManager1.addSubordinate (&developer3);
	projectManager2.addSubordinate (&developer4);
	projectManager2.addSubordinate (&developer5);

	manager.print();


	//Free memory
	for (int i = 0; i < sizeof (C_ARRAY_ANIMALS) / sizeof (Animal*); i++) {
		delete C_ARRAY_ANIMALS [i];
	};

	return 0;
};
