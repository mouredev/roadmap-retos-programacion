// URL del sitio web oficial de TypeScript: https://www.typescriptlang.org/

// Comentario de una línea
  
// Comentarios de varias líneas 
/*
Todo 
esto 
esta 
comentado
*/

// Comentarios de documentación
/** 
 * Calcula el cuadrado de un numero
 * @param valor - El numero a elevar al cuadrado
 * @returns El resultado al cuadrado
 */
function square(value: number): number {
    return value * value;
}

// Existen tres palabras en typescript para declarar variables, cada una tiene una funcionalidad distinta 

let variable: string; // La forma recomendada para variables cuyos valores puedan cambiar.
const variable2: number = 0; // Se utiliza para variables cuyos valores no cambiaran. No permite la reasignacion tras su inicializacion.
var variable3; // La forma tradicional de JavaScript, se recomienda evitar su uso en favor de let y const.


// Tipos de datos
// Cadenas o Strings
let miUsuario: string = "Pepisxd";
// Numeros
let edad: number = 24;
// Booleano
let isActive: boolean = false; // las variables booleanas tambien se pueden definir sin especificar el type ya que ts asume que son booleanos  
let isFalse = true;
// Null e Indefinidos
let nada: null = null;
let sinAsignar: undefined = undefined;
// Cualquiera
let flexible: any = 42;
flexible = "Ahora soy un arreglo";
// Void 
function noRegresaNada(): void{
    console.log("No regresa nada");
}
// Nunca
function falla(): never{
    throw new Error("Esto siempre falla");
}

// Datos Complejos 

// Matrices o  Arreglos
let numeros: number[] = [1,2,3]; 
let nombres: Array<string> = ["Juan", "Pepe", "Fede"];
// Tuples
let user: [string, number] = ["Oliver", 30];
// Enumes
enum Role{
    Admin,
    Editor,
    Lector
}

let userRole: Role = Role.Editor;

//Objetos
let persona: {name: string, age: number} = {
    name: "Pedro",
    age: 15 
};

console.log("Hola, Typescript!!");