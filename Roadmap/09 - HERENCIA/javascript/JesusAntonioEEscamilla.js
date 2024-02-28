/**
 * La herencia se refiere la capasidad de un objeto (Clase), de heredar propiedades
    y metodos de otra clase en este caso de una SuperClase que seria una clase principal.
 * Los objetos pueden compartir características entre ellos a través de algo llamado "prototipo".
 * Imagina que cada objeto tiene un amigo especial (su prototipo) al que puede preguntarle si no sabe algo.
 * Si ese amigo tampoco lo sabe, puede preguntar a su propio amigo, y así sucesivamente hasta llegar a un amigo
    que siempre sabe todo, y ese amigo es como el "amigo base" que todos comparten, llamado Object.prototype. 
 */
// Se define una superclase Animal
function Animal(nombre) {
    this.nombre = nombre;
    this.emitirSonido = function() {
        console.log('¡Hace otro sonido diferente!');
    };
}

// El Perro es herencia de Animal por tener nombre y emitir sonido
function Perro(nombre, raza) {
    Animal.call(this, nombre);
    this.raza = raza;
    this.emitirSonido = function() {
        console.log('¡Guau! ¡Guau!')
    }
}

// El Gato es herencia de Animal por tener nombre y emitir sonido
function Gato(nombre, color) {
    Animal.call(this, nombre);
    this.color = color;
    this.emitirSonido = function() {
        console.log('¡Miau! ¡Miau!');
    };
}

// El Hamster es herencia de Animal por tener nombre y emitir sonido
function Hamster(nombre, tamano) {
    Animal.call(this, nombre);
    this.tamano = tamano;
}

// Función para imprimir los sonidos de los gatos
function imprimirSonido(animal) {
    console.log(`${animal.nombre} dice:`);
    animal.emitirSonido();
    console.log('---');
}

// Crear instancias de las clases
var perro = new Perro('Hachico', 'Labrador');
var gato = new Gato('Kenta', 'Gris');
var hamster = new Hamster('Petronilo', 'Mediano');

// Ejemplo de herencia
imprimirSonido(perro);
imprimirSonido(gato);
imprimirSonido(hamster);



/**-----DIFICULTAD EXTRA-----*/
// Pendiente
/**-----DIFICULTAD EXTRA-----*/