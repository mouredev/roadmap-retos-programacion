// En JS estas estructuras no existen cómo tal, las debemos emular, por equivalencia sería como un ArrayList en c#:
const pila = [];

// Agregar elementos a la pila
pila.push(1);
pila.push(2);
pila.push(3);

// Eliminar el elemento superior de la pila
const elementoEliminadoPila = pila.pop(); // Eliminará 3 de la pila
console.log(elementoEliminadoPila); // Salida: 3

const cola = [];

// Agregar elementos a la cola
cola.push(1);
cola.push(2);
cola.push(3);

// Eliminar el primer elemento de la cola
const elementoEliminadoCola = cola.shift(); // Eliminará 1 de la cola
console.log(elementoEliminadoCola); // Salida: 1

//Dificultad adicional, hecha introduciendo los elementos automáticamente debido a que JS de consola no tiene método de entrada de teclado sin librerías:
class NavegadorWeb {
    constructor() {
        this.historial = [];
        this.indiceActual = -1;
    }

    navegar(pagina) {
        // Eliminar las páginas futuras al navegar a una nueva página
        this.historial = this.historial.slice(0, this.indiceActual + 1);
        
        // Agregar la nueva página al historial
        this.historial.push(pagina);
        
        // Incrementar el índice actual
        this.indiceActual++;
        
        console.log(`Navegando a: ${pagina}`);
    }

    retroceder() {
        if (this.indiceActual > 0) {
            this.indiceActual--;
            console.log(`Retrocediendo a: ${this.historial[this.indiceActual]}`);
        } else {
            console.log("No hay páginas anteriores para retroceder.");
        }
    }

    avanzar() {
        if (this.indiceActual < this.historial.length - 1) {
            this.indiceActual++;
            console.log(`Avanzando a: ${this.historial[this.indiceActual]}`);
        } else {
            console.log("No hay páginas siguientes para avanzar.");
        }
    }
}

const navegador = new NavegadorWeb();

// Ejemplo de uso
console.log();
console.log("Navegador: ");
navegador.navegar("https://www.google.com");
navegador.navegar("https://www.wikipedia.org");
navegador.navegar("https://www.openai.com");

// Retroceder una página
navegador.retroceder(); // Retrocediendo a: https://www.wikipedia.org

// Retroceder otra página
navegador.retroceder(); // Retrocediendo a: https://www.google.com

// Avanzar una página
navegador.avanzar(); // Avanzando a: https://www.wikipedia.org

// Navegar a una nueva página
navegador.navegar("https://www.github.com");

//Dificultad adicional impresora:
console.log();
console.log("Impresora: ");
class ImpresoraCompartida {
    constructor() {
        this.documentos = [];
    }

    agregarDocumento(documento) {
        this.documentos.push(documento);
        console.log(`Documento '${documento}' agregado a la cola de impresión.`);
    }

    imprimir() {
        if (this.documentos.length > 0) {
            const documento = this.documentos.shift();
            console.log(`Imprimiendo documento: ${documento}`);
        } else {
            console.log("No hay documentos en la cola de impresión.");
        }
    }

    mostrarCola() {
        console.log("Documentos en la cola de impresión:");
        this.documentos.forEach((documento, index) => {
            console.log(`${index + 1}. ${documento}`);
        });
    }
}

const impresora = new ImpresoraCompartida();

// Ejemplo de uso
impresora.agregarDocumento("Documento1.txt");
impresora.agregarDocumento("Documento2.txt");
impresora.agregarDocumento("Documento3.txt");

// Imprimir un documento
impresora.imprimir(); // Imprimiendo documento: Documento1.txt

// Mostrar la cola de impresión actual
impresora.mostrarCola();