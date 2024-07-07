function imprimir(n){
    if(n >= 0) {
        console.log(n);
        imprimir(n-1);
    }
}

imprimir(100);


///////////////////////////////////////////////////////////
//          EXTRA


function factorial(numero){
    if(numero === 0){
        return 1;
    }
    return numero * factorial(numero-1)
}

console.log(factorial(5))

function fibonacci(pos){
    if(pos === 0) return 0
    if(pos === 1) return 1
    return fibonacci(pos-1) + fibonacci(pos-2);
}

console.log(fibonacci(8));