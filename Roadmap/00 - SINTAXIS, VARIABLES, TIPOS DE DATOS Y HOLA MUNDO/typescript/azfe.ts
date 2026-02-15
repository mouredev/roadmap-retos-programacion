// 1.- Crea un comentario en el código y coloca la URL del sitio web oficial del lenguaje de programación que has seleccionado.

// https://www.typescriptlang.org/

/*
* TypeScript es un lenguaje de programación de código abierto desarrollado por Microsoft. Es un superconjunto de JavaScript, lo que significa que cualquier código JavaScript válido también es válido en TypeScript. TypeScript agrega características adicionales a JavaScript, como tipado estático, clases, interfaces y módulos, lo que facilita el desarrollo de aplicaciones grandes y complejas.

* Algunas de las características clave de TypeScript incluyen:
* 1. Tipado estático: TypeScript permite a los desarrolladores definir tipos para variables, funciones y objetos, lo que ayuda a detectar errores en tiempo de compilación y mejora la legibilidad del código.
* 2. Clases y objetos: TypeScript soporta la programación orientada a objetos, lo que permite a los desarrolladores crear clases, interfaces y herencia, facilitando la organización y reutilización del código.
* 3. Módulos: TypeScript permite a los desarrolladores organizar su código en módulos, lo que facilita la gestión de dependencias y la reutilización de código.
* 4. Compatibilidad con JavaScript: TypeScript es compatible con JavaScript, lo que significa que los desarrolladores pueden usar bibliotecas y frameworks de JavaScript existentes sin problemas.
* 5. Herramientas de desarrollo: TypeScript cuenta con un sistema de compilación que convierte el código TypeScript en JavaScript, lo que permite a los desarrolladores aprovechar las herramientas de desarrollo y depuración disponibles para JavaScript.

* En resumen, TypeScript es un lenguaje de programación que mejora la experiencia de desarrollo en JavaScript al agregar características de tipado estático y programación orientada a objetos, lo que facilita la creación de aplicaciones grandes y complejas.
*/

// 2.- Crea una variable (y una constante si el lenguaje lo soporta).

let variable: string = "Hola Mundo";

const PI: number = 3.1416;

// 3.- Crea variables representando todos los tipos de datos primitivos del lenguaje (cadenas de texto, enteros, booleanos...).

let texto: string = "Esto es una cadena de texto";
let num: number = 42;
let isTrue: boolean = true;
let valorNulo: null = null;
let valorUndefined: undefined = undefined;
let simbolo: symbol = Symbol("símbolo");
let any: any = "Esto puede ser cualquier tipo de dato";
let avoid: void = undefined;
let never: never;

// 4.- Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
console.log("¡Hola, TypeScript!");
