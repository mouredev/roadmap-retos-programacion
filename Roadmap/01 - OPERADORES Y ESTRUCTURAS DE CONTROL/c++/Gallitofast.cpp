// #include <iomanip>
#include <iostream>
int main() {
  float a{10}, b{6};
  // float result;
  //  Operadores aritmeticos
  std::cout<< "\n\n================================================================="<< std::endl;
  std::cout << "Operadores aritmeticos" << std::endl;
  std::cout << "variable a vale: " << a << " Variable b vale : " << b << std::endl;
  std::cout << "Suma a +b: " << a + b << "\n";
  std::cout << "resta a-b: " << a - b << "\n";
  std::cout << "Multiplicacion de a*b: " << a * b << "\n";
  std::cout << "Division de a/b: " << a / b << "\n";
  std::cout << "Incremento de a" << a++ << std::endl;
  std::cout << "Decremento de a " << a-- << std::endl;
  // Operaciones de comparacion
  // estos resultados se imprimiran en booleanos, 0 es falso y 1 verdadero, o
  // usar la funcion de showbool
  std::cout<< "\n\n================================================================="<< std::endl;
  std::cout << "Comparadores" << std::endl;
  std::cout <<"Los resultados booleanos por defecto se imprimen como 0=false y 1=true (existe std::boolaplha para imprimirlos en alfanumerico)\n";
  std::cout << "igual a: (a==b)-->" << (a == b) << std::endl;
  std::cout << "desigual a: (a!=b)" << (a != b) << std::endl;
  std::cout << "Mayor que (a>b)" << (a > b) << std::endl;
  std::cout << "Menor que (a<b)" << (a < b) << std::endl;
  std::cout << "Mayor o igual que (a>=b)" << (a >= b) << std::endl;
  std::cout << "Menor o igual que (a<=b)" << (a <= b) << std::endl;

  std::cout << "\n\n================================================================="<< std::endl;
  std::cout << "Operadores logicos\n";
  std::cout << "Los operadores logicos se representan asi; \nOR=|| \nAND=&& NOT=!"<< std::endl;
  std::cout << "and sirve para juntar dos condiciones, como las siguientes:"<< std::endl;
  std::cout << "a>5 %% b<<3: (" << (a > 5 && b < 3)<< ") (Como las dos se cumplieron dan 1 que significa true)\n";
  std::cout << "Or da true si una de las condiciones da verdad como la siguiente:"<< std::endl;
  std::cout << "a>15 (Falso) || b>2 (Verdadero): (" << (a > 15 || b > 1) << ")"<< std::endl;
  std::cout << "Not invierte los valores, si es false da true y si es true da false\n";
  std::cout << "!a>5 (es true pero dara false por el not): (" << (!(a > 5))<< ")" << std::endl;
  std::cout << "b>100 (es falso asi que dara true): (" << (!(b > 100)) << ")"<< std::endl;

  std::cout << "\n\n================================================================="<< std::endl;
  std::cout << "Operadores de asignacion\n" << std::endl;
  int numero{11};
  std::cout << "Operador de asignacion, puedes asignar a una variable con {} o = al declarar la variable o al modificarla"<< std::endl;
  std::cout << " todos son el signo del operador, seguidos de un ="<< std::endl;
  std::cout << "Operador de suma y asignacion +=3: ->" << (numero += 3)<< std::endl;
  std::cout << "Operador de resta y asignacion -=3: ->" << (numero -= 4)<< std::endl;
  std::cout << "Multiplicamos y asignacion de numero *=3: ->" << (numero *= 3)<< std::endl;
  std::cout << "Division y asignacion de numero /=3: ->" << (numero /= 3)<< std::endl;
  std::cout << "Modulo y asignacion de numero %=3: ->" << (numero %= 3)<< std::endl;
  std::cout << "Hasta aqui los operadores de asignacion que yo conozco"<<std::endl;
  std::cout << "\n\n================================================================="<< std::endl;
  std::cout<<"Condicionales"<<std::endl;
  int condicionales{4};
  if (condicionales>2){
    std::cout<<"Este texto acaba de ejecutarse a traves de una condicional if\n";
  }
  //Else
  if(condicionales>10){
    std::cout<<"Esta condicional no se cumplira";
  }else{std::cout<<"Esta condicional es el else asi que como no se cumplio el if, esto se imprimira\n";}
  //else if 
  if(condicionales>100){
    std::cout<<"Esta condicional de nuevo no se cumplira\n";
  }else if(condicionales==4){std::cout<<"else if paso\n\n";}

  //switch
  switch(condicionales){
    //aca puedes poner los casos que gustes pero por fines practicos usaremos union
    case 4:
      std::cout<<"Este caso se va a cumplir por que el 4 iguala el valor de la variable que es la condicion\n";
    break;
    default:
      std::cout<<"En caso que ningun caso se cumpla o exista algun error recomiendo usar el default para caso por omision\n";
    break;
  }
  std::cout<<"\n====================================================================================\n\n";
  std::cout<<"Operaciones iterativas"<<std::endl;
  int contador=10;
  for (;contador > 0;contador--){
       std::cout<<contador<<": Numero de iteracion con ciclo for\n";
  }
  contador=10; //Volvemos a darle valor al contador
  while(contador>0){
    std::cout<<contador<<": Numero de itaracion con ciclo while\n";
    contador--;

  }

  //Dificultad extra 
  for (int i=10; i<56; i++){
    if(i%2==0 && i!=16 && i%3!=0){
      std::cout<<"Numero: "<<i<<std::endl;
    }
  }
  return 0;
}
