//******************************************************************************
//* Nota: Para el Proyecto de Dificultad Extra se utilizara librerias
//* para mejor facilidad y no tener que crear cada funcionalidad desde
//* cero, y seran las siguientes.

#include <iostream> // Entrada y Salida de datos.
#include <string>   // Tipo de dato string. (de la Libreria estandar C++)
#include <vector>   // Tipo de dato Vector. (de la Libreria estandar C++)


//******************************************************************************

using namespace std;

//* Declaracion de funciones para el ejercicio Extra

struct Contactos {
    string nombre;
    string celular;
    string correo;
};

void formatear (  
    char caracter, string palabras, int orientacion=0, 
    bool vacio=true, int espacio = 44
);

int buscar_contacto(string buscar, vector<Contactos> vect);


// ********************** #03 - Estructuras de datos ********************** //

/*
 * Las estructuras de datos basicas Primitivas de C++ son:
 *  > int, float, double, char, bool (Tipos básicos) (Estructura de 1 solo dato)
 *  > Arrays (Arreglos estáticos)
 *  > struct (Agrupa distintos tipos de datos)
 *  > pointers (Punteros, es para trabajar con direcciones de memoria) (1 dato)
 *  > enum (Enumeraciones)
 * 
 * 
 * Las anteriores son las estructuras Basicas Primitivas, de los anteriores
 * surgen estructuras de datos, de la biblioteca estandar de C++,
 * es decir surgen mas estructuras de datos pero tienes que importarlas,
 * segun la que nesesites. (son aproximadamente mas de 14 bibliotecas
 * estandar con estructuras de datos diferentes).
 * 
 * Los siguientes son estructuras de datos Primitivas del lenguaje que no se
 * importan de ninguna biblioteca en las que se pueden almacenar varios datos
 * pero ninguna de ellas tienen funciones propias para utilizar operaciones de 
 * inserción, borrado, actualización y ordenación. (Eso toca crearlas uno mismo
 * o implementando algun tipo de datos de una libreria estandar)
 * 
 * Nota: Todo esto es asi para usar solo lo que requiere el programa y poder 
 * tener una buena obtimizacion del codigo.
*/



