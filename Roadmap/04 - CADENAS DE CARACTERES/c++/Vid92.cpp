#include <iostream>
#include <string>
#include <algorithm>

using namespace std;


void palindromo(string palabra){
    string wordPrueba;
    for(int i=(palabra.length()-1);i>=0;i--){
        wordPrueba += palabra[i];
    }
    if(wordPrueba == palabra){
        cout<<palabra + "... es un palindromo!"<<endl;
    }else{
        cout<<palabra + "... no es un palindromo!"<<endl;
    }
}

void anagrama(string palabra1, string palabra2){
    int count = 0;
    string palabra3;
    palabra3 = palabra2;
    if(palabra1.length()==palabra2.length()){
        for(int i=0;i<palabra1.length();i++){
            for(int j=0;j<palabra1.length();j++){
                if(palabra1[i] == palabra2[j]){
                    count++;
                    palabra2[j] = '\0';
                    break;
                }
            }
        }
        
        if (count == palabra1.length()){
            cout<<palabra1 + " es anagrama de "+ palabra3+"!"<<endl;
        }else{
            cout<<palabra1+" no es anagrama de "+palabra3+"!"<<endl;
        }
        
    }else{
        cout<<palabra1+" no es anagrama de "+palabra2+"!"<<endl;
    }
}

void isograma(string palabra){
    string temp = palabra;
    string tmp = palabra;
    int cont = 0;
    int conteo[palabra.length()];
    for(int i=0;i<palabra.length();i++){
        cont = 0;
        palabra = tmp;
        for(int j=0;j<palabra.length();j++){
            if((palabra[i]==tmp[j])&&(palabra[i]!='0')&&(tmp[j]!='\0')){
                tmp[j] = '\0';
                cont++;
                conteo[i] = cont;
            }
        }
    }
    
    int num = 0;
    for(int n=0;n<temp.length();n++){
        if(conteo[n]>=2){
            num++;
        }
    }
    
    if(num>2){
        cout<<temp+" es un isograma!"<<endl;
    }else{
        cout<<temp+" no es un isograma!"<<endl;
    }
}

void analizar(string word1,string word2){
    palindromo(word1);
    palindromo(word2);
    anagrama(word1,word2);
    isograma(word1);
    isograma(word2);
}


int main()
{
    //Concatenacion
    string name = "Mario ";
    string last_name = "Gonzales";
    
    cout<<name+last_name<<endl;
    
    //Longitud
    string tamaño = "longitud";
    
    cout<<"longitud: "<<tamaño.length()<<endl;
    cout<<"longitud: "<<tamaño.size()<<endl;
    
    //minuscula, mayuscula
    int ch = 0x70; //p
    
    cout<<"minuscula: "<<tolower(ch)<<endl; //p
    cout<<"mayuscula: "<<toupper(ch)<<endl; //P
    
    //replace
    name.replace(0,1,"rosa");
    cout<<"replace: "<<name<<endl;
    
    //erase
    tamaño.erase(5);
    cout<<"erase: "<<tamaño<<endl;
    
    //buscar
    string oracion = "La manzana es roja o verde";
    //bool pos = oracion.find("i");
    
    cout<<"posicion: "<<(oracion.find("roja"))<<endl;
    //cout<<"posicion: "<<pos<<endl;
    
    //subcadena
    string subcadena = "Hola mundo";
    cout<<"subcadena: "<<(subcadena.substr(0, 5))<<endl;
    
    //Ejercicio extra
    analizar("roma","amor");

    return 0;
}
