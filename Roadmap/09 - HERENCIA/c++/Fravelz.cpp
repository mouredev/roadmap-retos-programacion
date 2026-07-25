#include <iostream>
#include <vector>

using namespace std;

class Animal {
private:
    string name;

public:
    Animal(string name_) : name(name_) {}

    virtual void sonido() = 0;
};

class Perro : public Animal {
public:
    Perro(string name_) : Animal(name_) {};

    void sonido() override { cout << "\nGuau!!"; }
};

class Gato : public Animal {
public:
    Gato(string name_) : Animal(name_) {};

    void sonido() override { cout << "\nMiau!!"; }
};

// ***************** DIFICULTAD EXTRA (opcional) ***************** //

class Empleados {
protected:
    int id;
    string name;
    vector<string> empleados;


public:
    Empleados(string name_, int id_) {
        this->id = id_;
        this->name = name_;
    }

    virtual void agregar_empleados(string) = 0;

    void mostrarEmpreados() {
        if (empleados.size() >= 1) {
            cout << "\n > Empleados de " << name << ": ";
            for (string empleado : empleados) cout << empleado << ' ';

        } else {
            cout << "\n [!] " << name << " no tienes empleados...";
        }
    };
};

class Gerente : public Empleados {
public:
    Gerente(string name_="001", int id_=0) : Empleados(name_, id_) {}

    void cordinar_proyectos() { 
        cout << '\n' << name << " esta cordinando todos los proyectos..."; 
    };

    void agregar_empleados(string name_) { empleados.push_back(name_); };
};

class Gerente_de_Proyectos : public Empleados {
public:
    Gerente_de_Proyectos(string name_="001", int id_=0) : Empleados(name_, id_) {}

    void cordinar_proyecto() { cout << '\n' << name << " esta cordinando un proyecto..."; };

    void agregar_empleados(string name_) { empleados.push_back(name_); };
};

class Programador : public Empleados {
protected:
    string habilidad;

public:
    Programador(string name_, int id_, string habilidad) : Empleados(name_, id_) {
        this->habilidad = habilidad;
    }

    void codeando() { 
        cout << '\n' << name << " esta programando el codigo..." << " en lenguaje " << habilidad; 
    };

    void agregar_empleados(string info="Error") {
        cout << "\nEl programador no puede agregar empleados...";
    }
};

int main() {
    Perro perro("Zeus");
    Gato gato("Adonis");

    perro.sonido();
    gato.sonido();

    cout << '\n';

    // ************ Prueba Ejercicio Dificultad Extra ************ //
    
    Gerente gerente("MouroDev", 1);

    gerente.agregar_empleados("NinoTv");
    gerente.agregar_empleados("AFK Programming");
    gerente.cordinar_proyectos();
    gerente.mostrarEmpreados();
    cout << '\n';
    
    Gerente_de_Proyectos gerente_de_proyectos("Javier", 1);
    
    gerente_de_proyectos.agregar_empleados("Nasha DEV");
    gerente_de_proyectos.cordinar_proyecto();
    gerente_de_proyectos.mostrarEmpreados();
    cout << '\n';
    
    Programador programador("Francisco", 1, "C++");
    
    programador.agregar_empleados("Minecraft Delevoper");
    programador.codeando();
    programador.mostrarEmpreados();
    cout << '\n';

    return 0;
}