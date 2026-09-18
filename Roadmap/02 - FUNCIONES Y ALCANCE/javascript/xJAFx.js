let variableGlobal = "This is a global Variable!";


function vacia() {

} 

console.log(vacia());

const saludo1 = () => "Hello";

console.log(saludo1());

function saludo2(greet) {
    return greet
}

console.log(saludo2("Hi"));

function suma1 (num1, num2) {
    console.log(variableGlobal);
    return num1 + num2;
}

console.log(suma1(3, 5));

const suma2 = (num2, num3) => num2 + num3;

console.log(suma2(5, 7));

function externa(numeroExterno) {

    function interna(numeroInterno) {
        console.log(numeroExterno * numeroInterno);
    }

    interna(4);
}

externa(9);

console.log(isFinite(10 * 400));

function prueba() {
    let variableLocal = "This is a local Variable!";
    console.log(variableLocal);
    console.log(variableGlobal);
}

prueba();

/*

El siguiente intento de acceso a variableLocal dará error porque no existe fuera de la función en que es creada.
console.log(variableLocal);

*/

// Ejercicio Extra

function contadorACien(str1, str2) {
    str1 = "El número es múltiplo de 3";
    str2 = "El número es múltiplo de 5";
    let count = 0;

    for(let i = 1; i <= 100; i++) {
        if (i % 3 === 0 && i % 5 === 0) {
            console.log(str1 + " y " + str2);
        } else if(i % 3 === 0) {
            console.log(str1);
        } else if(i % 5 === 0) {
            console.log(str2);
        } else {
            console.log(i);
            count++;
        }
    }

    return count;
}

console.log(contadorACien());