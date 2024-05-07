let n: number = 20;
let m: number = 5;
let b: number = 2;

console.log(`[SUMA]: ${n} + ${m} = ${(n+m)}`);
console.log(`[RESTA]: ${n} + ${m} = ${(n-m)}`);
console.log(`[MULTIPLICACIÓN]: ${n} * ${m} = ${(n*m)}`);
console.log(`[DIVISIÓN]: ${n} / ${m} = ${(n/m)}`);
console.log(`[MÓDULO]: ${n} % ${m} = ${(n%m)}`);
console.log(`[POTENCIA]: ${m} ** ${b} = ${(m**b)}`);


console.log(`${n} === ${m} = ${n === m}`);
console.log(`${n} !== ${m} = ${n !== m}`);
console.log(`${n} == ${m} = ${n == m}`);
console.log(`${n} != ${m} = ${n != m}`);
console.log(`${n} > ${m} = ${n > m}`);
console.log(`${n} < ${m} = ${n < m}`);
console.log(`${n} >= ${m} = ${n >= m}`);
console.log(`${n} <= ${m} = ${n <= m}`);

if(b >= m){
    console.log([`[IF] Condición if`]);
}else if(n <= m){
    console.log([`[ELSE IF] Condición else if`]);
}else{
    console.log([`[ELSE] Condición else`]);
}

let opcion = 0;
switch(opcion){
    case 0:
        console.log(`[SWITCH] Opción 0`);
    case 1: 
        console.log(`[SWITCH] Opción 1`);
        break;
    default:
        console.log(`[SWITCH] Opción por defecto`);
        break;
}


for(let i = 0; i < 5; i++){
    console.log(`[${i}] Bucle for`);
}

let j: number = 0;
while(j < 5){
    console.log(`[${j}] Bucle while`);
    j++;
}

let k: number = 0;
do{
    console.log(`[${k}] Bucle do-while`);
    k++;
}while(k === 0)

function imprimirNumeros(n: number, m: number){
    for(; n <= m; n++){
        if((n % 2 === 0) && (n % 3 !== 0) && (n !== 16)){
            console.log(n);
        }
    }
}

imprimirNumeros(10,55);