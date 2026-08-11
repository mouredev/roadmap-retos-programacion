#include <iostream>
#include <vector>
#include <list>
#include <map>
#include <algorithm>

// Estructura ejercicio Extra
struct Agenda {
    std::vector<int> id;
    std::vector<std::string> nombre;
    std::vector<std::string> telefono;
};

int main() {
    
    // C++ permite utilizar estructuras de datos como arrays, vectores, listas y mapas

    // ARRAYS
    // Los arrays son estructuras de datos estaticas, es decir, su tamaño debe ser conocido en tiempo de compilación y no puede 
    // cambiar durante la ejecución del programa. Existen arrays unidimensionales y multidimensionales. Los arrays unidimensionales 
    // permiten almacenar elementos de un mismo tipo en una sola dimensión, mientras que los arrays multidimensionales permiten 
    // almacenar elementos en varias dimensiones, como matrices o grillas.

    int numeros[5] = {1, 2, 3, 4, 5}; // array unidimensional de enteros
    double matriz[2][3] = {{1.1, 2.2, 3.3}, {4.4, 5.5, 6.6}}; // array bidimensional de doubles
    double tensor[2][2][2] = {{{1.1, 2.2}, {3.3, 4.4}}, {{5.5, 6.6}, {7.7, 8.8}}}; // array tridimensional de doubles
    char caracteres[2][5] = {{'a', 'b', 'c', 'd', 'e'}, {'f', 'g', 'h', 'i', 'j'}}; // array bidimensional de caracteres

    tensor[1][0][1] = 9.9; // cambia el valor del tensor en la posición [1][0][1] a 9.9
    caracteres[0][2] = 'z'; // cambia el valor del array de caracteres en la posición [0][2] a 'z'

    // VECTORES
    // Los vectores son estructuras de datos dinámicas que permiten almacenar elementos de un mismo tipo en una secuencia. 
    // A diferencia de los arrays, los vectores pueden crecer o reducir su tamaño según sea necesario durante la ejecución del 
    // programa. Los vectores proporcionan métodos para agregar, eliminar y acceder a elementos de manera eficiente.

    std::vector<int> numerosVector1; // vector de enteros
    std::vector<double> numerosVector2; // vector de doubles
    std::vector<int> numerosVector3 = {1, 2, 3, 4, 5}; // vector de enteros
    std::vector<std::vector<double>> matrizVector = {{1.1, 2.2, 3.3}, {4.4, 5.5, 6.6}}; // vector bidimensional de doubles
    std::vector<std::vector<double>> matriz2D(3, std::vector<double>(4)); // vector bidimensional de doubles con 3 filas y 
    //4 columnas
    std::vector<std::vector<std::vector<double>>> tensorVector = {{{1.1, 2.2}, {3.3, 4.4}}, {{5.5, 6.6}, {7.7, 8.8}}}; // vector 
    // tridimensional de doubles
    std::vector<std::vector<std::vector<double>>> matriz3D(2, std::vector<std::vector<double>>(3, std::vector<double>(4))); 
    // vector tridimensional de doubles con 2 capas, 3 filas y 4 columnas

    numerosVector3[2] = 10; // cambia el valor del vector en la posición [2] a 10
    matrizVector[1][2] = 7.7; // cambia el valor del vector bidimensional en la posición [1][2] a 7.7
    tensorVector[1][0][1] = 9.9; // cambia el valor del vector tridimensional en la posición [1][0][1] a 9.9
    numerosVector1.push_back(6); // agrega el valor 6 al final del vector (inserción al final)
    numerosVector1.emplace_back(8); // agrega el valor 8 al inicio del vector (inserción al inicio)
    numerosVector1.insert(numerosVector1.begin() + 2, 7); // inserta el valor 7 en la posición [2] del vector (inserción en medio)
    numerosVector1.erase(numerosVector1.begin() + 1); // elimina el valor en la posición [1] del vector (eliminación en medio)
    
    // LISTAS
    // Las listas son estructuras de datos dinámicas que permiten almacenar elementos de un mismo tipo en una secuencia. 
    // A diferencia de los arrays y vectores, las listas permiten insertar y eliminar elementos en cualquier posición de 
    // la secuencia de manera eficiente. Las listas pueden ser simples o dobles, dependiendo de si cada elemento tiene un 
    // puntero al siguiente elemento o también al anterior.

    std::list<int> numerosLista1; // lista de enteros
    std::list<double> numerosLista2; // lista de doubles
    std::list<int> numerosLista3 = {1, 2, 3, 4, 5}; // lista de enteros
    std::list<std::list<double>> matrizLista = {{1.1, 2.2, 3.3}, {4.4, 5.5, 6.6}}; // lista bidimensional de doubles

    numerosLista3.push_back(6); // agrega el valor 6 al final de la lista (inserción al final)
    numerosLista3.push_front(0); // agrega el valor 0 al inicio de la lista (inserción al inicio)
    numerosLista3.insert(std::next(numerosLista3.begin(), 2), 7); // inserta el valor 7 en la posición [2] de la lista 
    // (inserción en medio)
    numerosLista3.erase(std::next(numerosLista3.begin(), 1)); // elimina el valor en la posición [1] de la lista (eliminación en medio)
    numerosLista3.pop_back(); // elimina el último elemento de la lista (eliminación al final)
    numerosLista3.pop_front(); // elimina el primer elemento de la lista (eliminación al inicio)

    // MAPAS
    // Los mapas son estructuras de datos que permiten almacenar pares de clave-valor, donde cada clave es única y se utiliza
    // para acceder a su valor correspondiente. Los mapas proporcionan métodos para agregar, eliminar y buscar elementos
    // de manera eficiente. Los mapas pueden ser implementados utilizando tablas hash o árboles binarios de búsqueda, 
    // dependiendo de la complejidad de las operaciones que se deseen realizar. 

    std::map<std::string, double> viscosidades = {{"Agua", 0.000001}, {"Aceite", 0.1}, {"Glicerina", 1.5}}; // mapa de viscosidades 
    // con clave de tipo string y valor de tipo double    
    std::map<std::string, int> edades; // mapa de edades con clave de tipo string y valor de tipo int
    edades["Alice"] = 25; // agrega un par de clave-valor al mapa
    edades["Bob"] = 30; // agrega un par de clave-valor al mapa
    edades["Charlie"] = 35; // agrega un par de clave-valor al mapa

    viscosidades["Agua"] = 0.000002; // cambia el valor del mapa en la clave "Agua" a 0.000002
    viscosidades.insert({"Etanol", 0.001}); // agrega un par de clave-valor al mapa
    viscosidades.erase("Aceite"); // elimina el par de clave-valor con clave "Aceite" del mapa

    // DIFICULTAD EXTRA

    struct Agenda Mi_agenda; // crea una instancia de la estructura Agenda
    bool salir = false; // variable para controlar el bucle principal
    int opcion; // variable para almacenar la opción seleccionada
    std::string nombre_temp; // variable temporal para almacenar el nombre del contacto
    std::string telefono_temp; // variable temporal para almacenar el teléfono del contacto

    do {
        std::cout << "***********************************************************" << std::endl;
        std::cout << "                       MENU PRINCIPAL" << std::endl;
        std::cout << "***********************************************************" << std::endl;
        std::cout << "***********************************************************" << std::endl;        
        std::cout << "         Bienvenido a tu agenda de contactos personal" << std::endl;
        std::cout << "***********************************************************" << std::endl;
        std::cout << "" << std::endl;
        std::cout << "Seleccione una opcion:" << std::endl;
        std::cout << "" << std::endl;
        std::cout << "1. Agregar contacto" << std::endl;
        std::cout << "2. Eliminar contacto" << std::endl;
        std::cout << "3. Buscar contacto" << std::endl;
        std::cout << "4. Actualizar contacto" << std::endl;
        std::cout << "5. Mostrar contactos" << std::endl;
        std::cout << "6. Salir" << std::endl;
        std::cin >> opcion;

        switch (opcion) {
            case 1: {
                // Lógica para agregar contacto
                std::cout << "Para agregar un contacto, ingrese el nombre:" << std::endl;
                std::cin >> nombre_temp;
                for (const auto& nombre : Mi_agenda.nombre) { // verifica si el nombre ya existe en la agenda
                    if (nombre == nombre_temp) {
                        std::cout << "El contacto ya existe en la agenda. Si desea actualizarlo, seleccione la opcion 4" << std::endl;
                        break;
                    }
                }
                Mi_agenda.nombre.emplace_back(nombre_temp); // agrega el nombre del contacto al vector de nombres
                fflush(stdin); // limpia el buffer de entrada para evitar problemas con la lectura de datos
                std::cout << "Ingrese el telefono:" << std::endl;
                std::cin >> telefono_temp;
                for (const auto& telefono : Mi_agenda.telefono) { // verifica si el teléfono ya existe en la agenda
                    if (telefono == telefono_temp) {
                        std::cout << "El telefono ya existe en la agenda. Si desea actualizarlo, seleccione la opcion 4" << std::endl;
                        break;
                    }
                }
                Mi_agenda.telefono.emplace_back(telefono_temp); // agrega el teléfono del contacto al vector de teléfonos
                std::cout << "Contacto agregado con exito." << std::endl;
                Mi_agenda.id.emplace_back(Mi_agenda.id.size() + 1); // asigna un ID único al contacto
                fflush(stdin); // limpia el buffer de entrada para evitar problemas con la lectura de datos
                break;
            }

            case 2: {
                // Lógica para eliminar contacto
                std::cout << "Ingrese el nombre del contacto que desea eliminar:" << std::endl;
                std::cin >> nombre_temp;
                auto it = std::find(Mi_agenda.nombre.begin(), Mi_agenda.nombre.end(), nombre_temp); // busca el nombre en el vector de nombres
                if (it != Mi_agenda.nombre.end()) { // si el nombre se encuentra en el vector
                    int index = std::distance(Mi_agenda.nombre.begin(), it); // obtiene el índice del contacto a eliminar
                    Mi_agenda.nombre.erase(it); // elimina el nombre del contacto del vector de nombres
                    Mi_agenda.telefono.erase(Mi_agenda.telefono.begin() + index); // elimina el teléfono del contacto del vector de teléfonos
                    Mi_agenda.id.erase(Mi_agenda.id.begin() + index); // elimina el ID del contacto del vector de IDs
                    std::cout << "Contacto eliminado con exito." << std::endl;
                } else {
                    std::cout << "El contacto no existe en la agenda." << std::endl;
                }
                break;
            }

            case 3:{
                // Lógica para buscar contacto
                std::cout << "Ingrese el nombre del contacto que desea buscar:" << std::endl;
                std::cin >> nombre_temp;
                auto it_search = std::find(Mi_agenda.nombre.begin(), Mi_agenda.nombre.end(), nombre_temp); // busca el nombre en el vector de nombres
                if (it_search != Mi_agenda.nombre.end()) {
                    int index = std::distance(Mi_agenda.nombre.begin(), it_search);
                    std::cout << "Contacto encontrado:" << std::endl;
                    std::cout << "ID    NOMBRE    TELEFONO" << std::endl;
                    std::cout << Mi_agenda.id[index] << "    " << Mi_agenda.nombre[index] << "    " << Mi_agenda.telefono[index] << std::endl;
                } else {
                    std::cout << "El contacto no existe en la agenda." << std::endl;
                }
        
                break;
            }
            case 4:{
                // Lógica para actualizar contacto
                std::cout << "Ingrese el nombre del contacto que desea actualizar:" << std::endl;
                std::cin >> nombre_temp;
                auto it_search2 = std::find(Mi_agenda.nombre.begin(), Mi_agenda.nombre.end(), nombre_temp); // busca el nombre en el vector de nombres
                if (it_search2 != Mi_agenda.nombre.end()) {
                    int index = std::distance(Mi_agenda.nombre.begin(), it_search2);
                    std::cout << "Ingrese el nuevo telefono:" << std::endl;
                    std::cin >> Mi_agenda.telefono[index]; // actualiza el teléfono del contacto en el vector de teléfono
                    std::cout << "Contacto actualizado con exito." << std::endl;
                } else {
                    std::cout << "El contacto no existe en la agenda." << std::endl;
                }
                
                break;
            }
            case 5:{
                // Lógica para mostrar contactos
                std::cout << "ID    NOMBRE    TELEFONO" << std::endl;
                for (int i = 0; i < Mi_agenda.nombre.size(); ++i) {
                    std::cout << Mi_agenda.id[i] << "    " << Mi_agenda.nombre[i] << "    " << Mi_agenda.telefono[i] << std::endl;
                }
                
                break;
            }
            case 6: {
                salir = true; // cambia la variable salir a true para salir del bucle
                
                break;
            }
            default:{
                std::cout << "Opcion invalida. Por favor, seleccione una opcion valida." << std::endl;
            }
        }
        fflush(stdin); // limpia el buffer de entrada para evitar problemas con la lectura de datos
    }
    while (salir == false); // bucle principal que se ejecuta mientras salir sea falso

    
}