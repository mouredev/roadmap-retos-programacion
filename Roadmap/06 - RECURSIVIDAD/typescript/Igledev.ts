// Ejercicio 1º
    function recursiva(num : number) : void{
        if(num < 0){
            return;
        }
        console.log(num);

        recursiva(num - 1);
    }

// Ejercicio Extra
    // Factorial
        function calcularFactorial(numero : number) : number{
            if(numero === 1 || numero === 0){
                return 1;
            }

            return numero * calcularFactorial(numero - 1);
        }

        let numeroFactorial : number = 5;
        console.log(calcularFactorial(numeroFactorial));

    // Fibonnacci
        function calcularFibonacci(num : number){
            if(num <= 1){
                return 1;
            }

            return calcularFibonacci(num - 1) + calcularFibonacci(num - 2);
        }

        let posicion : number = 6;
        console.log('La ' + posicion + 'º posición es: ' + calcularFibonacci(posicion));