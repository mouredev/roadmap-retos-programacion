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
/************************************************************************************************************
*******************************REFERENCIAS DEL LENGUAJE C++**************************************************
*************************************************************************************************************
*sitio oficial de referencia https://learn.microsoft.com/es-es/cpp/cpp/cpp-language-reference?view=msvc-170 *
*Referencias recomendadas personalmente:                                                                    *
*  https://en.cppreference.com/w/                                                                           *
*  https://www.learncpp.com/                                                                                *
************************************************************************************************************/
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
short miInt{10};                        //reservan 16bits de informacion en memoria
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

//Los int fast funcionan como los fixed width integers, pero son mâs râpidos, sin embargo hay que evitarlos pueden provocar desperdicio de memoria y undefinded behaviour, que seria como comportamientos indefinidos, esto sucede cuando se pierde rastro de las regiones de memoria, pero lo mejor es ver la referencia oficial para mayor informacion
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

//definicion de enum class Marca, los enum class se prefieren en ocaciones a los enum porque funcionan parecido a un namespace, esto evita colisiones entre tipos
enum class Marca{
    audi,
    ferrari,
    chevrolet,
    toyota,
    mercedez,
    mazda,
};
std::ostream& operator<< (std::ostream& out, const Marca& marca);// este es un fordwar declaration de el overloading que se hace del operador de salida
const std::string MarcaToString(const Marca& marca);//este es un overloading de la funcion que transforma de Marca (un enum class) a String

//Estructura sin sentido colocada como ejemplo
struct noReasonToExist{
    Marca foreverAndEver{Marca::mazda};
    int sI{0};
    std::string sExistance{"Existo Luego Existo"};
    std::bitset<16> sBit{0xaefd};
};
/*********************
*DEFINICION DE CLASES*
*********************/
//definicion de clase Velocidad que representa el movimiento hacia una direccion de un punto en el espacio 2D
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

        //overload de operador de subscripcion [] si se desea se puede quitar el comentario y velicidad podra modificarce haciendo objeto[index] como con cualquier array
        /*
        double& operator[] (int index)
        {
            return mVel[index];
        }
        */
};

//definicion de clase Punto que representa un punto en el espacio 2D
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

        //overload de operador de subscripcion [] si se desea se puede quitar el comentario y punto podra modificarce haciendo objeto[index] como con cualquier array
        /*
        double& operator[] (int index)
        {
            return mVel[index];
        }
        */
};


class Auto{
    private://Los miembros privados solo son accesibles para la misma clase, no se pueden acceder por funciones externas, amenos que sean funciones amigas de la clase
        /************************************
        /*Propiedades o miembros de la clase*
        ************************************/
        Marca mMarca{Marca::mazda};
        Velocidad mVelocidad2D{0,0};
        Punto mPunto2D{0,0};
    public://Los miembros publicos si pueden ser accedidos desde el exterior de la Clase utilizando la sintaxis objeto.miembro
        /***************
        *CONSTRUCTORES:*
        ***************/
        //Los constructores son funciones especiales que tienen el mismo nombre que la clase en c++
        Auto(Marca marca=Marca::mazda, Velocidad velocidad0={0,0}, Punto punto0={1,1})//aqui estan los parametros de entrada, luego se define que hacer con ellos
        {
            //aca se copian los parametros de entrada a los miembros deseados de la clase
            mMarca=marca;
            mVelocidad2D.setVelocidadX(velocidad0.getVelocidadX());
            mVelocidad2D.setVelocidadY(velocidad0.getVelocidadY());
            mPunto2D=punto0;
        }
        /*********
        *METODOS:*
        *********/
        //modifica la marca del auto Marca es tipo enum class
        void setMarca(Marca marca){
            mMarca = marca;
        }
        //retorna la marca del auto Marca es tipo enum class
        Marca getMarca(){
            return mMarca;
        }
        void setVelocidad2D(Velocidad velocidad){
            mVelocidad2D.setVelocidadX(velocidad.getVelocidadX());//velocidad en x se coloca por el metodo set a partir de referencia de x en objeto velocidad
            mVelocidad2D.setVelocidadY(velocidad.getVelocidadY());//igual que en caso anterior pero para Y
        }
        //Se modifica la velocidad del objeto, se necesita pasar objeto clase Velocidad(double x, double y), estos solo reciben dos parametros double
        Velocidad getVelocidad2D(){
            return mVelocidad2D;
        }
        //Se modifica la posicion del objeto, se necesita pasar objeto clase Punto(double x, double y), estos solo reciben dos parametros double
        void setPunto2D(Punto punto){
            mPunto2D = punto;                   //copia de objeto punto a mPunto2D
        }
        //Se retorna la posicion del objeto
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

    noReasonToExist lameExistance;

    std::cout<<"\n\n\nTEST DE PRINT\n\n";
    std::cout<<"No te vayas, pero si quieres irte, no sigas el camino por el que vengo, mis pasos son pesados y los senderos que recorro los hecho a perder \n";
    std::cout<<"Imprimiendo una expresion constante"<<Z<<'\n';
    std::cout<<"Muestra de valor entero constante: "<<TEN<<'\n';

