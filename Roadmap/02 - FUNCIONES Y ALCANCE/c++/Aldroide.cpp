/*
Ejercicio: Crear ejemplos de funciones basicas que representen diferentes
posiblidades del lenguaje:
    * Sin parametros ni retorno
    * Con uno o mas parametros,
    * Con retorno
    * Probar funciones dentro de funciones
    * Utilizar funciones ya creadas del lenguaje
    * Variable local y global
    * Debes hacer print por consola del resultado de todos los ejemplos.
    * (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
*/
#include <iostream>
#include <math.h>
using namespace std;
int EjercicioExtra(const char* param1, const char* param2);
void Simple(){
    cout<<"Funcion sin parametros ni retorno"<<endl;
}

void compuesta(string name){
    cout<<"Función que recibe tu nombre: "<<name<<" pero no tiene retorno"<<endl;
}

int suma(int a, int b){
    return a+b;
}

int i =10;

int main(){
    int local=90;
    Simple();
    compuesta("Aldo");
    cout<<"El resultado de 4 + 6 es: "<<suma(4,6)<<endl;
    cout<<"Se imprimieron "<<EjercicioExtra("Parametro1", "Parametro2")<<" numeros"<<endl;
    cout<<"Variable global: "<<i<<endl;
    cout<<i<<" elevado a 2 es: "<<exp(i)<<endl;
    cout<<"Variable local "<<local<<endl;
    return 0;

}


/*
* DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 */

int EjercicioExtra (const char* param1, const char* param2){
    int numVeces = 0;
    for (int i = 1; i <= 100; i++){
        if (i % 15 == 0){
            cout<<param1<<param2; 
        } else if (i % 3 == 0){
            cout<<param1;
        } else if (i % 5 == 0){
            cout<<param2;
        } else {
            cout<<i;
            numVeces++;
        }        
        cout<<endl;
    }
}