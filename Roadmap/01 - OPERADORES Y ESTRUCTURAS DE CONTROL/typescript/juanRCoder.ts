let num1: number = 10;
let num2: number = 12;
let str1: string = 'Hola';

// OPERADORES ARITMETICOS:
// (+) (-) (*) (/) (**) (%) = suma, resta, multiplicar, dividir, potencia, resto.
// (+=) (-=) (*=) (/=)	=> usados para operar en los valores de las variables.

console.log(num1 + num2) // 22
console.log(num1 - num2) // -2
console.log(num1 * num2) // 120
console.log(num1 / num2) // 0.8333333333333334
console.log(num1 ** num2) // 1000000000000
console.log(num1 % num2) // 10

console.log(str1 += ' Pedro') // Hola Pedro
console.log(num1 -= num2) // 10
console.log(num1 *= num2) // 120
console.log(num1 /= num2) // 10

// OPERADORES LOGICOS:
// (&&) (||) (!) = and(y) - o(or) - contrario,not(!).

console.log(str1 && 1 + 1)  //Ambas condiciones deben ser son true = true
console.log(str1 || 1 + 1)  //Basta con que una condicion sea true = true
console.log(!1)  //Si es true = false y viceversa


// OPERADORES DE COMPARACIÓN:
// (==) (!=) (===) (!==)	= igual - distinto - exactamante igual - exactamente distinto. 
// (>)  (<)  (>=)  (<=)	= mayor - menor - mayor e igual - menor e igual.

console.log(num1 == num2) // false
console.log(num1 != num2) // true
console.log(num1 === num2) // false
console.log(num1 !== num2) // true
console.log(num1 > num2) // false
console.log(num1 < num2) // true
console.log(num1 >= num2) // false
console.log(num1 <= num2) // true


// ESTRUCTURAS DE CONTROL
// if-else, si la condicion se cumple en la condicion if , ejecuta bloque if si no el bloque else.
if (15 < 20) {
    console.log('15 es menor que 20')
} else {
    console.log('20 es mayor que 15')
}

// switch, bloque en la cual se aplica diferentes casos segun la expresion
switch(15 < 20){
    case true:
        console.log('15 es menor que 20')
        break
    case false:
        console.log('20 es mayor que 15')
        break
    default:
        console.log('No se cumplio ninguno de los casos')
}

// For, iterable que se ejecuta segun un rango de numeros
// Se compone de (inicializacion, condicion, aumento/decremento)
for (let i=0; i<10; i++){
    console.log(i)
}

// While, igual que el for, iterable que se ejecuta indefinidamente hasta no cumplir la condicion
// OJO: agregarle un deliminador ya sea incremento/decremento
let i = 10
while(i < 10){
    console.log(i);
    i++;
}

/*
* DIFICULTAD EXTRA (opcional):
* Crea un programa que imprima por consola todos los números comprendidos
* entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
*
* Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
*/
const isNumbers = ():void => {
    const list: number[] = [];
    for (let i=10; i<=55; i++){
        if(i % 3 == 0 || i == 16){
            continue;
        }
        list.push(i);
    }
    console.log(list);
}

isNumbers();
// [
//     10, 11, 13, 14, 17, 19, 20, 22, 23,
//     25, 26, 28, 29, 31, 32, 34, 35, 37,
//     38, 40, 41, 43, 44, 46, 47, 49, 50,
//     52, 53, 55
// ]
