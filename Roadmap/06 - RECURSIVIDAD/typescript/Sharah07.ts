// Función recursiva: 
//Estas funciones tienen un caso base (condición que al cumplirse detiene la función)
// y un caso recursivo (caso que modifica el argumento con cada llamada a la función)
// Esta función se llama a si misma repetidamente cambiando su argumento 
// según se especifique hasta cumplir su caso base.
// Esto no modifica el argumento fuera de la función.

function recursiva(num) { // el argumento es 5
    if(num < 0) return;
    console.log(num);
    return recursiva(--num); // ahora el argumento pasa a valer 4 (solo dentro de la función) y tras cada llamada se decrementa 
}
recursiva(100);

//Extra:
//Calcular factorial.

function factorial(num):number{
    if(num < 0){
        console.log('Valor no valido') 
        return 0;  
    } 
    if(num == 1 || num == 0) return 1;
    return num * factorial(num - 1); //Mientras la función se llama a si misma, 
    // únicamente realiza la reducción del argumento(num-1) que se almacena en la pila de ejecución, 
    // 5 4 3 2 1(el caso base retorna 1) al llegar al caso base empieza el proceso de 
    // retorno(realiza la operación de retorno) en orden inverso y retorna el resultado.  

}
console.log(factorial(5));


function fibonacci(num:number):number{
    if(num <= 0){
        console.log('Posición invalida');
        return 0;
    } 
    if(num <= 2) return num-1;
    return fibonacci(num-1) + fibonacci(num-2);

}

console.log(fibonacci(6));
