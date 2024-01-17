//https://cplusplus.com
//https://isocpp.org

/*
  Esto es otro tipo de comentario,
  varias líneas
*/

#include <iostream>		
using namespace std;

const char lenguaje[4] = "C++";     //constante 

int main()
{
  int entero = -89;
  long enterolargo = 1022;
  short enterocorto = 256;
  unsigned short int enterocorto_sinsigno = 23470;           
  unsigned long int enterolargo_sinsigno = 	294967267;   
 
  float y = -1.5;			                         //variable tipo flotante
  double z = 0.000809;                               //variable tipo double
  
  bool bandera = true;		                         //variable tipo booleano
  bool bandera2 = false;
  
  char letra = 'H';                                  //variable tipo char
  unsigned char charsinsigno = 'A';
   

  cout << "Hola "<<lenguaje<<endl;		             //imprime por terminal
  
  return 0;
}