    /*******************************************************************************************************************************************
    *ACA SE IMPRIMEN LOS LIMITES MAYOR Y MENOR DE ALGUNAS VARIABLES, SE PUEDE USAR LA MISMA STRUCTURA PARA TODAS LAS VARIABLES DEFINIDAS EN C++*
    *************************************CORRER EL PROGRAMA PARA VER LOS RESULTADOS SI SE DESEA*************************************************
    *******************************************************************************************************************************************/

    std::cout<<"\n\n\nRANGOS DE VALORES PARA ALGUNOS TIPOS DE VARIABLES\n\n";
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

    /*********************************************************************
    *EN ESTA SECCION SE DEMUESTRAN ALGUNAS FORMAS DE TRABAJAR CON BITS****
    *********************************************************************/

    std::cout<<"\n\n\nTEST DE BANDERAS bitset\n\n";
    banderas.set(3);                                                    //set() es un metodo del tipo de objeto bitset que permite colocar el bit deseado como un 1 logico
    std::cout<<"Estados iniciales: "<<estados<<'\n';                    //imprimiendo estados iniciales
    estados = (estados & static_cast<std::bitset<16>>(0x0000));         //operacion and aplicada entre estados y el valor 0x0000 para borrar todo
    //se imprimen los datos
    std::cout<<"Estados reseteados exitosamente\n";
    std::cout<<"Muestra de estados despues de reset: "<<estados<<'\n';
    std::cout<<"Banderas: "<<banderas<<'\n';

    /*********************************************************************
    *EN ESTA SECCION SE DEMUESTRAN ALGUNAS FORMAS DE TRABAJAR CON OBJETOS*
    *********************************************************************/
    std::cout<<"\n\n---------------------------------------------\nPRUEBA DE OPERACIONES CON OBJETOS (OBJETO DE CLASE Auto).\n---------------------------------------------------";
    std::cout<<"\n\n\nESTADO INICIAL DE AUTO:\n\n";
    std::cout<<"Auto Marca: "<<primerAuto.getMarca()<<'\n'<<"desde latitud: "<<primerAuto.getPunto2D().getPuntoX()<<'\n'
    <<"longitud: "<<primerAuto.getPunto2D().getPuntoY()<<'\n'<<"Arrazando con todo a velocidad de: "<<primerAuto.getVelocidad2D().getVelocidadX()<<" al este\n"
    <<primerAuto.getVelocidad2D().getVelocidadY()<<" al norte\n";

    //MODIFICACION DE DATOS DEL OBJETO primerAuto
    primerAuto.setMarca(Marca::ferrari);                //NUEVA MARCA
    primerAuto.setVelocidad2D(Velocidad(180.00, 0.00)); //NUEVA VELOCIDAD
    primerAuto.setPunto2D(Punto(500.76, 122.55));       //NUEVO PUNTO EN EL ESPACIO 2D

    std::cout<<"\n\n\nESTADO DE AUTO ACTUALIZADO:\n\n";
    std::cout<<"Auto Marca: "<<primerAuto.getMarca()<<'\n'<<"desde latitud: "<<primerAuto.getPunto2D().getPuntoX()<<'\n'
    <<"longitud: "<<primerAuto.getPunto2D().getPuntoY()<<'\n'<<"Arrazando con todo a velocidad de: "<<primerAuto.getVelocidad2D().getVelocidadX()<<" al este\n"
    <<primerAuto.getVelocidad2D().getVelocidadY()<<" al norte\n";


    std::cout<<"\n\n\nDATOS DE ESTRUCTURA lameExistance CREADA ANTERIORMENTE:\n\n";
    std::cout<<"Auto: "<<lameExistance.foreverAndEver<<'\n';
    std::cout<<"sI: "<<lameExistance.sI<<'\n';
    std::cout<<"sExistance: "<<lameExistance.sExistance<<'\n';
    std::cout<<"sBit: "<<lameExistance.sBit<<'\n';
    return 0;

}

//funcion que simplemente devuelve una constante como demostracion de el uso de constantes definidas en run time
int returnTen(){
    return 10;
}
//funcion que imprime string con nombre de auto seleccionado (convierte Marca a Cadena de caracteres
const std::string MarcaToString(const Marca& marca){
    std::string strMarca{"Mazda"};

    switch(marca){
        case Marca::audi:
            strMarca="Audi";
            break;
        case Marca::ferrari:
            strMarca="Ferrari";
            break;
        case Marca::chevrolet:
            strMarca="Chevrolet";
            break;
        case Marca::toyota:
            strMarca="Toyota";
            break;
        case Marca::mercedez:
            strMarca="Mercedez";
            break;
        case Marca::mazda:
            strMarca="Mazda";
            break;
    }
    return strMarca;
}

//definiendo el overloading del operador de output << para aceptar enum class
std::ostream& operator<< (std::ostream& out, const Marca& marca){
    out<<MarcaToString(marca);
    return out;

}
