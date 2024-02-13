
/*
* EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
*/
        // recursividad
function conteo(n){
    if(n== 1){
        return n
    }else{
        console.log(n)
        return conteo(n-1)
    }
}
console.log(conteo(100))



        // dificultad extra
function factorial(n){
    if(n<= 1){
        return 1
    }else{
        return n * factorial(n-1)
    }
}
console.log(factorial(4))
