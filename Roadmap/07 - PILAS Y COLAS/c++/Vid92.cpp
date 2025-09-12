#include <iostream>
#include <queue>
#include <stack>
#include <ctype.h>

using namespace std;

void pageWeb(){
    cout<<endl<<"----------- Ejercicio 1 : pagina web --------------"<<endl;
    stack<string> pweb;
    
    pweb.push("www.github.com");    //posicion 1
    pweb.push("www.google.com");    //posicion 2
    pweb.push("www.youtube.com");   //posicion 3
    
    cout<<"Tamaño de pweb: "<<pweb.size()<<endl;
    
    string opcion;
    int pos = 1;
    
    while(1){
        cout<<"Ingrese opcion:  [>>atras<<] [>>adelante<<] [>>salir<<] "<<endl;
        cin>>opcion;
        
        string cadena;
        cadena = opcion;
        
        for (int indice = 0; cadena[indice] != '\0'; ++indice){
		    cadena[indice] = tolower(cadena[indice]);
	    }
        
        opcion = cadena;
        
        if(opcion=="atras"){
            pos-=1;
            if(pos<=0)
                pos = 3;
        }
        
        else if(opcion=="adelante"){
            pos+=1;
            if(pos>=4)
                pos = 1;
        }
        
        else if(opcion=="salir"){
            break;
        }
        
        if(pos==1)
            cout<<"www.github.com"<<endl;
        else if(pos==2)
            cout<<"www.google.com"<<endl;
        else if(pos==3)
            cout<<"www.youtube.com"<<endl;
    }
}

void doc_printer(){
    cout<<"-------------------- Ejercicio 2: Impresora ------------------"<<endl;
    queue<string>impresora;
    
    string op;

    while(1){
        cout<<endl<<"Ingrese opcion [>>Imprimir/Ingrese nombre del documento<<] [>>salir<<]"<<endl;
        cin>>op;
        
        string cadena;
        cadena = op;
        
        for (int indice = 0; cadena[indice] != '\0'; ++indice){
    	    cadena[indice] = tolower(cadena[indice]);
        }
            
        op = cadena;
        
        if(op=="salir"){
            break;
        }
        else if(op=="imprimir"){
            if(impresora.size() == 0){
                cout<<"No hay archivo que imprimir ..."<<endl;
            }else{
                cout<<"Imprime: "<<impresora.front()<<endl;
                impresora.pop();
            }
        }
        else{
            cout<<"se agrega ..."<<op<<endl;
            impresora.push(op);
        }
    }
}

int main()
{
    queue<int> cola;
    stack<int> pila;
    
    //Cola (Queue)
    cout<<"-----------Cola (Queue) -----------"<<endl;
    cola.push(10);          //Agrega elementos 
    cola.push(4);
    cola.push(1);
    cout<<"Indica el primer elemento del queue: "<<cola.front()<<endl;
    cout<<"Tamaño del queue: "<<cola.size()<<endl;
    cout<<"Indica el ultimo elemento del queue: "<<cola.back()<<endl;
    cola.pop();            //Elimina elementos - el primero del queue
    cout<<"Tamaño del queue despues de eliminar un elemento: "<<cola.size()<<endl;
    cout<<"Indica si esta vacia el queue (0-false,1-true): "<<cola.empty()<<endl;
    
    //Pila (Stack)
    cout<<endl<<"-----------Pila (Stack) -----------"<<endl;
    pila.push(7);           //Agrega elementos
    pila.push(13);
    pila.push(9);
    cout<<"Tamaño de stack: "<<pila.size()<<endl;
    pila.pop();             //Eliminar elementos - primer elemento 
    cout<<"Indica el primer elemento del stack: "<<pila.top()<<endl;
    cout<<"Tamaño de stack despues de eliminar un elemento: "<<pila.size()<<endl;
    cout<<"Indica si esta vacia el stack (0-false,1-true): "<<pila.empty()<<endl;
    
    //Dificuldad extra
    pageWeb();
    doc_printer();
    
    return 0;
}

