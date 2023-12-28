#include <iostream>
#include <cstdint>
#include <stdio.h>
#include <vector>
#include <array>
#include <string>
#include <limits>
#include <cassert>
#include <type_traits>
#include <bitset>


int returnTen();// fordware declaration de funcion que retorna el numero 10

//TODO LO DECLARADO ACA ES GLOBAL

/************************************************
*AQUI DECLARAMOS TODAS LAS CONSTANTES A UTILIZAR*
************************************************/
const int UNO{1}; //syntaxis: const /tipo/ /nombre/
const float UN_MEDIO{0.5};
const double UNO_Y_MEDIO{1.5};
const bool VERDADERO{true};
const int TEN{returnTen()};       //esta constante es especial, el valor no es conocido en tiempo de compilacion
//LAS SIGUIENTES SON CONSTANTES CUYO VALOR SERA CONOCIDO SIEMPRE EN TIEMPO DE COMPILACION
constexpr int DOS{2};
constexpr double DOS_MEDIOS{2.5};
constexpr double Z{DOS_MEDIOS+DOS}; //AQUI SE VE LA UTILIDAD DEL constexpr SON CONSTANT EXPESSIONS AUNQUE SEAN OPERACIONES, ESTAS SON CONOCIDAS ANTES DE CORRER EL PROGRAMA EN TIEMPO DE COMPILASION, POR LO QUE ES MAS EFICIENTE YA QUE LA OPERACION NO SE REPITE CADA VEZ QUE SE CORRE EL PROGRAMA

/*************************************************
**AQUI DECLARAMOS TODAS LAS VARIABLES A UTILIZAR**
*************************************************/

char miCaracterBase{0};                 //reservan 8bits de informacion en memoria, segun la arquitectura de sistema puede ser signado o no por defecto.
signed char miCaracter{-120};           //reservan 8bits de informacion en memoria, rango desde -128 a 127.
unsigned char miCaracterNoSign{255};    //reservan 8bits de informacion en memoria, rango desde 0 a 255
short miInt{10};                        //reservan 16bits de informacion en memoria, rango desde
signed short miIntSignado{};            //reservan 16bits de informacion en memoria, rango desde -32768 a 32767
unsigned short miIntNoSignado{};        //reservan 16bits de informacion en memoria, rango desde 0 a 65535
int miVariable{0};                      //valores enteros por defecto signado al menos de 16bits de informacion depende de modelo de datos del sistema en LP64 o 4/8/8 int es de 32bits
long miIntLong{0};                      //valores enteros por defecto signado al menos de 32bits de informacion depende de modelo de datos del sistema en LP64 o 4/8/8 int es de 64bits
unsigned long miUIntLong{0};            //version no signada de long
long long miInt2Long{0};                //valores enteros por defecto signado de 64bits
unsigned long long miUInt2Long{0};      //version no signada de long long
float miFlotante{0.0};                  //valores punto flotante usualmente de 32bits, siguen formato de IEEE-754 binary32 format
double miFlotanteD{0.0};                //valores punto flotante usualmente de 64bits, siguen formato de  IEEE-754 binary64 format
/*********************
*FIXED WIDTH INTEGERS*
*********************/
std::int8_t miInt8bits{0};              //int de 8bits estandarizado
std::uint8_t miUInt8bits{0};            //int de 8bits no signado estandarizado
std::int16_t miInt16bits{0};            //int de 16bits estandarizado
std::uint16_t miUInt16bits{0};          //int de 16bits no signado estandarizado
std::int32_t miInt32bits{0};            //int de 32bits estandarizado
std::uint32_t miUInt32bits{0};          //int de 32bits no signado estandarizado
std::int64_t miInt64bits{0};            //int de 64bits estandarizado
std::uint64_t miUInt64bits{0};          //int de 64bits no signado estandarizado
std::size_t s_t{0};                     //es definido como un typo integral no signado su tamaño varia dependiendo la arquitectura pero garantiza ser de al menos 16Bits

wchar_t miCaracter8Bit{};               //hecho para representar cualquier unidad de codigo UTF-32 en linux UTF-16 en windows
char16_t miCaracter16Bit{};             //para representar cualquier unidad de codigo UTF-16
char32_t miCaracter32Bit{};             //para representar cualquier unidad de codigo UTF-32

//Los int fast funcionan como los fixed width integers, pero son mâs râpidos, sin embargo hay que evitarlos pueden provocar desperdicio de memoria y
std::int_fast8_t miFastInt8bits{0};
std::uint_fast8_t miFastUInt8bits{0};
std::int_fast16_t miFastInt16bits{0};
std::uint_fast16_t miFastUInt16bits{0};
std::int_fast32_t miFastInt32bits{0};
std::uint_fast32_t miFastUInt32bits{0};
std::int_fast64_t miFastInt64bits{0};
std::uint_fast64_t miFastUInt64bits{0};




