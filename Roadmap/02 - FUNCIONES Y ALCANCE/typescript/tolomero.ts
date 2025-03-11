/*Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:*/

//función sinple

function saludar1(): void {
    console.log("Hola, mundo!");
}
saludar1()//funcion con retorno

function saludarRetorno(): string{
    return "Hola, mundo!";
}

const saludar2 = saludarRetorno;
console.log(saludar2());

// funcion con parametros	
function saludarConParametros(nombre: string, edad: number): void {
    console.log(`Hola, ${nombre}! Tienes ${edad} años.`);
}
saludarConParametros("Elena", 28);


//funcion con parametros por defecto

function saludarConApellido(saludar:string = "!Hola", apellido: string = "Perez"): void {
    console.log(`${saludar} parce ${apellido}`)
}

saludarConApellido();

//funcion con parametros rest

function saludarConRestParametros(saludo: string, ...nombres: string[]): void {
    nombres.forEach(nombre => {
        console.log(`${saludo} ${nombre}`);
    });
}
saludarConRestParametros("Hola", "Juan", "Pedro", "Luis");

//funcion con parametros y retorno

function elevarAlCuadrado(base: number): number {
    return base * base;
}

console.log(elevarAlCuadrado(3));

//funciones dentro de funciones

function saludarConFunciones(nombre: string): void {
    function saludar(): void {
        console.log(`Hola ${nombre}`);
    }

    saludar();
}

saludarConFunciones("Elena");

// variables globales

let variableGlobal = "Hola, soy global";

function variableGlobal2(): void {
    console.log(variableGlobal);

}



//variable local

function variableLocal(): void {
    let variableLocal = "Hola, soy local";
    console.log(variableLocal);
    console.log(variableGlobal);

}
variableLocal();

// ejercicio extra
let count: number = 0;
function dosTextos(texto1:string, texto2:string): number {
    
    for(let i = 1; i <= 100; i++){
        if ( i % 3 === 0) console.log(texto1 + texto2);
        else if (i % 3 === 0) console.log(texto1);
        else if (i % 5 === 0) console.log(texto2 );
        else console.log(i);
         count += 1 
    }
    return count
}

console.log(dosTextos("fizz", "buzz"));



