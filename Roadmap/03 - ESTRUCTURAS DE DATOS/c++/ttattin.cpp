#include <algorithm>
#include <iostream>
#include <limits>
#include <string>
#include <vector>

struct Contacto {
    std::string nombre;
    int telefono;
};

bool ejercicio_dificultad_extra();
void leer_entero(int &valor);
void mostrar_menu();
void anadir_contacto(std::vector<Contacto> &contactos);
void buscar_contacto(const std::vector<Contacto> &contactos);
void cambiar_numero_de_telefono(std::vector<Contacto> &contactos);
void eliminar_contacto(std::vector<Contacto> &contactos);

int main() {
    // STRING
    std::string s = "Hola";
    std::cout << "La variable std::string gestiona una secuencia de caracteres y permite acceder a ellos por índice, como en un array." << std::endl;
    std::cout << "Ejemplo de una variable string: " << s << std::endl << std::endl;

    // VECTOR
    std::vector<int> v = {6, 2, 4, 1, 5};
    std::cout << "En C++ los vectores son una secuencia dinámica de elementos contiguos, con acceso por índice como un array, pero puede cambiar de tamaño." << std::endl;
    std::cout << "Ejemplo de un vector de enteros: (el primer elemento tiene indice 0): " << std::endl;
    std::cout << "Se muestra la posicion y el valor del vector en esa posicion. El vector es {6, 2, 4, 1, 5}" << std::endl;
    for (size_t i = 0; i < v.size(); i++) {
        std::cout << "posicion " << i << ": " << v[i] << std::endl;
    }
    std::cout << "Los vectores pueden ser modificados en cualquier momento, incluido el numero de elementos." << std::endl;
    std::cout << "Ejemplo de eliminacion del ultimo elemento del vector: " << std::endl;
    v.pop_back();
    for (size_t i = 0; i < v.size(); i++) {
        std::cout << "posicion " << i << ": " << v[i] << std::endl;
    }
    std::cout << "Ejemplo de cambio de un valor del vector: " << std::endl;
    v[2] = 10;
    for (size_t i = 0; i < v.size(); i++) {
        std::cout << "posicion " << i << ": " << v[i] << std::endl;
    }
    std::cout << "Ejemplo de insercion de un valor al principio del vector: " << std::endl;
    v.insert(v.begin(), 10);
    for (size_t i = 0; i < v.size(); i++) {
        std::cout << "posicion " << i << ": " << v[i] << std::endl;
    }
    std::cout << "Ejemplo de ordenacion de un vector: " << std::endl;
    std::sort(v.begin(), v.end());
    for (size_t i = 0; i < v.size(); i++) {
        std::cout << "posicion " << i << ": " << v[i] << std::endl;
    }
    std::cout << std::endl;

    // ARRAYS
    int matriz[3][3] = {{1, 0, 0}, {0, 1, 0}, {0, 0, 1}};
    std::cout << "En C++ los arrays pueden tener mas de una dimension y son de tamaño fijo." << std::endl;
    std::cout << "Ejemplo de un array mostrando una matriz identidad de 3 x 3: " << std::endl;
    for (size_t i = 0; i < sizeof(matriz) / sizeof(matriz[0]); i++) {
        for (size_t j = 0; j < sizeof(matriz[0]) / sizeof(matriz[0][0]); j++) {
            std::cout << matriz[i][j] << " ";
        }
        std::cout << std::endl;
    }
    std::cout << "En un array se pueden cambiar los valores de los elementos" << std::endl;
    matriz[0][0] = 10;
    matriz[1][1] = 20;
    matriz[2][2] = 30;
    std::cout << "El array mostrando una matriz identidad de 3 x 3 con valores cambiados: " << std::endl;
    for (size_t i = 0; i < sizeof(matriz) / sizeof(matriz[0]); i++) {
        for (size_t j = 0; j < sizeof(matriz[0]) / sizeof(matriz[0][0]); j++) {
            std::cout << matriz[i][j] << " ";
        }
        std::cout << std::endl;
    }
    std::cout << std::endl;

    // ESTRUCTURAS DE DATOS
    struct Persona {
        std::string nombre;
        int edad;
        bool es_cliente;
    };

    Persona persona;
    persona.nombre = "Juan";
    persona.edad = 25;
    persona.es_cliente = true;
    std::cout << "Estructura de datos: " << std::endl;
    std::cout << "Una estructura de datos es una clase con variables publicas por defecto." << std::endl;
    std::cout << "En una estructura de datos se puede acceder a las variables para leerlas o modificarlas directamente." << std::endl;
    std::cout << "Ejemplo de una estructura de datos: " << std::endl;
    std::cout << "Nombre: " << persona.nombre << std::endl;
    std::cout << "Edad: " << persona.edad << std::endl;
    std::cout << "Es cliente: " << persona.es_cliente << std::endl;
    persona.nombre = "Luisa";
    persona.edad = 30;
    std::cout << "Nombre modificado: " << persona.nombre << std::endl;
    std::cout << "Edad modificada: " << persona.edad << std::endl;
    std::cout << std::endl;

    std::cout << "--------------------------------------------------------------------------------" << std::endl;
    std::cout << "------------------------------- DIFICULTAD EXTRA -------------------------------" << std::endl;
    std::cout << "--------------------------------------------------------------------------------" << std::endl;

    // DIFICULTAD EXTRA
    // Los numeros de telefono tendran nueve digitos.

    return ejercicio_dificultad_extra();
}

