#include <iostream>
#include <vector>
#include <algorithm> // necesario para remove
#include <map>
#include <regex>
using namespace std;

//* estructura 
/*
 una estructura es  es un tipo compuesto definido por el usuario. Se compone de campos o 
 de miembros que pueden tener diferentes tipos.
*/
struct PERSONA{  // nombre de la estructura(declarando la estructura)
// declarando los tipos de campos 
  int edad;
  string name;
  string last_name;
}miembros_de_la_familia; // definir el objeto de la estructura

struct AGENDA{
  string nombre;
  long long int numero;
};
//* estructura para poder retornar mas de un valor
struct RETORNAR
{
  bool encontrado=false;
  int posicion=NULL;
};




//* Prototipos de funciones
void insert_Sort(vector<int>); // funcion de ordenmiento por inserción
void imprimir_vector(vector<int>);
void burbuja_simple(vector<int>); // fucion de ordeanmeinto por burbuja simple
void eliminar_por_posicion(vector<int> &, int);
void eliminar_por_valor(vector<int> &, int);

//? funciones para el ejercicio extra
bool validarNombre(const string &nombre);
bool validarNumero(const string &input);
void menu(vector<AGENDA>&);
void ingresar_contacto(vector<AGENDA>&);
RETORNAR buscar_contacto(vector<AGENDA>&,string);
void actualizar_contacto(vector<AGENDA>&,string);
void ordenar_contactos(vector<AGENDA>);
void eliminar_contacto(vector<AGENDA>&,string nombre);
// funcion para ordenar los contactos
bool compararPorNombre(const AGENDA&, const AGENDA&);

int main(){
  
  //? struct PERSONA hermana; // declarando una estructura al estilo C
  // // ingresando los valores
  // hermana.edad = 23;
  // hermana.name = "berenice";
  // hermana.last_name = " Morales Zapata";

  // cout << "hemana: " << hermana.name <<hermana.last_name<<" "<<hermana.edad<< endl;
  //? Declarando estructuras al estilo c++
  //? PERSONA hermano = {14, "Matias", "Morales Zapata"};
  //? PERSONA papa = {40, "Pedro", "Morales"};
  //? PERSONA mama = {41, "Ana", "Zapata"};

  // cout << "hermano: " << hermano.name << " " << hermano.last_name << " edad: " << hermano.edad << endl;
  // cout << "papá: " << papa.name << " " << papa.last_name << " edad: " << papa.last_name << endl;
  // cout << "mama: " << mama.name << " " << mama.last_name << " edad: " << mama.edad << endl;

  // vector<int> numeros = {2,5,3,7,1};
  // insert_Sort(numeros);
  // cout<<"vector original "<<endl;
  // imprimir_vector(numeros);
  // cout << "ordenaminto por burbuja simple: " << endl;
  // burbuja_simple(numeros);
  // vector<int> numeros_2 = {4, 2, 9, 8, 5, 3};
  // imprimir_vector(numeros_2);
  // numeros_2.push_back(10); // se inserta un nuevo numeroal final del vector
  // imprimir_vector(numeros_2);
  // eliminar_por_posicion(numeros_2,3);
  // eliminar_por_valor(numeros_2,5);

  //* begin() da el inicio del iterador, 0, el prinicipio, end() da el final , tamaño n
  // numeros_2.insert((numeros_2.begin() + 3), 7);
  // imprimir_vector(numeros_2);
  //* map
  // map<string, int> people = { {"John", 32}, {"Adele", 45}, {"Bo", 29} };
  // map<string, int> estudiante = {{"jose", 923424323}, {"pedro,98768730"}};
  // for( auto es : people){
  //   cout << es.first << " is " << es.second << endl;
  // };
  // map<int, AGENDA> contactos;
  // AGENDA new_contacto;
  // contactos.insert({1, {new_contacto.nombre = "jose", new_contacto.numero = 98767887634}});
  // contactos.insert({2, {new_contacto.nombre = "maria", new_contacto.numero = 93456758965}});
  // for(auto persona : contactos){
  //   cout << persona.first << " : " << persona.second.nombre<<" "<<persona.second.numero<< endl;
  // }

  //? ejercicio extra
  vector<AGENDA> contactos = {{"jose", 987654623451},{"maria",98788765437}};
  
  
   menu(contactos);

  return 0;
}
void imprimir_vector(vector<int> numeros){
  for (int i = 0; i < numeros.size(); i++)
 {
   cout << numeros[i]<<", ";
 }
 cout << endl;
}

