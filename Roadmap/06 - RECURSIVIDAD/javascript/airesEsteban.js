function cuentaAtras(num){
    if (num >= 0){
        console.log(num)
        cuentaAtras(num-1)
    }
}

cuentaAtras(100)

// Dificultad extra

function factorial(num){
    if (num < 0){
        console.log("No se permiten usar numero negativos")
        return 0
    }else if(num == 0){
        return 1
    }else{
        return num * factorial(num-1)
    }
}

console.log(factorial(5))

function fibonacci(pos){
    if (pos <= 0){
        console.log("La posisicion debe ser mayor a 0")
        return 0
    }else if(pos==1){
        return 0
    }else if(pos ==2){
        return 1
    }else{
       return fibonacci(pos - 1) + fibonacci (pos - 2)
    }
}

console.log(fibonacci(5))