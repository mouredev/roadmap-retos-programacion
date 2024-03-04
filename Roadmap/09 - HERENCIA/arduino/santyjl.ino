/*
 * EJERCICIO:
 * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
 * implemente una superclase Animal y un par de subclases Perro y Gato,
 * junto con una función que sirva para imprimir el sonido que emite cada Animal.
 *
 * DIFICULTAD EXTRA (opcional):
 * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 * actividad, y almacenan los empleados a su cargo.
 */

// Clase base para representar un Animal
class Animal {
public:
    // Constructor que recibe el nombre del animal
    Animal(const char* nombre) : nombre(nombre) {}

    // Función virtual pura para obtener el sonido del animal
    virtual void sonido() const = 0;

protected:
    const char* nombre;  // Nombre del animal
};

// Clase derivada Perro que hereda de la clase Animal
class Perro : public Animal {
public:
    // Constructor que llama al constructor de la clase base con el nombre del perro
    Perro(const char* nombre) : Animal(nombre) {}

    // Implementación de la función virtual para obtener el sonido del perro
    void sonido() const override {
        Serial.print("El perro ");
        Serial.print(nombre);
        Serial.println(" hace guau");
    }
};

// Clase derivada Gato que hereda de la clase Animal
class Gato : public Animal {
public:
    // Constructor que llama al constructor de la clase base con el nombre del gato
    Gato(const char* nombre) : Animal(nombre) {}

    // Implementación de la función virtual para obtener el sonido del gato
    void sonido() const override {
        Serial.print("El gato ");
        Serial.print(nombre);
        Serial.println(" hace miau");
    }
};



// Clase base para representar un Empleado
class Empleado {
public:
    // Constructor que recibe el nombre y la edad del empleado
    Empleado(const char* nombre, int edad) : nombre(nombre), edad(edad) {}

    // Función virtual pura para deber
    virtual void deber() const = 0;

    // Función virtual pura para obtener el sueldo
    virtual void sueldo() const = 0;

    // Función para obtener una representación en cadena del empleado
    virtual const char* toString() const {
        return "";
    }

protected:
    const char* nombre;  // Nombre del empleado
    int edad;            // Edad del empleado
};

// Clase derivada Gerente que hereda de la clase Empleado
class Gerente : public Empleado {
public:
    // Constructor que llama al constructor de la clase base y recibe información adicional
    Gerente(const char* nombre, int edad, const char** empleados, int salario)
        : Empleado(nombre, edad), empleados(empleados), salario(salario) {}

    // Implementación de la función para deber
    void deber() const override {
        // Imprimir deber específico del Gerente
        Serial.print("El gerente tiene el deber de manejar, controlar y planificar el trabajo de sus empleados que son: ");
        for (int i = 0; empleados[i] != NULL; ++i) {
            Serial.print(empleados[i]);
            if (empleados[i + 1] != NULL) {
                Serial.print(", ");
            }
        }
        Serial.println();
    }

    // Implementación de la función para obtener el sueldo
    void sueldo() const override {
        Serial.print("El gerente tiene un sueldo de ");
        Serial.print(salario);
        Serial.println("$.");
    }

    // Implementación de la función para obtener una representación en cadena del gerente
    const char* toString() const override {
        return "Gerente";
    }

private:
    const char** empleados;  // Arreglo de empleados a cargo
    int salario;            // Salario del gerente
};

// Clase derivada GerenteDeProyecto que hereda de la clase Empleado
class GerenteDeProyecto : public Empleado {
public:
    // Constructor que llama al constructor de la clase base y recibe información adicional
    GerenteDeProyecto(const char* nombre, int edad, const char** proyectos)
        : Empleado(nombre, edad), proyectos(proyectos) {}

    // Implementación de la función para deber
    void deber() const override {
        // Imprimir deber específico del Gerente de Proyecto
        Serial.print("El Gerente de Proyecto tiene el deber de supervisar y coordinar proyectos como: ");
        for (int i = 0; proyectos[i] != NULL; ++i) {
            Serial.print(proyectos[i]);
            if (proyectos[i + 1] != NULL) {
                Serial.print(", ");
            }
        }
        Serial.println();
    }

    // Implementación de la función para obtener el sueldo
    void sueldo() const override {
        Serial.println("El sueldo del Gerente de Proyecto depende del éxito de los proyectos.");
    }

    // Implementación de la función para obtener una representación en cadena del gerente de proyecto
    const char* toString() const override {
        return "Gerente de Proyecto";
    }

private:
    const char** proyectos;  // Arreglo de proyectos supervisados
};

// Clase derivada Programador que hereda de la clase Empleado
class Programador : public Empleado {
public:
    // Constructor que llama al constructor de la clase base y recibe información adicional
    Programador(const char* nombre, int edad, const char** lenguajes)
        : Empleado(nombre, edad), lenguajes(lenguajes) {}

    // Implementación de la función para deber
    void deber() const override {
        // Imprimir deber específico del Programador
        Serial.print("El Programador tiene el deber de desarrollar software utilizando los siguientes lenguajes: ");
        for (int i = 0; lenguajes[i] != NULL; ++i) {
            Serial.print(lenguajes[i]);
            if (lenguajes[i + 1] != NULL) {
                Serial.print(", ");
            }
        }
        Serial.println();
    }

    // Implementación de la función para obtener el sueldo
    void sueldo() const override {
        Serial.println("El sueldo del Programador se basa en su experiencia y habilidades técnicas.");
    }

    // Implementación de la función para obtener una representación en cadena del programador
    const char* toString() const override {
        return "Programador";
    }

private:
    const char** lenguajes;  // Arreglo de lenguajes de programación utilizados
};


// Función de inicialización de Arduino
void setup() {
    Serial.begin(9600);  // Iniciar comunicación serial

    // Crear instancias de las clases y llamar a la función sonido
    Perro perro("Gaston");
    perro.sonido();

    Gato gato("Cachito");
    gato.sonido();

    //llamado al extra
    // Crear instancias de las clases Empleado, Gerente, GerenteDeProyecto y Programador
    const char* empleadosGerente[] = {"Fernando", "Cesar", NULL}; // null para señalar el final del conjunto
    Gerente gerente("Julian", 38, empleadosGerente, 6000);
    Serial.println(gerente.toString());
    gerente.deber();
    gerente.sueldo();

    const char* proyectosGerenteProyecto[] = {"Proyecto A", "Proyecto B", NULL};
    GerenteDeProyecto gerente_proyecto("Ana", 32, proyectosGerenteProyecto);
    Serial.println(gerente_proyecto.toString());
    gerente_proyecto.deber();
    gerente_proyecto.sueldo();

    const char* lenguajesProgramador[] = {"Python", "JavaScript", NULL};
    Programador programador("Carlos", 25, lenguajesProgramador);
    Serial.println(programador.toString());
    programador.deber();
    programador.sueldo();

}
void loop() {
    // Código que se ejecuta en bucle continuo
}


// Extra
// Resto del código para la jerarquía de empleados

// Extra
// Resto del código para la jerarquía de empleados
