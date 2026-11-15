/*
 * EJERCICIO:
 * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
 * atributos y una función que los imprima (teniendo en cuenta las posibilidades
 * de tu lenguaje).
 * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
 * utilizando su función.
 *
 * DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido.
 * 
 */

class Persona {
    constructor(nombre, peso, altura) {
        this.nombre = nombre;
        this.peso = peso;
        this.altura = altura;
    }


    calculoImc() {
        const resultadoCalculoImc = this.peso / (this.altura ** 2)
        return parseFloat(resultadoCalculoImc.toFixed(2));
    }

    obtenerResultado() {
        const valorIMC = this.calculoImc();
        if (valorIMC < 18.5) return `${valorIMC}: Bajo peso`;
        if (valorIMC <= 24.9) return `${valorIMC}: Peso normal`;
        if (valorIMC <= 29.9) return `${valorIMC}: Sobrepeso`;
        return `${valorIMC}: Obesidad`;
    };
};

const paciente1 = new Persona("cristian", 73, 1.80);

console.log(paciente1.obtenerResultado());
paciente1.peso = 77;

console.log(paciente1.obtenerResultado());



/*==========================DESAFÍO ====================================== */



// PILA (lifo)
class PilaPlatos {
    constructor() {
        this.plato = [];
    }

    agregar(plato) {
        this.plato.push(plato);
    }

    limpiar() {
        if (this.plato.length === 0) {
            console.log("no hay platos para lavar.")
            return;
        }
        return this.plato.pop();
    }

    cantidad() {
        return this.plato.length;
    }

    imprimir() {
        console.log(`Pila platos: [${this.plato.join(", ")}]`);
    }
}


// COLA (fifo) 

class FilaCaja {
    constructor() {
        this.cliente = [];
    }

    agregar(cliente) {
        this.cliente.push(cliente);
    }

    atender() {
        if (this.cliente.length === 0) {
            console.log("no hay cliente para atender.")
            return;
        }
        return this.cliente.shift();
    }

    cantidad() {
        return this.cliente.length;
    }

    imprimir() {
        console.log(`Clientes fila: [${this.cliente.join(", ")}]`);
    }
}

// ===== PRUEBA PILA =====
const limpiezaPlatos1 = new PilaPlatos();
limpiezaPlatos1.agregar("plato 1");
limpiezaPlatos1.agregar("plato 2");
limpiezaPlatos1.agregar("plato 3");
limpiezaPlatos1.imprimir();                          // Pila: [plato 1, plato 2, plato 3]
console.log(`Sale: ${limpiezaPlatos1.limpiar()}`);  // Sale: plato 3 (el último en entrar)
console.log(limpiezaPlatos1.cantidad());             // 3
limpiezaPlatos1.imprimir();                          // Pila: [plato 1, plato 2]

// ===== PRUEBA COLA =====
const caja01 = new FilaCaja();
caja01.agregar("cliente 1");
caja01.agregar("cliente 2");
caja01.agregar("cliente 3");
caja01.imprimir();                          // Cola: [cliente 1, cliente 2, cliente 3]
console.log(caja01.cantidad());             // 3
console.log(`Sale: ${caja01.atender()}`);  // Sale: cliente 1 (el primero en entrar)
caja01.imprimir();                          // Cola: [cliente 2, cliente 3]