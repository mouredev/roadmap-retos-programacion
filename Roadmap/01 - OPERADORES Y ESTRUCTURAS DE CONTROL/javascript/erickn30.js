//Operadores aritmeticos
//Suma
console.log(5 + 3);
//Resta
console.log(10 - 5);
//Multiplicacion
console.log(20 * 5);
//Division
console.log( 10 / 8);
//Residuo
console.log(25%4);
//Exponente
console.log(10**3);
//Division numero entero, hay que utilizar el metodo Math.Floor()
//para redondear ya que javascript no tiene un operador especial
console.log(Math.floor(5 / 2));

/*Opeadores comparacion*/

//Mayor que
console.log(15 > 10);
//Menor que
console.log(20 < 15);
//Mayor o igual que
console.log(15 >= 15)
//Menor o igual que 
console.log(20 <= 10)
//Igual
console.log("20" == 20);
//igual estricto
console.log("20" === 20);

//Operadores de asignacion

let mi_numero = 10;
console.log(mi_numero);
mi_numero -= 1
console.log(mi_numero);
mi_numero += 2
console.log(mi_numero);
//iteradores

//While
let iterador = 10
let i = 0
while(i <= iterador){
    console.log(i++);
}
//For
for(let i = 0; i <= 12; i++){
    let numero = 10;
    console.log(`${numero} X ${i} = ${numero * i}`)
}

//operadores logicos
console.log(15>= 10 && "pepito" == "pepito");
console.log(15>= 30 && "pepito" == "pepito");
console.log(30 - 5 == 20 + 5 || "30" === 30)

//Tema extra
for(let numero = 10; numero <= 55; numero++){
    
    if(numero % 2 == 0 && numero !== 16 && numero % 3 !== 0){
        console.log(numero);
    }
}


