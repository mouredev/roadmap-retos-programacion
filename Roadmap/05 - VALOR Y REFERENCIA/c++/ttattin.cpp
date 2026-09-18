// EJERCICIO 05 - VALOR Y REFERENCIA
// Autor: TTATTIN

#include <iostream>
#include <string>
#include <utility>



//FUNCIONES PRIMERA PARTE DEL EJERCICIO
void paso_por_valor(std::string cadena) {
    cadena = "Esto es la variable pasada por valor despues de ser modificada en la funcion paso_por_valor";
    std::cout << cadena << std::endl;
}

void paso_por_referencia_constante(const std::string& cadena) {
    std::cout << "Si una variable se pasa por referencia con el modificador const, el valor de la variable no se puede modificar dentro de la funcion." << std::endl;
    std::cout << "Esto es muy util para no tener que copiar el valor de la variable en otra." << std::endl;
    std::cout << "A la vez se impide modificar el valor de la variable por error o descuido dentro de la funcion." << std::endl;
    std::cout << "La variable pasada por referencia constante es:" << std::endl;
    std::cout << cadena << std::endl << std::endl;
}

void paso_por_referencia(std::string& cadena) {
    std::cout << "Si una variable se pasa por referencia, el valor de la variable se puede modificar." << std::endl;
    std::cout << "Esto es muy util para no tener que copiar el valor de la variable en otra." << std::endl;
    std::cout << "Si se necesita una funcion que modifique varias variables, se pueden pasar por referencia." << std::endl;
    cadena = "Esto es la modificacion de la variable pasada por referencia";
    std::cout << "Variable despues de ser modificada en la funcion paso_por_referencia:" << std::endl;
    std::cout << cadena << std::endl << std::endl;
}

void primera_parte() {
    int variable = 10;
    int copia = variable;
    int& referencia = variable;

    std::cout << "Las pruebas de asignacion de variables por valor y referencia se haran con un entero." << std::endl;
    std::cout << "La variable original inicialmente tiene el valor: " << variable << std::endl;
    std::cout << "Copia de la variable tiene el valor: " << copia << std::endl;
    std::cout << "Referencia de la variable tiene el valor: " << referencia << std::endl << std::endl;

    variable = 20;

    std::cout << "Variable original despues de ser modificada por asignacion de valor: " << variable << std::endl;
    std::cout << "Valor de la copia: " << copia << std::endl;
    std::cout << "Valor de la referencia: " << referencia << std::endl << std::endl;

    referencia = 30;

    std::cout << "Variable original despues de modificar la referencia por asignacion: " << variable << std::endl;
    std::cout << "Valor de la copia: " << copia << std::endl;
    std::cout << "Valor de la referencia: " << referencia << std::endl << std::endl;
}

void segunda_parte() {
    std::string cadena = "Esto es una variable string";

    std::cout << "Las pruebas de paso por valor y referencia se haran con una variable string." << std::endl;
    std::cout << "La variable inicialmente tiene el valor: " << cadena << std::endl << std::endl;

    paso_por_valor(cadena);
    std::cout << "Variable despues de salir de la funcion paso_por_valor: " << cadena << std::endl << std::endl;

    paso_por_referencia_constante(cadena);

    paso_por_referencia(cadena);
    std::cout << "Variable despues de salir de la funcion paso_por_referencia:" << std::endl;
    std::cout << cadena << std::endl << std::endl;
}


//FUNCIONES DIFICULTAD EXTRA
std::pair<int, int> intercambio_por_valor(int a, int b) {
    std::cout << "Intercambio de valores por valor:" << std::endl;
    
    int temp = a;
    a = b;
    b = temp;

    return {a, b};
}

std::pair<int, int> intercambio_por_referencia(int& a, int& b) {
    std::cout << "Intercambio de valores por referencia:" << std::endl;
    
    int temp = a;
    a = b;
    b = temp;

    return {a, b};
}




int main() {
    // Primera parte del ejercicio: asignacion de variables por valor y referencia
    primera_parte();

    // Segunda parte del ejercicio: paso de variablespor valor y referencia
    segunda_parte();

    // DIFICULTAD EXTRA
    std::cout << "--------------------------------------" << std::endl;
    std::cout << "---------- DIFICULTAD EXTRA ----------" << std::endl;
    std::cout << "--------------------------------------" << std::endl;
    std::cout << std::endl;

    int a1 = 5;
    int b1 = 8;

    std::cout << "Valor de a antes del intercambio: " << a1 << std::endl;
    std::cout << "Valor de b antes del intercambio: " << b1 << std::endl << std::endl;

    auto [a2, b2] = intercambio_por_valor(a1, b1);
    
    std::cout << "Valor de a devuelto por la funcion despues del intercambio: " << a2 << std::endl;
    std::cout << "Valor de b devuelto por la funcion despues del intercambio: " << b2 << std::endl;
    std::cout << "Valor de a fuera de la funcion despues del intercambio: " << a1 << std::endl;
    std::cout << "Valor de b fuera de la funcion despues del intercambio: " << b1 << std::endl << std::endl;


    auto [a3, b3] = intercambio_por_referencia(a1, b1);

    std::cout << "Valor de a devuelto por la funcion despues del intercambio: " << a3 << std::endl;
    std::cout << "Valor de b devuelto por la funcion despues del intercambio: " << b3 << std::endl;
    std::cout << "Valor de a fuera de la funcion despues del intercambio: " << a1 << std::endl;
    std::cout << "Valor de b fuera de la funcion despues del intercambio: " << b1 << std::endl << std::endl;

    return 0;
}

