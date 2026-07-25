/*
 ! EJERCICIO:
 * Implementa los mecanismos de introducción y recuperación de elementos propios de las
 * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
 * o lista (dependiendo de las posibilidades de tu lenguaje).
*/
#include<iostream>
#include<stack>
#include<queue>
#include<stdlib.h>// para el new
#include<algorithm>
#include<string>
using namespace std;
//! pila con estructua
// este es un nodo, puede tener cuantos datos quieras
struct PilaNodo
{
  int dato;
  PilaNodo *siguiente; // un nodo siempre apunta(* puntero a siguiente) a uno siguiente, por eso delmismo nodo
  //(PilaNodo) esta apuntando a siguiente
};
struct ColaNodo
{
  int dato;
  ColaNodo *siguiente;
};

// todo pila
void using_stack();
void pila();//!pila con estructura
void apilar(PilaNodo*&,int);// insertar elemento a la pila, ("*"puntero "&" referencia)
void desapilar(PilaNodo *&);
void verElementosPila(PilaNodo *&);
//todo cola
void using_queque();
void cola(); //! cola con structura
void insertarCola(ColaNodo*&,ColaNodo*&,int);
bool cola_vacia(ColaNodo *);
void eliminar_cola(ColaNodo *&, ColaNodo *&);
void mostrar_cola(ColaNodo *&, ColaNodo *&);
// todo extra
void historial_web();
string tolower_p(string);
void impresora();
int main(){

  using_stack();
  pila();
  using_queque();
  cola();
  historial_web();
  impresora();
  return 0;
}
// todo pila
void using_stack(){
  //! pila , lifo (last in first out), (ultimo en entrar, primero en salir)
  /*
  ?La clase stack tiene varios métodos que puedes utilizar:

  * push: Agrega un elemento al tope de la pila.
  * pop: Elimina el elemento en el tope de la pila.
  * top: Devuelve una referencia al elemento en el tope de la pila.
  * empty: Devuelve true si la pila está vacía, false en caso contrario.
  * size: Devuelve el número de elementos en la pila.
  */

  stack<int> pila;
  // ver si la pila está vacia o no
  if(pila.empty()){
    cout << "la pila esta vacia" << endl;
  }else{
    cout << "la pila tiene pila" << endl;
  }

  pila.push(1); //agregando elemento al tope de la pila
  pila.push(2); //agregando elemento al tope de la pila
  pila.push(3); //agregando elemento al tope de la pila
  cout << "pila original: " << pila.empty() << endl; // ver si la pila tiene
  stack<int> temp = pila; // temporal para imprimir los elementos de la pila
  while (!temp.empty())
  {
    cout << temp.top() << "-> ";
    //eliminando el tope de la pila copia 
    temp.pop();
  }
  
  cout << "\n tamaño de la pila original: " << pila.size() << endl;
}

//! pila con estrucura
void pila(){
  /*
  !pila 
  * es una estructua de datos de entradas ordenadas, tales que solo se pueden ingresar
  * y eliminar por un extremo, llamado cima.
  */
  PilaNodo *cima = nullptr;
  int option;
  int valor;
  bool continuar = true;
  while (continuar)
  {
    cout << "\n\tmenu\n";
    cout << "1- Apilar" << endl;
    cout << "2- Desapilar" << endl;
    cout << "3. Ver pila" << endl;
    cout << "4- Salir" << endl;
    cout << "\ningrese opcion: ";
    cin >> option;
    switch (option)
    {
      case 1:
        cout << "ingrese un valor: ";
        cin >> valor;
        apilar(cima,valor);
        break;
      case 2:
        if(cima == nullptr){
          cout << "NULL" << endl;
          break;
        }
        desapilar(cima);
        break;
      case 3:
        if(cima == nullptr){
          cout << " Null" << endl;
          break;
        }
        verElementosPila(cima);
        break;
      case 4:
        continuar = false;
        break;
      
      default:
        cout << "opcion no valida, ingrese otra" << endl;
        break;
    }
  }
}
//? insertar elemento en la pila
void apilar(PilaNodo*& cima,int valor){
  /*
  ? pasos para agregar un elemento a la pila
  *1- crear espacio en memoria para almacerar el nodo (con "new")
  *2- cargar el valor dentro del nodo(dato)
  *3- cargar el puntero pila dentro del nodo(*siguiente)
  *4- asignar el nuevo nodo a pila
  */

  PilaNodo *nuevoNodo = new PilaNodo();// #1
  nuevoNodo->dato = valor; // #2
  nuevoNodo->siguiente = cima;// #3
  cima = nuevoNodo; // #4
  cout << "elento apilado" << endl;
}