void insert_Sort(vector<int> numeros){
  /*
  * Pseudocodigo:
  * for j=1 hasta (tamaño) hacer
  *   key = vec[j]
  *   i= j-1
  *   while i>= 0 && vec[i]> key
  *     vec[i+1]= vec[i]
  *     i= i-1
  *   vec[i+1] = key 
  */
  int key;
  int i;
  for (int j = 1; j < numeros.size(); j++)
  {
     key = numeros[j];
     i = j - 1;
     while (i>= 0 && numeros[i]>key)
     {
       numeros[i + 1] = numeros[i];
       i = i - 1;
     }
     numeros[i + 1]= key;
 }

 imprimir_vector(numeros);
}

void burbuja_simple(vector<int> vec){

  /*
  *Pseudocodigo
  para i desde 0 hasta n-1 hacer
    para j desde 0 hasta n-i-1
     si vec[j] > vec[j+1] entonces
      intercambiar vec[j] y vec[j+1]
      fin_si
    fin_para
  fin_para
  */
  int aux=0;

  for (int i = 0; i < (vec.size()-1); i++)
  {
    for (int j = 0; j < (vec.size()-i-1); j++)
    {
      if (vec[j] > vec[j+1])
      {
        aux = vec[j];
        vec[j] = vec[j+1];
        vec[j+1] = aux;
      }
      
    }
 }

 imprimir_vector(vec);
}

void eliminar_por_posicion(vector<int>& vec, int pos){
   //* eliminar por un número por posición.
   //* estoy pasando el vector por referencia, asi que afecta al que fue creado en main
  vector<int>::iterator it = vec.begin() + pos;
  vec.erase(it);
  // *eliminando el valor de la posiicon ingresada
  imprimir_vector(vec);
}

void eliminar_por_valor(vector<int>& vec, int valor){
  //* eliminar por valor
  vec.erase(remove(vec.begin(), vec.end(), valor), vec.end());
  //* eliminando el valor ingresado
  imprimir_vector(vec);
}

//? funciones para el ejercicio extra
bool validarNombre(const string& nombre) {
    regex patron("^[A-Za-zÁÉÍÓÚáéíóúÑñ ]{1,}$"); 
    return regex_match(nombre, patron);
}
bool validarNumero(const string& input) {
    regex patron("^\\d{1,11}$"); // Expresión regular para validar números de 1 a 11 dígitos
    return regex_match(input, patron);
}
void menu(vector<AGENDA>& contactos)
{
  int option;
  while (option != 6)
  {
    system("cls");
    cout << "\t AGENDA DE CONTACTOS " << endl;
    cout << "1. ingresar contacto " << endl;
    cout << "2. buscar contacto " << endl;
    cout << "3. actualizar contacto " << endl;
    cout << "4. ordenar contactos " << endl;
    cout <<"5. eliminar contacto "<<endl;
    cout << "6. salir " << endl;
    cout << " opcion: ";
    cin >> option;
    string nombre;
    switch (option)
    {
    case 1:
      ingresar_contacto(contactos);
      system("pause");
      break;
    case 2:
      
      cout << "ingrese el nombre del contacto a buscar: ";
      cin >> nombre;
      buscar_contacto(contactos,nombre);
      system("pause");
      break;
    case 3:
     
      cout << "ingrese el nombre del contacto a buscar: ";
      cin >> nombre;
      actualizar_contacto(contactos,nombre);
      system("pause");
      break;
    case 4:
      ordenar_contactos(contactos);
      system("pause");
      break;
    case 5:
      cout << "ingrese el nombre del contacto a buscar: ";
      cin >> nombre;
      eliminar_contacto(contactos,nombre);
      system("pause");
      break;
      case 6:
        cout << " adios " << endl;
      system("pause");
        break;
    default:
      cout << " opcion no valida, intente denuevo " << endl;
      system("pause");
      break;
    }
  }
};
void ingresar_contacto(vector<AGENDA>& contactos){
  AGENDA new_contacto;
  string nombre;
  long long int numero;
  bool correcto = false;
  bool val_1 = false;
  bool val_2 = false;
  while (!correcto)
  {
    cout << "ingrese el nombre: ";
    cin >> nombre;
    if(!validarNombre(nombre)){
      cout << "almenos deve ingresar un caracter " << endl;
    }else{
      val_1 = true;
    }
    cout << "ingrese el numero, no mayor a 11 dijitos: ";
    cin>> numero;
    if (!validarNumero(to_string(numero)))
    {
      cout << "numero no valido" << endl;
    }else{
      val_2 = true;
    }
    if (val_1 && val_2)
    {
      correcto = true;
    }
    
    
  }
  
  
  contactos.push_back({new_contacto.nombre = nombre, new_contacto.numero = numero});
  cout << " se agrego el contacto " << endl;
};

