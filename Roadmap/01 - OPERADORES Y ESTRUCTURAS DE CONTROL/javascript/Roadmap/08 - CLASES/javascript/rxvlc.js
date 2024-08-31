// Definición de la clase MiClase
class MiClase {
    // Constructor de la clase MiClase
    constructor(nombre, edad) {
        this.nombre = nombre;
        this.edad = edad;
    }

    // Método para incrementar la edad
    CumplirAnyos() {
        this.edad++;
    }

    // Método para devolver información sobre la instancia de la clase
    VerInfo() {
        return `${this.nombre},${this.edad}`;
    }

    // Método toString para representación de cadena
    toString() {
        return `${this.nombre},${this.edad}`;
    }
}

// Definición de la clase Pila
class Pila {
    // Constructor de la clase Pila
    constructor() {
        this.elementos = [];
    }

    // Método para agregar un elemento a la pila
    Push(elemento) {
        this.elementos.push(elemento);
    }

    // Método para quitar y devolver el elemento superior de la pila
    Pop() {
        return this.elementos.pop();
    }

    // Método para obtener la cantidad de elementos en la pila
    Count() {
        return this.elementos.length;
    }

    // Método para imprimir el contenido de la pila
    Imprimir() {
        console.log("Contenido de la pila:");
        this.elementos.forEach(elemento => {
            console.log(elemento);
        });
    }
}

// Definición de la clase Cola
class Cola {
    // Constructor de la clase Cola
    constructor() {
        this.elementos = [];
    }

    // Método para agregar un elemento a la cola
    Enqueue(elemento) {
        this.elementos.push(elemento);
    }

    // Método para quitar y devolver el primer elemento de la cola
    Dequeue() {
        return this.elementos.shift();
    }

    // Método para obtener la cantidad de elementos en la cola
    Count() {
        return this.elementos.length;
    }

    // Método para imprimir el contenido de la cola
    Imprimir() {
        console.log("Contenido de la cola:");
        this.elementos.forEach(elemento => {
            console.log(elemento);
        });
    }
}

// Creación de una instancia de la clase MiClase
let objeto = new MiClase("Juan", 30);
console.log("Valores iniciales:");
console.log(objeto.toString());
objeto.nombre = "Pedro";
console.log("Valores modificados:");
console.log(objeto.toString());

// Ejemplo de uso de la clase Pila
let pila = new Pila();
pila.Push(1);
pila.Push(2);
pila.Push(3);
pila.Imprimir();
console.log("Número de elementos en la pila: " + pila.Count());
pila.Pop();
pila.Imprimir();
console.log("Número de elementos en la pila: " + pila.Count());

// Ejemplo de uso de la clase Cola
let cola = new Cola();
cola.Enqueue("Uno");
cola.Enqueue("Dos");
cola.Enqueue("Tres");
cola.Imprimir();
console.log("Número de elementos en la cola: " + cola.Count());
cola.Dequeue();
cola.Imprimir();
console.log("Número de elementos en la cola: " + cola.Count());