void desapilar(PilaNodo*& cima){
  /*
  !desapilar
  *1- creau una variable aux de tipo nodo (Nodo* aux)
  *2- igual n a aux->dato
  *3- pasar pila a siguiente nodo
  *4- eliminar aux
  */
  int valor;
  PilaNodo *aux = cima;// #1
  valor = aux->dato; // #2
  cima = aux->siguiente; // #3
  cout << "valor: " << valor << " eliminado " << endl;
  delete aux; // #4
}

void verElementosPila(PilaNodo*& cima){
 
  PilaNodo *copia = cima; // una copia de la pila para ir desapilando y mostrando los elementos
  while (copia != nullptr)
  {
    cout<<" " << copia->dato << " ->";
    copia = copia->siguiente;
  }
  cout << "Null" << endl;
}

//todo cola
void using_queque(){
  /*
  ! cola (fifo) (first in first out) (primero en entrar, primero en salir)
  ? queue tiene varios elmentos que puede utilizar

  * push: agrega un elemento al final de la cola
  * pop: elimina un elemento al principio de la cola
  * front: acceder al primer elemento de la cola 
  * back: acceder al ultimo elemento de la cola
  * empty: devuelve true si la pila esta vacia y false si es lo contrario
  * size: devuelve el numero de elementos de la cola
  */
  queue<int> cola;
  cout << "cola: " << cola.empty() << endl;
  cola.push(1); // agrega un elemento al final de la cola
  cola.push(2); // agrega un elemento al final de la cola
  cola.push(3); // agrega un elemento al final de la cola
  
  //* recorriendo la cola
  queue<int> copia = cola;
  while (!copia.empty())
  {
    cout << " "<<copia.front()<<" <- ";
    copia.pop();
  }
  cout << " Null." << endl;
  cout << "tamaño de la cola: " << cola.size()<<endl;
}

void cola(){
  /*
  !cola
  * es una estructura de datos, caracterizada por ser una secuencia de elementos en la que la operacion
  * de inserción se realiza por un extremo y la extracción por el otro
  */
  ColaNodo *frente = nullptr;
  ColaNodo *fin = nullptr;
  bool continuar = true;
  int option;
  int valor;
  while (continuar)
  {
    cout<<"\n\t menu \n"<<endl;
    cout << "1- agregar elemento " << endl;
    cout << "2- quitar elemento " << endl;
    cout << "3- mostrar cola " << endl;
    cout << "4- salir" << endl,
    cout << "\nopcion: ";
    cin >> option;
    switch (option)
    {
      case 1:
        cout << "ingrese el valor: ";
        cin >> valor;
        insertarCola(frente, fin, valor);
        break;
      case 2:
        if(cola_vacia(frente)){
          cout << "cola vacia " << endl;
          break;
        }
        eliminar_cola(frente, fin);
        cout << " eliminado" << endl;
        break;
      case 3:
        if(cola_vacia(frente)){
          cout << "cola vacia " << endl;
          break;
        }
        mostrar_cola(frente, fin);
        break;
      case 4:
        continuar = false;
        break;
      
      default:
        cout << "opcion no valida, intente denuevo " << endl;
        break;
    }
  }
  
}

void insertarCola(ColaNodo*& frente,ColaNodo*& fin,int valor){
  /*
    ?pasos para insertar elementos a la cola
    *1- crear un espacio en memoria para almacenar un nodo.
    *2- asignar ese nuevo nodo al dato que se quiere insertar.abor.
    *3- asignar los punteros frente y fin hacia el nuevo nodo.
  */
  ColaNodo *nuevo_nodo = new ColaNodo(); // #1
  nuevo_nodo->dato = valor; // #2
  nuevo_nodo->siguiente = nullptr;
  // #3
  if(cola_vacia(frente)){
    frente = nuevo_nodo;
  }else{
    fin->siguiente=nuevo_nodo;
  }
  fin = nuevo_nodo;
  cout << "\n elemento insertado a cola\n";
}

//* funcion para determinar si la cola está vacia o nó
bool cola_vacia(ColaNodo* frente){
  return frente == nullptr;
}

