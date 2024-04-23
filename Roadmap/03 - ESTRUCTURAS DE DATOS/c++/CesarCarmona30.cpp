#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <tuple>
#include <algorithm>

using namespace std;
/*
  ESTRUCTURAS DE DATOS
*/

// Arrays

/*
  Arreglo de enteros inicializado con valores específicos.
  Los arreglos son estructuras estáticas que no pueden modificarse en tiempo de ejecución.
  No tienen métodos o funciones nativas que permitan insertar, borrar o ordenar elementos.
  Sin embargo, podemos actualizar elementos individualmente.
*/

int my_array[] = {0, 5, 6, 2, 7, 2, 6 ,8, 9};

template <typename Structure>
void printStruct(const Structure& struc) {
  for (const auto& element : struc) {
    cout << element << " ";
  }
  cout << endl;
}

template <typename... Ts>
void printStruct(const tuple<Ts...>& tuple) {
  apply([](const auto&... args) {
    ((cout << args << " "), ... );
  }, tuple);
  cout << endl;
}

template<typename K, typename V>
void printStruct(const map<K, V>& map) {
  for (const auto& pair : map) {
    cout << pair.first << ": " << pair.second << endl;
  }
  cout << endl;
}


/*
  Arreglos inicializados en su declarción
  Si no se pasan la cantidad completa
  de elementos, los demas se inicializan por defecto

   int my_array2[5] = {1, 2, 3}; => {1, 2, 3, 0, 0};
   char my_arr[5] = {'a', 'b', 'c'}; => {'a', 'b', 'c', '', ''};
*/ 

map<string, string> agenda;


void searchContact(string contact_name) {
  if (agenda.find(contact_name) != agenda.end()) {
    cout << "Contacto: " << agenda.find(contact_name)->first << " - " << agenda.find(contact_name)->second << endl;
  } else {
    cout << "Contacto no encontrado." << endl;
  }
}

void newContact(string contact_name, string phone_number) {
  if (phone_number.size() != 10) {
    cout << "Numero de telefono invalido, debe tener 10 digitos." << endl;
    return;
  }
  agenda[contact_name] = phone_number;
  cout << "Contacto agregado correctamente" << endl;
}

void updateContact(string contact_name, string new_number) {
  if (agenda.find(contact_name) != agenda.end()) {
    agenda.erase(contact_name);
    newContact(contact_name, new_number);
    cout << "Contacto actualizado correctamente." << endl;
  } else {
    cout << "Contacto no encontrado." << endl;
  }

}

void deleteContact(string contact_name) {
  if (agenda.find(contact_name) != agenda.end()) {
    agenda.erase(contact_name);
    cout << "Contacto eliminado correctamente." << endl;
  } else {
    cout << "Contacto no encontrado." << endl;
  }
}

void showContacts() {
  printStruct(agenda);
}

void menu() {
  cout << "--AGENDA--" << endl;
  bool cont = true;
  do {
    string name, phone;
    int opcion = 0;
    cout << "1.- BUSCAR CONTACTO" << endl;
    cout << "2.- NUEVO CONTACTO" << endl;
    cout << "3.- ACTUALIZAR CONTACTO" << endl;
    cout << "4.- ELIMINAR CONTACTO " << endl;
    cout << "5.- LISTAR CONTACTOS " << endl;
    cout << "6.- SALIR " << endl;
    cout << "Seleccione una opcion: ";
    cin >> opcion;
    switch (opcion){
      case 1:
        cout << "Nombre del contacto a buscar: ";
        cin >> name;
        searchContact(name);
        break;
      case 2:
        cout << "Nombre del nuevo contacto: ";
        cin >> name;
        cout << "\nNumero de telefono: ";
        cin >> phone;
        newContact(name, phone);
        break;
      case 3:
        cout << "Nombre del contacto a actualizar: ";
        cin >> name;
        cout << "\nNuevo numero de telefono: ";
        cin >> phone;
        updateContact(name, phone);
        break;
      case 4:
        cout << "Nombre del contacto a eliminar: ";
        cin >> name;
        deleteContact(name);
        break;
      case 5:
        cout << "Lista de contactos: " << endl;
        showContacts();
        break;
      case 6:
        cont = false;
        cout << "Hasta luego" << endl;
        break;      
      default:
        cout << "Opcion no valida, intentelo de nuevo" << endl;
        break;
    }
  } while (cont);
}


