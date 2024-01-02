// 1º URL de TypeScript https://www.typescriptlang.org/

// 2º Tipos de Comentarios:
    // - Comentarios de una línea: 
        // Comentario
    // - Comentarios de varias línea: 
        /* Comentario de 
         * varias líneas 
         * de código 
        */
    // - Comentarios para la documentación: 
        /* Son comentarios que nos permiten documentar
        * nuestro código y la generación de documentación
        * automática conocidda como TSDoc que facilita la comprensión
        * y mantenimiento del código.
        * Pueden ir acompañados de etiquetas como @param o @return
        * que identifican valores 
        */

// 3º Variables - En Typescript las variables se pueden declarar con un let o un var
let variable1 : number = 18;
var variable2 : number = 19;
// Constantes
const constante1 : string = 'Adrián';

// 4º Lenguajes Primivitivos
const nombre : string = 'Igledev';
const edad : number = 19;
const peso : number = 67.8 // Tambien se utiliza para número decimales
const webdev : boolean = true;
const loquesea : any = 'Any' // Any es un tipo de dato que acepta cualquier valor pero no se recomienda su uso
//Arrays, pueden ser de 3 tipos y definirlas de maneras distintas
const lenguajes : Array<string> = ['TypeScript' , 'PHP' , 'JavaScript'];
const notas : Array<number> = [9.8, 5, 7.5];
const todo : Array<any> = ['TypeScript' , 'PHP' , 'JavaScript', 9.8 , 5 , 7.5];
// Tambien se pueden definir de esta manera:
const anhos : number[] = [2021, 2022, 2023, 2024]
const dinero : number | string = 20000; // Esto se llama Tupla y se utiliza para que una variable tengo múltiples tipos de datos
const sin_definir : undefined = undefined;
const vacio : null = null;
const numero_grande : bigint = 999999999999999999999999999999n; //permite representar enteros más grandes que el tipo number
const simbolo : symbol = Symbol('trifuerza'); // Es un tipo de dato cuyas instancias son únicas e inmutables
const objet : object = {};
const enum Tallas {Small, Medium, Large, ExtraLarge} //El tipo enum son listas de constantes que podemos referenciar en un futuro

// 5º Impresión por consola
console.log('¡Hola, TypeScript!')