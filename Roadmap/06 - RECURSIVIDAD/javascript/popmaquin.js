
/*---Recursividad---*/
function imprimirN(num){
    if (num>=0){
        console.log(num);
        return imprimirN(num-1)
    }
     
}
imprimirN(5);

//---Dificulta extra
function factorial(numero){
    if (numero==0){
        return 1;
    }else if(numero<0){
        return -1;
    }else{
        return (numero*factorial(numero-1));
    }
}

console.log(factorial(5)); //120

    //---Sucesion de fibonacci
    function fibonacci(num){
        if(num<2){
            return num;
        }else{
            return ((fibonacci(num-1)+fibonacci(num-2)))
        }
    }

    console.log(fibonacci(10));