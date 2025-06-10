(() => {
    // EJERCICIO:
    // Entiende el concepto de recursividad creando una función recursiva que imprima números del 100 al 0.
    function recursiveFunction(num:number):void {
        console.log(num)
        if(num > 0) {
            recursiveFunction(num-1)
        }
    }
    // DIFICULTAD EXTRA (opcional):
    // Utiliza el concepto de recursividad para:
    // - Calcular el factorial de un número concreto (la función recibe ese número).
    function factorial(num:number) {
        if(num <= 1) {
            return 1
        } else {
            return num * factorial(num-1)
        }
    }
    // - Calcular el valor de un elemento concreto (según su posición) en la sucesión de Fibonacci (la función recibe la posición).
    function fibonacci(posicion: number): number { 
        if (posicion <= 1) { 
            return posicion
        } else { 
            return fibonacci(posicion - 1) + fibonacci(posicion - 2); 
        } 
    }
})()