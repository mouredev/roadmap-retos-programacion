#include <iostream> 
#include <array> 
#include <iomanip>
#include <vector> 
#include <list>
#include <queue>
#include <deque> 
#include <tuple> 
#include <map>
#include <utility>
#include <set>
#include <iterator>
#include <algorithm> // se usa solamente en la operacion all_of 

using namespace std; 

// *******************************************************************************************
/*Esta funcion es necesaria para que queue pueda imprimirse, refierase al ejemplo de la cola */
void imprCola(queue <int>& q){
    while (!q.empty()){
        cout << q.front() << ' '; 
        q.pop(); 
    }
    cout << '\n'; 
}
// *******************************************************************************************
// *********************** Funciones para el uso de la agenda *****************************
void insert_num(string& nombre, string& numero, map <string, string>& mapa){

    cout << "Escribe el nombre: "; 
    cin >> nombre; 
    cout << " y el numero del contacto: "; 
    cin >> numero;

    if ((numero.length() > 0 && numero.length() <= 11) && (all_of(numero.begin(), numero.end(), ::isdigit))) {
        mapa[nombre] = numero; 
    }

    else{
        cout << "Solo pon 11 digitos y que sea digitos!" << '\n'; 
    } 
}

void search_num(string& nombre, map <string, string>& mapa){
    if (mapa.find(nombre) != mapa.end()){
        cout << "Aqui tienes al contacto " << mapa.find(nombre) -> first  << " - " <<  mapa.find(nombre) -> second << '\n'; 
    }
    else{
        cout << "No se encontro el contacto" << '\n'; 
    }
}

void delete_num(string& nombre, map<string, string>& mapa){
    if (mapa.find(nombre) != mapa.end()){
        mapa.erase(nombre); 
    }
    else{
        cout << "No se encontro el contacto" << '\n'; 
    }
}

void update_num(string& nombre, string& numero,  map<string,string>& mapa){
    if (mapa.find(nombre) != mapa.end()){
        mapa.erase(nombre); 

        insert_num(nombre,numero,mapa); 
        cout << "Este es el nuevo contacto" << '\n'; 
    }
    else{
        cout << "No se encontro el contacto" << '\n'; 
    }
}

