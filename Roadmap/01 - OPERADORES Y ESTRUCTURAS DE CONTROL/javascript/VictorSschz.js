let suma = 2+2;
console.log('La suma es ' + suma)
let resta = 2-2;
console.log('La resta es ' + resta)
let mult = 2*2;
console.log('La mult es ' + mult)
let division = 2/2;
console.log('La division es ' + division)
let resto = 2%2;
console.log('La resto es ' + resto)

let mayor = 10 > 9;
console.log('Es mayor =' + mayor)
let menor = 10 < 11;
console.log('Es menor =' + menor)
let menorOigual = 10 <= 11;
console.log('Es menorOigual =' + menorOigual)
let mayorOigual = 10 >= 1;
console.log('Es mayorOigual =' + mayorOigual)

let comparativo = 10 == "10";
console.log('Es comparativo (no restrictivo )=' + comparativo)
let comparativo2 = 10 === "10";
console.log('Es comparativo (no restrictivo )=' + comparativo2)
let distino = 10 != "10";
console.log('Es distino (no restrictivo )=' + distino)
let distinto2 = 10 !== "10";
console.log('Es distinto (resctrictivo)=' + distinto2)

let y = 10 === 10 && 2===2;
console.log('Condicion && =' + y)
let o = 10 === 10 || 2===2;
console.log('Condicion  || =' + o)

let x = 2;
console.log('asignacion compuesta suma ' + (x+=2))
let r = 2;
console.log('asignacion compuesta resta ' + (r-=2))
let m= 2;
console.log('asignacion compuesta multiplicacion ' + (m=2))
let d= 2;
console.log('asignacion compuesta division ' + (d*=2))
let restoC= 2;
console.log('asignacion compuesta resto ' + (restoC*=2))

for(let i=10; i<=55;i++){
    if(i%2 ===0){
        if(i=== 16 || i%3 === 0){
            continue;
        }
        console.log(i);
    }
}