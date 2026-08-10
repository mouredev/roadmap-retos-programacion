#include <iostream>
#include <string>
#include <algorithm>

// Variable global
int global = 0;

// Funcion void sin parametros
void funcion_void_sin_parametros() {
    std::cout << "Esto se escribe desde la funcion void sin parametros\n\n";
}

// Funcion void con parametros pasados por valor
void funcion_void_con_parametros_por_valor(int a, int b) {
    std::cout << "Cambio de valor de a y b dentro de la funcion con parametros por valor\n";
    a = 10;
    b = 20;
    std::cout << "a: " << a << std::endl;
    std::cout << "b: " << b << std::endl << std::endl;
}

// Funcion void con parametros pasados por referencia
void funcion_void_con_parametros_por_referencia(int &a, int &b) {
    std::cout << "Cambio de valor de a y b dentro de la funcion con parametros por referencia:\n";
    a = 10;
    b = 20;
    std::cout << "a: " << a << std::endl;
    std::cout << "b: " << b << std::endl << std::endl;
}

// Funcion que devuelve valor
int funcion_que_devuelve_valor() {
    return 200;
}

// Funcion de ejemplo para una lambda
void invertir_palabra (std::string s) {
    std::cout << "Texto antes de invertir: " << s << std::endl;
    std::cout << "Texto despues de invertir con una funcion lambda: ";
    std::for_each(s.rbegin(), s.rend(), [](char& c){ 
        std::cout << c;
    });
    std::cout << std::endl << std::endl;
}

// Funcion que usa variable global
void funcion_que_usa_variable_global() {
    global = 100;
}

// Funcion para el ejercicio de dificultad extra
int funcion_dificultad_extra(std::string s1, std::string s2) {
    int c = 0;
    for (int i = 1; i <= 100; i++) {
        if (i % 3 == 0 && i % 5 == 0) {
            std::cout << s1+s2 << std::endl;
        } else if (i % 3 == 0) {
            std::cout << s1 << std::endl;
        } else if (i % 5 == 0) {
            std::cout << s2 << std::endl;
        } else {
            std::cout << i << std::endl;
            c++;
        }
    }
    return c;
}

int main() {
    int a = 1;
    int b = 2;
    std::string s1 = "Hola";
    std::string s2 = "Mundo";

    funcion_void_sin_parametros();

    std::cout << "Valores de a y b antes de llamar a funcion con parametros por valor: " << std::endl;
    std::cout << "a: " << a << std::endl;
    std::cout << "b: " << b << std::endl << std::endl;
    funcion_void_con_parametros_por_valor(a, b);
    std::cout << "Valores de a y b despues de llamar a funcion con parametros por valor: " << std::endl;
    std::cout << "a: " << a << std::endl;
    std::cout << "b: " << b << std::endl << std::endl;

    funcion_void_con_parametros_por_referencia(a, b);
    std::cout << "Valores de a y b despues de llamar a funcion con parametros por referencia: " << std::endl;
    std::cout << "a: " << a << std::endl;
    std::cout << "b: " << b << std::endl << std::endl;

    a = funcion_que_devuelve_valor();
    std::cout << "Valor de a despues de llamar a funcion que devuelve valor: " << std::endl;
    std::cout << "a: " << a << std::endl << std::endl;

    std::cout << "En C++ no se pueden crear funciones dentro de funciones." << std::endl;
    std::cout << "Lo mas parecido a esto es una funcion lambda." << std::endl;
    std::cout << "Ejemplo de funcion lambda dentro de otra funcion" << std::endl;
    invertir_palabra ("Texto a invertir");
    
    std::cout << "Esto es un ejemplo de llamada a funcion size() proporcionada por la biblioteca string." << std::endl;
    std::cout << "s1: " << s1 << std::endl;
    std::cout << "La variable string s1 tiene " << s1.size() << " caracteres." << std::endl;
    std::cout << "s2: " << s2 << std::endl;
    std::cout << "La variable string s2 tiene " << s2.size() << " caracteres." << std::endl << std::endl;

    std::cout << "Valor de la variable global antes de llamar a funcion que cambia variable global: " << std::endl;
    std::cout << "global: " << global << std::endl << std::endl;
    funcion_que_usa_variable_global();
    std::cout << "Valor de la variable global despues de llamar a funcion que cambia variable global: " << std::endl;
    std::cout << "global: " << global << std::endl << std::endl;

    // DIFICULTAD EXTRA
    
    int c = funcion_dificultad_extra(s1, s2);
    std::cout << "Numero de veces que se ha impreso un numero: " << c <<std::endl;

    return 0;
}