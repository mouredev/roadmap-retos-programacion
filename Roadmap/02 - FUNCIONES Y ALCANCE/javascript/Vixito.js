function ej_1() {}
let ej_2 = function(a, b) {}
const ej_3 = (par_1, par_2) => {
    return par_1 + par_2;
}
function ej_4() {
    console.log(ej_3(1, 2));
}
ej_4();


// Funciones creadas por el lenguaje
const numeros = [1, 2, 3, 4];
console.log("\n" + numeros.length + ", " + numeros.push(Math.round(Math.random(Number.EPSILON)*numeros.length)));
console.log(numeros);

// Variables LOCAL y GLOBAL

const global = "Soy una variable global"
console.log("\n" + global.includes("global"));

function Local(){
    const local = "Soy una variable local";
    console.log(local.includes("local"));
}
try {
    console.log(local.includes("global"));
} catch (error) {
    error.message;
} finally{
    console.log("No hay variable local (globalmente)\n");
}

// DIFICULTAD EXTRA

function cadena_deTexto(cadena_1, cadena_2){
    // Los parámetros convierten todo tipo de dato a String
    cadena_1 = String(cadena_1);
    cadena_2 = String(cadena_2);
    let veces = 0;
    for (let number = 1; number <= 100; number++){
        if(number % 3 === 0 && number % 5 === 0){
            console.log(cadena_1 + " " + cadena_2);
        } else if(number % 3 === 0){
            console.log(cadena_1);
        } else if(number % 5 === 0){
            console.log(cadena_2);
        } else{
            console.log(number);
            veces++;
        }
    }
    console.log("\n" + veces + " números se han escrito.");
}

cadena_deTexto("Fizz", "Buzz");