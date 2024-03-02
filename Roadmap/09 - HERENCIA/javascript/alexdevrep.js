/*
 * EJERCICIO:
 * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
 * implemente una superclase Animal y un par de subclases Perro y Gato,
 * junto con una función que sirva para imprimir el sonido que emite cada Animal.
 *
 * DIFICULTAD EXTRA (opcional):
 * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 * actividad, y almacenan los empleados a su cargo.
 */

class Animal{
    constructor(nombre){
        this.nombre=nombre
    }
}

class Perro extends Animal{
   constructor(nombre,sonido){
    super(nombre)
    this.sonido=sonido
   }
   ladrar(){
    return `${this.nombre} está ${this.sonido}`
   }
}

class Gato extends Animal { //Extends palabra reservada para indicar de la clase que se hereda
    constructor(nombre,sonido){
        super(nombre) //Ejecutamos el constructor de la clase que heredamos
        this.sonido=sonido
    }
    maullar(){
        return `${this.nombre} está ${this.sonido}`
    }
}

//Instanciamos los objetos
const mi_perro= new Perro('Kinder','ladrando') //New palabra reservada para crear objetos de una clase 
const mi_Gato= new Gato('Manchita','maullando')

//Imprimimos los objetos por pantalla
console.log(mi_perro.ladrar())
console.log(mi_Gato.maullar())

//Dificultad EXTRA

class Empleados{
    constructor(id,nombre,equipo){
        this.id=id
        this.nombre=nombre
        this.equipo=equipo || []
    }
}

class Programador extends Empleados{
    constructor(id,nombre,equipo){
        super(id,nombre,equipo)
    }
    desarrollar(){
        return `${this.nombre} con el ID ${this.id} está desarrollando una aplicación móvil y lleva a cargo a ${this.equipo.length} personas`
    }
}

class Gerente_Proyecto extends Empleados{
    constructor(id,nombre,equipo){
        super(id,nombre,equipo)
    }
    supervisar(){
        return `${this.nombre} con el ID ${this.id} está supervisando que no haya bugs y lleva a cargo a ${this.equipo.length} personas`
    }
}


class Gerente extends Empleados{
    constructor(id,nombre,equipo){
        super(id,nombre,equipo)
    }
    dirigir(){
        return `${this.nombre} con el ID ${this.id} está decidiendo que característica añadir a la aplicación y lleva a cargo a ${this.equipo.length} personas`
    }
}

const programador1= new Programador('1','Alexdevrep',[])
const programador2= new Programador('1','Carlos',[])
const gerente_proyecto1= new Gerente_Proyecto('3','Brais',[programador1,programador2])
const gerente1=new Gerente('4','MoureDev',[gerente_proyecto1])

console.log(programador1.desarrollar())
console.log(programador2.desarrollar())
console.log(gerente_proyecto1.supervisar())
console.log(gerente1.dirigir())