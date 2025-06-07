//operadores

console.log(`10 + 3 = ${10 + 3}`)   //SUMA
console.log(`10 - 3 = ${10 - 3}`)   //RESTA
console.log(`10 / 3 = ${10 / 3}`)   //DIVISION  
console.log(`10 * 3 = ${10 * 3}`)   //MULTIPLICACION
console.log(`10 % 3 = ${10 % 3}`)   //MODULO - RESIDUO DE LA DIVISION
console.log(`10 ** 3 = ${10 ** 3}`)   //EXPONENCIA

let a = 10
let b = 5
//a = a ...
console.log(a += b)
console.log(a -= b)
console.log(a *= b)
console.log(a /= b)
console.log(a %= b)
console.log(a **= b)

//operador ternario
let x = 0
let y = 1
const res = y < x ? "X es mayor" : "Y es menor"
console.log(res)

variable = "gg"
variable2 = "GG"
//vars compara si son iguales 
vars = variable == variable2
console.log(vars)

const edad = 2

switch(edad){
    case 1:
        console.log("tienes 1 año")
        break
    case 2:
        console.log("tienes 2 años")
}

//RETO EXTRA
for(let i = 10;i <= 55; i++){
    if(i === 16 || i % 3 === 0 || i % 2 !== 0){

        //continue se salta esta iteracion y continua a la siguiente
        continue
        
    }
    console.log(i)
}