/*
 * EJERCICIO:
 * -//! Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
*/
function sinParametrosNiRetorno(): void {

}


function ConUnParametro(a: number): number {
    console.log(`Hola parametro ${a}`) // Hola parametro 7
    return a
}
const mostrarFun1 = ConUnParametro(7);
console.log(mostrarFun1) //7


function conVariosParametros(b: string, c: string): void {
    console.log(`Hola parametros ${b} ${c}`) //Hola parametros Hola Mundo
}
const mostrarFun2 = conVariosParametros("Hola", "Mundo");
console.log(mostrarFun2) // undefined 


/* 
*-//! Comprueba si puedes crear funciones dentro de funciones.
*/
function funcionExterna(nombre: string): string {
    function funcionInterna(saludo: string): string {
        return `${saludo}, ${nombre}!`;
    }
    return funcionInterna("Hola");
}

console.log(funcionExterna("Juan")); // Imprime: Hola, Juan!

/* 
*-//! Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
*/


//*Función básica con tipado explícito:
function sumar(a: number, b: number): number {
    return a + b;
}
console.log(sumar(5, 3)); // Salida: 8


//*Función con parámetros opcionales:
function saludar(nombre: string, saludo?: string): string {
    return saludo ? `${saludo}, ${nombre}!` : `Hola, ${nombre}!`;
}
console.log(saludar("Juan")); // Salida: Hola, Juan!
console.log(saludar("Ana", "Bienvenida")); // Salida: Bienvenida, Ana!


//*Función con parámetros por defecto:
function crearMensaje(mensaje: string, autor: string = "Anónimo"): string {
    return `${mensaje} - ${autor}`;
}
console.log(crearMensaje("Hola mundo")); // Salida: Hola mundo - Anónimo
console.log(crearMensaje("Saludos", "Carlos")); // Salida: Saludos - Carlos


//*Función con tipo de retorno void:
function logMensaje(mensaje: string): void {
    console.log(mensaje);
}
logMensaje("Este es un mensaje de prueba"); // Salida: Este es un mensaje de prueba


//*Función con unión de tipos:
function procesarValor(valor: string | number): string {
    return typeof valor === "string" ? valor.toUpperCase() : `Número: ${valor}`;
}
console.log(procesarValor("texto")); // Salida: TEXTO
console.log(procesarValor(42)); // Salida: Número: 42


//*Función con interfaz como parámetro:
interface Usuario {
    nombre: string;
    edad: number;
}

function mostrarUsuario(usuario: Usuario): string {
    return `${usuario.nombre} tiene ${usuario.edad} años`;
}
console.log(mostrarUsuario({ nombre: "María", edad: 25 })); // Salida: María tiene 25 años


//*Función flecha (Arrow Function):
const multiplicar = (a: number, b: number): number => a * b;
console.log(multiplicar(4, 5)); // Salida: 20


//*Función con promesas (asíncrona):
async function obtenerDatos(): Promise<string> {
    return new Promise((resolve) => {
        setTimeout(() => resolve("Datos obtenidos"), 1000);
    });
}
obtenerDatos().then((resultado) => console.log(resultado)); // Salida: Datos obtenidos (tras 1 segundo)


//*Función con genéricos:
function obtenerPrimerElemento<T>(arreglo: T[]): T {
    return arreglo[0];
}
console.log(obtenerPrimerElemento([1, 2, 3])); // Salida: 1
console.log(obtenerPrimerElemento(["a", "b", "c"])); // Salida: a


//*Función con sobrecarga (Function Overloading):
function combinar(a: string, b: string): string;
function combinar(a: number, b: number): number;
function combinar(a: any, b: any): any {
    return a + b;
}
console.log(combinar(10, 20)); // Salida: 30
console.log(combinar("Hola ", "mundo")); // Salida: Hola mundo


/*
*-//! Pon a prueba el concepto de variable LOCAL y GLOBAL.
*/

//variable global
let variableGlobal: string = 'Hola, soy una variable global'

function mostrarGlobal(): void {
    console.log(variableGlobal);
}
mostrarGlobal();
console.log(variableGlobal);


//variable local
function mostrarLocal(): void {
    let variableLocal: string = 'Hola, soy una variable local'
    console.log(variableLocal);
}

mostrarLocal(); // imprime 'Hola, soy una variable local'
console.log(variableLocal); //presenta error


/*
 *- Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
*/

function dificultadExtra(param1: string, param2: string): number {
    let i: number = 1
    let x: number = 0
    while (i <= 100) {
        if (i % 3 === 0 && i % 5 === 0) {
            console.log(param1, 'y ' + param2)
            x++;
        }
        if (i % 3 === 0) {
            console.log(param1)
            x++;
        }
        else if (i % 5 === 0) {
            console.log(param2)
            x++;
        }
        i++;
    }
    return x //53
}

const mostrarDE = dificultadExtra('es multiplo de 3', 'es multiplo de 5')
console.log(mostrarDE)