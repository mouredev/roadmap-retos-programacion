/*
 * EJERCICIO:
 * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
 * atributos y una función que los imprima (teniendo en cuenta las posibilidades
 * de tu lenguaje).
 * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
 * utilizando su función.
 * 
 */

 class programador {

    constructor (name,age,languages){
        this.name = name;
        this.age = age;
        this.languages =languages;
    }
     
    contenido(){
        console.log(`Hola, mi nombre es ${this.name} y tengo ${this.age} años. y programo en estos lenguajes: ${this.languages.join(", ")}`)
    }
    
 }

 let newProgramer = new programador('julian',36,['java','Python','solidity']);
 newProgramer.contenido();



newProgramer.age = 34;
newProgramer.contenido();

newProgramer.name = 'JuliusCañas';
newProgramer.contenido();


 /*
 *  DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido.
 */
 const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

class Pila {  // Capitaliza el nombre de la clase
  constructor() {
    this.elementos = [];
  }

  push(elemento) {
    this.elementos.push(elemento);
  }

  pop() {
    if (this.elementos.length === 0) {
      console.log('La pila está vacía');
      return null;
    }
    return this.elementos.pop();
  }

  shift() {
    if (this.elementos.length === 0) {
      console.log('La pila está vacía');
      return null;  // Agregar retorno nulo para mantener consistencia
    }
    return this.elementos.shift();
  }

  mostrarElemento() {
    if (this.elementos.length === 0) {
      console.log('La pila está vacía');
    } else {
      console.log(['Los elementos son:', this.elementos]);
    }
  }
}

let miPila = new Pila();  // Crear instancia de la clase

let principalClass = () => {
  rl.question('Ingrese el elemento que desea guardar: ', (elementoG) => {
    let numeroElemento = miPila.elementos.length + 1;
    miPila.push({ numero: numeroElemento, elementoGuardado: elementoG });

    miPila.elementos.forEach(numero => {
      console.log([`${numero.numero}. ${numero.elementoGuardado}`]);
    });

    entrada();
  });
};

let entrada = () => {
  rl.question('Ingrese ENTRAR para guardar los elementos, SALIR para salir del programa, IMPRIMIR para mostrar los elementos en consola, ELIMINAR para eliminar elementos: ', (instruccion) => {
    if (instruccion === 'ENTRAR') {
      principalClass();
    } else if (instruccion === 'IMPRIMIR') {
      miPila.mostrarElemento();
      entrada();
    } else if (instruccion === 'SALIR') {
      console.log('Saliendo del programa');
      rl.close();
    } else if (instruccion === 'ELIMINAR') {  // Corrige el espacio extra
      let eliminarUltimo = miPila.pop();
      if (eliminarUltimo) {
        console.log('El último elemento eliminado es:', eliminarUltimo);
      }

      let eliminarPrimero = miPila.shift();
      if (eliminarPrimero) {
        console.log('El primer elemento eliminado es:', eliminarPrimero);
      }

      entrada();  // Reingresar al menú después de eliminar elementos
    } else {
      console.log('Ingrese una instrucción válida');
      entrada();
    }
  });
};

entrada();
