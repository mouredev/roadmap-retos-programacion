#include<iostream>
#include<fstream>
#include<cstdio>
using namespace std;

void escritura(){
	ofstream archivo;
	string texto;
	archivo.open("dylanb55.txt",ios::out);
	
	cout << "Ingrese su nombre: " << endl;
	getline(cin,texto);
	
	archivo << "Nombre: " << texto << endl;
	
	cout << "Ingrese su edad: " << endl;
	getline(cin,texto);
	
	archivo << "Edad: " << texto << endl;
	
	cout << "Ingrese su lenguaje de programacion favorito " << endl;
	getline(cin,texto);
	
	archivo << "Lenguaje de programacion favorito: " << texto << endl;
	
	archivo.close();
}

void lectura(){
	ifstream archivo;
	string texto;
	
	archivo.open("dylanb55.txt",ios::in);
	
	cout << "\nMostrando Informacion\n" << endl;
	
	while(archivo.eof() != true){
		getline(archivo,texto);
		cout << texto << endl;
	}
	archivo.close();
	
	int eliminar = remove("dylanb55.txt");
	
	if(eliminar != 0){
		cout << "No se ha eliminado correctamente el fichero" << endl;
	}
	else{
		cout << "Fichero eliminado correctamente " << endl;
	}
	
}

int main(){
	escritura();
	lectura();
}
