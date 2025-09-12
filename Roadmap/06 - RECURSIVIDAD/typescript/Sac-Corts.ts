function printNumbers(num: number): void {
    if (num < 0) return;
        console.log(num);
        printNumbers(num - 1);
}

printNumbers(100);

// *** Extra Exercise *** //
function factorial(n: number): number {
    if (n <= 1) {
        return 1;
    } 
    return n * factorial(n - 1);
}

console.log(factorial(5));

function fibonacci(n: number): number {
    if (n <= 1) return n; 
    return fibonacci(n - 1) + fibonacci(n - 2); 
}


console.log(fibonacci(4));