/*****************************************************************************
*<bitset> es una libreria que permite la manipulacion directa con bits en c++*
*****************************************************************************/
std::bitset<8> banderas{0b0000'0000};   //el valor correcto a usar con bitset es en formato de bits como se muestra en este ejemplo
std::bitset<16> estados{0x00FF};        //en este caso colocamos el valor de 0x00FF que es tratado como int o char, pero cpp hace una conversion implîcita a bits


/*********************
*DEFINICION DE CLASES*
*********************/
class Velocidad{
    private:
        std::vector<double> mVel{0,0};
    public:
        Velocidad(double x=0, double y=0)
        {
            mVel[0]=x;
            mVel[1]=y;
        }

        const double& getVelocidadX(){
            return mVel[0];
        }
        const double& getVelocidadY(){
            return mVel[1];
        }
        void setVelocidadX(double x){
            mVel[0]=x;
        }
        void setVelocidadY(double y){
            mVel[1]=y;
        }

        //overload de operador de subscripcion []
        /*
        double& operator[] (int index)
        {
            return mVel[index];
        }
        */
};

class Punto{
    private:
        std::array<double, 2> mPunto{0,0};
    public:
        Punto(double x=0, double y=0)
        {
            mPunto[0]=x;
            mPunto[1]=y;
        }

        const double& getPuntoX(){
            return mPunto[0];
        }
        const double& getPuntoY(){
            return mPunto[1];
        }
        void setPuntoX(double x){
            mPunto[0]=x;
        }
        void setPuntoY(double y){
            mPunto[1]=y;
        }

        //overload de operador de subscripcion []
        /*
        double& operator[] (int index)
        {
            return mVel[index];
        }
        */
};


class Auto{
    private:
        //Propiedades o miembros de la clase
        std::string mMarca{""};
        Velocidad mVelocidad2D{0,0};
        Punto mPunto2D{0,0};
    public:
        //Constructores
        //Auto()=default;
        Auto(std::string marca="", Velocidad velocidad0={0,0}, Punto punto0={1,1}){
            mMarca=marca;
            mVelocidad2D.setVelocidadX(velocidad0.getVelocidadX());
            mVelocidad2D.setVelocidadY(velocidad0.getVelocidadY());
            mPunto2D=punto0;
        }
        //Metodos
        void setMarca(std::string marca){
            mMarca = marca;
        }

        std::string getMarca(){
            return mMarca;
        }
        /*
        void setVelocidad2D(Velocidad velocidad){
            mVelocidad2D.setVelocidadX(velocidad[0]);
            mVelocidad2D.setVelocidadY(velocidad[1]);
        }*/
        void setVelocidad2D(Velocidad velocidad){
            mVelocidad2D.setVelocidadX(velocidad.getVelocidadX());//velocidad en x se coloca por el metodo set a partir de referencia de x en objeto velocidad
            mVelocidad2D.setVelocidadY(velocidad.getVelocidadY());//igual que en caso anterior pero para Y
        }

        Velocidad getVelocidad2D(){
            return mVelocidad2D;
        }

        void setPunto2D(Punto punto){
            mPunto2D = punto;                   //copia de objeto punto a mPunto2D
        }
        Punto getPunto2D(){
            return mPunto2D;
        }



};



//Este es main, funcion principal
int main(){
    //Aqui colocamos variables que se usaran en la funcion main
    //metodos de inicializacion
    int numerador=0;            //inicializacion por copia
    int denominador(1);         //inicializacion directa, se puede confundir con el forward declaration y por ello se evita, fordward declaration puede traducirse como declaracion frontal y es cuando un objeto o funcion se declara sin ser definida en su totalidad
    int entrada1{1};            //inicializacion directa, modo lista
    int entrada2{};             //igual que anterios, pero limpia la memoria reservada por la variable (coloca 0)
    int resultado={99};         //inicializacion por copia a partir de lista

    Auto primerAuto;            //se instancia un objeto primerAuto como clase Auto
    Velocidad v;                //se instancia un objeto v como clase Velocidad
    Punto p;                    //se instancia un objeto p como clase Punto

    //std::array<double, 2> puntoInicial{primerAuto.getPunto2D()};

    v=primerAuto.getVelocidad2D();

    std::cout<<"No te vayas, pero si quieres irte, no sigas el camino por el que vengo, mis pasos son pesados y los senderos que recorro los hecho a perder \n";
    std::cout<<"Imprimiendo una expresion constante"<<Z<<'\n';
    std::cout<<"Muestra de valor entero constante: "<<TEN<<'\n';
    std::cout<<"Limite char maximo: "<<static_cast<int>(std::numeric_limits<decltype(miCaracterBase)>::max())<<'\n';
    std::cout<<"Limite char minimo: "<<static_cast<int>(std::numeric_limits<decltype(miCaracterBase)>::min())<<'\n';
    std::cout<<"Limite signed char maximo: "<<static_cast<int>(std::numeric_limits<decltype(miCaracter)>::max())<<'\n';
    std::cout<<"Limite signed char minimo: "<<static_cast<int>(std::numeric_limits<decltype(miCaracter)>::min())<<'\n';
    std::cout<<"Limite unsigned char maximo: "<<static_cast<int>(std::numeric_limits<decltype(miCaracterNoSign)>::max())<<'\n';
    std::cout<<"Limite unsigned char minimo: "<<static_cast<int>(std::numeric_limits<decltype(miCaracterNoSign)>::min())<<'\n';
    std::cout<<"Limite short maximo: "<<std::numeric_limits<decltype(miInt)>::max()<<'\n';
    std::cout<<"Limite short minimo: "<<std::numeric_limits<decltype(miInt)>::min()<<'\n';
    std::cout<<"Limite signed short maximo: "<<std::numeric_limits<decltype(miIntSignado)>::max()<<'\n';
    std::cout<<"Limite signed short minimo: "<<std::numeric_limits<decltype(miIntSignado)>::min()<<'\n';
    std::cout<<"Limite unsigned short maximo: "<<std::numeric_limits<decltype(miIntNoSignado)>::max()<<'\n';
    std::cout<<"Limite unsigned short minimo: "<<std::numeric_limits<decltype(miIntNoSignado)>::min()<<'\n';
    std::cout<<"Limite int maximo: "<<std::numeric_limits<decltype(miVariable)>::max()<<'\n';
    std::cout<<"Limite int minimo: "<<std::numeric_limits<decltype(miVariable)>::min()<<'\n';
    std::cout<<"Limite long int maximo: "<<std::numeric_limits<decltype(miIntLong)>::max()<<'\n';
    std::cout<<"Limite long int minimo: "<<std::numeric_limits<decltype(miIntLong)>::min()<<'\n';
    std::cout<<"Limite unsigned long int maximo: "<<std::numeric_limits<decltype(miUIntLong)>::max()<<'\n';
    std::cout<<"Limite unsigned long int minimo: "<<std::numeric_limits<decltype(miUIntLong)>::min()<<'\n';
    std::cout<<"Limite long long int maximo: "<<std::numeric_limits<decltype(miInt2Long)>::max()<<'\n';
    std::cout<<"Limite long long int minimo: "<<std::numeric_limits<decltype(miInt2Long)>::min()<<'\n';
    std::cout<<"Limite unsigned long long int maximo: "<<std::numeric_limits<decltype(miUInt2Long)>::max()<<'\n';
    std::cout<<"Limite unsigned long long int minimo: "<<std::numeric_limits<decltype(miUInt2Long)>::min()<<'\n';
    std::cout<<"Limite float maximo: "<<std::numeric_limits<decltype(miFlotante)>::max()<<'\n';
    std::cout<<"Limite float minimo: "<<std::numeric_limits<decltype(miFlotante)>::min()<<'\n';

    banderas.set(3);
    std::cout<<"Estados antes de reset: "<<estados<<'\n';
    estados = (estados & static_cast<std::bitset<16>>(0x0000));
    std::cout<<"Banderas: "<<banderas<<'\n';
    std::cout<<"Estados despues de reset: "<<estados<<'\n';
    std::cout<<p.getPuntoX()<<'\n';
    std::cout<<v.getVelocidadX()<<'\n';
    v.setVelocidadX(25.5);
    double testCopy{v.getVelocidadX()};
    std::cout<<"Copiado componente x de velocidad v \n";
    std::cout<<v.getVelocidadX()<<'\n';
    v.setVelocidadX(55.7);
    std::cout<<v.getVelocidadX()<<'\n';


    std::cout<<"Copia realizada de componente x de velocidad v "<<testCopy<<'\n';

    p.setPuntoX(25.5);
    testCopy = p.getPuntoX();
    std::cout<<"Copiado componente x de punto p \n";
    std::cout<<p.getPuntoX()<<'\n';
    p.setPuntoX(55.7);
    std::cout<<p.getPuntoX()<<'\n';

    std::cout<<"Copia realizada de componente x de punto p "<<testCopy<<'\n';

    return 0;

}

int returnTen(){
    return 10;
}
