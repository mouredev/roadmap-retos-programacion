

// HERENCIA ============================

/*

En la programación orientada a objetos, la herencia 
es un mecanismo que permite a una clase heredar propiedades 
y métodos de otra clase. En JavaScript ES6, la herencia se 
logra mediante la palabra clave class.

*/

/*
 ⚡  EJERCICIO ===============================
   - Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
   - implemente una superclase Animal y un par de subclases Perro y Gato,
   - junto con una función que sirva para imprimir el sonido que emite cada Animal.
*/


// Super Clase
class Animal {

    name  = 'Animal';
    sound = 'Sound';

    constructor( name,sound ){
        this.name  = name;
        this.sound = sound;
    }

};

//Clases extendida de Animal
class Species extends Animal {

    constructor( name,sound ){
        super( name,sound );
    }

    makeSound(){
        console.log(
            `${this.name} : ${this.sound}`
            );
    }
};

// Instancias de Species
const dog1  = new Species('Dog','Woof,Woof!');
const cat1  = new Species('Cat','Meow,Meow!');
const bird1 = new Species('Bird','Pío,Pío!');

// Muestro en consola
console.log( dog1 );
dog1.makeSound();
console.log( cat1 );
cat1.makeSound();
console.log( bird1 );
bird1.makeSound();



/*

⚡ DIFICULTAD EXTRA (opcional) ===========================
   Implementa la jerarquía de una empresa de desarrollo formada por Empleados que:

   - pueden ser Gerentes, Gerentes de Proyectos o Programadores.
   - Cada empleado tiene un identificador y un nombre.
   - Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
   - actividad, y almacenan los empleados a su cargo.

*/

// ⚡ Super Clase  =========================

class Empleado {

    id;
    nombre;
    empleadosACargo = [];

    constructor( id, nombre,empleadosACargo = [] ) {
        this.id = id;
        this.nombre = nombre;
        this.empleadosACargo = empleadosACargo;
    }

    trabajar(){
        console.log(
            `${this.nombre} Esta trabajando ...`
            );
    }

    verEmpleadosACargo() {
        if (this.empleadosACargo.length === 0) {
          console.log(`${this.nombre} no tiene empleados a cargo.`);
        } else {
          console.log(
            `${this.nombre} tiene empleados a cargo:`);
          this.empleadosACargo.forEach(empleado => {
            console.log(
                `- ${empleado.nombre}`
                );
          });
        }
      }

};


//⚡  Clase Gerente ==========================

class Gerente extends Empleado{

    constructor(Id, nombre,area){
        super(Id, nombre);
        this.area = area;
    }

    asignarTarea(empleado) {

        this.empleadosACargo.push(empleado);

        console.log(
            `${this.nombre} asignó una tarea a ${empleado.nombre}
            en el area de ${this.area}`
            );
    }
};


// ⚡ Clase Gerente de Proyecto ===============

class GerenteProyecto extends Gerente{

    constructor(id, nombre, area, proyecto) {
        super( id,nombre,area );
        this.proyecto = proyecto;
    }
    
    coordinarProyecto() {
        console.log(
            `${this.nombre} está coordinando el proyecto : 
            ${this.proyecto} en el área: ${this.area}`
            );
    }
};


// ⚡ Clase Programador ========================

class Programador extends Empleado {

    constructor(id, nombre, lenguaje) {
      super(id, nombre);
      this.lenguaje = lenguaje;
    }
  
    programar() {
      console.log(
        `${this.nombre} está programando en : 
        ${this.lenguaje}.`
        );
    }
};


// Instancias: 
const gerente1 = new Gerente( 1, 'Artic', 'Programación' );
const programador1 = new Programador( 2, 'Luisa', 'JavaScript' );
const gerenteProyecto1 = new GerenteProyecto(3, 'María', 'Desarrollo', 'Sistema X');


console.log( gerente1 );
console.log( programador1 );
console.log( gerenteProyecto1 );


//Métodos
gerente1.trabajar();      // Salida: Artic está trabajando.
programador1.trabajar();  // Salida: Luisa está trabajando.


//Asignar Tareas con Método
gerente1.asignarTarea( programador1 ); 
// Artic asignó una tarea a Luisa en el area de Programación

//Coordinar Proyecto con Método
gerenteProyecto1.coordinarProyecto();
// Salida: María está coordinando el proyecto : Sistema X en el área: Desarrollo  

//Ver empleados a cargo
gerente1.verEmpleadosACargo();
gerenteProyecto1.verEmpleadosACargo();
programador1.verEmpleadosACargo();