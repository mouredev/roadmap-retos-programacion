//función recursiva, se llama así misma hasta que cumple la condición que se le pide
function recursiva(_count:number){
    let count:number=_count;
    console.log(count);
    count--;
    if(count>=0){
        recursiva(count);
    }
}
recursiva(100);

//EXTRA
let numero:number=7;
function getfactorial(num:number){
    if(num==0){
        return 1;
    } 
    return num * getfactorial(num-1);
}

function getFibonacci(posicion:number){
    if(posicion<=1){
        return posicion;
    } 
    return getFibonacci(posicion-1)+getFibonacci(posicion-2);
}

console.log(`la posición ${numero} de fibonacci es ${getFibonacci(numero)}`)
console.log(`el factorial de ${numero} es ${getfactorial(numero)}`);