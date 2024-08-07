class Vehiculo {
    constructor(nombre, numRuedas){
        this.nombre = nombre;
        this.numRuedas = numRuedas;
    }

    toString(){
        return "Nombre: " + this.nombre + ", Ruedas: " + this.numRuedas;
    }
}

let coche = new Vehiculo("Coche", 4);
let bicicleta = new Vehiculo("Bicicleta", 2);

console.log(coche.toString());
console.log(bicicleta.toString());

class Pila {
    constructor(){
        this.pila = [];
    }

    push(elemento){
        this.pila.push(elemento);
    }

    pop(){
        return this.pila.pop();
    }

    toString(){
        return this.pila.toString();
    }

    size(){
        return this.pila.length;
    }
}

class Cola {
    constructor(){
        this.cola = [];
    }

    push(elemento){
        this.cola.push(elemento);
    }

    pop(){
        return this.cola.shift();
    }

    toString(){
        return this.cola.toString();
    }

    size(){
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
