#include<iostream>
using namespace std;

class Animal{
	private:
		string nombre_animal;
		int edad_animal;
	public:
		//Constructor
		Animal(string nombre_animal, int edad_animal){
			this->nombre_animal = nombre_animal;
			this->edad_animal = edad_animal;
		}
		
		//Setters
		
		void setNombreAnimal(string nuevoNombreAnimal){
			this->nombre_animal = nuevoNombreAnimal;
		}
		
		void setNuevaEdad(int nuevaEdad){
			this->edad_animal = nuevaEdad;
		}
	
		//Getters
		
		string getNombreAnimal(){
			return nombre_animal;
		}
		
		int getEdadAnimal(){
			return edad_animal;
		}
	
		//Funcion virtual
		
		void virtual sonido() = 0;
};

class Perro : public Animal{
	public:
		//Constructor por defecto, inicializamos con la herencia animal
		Perro(string nombre_animal, int edad_animal) : Animal(nombre_animal,edad_animal){
			
		}
		
		//Ya tenemos la certeza del sonido de un perro implementamos la funcion sonido
		
		void sonido(){
			cout << "El Perro hace de sonido: Guau" << endl;
		}
};

class Gato : public Animal{
	public:
		//Constructor por defecto, inicializamos con la herencia animal
		
		Gato(string nombre_animal,int edad_animal) : Animal(nombre_animal,edad_animal){
			
		}
		
		//Ya tenemos la certeza del sonido de un gato implementamos la funcion sonido
		
		void sonido(){
			cout << "El gato hace de sonido: Miau" << endl;
		}
};

//EMPIEZA DIFICULTAD EXTRA

class Empleados{
	private:
		string nombre_empleado;
		string identificador_empleado;
	public:
		//Constructor de un empleado
		Empleados(string nombre_empleado, string identificador_empleado){
			this->nombre_empleado = nombre_empleado;
			this->identificador_empleado = identificador_empleado;
		}
		
		//Setters
		
		void setNombreEmpleado(string nuevoNombreEmpleado){
			this->nombre_empleado = nuevoNombreEmpleado;
		}
		
		void setIdentificadorEmpleado(string nuevoIdentificadorEmpleado){
			this->identificador_empleado = nuevoIdentificadorEmpleado;
		}
		
		//Getters
		
		string getNombreEmpleado(){
			return nombre_empleado;
		}
		
		string getIdentificadorEmpleado(){
			return identificador_empleado;
		}
		
		//Funciones
		virtual void actividad() = 0;
		virtual void almacen_cargo() = 0;
};

class Gerente : public Empleados{
	private:
		int anios_exp;
		string titulo_universitario;
	public:
		//Constructor
		
		Gerente(string nombre_empleado, string identificador_empleado, int anios_exp, string titulo_universitario) : Empleados(nombre_empleado,identificador_empleado){
			this->anios_exp = anios_exp;
			this->titulo_universitario = titulo_universitario;
		}
		
		//Getters
		
		int getAniosExp(){
			return this->anios_exp;
		}
		
		string getTituloUniversitario(){
			return this->titulo_universitario;
		}
		
		//Setters
		
		void setNuevosAnios(int nuevaExp){
			this->anios_exp = nuevaExp;
		}
		
		void setNuevoTitulo(string nuevo_titulo_universitario){
			this->titulo_universitario = nuevo_titulo_universitario;
		}
		
		
		//Ya tenemos clara la actividad de un Gerente programamos las funciones virtuales
		void actividad(){
			cout << "Los gerentes se encargan de mantener una empresa, a traves del liderazgo, las reuniones con directores, entre otros. " << endl;
		}
		void almacen_cargo(){
			cout << "Los gerentes tienen a cargo a los gerentes de proyecto y programadores, ademas de otros empleados menores" << endl;
		}
};

class GerenteProyectos : public Empleados{
	private:
		string titulo_universitario;
		int anios_exp;
	public:
		//Constructor
		
		GerenteProyectos(string nombre_empleado, string identificador_empleado, int anios_exp, string titulo_universitario) : Empleados(nombre_empleado,identificador_empleado){
			this->anios_exp = anios_exp;
			this->titulo_universitario = titulo_universitario;
		}
		
		//Getters
		
		string getTituloUniversitario(){
			return this->titulo_universitario;
		}
		
		int getAniosExp(){
			return this->anios_exp;
		}
		
		//Setters
		
		void setTituloUniversitario(string nuevoTituloUniversitario){
			this->titulo_universitario = nuevoTituloUniversitario;
		}
		
		void setAniosExp(int nuevaExp){
			this->anios_exp = nuevaExp;
		}
		
		//Ya tenemos clara la actividad de un gerente de proyectos programamos las funciones virtuales
		void actividad(){
			cout << "Los gerente de proyecto se encargan de la supervision de un proyecto en una empresa, los cuales generalmente los programadores tienen la tarea de realizar, el gerente apoya" << endl;
		}
		void almacen_cargo(){
			cout << "Los gerente de proyecto tienen en su almacen de cargos a los programadores especialmente" << endl;
		}
};

class Programadores : public Empleados{
	private:
		string lenguaje_programacionExperimentado;
		string titulo_universitario;
		bool es_jr;
	public:
		//Constructor 1 (No todos los programadores tenemos titulo)
		
		Programadores(string nombre_empleado, string identificador_empleado,string lenguaje_programacionExperimentado, bool es_jr) : Empleados(nombre_empleado,identificador_empleado){
			this->lenguaje_programacionExperimentado = lenguaje_programacionExperimentado;
			this->es_jr = es_jr;
		}
		
		//Constructor 2 (Con titulo universitario)
		Programadores(string nombre_empleado, string identificador_empleado,string lenguaje_programacionExperimentado, string titulo_universitario, bool es_jr) : Empleados(nombre_empleado,identificador_empleado){
			this->lenguaje_programacionExperimentado = lenguaje_programacionExperimentado;
			this->titulo_universitario = titulo_universitario;
		}
		
		void actividad(){
			cout << "Los programadores se encargan de la creacion, mantenimiento, de software computacional " << endl;
		}
		void almacen_cargo(){
			if(es_jr == false){
				cout << "Este programador tiene a en su almacen de cargo a todos los programadores juniors" << endl;
			}
			else{
				cout << "Este programador no tiene personas en su almacen de cargos " << endl;
			}
		}
		
			
};

int main(){
	//Probamos nuestras clases con dos objetos dinamicos del tipo perro y gato
	Perro* perro1 = new Perro("Rex",4);
	Gato* gato1 = new Gato("Manchitas",3);
	
	perro1->sonido();
	gato1->sonido();
	
	cout << endl;
	//Probamos la jerarquia de empleados
	
	Gerente* gerente1 = new Gerente("Jose","765423",10,"Ingeniero Industrial y Doctorado en Ciencias de la computacion");
	gerente1->actividad();
	gerente1->almacen_cargo();
	cout << endl;
	GerenteProyectos* gerentep1 = new GerenteProyectos("Ricardo","543456",5,"Ingeniero en informatica");
	gerentep1->actividad();
	gerentep1->almacen_cargo();
	cout << endl;
	cout << endl;
	Programadores* programador1 = new Programadores("Pedro","54123","JavaScript",false);
	programador1->actividad();
	programador1->almacen_cargo();
}
