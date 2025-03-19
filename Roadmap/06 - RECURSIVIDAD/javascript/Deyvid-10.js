function recursividad(n)
{
    if(n >= 0)
    {
        console.log(n);
        recursividad(n-1)
    } 
}

recursividad(100)

// DIFICULTAD EXTRA

function factorial(n) {
    if(n < 0)
    {
        return "Los numero negativos no tienen factorial"
    }
    else if(n == 0) 
    {
       return 1 
    } 
    else 
    { 
       return n * factorial(n-1)
    }

 }

console.log(factorial(5));


let fibo = [0, 1]
let indice = 0
function fibonacci(posicion)
{
    if(indice < posicion)
    {
        fibo.push(fibo[indice] + fibo[indice + 1])
        indice++  
        fibonacci(posicion)
        return fibo[posicion - 1]
    }
}

console.log(fibonacci(5));