int main() {
    // ****************************** Arreglos ****************************** //
    // Se define el tamaño entre [] y la lista de datos entre {}
    int array[3] = {1, 2, 3};

    // Tambien se puedde definir y luego colocar valores 1 por 1
    int array2[3];
    
    array2[0] = 1; // Los valores para llamar cada parte de la lista empiezan 
    array2[1] = 2; // con cero.
    array2[2] = 3;

    // Los arreglos son lista de la forma {1, 2, 3, ...}

    // *********************** Arreglos 2 Dimensiones *********************** //
    
    /* 
     * Similares al arreglo pero son de la forma:
     * {
     *      {1, 2, 3},
     *      {4, 5, 6},
     *      {7, 8, 9},
     * }
     * 
     * Practicamente un arreglo con arreglos adentro.
    */

    int array3[3][2] = {{1,2}, {3,4}, {5, 6}};
    // Se debe indicar tambien el tamaño de los arrglos del interior.


    // ******************************* String ******************************* //
    // El string es un arreglo que utiliza el tipo de dato char.
    
    char texto[11] = "Hola Mundo";
    
    // Normalmente se importa <string> y se utiliza std::string porque ofrece
    // automaticamente muchas facilidades que para un arreglo tipo char, 
    // no ofrece, pero tocaria importar de la biblioteca estandar.
    // Normalmente se utiliza mucho las bibliotecas estandar para cualquier cosa
    // en el codigo (Y muchas veces es lo recomendado).
    
    // ******************************* Struct ******************************* //
    // Se utiliza para agrupar varias variables de diferentes datos 
    // Relacionadas entre si.

    struct Persona {
        char nombre[50];
        int edad;
        float estatura;
    };

    int i = 0;
    struct Persona yo;

    // Como el string es array entonces toca asi, o importando la libreria
    // <cstring> y utilizando la siguiente linea  strcpy(yo.nombre, "Fravelz");

    for (char letter : "Fravelz") { 
        yo.nombre[i] = letter;
        i++;
    }

    yo.edad = 99;
    yo.estatura = 1.72;

    // ************************** Enum (Enumeraciones) ********************** //
    // Enumera las variables que posee, con numeros enteros, se puede utilizar
    // para retornar estados de una app o programa, etc.

    enum sistema {
        activo,   // El valor es: 0
        inactivo, // 1
        hackeado  // 2
    };

    cout << activo << '\n'; 

    // Se cambia los valores numericos poe defecto
    enum CodigoError {
        OK = 0,
        NotFound = 404,
        ServerError = 500
    };

    cout << NotFound << '\n';

    // Se Fuerza a utilizar un identificador para evitar confucciones en codigo.

    enum class ajedrez { // :v
        arfil = 3,
        caballo = 3,
        torre = 11092001, 
        dama = 9,
        peon = 1
    };

    // Para imprimir el numero toca asi porque son tipos fuertemente tipados.
    // static_cast<int> con esta linea. 

    cout << static_cast<int>(ajedrez::torre) << '\n';

    // ********************* Ejercicio Dificultad Extra ********************* //
    
    // cout <<  búsqueda, inserción, actualización y eliminación de contactos.

    // cout ;

    //* Bueno, con la funcion anterior aqui digito la informacion 
    //* para formatear la salida del texto.
    bool salir = false;
    char c = '*', opc;

    vector<Contactos> agenda;

    while (!salir){
        formatear(c, "", 0, false);
        formatear(c, "Agenda de contactos", 0, false);
        formatear(c, "", 0, false);
        
        formatear(c, "1. Buscar Contacto.", 1);
        formatear(c, "2. Agregar Contacto.", 1);
        formatear(c, "3. Actualizar Contacto.", 1);
        formatear(c, "4. Eliminar Contactos.", 1);
        formatear(c, "5. Salir.", 1);
        formatear(c, "", 0, false);
        
        cout << c << " # "; 
        cin >> opc;
        cin.ignore();

        string buscar, dato_opc, data_actualizar;
        bool correct = false;
        int buscado;

        switch(opc) {
            case '1': {
                string buscar;
                formatear(c, "Digite el nombre del contacto a buscar:", 1);
                cout << c << " > ";
                getline(cin, buscar);

                formatear(c, "", 0);
                int buscado = buscar_contacto(buscar, agenda);

                if (buscado != -1) {
                    formatear(c, "Nombre: " + agenda[buscado].nombre, 1);
                    formatear(c, "Celular: " + agenda[buscado].celular, 1);
                    formatear(c, "Correo: " + agenda[buscado].correo, 1);

                } else {
                    formatear(c, "El contacto que buscas NO Existe.", 0);
                };

                formatear(c, "", 0, false);
                break;
            }

            case '2': {
                Contactos contacto;
                cout << c << " > Digite el nombre: ";
                getline(cin, contacto.nombre);
                
                cout << c << " > Digite el celular: ";
                getline(cin, contacto.celular);
                
                cout << c << " > Digite el correo: ";
                getline(cin, contacto.correo);

                agenda.push_back(contacto);
                            
                formatear(c, "", 0);
                formatear(c, "Nuevo Contacto Creado :)", 0);
                formatear(c, "", 0, false);
                break;
            }

            case '3': 
                formatear(c, "D. el nombre del contacto a Actualizar:", 1);
                cout << c << " > ";
                getline(cin, buscar);

                formatear(c, "", 0);                
                buscado = buscar_contacto(buscar, agenda);

                if (buscado != -1) {
                    do {
                        formatear(c, "Cual dato quieres actualizar:", 1);
                        cout << c << " (nombre=0, celular=1, correo=2) > ";
                        getline(cin, dato_opc);
                        
                        if (dato_opc == "0") {
                            cout << c << " Que nuevo Nombre deseas: ";
                            getline(cin, data_actualizar);
                            agenda[buscado].nombre = data_actualizar;
                            correct = true;
                            
                        } else if (dato_opc == "1") {
                            cout << c << " Que nuevo # Celular deseas: ";
                            getline(cin, data_actualizar);
                            agenda[buscado].celular = data_actualizar;
                            correct = true;
                            
                        } else if (dato_opc == "2") {
                            cout << c << " Que nuevo Correo deseas: ";
                            getline(cin, data_actualizar);
                            agenda[buscado].correo = data_actualizar;
                            correct = true;
                            
                        } else {
                            formatear(c, "Error: Intentelo de nuevo.", 1);
                        }
                    } while (!correct);
    
                    formatear(c, "", 0);                
                    
                    formatear(c, "Nombre: " + agenda[buscado].nombre, 1);
                    formatear(c, "Celular: " + agenda[buscado].celular, 1);
                    formatear(c, "Correo: " + agenda[buscado].correo, 1);

                } else {
                    formatear(c, "El contacto que buscas NO Existe.", 0);
                };

                formatear(c, "", 0, false);
                break;

            case '4': {
                formatear(c, "D. el nombre del contacto a Eliminar:", 1);
                cout << c << " > ";
                getline(cin, buscar);

                formatear(c, "", 0);                
                buscado = buscar_contacto(buscar, agenda);

                if (buscado != -1) {    
                    formatear(c, "", 0);                
                    
                    formatear(c, "Nombre: " + agenda[buscado].nombre, 1);
                    formatear(c, "Celular: " + agenda[buscado].celular, 1);
                    formatear(c, "Correo: " + agenda[buscado].correo, 1);
                    
                    formatear(c, "", 0);                
                    formatear(c, "Contacto eliminado :(", 0);

                    agenda.erase(agenda.begin() + buscado);
                    formatear(c, "", 0, false);


                } else {
                    formatear(c, "El contacto NO Existe.", 0);
                };

                break;
            }
            
            case '5': 
                salir = true; break;

            default: {
                
                formatear(c, "", 0);
                formatear(c, "Nuevo Contacto Creado :)", 0);
                formatear(c, "", 0, false);
            }
        }
        cout << '\n';
    }

    formatear(c, "", 0, false);
    formatear(c, "Cordial Saludo!", 2);
    formatear(c, "", 0, false);
        
    
    return 0;
}

