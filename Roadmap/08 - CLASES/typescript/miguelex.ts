class Vehiculo {
    nombre: string;
    numRuedas: number;

    constructor(nombre: string, numRuedas: number) {
        this.nombre = nombre;
        this.numRuedas = numRuedas;
    }

    toString(): string {
        return `Nombre: ${this.nombre}, Ruedas: ${this.numRuedas}`;
    }
}

let coche = new Vehiculo("Coche", 4);
let bicicleta = new Vehiculo("Bicicleta", 2);

console.log(coche.toString());
console.log(bicicleta.toString());

class Pila {
    pila: any[];

    constructor() {
        this.pila = [];
    }

    push(elemento: any): void {
        this.pila.push(elemento);
    }

    pop(): any {
        return this.pila.pop();
    }

    toString(): string {
        return this.pila.toString();
    }

    size(): number {
        return this.pila.length;
    }
}

class Cola {
    cola: any[];

    constructor() {
        this.cola = [];
    }

    push(elemento: any): void {
        this.cola.push(elemento);
    }

    pop(): any {
        return this.cola.shift();
    }

    toString(): string {
        return this.cola.toString();
    }

    size(): number {
        return this.cola.length;
    }
}

let pila = new Pila();

console.log("Ejemplo de pila");

pila.push(1);
pila.push(2);
pila.push(3);
console.log("Contendido de la pila: " + pila.toString());
console.log("Extraigo en elemento que esta en la cima: " + pila.pop());
console.log("Contendido de la pila: " + pila.toString());
console.log("Tamaño de la pila: " + pila.size());

let cola = new Cola();

console.log("Ejemplo de cola");

cola.push(1);
cola.push(2);
cola.push(3);

console.log("Contendido de la cola: " + cola.toString());
console.log("Extraigo el primer elemento de la cola: " + cola.pop());
console.log("Contendido de la cola: " + cola.toString());
console.log("Tamaño de la cola: " + cola.size());
