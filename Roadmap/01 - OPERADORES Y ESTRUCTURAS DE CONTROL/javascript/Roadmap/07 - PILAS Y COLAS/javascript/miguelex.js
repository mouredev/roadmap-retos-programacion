class Cola {
    constructor() {
        this.cola = [];
        this.inicio = 0;
        this.fin = 0;
        this.max = 10; // Opcional para limitar el tamaño de la cola
    }

    encolar(elemento) {
        if (this.fin < this.max) {
            this.cola[this.fin] = elemento;
            this.fin++;
        } else {
            console.log("La cola está llena");
        }
    }

    desencolar() {
        if (this.inicio < this.fin) {
            const elemento = this.cola[this.inicio];
            delete this.cola[this.inicio];
            this.inicio++;
            return elemento;
        } else {
            console.log("La cola está vacía");
        }
    }

    mostrar() {
        if (this.inicio === this.fin) {
            console.log("La cola está vacía");
        } else {
            for (let i = this.inicio; i < this.fin; i++) {
                console.log(this.cola[i] + " ");
            }
        }
    }
}

class Pila {
    constructor() {
        this.pila = [];
        this.tope = 0;
        this.max = 7; // Opcional para limitar el tamaño de la pila
    }

    apilar(elemento) {
        if (this.tope < this.max) {
            this.pila[this.tope] = elemento;
            this.tope++;
        } else {
            console.log("La pila está llena");
        }
    }

    desapilar() {
        if (this.tope > 0) {
            this.tope--;
            const elemento = this.pila[this.tope];
            delete this.pila[this.tope];
            return elemento;
        } else {
            console.log("La pila está vacía");
        }
    }

    mostrar() {
        if (this.tope === 0) {
            console.log("La pila está vacía");
        } else {
            for (let i = this.tope - 1; i >= 0; i--) {
                console.log(this.pila[i] + " ");
            }
        }
    }
}

const cola = new Cola();
const pila = new Pila();

console.log("Vamos a trabajar con la cola");
console.log("Vamos a mostrar el contenido de la cola al inicio de la misma: ");
cola.mostrar();

console.log("\nVamos a encolar 3 elementos: 1, 2 y 3");
cola.encolar(1);
cola.encolar(2);
cola.encolar(3);

console.log("Vamos a mostrar el contenido de la cola después de encolar 3 elementos: ");
cola.mostrar();

console.log("\nVamos a desencolar un elemento");
cola.desencolar();

console.log("Vamos a mostrar el contenido de la cola después de desencolar un elemento: ");
cola.mostrar();

console.log("\nVamos a encolar 2 elementos: 4 y 5 y vamos a desencolar dos");
cola.encolar(4);
cola.encolar(5);
cola.desencolar();
cola.desencolar();

console.log("Vamos a mostrar el contenido de la cola después de encolar 2 elementos y desencolar dos: ");
cola.mostrar();

console.log("\nPor último, vamos a desencolar tres elementos (recuerda que realmente solo nos quedan 2 dentro de la cola)");
cola.desencolar();
cola.desencolar();
cola.desencolar();

console.log("Vamos a mostrar el contenido de la cola después de desencolar tres elementos: ");
cola.mostrar();

console.log("\nAhora, vamos a trabajar con la pila");

console.log("Vamos a mostrar el contenido de la pila al inicio de la misma: ");
pila.mostrar();

console.log("\nVamos a apilar 3 elementos: 1, 2 y 3");

pila.apilar(1);
pila.apilar(2);
pila.apilar(3);

console.log("Vamos a mostrar el contenido de la pila después de apilar 3 elementos: ");
pila.mostrar();

console.log("\nVamos a desapilar un elemento");
pila.desapilar();

console.log("Vamos a mostrar el contenido de la pila después de desapilar un elemento: ");
pila.mostrar();

console.log("\nVamos a apilar 2 elementos: 4 y 5 y vamos a desapilar dos");

pila.apilar(4);
pila.apilar(5);

pila.desapilar();
pila.desapilar();

console.log("Vamos a mostrar el contenido de la pila después de apilar 2 elementos y desapilar dos: ");
pila.mostrar();

console.log("\nPor último, vamos a desapilar tres elementos (recuerda que realmente solo nos quedan 2 dentro de la pila)");
pila.desapilar();
pila.desapilar();
pila.desapilar();

console.log("Vamos a mostrar el contenido de la pila después de desapilar tres elementos: ");
pila.mostrar();

console.log("\nVamos a simular el mecanismo adelante/atrás de un navegador web");

const pilaNavegador = new Pila();
let ultimoIndexVisitado = -1;

const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});

function navegacion() {
    const cabeza = pilaNavegador.tope - 1;

    readline.question("Escribe el nombre de la web, adelante, atras o salir: ", (entrada) => {
        if (entrada === "adelante") {
            if (ultimoIndexVisitado < cabeza) {
                ultimoIndexVisitado++;
                console.log("Navegando adelante a la web: " + pilaNavegador.pila[ultimoIndexVisitado]);
            } else {
                console.log("No hay más webs para navegar adelante");
            }
        } else if (entrada === "atras") {
            if (ultimoIndexVisitado > 0) {
                ultimoIndexVisitado--;
                console.log("Navegando atrás a la web: " + pilaNavegador.pila[ultimoIndexVisitado]);
            } else {
                console.log("No hay más webs para navegar atrás");
            }
        } else if (entrada !== "salir") {
            pilaNavegador.apilar(entrada);
            ultimoIndexVisitado = pilaNavegador.tope - 1;
            console.log("Estás en la web: " + entrada);
        }

        if (entrada !== "salir") {
            navegacion();
        } else {
            readline.close();
        }
    });
}

navegacion();

console.log("\nVamos a simular el mecanismo de una cola de impresión");

const colaImpresion = new Cola();

function impresion() {
    readline.question("Escribe el nombre del documento, imprimir o exit: ", (entrada) => {
        if (entrada === "imprimir") {
            const documento = colaImpresion.desencolar();
            if (documento !== undefined) {
                console.log("Imprimiendo documento: " + documento);
            } else {
                console.log("No hay documentos para imprimir");
            }
        } else if (entrada !== "exit") {
            colaImpresion.encolar(entrada);
            console.log("Documento encolado: " + entrada);
        }

        if (entrada !== "exit") {
            impresion();
        } else {
            readline.close();
        }
    });
}

impresion();
