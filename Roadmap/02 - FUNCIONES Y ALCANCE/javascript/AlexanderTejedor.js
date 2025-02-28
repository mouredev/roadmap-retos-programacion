//Funciones Basicas
/**
 * Función Tradicional
 * Sin parametros 
 */
function myFunction() { return console.log('Esta es una función') };
myFunction();
/**Con Parametro */
function saludar (name){ return console.log(`Hola ${name}`) };
saludar('JavaScript');
/**Con mas parametros */
function suma (a,b) { return console.log('El resultado de la suma es: ' + (a + b)) };
suma(2, 3);

/**Función anónima */
let despedida = function (nombre) { return console.log(`Esta mi canción de despedida ${nombre}`) };
despedida('Sera lo mejor para los dos');

let despedirse = function (name) { return `Hasta luego ${name}`; };
console.log(despedirse('Alex'));

/**Función de flecha */
const multiplicar = (a, b) =>  a * b ;
console.log(multiplicar( 28, 32 ));

/**Función con parámetros por Defecto */
let saludarConIdioma = (nombre, idioma = 'es') => { return idioma === 'es' ? `Hola ${nombre}` : `Hello ${nombre}`; }
console.log(saludarConIdioma('JavaScript'));
console.log(saludarConIdioma('JavaScript', 'en'));

/**Función autoejecutable (IIFE) */
(function(){console.log('Esta funcion se ejecuta inmediatamente.');})
();

/**Función recursiva */
function factorial (n) { return n === 0 ? 1 : n * factorial(n - 1) };
console.log(factorial(5));

/**Función de orden superior (High Order Function) */
function operar (a, b, operacion) { return operacion(a, b) };
const sumar = (x, y) => x + y;
console.log(operar(5, 78, sumar));

/**Función que devuelve otra función (closures) */
function crearSaludo(saludo) { return function (nombre) { return `${saludo} ${nombre}` } };
const saludoFormal = crearSaludo('Buenos días');
console.log(saludoFormal('JavaScript'));

/**Función asíncrona con async/await */
async function obtenerDatos() { return new Promise(resolve => setTimeout(() => resolve("Datos recibidos"), 2000));}
obtenerDatos().then(console.log);

/**Función con Callbacks */
function procesarUsuario(nombre, callback) { console.log(`Procesando usuario ${nombre}...`);
callback();}
procesarUsuario("Luis", () => console.log("Usuario procesado."));

/**Función constructora */
function Persona(nombre, edad) {
    this.nombre = nombre;
    this.edad = edad;
    this.saludar = function() {
        return `Hola, soy ${this.nombre} y tengo ${this.edad} años.`;
    };
}
const persona1 = new Persona("Luis", 30);
console.log(persona1.saludar());

/**Función generadora ( function* ) */
function* contar() { yield 1; yield 2; yield 3; }
const generador = contar();
console.log(generador.next().value);
console.log(generador.next().value);
console.log(generador.next().value);

/**Función con bind() */
const usuario = { nombre: "Ana", saludar: function() { console.log(`Hola, soy ${this.nombre}`); }};
const nuevaFuncion = usuario.saludar.bind(usuario);
nuevaFuncion();

/**Función con call() y apply()*/
function presentar (cargo) { console.log(`Hola, soy ${this.nombre} y trabajo como ${cargo}`);}
const persona = { nombre: "Carlos" };
presentar.call(persona, "desarrollador"); 
presentar.apply(persona, ["diseñador"]);

/**Funciones como Métodos y Objetos */
const coche = { marca: "Toyota",arrancar: function() { return `${this.marca} está arrancando...`;} };
console.log(coche.arrancar());

/**Funciones como parametros callback */
function operar(a, b, operacion) {
    return operacion(a, b);
}
console.log(operar(5, 3, (x, y) => x - y)); // Resta

/**Función en clases */
class Animal {
    constructor(nombre) {
        this.nombre = nombre;
    }
    hablar() {
        return `${this.nombre} hace un sonido.`;
    }
}
const perro = new Animal("Perro");
console.log(perro.hablar());

//Variable local y global (scope)

/**Scope global */
var nombre = 'Alexander';
var nombreCompleto = () => {
    /**Scope Local */
    let apellido = 'Tejedor';
    console.log(`Hola, ${nombre} ${apellido}`)
}
// try{ 
//     nombreCompleto()
//     console.log(apellido)
// }catch (error) {
//     console.error(error);
// }

/**DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 * - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 * - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 * - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 * - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 * */

let myFunc = (str1, str2) => {
    let contador = 0;
    for (i = 1; i <= 100; i++){
        let cadena1 = String(str1);
        let cadena2 = String(str2);

        if (i % 3 === 0 && i % 5 === 0){
            console.log(i + ' ' + cadena1 + ' ' + cadena2)
        }else if (i % 3 === 0){
            console.log(cadena1)
        }else if (i % 5 === 0){
            console.log(cadena2)
        }else{
            console.log(i)
            contador++;
        }
    }
    return contador;
};
let resultado = myFunc('Hola', 'JavaScript');
console.log(`Se han impreso los numeros ${resultado} veces en vez de textos`);