int main() {
  /*
    Vectores: Estructuras de un solo tipo de dato
    que pueden cambiar dinámicamente en tiempo de 
    ejecución
  */
  cout << "VECTOR: " << endl;
  vector<int> my_vector = {1, 3, 5, 74, 21, 12};
  printStruct(my_vector);
  // Inserción al final
  my_vector.push_back(43); // {1, 3, 5, 74, 21, 12, 43}
  printStruct(my_vector);
  // Inserción 5 posiciones despues del primer elemento (indice 5)
  my_vector.insert(my_vector.begin() + 5, 10);  // {1, 3, 5, 74, 21, 10, 12, 43}
  printStruct(my_vector);
  // Eliminación del último elemento
  my_vector.pop_back();  // {1, 3, 5, 74, 21, 10, 12}
  printStruct(my_vector);
  // Eliminación del elemento con índice 5 (vector original)
  my_vector.erase(my_vector.begin() + 5);   // {1, 3, 5, 74, 21, 12}
  printStruct(my_vector);
  // Eliminación del índice 2 al 4 
  my_vector.erase(my_vector.begin() + 2, my_vector.begin() + 4);   // {1, 3, 10, 12}
  printStruct(my_vector);
  // Ordenamiento, menor a mayor
  sort(my_vector.begin(), my_vector.end());
  printStruct(my_vector);
  // Ordenamiento mayor a menor
  sort(my_vector.begin(), my_vector.end(), greater<int>());
  printStruct(my_vector);
  // Actualización 
  my_vector[3] = 5;
  printStruct(my_vector);
  sort(my_vector.begin(), my_vector.end());
  printStruct(my_vector);
  /*
    Sets: Estructuras de un solo tipo
    de dato, únicos, que no permiten duplicados y pueden 
    cambiar de tamaño dinámicamente en tiempo de ejecución.
    -No se pueden ordenar de otro modo que el establecido
    -No se pueden actualizar los datos
  */ 
  cout << "\nSET: " << endl; 
  set<int> my_set = {1, 23, 8, 3, 6};
  printStruct(my_set);
  // Insercion al final
  my_set.insert(7);
  printStruct(my_set);
  my_set.insert(5);
  my_set.insert(6); // No se inserta
  printStruct(my_set);
  // Eliminación del elemento con valor 5
  my_set.erase(5);
  printStruct(my_set);
  // Eliminación de todo el set
  my_set.clear();
  printStruct(my_set);
  /*
    Tuples: Estructuras de múltiples tipos de datos inmutables,
    por lo tanto no hay manera de insertar, borrar, actualizar
    y ordenar elementos.
  */ 
  cout << "\nTUPLE: " << endl; 
  tuple<int, int, int> my_tuple = {2, 4, 6};
  printStruct(my_tuple);
  tuple<int, string, char> my_tuple2 = {19, "Cesar", 'H'};
  printStruct(my_tuple2);

  /*
    Maps: Estructuras de pares clave-valor con claves o identificadores
    únicos, ordenados por defecto
  */
  cout << "\nMAP: " << endl; 
  map<int, string> my_map = {{1, "One"}, {2, "Two"}, {5, "Five"}, {8, "Eigth"}};
  //Inserción
  my_map.insert({7, "Seven"});
  my_map[6] = "Seis";
  my_map.insert({5, "Cinco"}); // No se inserta
  printStruct(my_map);
  // Eliminación, se hace por el identificador o clave
  my_map.erase(6);
  printStruct(my_map);
  // Actualización
  my_map[8] = "Eight";
  printStruct(my_map);

  cout << endl;

  menu();
  return 0;
}