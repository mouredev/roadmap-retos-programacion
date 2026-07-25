// Estructuras de datos

#include <iostream>
#include <vector>
#include <list>
#include <stack>
#include <queue>
#include <deque>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

void arrays() {
    string names[3] = {"Joseph", "Miley", "Rick"};
    
    cout << "El segundo elemento del arreglo: " << names[1] << endl;
    cout << "El primer elemento del arreglo: " << names[0] << "," << endl;
    
    names[0] = "Roberto";
    
    cout << "ahora es " << names[0] << endl;
}

void vectors() {
    vector<string> names = {"Joseph", "Miley", "Rick"};
    
    cout << "El primer elemento del vector: " << names.front() << endl;
    cout << "El segundo elemento del vector: " << names[1] << endl; 
    // Preferencia usar para vectores porque hace saber si ocurrió un error
    cout << "El segundo elemento del vector: " << names.at(1) << endl;
    cout << "El último elemento del vector: " << names.back() << endl;
    
    names.back() = "Ricardo";
    
    cout << "Ahora el último elemento es " << names.at(2) << endl;

    names.push_back("Alan");
    
    cout << "Se agregó un nuevo nombre: " << names.back() << endl;

    names.pop_back();

    cout << "El último elemento del vector: " << names.back() << endl;
}

void lists() {
    list<string> names = {"Joseph", "Miley", "Rick"};

    cout << "El primer elemento de la lista: " << names.front() << endl;
    cout << "El último elemento de la lista: " << names.back() << endl;

    names.front() = "Alan";

    cout << "Ahora el primer elemento es " << names.front() << endl;

    names.push_front("Fil");
    names.push_back("Flor");

    cout << "La lista completa:" << endl;

    for (string name : names) {
        cout << name << endl;
    }

    names.pop_back();
    names.pop_front();

    cout << "La lista completa:" << endl;

    for (string name : names) {
        cout << name << endl;
    }
}

void stacks() {
    stack<string> names;

    names.push("Rick");
    names.push("Joseph");
    names.push("Alan");

    cout << "El primer elemento tomado de la pila: " << names.top() << endl;

    names.top() = "Flor";

    cout << "Ahora el primer elemento tomado de la pila es " << names.top() << endl;

    names.pop();

    cout << "Ahora el primer elemento tomado de la pila es " << names.top() << endl;
}

void queues() {
    queue<string> names;

    names.push("Rick");
    names.push("Joseph");
    names.push("Alan");

    cout << "El primer elemento de la queue: " << names.front() << endl;
    cout << "El último elemento de la queue: " << names.back() << endl;

    names.front() = "Gil";

    cout << "Ahora el primer elemento de la queue es " << names.front() << endl;

    names.pop();

    cout << "Ahora el primer elemento de la queue es " << names.front() << endl;
}

void dequeues() {
    deque<string> names = {"Rick", "Sam", "Joseph"};
    
    cout << "El primer elemento de la deque: " << names.front() << endl;
    cout << "El último elemento de la deque: " << names.back() << endl;

    names.at(1) = "Flor";
    names.push_back("Gil");
    names.push_front("Vale");

    for (string name : names) {
        cout << name << endl;
    }

    names.pop_back();
    names.pop_front();

    for (string name : names) {
        cout << name << endl;
    }
}

void sets() {
    set<string> namesAsc = {"Rick", "Sam", "Joseph", "Rick"};

    for (string name : namesAsc) {
        cout << name << endl;
    }

    set<float> numbers = {2.5, 10.3, 5.1, 1.3, -0.5};

    for (float number : numbers) {
        cout << number << endl;
    }

    set<string, greater<string>> namesDesc= {"Rick", "Sam", "Joseph"};

    namesDesc.insert("Vale");

    for (string name : namesDesc) {
        cout << name << endl;
    }

    cout << "---------" << endl;

    namesDesc.erase("Rick");

    for (string name : namesDesc) {
        cout << name << endl;
    }

    cout << "---------" << endl;

    // Elimina todos los elementos
    namesDesc.clear();

    for (string name : namesDesc) {
        cout << name << endl;
    }

    cout << "---------" << endl;
}

void maps() {
    map<string, string> translations = {{"hello", "hola"}, {"world", "mundo"}, 
        {"code", "código"}};

    cout << "La traducción para 'hello' es " << translations["hello"] << endl;
    cout << "La traducción para 'world' es " << translations["world"] << endl;
    // Se prefiere utilizar .at() porque lanzaría un error si no existe la key
    cout << "La traducción para 'code' es " << translations.at("code") << endl;

    translations.at("hello") = "bonjour";
    cout << "La traducción para 'hello' es " << translations.at("hello") << endl;

    // Es correcto usar cualquiera de éstas para insertar nuevos key-value
    translations["language"] = "lenguaje";
    translations.insert({"syntax", "sintaxis"});

    cout << "La traducción para 'language' es " << translations.at("language") << endl;
    cout << "La traducción para 'syntax' es " << translations.at("syntax") << endl;

    translations.erase("language");

    for (auto translation : translations) {
        cout << translation.first << " - " << translation.second << endl;
    }

    cout << "---------" << endl;

    translations.clear();

    for (auto translation : translations) {
        cout << translation.first << " - " << translation.second << endl;
    }

    cout << "---------" << endl;
}

