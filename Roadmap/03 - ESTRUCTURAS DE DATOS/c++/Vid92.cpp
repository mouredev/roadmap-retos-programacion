#include <iostream>
#include <string>
#include <sstream>
//#include <cmath>

using namespace std;


//Ejercicio extra - agenda contactos
struct agenda{
    string nombre;
    int telefono;
};


agenda *contacto = new agenda[50];

bool flag = false;
bool flagOut = false;
int n = 1;


void inserte(){
    string num;
    do{
        cout<<"Ingrese nombre:"<<endl;
        cin>>contacto[n].nombre;
        
        num = "";
        flag = false;
        cout<<endl<<"Ingrese telefono:"<<endl;
        cin>>num;
        
        for(int i=0;i<num.length();i++){
            if(!isdigit(num[i])){
                flag = true; 
                goto next;
            }
        }
        
        next:
        if(num.length()>11 | flag){
            cout<<"Error, longitud o digitos no numericos"<<endl;
            contacto[n].nombre = "";
            n--;
        }
        else{
            contacto[n].telefono = stoi(num);
        }
            
        n++;
    }while(num.length()>11 | flag);
    cout<<endl;
}

void buscar(){
    string nombre;
    bool flag=false;
    cout<<"Nombre de contacto a buscar..."<<endl;
    cin>>nombre;
    for(int x=1;x<n;x++){
       if(contacto[x].nombre==nombre){
           cout<<" Contacto encontrado! : "<<contacto[x].nombre<<" -- "<<contacto[x].telefono<<endl; 
           flag = true;
           break;
       }
    }
    
    if(!flag)
        cout<<endl<<"Contacto no encontrado"<<endl<<endl;
}

void actualizar(){
    cout<<endl<<"-------Nombre--------|-----------Telefono----------"<<endl;
    for(int x=1;x<n;x++){
       cout<<"       "<<contacto[x].nombre<<"                    "<<contacto[x].telefono<<endl; 
    }
}

void eliminar(){
    string nombre;
    actualizar();
    cout<<"Eliminar contacto con nombre..."<<endl;
    cin>>nombre;
    
    for(int x=1;x<n;x++){
       if(contacto[x].nombre==nombre){
           for(int i=x;i<n;i++){
                contacto[i].nombre = contacto[i+1].nombre;
                contacto[i].telefono = contacto[i+1].telefono;
           }
       }
    }
    n--;
    actualizar();
}

void menu(){
    int a;
    cout<<endl<<"------------------------------ Agenda de Contactos -----------------------------------------"<<endl;
    cout<<endl<<"Inserte numero para elegir opcion:"<<endl;
    cout<<endl<<"| 1. Busqueda | 2. Insertar | 3. Actualizar | 4. Eliminar | 5. Salir |"<<endl<<endl;
    cin>>a;
    
    switch(a){
        case 1:
        buscar();
        break;
        
        case 2:
        inserte();
        break;
        
        case 3:
        actualizar();
        break;
        
        case 4:
        eliminar();
        break;
        
        case 5:
        cout<<"Fin"<<endl;
        flagOut = true;
        break;
        
        
        default:
        cout<<"Opcion no encontrada"<<endl;
        break;
    }
}


int main(){
    do{
        menu();
    }while(!flagOut);
    return 0;
}
