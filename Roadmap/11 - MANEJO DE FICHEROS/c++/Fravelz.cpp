#include <iostream>
#include <vector>
#include <string>

#include <fstream>
#include <cstdio>

using namespace std;

struct Producto {
    string name;
    string amount;
    string price;
};

// Solo guarda informacion, al finalizar el programa se borra el archivo..
class Productos { 
private:
    vector<Producto> productos; 
    fstream archivo;
    
    bool indice_valido(unsigned int i) {
        if (!(i < productos.size())) {
            cout << " [-] Numero de producto invalido.";
            return false;
        }
        return true;
    }

    void leer_archivo(string name, string amount, string price, string msg="") {
        ofstream archivo("fravelz_products.txt", ios::app);

        if (archivo.is_open()) {
            archivo << "\n > " << msg << " ({" << name << ", " << amount << ", " << price << "})";

        } else {
            cout << "\n [!] Error al escribir en el archivo.";
        }
    }

public:
    Productos(string name = "", string amount = "", string price = "") {
          archivo.open("fravelz_products.txt", ios::out | ios::app); 

        if (!archivo.is_open()) {
        cout << "\nError: no se pudo abrir el archivo fravelz_products.txt\n";
    }
        if (name != "" && amount != "" && price != "") {
            agregar(name, amount, price);
        }
    }

    ~Productos() {
        archivo.close();
        remove("fravelz_products.txt");
    }


    void agregar(string name, string amount, string price) {
        productos.push_back({name, amount, price});
        leer_archivo(name, amount, price, ("Producto Nuevo: "));
    };

    void consultar(unsigned int numero_producto = 0) {
        if (!indice_valido(numero_producto)) return;

        cout << "\n > Nombre:   " << productos[numero_producto].name;
        cout << "\n > Cantidad: " << productos[numero_producto].amount;
        cout << "\n > Precio:   " << productos[numero_producto].price;

    };

    void actualizar(
        unsigned int numero_producto, 
        string name = "", string amount = "", string price = ""
    ) {
        if (!indice_valido(numero_producto)) return;

        if (!name.empty())   productos[numero_producto].name = name;
        if (!amount.empty()) productos[numero_producto].amount = amount;
        if (!price.empty())   productos[numero_producto].price = price;

        leer_archivo(
            productos[numero_producto].name,
            productos[numero_producto].amount,
            productos[numero_producto].price,
            "Producto Actualizado: "
        );
    };

    void eliminar(unsigned int numero_producto) {
        if (!indice_valido(numero_producto)) return;

        leer_archivo(
            productos[numero_producto].name, 
            productos[numero_producto].amount,
            productos[numero_producto].price,
            "[!] Producto Eliminado: "
        );

        productos.erase(productos.begin() + numero_producto);
    };
};


int main() {
    fstream archivo("Fravelz.txt", ios::out);

    string contenido = "Nombre: Francisco Velez\nEdad: NULL \n";
    contenido += "Lenguaje favorito: C++";

    cout << contenido;
    archivo << contenido;

    archivo.close();

    cout << "\n\n > Enter para borrar archivo: "; cin.ignore();
    remove("Fravelz.txt");

    // *************** Ejercicio DIFICULTAD EXTRA *************** //

    string data; Productos productos("", "");
    
    while (data != "5") {
        cout << "\n===============================================";
        cout << "\nGestion del Almacen: ";
        cout << "\n\t1. Agregar.";
        cout << "\n\t2. Consultar.";
        cout << "\n\t3. actualizar.";
        cout << "\n\t4. Eliminar Productos.";
        cout << "\n\t5. Salir.";

        cout << "\n\n > "; 
        cin >> data; cin.ignore();

        if (data == "1") {
            string name, amount, price;

            cout << "\n > Nombre del producto: "; getline(cin, name);
            cout << " > Cantidad del producto: "; getline(cin, amount);
            cout << " > Precio del producto: "; getline(cin, price);

            productos.agregar(name, amount, price);

        } else if (data == "2") {
            unsigned int number;

            cout << "\n > Numero del producto a consultar: ";
            cin >> number; cin.ignore();

            productos.consultar(number);

        } else if (data == "3") {
            unsigned int number;
            string name, amount, price;

            cout << "\n > Numero del producto a actualizar: ";
            cin >> number; cin.ignore();

            cout << " (Deja vacío el campo si no quieres modificarlo)\n";

            cout << " > Nombre nuevo: "; getline(cin, name);
            cout << " > Cantidad nueva: "; getline(cin, amount);
            cout << " > Precio nuevo: "; getline(cin, price);

            productos.actualizar(number, name, amount, price);

        } else if (data == "4") {
            unsigned int number;

            cout << "\n > Numero del producto a eliminar: ";
            cin >> number; cin.ignore();

            productos.eliminar(number);
        }
    }

    cout << "\n\n [+] Al dar enter el archivo sera borrado: "; 
    cin.ignore();

    return 0;
}
