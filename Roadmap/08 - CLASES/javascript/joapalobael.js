/* Clase */

class Persona {
    // Constructor
    constructor(nombre, apellido, edad) {
        this.nombre = nombre;
        this.apellido = apellido;
        this.edad = edad;
    }
    // Métodos
    saludar (){
        console.log (`${this.nombre} ${this.apellido} tiene ${this.edad} años.`);
    }

}

let persona1 = new Persona ("Alan", "Martinez", 65);
persona1.saludar();

/* DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido.
 * 
 */

/*Pila*/
class SesionChrome{
    //Constructor
    constructor(){
        this.navegador = ["Inicio"] //Inicia lista
    }
    //LI (Push)
    adelante (web){
        this.navegador.push(web);
        console.log(this.navegador);
    }
    //FO (POP)
    atras(){
        if (this.navegador.length <= 1) {
            console.log("Hasta aquí llegaste");
        } else {
            this.navegador.pop();
            console.log(this.navegador);
        }
    }
    cantidadSitios(){
        if (this.navegador.length <= 1) {
            console.log(`Estas en el inicio`);
        } else {
            console.log(`Estas a ${this.navegador.length} webs del inicio`);
        }
    }
    listaDeSitios(){
        console.log(this.navegador);
    }
}

let user1 = new SesionChrome();
user1.adelante("Instragram");
user1.adelante("Facebook");
user1.atras();
user1.cantidadSitios();
user1.listaDeSitios();

/*Cola*/
class Impresion {
    constructor(){
        this.colaImpresion = [];
    }
    //FI (push)
    agregar(archivo){
        this.colaImpresion.push(archivo);
    }
    //FO (shift)
    imprimir(){
         if (this.colaImpresion.length <=0) {
            console.log("No hay archivos para imprimir");
         } else {
            let archivoImpreso = this.colaImpresion.shift();
            console.log(`El archivo "${archivoImpreso}" fue impreso y luego se eliminó de la cola`);
         }
    }
    mostrarCola(){
        console.log(this.colaImpresion);
    }
    cantidadCola(){
        console.log(`Hay ${this.colaImpresion.length} archivos en cola.`);
    }

}

let cola1 = new Impresion;
cola1.agregar("notas");
cola1.agregar("boletín");
cola1.mostrarCola();
cola1.imprimir();
cola1.cantidadCola();
cola1.imprimir();
cola1.cantidadCola();