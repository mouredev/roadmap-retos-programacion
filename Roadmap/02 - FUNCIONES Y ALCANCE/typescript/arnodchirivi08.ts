/*
 * EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
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

// Función sin parámetros ni retorno
function saludar(): void {
    console.log("¡Hola, mundo!");
}

saludar(); 

// Función con un parámetro y sin retorno
function saludarPersona(nombre:string):void {
    console.log(`¡Hola, ${nombre}!`);
}

saludarPersona("Luis");

// Función con varios parámetros y con retorno
function sumar(a:number, b:number):number {
    return a + b;
}

console.log(`El valor de la suma es ${sumar(5, 3)}`);

// Función de orden superior (función dentro de función)
function greeter(fn: (name:string) => void){
  fn("hello, world");
}

function printConsole(s:string){
  console.log(s);
}

greeter(printConsole)


type operarNumeros = (n:number) => number;

const numerosDePrueba = [25,30,45,20]

function operandoNumeros(numeros: number[], operacion: operarNumeros){
  let valorFinal: number[] = [];
  for(let numero of numeros){
    const nuevoValor = operacion(numero)
    valorFinal.push(nuevoValor)
  }

  return valorFinal;
}

function duplicar(numero: number){
  return numero * 2
}


console.log(operandoNumeros(numerosDePrueba, duplicar));
console.log(operandoNumeros(numerosDePrueba, (n) => n /2));

// Call signatures 
type DescribableFunction = {
  description: string;
  (someArg: number): boolean;
}

function doSomething(fn:DescribableFunction){
  console.log(`${fn.description} returned ${fn(22)}`);
}

function myFunc(someArg: number) {
  return someArg > 10;
}

myFunc.description = "Default description"

doSomething(myFunc);

// Construct Signatures

interface CallOrConstruct {
  (n?: number): string;
  new (s: string): Date;
}

function fn(ctor: CallOrConstruct) {
  console.log(ctor(10));
  console.log(new ctor("10"));

}

fn(Date);

// Generic Functions
/*Las funciones genéricas son una de las características más potentes de TypeScript. En pocas palabras, son funciones que pueden trabajar con diferentes tipos de datos 
sin perder la seguridad de tipos. Actúan como plantillas o moldes que se adaptan al tipo de dato que les pases. */
// A continuación se muestra un ejemplo de función genérica que devuelve el primer elemento de un array y aplica inferencia de tipos que 
// es la capacidad de TypeScript para deducir automáticamente el tipo de una variable o expresión en función del contexto en el que se utiliza.
function firstElement<T>(arr: T[]): T | undefined {
  return arr[0];
}

console.log(firstElement(["a","b","c"]));
console.log(firstElement([1,2,3]));
console.log(firstElement([]))


/* Funcion generica con restricciones (Constraints)
Permiten limitar los tipos que se pueden usar en una variable generia. A veces se necesita que se tengan ciertas propiedades o metodos. 
Para esto se usa extends. */
interface ConLongitud {
  length: number,
}

function imprimirLongitud<T extends ConLongitud>(arg:T): void {
  console.log(`La longitud es: `, arg.length)
}

imprimirLongitud("Hola")
imprimirLongitud([1,2,3,4,5]);
//imprimirLongitud(122) //Genera error por trabajar con Valores Restringidos (Working with Constrained Values), debido a que number no tiene la propiedad length 


//Especificar Argumentos de Tipo (Specifying Type Arguments)
//Es cuando le das a TypeScript "instrucciones directas" sobre el tipo a usar.

function crearArray<T>(): T[]{
  return [];
}

const arrayNumeros = crearArray<number>();
const arrayDeStrings = crearArray<string>();

arrayNumeros.push(123);
//arrayNumeros.push(true); genera error por que se especifico que es un array de numeros
console.log(arrayNumeros);

// Parametros opcionales en funciones
function saludarConOpcional(nombre: string, apellido?: string): void {
    console.log(`Hola, ${nombre} ${apellido ? apellido : ''}`.trim());
}

saludarConOpcional("Carlos");
saludarConOpcional("Carlos", "Gomez");  
saludarConOpcional("Carlos", undefined);


// Sobrecarga de funciones (function overloads)

function procesar(texto:string): string;
function procesar(textos: string[]):string;
function procesar(parametro: string | string[]): string {
  if(typeof parametro === 'string'){
    return parametro.toUpperCase();
  }
  else {
    return parametro.join(' ');
  }
}

console.log(procesar('buenas tardes!'));
console.log(procesar(['Hola,', 'Buenas', 'Noches']));

//Otros tipos en TypedPropertyDescriptor

//void
//Se usa principalmente para indicar que una función no devuelve nada.
function mostrarMensaje(mensaje: string): void {
  console.log(mensaje);
}

mostrarMensaje('Maurodev')

//object
//Es útil cuando sabes que vas a recibir un objeto, pero no te importan sus propiedades específicas.

function trabajarConObjeto(obj: object): void {
  console.log('Se recibio un objeto' + JSON.stringify(obj));
}

trabajarConObjeto({ id: 1, nombre: "producto" });


//unknown 
//Representa un valor cuyo tipo desconocemos. 
//TypeScript no  permite hacer casi nada con un valor de tipo unknown hasta que primero verifiques su tipo

function procesarValor(valor: unknown) {
  if (typeof valor === 'string') {
    console.log(valor.toUpperCase());
  }
}

procesarValor("hola"); // Funciona
procesarValor(123) // No hace nada

//never
//representa un valor que nunca debería ocurrir. Se usa para funciones que nunca terminan su ejecución o que siempre lanzan una excepción.
/*function lanzarError(mensaje: string): never {
  throw new Error(mensaje);
}

lanzarError('Sucedio un error')*/

//Function  es un tipo global que representa cualquier valor de tipo función. Generalmente, debes evitar usarlo
// NO RECOMENDADO
function llamarCallback(cb: Function) {
  cb(1, "hola"); 
}

// Recomendado
function llamarCallbackSeguro(cb: (num: number, str: string) => void) {
  cb(1, "hola");
}


//Parámetros Rest 
function sumarTodo(...numeros: number[]): number {
  return numeros.reduce((total, num) => total + num, 0);
}

console.log(sumarTodo(5, 10, 15));

/*DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.*/

function imprimir(cadenaUno:string, cadenaDos:string): number {
   var numeroDeVecesImpreso = 0;
   for(let i = 1; i <=100; i++){
    let stringFinal = '';
    const esMultiploDeTres = i % 3 === 0;
    const esMultiploDeCinco = i % 5 === 0;

    if(esMultiploDeTres){
      stringFinal += cadenaUno;
    }
    if(esMultiploDeCinco) {
      stringFinal += stringFinal && ' ';
      stringFinal += cadenaDos;
    }     

  
    stringFinal || numeroDeVecesImpreso++;
    console.log(stringFinal === '' ? i : stringFinal);
   }
   return numeroDeVecesImpreso;
 }

 console.log(imprimir('Buenas', 'Noches'))