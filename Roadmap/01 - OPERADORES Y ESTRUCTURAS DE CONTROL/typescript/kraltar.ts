// Tipos de operadores
//Aritméticos

let numb1: number = 10;
let numb2: number = 2;
//suma
console.log( numb1 + numb2);
//resta
console.log( numb1 - numb2);
//multiplicación
console.log( numb1 * numb2);
//división 
console.log( numb1 / numb2);
//modular
console.log(numb1 % numb2);

//Lógicos

let a: boolean = true;
let b: boolean = false;

console.log( a && b ); 
console.log( a || b ); 
console.log( !b ); 

//Asignacion

console.log(numb1 += numb2);
console.log(numb1 -= numb2);
console.log(numb1 *= numb2);
console.log(numb1 /= numb2);
console.log(numb1 %= numb2);

//Identidad

console.log( numb1 === numb2);
console.log( numb1 !== numb2);

//comparacion

console.log(numb1 == numb2);
console.log(numb1 != numb2);
console.log(numb1 < numb2);
console.log(numb1 > numb2);
console.log(numb1 <= numb2);
console.log(numb1 >= numb2);

// Bits

console.log(numb1 & numb2);
console.log(numb1 ^ numb2);
console.log(~numb2);
console.log(numb1 | numb2);



//Etructuras de control
//Ternarios

let height: number = 180;
let result: string = height >= 180 ? 'Eres muy alto' : 'Estas dentro de la media' 
console.log(result);



//condicionales
//switch

let fruitColor = 'morado'
switch(fruitColor) {
    case "rojo":
        console.log(["manzana", "cereza"]);
        break;
    case "amarillo":
        console.log(["platano", "piña"]);
        break;
    case "morado":
        console.log(["mora", "uva"]);
        break;
    default:
        console.log("Color no reconocido");
}

//if
if(height < 180) {
    console.log('Estas dentro de la media');
    
}
//if/else
if(height > 180) {
    console.log('Eres muy alto');
    
} else {
    console.log('Estas dentro de la media');
    
}
// else if
if(height < 180) {
    console.log('Estas dentro de la media');
    
}else if (height < 150){
    console.log('Eres bajito');
}else {
    console.log('Eres muy alto');
    
}

//loops
//ciclo for

for ( let i = 0; i < 10; i++ ){
    console.log(i);
}


//while
let x = 0
while (x < 10) {
    console.log(x);
    x++;
    
}

//do/while

do {
    console.log(x);
    x++
    
} while (x < 10)


//  DIFICULTAD EXTRA (opcional):
// Crea un programa que imprima por consola todos los números comprendidos
// entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
let i = 10
for (i = 10; i <= 55; i++){
    if ( i % 2 === 0 && i !== 16 && i % 3 !== 0)
        console.log(i);
        
}

