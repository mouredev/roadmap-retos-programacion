#include <iostream>
#include <cstdint>
#include <stdio.h>

#include <vector>
#include <array>
#include <string>
#include <bitset>

constexpr int numConst{20};
int numA{2};
int numB{5};
int numResult{0};

double realA{4};
double realB{8};
double realResult{0};

bool boolA{true};
bool boolB{false};
bool boolC{true};
bool boolResult{false};


int main(){


    /*************************
    **OPERADORES ARITMETICOS
    *************************/

    //Variables y constantes a utilizar
    std::cout<<"numConst = "<<numConst<<'\n';
    std::cout<<"numA: "<<numA<<'\n';
    std::cout<<"numB: "<<numB<<'\n';

    //operador de asignacion =
    std::cout<<"operador ="<<'\n';
    numResult = numConst;
    std::cout<<"numResult =  numConst \n"<<"= "<<numResult<<'\n';

    //operador de adision
    std::cout<<"operador +"<<'\n';
    std::cout<<"numA + numB = numResult\n";
    numResult = numA + numB;
    std::cout<<numA<<" + "<<numB<<" = "<<numResult<<'\n';

    //operador de substraccion
    std::cout<<"operador -"<<'\n';
    std::cout<<"numA - numB = numResult\n";
    numResult = numA - numB;
    std::cout<<numA<<" - "<<numB<<" = "<<numResult<<'\n';

    //operador de multiplicacion
    std::cout<<"operador *"<<'\n';
    std::cout<<"numA * numB = numResult\n";
    numResult = numA * numB;
    std::cout<<numA<<" * "<<numB<<" = "<<numResult<<'\n';

    //operador de division
    std::cout<<"operador /"<<'\n';
    std::cout<<"realA / realB = realResult\n";
    realResult = realA / realB;
    std::cout<<realA<<" / "<<realB<<" = "<<realResult<<'\n';

    //operador modulo
    std::cout<<"operador %"<<'\n';
    std::cout<<"realA % realB = realResult\n";
    realResult = (static_cast<int>(realB)) % (static_cast<int>(realA));
    std::cout<<realB<<" % "<<realA<<" = "<<realResult<<'\n';



    /*************************************
    **OPERADORES DE ASIGNACION COMPUESTOS*
    *************************************/

    std::cout<<"operador +="<<'\n';
    std::cout<<"realA += realB =\n";
    std::cout<<realA<<" += "<<realB<<" = "<<(realA += realB, realA)<<'\n';

    std::cout<<"operador -="<<'\n';
    std::cout<<"realA -= realB =\n";
    std::cout<<realA<<" -= "<<realB<<" = "<<(realA -= realB, realA)<<'\n';

    std::cout<<"operador *="<<'\n';
    std::cout<<"realA *= realB =\n";
    std::cout<<realA<<" *= "<<realB<<" = "<<(realA *= realB, realA)<<'\n';

    std::cout<<"operador /="<<'\n';
    std::cout<<"realA /= realB =\n";
    std::cout<<realA<<" /= "<<realB<<" = "<<(realA /= realB, realA)<<'\n';


    /***************************************
    **OPERADORES DE RELACION Y COMPARACION**
    ***************************************/

    //operador igual a ==
    std::cout<<"operador =="<<'\n';
    std::cout<<"numA == numB = numResult\n";
    boolResult = numA == numB;
    std::cout<<numA<<" == "<<numB<<" = "<<boolResult<<'\n';

    //operador diferente de !=
    std::cout<<"operador !="<<'\n';
    std::cout<<"numA != numB = numResult\n";
    boolResult = numA != numB;
    std::cout<<numA<<" != "<<numB<<" = "<<boolResult<<'\n';

    //operador menor que <
    std::cout<<"operador <"<<'\n';
    std::cout<<"numA < numB = numResult\n";
    boolResult = numA < numB;
    std::cout<<numA<<" < "<<numB<<" = "<<boolResult<<'\n';

    //operador mayor que >
    std::cout<<"operador >"<<'\n';
    std::cout<<"numA > numB = numResult\n";
    boolResult = numA > numB;
    std::cout<<numA<<" > "<<numB<<" = "<<boolResult<<'\n';

    //operador menor o igual que <=
    std::cout<<"operador <="<<'\n';
    std::cout<<"numA <= numB = numResult\n";
    boolResult = numA <= numB;
    std::cout<<numA<<" <= "<<numB<<" = "<<boolResult<<'\n';

    //operador mayor o igual que >=
    std::cout<<"operador >="<<'\n';
    std::cout<<"numA >= numB = numResult\n";
    boolResult = numA >= numB;
    std::cout<<numA<<" >= "<<numB<<" = "<<boolResult<<'\n';


    /**********************
    **OPERADORES LOGICOS**
    **********************/



    /*****************************
    **OPERACIONES CON CARACTERES**
    *****************************/

    /***********************************
    **OPERACIONES CON CADENAS DE TEXTO**
    ***********************************/



    return 0;
}
