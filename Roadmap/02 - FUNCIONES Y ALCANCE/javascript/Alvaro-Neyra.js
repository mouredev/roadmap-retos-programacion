// Funciones
/*Sin parametros ni retorno, con uno o varios parametros, con retorno....*/

// Funcion sin parametros ni retorno
function funcionNormal() {
    console.log(`Esta es una funcion normal que no tiene parametros ni retorna algo`);
}

funcionNormal()

// Funcion con varios parametros sin retorno
function funcionDeDosParametros(nombre, edad) {
    console.log(`Hola tu nombre es: ${nombre} y tu edad es: ${edad}`);
}

// Funcion con varios parametros con retorno
function funcionConRetorno(string, numero) {
    // Retorna la cantidad de caracteres del string menos el numero
    let length = string.length;
    return length - numero;
}

cantidadDeCaracteresMenosNumero = funcionConRetorno("Hola, Mundo!", 5);
console.log(`Esta es el valor de la longitud del String menos el numero pasado: ${cantidadDeCaracteresMenosNumero}`);

// Llama a una funcion con valores opcionales
function saludar(nombre = "Invitado", saludo = "Hola") { // Este modo de poner valores opcionales en los parametros es valido a partir de ES6+
    return `${saludo}, ${nombre}!`
}

saludo = saludar()
console.log(saludo)

// Una funcion con parametros opcionales y uno obligatorio
function retornarValores(nombre, apellido = "No Especificado", origen = "No Especificado") {
    if (nombre) {
        console.log(`Tu nombre es: ${nombre}`)
    }
    if (apellido) {
        console.log(`Tu apellido es: ${apellido}`)
    }
    if (origen) {
        console.log(`Tu origen es: ${origen}`)
    }
}

retornarValores("Alvaro")

// Funcion con parametros usando `...args`:
// En este caso ...args es un array
function sumaIlimitada(...args) {
    let suma = 0;
    for (let i = 0; i < args.length; i++) {
        suma+= args[i];
    }
    return suma;
}

resultado = sumaIlimitada(20, 30, 40, 100);
console.log(resultado);

// Function Expressions:
/* Las function expressions son casi similares a la declaracion de una funcion normal. La diferencia principal
es el nombre de la funcion ya que podria ser omitida en ciertos casos o podrias ser asignada a un variable para luego ejecutarse
con el nombre de esa variable*/
// OJO: Las function expressions no son afectadas en el hosting, esto quiere decir que no podrias usar este tipo de funcion antes de que sea declarada
const functionExpression = function () {
    console.log(`Esta es una function expression!`);
}
functionExpression();

// Usando el function expression como un callback:
/* Los function expressions no necesariamente van a ser asignadas a una variable tambien podrian usarse para administrar un evento
y no necesita un nombre: */
/* button.addEventListener.("click", function (event) {
    console.log(`This is an anonymous function expression that handles an event, the event: ${event}!`)
}) */

// Immediately Invoked Function Expression (IIFE)
// Esta funcion en espano es funcion expresion inmediatamende invocada, esta funcion se ejecuta luego de ser creada, como puedes ver no necesita un nombre:
(function () {
    console.log("IIFE funciona!")
})();

// Arrow functions:
// Los Arrow function es una alternativa a la tradicional function expression, pero con algunas diferencias y limitaciones:
/* - Los arrow functions no pueden tener sus propias identificadores the valor como: `this`
   - Arrow functions no pueden ser usados como constructores.*/

// Un arrow function vacio: NO EJECUTA NADA
const emptyArrowFunction = () => {};
emptyArrowFunction()
// IIFE pero con Arrow function: retorna "Hola, Mundo!"
console.log((() => "Hola, Mundo!")());
// Arrow functions con retorno y llaves
const sumaArrow = (number1, number2) => { return number1 + number2};
resultadoSuma = sumaArrow(40,3);
console.log(resultadoSuma);
// Arrow function sin parentesis, sin llaves y de una sola linea
const siEsMayorATreinta = number => number > 30 ? 30 : 10
console.log(siEsMayorATreinta(31)) // -> 30
console.log(siEsMayorATreinta(16)) // -> 10
// Arrow functions con retorno implicito (no se usa la palabra reservada 'return')
const maximoNumero = (numero1, numero2) => (numero1 > numero2 ? numero1 : numero2);
let maxNumber = maximoNumero(20, 30);
console.log(maxNumber);

// Funciones asincronas
// Creando la primera funcion asincrona
//    const corutina1 = async () => {
//       console.log("Inicio de la funcion asincrona 1");

//        await new Promise(resolve => setTimeout(resolve, 500));

//       console.log("Fin de la funcion asincrona!");
//    }
//    // Creando la segunda funcion asincrona
//    const corutina2 = async () => {
//        console.log("Inicio de la funcion asincrona 2");

//        await new Promise(resolve => setTimeout(resolve, 500));

