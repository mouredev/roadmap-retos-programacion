//EJERCICIO
//OPERADORES
//-Aritmeticos-
let num: number = 20;
let num1: number = 2;

const add = num + num1;
const multiplication = num * num1;
const substract = num - num1;
const division = num / num1;
const remainder = num % num1;
const exponent = num ** num1;

console.log(add); //suma
console.log(multiplication); //multiplicación
console.log(substract); //resta
console.log(division); //división
console.log(remainder); //resto
console.log(exponent); //potencia

//-De asignacion-
let num2: number = 20;

console.log((num2 += 2)); //igual a si mismo mas
console.log((num2 -= 1)); //igual a... menos
console.log((num2 *= 2)); //igual a... multiplicado por
console.log((num2 /= 4)); //igual a... entre
console.log(-num2);

///-De comparacion-
let firstValue: number = 10;
let secondValue: number = 10;

console.log(firstValue == secondValue); //equivalente
console.log(firstValue === secondValue); //igual
console.log(firstValue != secondValue); //no equivalente
console.log(firstValue !== secondValue); //no igual

let num3: number = 4;
let num4: number = 2;

console.log(num3 > num4); //mayor que
console.log(num3 < num4); //menor que
console.log(num3 >= num4); //mayor o igual que
console.log(num3 <= num4); //menor o igual que

//-Logicos-
const myBool1: boolean = true;
const myBool2: boolean = false;
const myBool3: boolean = true;

console.log(myBool1 && myBool3); //And
console.log(myBool1 || myBool2); //Or
console.log(!myBool2); //Negacion

//-De incremento y decremento-
let count: number = 0;
console.log(++count);
console.log(count); //pre-incremento

let count2: number = 0;
console.log(count2++);
console.log(count2); //post-incremento

let count3: number = 0;
console.log(--count3);
console.log(count3); //pre-decremento

let count4: number = 0;
console.log(count4--);
console.log(count4); //post-decremento

//-Operadores ternarios-
let num5: number = 7;

num5 > 0 ? console.log('Numero positivo') : console.log('Numero negativo');

num5 = -5;

num5 > 0 ? console.log('Numero positivo') : console.log('Numero negativo');

//ESTRUCTURAS DE CONTROL
//-Condicionales-
//if
let totalPoints: number = 5003;

console.log('Nivel completado!');
if (totalPoints > 5000) {
	console.log('Logro desbloqueado: maestro espadachin');
}

//if else
let checkEvenNum = (num: number) => {
	if (num % 2 === 0) {
		console.log(`${num} es par`);
	} else {
		console.log(`${num} no es par`);
	}
};

//Switch
let clima: string = 'nublado';
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
let n: number = 5;

while (n < 10) {
	console.log(n);
	n++;
}

//Do/While
let m: number = 10;

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
