#include <iostream>
#include <cstdint>
#include <stdio.h>
#include <compare>
#include <typeinfo>
#include <numeric>

#include <vector>
#include <array>
#include <string>
#include <bitset>

/*****************************************************************************************************************************************************
El siguiente es un programa de ejemplo que muestra conceptos de operaciones en cpp y structuras de control, el codigo se divide de la siguiente forma
**primera seccion:
******Formado por los forward declaration de las funciones a utilizar, se declaran antes de definirce para que el compilador sepa que existen
**segunda seccion:
******Declaracion de variables y punteros
**tercer seccion:
******Definicion de Clases, estructuras y enumeradores
******respecto al enumerador se define para uso de un menu de opciones e incluye un overload del operador de entrada de datos >>
**cuarta seccion:
******la cuarta seccion es donde corre el programa, comienza con main y luego va a la funcion runMenu() que corre todo
**quinta seccion:
******la quinta seccion es donde se encuentran todos los ejemplos de operadores, aqui se debe referir si se quieren ver los ejemplos
***NOTA: Falta agregar iteradores, es un tema muy amplio, por lo que se agregara luego
******************************************************************************************************************************************************/


/********************
**FUNCION PRINCIPAL**
********************/
void runMenu();




/********************************************
**FUNCION QUE MUESTRA OPERADORES ARITMETICOS*
********************************************/
void showArith();
/*****************************************
**FUNCION QUE MUESTRA OPERADORES LOGICOS**
*****************************************/
void showLogic();
/*****************************************
**FUNCION QUE MUESTRA OPERADORES DE BITS**
*****************************************/
void showBits();
/*********************************************************
**FUNCION QUE MUESTRA OPERADORES DE ASIGNACION COMPUESTOS*
*********************************************************/
void showAssign();
/***********************************************************
**FUNCION QUE MUESTRA OPERADORES DE RELACION Y COMPARACION**
***********************************************************/
void showComp();
/*******************************************************
**FUNCION QUE MUESTRA OPERADORES DE ACCESO A MIEMBROS **
*******************************************************/
void showAcces();
/**************************************
**FUNCION QUE MUESTRA EJEMPLO DE FOR **
**************************************/
void showFor();
/**************************************
**FUNCION QUE MUESTRA EL RETO EXTRA **
**************************************/
void retoExtra();

std::string compResult(const auto x);//FUNCION COMPLEMENTARIA PARA MUESTRA DE UNO DE LOS EJEMPLOS EN OPERADORES DE COMPARACION


/**************************
**DECLARACION DE VARIABLES*
**************************/
constexpr int numConst{20};
constexpr int SIZE_INIT{10};
constexpr int SIZE_FINAL{55};
constexpr int nSize{(SIZE_FINAL+1)-SIZE_INIT};
int numA{2};
int numB{5};
int numResult{0};
double realA{4};
double realB{8};
double realResult{0};

double matrixA[2][2]={  {12.4,20.6},
                        {3.5,10.1}};

bool boolA{true};
bool boolB{false};
bool boolC{true};
bool boolResult{false};

