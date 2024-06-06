#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <cstdlib>

/*
* IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.
* 
* EJERCICIO:
* Desarrolla un programa capaz de crear un archivo que se llame como
* tu usuario de GitHub y tenga la extensión .txt.
* Añade varias líneas en ese fichero:
* - Tu nombre.
* - Edad.
* - Lenguaje de programación favorito.
* Imprime el contenido.
* Borra el fichero.
*
* DIFICULTAD EXTRA (opcional):
* Desarrolla un programa de gestión de ventas que almacena sus datos en un 
* archivo .txt.
* - Cada producto se guarda en una línea del arhivo de la siguiente manera:
*   [nombre_producto], [cantidad_vendida], [precio].
* - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
*   actualizar, eliminar productos y salir.
* - También debe poseer opciones para calcular la venta total y por producto.
* - La opción salir borra el .txt.
*/


// Const zone
const std::string nameFile = "./hectorio23.txt";
const std::string language = "Python/C++";
const std::string name = "Héctor Adán";
const int age = 19;


// Definiciones de funciones
void actualizarProducto(const std::string& nombre, int cantidad, float precio, std::ifstream& archivo, std::ofstream& temporal);
void agregarProducto(std::ofstream& archivo, const std::string& nombre, int cantidad, float precio);
void eliminarProducto(const std::string& nombre, std::ifstream& archivo, std::ofstream& temporal);
float calcularVentaPorProducto(const std::string& nombre, std::ifstream& archivo);
float calcularVentaTotal(std::ifstream& archivo);
void consultarProductos(std::ifstream& archivo);
void printFileValues();
void writeFile();
void salir();

int main() {
    // Antes de todo, hay que crear el archivo con los 
    // datos requeridos para la resolucion del ejercicio.  
    std::cout << "\n EjERCICIO \n"; 
    std::cout << "Creado el archivo hectorio23.txt e insertando datos\n";
    writeFile();

    // Ahora imprimimos los valores del Archivi .txt
    std::cout << "Imprimiendo los valores contenidos en el archivo hectorio23.txt\n";
    printFileValues();

    std::cout << "\n EjERCICIO EXTRA \n"; 

    std::ifstream archivoEntrada("ventas.txt");
    std::ofstream archivoSalida("temporal.txt", std::ios::app);

    int opcion;
    std::string nombreProducto;
    int cantidad;
    float precio;

    std::cout << "===== Gestión de Ventas =====" << std::endl;
    std::cout << "1. Añadir producto" << std::endl;
    std::cout << "2. Consultar productos" << std::endl;
    std::cout << "3. Actualizar producto" << std::endl;
    std::cout << "4. Eliminar producto" << std::endl;
    std::cout << "5. Calcular venta total" << std::endl;
    std::cout << "6. Calcular venta por producto" << std::endl;
    std::cout << "7. Salir" << std::endl;
    std::cout << "Seleccione una opción: ";
    std::cin >> opcion;

    switch(opcion) {
        case 1:
            std::cout << "Nombre del producto: ";
            std::cin >> nombreProducto;
            std::cout << "Cantidad vendida: ";
            std::cin >> cantidad;
            std::cout << "Precio: ";
            std::cin >> precio;
            agregarProducto(archivoSalida, nombreProducto, cantidad, precio);
            break;
        case 2:
            consultarProductos(archivoEntrada);
            break;
        case 3:
            std::cout << "Nombre del producto a actualizar: ";
            std::cin >> nombreProducto;
            std::cout << "Nueva cantidad vendida: ";
            std::cin >> cantidad;
            std::cout << "Nuevo precio: ";
            std::cin >> precio;
            actualizarProducto(nombreProducto, cantidad, precio, archivoEntrada, archivoSalida);
            break;
        case 4:
            std::cout << "Nombre del producto a eliminar: ";
            std::cin >> nombreProducto;
            eliminarProducto(nombreProducto, archivoEntrada, archivoSalida);
            break;
        case 5:
            std::cout << "Venta total: $" << calcularVentaTotal(archivoEntrada) << std::endl;
            break;
        case 6:
            std::cout << "Nombre del producto para calcular venta: ";
            std::cin >> nombreProducto;
            std::cout << "Venta de " << nombreProducto << ": $" << calcularVentaPorProducto(nombreProducto, archivoEntrada) << std::endl;
            break;
        case 7:
            salir();
            break;
        default:
            std::cerr << "Opción no válida" << std::endl;
            break;
    }

    archivoEntrada.close();
    archivoSalida.close();
    std::remove("ventas.txt");
    std::rename("temporal.txt", "ventas.txt");

    return EXIT_SUCCESS;
}

