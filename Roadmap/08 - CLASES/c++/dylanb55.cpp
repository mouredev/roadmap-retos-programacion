#include<iostream>
#include<stack>
#include<queue>
using namespace std;

class Persona{
	private:
		string nombre;
		string pais_origen;
		string titulo_universitario;
		bool titulo;
		int edad;
	public:
		//Constructor 1 (para personas sin titulo universitario)
		
		Persona(string nombre, string pais_origen, int edad){
			this->nombre = nombre;
			this->pais_origen = pais_origen;
			this->edad = edad;
			titulo = false;
		}
		
		//Constructor 2 (para personas con titulo universitario)
		
		Persona(string nombre, string pais_origen, string titulo_universitario, int edad){
			this->nombre = nombre;
			this->pais_origen = pais_origen;
			this->titulo_universitario = titulo_universitario;
			this->edad = edad;
			titulo = true;
		}
		
		//Setters
		
		void setNuevoNombre(string nombre){
			this->nombre = nombre;
		}
		
		void setNuevoPais(string pais_origen){
			this->pais_origen = pais_origen;
		}
		
		void setNuevoTitulo(string titulo_universitario){
			this->titulo_universitario = titulo_universitario;
		}
		
		void setNuevaEdad(int edad){
			this->edad = edad;
		}
		
		string getNombre(){
			return this->nombre;
		}
		
		string getPais(){
			return this->pais_origen;
		}
		
		string getTitulo(){
			return this->titulo_universitario;
		}
		
		int getEdad(){
			return this->edad;
		}
		
		//Funciones
		
		void imprimirDatos(){
			cout << "Nombre: " << nombre << endl;
			cout << "Pais: " << pais_origen << endl;
			if(titulo == true){
				cout << "Titulo: " << titulo_universitario << endl;
			}
			else{
				cout << nombre << " no cuenta con titulo universitario " << endl;
			}
			cout << "Edad: " << edad << endl;
		}
};

class Pila{
	private:
		stack<int> mi_pila;
	public:
		//Constructor por defecto para pila
		Pila(){
			
		}
		void ingresarNumero(int numero){
			mi_pila.push(numero);
			cout << "Se ha ingresado correctamente el numero a pila" << endl;
		}
		
		
		void eliminarDato(){
			mi_pila.pop();
			cout << "\nSe ha eliminado correctamente un numero de la pila" << endl;
		}
		
		void mostrarLargo(){
			cout << "El largo de la pila es: " << mi_pila.size() << endl;
		}
		
		void mostrarElementos(){
			while(mi_pila.empty() != true){
				cout << "Numero:" << mi_pila.top() << endl;
				mi_pila.pop();
			}
		}
};

class Cola{
	private:
		queue<int> mi_cola;
	public:
		//Constructor por defecto para cola
		Cola(){
			
		}
		
		void ingresarNumero(int numero){
			mi_cola.push(numero);
			cout << "Numero ingresado correctamente a la cola" << endl;
		}	
		void eliminarDato(){
			mi_cola.pop();
			cout << "Se ha eliminado correctamente un numero de la cola" << endl;
		}
		
		void mostrarLargo(){
			cout << "El largo de la cola es: " << mi_cola.size() << endl; 
		}
		void mostrarElementos(){
			while(mi_cola.empty() != true){
				cout << "Numero: " << mi_cola.front() << endl;
				mi_cola.pop();
			}
		}
};
int main(){
	//Probamos la clase Persona
	
	Persona* p1 = new Persona("Mauricio","Argentina","Ingeniero en informatica",30);
	p1->imprimirDatos();
	cout << endl;
	Persona* p2 = new Persona("Jorge","Chile",19);
	p2->imprimirDatos();
	cout << endl;
	//Probamos la pila
	
	Pila* pila1 = new Pila();
	pila1->ingresarNumero(5);
	pila1->ingresarNumero(10);
	pila1->ingresarNumero(323);
	pila1->mostrarLargo();
	pila1->eliminarDato(); //Recordar que las pilas usan el metodo ultimo en entrar primero en salir, es decir se borraria el elemento 323
	pila1->mostrarElementos();
	cout << endl;
	
	//Probamos la cola
	
	cout << endl;
	
	Cola* cola1 = new Cola();
	
	cola1->ingresarNumero(50);
	cola1->ingresarNumero(300);
	cola1->ingresarNumero(23);
	cola1->ingresarNumero(3);
	cola1->ingresarNumero(-3);
	cola1->mostrarLargo();
	cola1->eliminarDato(); //Recordar que las colas usan el metodo el primero en entrar es el primero en salir, es decir se borra el elemento 50;
	cola1->mostrarElementos();
}
 