std::bitset<8> inputA{0b0000'1000};
std::bitset<8> inputB{0b0000'0010};
std::bitset<8> inputC{0b0000'1111};
std::bitset<8> outputR{0b0000'0000};

std::vector<int> rangoN(nSize);

/**********
**PUNTEROS*
**********/

int* pointerA{new int{20}};
int* pointerB{new int{30}};
int* pointerC{nullptr};



/**********************************************************************
*****************************ESTRUCTURAS Y CLASES**********************
**********************************************************************/
struct myStruct{
    int x{};
    int y{};
    void print(){
        std::cout<<"member x= "<<x<<'\n';
        std::cout<<"member y= "<<y<<'\n';
    }

};

class myClass{
    private:
        std::bitset<8>* mInputB{new std::bitset<8>{0b0000'1000}};
        std::bitset<8> mInputA{0b0001'1000};
    public:
        static std::bitset<8> mInputS;

    public:
        myClass(std::bitset<8> inputA=0b0001'1000){
            mInputA=inputA;
            mInputS<<=1;
        }
        ~myClass(){
            delete mInputB;
            std::cout<<"\nmInputB deleted\n";
            mInputB=nullptr;
        }
        void print(){
            std::cout<<"member mInputA= "<<mInputA<<'\n';
            std::cout<<"member mInputB= "<<*mInputB<<'\n';
        }
        static void staticPrint(){
            std::cout<<"member mInputS= "<<mInputS<<'\n';
        }
};
std::bitset<8> myClass::mInputS=0b0000'0001;

/******************************************************************************************
*********************ENUMERADOR LLAMADO Options********************************************
******************************************************************************************/
enum class Options
{
    aritmetic,
    logic,
    bits,
    asign,
    comp,
    acces,
    ejemplofor,
    retopluss,
    si,
    no,
    invalido,
    limit
};
//se hace overload de operador de input >> para aceptar Options
std::istream& operator>> (std::istream& in, Options& op)
{
    std::string input{};
    in>>input;
    /****************************************
    *ESTRUCTURA DE CONTROL IF, ELSE IF, ELSE*
    ****************************************/
        if(input == "ari"){
            op = Options::aritmetic;
        }else if(input == "log"){
            op = Options::logic;
        }else if(input == "bit"){
            op = Options::bits;
        }else if(input == "asi"){
            op = Options::asign;
        }else if(input == "com"){
            op = Options::comp;
        }else if(input == "acc"){
            op = Options::acces;
        }else if(input == "for"){
            op = Options::ejemplofor;
        }else if(input == "ext"){
            op = Options::retopluss;
        }else if(input == "si"){
            op = Options::si;
        }else if(input == "no"){
            op = Options::no;
        }else if(input == "lim"){
            op = Options::limit;
        }else{
            op = Options::invalido;
        }

    return in;
}
/*********AQUI FINALIZA LO REFERENTE A Options*************/



myClass xObject{};
myClass* xObjectPrt{new myClass{inputC}};



int main(){

    std::iota(rangoN.begin(), rangoN.end(), SIZE_INIT);

    runMenu();//corre menu, es donde se corre todo lo referente a los ejemplos

    //para todo puntero se debe liberar la memoria reservada con delete
    delete pointerA;
    delete pointerB;
    delete pointerC;
    delete xObjectPrt;

    //una vez liberada la memoria de los punteros se debe asignar puntero nulo como buena practica
    pointerA=nullptr;
    pointerB=nullptr;
    pointerC=nullptr;
    xObjectPrt=nullptr;

    return 0;
}

void runMenu(){



    Options selected{Options::limit};

    /****************************
    ***ESTE ES UN BUCLE DO WHILE*
    ****************************/
    do{
        std::cout<<"TE MOSTRAMOS LOS DIFERENTES OPERADORES EN C++\n \
            selecciona entre las siguientes secciones para ver ejemplos:\n \
            codigo: | tema:...............................\n \
            ari     | OPERADORES ARITMETICOS              \n \
            log     | OPERADORES LOGICOS                  \n \
            bit     | OPERADORES DE BITS                  \n \
            asi     | OPERADORES DE ASIGNACION COMPUESTOS \n \
            com     | OPERADORES DE RELACION Y COMPARACION\n \
            acc     | OPERADORES DE ACCESO A MIEMBROS\n \
            for     | ESTRUCTURA DE CONTROL FOR, ES PARA ITERAR\n \
            ext     | entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3\n\
                        \nIngresa el codigo para la opcion deseada\n";
        std::cin>>selected;

        /**********************************
        *ESTRUCTURA DE CONTROL SWITCH CASE*
        **********************************/
        switch(selected){
            case Options::aritmetic:
                std::cout<<"Has seleccionado aritmeticos\n";
                showArith();
            break;
            case Options::logic:
                std::cout<<"Has seleccionado logicas\n";
                showLogic();
            break;
            case Options::bits:
                std::cout<<"Has seleccionado bits\n";
                showBits();
            break;
            case Options::asign:
                std::cout<<"Has seleccionado asignasion\n";
                showAssign();
            break;
            case Options::comp:
                std::cout<<"Has seleccionado comparacion\n";
                showComp();
            break;
            case Options::acces:
                std::cout<<"Has seleccionado acceso\n";
                showAcces();
            break;
            case Options::ejemplofor:
                std::cout<<"Has seleccionado Ejemplo de bucle for\n";
                showFor();
            break;
            case Options::retopluss:
                std::cout<<"Has seleccionado El reto extra\n";
                retoExtra();
            break;
            case Options::limit:
                std::cout<<"estas fuera de rango\n";
            break;
            default:
                std::cout<<"Invalido\n";
            break;
        }
        /******************************
        ***ESTE ES OTRO BUCLE DO WHILE*
        ******************************/
        do{
            std::cout<<"Deseas correr otro ejemplo? selecciona: \n\
            --si\n\
            --no\n";
            std::cin>>selected;
            if((selected != Options::si) && (selected != Options::no)) {
                selected=Options::invalido;
                std::cout<<"Invalido\n";
            }
        }while(selected == Options::invalido);//SIEMPRE QUE SE CUMPLA LA CONDICION selected == Options::invalido EL BUCLE SE REPITE

    }while(selected == Options::si);//SIEMPRE QUE SE CUMPLA LA CONDICION selected == Options::si EL BUCLE SE REPITE



}

void showArith(){
    /*************************
    **OPERADORES ARITMETICOS
    *************************/

    //Variables y constantes a utilizar
    std::cout<<"numConst = "<<numConst<<'\n';
    std::cout<<"numA: "<<numA<<'\n';
    std::cout<<"numB: "<<numB<<"\n\n";

    //operador de asignacion =
    std::cout<<"operador ="<<'\n';
    numResult = numConst;
    std::cout<<"numResult =  numConst \n"<<"= "<<numResult<<"\n\n";

    //operador de adision
    std::cout<<"operador +"<<'\n';
    std::cout<<"numA + numB = numResult\n";
    numResult = numA + numB;
    std::cout<<numA<<" + "<<numB<<" = "<<numResult<<"\n\n";

    //operador de substraccion
    std::cout<<"operador -"<<'\n';
    std::cout<<"numA - numB = numResult\n";
    numResult = numA - numB;
    std::cout<<numA<<" - "<<numB<<" = "<<numResult<<"\n\n";

    //operador de multiplicacion
    std::cout<<"operador *"<<'\n';
    std::cout<<"numA * numB = numResult\n";
    numResult = numA * numB;
    std::cout<<numA<<" * "<<numB<<" = "<<numResult<<"\n\n";

    //operador de division
    std::cout<<"operador /"<<'\n';
    std::cout<<"realA / realB = realResult\n";
    realResult = realA / realB;
    std::cout<<realA<<" / "<<realB<<" = "<<realResult<<"\n\n";

    //operador modulo
    std::cout<<"operador %"<<'\n';
    std::cout<<"realA % realB = realResult\n";
    realResult = (static_cast<int>(realB)) % (static_cast<int>(realA));
    std::cout<<realB<<" % "<<realA<<" = "<<realResult<<"\n\n";


};
void showLogic(){

    /**********************
    **OPERADORES LOGICOS**
    **********************/

    //operador OR || con boolean
    std::cout<<"operador ||"<<'\n';
    std::cout<<"boolA || boolB = boolResult\n";
    boolResult = boolA || boolB;
    std::cout<<boolA<<" || "<<boolB<<" = "<<boolResult<<"\n\n";

    //operador AND && con boolean
    std::cout<<"operador &&"<<'\n';
    std::cout<<"boolA && boolB = boolResult\n";
    boolResult = boolA && boolB;
    std::cout<<boolA<<" && "<<boolB<<" = "<<boolResult<<"\n\n";

    //operador NOT ! con boolean
    std::cout<<"operador !"<<'\n';
    std::cout<<"!boolA = boolResult\n";
    boolResult = !boolA;
    std::cout<<" !"<<boolA<<" = "<<boolResult<<"\n\n";
};

void showBits(){
    /**********************
    **OPERADORES DE BITS**
    **********************/

    //operador OR |
    std::cout<<"operador |"<<'\n';
    std::cout<<"inputA | inputB = outputR\n";
    outputR = inputA | inputB;
    std::cout<<inputA<<" | "<<inputB<<" = "<<outputR<<"\n\n";

    //operador AND &
    std::cout<<"operador &"<<'\n';
    std::cout<<"inputA & inputB = outputR\n";
    outputR = inputA & inputB;
    std::cout<<inputA<<" & "<<inputB<<" = "<<outputR<<"\n\n";

    //operador NOT ~
    std::cout<<"operador ~"<<'\n';
    std::cout<<"~inputA = outputR\n";
    outputR = ~inputA;
    std::cout<<" ~"<<inputA<<" = "<<outputR<<"\n\n";

    //operador XOR ^
    std::cout<<"operador ^"<<'\n';
    std::cout<<"inputA ^ inputC = outputR\n";
    outputR = inputA ^ inputC;
    std::cout<<inputA<<" ^ "<<inputC<<" = "<<outputR<<"\n\n";

    //operador  dezplazamiento logico a izquierda (left shift) <<
    std::cout<<"operador <<"<<'\n';
    std::cout<<"inputC << numA = outputR\n";
    outputR = inputC << numA;
    std::cout<<inputC<<" << "<<numA<<" = "<<outputR<<"\n\n";

    //operador  dezplazamiento logico a derecha (right shift) >>
    std::cout<<"operador >>"<<'\n';
    std::cout<<"inputC >> numA = outputR\n";
    outputR = inputC >> numA;
    std::cout<<inputC<<" >> "<<numA<<" = "<<outputR<<"\n\n";

};
void showAssign(){
    /*************************************
    **OPERADORES DE ASIGNACION COMPUESTOS*
    *************************************/

    std::cout<<"operador +="<<'\n';
    std::cout<<"realA += realB =\n";
    std::cout<<realA<<" += "<<realB<<" = "<<(realA += realB, realA)<<"\n\n";

    std::cout<<"operador -="<<'\n';
    std::cout<<"realA -= realB =\n";
    std::cout<<realA<<" -= "<<realB<<" = "<<(realA -= realB, realA)<<"\n\n";

    std::cout<<"operador *="<<'\n';
    std::cout<<"realA *= realB =\n";
    std::cout<<realA<<" *= "<<realB<<" = "<<(realA *= realB, realA)<<"\n\n";

    std::cout<<"operador /="<<'\n';
    std::cout<<"realA /= realB =\n";
    std::cout<<realA<<" /= "<<realB<<" = "<<(realA /= realB, realA)<<"\n\n";

    std::cout<<"operador %="<<'\n';
    std::cout<<"numB %= numA =\n";
    std::cout<<numB<<" %= "<<numA<<" = "<<(numB %= numA, numB)<<"\n\n";

    std::cout<<"operador |= usando bits"<<'\n';
    std::cout<<"inputA |= inputB =\n";
    std::cout<<inputA<<" |= "<<inputB<<" = "<<(inputA |= inputB, inputA)<<"\n\n";

    std::cout<<"operador |= usando booleanos"<<'\n';
    std::cout<<"boolA |= boolB =\n";
    std::cout<<boolA<<" |= "<<boolB<<" = "<<(boolA |= boolB, boolA)<<"\n\n";

    std::cout<<"operador &= usando bits"<<'\n';
    std::cout<<"inputA &= inputB =\n";
    std::cout<<inputA<<" &= "<<inputB<<" = "<<(inputA &= inputB, inputA)<<"\n\n";

    std::cout<<"operador &= usando booleanos"<<'\n';
    std::cout<<"boolA &= boolB =\n";
    std::cout<<boolA<<" &= "<<boolB<<" = "<<(boolA &= boolB, boolA)<<"\n\n";

    std::cout<<"operador ^= usando bits"<<'\n';
    std::cout<<"inputA ^= inputC =\n";
    std::cout<<inputA<<" ^= "<<inputC<<" = "<<(inputA ^= inputC, inputA)<<"\n\n";

    std::cout<<"operador ^= usando booleanos"<<'\n';
    std::cout<<"boolA ^= boolC =\n";
    std::cout<<boolA<<" ^= "<<boolC<<" = "<<(boolA ^= boolC, boolA)<<"\n\n";

    std::cout<<"operador <<= usando bits"<<'\n';
    std::cout<<"inputA <<= numA =\n";
    std::cout<<inputA<<" <<= "<<numA<<" = "<<(inputA <<= numA, inputA)<<"\n\n";

    std::cout<<"operador >>= usando bits"<<'\n';
    std::cout<<"inputA >>= numB =\n";
    std::cout<<inputA<<" >>= "<<numB<<" = "<<(inputA >>= numB, inputA)<<"\n\n";
};
void showComp(){

    /***************************************
    **OPERADORES DE RELACION Y COMPARACION**
    ***************************************/

    //operador igual a ==
    std::cout<<"operador =="<<'\n';
    std::cout<<"numA == numB = numResult\n";
    boolResult = numA == numB;
    std::cout<<numA<<" == "<<numB<<" = "<<boolResult<<"\n\n";

    //operador diferente de !=
    std::cout<<"operador !="<<'\n';
    std::cout<<"numA != numB = numResult\n";
    boolResult = numA != numB;
    std::cout<<numA<<" != "<<numB<<" = "<<boolResult<<"\n\n";

    //operador menor que <
    std::cout<<"operador <"<<'\n';
    std::cout<<"numA < numB = numResult\n";
    boolResult = numA < numB;
    std::cout<<numA<<" < "<<numB<<" = "<<boolResult<<"\n\n";

    //operador mayor que >
    std::cout<<"operador >"<<'\n';
    std::cout<<"numA > numB = numResult\n";
    boolResult = numA > numB;
    std::cout<<numA<<" > "<<numB<<" = "<<boolResult<<"\n\n";

    //operador menor o igual que <=
    std::cout<<"operador <="<<'\n';
    std::cout<<"numA <= numB = numResult\n";
    boolResult = numA <= numB;
    std::cout<<numA<<" <= "<<numB<<" = "<<boolResult<<"\n\n";

    //operador mayor o igual que >=
    std::cout<<"operador >="<<'\n';
    std::cout<<"numA >= numB = numResult\n";
    boolResult = numA >= numB;
    std::cout<<numA<<" >= "<<numB<<" = "<<boolResult<<"\n\n";

    //operador de tres vias <=>, no lo entendi bien, queda de tarea investigar mas

    std::cout<<"operador <=>"<<'\n';
    std::cout<<"realA <=> numB = numResult\n";
    {
        auto x = realA <=> numB;
        std::cout<<realA<<" <=> "<<numB<<" = "<<realA<<compResult(x)<<numB<<"\n\n";
    }


    std::cout<<"realA <=> realB = numResult\n";
    {
        auto x = numA <=> numB;
        std::cout<<realA<<" <=> "<<realB<<" = "<<realA<<compResult(x)<<realB<<"\n\n";
    }
};
void showAcces(){
    /***********************************
    **OPERADORES DE ACCESO A MIEMBROS **
    ***********************************/

    //operador de subscripcion []
    std::cout<<"operador [](subscripcion)"<<'\n';
    std::cout<<"Suponiendo que se tiene la siguiente matriz:\n double matrixA[2][2]={  {12.4,20.6},{3.5,10.1}};\n";
    std::cout<<"Se puede acceder a primera columna primera fila de la siguiente forma matrixA[0][0]\n"<<matrixA[0][0]<<'\n';
    std::cout<<"Se puede acceder a segunda columna primera fila de la siguiente forma matrixA[0][1]\n"<<matrixA[0][1]<<'\n';
    std::cout<<"\n\n";


    //operador  direccion de &
    std::cout<<"operador &(direccion de)"<<'\n';
    pointerC = new int{0};
    std::cout<<"Para pointerC inicialmente:\n";
    std::cout<<*pointerC<<" es el valor "<<pointerC<<" la direccion "<<"\n\n";
    std::cout<<"pointerC = &numResult ---> pointerC apunta a direccion de numResult\n";
    delete pointerC;
    pointerC = &numResult;
    std::cout<<"Para pointerC:\n";
    std::cout<<*pointerC<<" es el valor "<<pointerC<<" la direccion "<<"\n\n";
    std::cout<<"Para numResult:\n";
    std::cout<<numResult<<" es el valor "<<&numResult<<" la direccion "<<"\n";
    std::cout<<"\n\n";
    //operador  de dereferencia *
    std::cout<<"operador * (de dereferencia)"<<'\n';
    pointerC = new int{0};
    std::cout<<"*pointerC = *pointerA ---> pointerC apunta a direccion diferente de pointerA, pero a copiado el valor\n";
    *pointerC = *pointerA;
    std::cout<<"Para pointerC:\n";
    std::cout<<*pointerC<<" es el valor "<<pointerC<<" la direccion donde apunta "<<&pointerC<<" la direccion del puntero C"<<"\n\n";
    std::cout<<"Para pointerA:\n";
    std::cout<<*pointerA<<" es el valor "<<pointerA<<" la direccion donde apunta "<<&pointerA<<" la direccion del puntero A"<<"\n\n";


    //operador  miembro de objeto .
    std::cout<<"operador . (acceso a miembro de objeto)"<<'\n';
    std::cout<<"se instancia objeto xObject clase myClass y accedemos a metodo print con xObject.print()\n";
    xObject.print();
    std::cout<<"\n\n";

    //operador  miembro de puntero ->
    std::cout<<"operador -> (acceso a miembro de puntero)"<<'\n';
    std::cout<<"puntero xObjectPrt apunta a objeto clase myClass, accedemos a metodo print con xObjectPrt->print()\n";
    xObjectPrt->print();
    std::cout<<"\n\n";

    //operador  puntero a miembro de objeto .*
    std::cout<<"operador .* (puntero a miembro de objeto)"<<'\n';
    std::cout<<"print es metodo de clase myClass, se puede hacer puntero al metodo asi: void (myClass::*printPtr)() = &myClass::print;\n";
    void (myClass::*printPtr)() = &myClass::print;
    std::cout<<"llamamos al metodo con cualquier objeto de la clase de la siguiente forma (xObject.*printPtr)();\n";
    (xObject.*printPtr)();
    std::cout<<"\n\n";

    //operador  puntero a miembro de puntero ->*
    std::cout<<"operador ->* (puntero a miembro de puntero)"<<'\n';
    std::cout<<"tambien podemos llamar al metodo con cualquier puntero apuntando a la clase de la siguiente forma (xObjectPrt->*printPtr)();\n";
    (xObjectPrt->*printPtr)();
    std::cout<<"\n\n";

    printPtr=nullptr;
};

void showFor(){
    /******************************************
    *ESTRUCTURA DE CONTROL FOR, ES PARA ITERAR*
    ******************************************/
    for(int i=0;i<=1;++i){
        for(int j=0;j<=1;++j) std::cout<<"columna: "<<i+1<<" fila: "<<j+1<<" : "<<matrixA[i][j]<<'\n';
    }
}
void retoExtra(){
    /***********************
    **ESTE ES EL RETO EXTRA*
    ***********************/
    for(auto elementN : rangoN){
        if(!(elementN%2) && elementN!=16 && (elementN%3)){
            std::cout<<elementN<<'\n';
        }
    }
}



std::string compResult(const auto x){
    /****************************************
    *ESTRUCTURA DE CONTROL IF, ELSE IF, ELSE*
    ****************************************/
    if(typeid(x) == typeid(std::strong_ordering)){
        if(x<0){
            return " + menor que ";
        }else if(x>0){
            return " + mayor que ";
        }else if(x==0){
            return " + igual valor que ";
        }else{
            return " tipo incompatible ";
        }
    }else if(typeid(x) == typeid(std::partial_ordering)){
        if(x<0){
            return " - menor que ";
        }else if(x>0){
            return " - mayor que ";
        }else if(x==0){
            return " - igual valor que ";
        }else{
            return " tipo incompatible ";
        }
    }else{
        return "No valido";
    }

}
