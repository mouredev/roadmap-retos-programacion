//Funciones Sin Parámetros ni Retorno
function saludar(): void {
    console.log("¡Hola Mundo!");
}
saludar(); // ¡Hola Mundo!

//Funciones Con Parámetros
//Un Parámetro
function saludarPersona(nombre: string): void {
    console.log(`¡Hola, ${nombre}!`);
}
saludarPersona("Juan"); // ¡Hola, Juan!

//Varios Parámetros
function sumar(a: number, b: number): void {
    console.log(a + b);
}
sumar(5, 3); // 8

//Funciones Con Retorno
//Retorno de un Valor
function obtenerEdad(): number {
    return 25;
}

let edad: number = obtenerEdad();
console.log(edad); // 25

//Retorno de Varios Valores (tupla)
function obtenerCoordenadas(): [number, number] {
    return [10, 20];
}

let coordenadas: [number, number] = obtenerCoordenadas();
console.log(coordenadas); // [10, 20]

//Funciones con Parámetros Opcionales y Valores Predeterminados
//Parámetros Opcionales
function saludarOpcional(nombre?: string): void {
    if (nombre) {
        console.log(`¡Hola, ${nombre}!`);
    } else {
        console.log("¡Hola!");
    }
}

saludarOpcional("Ana"); // ¡Hola, Ana!
saludarOpcional();      // ¡Hola!

//Parámetros con Valores Predeterminados
function saludarConPredeterminado(nombre: string = "Amigo"): void {
    console.log(`¡Hola, ${nombre}!`);
}

saludarConPredeterminado("Pedro"); // ¡Hola, Pedro!
saludarConPredeterminado();        // ¡Hola, Amigo!

//Funciones Anónimas
let saludarAnonimo = function(nombre: string): void {
    console.log(`¡Hola, ${nombre}!`);
};

saludarAnonimo("Carlos"); // ¡Hola, Carlos!

//Funciones Flecha
let saludarFlecha = (nombre: string): void => {
    console.log(`¡Hola, ${nombre}!`);
};

saludarFlecha("Laura"); // ¡Hola, Laura!

//Funciones que Aceptan Otras Funciones como Parámetros
//Funciones como Parámetros
function procesar(callback: (a: number, b: number) => number, a: number, b: number): void {
    console.log(callback(a, b));
}

function sumando(a: number, b: number): number {
    return a + b;
}

procesar(sumando, 5, 3); // 8

//Funciones que Devuelven Funciones
function crearMultiplicador(multiplicador: number): (valor: number) => number {
    return (valor: number) => valor * multiplicador;
}

let duplicar = crearMultiplicador(2);
console.log(duplicar(5)); // 10

//Funcion dentro de una funcion
function externa() {
    let mensaje: string = "Hola desde la función externa";

    function interna() {
        console.log(mensaje);
    }

    interna();
}

externa(); // "Hola desde la función externa"

//Funcion ya creada en TypeScript
let mensaje: string = "Hola Mundo";
console.log(mensaje.toUpperCase()); // "HOLA MUNDO"
console.log(mensaje.includes("Mundo")); // true


//Variables locales versus variables globales
let globalVariable: string = "Variable global";

function ejemplo() {
    let localVariable: string = "Variable local";

    console.log(globalVariable); // "Variable global"
    console.log(localVariable); // "Variable local"

    globalVariable = "Variable global modificada";

    if (true) {
        let localEnBloque: string = "Variable local en bloque";
        console.log(localEnBloque); // "Variable local en bloque"
    }

    // La siguiente línea daría un error porque `localEnBloque` no está definida en este alcance.
    // console.log(localEnBloque);
}

ejemplo();

console.log(globalVariable); // "Variable global modificada"
// La siguiente línea daría un error porque `localVariable` no está definida en este alcance.
// console.log(localVariable);

function ejercicio(a: string, b: string): number{
    let impresiones:number=0;
    for(let contador: number = 1; contador <=100;contador++){
        if ((contador % 3 == 0)&&(contador % 5 == 0)){
            console.log(a+b);
        }else if (contador % 3 == 0){
            console.log(a);
        }else if (contador % 5 == 0){
            console.log(b);
        }else {console.log(contador)
            impresiones++;
        }
    }
    return impresiones;
}

console.log("Cantidad de veces que se imprimio un numero = "+ ejercicio("Wenas ","Taldes"));
