
#include <iostream>
#include <queue>
#include <stack>

using namespace std;

class persona{
    private:
        string name;
        string profesion;
        int edad;
        
    public: //constructor 
        persona(string name,string profesion,int edad){
            this->name = name;
            this->profesion = profesion;
            this->edad = edad;
        }
        
        void imprimir(){
            cout<<"Nombre: "<<this->name<<endl<<"Edad: "<<this->edad<<endl<<"Profesion: "<<this->profesion<<endl;
        }
};

class Pila{
    private:
        stack<int>pp;
        
    public:
        Pila(){
            
        }
        
    void agregarDato(int dato){
        pp.push(dato);
        cout<<"El número ingresado a la Pila: "<<dato<<endl;
    }
    
    void eliminarDato(){
        pp.pop();
        cout<<"Se elimina un número de la Pila"<<endl;
    }
    
    void primerStack(){
        cout<<"Primer elemento de la Pila: "<<pp.top()<<endl;
    }
    
    void tamañoStack(){
        cout<<"Tamaño de la Pila: "<<pp.size()<<endl;
    }
    
    void totalStack(){
        stack<int> tmp=pp;
        int i = 1;
        cout<<"Elementos en Pila:"<<endl;
        while(i!=tmp.size()){
            i++;
            if(!tmp.empty()){
                cout<<tmp.top()<<endl;
                tmp.pop();   
            }
            else{
                break;
            }
        }
    }
};

class Cola{
    private:
        queue<int>qq;
        int numero;
        
    public:
        Cola(){
            this->numero;
        }
       
        
    void agregarDato(int dato){
        this->numero = dato;
        qq.push(this->numero);
        cout<<"El número ingresado al Queue: "<<this->numero<<endl;
    }
    
    void eliminarDato(){
        qq.pop();
        cout<<"Se elimina un número del Queue"<<endl;
    }
    
    void mostrarQueue(){
        cout<<"Primer elemento del Queue: "<<qq.front()<<endl;
    }
    
    void tamañoQueue(){
        cout<<"Tamaño del Queue: "<<qq.size()<<endl;
    }
    
    void ultimoQueue(){
        cout<<"Ultimo elemento: "<<qq.back()<<endl;
    }
    
    void totalQueue(){
        queue<int> tmp=qq;
        int i = 1;
        cout<<"Elementos en Queue:"<<endl;
        while(i!=tmp.size()){
            i++;
            if(!tmp.empty()){
                cout<<tmp.front()<<endl;
                tmp.pop();   
            }
            else{
                break;
            }
        }
    }
};

int main()
{
    persona* gente1 = new persona("María","Doctora",19);
    gente1->imprimir();
    
    cout<<endl;
    
    persona* gente2 = new persona("Jóse","Profesor",30);
    gente2->imprimir();
    
    //Dificultad extra
    Cola par;
    Pila par2;
    
    cout<<endl<<"------------------------Queue------------------------"<<endl;
    
    par.agregarDato(30);
    par.agregarDato(7);
    par.agregarDato(11);
    par.agregarDato(5);
    
    cout<<endl;
    par.mostrarQueue();
    par.totalQueue();
    par.ultimoQueue();
    par.tamañoQueue();
    par.eliminarDato();
    par.mostrarQueue();
    par.tamañoQueue();
    
    cout<<endl<<"-----------------------Stack-----------------------"<<endl;
    
    par2.agregarDato(10);
    par2.agregarDato(3);
    par2.agregarDato(9);
    par2.agregarDato(17);
    
    cout<<endl;
    par2.tamañoStack();
    par2.totalStack();
    par2.primerStack();
    par2.eliminarDato();
    par2.tamañoStack();
    par2.primerStack();
    
    return 0;
}
