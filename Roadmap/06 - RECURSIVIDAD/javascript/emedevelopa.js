//Recursividad

function numeros (n) {
    if (n < 0) {
        return;
    }
    console.log(n);
    numeros (n - 1);
}

numeros(100);

//Extra

function factorial (num) {
    if (num === 0) {
        return 1;
    }
    return num * factorial (num - 1);
} 
console.log(factorial(5));