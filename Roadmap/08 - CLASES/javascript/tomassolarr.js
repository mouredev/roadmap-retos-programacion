/*
 * EJERCICIO:
 * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
 * atributos y una función que los imprima (teniendo en cuenta las posibilidades
 * de tu lenguaje).
 * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
 * utilizando su función.
 */

class Estudiante{
    constructor(nombre, apellido, telefono){
        this.nombre=nombre;
        this.apellido=apellido;
        this.telefonos=telefono
    }
    mostrarDatos() {
        console.log(`
        Nombre: ${this.nombre}
        Apellido: ${this.apellido}
        Teléfono: ${this.telefono}
        `);
    }
}

class Colegio {

    constructor(nombreColegio) {

        this.nombreColegio = nombreColegio;
        this.estudiantes = [];
    }

    agregarPersona(estudiante) {

        this.estudiantes.push(estudiante);

    }

    mostrarPersonas() {

        console.log(`
        Colegio: ${this.nombreColegio}
        `); 
        this.estudiantes.forEach(estudiante => {
            estudiante.mostrarDatos();
        });
    }
}

const persona1 = new Estudiante(
    "Tomás",
    "Solar",
    "123456789"
);

const persona2 = new Estudiante(
    "Ana",
    "Pérez",
    "987654321"
);

const colegio = new Colegio(
    "Instituto Nacional"
);

colegio.agregarPersona(persona1);
colegio.agregarPersona(persona2);

colegio.mostrarPersonas();


 /* DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido.
 * 
 */

class Pila{
    constructor(){
        this.elemento=[]
    }
    agregar(item){
        this.elemento.push(item)
    }
    eliminar(){
        this.elemento.pop()
    }
    mostrar(){
        return this.elemento
    }

}
const pila= new Pila;

pila.agregar(1)
pila.agregar(2)
pila.agregar(3)
console.log(pila.mostrar())

pila.eliminar()

console.log(pila.mostrar())

class Cola{
    constructor(){
        this.elemento=[]
    }
    agregar(item){
        this.elemento.push(item)
    }
    eliminar(){
        this.elemento.shift()
    }
    mostrar(){
        return this.elemento
    }
}

const cola= new Cola;

cola.agregar(1)
cola.agregar(2)
cola.agregar(3)
console.log(cola.mostrar())

cola.eliminar()

console.log(cola.mostrar())