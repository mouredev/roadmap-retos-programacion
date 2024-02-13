/*
 * EJERCICIO:
 * Implementa los mecanismos de introducción y recuperación de elementos propios de las
 * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
 * o lista (dependiendo de las posibilidades de tu lenguaje).
 *
 * DIFICULTAD EXTRA (opcional):
 * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
 *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
 *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
 *   Las palabras "adelante", "atras" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
 * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos.
 */

/************************ PARTE 1 ************************/

/***** PILAS *****/
/*
Una PILA es una estructura de datos que almacena datos en una secuencia. Solo hay una forma para alegrar elementos y estos se incorportanen un orden determinado. Operan bajo la modalidad llamada LIFO, es decir, siempre el último elemento agregado va a ser el primero que saquemos. 
Un ejemplo de pila es el historial del navegador, donde podemos ver que cada página que visitamos se monta encima de la anterior. Esto genera una pila de registros, y podemos volver a ella dando click al botón de "Volver" del navegador.
*/
/****************/

class Pila {

    constructor() {
        this.pila = [];
    }

    push(elemento) {
        this.pila.push(elemento);
    }

    pop() {
        this.pila.pop();
    }

    peek(){
        return this.pila[this.pila.length - 1]
    }

    size() {
        return this.pila.length
    }

    print() {
        return this.pila
    }

}

const ejemploPila = new Pila();

console.log(`Al inicio, la pila está vacía por lo que el size() devolverá 0: ${ejemploPila.size()}`);

for (let i = 0; i < 5; i++) {
    ejemploPila.push(i);
}

console.log(`Luego del push, la pila tiene ${ejemploPila.size()} elementos, que son: ${ejemploPila.print()}`);
console.log(`El peek o primer elemento de la pila es: ${ejemploPila.peek()}. Recuerda que este es el último elemento agregado a la pila.`);

ejemploPila.pop();

console.log(`Luego del pop, la pila tiene ${ejemploPila.size()} elementos, que son: ${ejemploPila.print()}. Su peek ahora es ${ejemploPila.peek()}`);

