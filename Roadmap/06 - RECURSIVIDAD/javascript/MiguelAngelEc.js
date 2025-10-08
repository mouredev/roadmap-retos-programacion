// Recursividad

function returnNumber(n){
    if (n === 0) return;
    console.log(n);
    returnNumber(n - 1);
}
returnNumber(100);

// Recursividad con Factorila

function factoria(n){
    if(n === 0) return 1;
    return n *(n - 1);
}
console.log(factoria(5));

// Fibonacci

function Fibonacci(n) {
    return (n === 0 || n === 1) ? n : Fibonacci(n - 1) + Fibonacci(n - 2);
}

console.log(Fibonacci(10));