//        console.log("Fin de la funcion asincrona!");
//    }
//    // Creando la funcion que va a ejecutar las dos funciones asincronas
//    async function ejecutarFuncionesAsincronas() {
//        try {
//            process.stdout.write("Ejecutando funciones asincronas. Espere")

//            // Imprimiendo puntos consecutivos
//            for (let i = 0; i < 8; i++) {
//                await new Promise(resolve => setTimeout(resolve, 500));
//                process.stdout.write(".");
//           }

//            // Nueva linea
//            console.log();

//            // Ejecutando la primera funcion asincrona
//            await new Promise(resolve => resolve(corutina1()));

//            process.stdout.write("Esperando a la funcion asincrona 2")

//            // Imprimiendo puntos consecutivos
//            for (let i = 0; i < 8; i++) {
//                await new Promise(resolve => setTimeout(resolve, 500));
//                process.stdout.write(".");
//            }

//            // Nueva linea
//            console.log();

//            // Ejecutando la funcion asincrona 2
//            await new Promise(resolve => resolve(corutina2()));
//        }
//        catch (error) {
//            console.error("Se ha producido un error: ", error.message);
//        }
//    }
//    ejecutarFuncionesAsincronas();

//* - Comprueba si puedes crear funciones dentro de funciones.
function funcionExterna(numero){
    function funcionInterna(numeroAlDoble) {
        return numeroAlDoble * 2;
    }
    let numeroDoblado = funcionInterna(numero);
    return numeroDoblado;
}

resultadoDelNumero = funcionExterna(20);
console.log(resultadoDelNumero);

//* - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.

// toString()
let numero = 43000.3;
let convertidoAString = numero.toString();
console.log(convertidoAString);

// max()
let nuevoArray = [20, 30, 400, 40, 50];
let numeroMax = Math.max(...nuevoArray);
console.log(numeroMax);

// min()
let numeroMin = Math.min(20, 10, 0, 400);
console.log(numeroMin);

// console.log()
console.log(`'console.log' tambien es una funcion integrada del lenguaje!`);

//* - Pon a prueba el concepto de variable LOCAL y GLOBAL.

// Variable local en JavaScript:
/* SI UNA VARIABLE SE DECLARA DENTRO DE UNA FUNCION O ESTRUCTURA DE CONTROL USANDO `VAR`, `LET O `CONST`, SE CONSIDERA
UNA VARIABLE LOCAL Y SOLO ES VISIBLE DENTRO DE ESA FUNCION O ESTRUCTURA DE CONTROL. */
// Mira este ejemplo:
let variableInterna = 20; // Se declara una variable en el ambito global
{
    let variableInterna = 10; // Se declara una variable con el mismo nombre en el ambito local
    console.log(variableInterna); // Solo existe en este ambito (dentro de los corchetes), se imprime en consola su valor asignado
}
console.log(variableInterna) // Se imprime el valor de la varaible global no la de local
// Otro ejemplo:
{
    const nuevaVariable = "Hola";
    console.log(nuevaVariable);
}
//console.log(nuevaVariable); // Dara error ya que la variable 'nuevaVariable no existe en el ambito GLOBAL' ❌

// Variable Global
/* Si una variable se declara fuera de cualquier función o bloque, se considera una variable global 
y es accesible desde cualquier parte del código. */
let variableGlobal = "Mundo!"

function imprimeVariableGlobal() {
    console.log(variableGlobal);
}

imprimeVariableGlobal(); // La variable 'variableGlobal' es accesible en cualquier ambito del codigo.

// DIFICULTAD EXTRA!::
const intercambiarNumeros = (string1, string2) => {
    // Creando contadores:
    let contadorDeString1YString2 = 0;
    let contadorDeString1 = 0;
    let contadorDeString2 = 0;
    let contadorDeNumerosNoIntercambiados = 0;

    for (let i = 1; i <= 100; i++) {
        if (i % 3 === 0 && i % 5 === 0) {
            console.log(string1+string2);
            contadorDeString1YString2++;
        }
        else if (i % 3 === 0) {
            console.log(string1);
            contadorDeString1++;
        }
        else if (i % 5 === 0) {
            console.log(string2);
            contadorDeString2++;
        }
        else {
            contadorDeNumerosNoIntercambiados++;
        }
    }
    console.log(`Numero de veces que los numeros han sido intercambiados por la primera cadena de texto: ${contadorDeString1}`)
    console.log(`Numero de veces que los numeros han sido intercambiados por la segundo cadena de texto: ${contadorDeString2}`)
    console.log(`Numero de veces que los numeros han sido intercambiados por la primera y segunda cadena de texto: ${contadorDeString1YString2}`)
    return contadorDeNumerosNoIntercambiados;
}

let cuentaDeNumeroNoIntercambiados = intercambiarNumeros("Hola", "Mundo");
console.log(`Numero de veces que los numeros no han sido intercambiados: ${cuentaDeNumeroNoIntercambiados}`)