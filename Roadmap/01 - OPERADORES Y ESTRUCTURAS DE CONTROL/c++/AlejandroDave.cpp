// Ejercicio 01
#include <iostream>
using namespace std;

int main(){
    //============ Operaciones Aritmeticas ================
    int a,b,c,d;
    cin>>a>>b;   // a y b seran declaradas por el usuario
    c = 20; d = 54 ; // c y d seran declaradas por el programa

    cout<<a<<" + "<<b<<" = "<<a+b<<endl;
    cout<<a<<" - "<<b<<" = "<<a-b<<endl;
    cout<<a<<" * "<<b<<" = "<<a*b<<endl;
    if(b!=0)cout<<a<<" / "<<b<<" = "<<a/b<<endl;

    //============ Operaciones logicas ===============
    /*
    para las operaciones logicas tenemos las siguientes operaciones
    && representa la operacion AND
    || representa la operacion OR
    ! representa la operacion NOT
    > representa mayor que
    < representa menor que
    == representa igualdad

    las operaciones booleanas nos devolveran un 1 si es true, y un 0 si es false
    */
    bool b1,b2,b3;
    b1 = (a>b)&&(c==d);
    b2 = (a==c)||(b>=d);
    b3 = !(a>b);
    cout<<b1<<b2<<b3;
    cout<<endl;
    //============= Operaciones condicionales ==================
    /*
    Los comandos condicionales se activan cuando se cumplen algun tipo de parametro establecido en el programa, como se vio en la representacion
    de la division, se genero una condicion donde se efectuara el siguiente codigo siempre y cuando se cumpla que b sea diferente de 0

    la condicional if/else se ejecuta cuando se cumple un parametro y en caso de no cumplirse se ejecutara el siguiente codigo
    la condicional while se ejecutara mientras el parametro se cumpla
    la condicional for se ejecutara de igual forma que el while, cuando se cumpla un parametro.
    */

    if(a>b) cout<<a<<" es mayor que "<<b<<endl;
    else cout<<a<<" es menor que "<<b<<endl;
    while(a>0){cout<<a<<" ";a--;}
    cout<<endl;
    for(int i = 0; i<b;i++){cout<<i<<" ";}
    cout<<endl;
    // Ejercicio extra

    for(int i=10;i<56;i++){
        if(i%2==0){
            if(i%3==1){
                if(i!=16){
                    cout<<i<<endl;
                }
            }
        }
    }

    return 0;
    }
