// Función sin parámetros ni retorno
function sinParametros() {
    console.log("Esta función no tiene parámetros ni devuelve nada");
}

// Función con un parámetro y sin retorno
function conUnPar(parametro) {
    const nombre = "Juan";
    console.log(`Hola, ${nombre}`);
}

// Función con múltiples parámetros y sin retorno
function conMultiplesParams(a, b, c) {
    console.log(`Recibí: ${a}, ${b}, ${c}`);
}

// Función con parámetros y retorno
function suma(a, b) {
    return a + b;
}

// Función anidada
function funcionAnidata() {
    function subFuncion() {
        console.log("Soy una función anidada");
    }
    console.log("Estoy en la función principal");
    subFuncion();
}


let globalVar = "Esta es una variable global";

// Función que usa la variable global
function usarVariableGlobal() {
    globalVar += " modificada";
    console.log(globalVar);
}

sinParametros();
conUnPar("Carlos");
conMultiplesParams(1, 2, 3);
console.log(suma(5, 7));
funcionAnidata();
usarVariableGlobal();


const localVar = "Esta es una variable local";

// Función que usa la variable local
function usarVariableLocal() {
    console.log(localVar);
}
usarVariableLocal(); // Esto causaría un error porque localVar está fuera del alcance


// Ejercicio Extra
function imprimirMultiplos(texto1, texto2) {
    let contador = 0;
    
    for (let i = 1; i <= 100; i++) {
        if (i % 3 === 0 && i % 5 !== 0) {
            console.log(texto1);
        } else if (i % 5 === 0 && i % 3 !== 0) {
            console.log(texto2);
        } else if (i % 3 === 0 && i % 5 === 0) {
            console.log(`${texto1}${texto2}`);
        } else {
            console.log(i);
        }
        
        contador++;
    }
    
    return contador;
}

const resultado = imprimirMultiplos("Tres", "Cinco");
console.log(`\nSe imprimieron ${resultado} números.`);

