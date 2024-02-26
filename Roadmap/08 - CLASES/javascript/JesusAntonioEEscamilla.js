/**
 * Las cales son plantillas para crear objetos.
 *  Las clases son una forma de encapsular datos y funciones relacionadas en un solo objeto,
    proporcionando una estructura más organizada y orientada a objetos al código JavaScript. 
 */

//-----CLASE-----
class Persona{
    // Inicializar
    constructor(nombre, edad){
        this.nombre = nombre;
        this.edad = edad;
    }

    // Función
    saludar(){
        console.log(`Hola, soy ${this.nombre} y tengo ${this.edad} años.`);
    }
}

// Crear un objeto para usar la clase
const persona1 = new Persona("Jesus Antonio", 24);

// Imprime la información
persona1.saludar(); // Llama el saludo que esta dentro de la clase

// Modificación del objeto
persona1.nombre = "Fatima";
persona1.edad = 19;

// Imprimir información después de la modificación
persona1.saludar();



/**-----DIFICULTAD EXTRA-----*/
//  Pendiente.....
/**-----DIFICULTAD EXTRA-----*/