// **************** Funciones de Ejercicio Dificultad Extra  **************** //

// Funcion encargada del formateo del texto :)
// Hiba a utilizar la Libreria <iomanip> pero no me funciono.
void formatear ( 
    char caracter, string palabras, int orientacion, 
    bool vacio, int espacio
) {
    int longitud = palabras.length(); // abc = 3
    int izquierda = 0, derecha = 0;   // |*Izquierda + *Derecha|

    int relleno = espacio - longitud; // |***| - a(1) = |**| 
    if (palabras != "") relleno -= 2;            // |***a***| -2 = |** a **|

    if (orientacion == 0) { // * Orientacion Centrada
        izquierda = relleno / 2; 
        derecha = relleno - izquierda;
        
        for (int i = 0; i < izquierda; ++i) {
            if (vacio) {
                cout << ((i == 0) ? caracter : ' ');

            } else { cout << caracter; }
        }

        string espacio_1 = (palabras != "") ? " " : "";
        cout << espacio_1 << palabras << espacio_1;

        for (int i = 0; i < derecha; ++i) {
            if (vacio) {
                cout << ((i != derecha-1) ? ' ' : caracter);

            } else { cout << caracter; }
        };


    } else if (orientacion == 1) { // * Orientacion Izquierda
        izquierda = 0;
        derecha = relleno-1;

        for (int i = 0; i < izquierda; ++i) {
            if (vacio) {
                cout << ((i == 0) ? caracter : ' ');

            } else { cout << caracter; }
        }

        string espacio_1 = (palabras != "") ? " " : "";
        cout << caracter << espacio_1 << palabras << espacio_1;

        for (int i = 0; i < derecha; ++i) {
            if (vacio) {
                cout << ((i == derecha-1) ? caracter : ' ');

            } else { cout << caracter; }
        };


    } else if (orientacion == 2) { // * Orientacion Derecha
        izquierda = relleno-1;
        derecha = 0;

        for (int i = 0; i < izquierda; ++i) {
            if (vacio) {
                cout << ((i == 0) ? caracter : ' ');

            } else { cout << caracter; }
        };
        string espacio_1 = (palabras != "") ? " " : "";

        cout << espacio_1 << palabras << espacio_1 << caracter;
        for (int i = 0; i < derecha; ++i) {
            if (vacio) {
                cout << ((i == 0) ? caracter : ' ');

            } else { cout << caracter; }
        };
    }
    cout << '\n';
};

