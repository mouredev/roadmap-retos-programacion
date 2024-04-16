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
 */

//Las clases son funciones "especiales", su sintaxis tiene dos componentes: expresiones de clase y declaraciones de clase

//Declaramos una clase en JavaScript

 class ejemplo {
    //Inicializamos la clase con el método constructor
    constructor(cadena1,cadena2){ 
        //Estos son los atributos de la clase
        this.saludo = cadena1  
        this.nombre = cadena2


    }
    //Esta es la función que va a imprimir los atributos de la clase tambien llamado método
    saludar(){ 
        return this.saludo + "," + this.nombre
    }

}

//Creamos instancias de la clase ejemplo con parámetros diferentes
const hola = new ejemplo("Hola","JavaScript") 


//Imprimimos por pantalla el contenido de la clase
console.log(hola.saludar()) 

//Tambien podemos modificar los atributos de la clase
hola.nombre= "Alexdevrep"

//Imprimimos el resultado nuevamente
console.log(hola.saludar())


//Dificultad EXTRA
//Pila
class Pila {
    constructor() {
        this.elementos = [];
    }

    añadir(objeto) {
        this.elementos.push(objeto);
    }

    eliminar() {
        if (this.elementos.length === 0) {
            console.log("La pila está vacía");
            return;
        }
        return this.elementos.pop();
    }

    imprimirTodo() {
        if (this.elementos.length === 0) {
            console.log("La pila está vacía");
            return;
        }
        console.log("Contenido de la pila: ");
        this.elementos.forEach(function(objeto, index) {
            console.log(`${index + 1}.${objeto}`);
        });
    }

    numeroElementos() {
        return this.elementos.length;  // Corregido para retornar el número de elementos
    }
}

// Creamos la instancia de la clase
const pilaObjetos = new Pila();

// Añadimos elementos a la pila
pilaObjetos.añadir("Objeto 1");
pilaObjetos.añadir("Objeto 2");
pilaObjetos.añadir("Objeto 3");

// Imprimimos el contenido de la pila
pilaObjetos.imprimirTodo();

// Eliminamos el último elemento de la pila en entrar
pilaObjetos.eliminar();

// Imprimimos de nuevo la pila para comprobar que ha pasado
pilaObjetos.imprimirTodo();

// Obtenemos el numero de elementos de la Pila
const cantidadElementos = pilaObjetos.numeroElementos();
console.log(`Número de elementos en la pila: ${cantidadElementos}`);

//Cola
class cola {
    constructor(){
        this.cola = []
    }
    insertar(cadena){
        this.cola.push(cadena)

    }
    borrar(){
        if(this.cola.length===0){
            console.log("La cola está vacía")
            return
        }
        return this.cola.shift()
    }
    imprimirCola(){
        if (this.cola.length===0){
            console.log("La cola está vacía")
            return 
        
        }
        console.log("Contenido de la cola:")
        this.cola.forEach(function(cadena,index){
            console.log(`${index +1}.${cadena}`)
        })
    }
    objetosEnCola(){
        return this.cola.length
    }
}

const colaObjetos = new cola()

colaObjetos.insertar("Objeto1")
colaObjetos.insertar("Objeto2")
colaObjetos.insertar("Objeto3")

colaObjetos.imprimirCola()

colaObjetos.borrar()//Borramos el primer elemento insertado en la cola

colaObjetos.imprimirCola()

const cantidadObjetos = colaObjetos.objetosEnCola()
console.log(`Número de elementos en la pila: ${cantidadObjetos}`);





