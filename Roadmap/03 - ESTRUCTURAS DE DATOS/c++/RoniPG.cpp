// @RoniPG

#include <iostream>
#include <array>
#include<stack>
#include<queue>
#include<map>

using namespace std;

int main() {

	//Arrays

	//Arrays estaticos

	int numeros[] = { 1, 2, 3, 4, 5 }; // Instanciamos con variables asignadas
	int numeros2[5]; // Instaciamos con cantidad de variables

	// Acceder y modificar datos del array

	numeros2[0] = 1;

	cout << (numeros2[0] = 1) << endl; // Asignamos el valor 1 en la posicion 0
	cout << (numeros2[1] = 2) << endl; // Asignamos el valor 2 en la posicion 1
	cout << "Valor de la primera posicion en el array numeros: " << numeros[0]
			<< endl; // Asignamos el valor 1 en la posicion 0
	cout << "Valor de la primera posicion en el array numeros: ";
	cout << (numeros[0] = 6) << endl; // Asignamos el valor 6 en la posicion 0
	for (int i : numeros) { // ---> Foreach
		cout << i << ",";
	}
	cout << "" << endl;
	for (int i = 0; i < 5; ++i) { // No hay una funcion que devuelva el tama├▒o del arrray
		cout << numeros[i] << ",";
	}
	cout << "" << endl;

	//Ordenar

	/* No existe un metodo que ordene automaticamente el array como en java.
	 * Pero podemos implementar funciones que realizen esta funcion.
	 * Disponemos de varias funciones com podrian ser: Burbuja, Quicksort, entre otros.
	 */

	numeros[0] = 3;
	numeros[1] = 1;
	numeros[2] = 5;
	numeros[3] = 2;
	numeros[4] = 4;

	for (int i : numeros) {
		cout << i << ",";
	}
	cout << "" << endl;

	//Funcion burbuja

	for (int i = 0; i < 5; ++i) { // --> Hay que indicar el tama├▒o del array
		for (int j = i + 1; j < 5; ++j) {
			if (numeros[i] > numeros[j]) { // --> Con el signo elegimos el orden, si de mayor a menor (<) o de menor a mayour (>).
				int aux = numeros[i];
				numeros[i] = numeros[j];
				numeros[j] = aux;
			}
		}
	}
	for (int i : numeros) {
		cout << i << ",";
	}
	cout << endl;

	//Estructura (struct)

	/* En una estructura podemos guardar varios tipos de datos.
	 * Cada variable que creemos tendra los mismos tipos de datos que la estrucutura
	 */

	struct Persona {
		string nombre;
		int edad;
	};

	//Insercion datos

	Persona persona1 = { "Pedro", 47 };
	Persona persona2 = { "Alberto", 34 };

	cout << persona1.nombre << "\t" << persona1.edad << endl;
	cout << persona2.nombre << "\t" << persona2.edad << endl;

	//Borrar

	/* Para borrar podemos dejar sus datos vacios
	 * La variable creada no se podra borrar
	 *
	 * Ejemplo
	 *
	 */persona2 = { }; // --> Valor acutal 0
	cout << persona2.nombre << endl;
	cout << persona2.edad << endl;

	//Actualizacion

	/*Para actualizar podemos indicar la variable y cambiarle los datos
	 * La variable sera sustituida por los nuevos datos o creada si no existe
	 *
	 * Ejemplo
	 *
	 */persona2 = { "Alberto", 34 };
	cout << persona2.nombre << endl;
	cout << persona2.edad << endl;

	/* Ordenacion
	 * Al ser una esctrucura que se declara en variables la manera de ordenarlo seria
	 * declarar las variables dentro de un array y luego aplicarle algun metodo de ordenacion
	 */

	//Pilas(stack)
	/*
	 * Los datos se almancenan en pila con ordenacion LIFO (LAST IN, FIRST OUT)
	 * El ultimo dato introducido sera el primero en salir
	 */
	stack<int> pila; // ---> #include<stack>

	//Insertar Datos

	pila.push(7);
	pila.push(8);
	pila.push(9);

	cout << "El tama├▒o de la pila es de: " << pila.size() << " elementos"
			<< endl;

	//Extraer Datos

	cout << "El valor actual de la cima de la pila es: " << pila.top() << endl;
	pila.pop(); // ---> Elimina el dato de arriba
	cout << "El valor actual de la cima de la pila es: " << pila.top() << endl;

	//Colas(Queue)
	/*
	 * Los datos se almacenan en fila con ordenacion FIFO (FIRST IN, FIRST OUT)
	 * El ultimo dato introducido sera el ultimo en salir
	 */
	queue<int> cola; // ---> #include<queue>

	//Insertar Datos

	cola.push(7);
	cola.push(8);
	cola.push(9);

	cout << "El tama├▒o de la cola es de: " << cola.size() << " elementos"
			<< endl;

	//Extraer Datos

	cout << "El valor actual del primero de la cola es: " << cola.front()
			<< endl;
	cola.pop(); // ---> Elimina el dato del primero de la cola
	cout << "El valor actual del primero de la cola es: " << cola.front()
			<< endl;

	//Map
	/*
	 * Podemos ordenar los datos con clave-valor, en donde la clave nos permitira acceder/locacalizar el valor
	 */
	map<int, int> mapa; // ---> #include<map>

	//Insertar Datos

	mapa[1] = 15;
	mapa[2] = 25;
	mapa[3] = 35;
	mapa[4] = 45;
	mapa[5] = 55;

	for (auto &x : mapa) {
		cout << "Key: " << x.first << " Value: " << x.second << endl;
	}

	//Borrar Datos

	//mapa.clear(); ---> Eliminar(limpiar) todos los datos de la lista
	mapa.erase(3);
	cout << "Se ha borrado la tercera llave" << endl;
	for (auto &x : mapa) {
		cout << "Key: " << x.first << " Value: " << x.second << endl;
	}

	//Para actualizar los datos podemos indicar la llave y asignarle el nuevo valor,
	//Para actualizar la llave, tenemos que eliminar la que desemos cambiar y crear una nueva
	//Las estructuras map no se pueden ordenar por naturaleza.

	/* DIFICULTAD EXTRA (opcional):
	 * Crea una agenda de contactos por terminal.
	 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
   * - Cada contacto debe tener un nombre y un número de teléfono.
   * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
   *   los datos necesarios para llevarla a cabo.
   * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
   *   (o el número de dígitos que quieras)
   * - También se debe proponer una operación de finalización del programa.
   */
	map<string, string> agenda;
	int opcion;
	int contador = 0;
	do {
		cout << "\n*************Agenda de Contactos*************" << endl;
		cout << endl;
		cout << "Decida la opcion que quiera realizar: " << endl;
		cout << endl;
		cout << "Opcion 1: Buscar contacto" << endl;
		cout << "Opcion 2: Nuevo contacto" << endl;
		cout << "Opcion 3: Actualizar contacto" << endl;
		cout << "Opcion 4: Eliminar contacto" << endl;
		cout << "Opcion 5: Salir" << endl;
		cout << endl;
		cout << "Intruzca el numero de la opcion que desee: " << endl;
		cin >> opcion;
		cin.ignore();
		if (opcion == 1) {
			cout << "Nombre\t\t\tTelefono" << endl;
			cout << endl;
			for (auto &x : agenda) {
				cout << x.first << "\t\t\t" << x.second << endl;
			}
		} else if (opcion == 2) {
			cout << "Introduzca el nombre del contacto: " << endl;
			string nombre;
			getline(cin, nombre);
			cout << "\nIntroduzca el numero del contacto (max 11 digitos): "
					<< endl;
			string numero;
			getline(cin, numero);
			if (numero.length() > 11) {
				cout << "Ha excedido el limite de digitos, intente de nuevo: "
						<< endl;
			} else {
				for (int i = 0; i < numero.length(); ++i) {
					if ((numero.at(i) != '0') && (numero.at(i) != '1')
							&& (numero.at(i) != '2') && (numero.at(i) != '3')
							&& (numero.at(i) != '4') && (numero.at(i) != '5')
							&& (numero.at(i) != '6') && (numero.at(i) != '7')
							&& (numero.at(i) != '8') && (numero.at(i) != '9')) {
						cout << "Ha introducido un dato no numerico, " << endl;
						break;
					}
					agenda[nombre] = numero;
				}
			}
		} else if (opcion == 3) {
			cout << "Nombre\t\t\tTelefono" << endl;
			cout << endl;
			for (auto &x : agenda) {
				cout << x.first << "\t\t\t" << x.second << endl;
			}
			cout << "Decida la opcion que quiera realizar: \n" << endl;
			cout << "Opcion 1: Actulizar nombre" << endl;
			cout << "Opcion 2: Actulizar numero" << endl;
			int subOpcion;
			cin >> subOpcion;
			cin.ignore();
			if (subOpcion == 1) {
				cout << "Introduzca el numero del contacto: " << endl;
				string numero;
				getline(cin,numero);
				if (numero.length() > 11) {
					cout
							<< "Ha excedido el limite de digitos, intentelo de nuevo: "
							<< endl;
				} else {
					for (int i = 0; i < numero.length(); ++i) {
						if ((numero.at(i) != '0') && (numero.at(i) != '1')
								&& (numero.at(i) != '2')
								&& (numero.at(i) != '3')
								&& (numero.at(i) != '4')
								&& (numero.at(i) != '5')
								&& (numero.at(i) != '6')
								&& (numero.at(i) != '7')
								&& (numero.at(i) != '8')
								&& (numero.at(i) != '9')) {
							cout << "Ha introducido un dato no numerico, intentelo de nuevo: "
									<< endl;
							break;
						}
					}
				}
				for (auto &x : agenda) {
					if (x.second.compare(numero)==0) {
						cout << "El numero coincide con el nombre: "<< x.first << endl;
						cout << "Introduzca el nuevo nombre: " <<endl;
						string nombre;
						getline(cin, nombre);
						agenda.erase(x.first);
						agenda[nombre]=numero;
						contador=0;
						break;
					}
					contador++;
				}
				if (agenda.size() == contador) {
					cout << "El numero no ha encontrado coincidencias, intentelo de nuevo" << endl;
					contador=0;
				}
			}else if(subOpcion == 2){
				cout << "Introduzca el nombre del contacto: " << endl;
				string nombre;
				getline(cin,nombre);
				for (auto &x : agenda) {
					if (x.first.compare(nombre)==0) {
						cout << "El nombre coincide con el numero: "<< x.second << endl;
						cout << "Introduzca el nuevo numero: " <<endl;
						string numero;
						getline(cin, numero);
						if (numero.length() > 11) {
							cout
									<< "Ha excedido el limite de digitos, intente de nuevo: "
									<< endl;
							break;
						}else{
							for (int i = 0; i < numero.length(); ++i) {
								if ((numero.at(i) != '0') && (numero.at(i) != '1')
										&& (numero.at(i) != '2')
										&& (numero.at(i) != '3')
										&& (numero.at(i) != '4')
										&& (numero.at(i) != '5')
										&& (numero.at(i) != '6')
										&& (numero.at(i) != '7')
										&& (numero.at(i) != '8')
										&& (numero.at(i) != '9')) {
									cout << "Ha introducido un dato no numerico, intentelo de nuevo: "
											<< endl;
									break;
								}
								agenda.erase(x.first);
								agenda[nombre]=numero;
								break;
							}
						}
					}
				}
				cout << "El numero no ha encontrado coincidencias, intentelo de nuevo" << endl;
			}

		}else if (opcion == 4) {
			cout << "Nombre\t\t\tTelefono" << endl;
			cout << endl;
			for (auto &x : agenda) {
				cout << x.first << "\t\t\t" << x.second << endl;
			}
			cout << "Introduce el nombre del contacto que quieras eliminar" << endl;
			string nombre;
			getline(cin,nombre);
			for(auto &x: agenda){
				if (x.first.compare(nombre) == 0) {
					agenda.erase(nombre);
					cout << "Contacto eliminado" << endl;
					contador =0;
					break;
				}
				contador++;
			}
			if (agenda.size()==contador){
			cout << "El nombre no coincide con ningun contacto" << endl;
			contador=0;
			}
		} else {

		}

	} while (opcion != 5);

	return 0;
}