bool ejercicio_dificultad_extra() {
    std::vector<Contacto> contactos;

    while (true) {
        int opcion = 0;
        mostrar_menu();
        leer_entero(opcion);
        switch (opcion) {
            case 1:
                anadir_contacto(contactos);
                break;
            case 2:
                buscar_contacto(contactos);
                break;
            case 3:
                cambiar_numero_de_telefono(contactos);
                break;
            case 4:
                eliminar_contacto(contactos);
                break;
            case 5:
                return 0;
            default:
                std::cout << "Opcion no valida" << std::endl;
                break;
        }
    }
}

void leer_entero(int &valor) {
    int valor_temp = 0;
    while (true) {
        std::cin >> valor_temp;
        if (std::cin.fail()) {
            std::cin.clear();
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
            std::cout << "El valor introducido no es correcto. Introducelo de nuevo: ";
            continue;
        }
        valor = valor_temp;
        return;
    }
}

void mostrar_menu() {
    std::cout << "\n\nMenu principal:" << std::endl;
    std::cout << "1. Agregar contacto" << std::endl;
    std::cout << "2. Buscar contacto" << std::endl;
    std::cout << "3. Cambiar Num. de Telefono" << std::endl;
    std::cout << "4. Eliminar contacto" << std::endl;
    std::cout << "5. Salir" << std::endl;
    std::cout << "Opcion: ";
}

void anadir_contacto(std::vector<Contacto> &contactos) {
    Contacto contacto;
    std::cout << "Nombre: ";
    std::cin >> contacto.nombre;
    int telefono = 0;
    while (telefono < 100000000 || telefono > 999999999) {
        std::cout << "Numero de telefono (9 digitos): ";
        leer_entero(telefono);
    }
    contacto.telefono = telefono;
    contactos.push_back(contacto);
    std::cout << "Contacto agregado correctamente" << std::endl;
}

void buscar_contacto(const std::vector<Contacto> &contactos) {
    if (contactos.size() == 0) {
        std::cout << "No hay contactos" << std::endl;
        return;
    }
    std::cout << "Introduzca el nombre del contacto: ";
    std::string nombre;
    std::cin >> nombre;
    for (size_t i = 0; i < contactos.size(); i++) {
        if (contactos[i].nombre == nombre) {
            std::cout << "Contacto encontrado" << std::endl;
            std::cout << "Nombre: " << contactos[i].nombre << std::endl;
            std::cout << "Numero de telefono: " << contactos[i].telefono << std::endl;
            return;
        }
    }
    std::cout << "No se encontro el contacto" << std::endl;
}

void cambiar_numero_de_telefono(std::vector<Contacto> &contactos) {
    if (contactos.size() == 0) {
        std::cout << "No hay contactos" << std::endl;
        return;
    }
    std::cout << "Introduzca el nombre del contacto: ";
    std::string nombre;
    std::cin >> nombre;
    for (size_t i = 0; i < contactos.size(); i++) {
        if (contactos[i].nombre == nombre) {
            int nuevo_numero = 0;
            while (nuevo_numero < 100000000 || nuevo_numero > 999999999) {
                std::cout << "Numero de telefono (9 digitos): ";
                leer_entero(nuevo_numero);
            }
            contactos[i].telefono = nuevo_numero;
            std::cout << "Numero de telefono modificado" << std::endl;
            return;
        }
    }
    std::cout << "No se encontro el contacto" << std::endl;
}

void eliminar_contacto(std::vector<Contacto> &contactos) {
    if (contactos.size() == 0) {
        std::cout << "No hay contactos" << std::endl;
        return;
    }
    std::cout << "Introduzca el nombre del contacto a eliminar: ";
    std::string nombre;
    std::cin >> nombre;
    for (size_t i = 0; i < contactos.size(); i++) {
        if (contactos[i].nombre == nombre) {
            contactos.erase(contactos.begin() + i);
            std::cout << "Contacto eliminado" << std::endl;
            return;
        }
    }
    std::cout << "No se encontro el contacto" << std::endl;
}