// Funcion qur imprime los valores en pantalla
void printFileValues() {
    // Se crea un objeto de tipo fstream el cual nos permitirá
    // acceder a algunos metodos útiles para el manejo de archivos
    //, es decir, Input Output en Archivos I/O
    std::fstream myFile;

    // Abre el archivo en modo lectura 
    myFile.open(nameFile, std::ios::in); 
    if (myFile.is_open()) {
        std::string lines;
        // Imprime todo el contenido del archivo por lineas
        // de caracteres hasta que no haya más que imprimir 
        while (std::getline(myFile, lines)) {
            std::cout << lines << "\n";
        }
        myFile.close();
    }
}

void writeFile() {
    // Se crea un objeto de tipo fstream el cual nos permitirá
    // acceder a algunos metodos útiles para el manejo de archivos
    //, es decir, Input Output en Archivos I/O
    std::fstream myFile;
    // LA siguiente instruccion abre un archivo en modo de escritura 
    // Por defecto, en caso de no existir el archivo en la direccion
    // dada por el programador, el archivo se crea de manera implicita 
    myFile.open(nameFile, std::ios::out);  

    // Las siguientes instrucciones son para escribir el archivo
    myFile << "Nombre: " << name << "\n";
    myFile << "Lenjuages favoritos: " << language << "\n";
    myFile << "Edad: " << age;

    // Se cierra el archivo
    myFile.close();
}

// Funciones definidas
void agregarProducto(std::ofstream& archivo, const std::string& nombre, int cantidad, float precio) {
    archivo << nombre << ", " << cantidad << ", " << precio << std::endl;
}

void consultarProductos(std::ifstream& archivo) {
    std::string linea;
    while (std::getline(archivo, linea)) {
        std::cout << linea << std::endl;
    }
}

void actualizarProducto(const std::string& nombre, int cantidad, float precio, std::ifstream& archivo, std::ofstream& temporal) {
    std::string linea;
    while (std::getline(archivo, linea)) {
        std::stringstream ss(linea);
        std::string nombreProducto;
        std::getline(ss, nombreProducto, ',');
        if (nombreProducto == nombre) {
            temporal << nombre << ", " << cantidad << ", " << precio << std::endl;
        } else {
            temporal << linea << std::endl;
        }
    }
}

void eliminarProducto(const std::string& nombre, std::ifstream& archivo, std::ofstream& temporal) {
    std::string linea;
    while (std::getline(archivo, linea)) {
        std::stringstream ss(linea);
        std::string nombreProducto;
        std::getline(ss, nombreProducto, ',');
        if (nombreProducto != nombre) {
            temporal << linea << std::endl;
        }
    }
}

float calcularVentaTotal(std::ifstream& archivo) {
    float total = 0;
    std::string linea;
    while (std::getline(archivo, linea)) {
        std::stringstream ss(linea);
        std::string cantidadStr, precioStr;
        std::getline(ss, cantidadStr, ',');
        std::getline(ss, precioStr, ',');
        int cantidad = std::stoi(cantidadStr);
        float precio = std::stof(precioStr);
        total += cantidad * precio;
    }
    return total;
}

float calcularVentaPorProducto(const std::string& nombre, std::ifstream& archivo) {
    float venta = 0;
    std::string linea;
    while (std::getline(archivo, linea)) {
        std::stringstream ss(linea);
        std::string nombreProducto, cantidadStr, precioStr;
        std::getline(ss, nombreProducto, ',');
        if (nombreProducto == nombre) {
            std::getline(ss, cantidadStr, ',');
            std::getline(ss, precioStr, ',');
            int cantidad = std::stoi(cantidadStr);
            float precio = std::stof(precioStr);
            venta = cantidad * precio;
            break;
        }
    }
    return venta;
}

void salir() {
    std::remove("ventas.txt");
    std::cout << "Archivo borrado. Saliendo del programa..." << std::endl;
    exit(0);
}