void print_num(map<string,string>& mapa){
    for (auto &pair : mapa){
        cout << pair.first << " ---- " <<  pair.second << '\n'; 
    }
}
// ********************* fin de el uso de las funciones para la agenda ******************
// ********************************************************************************************
int main()
{
    // *******************************************************************
    // Matriz de una dimension
    string nombres[8] = {"Eduardo", "Roberto", "Camilo", "Mario", "Edgardo" ,"Emiliano", "Marty", "Alejandro"};
    cout << "Ejemplos de Matrices de una y dos dimensiones: " <<  '\n';
    
    nombres[2] = "Mariano"; // cambia el nombre de el 3er individuo. Indice 2

    for (string i : nombres){
        cout << i << " "; 
    }
    cout << '\n';
     
    // Matriz de 2 dimensiones
    int cuadricula [3][5] = {1,2,3,4,5,
                            6,7,8,9,10,
                            11,12,13,14,15}; 

    for (int i = 0 ; i < 3; i++){
        cout << setw(6) << '\n'; 
        cuadricula[2][1] = 98; // cambia el 2do elemento de la 3er fila de 12 a 98
        for(int j = 0; j < 5; j++){
            cout << cuadricula[i][j] << " ";
        }
    }
    cout << '\n'; 
    cout << "El size de la cuadricula es de: " << sizeof(cuadricula) << " bytes" <<  '\n'; // imprime el tamano de la matriz  
        // *******************************************************************

    cout << '\n';
    cout << '\n'; 
    // Estructura (struct)
        // ********************************************************************
    cout << "Ejemplo de estructura: " << '\n'; 
    struct Persona {
        string nombre; 
        int edad; 
        string pasatiempo; 
        
    }; 
    Persona persona1, persona2; 
    persona1.nombre = "Miguel"; 
    persona1.edad = 23; 
    persona1.pasatiempo = "jugar videojuegos"; 

    cout << "Te presento a: " << persona1.nombre << " el tiene " << persona1.edad << " años, y le gusta " 
         << persona1.pasatiempo << '\n'; 

    persona2.nombre = "Juan"; 
    persona2.edad = 19; 
    persona2.pasatiempo = "nadar";

    cout << "Te presento a: " << persona2.nombre << " el tiene " << persona2.edad << " años, y le gusta " 
         << persona2.pasatiempo << '\n'; 

        // *************************************************************** 
    cout << '\n'; 
    cout << '\n';  
    // *******************************************************************
    // Vector
    cout << "Ejemplo Vector en una secuencia de numeros: "; 
    vector <int> secuencia;
    vector <int> secuencia2; 
    

    secuencia.push_back(5);      //   0.   [5]
    secuencia.push_back(3);     //    1.   [3]
    secuencia.push_back(1);    //     2.   [1]
   
    vector<int> :: iterator it = secuencia.begin() + 1; // se posisiona en el indice 2 

    secuencia.emplace(it, -2);  //   1. [-2]
    secuencia.emplace_back(-7); //   3. [-7] agrega un elemento adicional en el fondo de la secuencia
    secuencia.emplace_back(-9); //   4. [-9] ""     ""    ""        ""    "" ""  ""  despues del indice 3

    secuencia.push_back(-25);  //    5. [-25] va en orden, asi que se agrega despues de la operacion anterior
    secuencia.front() += secuencia.back(); //     1. indice de el frente [5]
                                        //        = [5] + indice de el fondo [-25] -> [20]
    secuencia.pop_back();     //      remueve el elemento -25
    for(int i = 0; i < secuencia.size(); i++){ 
        cout << secuencia[i] << " ";  // imprime cada elemento del vector
    }
    cout << '\n'; 
    cout << "2da forma para llamar a la secuencia: ";  
    for (vector<int> :: iterator it1 = secuencia.begin(); it1 != secuencia.end(); it1++){
        cout << *it1 << ' ';  
    }
    
    cout << '\n'; 

    for(int i = 0; i < 4; i++){
        secuencia2.push_back(i); 
    }
    
    cout << '\n'; 
    cout << "Este es el numero en el espacio 5 es igual a [4] del vector: " << secuencia.at(4) << '\n'; 
    cout <<"Este es el tamaño de la secuencia: " <<  secuencia.size() << '\n';  
    
    secuencia2.assign(4, -20);  //  0 - 4 [-20,-20,-20,-20] assigna a los 4 espacios el valor -20
    secuencia.swap(secuencia2); // remplaza el contenido de secuencia 2 desde secuencia
    secuencia2.swap(secuencia); // deshace la operacion anterior 
    it = secuencia2.begin(); // reinicia el valor del iterador y lo pone en el segundo elemento de 
                                //  la secuencia 2 
    secuencia2.insert((it + 3), 2, 39); // en el indice 4 se posisiona el fichero e imprime en los siguientes 
    // 2 (3 - 4) indices el numero 39 
    it = secuencia2.begin(); 
    secuencia2.emplace((it + 2) , 50);  // 3. [50] es substituido  
    secuencia2.erase((secuencia2.begin() + 2), secuencia2.end() - 2); // borra el elemento del indice 1 y 
    // del indice 4 [5] de la secuencia
    // clear() borrar la secuencia 
    
    cout << "Este es el contenido de secuencia 2: "; 
    for(vector<int> :: iterator it2 = secuencia2.begin(); it2 != secuencia2.end(); ++it2){
        cout << *it2 << ' '; 
    }

    cout << '\n'; 
    cout << '\n';
    // *******************************************************************
    // Lista
    // Tiene los miembros de funciones al igual que los vectores 
    // Solo que este incluye emplace_front()
    cout << "Ejemplo de una lista " << '\n'; 
    list <string> lista_compras {"tomates, cebollas, chiles", "papaya"}; 

    list <string> :: iterator itr; 
    lista_compras.push_back("zanahorias"); 
    lista_compras.push_back("brocolis"); 
    lista_compras.push_back("rabanos"); 
    lista_compras.push_back("frijoles"); 
    lista_compras.pop_front(); // remueve el elemento tomates de la lista
    lista_compras.emplace_front("camotes"); // substituye a cebollas de la lista 
    lista_compras.emplace_back("berenjena"); // se posisiona al final 

    cout <<"Este es el frente de la lista: " <<  lista_compras.front() << '\n'; 
    cout << "Este es el fondo de la lista: " << lista_compras.back() << '\n'; 
    
    cout << "Lista completa aqui: "; 
    for (auto itr = lista_compras.begin(); itr != lista_compras.end(); ++itr){
        cout << *itr << ' '; 
    }
    // **********************************************************************
    cout << '\n'; 
    cout << '\n'; 
    // **********************************************************************
    // cola 
    cout << "Ejemplo de cola: "<< '\n'; 

    queue <int> lugar; 
    lugar.push(20); 
    lugar.push(25); 
    lugar.push(45); 
    lugar.push(19); 
    lugar.emplace(42); 
    lugar.pop(); 
    lugar.pop(); 

    imprCola(lugar); 
    // ************************************************************************
    cout << '\n';  
    // ************************************************************************

    // Tuplas
    cout << "Ejemplo de tupla: " << '\n'; 
    tuple <int, double, string> num_y_nom (10.4, 27.5, "Julio") ; 
    tuple <int, double, string> num_y_nom2; (9, 5.2, "Mario"); 

   
    cout << get<0>(num_y_nom) << ' ' << get<1>(num_y_nom) << ' ' << get<2>(num_y_nom) << '\n'; 

    num_y_nom.swap(num_y_nom2); // intercambia las tuplas num_y_nom2 por las de num_y_nom

    cout << get<0>(num_y_nom2) << ' ' << get<1>(num_y_nom2) << ' ' << get<2>(num_y_nom2) << '\n'; 
    cout << '\n'; 
    // ***************************************************************************
    // Sets 
    cout << "Ejemplo de set: " << '\n'; 
    set <int> set_num; 
    set_num.insert(10); 
    set_num.insert(23); 
    set_num.insert(107); 
    set_num.erase(23); 
    set_num.emplace_hint(set_num.begin(), 29); 
    set_num.emplace_hint(set_num.end(), 72); 
    set_num.emplace(11); 

    for (auto it = set_num.begin(); it != set_num.end(); ++it){
        cout << *it << ' '; 
    }
    cout << '\n'; 
    // ****************************************************************************
    // Colas de doble fin
    cout << "Ejemplo de un deque: "; 
    deque <string> bebidas = {"soda", "jugos", "agua"}; 

    bebidas.push_front("cerveza"); // luego este
    bebidas.push_back("vino"); 
    bebidas.emplace_front("té"); // este elemento se pone primero 
    bebidas.emplace_back("agua carbonatada"); 


    for (deque <string> :: iterator it = bebidas.begin(); it != bebidas.end(); ++it){
        cout << *it << ' '; 
    }
    cout << '\n'; 
    cout << '\n'; 
    // ******************************************************************************
    // Mapa 
    cout << "Ejemplo de un mapa #1: " << '\n';  
    map <string, string> traductor; 
    traductor.insert (pair <string, string> ("bote", "boat"));
    traductor.insert (pair <string, string> ("manzana", "apple")); 
    traductor["paleta"] = "lolleypop"; 
    traductor["carne"] = "steak"; 

    for (auto pair : traductor){
        cout << pair.first << " ---- la traduccion: ----- " << pair.second << '\n'; 
    }

    cout << '\n'; 

    cout << "Ejemplo de otro mapa #2: " << '\n'; // este ejemplo usa una lista como 
    cout << '\n'; 
    map <string, list<string> > DBZ; 

    list <string> ataque_Goku {"kamehameha", "kienzan", "kaio ken"}; 
    list <string> ataque_Piccolo {"makankosappo", "masenko", "mafuba", "kaikosen"}; 
    list <string> ataque_Gohan {"kamehameha", "makankosappo", "gekizturanma", "super masenko"}; 

    DBZ.insert(pair<string, list<string>> ("Goku", ataque_Goku));
    DBZ.insert(pair<string, list<string>> ("Gohan", ataque_Gohan));
    DBZ.insert(pair<string, list<string>> ("Piccolo", ataque_Piccolo)); 

    for (auto pair : DBZ){
        cout << pair.first << " posee: "; 
        for (auto ataque : pair.second){
            cout << ataque << " ";  
        }
        cout << '\n'; 
    }

    /* DIFICULTAD EXTRA (opcional):
     * Crea una agenda de contactos por terminal.
     * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
    * - Cada contacto debe tener un nombre y un número de teléfono.
    * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
    *   los datos necesarios para llevarla a cabo.
    * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
     *   (o el número de dígitos que quieras)
    * - También se debe proponer una operación de finalización del programa. */
   

   int opcion = 0; 
   bool cont = true; // esta condicion se mantiene true, se usa en el bucle while
   map <string, string> numero_cel; 
   string nombre, numero; 
    while(cont){
        cout << '\n' << '\n'; 
        cout << "-----AGENDA DE CONTACTOS ------" << '\n'; 
        cout << "¿Que quisieras hacer?  " << '\n';
        cout << "1. Insercion " << '\n'; 
        cout << "2. Busqueda " << '\n'; 
        cout << "3. Actualizacion " << '\n'; 
        cout << "4. Eliminacion " << '\n'; 
        cout << "5. Terminar el programa" << '\n'; 
        cout << "Selecciona la opcion: "; 
        cin >> opcion; 
        cout << '\n'; 

        if(cin.fail()){
            cin.clear(); // limpia el flag de error para futuras operaciones  
            cin.ignore(numeric_limits<streamsize>::max(),'\n'); // previene que los viejos input de operaciones 
            // pasadas no interfieran con nuevos inputs 
            cout << "No es valido! Elige algo entre 1 y 5" << '\n'; 
            continue;
        }

        switch(opcion){
            case 1:
                insert_num(nombre,numero,numero_cel); 
                cout << '\n'; 
                print_num(numero_cel); 
 
                break; 
            case 2: 
                cout << "Escribe el nombre del contacto que quieres buscar: ";
                cin >> nombre; 

                search_num(nombre,numero_cel);
                cout << '\n'; 
                print_num(numero_cel); 

                break; 
            case 3: 
                cout << "Escribe el nombre que quieres actualizar: "; 
                cin >> nombre; 

                update_num(nombre,numero,numero_cel); 
                cout << '\n'; 
                print_num(numero_cel);

                break; 

            case 4: 
                cout << "Escribe el nombre que quieres eleminar: ";
                cin >> nombre; 

                delete_num(nombre,numero_cel);
                cout << '\n';  
                print_num(numero_cel); 

                break;

            case 5: 
                cout << "El fin de la agenda." << '\n'; 
                cont = false;  
                break; 
            default: 
                cout << "No es valido! Elige algo entre el 1 al 5." << '\n'; 
                break; 
        }
    }
}
