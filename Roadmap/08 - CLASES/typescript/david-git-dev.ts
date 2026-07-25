/*
  EJERCICIO:
  Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
  atributos y una función que los imprima (teniendo en cuenta las posibilidades
  de tu lenguaje).
  Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
  utilizando su función.
  */
class Ventilador {
  private velocidad: number = 0;
  private encendido: boolean = false;
  constructor() {
    this.encendido = true;
  }
  subir() {
    this.velocidad += 1;
  }
  bajar() {
    if (this.velocidad > 0) this.velocidad -= 1;
  }
  encenderApagar(): boolean {
    return (this.encendido = !this.encendido);
  }
  estado(): {} {
    return { staus: this.encendido, velocidad: this.velocidad };
  }
}
const ventilador = new Ventilador();
ventilador.estado();
ventilador.encenderApagar();
ventilador.subir();
ventilador.subir();
ventilador.subir();
ventilador.estado();
ventilador.bajar();
ventilador.estado();
ventilador.encenderApagar();
ventilador.estado();
ventilador.encenderApagar();
ventilador.estado();
/*
 * DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido.
 */
class Stack {
  private stack: any[] = [];
  constructor(stack: any[] = []) {
    this.stack = stack;
  }
  agregar(value: any) {
    this.stack.push(value);
  }
  eliminar() {
    return this.stack.pop();
  }
  get getLength() {
    return this.stack.length;
  }
  get content() {
    return this.stack;
  }
}
const stack = new Stack([1, 2, 3, 4]);
stack.agregar(999);
stack.getLength;
stack.eliminar();
stack.content;
