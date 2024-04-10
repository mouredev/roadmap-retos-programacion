var recursiveFunction = function(value){
    console.log(value);
    if (value == 0){
        return;
    } else {
        recursiveFunction(value - 1);
    }
};

recursiveFunction(10);

var obtenerFactorial = function(num){
    if (num === 0 || num === 1){
        return 1;
    } else {
        return (num * obtenerFactorial(num - 1));
    }
}
console.log(obtenerFactorial(5));

// Posición Fibonacci
const valorFibonacci = function(posicion){
    if (posicion === 1 || posicion === 2){
        return 1;
    } else {
        return valorFibonacci(posicion - 1) + valorFibonacci(posicion - 2);
    } 
}

console.log(valorFibonacci(10));