/*
 ! EJERCICIO:
 * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
 * implemente una superclase Animal y un par de subclases Perro y Gato,
 * junto con una función que sirva para imprimir el sonido que emite cada Animal.
*/
/*
 ! DIFICULTAD EXTRA (opcional):
 * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 * actividad, y almacenan los empleados a su cargo.
*/
#include<iostream>
#include<string>
#include<vector>
using namespace std;
// todo clases ejercicio
class Animal{
  //* atributos, en este caso como solo piden el sonido que hacen , solo sonido
  private:
    string _sonido;
    string _nombre;

  public:
    //* constructor, está vacio :v
    Animal(string nombre, string sonido){
      _nombre = nombre;
      _sonido = sonido;
    };
    //? metodos
    //* metodo set sonido , para ingresar el sonido que produce el  animal
    // void setAtributos(string nombre, string nuevoSonido){
    //    _sonido = nuevoSonido;
    //    _nombre = nombre;
    // }
    //* metodo para mostrar el sonido que produce el animal
    void get_sonido(){
      cout <<_nombre<<": "<< _sonido << endl;
    };
};

class Perro : public Animal{
  public:
    Perro(string nombre, string sonido):Animal(nombre,sonido){};
};

class Gato : public Animal{
  public:
    Gato(string nombre,string sonido):Animal(nombre,sonido){};
};
// todo clases extra

class Empleado{
  private:
    string _id;
    string _nombre;
    string _cargo;

  public:
  Empleado(string id,string nombre,string cargo){
    _id = id;
    _nombre = nombre;
    _cargo = cargo;
  }
  void getInfoEmpleado(){
    cout << "Empleado: " << _id << ": " << _nombre<<" cargo: "<<_cargo << endl;
  }
};
class Gerente: public Empleado{
  private:
    string _nombre;
    vector<Empleado> personal;

  public:
    Gerente(string id,string nombre,string cargo): Empleado(id,nombre,cargo){
      _nombre = nombre;
    }
    void set_agregar_personal(Empleado nuevoP){
      personal.push_back(nuevoP);
    }
    void getPersonal(){
      cout << "Gerente: " << _nombre << " personal a cargo \n";
      for (int i = 0; i < personal.size();i++){
        personal[i].getInfoEmpleado();
      }
      
    }
  
};

class GerenteProyecto : public Empleado{
  private:
    string _nombre;
    vector<Empleado>equipo;
    vector<string> proyectos;

  public:
   GerenteProyecto(string id, string nombre,string cargo):Empleado(id,nombre,cargo){
     _nombre = nombre;
   }
   void setPersonalAcargo(Empleado miembro){
    equipo.push_back(miembro);
   }
       
   void setProyectos(string nombreProyecto){
     proyectos.push_back(nombreProyecto);
   }
   void getEquipo(){
     cout << "Gerente de proyectos " << _nombre << ": miembros de su equipo:\n";
     for (int i = 0; i < equipo.size();i++){
       equipo[i].getInfoEmpleado();
     }
   }
   void getProyectos(){
    cout << "Gerente de proyectos " << _nombre << ": proyectos a cargo:\n";
    for (int i = 0; i < proyectos.size();i++){
      cout << proyectos[i] << endl;
    }
   }
};

class Programador : public Empleado{
  private:
    string _nombre;
    string _proyectoEnCurso ="ninguno";

  public:
    Programador(string id, string nombre,string cargo):Empleado(id,nombre,cargo){
      _nombre = nombre;
    }
    void setProyecto(string proyecto){
    _proyectoEnCurso = proyecto;
    }
    void getProyectoEnCurso(){
      cout << "Programador: " << _nombre << endl;
      cout << "proyecto en curso: " << _proyectoEnCurso << endl;
    }
};

void ejercicio();
void extra();
int main(){

  ejercicio();
  extra();
  return 0;
}
void ejercicio(){
  Perro chester("Chester","Guau!");
  Gato lita("Lita","Miau!");
  // chester.setAtributos("Chester","Guau!");
  // lita.setAtributos("Lita","Miau!");
  chester.get_sonido();
  lita.get_sonido();
}

void extra(){
  Gerente manuel("A125", "Manuel Zoto","Gerente");
  GerenteProyecto jonas("G233", "Jonas Marques","Gerente de proyectos");
  Programador roberto("P564", "Roberto Hernandez","programador");
  manuel.getInfoEmpleado();
  jonas.getInfoEmpleado();
  roberto.getInfoEmpleado();
  manuel.set_agregar_personal(jonas);
  manuel.set_agregar_personal(roberto);
  manuel.getPersonal();
  jonas.setPersonalAcargo(roberto);
  jonas.setProyectos("cambiar color del boton");
  jonas.setProyectos("reiniciar la pc");
  jonas.getEquipo();
  jonas.getProyectos();
  roberto.setProyecto("cambiar color boton");
  roberto.getProyectoEnCurso();
}
