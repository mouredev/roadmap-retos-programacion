//https://www.typescriptlang.org/

console.log("Hola typeScript");

// variables y constantes
const constante : string = "constante";
let variableLet : string;
var variableVar : string;

// Tipos de datos permitos den 
let variableNumerica : number;
let variableString : string;
let variableBoolean : boolean;
let variableArray : Array<string>;

// Arreglos de strings
const arr1: string[] = ['foo', 'bar'];
const arr2: Array<string> = ['foo', 'bar'];
// Arreglos de números
const arr3: number[] = [1, 2, 3, 4, 5];
const arr4: Array<number> = [1, 2, 3, 4, 5];
// Arreglos de strings o números
const arr5: (string|number)[] = ['foo', 1, 'bar', 2];
const arr6: Array<string|number> = ['foo', 1, 'bar', 2];

// tipo object generico
const fruticas : object  = {
    nombre: "nombre",
    apellido : "apellido"
}

// objeto con propiedades
const fruticasConCiudad : { nombre: string, ciudad: string } = {
    nombre: "manzana",
    ciudad: "cali"
}

// Los ennumeradores son un tipo de dato donde todos los valores
// que contiene son constantes.
enum ProductosLimpieza {
    FABULOSO,
    JABON_LOSA,
    JAVON_BAÑO,
}

// any es el tipo mas flexible, es como trabajar cono js directamente
let variableAny : any;
variableAny = 23
variableAny = "Hola como estas";
variableAny = {
    nombre: "hola como estas?",
    numero: 23,
}

// Alias
type StringOrNumber = string | number;
const var20: StringOrNumber = '1';
const var21: StringOrNumber = 1;

type Geo = { country: string; city: string; };
const var22: Geo = {
    country: 'Spain',
    city: 'Málaga',
}

// never, void, unknown, funciones y callbacks;