void algorithms() {
    vector<string> names = {"Miley", "Joseph", "Rick"};

    vector<string>::iterator it;            
    
    sort(names.begin(), names.end());

    for (it = names.begin(); it != names.end(); it++) {
        cout << *it << endl;
    }

    auto name = find(names.begin(), names.end(), "Joseph");

    if (name != names.end()) {
        cout << "Joseph ha sido encontrado" << endl;
    } else {
        cout << "No se ha encontrado Joseph" << endl;
    }
}

/*
EJERCICIO EXTRA
Crea una agenda de contactos por terminal.
- Debes implementar funcionalidades de búsqueda, inserción, actualización
  y eliminación de contactos.
- Cada contacto debe tener un nombre y un número de teléfono.
- El programa solicita en primer lugar cuál es la operación que se quiere realizar,
  y a continuación los datos necesarios para llevarla a cabo.
- El programa no puede dejar introducir números de teléfono no numéricos y con más
  de 11 dígitos (o el número de dígitos que quieras).
- También se debe proponer una operación de finalización del programa.
*/

map<string, string> people;

void showMenu() {
    cout << "1. Agregar nuevo contacto" << endl;
    cout << "2. Buscar contacto" << endl;
    cout << "3. Actualizar contacto" << endl;
    cout << "4. Eliminar contacto" << endl;
    cout << "5. Salir" << endl;
}

bool isEmpty() {
    return people.empty();
}

void addPerson() {
    string name, telephone;
    cout << "Escribe el nombre: ";
    cin >> name;
    cout << "Escribe el número de teléfono (debe ser de 10 dígitos): ";
    cin >> telephone;

    while (true) {
        if (telephone.size() > 10 || telephone.size() < 10 ||
        !all_of(telephone.begin(), telephone.end(), ::isdigit)) {
            cout << "El número de teléfono no es válido. Inserte uno nuevo: ";
            cin >> telephone;
        } else {
            people.insert({name, telephone});
            cout << "Nuevo contacto agregado.\n";
            break;
        }
    }
}

void findPerson() {
    string name, telephone;

    if (isEmpty()) {
        cout << "La agenda está vacía." << endl;
    } else {
        cout << "Escribe el nombre: ";
        cin >> name;

        try {
            telephone = people.at(name);

            cout << "Nombre: " << name << "\nTeléfono: " << telephone << endl;
        } catch (out_of_range) {
            cout << "No existe el nombre en tu agenda de contactos." << endl;
        }
    }
}

void updatePerson() {
    string name, telephone;

    if (isEmpty()) {
        cout << "La agenda está vacía." << endl;
    } else {
        cout << "Escribe el nombre: ";
        cin >> name;

        try {
            people.at(name);

            cout << "Escribe el nuevo número de teléfono: ";
            cin >> telephone;

            while (true) {
                if (telephone.size() > 10 || telephone.size() < 10 || 
                !all_of(telephone.begin(), telephone.end(), ::isdigit)) {
                    cout << "El número de teléfono no es válido. Inserte uno nuevo: ";
                    cin >> telephone;
                } else {
                    people.at(name) = telephone;
                    cout << "Contacto actualizado." << endl;
                    break;
                }
            }
        } catch (out_of_range) {
            cout << "No existe el nombre en tu agenda de contactos." << endl;
        }
    }
}

void deletePerson() {
    string name;

    if (isEmpty()) {
        cout << "La agenda está vacía." << endl;
    } else {
        cout << "Escribe el nombre: ";
        cin >> name;

        try {
            people.at(name);
            people.erase(name);

            cout << "Contacto eliminado." << endl;
        } catch (out_of_range) {
            cout << "No existe el nombre en tu agenda de contactos." << endl;
        }
    }
}

void telcel() {
    int inputMenu;
    cout << "Bienvenido a Telcel, qué deseas hacer hoy?" << endl;

    do {
        cout << endl;
        showMenu();
        cin >> inputMenu;
        cout << endl;

        switch (inputMenu) {
            case 1:
                addPerson();
                break;
            case 2:
                findPerson();
                break;
            case 3:
                updatePerson();
                break;
            case 4:
                deletePerson();
                break;
            case 5:
                break;
            default:
                cout << "Elige un valor válido, por favor." << endl;
                break;
        }
    } while (inputMenu != 5);
    
}

int main() {
    cout << "ARREGLOS" << endl;
    arrays();

    cout << "\nVECTORES" << endl;
    vectors();

    cout << "\nLISTAS" << endl;
    lists();

    cout << "\nSTACKS" << endl;
    stacks();

    cout << "\nQUEUES" << endl;
    queues();

    cout << "\nDEQUEUES" << endl;
    dequeues();

    cout << "\nSETS" << endl;
    sets();

    cout << "\nMAPS" << endl;
    maps();

    cout << "\nALGORITHMS" << endl;
    algorithms();
    
    cout << "-------------------------------------" << endl;

    telcel();

    return 0;
}