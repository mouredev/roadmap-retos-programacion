
let suma = 2 + 2    
let resta = suma -2
let multiplicacion = suma * 2   
let division = multiplicacion / 2   
let resto = division % 2    
let incrementa = suma++
let decrementa = resta-- 
let exponente = 2 ** 3

let asignacion = 2 = 2
let asignacionSuma = 2 += 2
let asignacionResta = 2 -= 2
let asignacionMultiplicacion = 2 *= 2
let asignacionDivision = 2 /= 2
let asignacionResto = 2 %= 2
let asignacionExponente = 2 **= 2

let igualdad = 2 == 2
let igualdadEstricta = 2 === 2
let desigualdad = 2 != 2    
let desigualdadEstricta = 2 !== 2
let mayorQue = 2 > 2
let menorQue = 2 < 2
let menorQueOIgual = 2 <= 2
let mayorQueOIgual = 2 >= 2
let and = 2 && 2
let or = 2 || 2
let not = !2

if(suma > 2){
    console.log("Es mayor")
}else{
    console.log("Es menor")}

switch(suma){
    case 1: console.log("Es 1");
    break;
    default: console.log("Es otro valor")   
}

for(let i = 0; i<10; i++){
    console.log(i)
}

while(suma < 10){
    console.log(suma)
    suma++
}

do{
    console.log(suma)
    i++
}while(i<5)

    // Programa para imprimir por consola

const printNumbers =(num1, num2)=>{

    while(num1 < num2){

        if(num1 === 16 || num1%3 === 0){
            num1++
            continue
        }
        
        if(num1 >= 10 && num1 <=55){
            console.log(num1)
        }else if(num1%2 === 0){
            console.log(num1)
        }
        num1++
    }
}

printNumbers(4, 90);

