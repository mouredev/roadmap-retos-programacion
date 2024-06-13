//EJERCICIO
//**OPERADORES**
//-Aritmeticos-
let num1 = 4;
let num2 = 2;

console.log(num1 + num2); //suma
console.log(num1 - num2); //resta
console.log(num1 * num2); //multiplicacion
console.log(num1 / num2); //division
console.log(num1 % num2); //resto
console.log(num1 ** num2); //potencia

//-De asignacion-
let a = 20;

console.log((a += 2)); //igual a si mismo mas
console.log((a -= 1)); //igual a... menos
console.log((a *= 2)); //igual a... multiplicado por
console.log((a /= 4)); //igual a... entre

///-De comparacion-
let firstValue = 10;
let secondValue = '10';

console.log(firstValue == secondValue); //equivalente
console.log(firstValue === secondValue); //igual
console.log(firstValue != secondValue); //no equivalente
console.log(firstValue !== secondValue); //no igual

let num3 = 4;
let num4 = 2;

console.log(num3 > num4); //mayor que
console.log(num3 < num4); //menor que
console.log(num3 >= num4); //mayor o igual que
console.log(num3 <= num4); //menor o igual que

//-Logicos-
const myBool1 = true;
const myBool2 = false;
const myBool3 = true;

console.log(myBool1 && myBool3); //And
console.log(myBool1 || myBool2); //Or
console.log(!myBool2); //Negacion

//-De incremento y decremento-
let count = 0;
console.log(++count);
console.log(count); //pre-incremento

let count2 = 0;
console.log(count2++);
console.log(count2); //post-incremento

let count3 = 0;
console.log(--count3);
console.log(count3); //pre-decremento

let count4 = 0;
console.log(count4--);
console.log(count4); //post-decremento

//-Operadores ternarios-
let num5 = 7;

num5 > 0 ? console.log('Numero positivo') : console.log('Numero negativo');

num5 = -5;

num5 > 0 ? console.log('Numero positivo') : console.log('Numero negativo');

//**ESTRUCTURAS DE CONTROL**

//-Condicionales-
//if
let totalPoints = 5003;

console.log('Nivel completado!');
if (totalPoints > 5000) {
	console.log('Logro desbloqueado: maestro espadachin');
}

//if else
function checkEvenNum(n) {
	if (typeof n === 'number') {
		if (n % 2 === 0) {
			console.log(`${n} es par`);
		} else {
			console.log(`${n} no es par`);
		}
	} else {
		console.log('Valor invalido');
	}
}

checkEvenNum(7);

//Switch
let clima = 'nublado';
switch (clima) {
	case 'lluvioso':
		console.log('Usa impermeable');
		break;
	case 'nublado':
		console.log('Usa abrigo. Puede que llueva');
		break;
	case 'soleado':
		console.log('Sal tranquilo');
		break;
	default:
		console.log('No necesitas impermeable');
}

//-Bucles-
//For
for (let i = 0; i <= 5; i++) {
	console.log(i);
}

//While
let n = 5;

while (n < 10) {
	console.log(n);
	n++;
}

//Do/While
let m = 10;

do {
	console.log(m);
	m--;
} while (m > 0);

//EXTRA
for (let i = 10; i <= 55; i++) {
	if (i !== 55) {
		if (i !== 16 && i % 3 !== 0 && i % 2 === 0) {
			console.log(i);
		}
	} else {
		console.log(i);
	}
}