int buscar_contacto(string buscar, vector<Contactos> vect){
    for (int x = 0; x < vect.size(); x++) {
        if (buscar == vect[x].nombre) {
            return x;
        }
    }
    return -1;
}

// ****** Demostraccion de la Consola del Ejercicio Dificultad Extra  ****** //

/*
 TODO: Se puede obtimizar el codigo pero uf, es mucho, mejor voy a continuar 
 Todo: mejor....

 TODO: Muestra por Consola del programa:

********************************************
*********** Agenda de contactos ************
********************************************
* 1. Buscar Contacto.                      *
* 2. Agregar Contacto.                     *
* 3. Actualizar Contacto.                  *
* 4. Eliminar Contactos.                   *
* 5. Salir.                                *
********************************************
* # 2
* > Digite el nombre: Xi
* > Digite el celular: 123 456 78 90
* > Digite el correo: correo@hotmail.com
*                                          *
*         Nuevo Contacto Creado :)         *
********************************************

********************************************
*********** Agenda de contactos ************
********************************************
* 1. Buscar Contacto.                      *
* 2. Agregar Contacto.                     *
* 3. Actualizar Contacto.                  *
* 4. Eliminar Contactos.                   *
* 5. Salir.                                *
********************************************
* # 1
* > Xi
*                                          *
* Nombre: Xi                               *
* Celular: 123 456 78 90                   *
* Correo: correo@hotmail.com               *
********************************************

********************************************
*********** Agenda de contactos ************
********************************************
* 1. Buscar Contacto.                      *
* 2. Agregar Contacto.                     *
* 3. Actualizar Contacto.                  *
* 4. Eliminar Contactos.                   *
* 5. Salir.                                *
********************************************
* # 3
* D. el nombre del contacto a Actualizar:  *
* > Xi
*                                          *
* Cual dato quieres actualizar:            *
* (nombre=0, celular=1, correo=2) > 0
* Que nuevo Nombre deseas: FV
*                                          *
* Nombre: FV                               *
* Celular: 123 456 78 90                   *
* Correo: correo@hotmail.com               *
********************************************

********************************************
*********** Agenda de contactos ************
********************************************
* 1. Buscar Contacto.                      *
* 2. Agregar Contacto.                     *
* 3. Actualizar Contacto.                  *
* 4. Eliminar Contactos.                   *
* 5. Salir.                                *
********************************************
* # 4
* D. el nombre del contacto a Eliminar:    *
* > FV
*                                          *
*                                          *
* Nombre: FV                               *
* Celular: 123 456 78 90                   *
* Correo: correo@hotmail.com               *
*                                          *
*          Contacto eliminado :(           *
********************************************

********************************************
*********** Agenda de contactos ************
********************************************
* 1. Buscar Contacto.                      *
* 2. Agregar Contacto.                     *
* 3. Actualizar Contacto.                  *
* 4. Eliminar Contactos.                   *
* 5. Salir.                                *
********************************************

********************************************
*********** Agenda de contactos ************
********************************************
* 1. Buscar Contacto.                      *
* 2. Agregar Contacto.                     *
* 3. Actualizar Contacto.                  *
* 4. Eliminar Contactos.                   *
* 5. Salir.                                *
********************************************
* # 1
* Digite el nombre del contacto a buscar:  *
* > FV
*                                          *
*    El contacto que buscas NO Existe.     *
********************************************

********************************************
*********** Agenda de contactos ************
********************************************
* 1. Buscar Contacto.                      *
* 2. Agregar Contacto.                     *
* 3. Actualizar Contacto.                  *
* 4. Eliminar Contactos.                   *
* 5. Salir.                                *
********************************************
* # 5

********************************************
*                          Cordial Saludo! *
********************************************


? NOTA: Los datos recibidos no son verificados por el programa, es
? decir si escribes un numero de celular de solo letras lo aceptara,
? y el programa se puede obtimizar, algun dia lo hare :)
*/
