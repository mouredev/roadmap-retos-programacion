//PILAS

let pila = ["Marea", "León", "Roberto"];
console.log(pila);

pila.push("Maria");
console.log(pila);

pila.pop();
console.log(pila);

//COLAS

let cola = [1, 2, 3];
console.log(cola);

cola.push(4);
console.log(cola);

cola.shift();
console.log(cola);


//EXTRA

class NavegadorWeb {
    constructor() {
        this.historial = []; //Array vacío que almacenará las urls
        this.indiceActual = -1; // indica la posición en el historial, se establece en -1 por que todavía no hemos visitado nada.
    }

    navegar(url) {
        if (this.indiceActual < this.historial.length - 1) { // Verificamos si el usuario ha retrocedido en el historial y luego navegado a una nueva página. Si es así, eliminamos todas las páginas futuras del historial.
            this.historial.splice(this.indiceActual + 1);
        }
        this.historial.push(url); //Añade la url visitada al historial
        this.indiceActual ++;
        console.log("Navegando a:", url);
    }

    retroceder() {
        if (this.indiceActual > 0) { // verificamos si hay páginas anteriores en el historial.
            this.indiceActual--; // si hay paginas para retroceder se decrementa el indiceActual
            console.log("Navegando hacia atrás a:", this.historial[this.indiceActual]);
        } else {
            console.log("No hay páginas disponibles para retroceder.");
        }
    }

    avanzar() {
        if (this.indiceActual < this.historial.legth - 1) { //Verificamos si hay páginas disponibles después de la página actual en el historial
            this.indiceActual++; // si las hay, incrementamos y accedemos a la pag correspondiente en el historial y mostramos mensaje.
            console.log("Navegando hacia adelante a:", this.historial[this.indiceActual]);
        } else {
            console.log("No hay páginas disponibles para avanzar.");
        }
    }
}

const navegador = new NavegadorWeb();
navegador.navegar("www.google.com");
navegador.navegar("www.twitter.com");
navegador.retroceder();
navegador.avanzar();


class Impresora {
    constructor () {
        this.cola = [];
    }

    añadirDocumento(documento) {
        this.cola.push(documento);
    }

    imprimir() {
        if (this.cola.length > 0) {
            const documento = this.cola.shift();
            console.log(`Imprimiendo documento: ${documento}`);
        } else {
            console.log("No hay nada que imprimir");
        }
    }
}

const impresoraCompartida = new Impresora();

impresoraCompartida.añadirDocumento("Documento 1");
impresoraCompartida.añadirDocumento("Documento 2");

impresoraCompartida.imprimir();
impresoraCompartida.imprimir();
impresoraCompartida.imprimir();
