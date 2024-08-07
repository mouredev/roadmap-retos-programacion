/*
 * EJERCICIO:
 * Implementa los mecanismos de introducción y recuperación de elementos propios de las
 * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
 * o lista (dependiendo de las posibilidades de tu lenguaje).
 */


// PILA (Last In First Out)

class Pila {
    constructor(){
        this.elements = []
    }

    insert (element) {
        this.elements.push(element);
    }

    delete () {
        this.elements.pop();
    }

    peek () {
        return this.elements[this.elements.length-1];
    }

    size () {
        return this.elements.length;
    }

    print () {
        return this.elements;
    }
}

const pila1 = new Pila();

pila1.insert('Naranja');
pila1.insert('Manzana');
pila1.insert('Pera');
console.log(pila1.print()); // ['Naranja', 'Manzana', 'Pera']
console.log(pila1.peek()); // Pera
console.log(pila1.size()); // 3
pila1.delete();
console.log(pila1.print()); // ['Naranja', 'Manzana']


// COLA First In First Out

class Cola {
    constructor(){
        this.elements = []
    }

    insert (element) {
        this.elements.push(element);
    }

    delete () {
        this.elements.shift();
    }

    peek () {
        return this.elements[0];
    }

    size () {
        return this.elements.length;
    }

    print () {
        return this.elements;
    }
}

const cola1 = new Cola();

cola1.insert('Naranja');
cola1.insert('Manzana');
cola1.insert('Pera');
console.log(cola1.print()); // ['Naranja', 'Manzana', 'Pera']
console.log(cola1.peek()); // Naranja
console.log(cola1.size()); // 3
cola1.delete();
console.log(cola1.print()); // ['Manzana', 'Pera']

/*
 * DIFICULTAD EXTRA (opcional):
 * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
 *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
 *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
 *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
 */


class Browser{
    constructor(){
        this.pila = new Pila();
        this.index = -1
    }

    order (element) {
        if (element == 'adelante'){
            if (this.index == this.pila.size()-1){
                return "No puedes avanzar más, estás en la última página"
            }
            else{
                this.index ++; 
                return "Avanzas hasta la página " + this.pila.elements[this.index];
            }
        }
        else if (element == 'atrás'){
            if (this.index == 0){
                return "No puedes retroceder más, no hay más historial"
            }
            else{
                this.index --;
                return "Retrocedes hasta la página " + this.pila.elements[this.index];
            }
        }
        else{
            this.pila.insert(element);
            this.index = this.pila.size()-1;
            return "Navegas hasta la nueva página " + element + " | index:" + this.index;
        }
    }
}

const navegador1 = new Browser();

console.log(navegador1.order('facebook.com'));
console.log(navegador1.order('google.com'));
console.log(navegador1.order('instagram.com'));
console.log(navegador1.order('atrás'));
console.log(navegador1.order('atrás'));
console.log(navegador1.order('adelante'));
console.log(navegador1.order('adelante'));
console.log(navegador1.order('adelante'));
console.log(navegador1.order('adelante'));
console.log(navegador1.order('atrás'));
console.log(navegador1.order('atrás'));
console.log(navegador1.order('youtube.com'));
console.log(navegador1.order('adelante'));
console.log(navegador1.order('atrás'));
console.log(navegador1.order('atrás'));
console.log(navegador1.order('atrás'));
console.log(navegador1.order('atrás'));
console.log(navegador1.order('atrás'));
console.log(navegador1.order('twitter.com'));



/* - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos.
 */

class Impresora{
    constructor(){
        this.cola = new Cola();
    }

    order (element) {
        if (element!='imprimir'){
            this.cola.insert(element);
            return "El documento " + element + " se ha puesto a la cola";
        }
        else{
            let msg = "Se ha impreso el documento " + this.cola.peek();
            this.cola.delete(element);
            return msg
        }
    }
}

const impresora1 = new Impresora();
console.log(impresora1.order('Factura'));
console.log(impresora1.order('Email'));
console.log(impresora1.order('Documento 1'));
console.log(impresora1.order('imprimir'));
console.log(impresora1.order('Documento 2'));
console.log(impresora1.order('imprimir'));