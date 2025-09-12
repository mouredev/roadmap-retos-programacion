
#include <iostream>
using namespace std;

int main()
{
  //operadores aritmeticos(+,-,*,/,%)
  cout<<endl<<"------Operadores aritmeticos--------"<<endl;
  cout<<"Suma: "<<(12+5)<<endl;
  cout<<"Resta: "<<(12-5)<<endl;
  cout<<"Multiplicación: "<<(12*5)<<endl;
  cout<<"División: "<<(12/5)<<endl;
  cout<<"Modulo: "<<(12%5)<<endl;
  
  //Operadores comparación (==,!=,>,<,>=,<=)
  cout<<endl<<"------Operadores comparacion--------"<<endl;
  cout<<"10 igual a 5: "<<(10==5)<<endl;
  cout<<"5 diferente a 5: "<<(5!=5)<<endl;
  cout<<"10 mayor a 5: "<<(10>5)<<endl;
  cout<<"5 menor a 1: "<<(5<1)<<endl;
  cout<<"8 mayor o igual a 5: "<<(8>=5)<<endl;
  cout<<"8 menor o igual a 5: "<<(8<=5)<<endl;
  
  //operadores asignacion (+=,-=,*=,/=,%=,>>=,<<=,&=,^=,|=)
  int y = 10;
  cout<<endl<<"------Operadores asignacion--------"<<endl;
  cout<<" (y+=2)=  "<<(y+=2)<<endl;
  cout<<" (y-=5)=  "<<(y-=5)<<endl;
  cout<<" (y*=3)=  "<<(y*=3)<<endl;
  cout<<" (y/=3)=  "<<(y/=3)<<endl;
  cout<<" (y%=4)=  "<<(y%=4)<<endl;
  cout<<" (y>>=1)= "<<(y>>=1)<<endl;
  cout<<" (y<<=2)= "<<(y<<=2)<<endl;
  cout<<" (y&=1)=  "<<(y&=1)<<endl;
  cout<<" (y^=3)=  "<<(y^=3)<<endl;
  cout<<" (y|=4)=  "<<(y|=4)<<endl;
  
  //logicos (!,&&,||)
  cout<<endl<<"------Operadores logicos--------"<<endl;
  cout<<"!(5==5)= "<<!(5==5)<<endl;
  cout<<"!(5<4)= "<<!(5<4)<<endl;
  cout<<"!(5>4)= "<<!(5>4)<<endl;
  cout<<"!true= "<<!true<<endl;
  cout<<"!false= "<<!false<<endl;
  cout<<"((5<4)&&(6==6))= "<<((5<4)&&(6==6))<<endl;
  cout<<"((9>3)&&(6!=4))= "<<((9>3)&&(6!=4))<<endl;
  cout<<"((1<6)&&(6>4))= "<<((1<6)&&(6>4))<<endl;
  cout<<"((7>10)||(6!=8))= "<<((7>10)||(6!=8))<<endl;
  cout<<"((3>5)||(5==1))= "<<((3>5)||(5==1))<<endl;
  cout<<"((7<12)||(9>=2))= "<<((7<12)||(9>=2))<<endl;
  
 //operadores bit (&,|,^,~,<<,>>)
  cout<<endl<<"------Operadores bit--------"<<endl;
  cout<<"AND (12&6)= "<<(12&6)<<endl;
  cout<<"OR (12|6)= "<<(12|6)<<endl;
  cout<<"XOR (12^6)= "<<(12^6)<<endl;
  cout<<"NOT (~12)= "<<(~12)<<endl;
  cout<<"SHL (12<<6)= "<<(12<<6)<<endl;
  cout<<"SHR (12>>6)= "<<(12>>6)<<endl;
  
  //operadores ternarios condicionales (?)
  cout<<endl<<"------Operadores ternarios condicionales--------"<<endl;
  cout<<"7==5 ? 4:3= "<<(7==5?4:3)<<endl;
  cout<<"7>=5 ? 4:3= "<<(7>=5?4:3)<<endl;
  cout<<"7>7 ? 4:3= "<<(7<5?4:3)<<endl;
  cout<<"7<=7 ? 4:3= "<<(7<=7?4:3)<<endl;
  cout<<"7<7 ? 4:3= "<<(7<5?4:3)<<endl;
  cout<<"a==b ? s:n= "<<('a'=='b'?'s':'n')<<endl;
  
  //Estructuras de control: condicional
  cout<<endl<<"------if else--------"<<endl;
  int numero = 5;
  if(numero%2==0)
    cout<<"El numero es par"<<endl;
  else if(numero%3!=0)
    cout<<"El numero es impar"<<endl;
  else
    cout<<"El numero no es par ni impar"<<endl;
 
    
  //Estructuras de control: While
  cout<<endl<<"------While--------"<<endl;
  
  int a = 0;
  
  while(a<5){
    cout<<"Valor de a: "<<a<<endl;
    a++;
  }
  
  //Estructuras de control: Do-While
  cout<<endl<<"------Do-While--------"<<endl;
  int x = 0;
  do{
    cout<<"Valor de x es: "<<x<<endl;
    x++;  
  }while(x<5);
  
  //Estructuras de control: For
  cout<<endl<<"------For--------"<<endl;
  
  for(int n=0;n<5;n++){
    cout<<"Valor de n es: "<<n<<endl;
  }
  
  //Estructuras de control: Switch
  cout<<endl<<"------Switch--------"<<endl;
  int dia = 5;
  switch(dia){
    case 1:
    cout<<"Dia 1 de la semana, Lunes"<<endl;
    break;
    case 2:
    cout<<"Dia 2 de la semana, Martes"<<endl;
    break;
    case 3:
    cout<<"Dia 3 de la semana, Miercoles"<<endl;
    break;
    case 4:
    cout<<"Dia 4 de la semana, Jueves"<<endl;
    break;
    case 5:
    cout<<"Dia 5 de la semana, Viernes"<<endl;
    break;
    case 6:
    cout<<"Dia 6 de la semana, Sabado"<<endl;
    break;
    case 7:
    cout<<"Dia 7 de la semana, Domingo"<<endl;
    break;
    default:
    cout<<"No se encuentra"<<endl;
    break;
  }
  
  //Estructuras de control: Excepcion
  cout<<endl<<"------Excepcion--------"<<endl;
  
  try{
    int edad = 10;
    if (edad>=18)
        cout<<"Eres mayor de edad, tienes "<<edad<<" años"<<endl;
    else
        throw edad;
  }
  catch (int num) {
    cout<<"Eres menor de edad, tienes "<<num<<" años"<<endl;
  }
  
  //Ejercicio extra
  cout<<endl<<"------Ejercicio Extra--------"<<endl;
  
  for(int i=10;i<56;i++){
    if((i%2==0)&&(i%3!=0)&&(i!=16))
        cout<<i<<endl;
  }
  
  return 0;
}
