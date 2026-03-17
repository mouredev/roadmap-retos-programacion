#include <iostream>
#include <string>
#include <cmath>

using namespace std;

// Operadores !!!
int main () {
   // Operadores Aritmeticos
   cout << "Suma 16 + 7 = 23 \n";

   int a,b;
   cout << "Valor de a: ";
   cin >> a;
   cout << "Valor de b: ";
   cin >> b;

   int suma = a + b;
   cout << "La suma de a y b es: " << suma << endl;
   cout << "Suma: " << 23 + 6;
   cout << "\nResta: " << 23 - 6;
   cout << "\nProducto: " << 23*6;
   cout << "\nDivision: " << 23/6;
   double division = 23.0/6.0;
   cout << "\nDivision corregido: " << division;
   long potencia = pow(23,3);
   cout << "\nPotencia de 23^3: " << potencia << endl;
   cout << "--------------------------------------------------------------" << endl; 

   // Operadores de comparacion
   cout << boolalpha; 
   cout << "Igualdad: 15 == 5 es " << (15 == 5) << endl;
   cout << "Desigualdad: 16 != 4*4 es " << (16 != 4*4) << endl;
   cout << "Desigualdad: 153 != 234 es " << (153 != 234) << endl;
   cout << "Mayor: 15 > 6 es " << (15 > 6) << endl;
   cout << "Mayor o igual: 15 >= 15 es " << (15 >= 15) << endl;
   cout << "Menor o igual: 15 <= 17 es " << (15 >= 17) << endl;
   cout << "--------------------------------------------------------------" << endl;

   // Operadores logicos
   // Ejemplos de edad 
   cout << "Que edad tienes?"<< endl;
   int edad;
   cin >> edad;
   if (edad >= 18 && edad < 50) {
      cout << "Tiene permiso de entrar al club." ;
   } else {
      cout << "No tiene permiso de entrar :(" << endl;
   } 
   // Ejemplos simple
   cout << "Es verdadero decir que 16!=5? Rpta: " << !(16!=5) << endl;
   cout << "Es verdadero decir que  30>14 o 32<33? Rpta: " << (30>14 or 32<33) << endl;
   cout << "Es Falso decir que 13 > 8 y 15 < 16? Rpta: " << !(13 > 8 and 15 < 16) << endl;
   // Operadores de identidad
   // cout << boolalpha; 

   int my_number = 10;
   int &my_new_number = my_number; // creamos una referencia (mismo objeto)
   int other_number = 10; /// Mismo valor pero otro objeto

   // is es como comparar las dirreciones de memoria (&)
   cout << "my_number is my_new_number es " << (&my_number == &my_new_number) << endl;
   // is not es como comparar que las dirreciones sean distintas
   cout << "my_number is not other_number es " << (&my_number != &other_number) << endl;

   // Operadores de pertenencia
   cout << boolalpha;
   string palabra = "massito";
   char letra = 'l';

   if (palabra.find(letra) != string::npos){
      cout << "La letra " << letra << " SI pertenece a la palabra: " << palabra << endl;
   } else {
      cout << "La letra " << letra << " NO pertenece a la palabra: " << palabra << endl;
   }
   // Operadores de bit
   
   int x = 11; // 1011
   int y = 2; // 0010

   cout << "AND (11 & 2): " << (x & y) << endl; // 0010 = 2
   cout << "OR (11 | 2): " << (x | y) << endl; //  1011 = 11
   cout << "XOR (11 ^ 2): " << (x ^ y) << endl; // 1001 = 9
   cout << "NOT (11): " << (~x) << endl; 
   cout << "Desplazamiento a la derecha: 11 >> 2 es " << (x >> 2) << endl; // 0010 = 2 

   // ___Estructura de control___

   // Condicionales

   string my_name = "Massito" ; // Definimos variable
   if (my_name == "massi") {
      cout << "my_name es 'massi'" << endl;
   }else if (my_name == "Massito") {
      cout << "my_name es 'Massito'" << endl;
   } else {
      cout << "No es ni 'massi' ni 'Massito'" << endl;
   }

   // Iterativas
   
   for(int i=0 ; i<15; i++) {
      cout << i << endl;
   }

   int i = 0;
   while(i <= 9) {
      cout << i << endl;
      i++;

   } 

   // Manejo de excepciones
   int numerador = 10;
   int denominador = 0;
   
   try {
      if (denominador == 0){
         throw runtime_error("Error, no se puede dividir entre 0");

      }
      int resultado = numerador / denominador;
      cout << "Resultado: " << resultado << endl;
   }
   catch (const runtime_error& e) {
      cout << "Se produjo una excepcion: " << e.what() << endl; //capturamos el error y mostramos el mensaje
   } catch(...) {
      cout << "Ocurrio un error desconocido." << endl; // bloque opcional para cualquier tipo de error
   }

   // Ejercicio adicional!!!

   cout << "El programa sigue ejecutandose..." << endl; 

   for(int i = 10; i <=55; i++){
      if (i % 2 != 0) {
         continue; 
      }
      if (i == 16) {
         continue;
      }
      if (i % 3 == 0) {
         continue;
      }
      cout << i << endl;

   }

   return 0;
}
