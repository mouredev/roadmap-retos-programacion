// Entiende el concepto de recursividad creando una función recursiva que imprima
//  * números del 100 al 0.

function countDown (num) {
    if (num === 1 ){
        return  console.log(1)
    }
    console.log(num)
    return countDown( num - 1) 
}

// console.log(countDown(100))


// extra 

// Utiliza el concepto de recursividad para:
//  * - Calcular el factorial de un número concreto (la función recibe ese número).
//  * - Calcular el valor de un elemento concreto (según su posición) en la 
//  *   sucesión de Fibonacci (la función recibe la posición).

function factorial (num) {
if ( num < 0) {
    return console.log('los numeros negativos no son validos')
}else if(num == 0) {
    return 1
}
console.log(num)
return num * factorial(num -1)
}
console.log(factorial(5))

// ---------------------------

function fibonacci (num) {
if( num < 2 ) return num

return fibonacci( num - 2) + fibonacci(num - 1)
}

console.log(fibonacci(6))

