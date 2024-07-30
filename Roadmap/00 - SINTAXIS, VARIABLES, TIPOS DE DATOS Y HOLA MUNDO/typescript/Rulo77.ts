//sitio oficial https://www.typescriptlang.org/docs/

//comentario en una linea

/*
    Esto es un comentario
    en varias lineas
    de codigo
*/

//maneras de declarar una variable
var variable = 4;
let variable2 = 1.2;
//manera de declarar una constante
const constante = 'Hola';

// primitives types
const cadena:string = "mi cadena";
const numero:number = 124;
const booleano:boolean = true;

//Less Common Primitives
// Creating a bigint via the BigInt function
const numeroGrande:bigint = BigInt(100);
// Creating a BigInt via the literal syntax
const anotherHundred:bigint = 100n;
const nombre:symbol = Symbol("name");

//primitive values
const nulo:null = null;
const indefinido:undefined = undefined;

//others variables types
const array:Array<string> = ['hola','adios'];
const array2:number[] = [1,2,2,4];
const cualquierCosa:any = '';
const objeto: {x:number, y:number} = {x:10, y:5}

console.log('Hola typescript');

