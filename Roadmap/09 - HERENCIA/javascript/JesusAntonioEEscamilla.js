/** #09 - JavaScript ->Jesus Antonio Escamilla */
/**
 * La herencia se refiere la capacidad de un objeto (Clase), de heredar propiedades
    y métodos de otra clase en este caso de una SuperClase que seria una clase principal.
 * Los objetos pueden compartir características entre ellos a través de algo llamado "prototipo".
 * Imagina que cada objeto tiene un amigo especial (su prototipo) al que puede preguntarle si no sabe algo.
 * Si ese amigo tampoco lo sabe, puede preguntar a su propio amigo, y así sucesivamente hasta llegar a un amigo
    que siempre sabe todo, y ese amigo es como el "amigo base" que todos comparten, llamado Object.prototype. 
 */

// Se define una superclase Animal
class Animal {
    constructor(nombre) {
        this.nombre = nombre;
    }
}

// El Perro es herencia de Animal por tener nombre y emitir sonido
class Perro extends Animal{
    constructor(nombre, raza){
        // Llamamos al constructor de la clase base utilizando "super"
        super(nombre);

        // Agregamos propiedades específicas de la subclase
        this.raza = raza;

    }
    saludar(){
        console.log(`Hola, soy ${this.nombre} y mi raza es ${this.raza}`);
    }
}

// El Gato es herencia de Animal por tener nombre y emitir sonido
class Gato extends Animal {
    constructor(nombre, color) {
        super(nombre);
        this.color = color;
    }
    // Sobrescribimos el método saludar para la subclase
    saludar() {
        console.log(`Hola, soy ${this.nombre} y mi pelaje es de color ${this.color}`);
    }
}

// El Hamster es herencia de Animal por tener nombre y emitir sonido
class Hamster extends Animal{
    constructor(nombre, size){
        super(nombre);
        this.size = size;
    }
    saludar(){
        console.log(`Hola, soy ${this.nombre} y mi tamaño es de ${this.size}`);
    }
}

// Crear instancias de las clases
var perro = new Perro('Hachico', 'Labrador');
var gato = new Gato('Kenta', 'Gris');
var hamster = new Hamster('Petronilo', 'Mediano');

// Ejemplo de herencia
perro.saludar();
gato.saludar();
hamster.saludar();


/**-----DIFICULTAD EXTRA-----*/

// Función que genera un identificador único
function generarIdentificador() {
    const numeroAleatorio = Math.floor(Math.random() * 1000);
    const identificador = `ID_${numeroAleatorio}`;
    return identificador;
}

// Super-Clase de Empleado
class Empleado{
    constructor(nombre){
        this.Id = generarIdentificador();
        this.nombre = nombre;
        this.empleado = [];
    }
    agregar_empleados(empleado){
        this.empleado.push(empleado);
    }
    imprimirEmpleado(){
        console.log(this.empleado);
    }
}

//  Clase Gerente que extiende de Empleado
class Gerente extends Empleado{
    constructor(Id, nombre){
        super(Id, nombre);
    }
    coordinar_proyectos(){
        console.log(`${this.nombre} esta coordinando todos los proyectos de la empresa`);
    }
}

//  Clase Gerente de Proyecto que extiende de Empleado
class GerenteProyecto extends Empleado{
    constructor(nombre, proyecto){
        super(nombre);
        this.proyecto = proyecto;
    }

    coordinar_proyecto(){
        console.log(`${this.nombre} esta coordinando su proyecto`);
    }
}

//  Clase Programador que extiende de Empleado
class Programador extends Empleado{
    constructor(nombre, language){
        super(nombre);
        this.language = language;
    }

    code(){
        console.log(`${this.nombre} esta programando en ${this.language}`)
    }

    agregar_empleado(){
        console.log(`Un programador no puede tener empleado.`);
    }
}


//  Asignamos valores a la empresa
const mi_gerente = new Gerente("Jesus Antonio");
const mi_gerente_proyecto_1 = new GerenteProyecto("Fatima", "Proyecto1");
const mi_gerente_proyecto_2 = new GerenteProyecto("Angel", "Proyecto2");
const mi_programador_1 = new Programador("Adolfo", "Python");
const mi_programador_2 = new Programador("Naty", "JavaScript");
const mi_programador_3 = new Programador("Ruben", "Kotlin");
const mi_programador_4 = new Programador("Axel", "PHP");

//  Agregamos la jerarquía
mi_gerente.agregar_empleados(mi_gerente_proyecto_1);
mi_gerente.agregar_empleados(mi_gerente_proyecto_2);
mi_gerente_proyecto_1.agregar_empleados(mi_programador_1);
mi_gerente_proyecto_1.agregar_empleados(mi_programador_2);
mi_gerente_proyecto_2.agregar_empleados(mi_programador_3);
mi_gerente_proyecto_2.agregar_empleados(mi_programador_4);

mi_programador_1.agregar_empleado(mi_gerente_proyecto_1); // Esta No Puede Agregar

//  Usamos las funciones o propiedades de las clases
mi_programador_1.code();
mi_gerente_proyecto_1.coordinar_proyecto();
mi_gerente.coordinar_proyectos();
mi_gerente.imprimirEmpleado();
mi_gerente_proyecto_1.imprimirEmpleado();
mi_programador_1.imprimirEmpleado();

/**-----DIFICULTAD EXTRA-----*/