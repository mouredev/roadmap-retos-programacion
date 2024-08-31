// @Roni

#include<iostream>
#include<vector>
#include<string>

/*
 * EJERCICIO:
 * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
 * implemente una superclase Animal y un par de subclases Perro y Gato,
 * junto con una función que sirva para imprimir el sonido que emite cada Animal.
 */
class Animal{ // --> Superclase
public :
	void sonidoAnimal(){
		std::cout<<"Soy un animal que emite sonido\n";
	}
};
class Perro : Animal{ // --> Subclase
public:
	void sonidoAnimal(){
		std::cout<<"Soy un perro y ladro\n";
	}
};
class Gato : Animal{
public:
	void sonidoAnimal(){ // --> Subclase
		std::cout<<"Soy un gato y maúllo\n";
	}
};
/* DIFICULTAD EXTRA (opcional):
	 * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
	 * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
	 * Cada empleado tiene un identificador y un nombre.
	 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
	 * actividad, y almacenan los empleados a su cargo.
	 */
//Declaracion de clases para su posterior creación
class Empleado;
class Gerente;
class Gerente_de_Proyectos;
class Programador;
class Empleado{ // --> Superclase
//Atibutos heredables
protected :
	int identificador;
	std::string nombre;

public:
	Empleado(int identificador, std::string nombre) :
	identificador(identificador),
	nombre(nombre)
	{}
	int getIdentificador() const {
		return identificador;
	}

	void setIdentificador(int identificador) {
		this->identificador = identificador;
	}

	const std::string& getNombre() const {
		return nombre;
	}

	void setNombre(const std::string &nombre) {
		this->nombre = nombre;
	}
};
class Gerente : public Empleado{ // --> Subclase
//Atributos propios
private:
	std::string cargo;
	std::vector<Empleado> g_d_p; // --> Lista de empleados
public:
	Gerente(int identificador, std::string nombre) :
	Empleado(identificador, nombre),
	cargo("Gerente")
	{}
	//Metodos propios
	void asignarEmpleado(Empleado& gdp){
		g_d_p.push_back(gdp);
	}
	void soy(){
		std::cout<<"\nSoy: "<<this->nombre<<"\nMi cargo es: "<<this->cargo;
		for(Empleado gdp : this->g_d_p){
			std::cout<<"\nTengo a cargo a: "<<gdp.getNombre();
		}
	}

};
class Gerente_de_Proyectos : public Empleado{ // --> Subclase
//Atibutos propios
private:
	std::string cargo;
	std::vector<Empleado> programadores; // --> Lista de empleados
public:
	Gerente_de_Proyectos(int identificador, std::string nombre) :
		Empleado(identificador,nombre),
		cargo("Gerente de Proyectos")
	{}
	void asignarEncargado(Gerente& ger){
		ger.asignarEmpleado(*this);
	}
	void asignarEmpleado(Empleado& pgr){
		programadores.push_back(pgr);
	}
	void soy(){
		std::cout<<"\nSoy: "<<this->nombre<<"\nMi cargo es: "<<this->cargo;
		for(Empleado gdp : this->programadores){
			std::cout<<"\nTengo a cargo a: "<<gdp.getNombre();
		}
	}
};
class Programador : public Empleado{ // --> Subclase
//Atributos propios
private:
	std::string cargo;
public:
	Programador(int identificador, std::string nombre) :
		Empleado(identificador,nombre),
		cargo("Programador")
	{}
	void asignarEncargado(Gerente_de_Proyectos& gdp){
		gdp.asignarEmpleado(*this);
	}
	void soy(){
		std::cout<<"\nSoy: "<<this->nombre<<"\nMi cargo es: "<< this->cargo;
	}
};


int main() {
	//Instanciamos los objetos
	Animal an; // --> Objeto animal
	Perro perro; // --> Objeto perro
	Gato gt; // --> Objeto gato
	//Llamamos a su funciones
	an.sonidoAnimal(); // --> Función de la superclase
	perro.sonidoAnimal(); // --> Función de la subclase sobreescrita
	gt.sonidoAnimal();// --> Función de la subclase

	// Instaciamos los objetos
	Gerente ger1(0,"A"); // --> Objeto gerente
	Gerente ger2(1,"B"); // --> Objeto gerente
	Gerente_de_Proyectos gdp1(2,"C"); // --> Objeto gerente de proyectos
	Gerente_de_Proyectos gdp2(3,"D"); // --> Objeto gerente de proyectos
	Programador pgr1(4,"E"); // --> Objeto gerente de programador
	Programador pgr2(5,"F"); // --> Objeto gerente de programador
	// Le asignamos un empleado(Gerente de proyecto) al Gerente
	ger1.asignarEmpleado(gdp1); // --> Le asignamos un empleado
	ger1.soy(); // --> Llamamos a la función propia del Gerente
	// Le asignamos un Encargado(Gerente) al Gerente de proyecto
	gdp2.asignarEncargado(ger2);// --> Le asignamos un encargado
	ger2.soy(); // --> Llamamos a la función propia del Gerente
	// Le asignamos un empleado(Programador) al Gerente de proyecto
	gdp1.asignarEmpleado(pgr1);
	gdp1.soy(); // --> Llamamos a la función propia del Gerente de proyecto de proyecto sobrescrita
	// Le asignamos un Encargado(Gerente de proyecto) al Programador
	pgr2.asignarEncargado(gdp2);
	gdp2.soy();// --> Llamamos a la función propia del Gerente de proyecto de proyecto sobrescrita
	pgr1.soy();// --> Llamamos a la función propia del Programador de proyecto sobrescrita
	pgr2.soy();// --> Llamamos a la función propia del Programador de proyecto sobrescrita

	return 0;
}
