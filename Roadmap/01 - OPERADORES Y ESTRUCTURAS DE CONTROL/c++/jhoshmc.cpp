#include <iostream>
using namespace std;
int main(){
  int a = 6;
  int b = 5;

  //! aritmeticos :
  int suma = a + b;
  int resta = a - b;
  int multiplicacion = a *b;
  float divicion = a / b;
  float modulo = a % b;
  cout << "\t aritmeticos "<<endl;
  cout<<a << " + " <<b<<" = "<< suma << endl;
  cout<<a << " - " <<b<<" = "<< resta << endl;
  cout<<a << " * " <<b<<" = "<< multiplicacion << endl;
  cout<<a << " / " <<b<<" = "<< divicion << endl;
  cout<<a << " % " <<b<<" = "<< modulo << endl;

  //! lógico:
  bool x = true;
  bool y = false;
  bool and_logico = x && y;
  bool or_logico = x || y;
  bool negacion = !x;
  cout << "\t logicos " << endl;
  cout << "verdadero: " << x << endl;
  cout << "falso: " << y << endl;
  cout<<x << " && " <<y<<" = "<< and_logico << endl;
  cout<<x << " || " <<y<<" = "<< or_logico << endl;
  cout << "!" <<x<<" = "<< negacion << endl;

  //! comparacion
  bool igualdad = a == b;
  bool mayor = a > b;
  bool menor = a < b;
  bool mayor_igual = a >= b;
  bool menor_igual = a <= b;
  bool diferentes = a != b;
  cout << "\t comparacion " << endl;
  cout << a << " == " << b << " = " << igualdad << endl;
  cout << a << " > " << b << " = " << mayor << endl;
  cout << a << " < " << b << " = " << menor << endl;
  cout << a << " >= " << b << " = " << mayor_igual << endl;
  cout << a << " <= " << b << " = " << menor_igual << endl;
  cout << a << " != " << b << " = " << diferentes << endl;

  //! asignacion:
  int n = 0;
  cout << "numero original: " << n << endl;
  cout << "asignar a esa variable el numero 5: " << endl;
  cout << "n: " << n << endl;
  n = 5;
 cout<< "ahora n = 5: " << n  << endl;

 //! operadores bits

 cout << "\t operadores a nivel de bits: " << endl;
 cout<<"AND: " << a << " & "<<b<<" = " << (a & b) << endl;
 cout<<"OR: " << a << " | "<<b<<" = " << (a | b) << endl;
 cout<<"XOR: " << a << " ^ "<<b<<" = " << (a ^ b) << endl;

 //! operaciones con operadores
 //? condicional if(si) else(si no)
 cout << "\t if else clasico: " << endl;
 if (modulo >= 1)
 {
   cout << "es verdad que el resto es mayor a 1"<<endl;
  }else{
    cout << "es mentira que el resto es menor a 1" << endl;
  }
  //? ternario
  cout << "\t if else ternrio: " << endl;
  bool c;
  c = (a == b) ? x : y;
  cout << " respuesa al ternario : a==b: " << c<<endl;

  //? iteraciones (ciclos , repeticiones)
  //* ciclo for
  cout << "\t ciclo for: " << endl;
  for (int i = 0; i < b; i++)
  {
    cout <<i<< ", ";
  }
  cout << endl;
  cout << "\t ciclo while: " << endl;
  //* ciclo while
  while (n>= 1)
  {
    cout << "n: " << n << endl;
    n--;
  }
  cout << endl;
  cout << "\t ciclo doWhile " << endl;
  //* ciclo doWhile
  do
  {
    cout << "n: "<< n << endl;
    n++;
  } while (n< a);

  cout << endl;
  //! manejo de ecepciones

  try
  {
    /* no se que poner , pero es manejo de errores */
  }
  catch(const std::exception& e)
  {
    std::cerr << e.what() << '\n';
  }

  int base = 10;
  int final = 55;

  for (base; base <= final; base++)
  {
    if ((base% 2 == 0)&& (base != 16) && (base%3!= 0) || (base == final))
    {
      cout << "numero: " << base << endl;
    }
    
  }
  

  return 0;
}