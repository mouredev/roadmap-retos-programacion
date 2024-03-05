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
// Pendiente
/**-----DIFICULTAD EXTRA-----*/