console.log('-------------asignación-------------');

let num = 50;

console.log(`El número inicial es ${num}\n`)

console.log(`Asignación (num = 25): ${num = 25}`);
console.log(`Asignación por suma (num + 25): ${num += 25}`);
console.log(`Asignación por resta (num - 4): ${num -= 4}`);
console.log(`Asignación por multiplicación (num * 3): ${num *= 3}`);
console.log(`Asignación por división (num / 3): ${num /= 3}`);
console.log(`Asignación por residuo (num % 8): ${num %= 8}`);
console.log(`Asignación por exponenciación (num ** 7): ${num **= 7}`);
console.log(`Asignación de desplazamiento a la izquierda (num << 3): ${num <<= 3}`);
console.log(`Asignación de desplazamiento a la derecha (num >> 4): ${num >>= 4}`);//si hay valores negativos basta con colocar >>> para evitar
console.log(`Asignación AND bit a bit (num & 40000): ${num &= 40000}`);
console.log(`Asignación XOR bit a bit (num ^ 32): ${num ^= 32}`);
console.log(`Asignación OR bit a bit (num | 74): ${num |= 74}`);
console.log(`Asignación AND lógico (num && 65): ${num &&= 65}`);
console.log(`Asignación OR lógico (num || null) ${num ||= 43}`);//no cambia porque la izquierda es true
console.log(`Asignación de anulación lógica (num ?? 43) ${num ??= 43}\n`);// tampoco cambia porque es true

console.log('-------------desestructuración----------------');

const array = [1, 3, 5, 6, 8];

const [valor1, valor2, valor3] = array;
console.log(valor3);//imprime 5

console.log('-------------operadores de comparación-------');
let num1 = 3
let num2 = 4

console.log(`estos son los numeros num1 = ${num1} y num2 = ${num2}\n`)

console.log(`comparación de igualdad débil:\nnum1 == num2: ${num1 == num2}\n`);
console.log(`comparación de igualdad fuerte:\nnum1 === num2: ${num1 === num2}\n`);
console.log(`comparación de desigualdad débil:\nnum1 != num2: ${num1 != num2}\n`);
console.log(`comparación de desigualdad fuerte:\nnum1 !== num2: ${num1 !== num2}\n`);
console.log(`mayor que:\nnum1 > num2: ${num1 > num2}\n`);
console.log(`menor que:\nnum1 < num2: ${num1 < num2}\n`);
console.log(`mayor o igual que:\nnum1 >= num2: ${num1 >= num2}\n`);
console.log(`menor o igual que:\nnum1 <= num2: ${num1 <= num2}\n`);

console.log('-------------operadores aritméticos-------');

let x = 84;
let y = 94;

console.log(`Valores iniciales: x = ${x} y = ${y}\n`);
console.log(`residuo:\n x % y: ${x % y} <= da el residuo de una división`);
console.log(`incremento:\n ++x: ${++x} <= se incrementa a si mismo 1 vez el operador se pone al inicio para que muestre el valor`);
console.log(`decremento:\n --y: ${--y} <= decrementa 1 vez`);
console.log(`negación unaria:\n -x: ${-x} <= se niega el número, esto quiere decir que se vuelve negativo`);
console.log(`positivo unario:\n +x: ${+x} <= se coloca el número en positivo`);
console.log(`operador de exponenciación:\n x**y: ${x**y}\n`);

console.log(`-------------operadores bit a bit---------`);

x = 13;
y = 52;

console.log(`valores iniciales ${x} y ${y}\n`);
console.log(`AND a nivel de bits:\n x & b = ${x & y}`);
console.log(`OR a nivel de bits:\n x | y = ${x | y}`);
console.log(`XOR a nivel de bits:\n x ^ y = ${x ^ y}`);
console.log(`NOT a nivel de bits:\n ~x = ${~x}`);
console.log(`Desplazamiento a la izquierda:\n x << y = ${x << y}`);
console.log(`Desplazamiento a la derecha:\n x >> y = ${x >> y}\n`);

console.log('----------operadores lógicos--------------');

let bool = true;
let bool2 = false;

console.log(`operador &&:\n bool && bool2 = ${bool && bool2} <= No se cumple porque ambos son diferentes`);
console.log(`operador ||:\n bool || bool2 = ${bool || bool2} <= Este si devuelve true porque uno de los dos es true`);
console.log(`operador !:\n !bool = ${!bool} <= deuvelve false porque lo invierte\n`);

console.log('-----------operador de cadena-------------');

let animal1 = 'dog';
let animal2 = 'cat';

console.log('I have 2 pets' + ' ' + animal1 + ' and ' + `${animal2}\n`);

console.log('-------operador condicional ternario------');

let ana = 'bird'
const result = ana === 'dog' 
    ? 'Es su mascota' 
    : 'No es su mascota';

console.log(`${result}\n`);

console.log('-------------operador in------------------');

const cars = [
    car1 = {
        make: 'Honda', 
        model: '2027'
    }, 
    car2 = {
        make: 'Suzuki', 
        model: '2027'
        }, 
    car3 = {
        make: 'Chevrolet', 
        model: '2027'
    }
];

console.log(JSON.stringify(cars, null, 3))

console.log(4 in cars ,'\n')

//Estructuras de control

console.log('----------------if-else-------------------');


function clasificarEdad(edad) {
    if (edad < 0){
        console.log('Edad invalida')
    } else if(edad <= 12) {
        console.log('Niño/a')
    } else if(edad <= 17){
        console.log('Adolescente')
    } else if(edad <= 59){
        console.log('Adulto')
    } else{
        console.log('Adulto mayor')
    }
}

clasificarEdad(60);

console.log('----------------switch--------------------');

let color = 2

switch (color) {
    case 1:
        console.log('Color elegido: amarillo')
        break;

    case 2:
        console.log('Color elegido: Verde')
        break;

    case 3:
        console.log('Color elegido: Azul')
        break;

    default:
        break;
}

console.log('------------------for---------------------');

let numeral = ''

for(let i = 0; i < 10; ++i){
    let inglz = numeral += '#';
    console.log(inglz)
}

console.log('-----------------while--------------------');

let f = 0
let conteo = 5

while (f < 5){
    f++
    console.log(conteo--);
    if (f ==5){
        console.log('!Despegue')
    }
}


console.log('-------------RETO OPCIONAL----------------');
for (let i = 10; i <= 55; i++){
    if (i !== 16 && i%3 !== 0){
        console.log(i)
    }
}