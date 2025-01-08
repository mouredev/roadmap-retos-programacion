//@Roni
#include <iostream>
#include <string>
#include <stack>
#include <queue>
/*
 * EJERCICIO:
 * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
 * atributos y una función que los imprima (teniendo en cuenta las posibilidades
 * de tu lenguaje).
 * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
 * utilizando su función.
 */
class Iguana{
private:
	std::string genero;
	std::string endemico;
	std::string especie;
public:
	Iguana(){
		this ->genero="";
		this ->endemico="";
		this ->especie="";
	}

	const std::string& getEndemico() const {
		return endemico;
	}

	void setEndemico(const std::string &endemico) {
		this->endemico = endemico;
	}

	const std::string& getEspecie() const {
		return especie;
	}

	void setEspecie(const std::string &especie) {
		this->especie = especie;
	}

	const std::string& getGenero() const {
		return genero;
	}

	void setGenero(const std::string &genero) {
		this->genero = genero;
	}
	void print(){
		std::cout<<"Genero: "<<this->genero<<"\nEndemico: "<<this->endemico<<"\nEspecie: "<<this->especie<<std::endl;
	}
};
/*
* DIFICULTAD EXTRA (opcional):
* Implementa dos clases que representen las estructuras de Pila y Cola
* (estudiadas en el ejercicio número 7 de la ruta de estudio)
* - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
*   retornar el número de elementos e imprimir todo su contenido.
*/
class Pila{
	private:
		std::stack<int> datos;
	public:
	Pila() {
    }
    void anyadirDatos(int dato) {
    	this->datos.push(dato);
    }
    void elminarDatos() {
    	if (!datos.empty()) {
    		this->datos.pop();
        }else {
        	std::cout<<"La pila esta vacía"<<std::endl;
        }
    }
    int numeroDeElementos() {
    	return datos.size();
    }
    void print() {
    	std::stack<int> temp=datos;
    	int i=0;
    	while(!temp.empty()){
    		i++;
    		std::cout<<"Dato "<<i<<"= "<<temp.top()<<std::endl;
    		temp.pop();
    	}
    }
};
class Cola{
	private:
	std::queue<std::string> datos;
	public:
	Cola() {
	}
	void anyadirDatos(std::string dato) {
		this->datos.push(dato); // --> También podríamos utilizar datos.add(dato);
	}
	void elminarDatos() {
		if (!datos.empty()) {
			this->datos.pop();
		}else {
			std::cout<<"La pila esta vacía"<<std::endl;
        }
	}
	int numeroDeElementos() {
		return datos.size();
	}
	void print() {
		std::queue<std::string> temp=datos;
		int i=0;
		while(!temp.empty()){
			i++;
			std::cout<<"Dato "<<i<<"= "<<temp.front()<<std::endl;
			temp.pop();
		}
	}
};

int main(){
	Iguana ig1; // --> Instanciamos/Incicalizamos la clase
	std::cout<<"****IGUANA****"<<std::endl;
	 /*Le asignamos los valores*/
	ig1.setGenero("Macho");
	ig1.setEndemico("Sudamerica");
	ig1.setEspecie("Iguana");
	ig1.print(); // --> Llamamos al método que nos devolvera los valores
	std::cout<<"****PILA****"<<std::endl;
	Pila pila ; // --> Instanciamos/Incicalizamos la clase
	/*Le asignamos los valores*/
	pila.anyadirDatos(1);            pila.anyadirDatos(2);            pila.anyadirDatos(3);
	std::cout<<"El número de elementos es: "<<pila.numeroDeElementos()<<std::endl; // --> Imprimimos números de elementos
	std::cout<<"Su contenido es:\n"; pila.print(); // --> Imprimimos todos los datos
	pila.elminarDatos(); // --> Eliminamos elemento de arriba de la pila
	std::cout<<"El número de elementos despúes de pila.elminarDatos(): "<<pila.numeroDeElementos()<<std::endl;
	std::cout<<"Su contenido despúes de pila.elminarDatos():\n"; pila.print();
	pila.elminarDatos();
	pila.elminarDatos();
	pila.elminarDatos(); // --> Salta el aviso
	std::cout<<"****COLA****"<<std::endl;
	Cola cola ; // --> Instanciamos/Incicalizamos la clase
	/*Le asignamos los valores*/
	cola.anyadirDatos("Elemento 0");         cola.anyadirDatos("Elemento 1");         cola.anyadirDatos("Elemento 2");
	std::cout<<"El número de elementos es: "<<cola.numeroDeElementos()<<std::endl; // --> Imprimimos números de elementos
	std::cout<<"Su contenido es:\n"; cola.print(); // --> Imprimimos todos los datos
	cola.elminarDatos(); // --> Eliminamos elemento de la cabeza de la cola
	std::cout<<"El número de elementos despúes de cola.elminarDatos(): "<<cola.numeroDeElementos()<<std::endl;
	std::cout<<"Su contenido despúes de cola.elminarDatos():\n"; cola.print();
	cola.elminarDatos();
	cola.elminarDatos();
	cola.elminarDatos(); // --> Salta el aviso
	return 0;
}
