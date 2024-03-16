class song {
    constructor(titulo, artista, duracion) { //Inicialización
        this.titulo = titulo;
        this.artista = artista;
        this.duracion = duracion;
    }

    imprimir() { //Impresión
        console.log(`Título: ${this.titulo}`);
        console.log(`Artista: ${this.artista}`);
        console.log(`Duración: ${this.duracion}`);
    }
}

const song1 = new song("Before the begining", "John Frusciante", 3 + " minutos");
song1.imprimir();

song1.titulo = "La Macarena";
song1.artista = "Los del Río";
song1.duracion = 4 + " min";

song1.imprimir();

//

class pila  {
    constructor () {
        this.pila = [];
    }

    add(elemento) {
        this.pila.push(elemento);
    }

    delete() {
        if (this.pila.length === 0) {
            return "La pila está vacía";
        }
        return this.pila.pop();
    }

    length() {
        return this.pila.length;
    }

    imprimirElementos() {
        for(let i = this.pila.length - 1; i >= 0; i--) {
            console.log(this.pila[i]);
        }
    }
}

const pila1 = new pila();
pila1.add("Ana");
pila1.add("Garcia");
pila1.add(88);

pila1.delete(); // 88 no lo imprime por que borra el último elemento añadido.
pila1.imprimirElementos();


class cola {
    constructor() {
        this.cola = [];
    }

    add1 (numero) {
        this.cola.push (numero);
    }

    delete1 () {
        this.cola.shift();
    }

    imprimirElementos1 () {
        for (let a = 0; a < this.cola.length; a++) {
            console.log(this.cola[a]);
        }
    }
}

const cola1 = new cola();
cola1.add1(1);
cola1.add1(2);
cola1.add1(3);

cola1.imprimirElementos1();
cola1.delete1();
cola1.imprimirElementos1();