RETORNAR buscar_contacto(vector<AGENDA>& contactos,string nombre){
  
  bool encontrado=false;
  int posicion;
  int i = 0;
  RETORNAR retornar_variables; // estructura para retornar 2 valores
  while ( i<=contactos.size())
  {
    if (contactos[i].nombre == nombre)
    {
      posicion = i;
      encontrado = true;
      break;
    }
    
    i++;
  }
  if (encontrado)
  {
    
    cout << "contacto encontrado "<<endl;
    cout << contactos[posicion].nombre << endl;
    cout <<"Movil "<< contactos[posicion].numero << endl;
    retornar_variables.encontrado = true;
    retornar_variables.posicion = posicion;
  }else{
    cout << "contacto no encontrado " << endl;
    retornar_variables.encontrado = false;
  }

  return retornar_variables; // retornar 2 valores
};

void actualizar_contacto(vector<AGENDA>& contactos,string nombre){
  RETORNAR respuesta; // estructura para tomar los 2 valores retornados
  respuesta=buscar_contacto(contactos, nombre);
  int posicion=respuesta.posicion;
  bool encontrado=respuesta.encontrado;
  int op;

  if (encontrado)
  {
    // cout << "contacto: " << endl;
    // cout << contactos[posicion].nombre << " " << contactos[posicion].numero << endl;
    cout << "actualizar contacto: " << endl;
    cout << "cambiar el nombre? , si=1, no=0" << endl;
    cout << "op: ";
    long long numero;
    cin >> op;
    bool val = false;
    if (op ==1)
    {
      cout << "nombre: ";
      cin>>contactos[posicion].nombre;
     
    }
    cout << " cambiar el numero?, si=1, no=0" << endl;
     cout << "op: ";
    cin >> op;
    if (op==1)
    {
      while (!val)
      {
        cout << "numero: ";
        cin >> numero;
      
       if (!validarNumero(to_string(numero)))
       {
         cout << "numero no valido" << endl;
       }else{
        val = true;
        contactos[posicion].numero= numero;
      
       }
      
      }
      
      
    }
    cout << "contacto actualizado: " << endl;
    cout << contactos[posicion].nombre << " " << contactos[posicion].numero << endl;
  }else{
    cout << "paso algo :c" << endl;
  }
  
};

void ordenar_contactos(vector<AGENDA> contactos){
  
  // funcion para ordenar los nombres segun el alfabeto 
  sort(contactos.begin(), contactos.end(), compararPorNombre);

  for (int i = 0; i < contactos.size(); i++)
  {
    cout << "-----------------------" << endl;
    cout << contactos[i].nombre << endl;
    cout <<"Movil "<< contactos[i].numero << endl;
    
  }

};
void eliminar_contacto(vector<AGENDA>& contactos,string nombre){
  RETORNAR respuesta;
  respuesta = buscar_contacto(contactos, nombre);
  int posicion = respuesta.posicion;
  bool encontrado = respuesta.encontrado;
  if (encontrado)
  {
    vector<AGENDA>::iterator it = contactos.begin() + posicion;
    contactos.erase(it);
    cout << "contacto eliminado " << endl;
  }
  

};

bool compararPorNombre(const AGENDA &a, const AGENDA &b) {
    return a.nombre < b.nombre;
}