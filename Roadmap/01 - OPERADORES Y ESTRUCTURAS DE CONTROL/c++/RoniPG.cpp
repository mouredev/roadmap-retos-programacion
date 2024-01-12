// @RoniPG

#include <iostream>
//#include <sstream>

using namespace std;

int main() {

	cout << "Tipo de operadores." << endl;

	cout << "Operadores Aritmeticos." << endl;

	cout
			<< "Suma +, Resta -, Division /, Multiplicacion *, Resto % (En la division inexacta = lo que sobra)"
			<< endl;

	cout << "Ejemplos" << endl;

	int a = 2;
	int b = 3;

	int suma = a + b;
	cout << a << " - " << b << " = " << suma << endl;

	int resta = a - b;
	cout << a << " - " << b << " = " << resta << endl;

	int division = a / b;
	cout << a << " / " << b << " = " << division << endl;

	int multiplicacion = a * b;
	cout << a << " * " << b << " = " << multiplicacion << endl;

	int resto = a % b;
	cout << a << " % " << b << " = " << resto << endl;

	cout << "Operadores de Asignacion." << endl;

	cout << " = para asignar el valor sobrescirbiendolo" << endl;
	cout << "+= sumar a la variable el valor dedicidido" << endl;
	cout << "-= restar a la variable el valor dedicidido" << endl;
	cout << "*= mutilpicar a la variable el valor dedicidido" << endl;
	cout << "/= dividir a la variable el valor dedicidido" << endl;

	cout << "Ejemplos" << endl;

	cout << a << endl;
	cout << a << " += 2 " << endl;
	a += 2;
	cout << a << endl;
	cout << a << " -= 2 " << endl;
	a -= 2;
	cout << a << endl;
	cout << a << " *= 2 " << endl;
	a *= 2;
	cout << a << endl;
	cout << a << " /= 2 " << endl;
	a /= 2;
	cout << a << endl;

	cout << "Operadores de comparacion" << endl;

	cout << "== igual a (para objetos equals(), != difente de, < menor que,"
			<< endl;

	cout << "<= menor o igual que, >= mayor o igual que, > mayor que." << endl;

	cout << "Todos estos valores devuelven un booleano true o false" << endl;

	cout << "Ejemplos" << endl;

	bool comparacion;

	cout << std::boolalpha;
	cout << a << " | " << b << endl;
	comparacion = a == b;
	cout << a << " es igual a " << b << ": " << comparacion << endl;
	comparacion = a != b;
	cout << a << " no es igual a " << b << ": " << comparacion << endl;
	comparacion = a < b;
	cout << a << " es menor que " << b << ": " << comparacion << endl;
	comparacion = a <= b;
	cout << a << " es menor o igual que " << b << ": " << comparacion << endl;
	comparacion = a >= b;
	cout << a << " es mayor o igual que " << b << ": " << comparacion << endl;
	comparacion = a > b;
	cout << a << " es mayor que " << b << ": " << comparacion << endl;

	cout << "Operadores logicos." << endl;

	cout << "|| operador OR (devuelve true si una de las variables se cumple)"
			<< endl;
	cout << "&& operador AND (devuelve true si todas las variables se cumplen)"
			<< endl;
	cout
			<< "! operador NOT (invierte el valor de la condicion, de true a false y viceversa)"
			<< endl;

	cout << "Ejemplos" << endl;

	bool logico = true;
	comparacion = false;

	cout << "Operador OR: " << comparacion << " || " << logico << endl;
	if (comparacion || logico) {
		cout << logico << endl;
	} else {
		cout << comparacion << endl;
	}
	cout << "Operador AND: " << comparacion << " && " << logico << endl;
	if (comparacion && logico) {
		cout << logico << endl;
	} else {
		cout << comparacion << endl;
	}
	cout << "Operador NOT: !" << comparacion << endl;
	if (!comparacion) {
		cout << logico << endl;
	} else {
		cout << comparacion << endl;
	}

	cout <<"Operadores de incremento y decremento." << endl;

	cout <<"++ Incrementa en uno la variable." << endl;
	cout <<"-- Incrementa en uno la variable." << endl;

	cout <<"Ejemplos" << endl;

	a = 2;
	cout <<a << endl;
	cout <<" ++ " << a << endl;
	a++;
	cout <<a << endl;
	cout <<" -- " << a << endl;
	a--;
	cout <<a << endl;

	cout << "Operadores ternarios" << endl;

	cout << "Tienen la forma condicion ? valor_si_verdadero : valor_si_falso."
			<< endl;

	cout << "Ejemplos" << endl;

	bool ternario = false;

	ternario = (comparacion || logico) ? logico : comparacion;
	cout << "Operador OR en ternario: " << comparacion << " || " << logico
			<< " ternario = " << ternario << endl;
	ternario = (comparacion && logico) ? logico : comparacion;
	cout << "Operador AND en ternario: " << comparacion << " && " + logico
			<< " ternario = " << ternario << endl;
	ternario = (!comparacion) ? logico : comparacion;
	cout << "Operador NOT en ternario: !" << comparacion << " ternario = "
			<< ternario << endl;
	cout << "Operadores de concatenacion" << endl;

	cout << "+ Unir diferentes strings a uno solo." << endl;

	cout << "Ejemplos" << endl;

	string texto1 = "Hola, ";
	cout << texto1 << endl;
	string texto2 = "Java!";
	cout << texto2 << endl;
	string textoFinal = texto1 + texto2;
	cout << textoFinal << endl;

	cout << "Operadores de conversion de tipo" << endl;

	cout << "Para covertir a numero se puede utlizar: stoi (texto_a_convertir) mediante la libreria <string>, \n "
			" o tambien mediante la libreria <sstream> creando un objeto que realizara la conversion" << endl;

	cout << "Para covertir a texto se puede utlizar: to_string (texto_a_convertir) mediante la libreria <string>, \n "
			" o tambien mediante la libreria <sstream> creando un objeto que realizara la conversion" << endl;

	cout << "Para covertir a flotante se puede utlizar: stof (texto_a_convertir) mediante la libreria <string>, \n "
			" o tambien mediante la libreria <sstream> creando un objeto que realizara la conversion" << endl;

	cout << "Ejemplos" << endl;

	texto1 = "2";
	cout << "Dato en texto = " << texto1 << endl;
	/*stringstream convert;
	 convert << texto1;
	 convert >> a;*/
	a = stoi(texto1);
	cout << "Dato convertido a entero = " << a << endl;
	/*stringstream convert;
	 convert << a;
	 convert >> texto1;*/
	texto1 = to_string(a);
	cout << "Dato convertido a texto = " << texto1 << endl;
	float ft;
	/*stringstream convert;
	 convert << texto1;
	 convert >> ft;*/
	ft = stof(texto1);
	cout << "Dato convertido a flotante = " << ft << endl;

	cout << "Tipo de estucturas." << endl;

	cout << "Estructura if" << endl;

	cout << "Se ejecuta el bolque si se cumple la condicion." << endl;

	cout << "Ejemplos" << endl;

	a = 2;
	b = 2;

	cout << "Si " << a << " = " << b << endl;
	if (a == b) {
		cout << "Se ejecuta el bloque" << endl;
	}

	cout << "Estructura if-else" << endl;

	cout <<
			"Se ejecuta el bloque if si se cumple la condicion, si no se cumple se ejecuta el else." << endl;

	cout << "Ejemplos" << endl;

	cout << "Si " << a << " < (menor que) " << b << endl;
	if (a < b) {
		cout << "Se ejecuta el bloque if" << endl;
	} else {
		cout << "Se ejecuta el bloque else" << endl;
	}

	cout << "Estructura if else-if else" << endl;

	cout << "Se ejecuta el bloque if si se cumple la condicion." << endl;
	cout <<
			"Si no se cumple se ejecuta la siguiente condicion else if(asi sucesivamente)." << endl;
	cout << "Si no se cumple niguna condicion se ejecuta el else." << endl;

	cout << "Ejemplos" << endl;

	cout <<
			"if " << a << " < (menor que) " << b << "\n"
			"else if " << a << " = (igula a) " << b << endl;
	if (a < b) {
		cout << "Se ejecuta el bloque if" << endl;
	} else if (a == b) {
		cout << "Se ejecuta el bloque else if" << endl;
	} else {
		cout << "Se ejecuta el bloque else" << endl;
	}

	cout << "Estructura switch" << endl;

	cout <<
			"Se pasa una variable para luego indicar los casos en los que se ejecutaria." << endl;
	cout <<
			"Dentro de cada caso se añade 'break;'(opcional), para salir del switch despues de ejecutar el bloque de codigo." << endl;
	cout <<
			"Tambien se puede añadir 'default:' para ejecutar el codigo si no se cumple ningun case." << endl;

	cout << "Ejemplos" << endl;

	a = 1;
	b = 2;
	int c = 3;

	cout <<
			"Case 1 = " << a << ",caso 2 = " << b << ",caso 3 = " << c
					<< ",si no = " << endl;
	switch (a) {
	case 1:
		cout << "Se ejecuta el primer caso" << endl;
		break;
	case 2:
		cout << "Se ejecuta el segundo caso" << endl;
		break;
	case 3:
		cout << "Se ejecuta el tecero caso" << endl;
		break;
	default:
		cout << "No se ejecuta ningun caso" << endl;
		break;
	}

	cout << "Estructura de bucles" << endl;

	cout << "Bucle for" << endl;

	cout <<
			"Se ejecuta un bloque de codigo mientras la condicion sea verdadera." << endl;
	cout <<
			"Esto se controla mediante un iterador que se ira modificando por cada ejecucion del bucle." << endl;

	cout << "Ejemplos" << endl;

	for (int i = 0; i < c; i++) {
		cout << i << endl;
	}

	cout << "Bucle while" << endl;

	cout <<
			"Se ejecuta un bloque de codigo mientras la condicion sea verdadera." << endl;
	cout <<
			"El bucle se ejecutara hasta que se modifique la condicion." << endl;

	cout << "Ejemplos" << endl;

	cout << "Condicion: " << a << " distito de " << c << endl;

	while (a != c) {
		cout << "La condicion es verdera" << endl;
		a++;
		cout << a << endl;
	}
	cout << "Bucle do-while" << endl;

	cout <<
			"Primero se ejecuta un bloque de codigo, luego se comprueba que la condicion sea verdadera." << endl;
	cout <<
			"El bucle se ejecutara hasta que se modifique la condicion." << endl;

	cout << "Ejemplos" << endl;

	a = 0;

	do {
		cout << "Condicion: " << a << " distinto " << c << endl;
		cout << "La condicion es verdera" << endl;
		a++;
	} while (a != c);

	cout << "DIFICULTAD EXTRA (opcional):" << endl;
	cout <<
			"Crea un programa que imprima por consola todos los números comprendidos" << endl;
	cout <<
			"entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3." << endl;

	for (int i = 10; i <= 55; i++) {
		if (i % 2 != 0) {

		} else if ((i == 16) || (i % 3 == 0)) {

		} else {
			cout << i << endl;
		}
	}
	return 0;
}