void eliminar_cola(ColaNodo *& frente, ColaNodo *& fin){
  /*
  ? pasos para eliminar elementos de la cola
  
  *1- obtener el valor del nodo
  *2- crear un nodo aux y asignarele el frente de la cola
  *3- eliminar el nodo del frente de la cola
  */
  int valor = frente->dato; // #1
  ColaNodo *aux = frente; // #2
  // #3
  if(frente == fin){
    frente = nullptr;
    fin = nullptr;
  }else{
    frente = frente->siguiente;
  }
  delete aux;
  cout << valor;
}

void mostrar_cola(ColaNodo *& frente, ColaNodo *& fin){
  ColaNodo *copia_frente = frente;
  ColaNodo *copia_fin = fin;
  while (copia_frente != nullptr)
  {
    eliminar_cola(copia_frente, copia_fin);
    if(copia_frente != nullptr){
      cout << " <- ";
    }else{
      cout << " Null." << endl;
    }
  }
  
  
}
/*
 ! DIFICULTAD EXTRA (opcional):
 * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
 *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
 *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
 *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
 * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos.
*/


 void historial_web(){
  //* creando dos pilas para los historiales, tanto de atras como de adelante
   stack<string> historial_atras;
   stack<string> historial_adelante;
   string pagina_actual="Inicio";
   string var;
   cout << "\t\nhistorial web\n";
   cout << "en este menu hay 4 opciones: " << endl;
   cout << "ingrese el nombre de la pagina a la que quiere visitrar" << endl;
   cout << "escribir la letra (b) para retroceder a una pagina anterior(si es que la hay)" << endl;
   cout << "escribir la palabra (f), para avanzar a una pagina ya antes ingresada" << endl;
   cout << "escribir la letra (s), para salir" << endl;
   while (true) 
   {
     cout << "\npagina actual: " << pagina_actual << endl;
     cout << "\ningrese la opcion (b,f,s,pagina): ";
     getline(cin, var);
     var = tolower_p(var);
     if (var =="s" || var =="b" || var=="f")
     {
      if (var == "s")
      {
        cout << "\nsaliendo del historial........................" << endl;
        break;
      }
      if (var == "b")
      {
        if(!historial_atras.empty())//* revisar si aun hay elemtos en la pila
        {
          //*es escogio retroceder, la pagina actual, se pasa a la pila de siguiente
          historial_adelante.push(pagina_actual);
          pagina_actual = historial_atras.top();//* se asigna el tope de historial atras a pagina actual
          historial_atras.pop();//* se elimina la ultima pagina del historial de atras
        }else{
          cout << "\nno hay mas paginas registradas" << endl;
        }
      }
      if(var == "f"){
        if(!historial_adelante.empty()){//* comprovar si hay elementos en la pila
        //* se escogio adelantar, la pagina actual, se pasa a la pila de atras
          historial_atras.push(pagina_actual);//*se pasa a atras la pagina actual
          pagina_actual = historial_adelante.top();//* se asigna a pagina actual el elemento que este en la sima de siquiente
          historial_adelante.pop();//* se elimina el tope de la pila siguiente
        }else{
          cout << "\nno hay mas paginas registradas" << endl;
        }
        
      }
     }else{
      //* se ingreso una nueva pagina
      historial_atras.push(pagina_actual);//* se pasa a la pila atras la pagina actual
      pagina_actual = var;//* se asigna a pagina actula, la pagina recien ingresada
     }
     
    
   }
   
 }

 string tolower_p(string palabra){
   transform(palabra.begin(), palabra.end(), palabra.begin(), ::tolower);
   return palabra;
}

void impresora(){
  queue<string> documentos;
  string var;
  string copia;

  cout << "\n\t impresora compartida\n";
  while (true)
  {
    if(!documentos.empty()){
      cout << "\nnumero de elmentos en cola: " << documentos.size() << endl;
      cout << "nombre de documento en la cola: " << documentos.front();
      cout << "\ningrese un nombre de documento, (p) para imprimir o (s) para salir: ";
      getline(cin, var);
      copia = tolower_p(var);
      if(copia =="p" || copia=="s"){

        if(copia =="p"){
          cout << "imprimiendo: " << documentos.front() << endl;
          documentos.pop();
        }
        if(copia =="s"){
          cout << "\nsaliendo de la impresora\n";
          break;
        }
      }else{
        documentos.push(var);
        cout << "\nse agrego documento";
      }
    }else{
      cout<<" la impresora esta vacia, ingrese un nombre de documento: ";
      getline(cin, var);
      documentos.push(var);
    }
  }
  
}