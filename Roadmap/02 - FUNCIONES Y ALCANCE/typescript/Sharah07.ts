// *** TIPOS DE FUNCIONES Y SUS VARIACIONES/POSIBILIDADES:

// *** FUNCIÓN NORMAL (DECLARACIÓN ESTÁNDAR)
/**
 * Función sin parámetros ni retorno: no reciben argumentos ni veduelven un valor. 
 * Realizan solo el çodigo dentro de su bloque.
 */
function mensaje(): void{
    console.log('Función sin parámetros ni retorno'); 
}

mensaje(); //Función sin parámetros ni retorno
/**
 * Sin parámetros, pero con retorno: no usan parámetros, 
 * pero sí retornan un resultado al llamarlas.
 */
function mostrarFecha() {
    return console.log(new Date()); //2025-03-13T15:45:43.284Z
}

mostrarFecha();
/**
 * Con un parámetro y sin retorno: toman solo un parámetro y no devuelven un resultado.
 */
function mostrarNombre(nombre:string){
    console.log('Hola ', nombre);
}

mostrarNombre('Seira'); //Hola  Seira

/**
 * Con uno o varios parámetros y con retorno: recibe uno o varios parámetros 
 * y devuelve un resultado.
 */
function areaCuadrado(a:number):number{
    return a*a;
}

function areaRectangulo(a:number, b:number):number{
    return a*b;
}

areaCuadrado(4); //Salida: 16
areaRectangulo(3,6); //Salida: 18

/**
 * Parámetros opcionales.
 */
function saludoConOpcional(nombre?: string) {
    if (nombre) {
        return console.log('Hola, ', nombre, '!');
    }
    else {
        return console.log('Hola!');
    }
}

saludoConOpcional('Sharah'); //Hola,  Sharah !
saludoConOpcional(); //Hola!

/**
 * Con valores predeterminados: los parámetros tienen valores predeterminados que la
 * función usa si no se le pasan argumentos.
 */

function bienvenido(nombre:string = 'Usuario/a'){
    return console.log('Bienvenido/a, ', nombre, '!');
}

bienvenido(); //Bienvenido/a,  Usuario/a !
bienvenido('Sharah'); //Bienvenido/a,  Sharah !

// *** FUNCIONES ANÓNIMAS.
/** Es una función sin nombre que se asigna a una variable o constante, suele crearse al momento en situaciones
 * donde no requiere ser reutilizada.
 * También sirve como callback (argumento en otra función).
 */
var operacion = function (a, b) {   //función anónima
    return a * b;
};
function areaTriangulo(a=2) {
    var area = operacion(8, 6) / a;
    return console.log(area);
}

areaTriangulo(); //24

// *** FUNCIONES FLECHA (ARROW FUNCTION).
/**Hacen el código más compacto y fácil de leer,
 * especialmente en funciones pequeñas.
 */
const division = (a:number, b:number):number =>{
    return a/b;
}
console.log(division(8,2)); // 4

const suma = (a:number, b:number):number => a + b;
console.log(suma(4,2)); // 6

// *** FUNCIONES GENÉRICAS.
/**Permiten trabajar con distintos tipos de datos manteniendo la seguridad de tipos,
 * son útiles cuando no sabemos con que tipos de datos trabajará la función 
 * y ahorran espacio al no tener que definir diferentes funciones para diferentes tipos de datos. 
 */
function valor<T>(a:T):T{
    return a;
}
 
console.log(valor('Sharah')); //Sharah 
console.log(valor(27)); //27

function combinar<T,U>(a: T, b: U): [T,U]{
    return [a, b];
}
console.log(combinar('Seira', 21)); //[ 'Seira', 21 ]

// ***FUNCIONES COMO TIPOS PERSONALIZADOS.
/**Permiten definir la estructura de una función (parámetros y valor de retorno) como un tipo independiente.
 * Sirve cuando tenemos varias funciones con la misma estructura, lo que evita tener que definirla cada vez.
*/

// Type Alias
type operacion = (a:number, b:number) => number;

const multiplicaion: operacion = (a, b) => a*b;
const dividir:operacion = (a, b) => a/b;

console.log(multiplicaion(6,2)); // 12
console.log(dividir(6,2)); // 3

// Interface
interface operacion2 {
    (a:number, b:number): number;
}

const suma2: operacion2 = (a, b) => a+b;
const resta: operacion2 = (a, b) => a-b;

console.log(suma2(4,8)); //12
console.log(resta(4,8)); //-4

// *** FUNCIÓN DENTRO DE FUNCIÓN (FUNCIONES ANIDADAS).
/**
 * Son funciones que se definen dentro del cuerpo de otra función.
 * Sirven para encapsular código, reducir su uso donde realmente es necesario 
 * y reducir repetición de código. 
 * */  

function areaDeCuadrado(a) {
    function multiplicar() {
        return a * a;
    }
    return multiplicar();
}
console.log(areaDeCuadrado(3)); //9

// *** EJEMPLO DE FUNCIÓN DEL LENGUAJE.

const persona2 = {nomber: 'Seira', edad: 20};      

console.log(Object.keys(persona2)); //[ 'nomber', 'edad' ]
console.log(Object.values(persona2)); //[ 'Seira', 20 ]
console.log(Object.entries(persona2)); //[ [ 'nomber', 'Seira' ], [ 'edad', 20 ] ]             

// *** VARIABLE LOCAL Y GLOBAL.
/**
 * Variable Global: Esta variable se declara fuera de cualquier función, bloque o clase, 
 * por lo que se puede acceder a ella desde cualquier parte del código, mientras no haya ninguna restrincción. 
 * 
 * Variable Local: Se defini dentro de una función, bloque o clase 
 * y su uso se limita al ámbito en el que fue definida.
 */
let variableGlobal = 'Esta es una variable global.';
function mostrar(){
    let variableLocal='Esta es una variable local.';
    console.log(variableGlobal); //'Esta es una variable global.'
    console.log(variableLocal); //'Esta es una variable local.'
}
console.log(variableGlobal); //'Esta es una variable global.'


// *** DIFICULTAD EXTRA.

function numeros(m3:string, m5:string){
    m3 = 'múltiplo de 3';
    m5 = 'múltiplo de 5';
    let contadorExterno=0;
    for(let i=1; i <= 100; i++){
        if(i%3 == 0 && i%5 == 0){
            console.log(m3, 'y ', m5);
        }else if(i%3 == 0){
            console.log(m3);
        }else if(i%5 == 0){
            console.log(m5);
        }else{
            console.log(i);
        }
        contadorExterno++;
    }
    return console.log('retorno: ',contadorExterno);
}

numeros();