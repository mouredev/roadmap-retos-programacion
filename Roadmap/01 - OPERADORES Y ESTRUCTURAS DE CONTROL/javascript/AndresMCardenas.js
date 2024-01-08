// Operadores y Estructuras de Control

//Operadores aritméticos

//Suma
let suma = 5 + 5;// se asigna el valor de la suma a la variable suma
console.log(suma); // se imprime el valor de la variable suma

//Resta
let resta = 10 - 5;// se asigna el valor de la resta a la variable resta
console.log(resta); // se imprime el valor de la variable resta

//Multiplicación
let multiplicacion = 5 * 5;// se asigna el valor de la multiplicacion a la variable multiplicacion
console.log(multiplicacion); // se imprime el valor de la variable multiplicacion

//División
let division = 10 / 5;
console.log(division);

//Módulo
let modulo = 10 % 5;
console.log(modulo);

//Incremento
let incremento = 10;
incremento++;// incremento se le suma 1
console.log(incremento);

//Decremento
let decremento = 10;
decremento--;// decremento se le resta 1
console.log(decremento);

//Operadores de asignación

//Asignación
let asignacion = 10;
console.log(asignacion);

//Suma y asignación
let sumaAsignacion = 10;
sumaAsignacion += 5;//sumaAsignacion = sumaAsignacion + 5
console.log(sumaAsignacion); // se imprime el valor de la variable sumaAsignacion

//Resta y asignación
let restaAsignacion = 10;
restaAsignacion -= 5;//restaAsignacion = restaAsignacion - 5
console.log(restaAsignacion); // se imprime el valor de la variable restaAsignacion

//Multiplicación y asignación
let multiplicacionAsignacion = 10;
multiplicacionAsignacion *= 5;//multiplicacionAsignacion = multiplicacionAsignacion * 5
console.log(multiplicacionAsignacion); // se imprime el valor de la variable multiplicacionAsignacion

//División y asignación
let divisionAsignacion = 10;
divisionAsignacion /= 5;//divisionAsignacion = divisionAsignacion / 5
console.log(divisionAsignacion); // se imprime el valor de la variable divisionAsignacion

// Módulo y asignación
let moduloAsignacion = 10;
moduloAsignacion %= 5;//moduloAsignacion = moduloAsignacion % 5
console.log(moduloAsignacion); // se imprime el valor de la variable moduloAsignacion

//Operadores de comparación

//Igualdad
let igualdad = 10 == 10;
console.log(igualdad);// se imprime true el valor de la variable igualdad

//Igualdad estricta
let igualdadEstricta = 10 === 10;
console.log(igualdadEstricta);// se imprime true el valor de la variable igualdadEstricta

let igualdadEstricta2 = 10 === '10';
console.log(igualdadEstricta2);// se imprime false el valor de la variable igualdadEstricta2

//Desigualdad
let desigualdad = 10 != 10;
console.log(desigualdad);// se imprime false el valor de la variable desigualdad

//Desigualdad estricta  
let desigualdadEstricta = 10 !== 10;
console.log(desigualdadEstricta);// se imprime false el valor de la variable desigualdadEstricta

let desigualdadEstricta2 = 10 !== '10';
console.log(desigualdadEstricta2);// se imprime true el valor de la variable desigualdadEstricta2

//Mayor que 
let mayorQue = 10 > 5;  
console.log(mayorQue);// se imprime true el valor de la variable mayorQue

//Menor que
let menorQue = 10 < 5;
console.log(menorQue);// se imprime false el valor de la variable menorQue

//Mayor o igual que 
let mayorOIgualQue = 10 >= 10;
console.log(mayorOIgualQue);// se imprime true el valor de la variable mayorOIgualQue

//Menor o igual que
let menorOIgualQue = 10 <= 5;
console.log(menorOIgualQue);// se imprime false el valor de la variable menorOIgualQue

//Operadores lógicos

//AND
let and = (10 > 5) && (10 < 20);
console.log(and);// se imprime true el valor de la variable and

//OR
let or = (10 > 5) || (10 > 20);
console.log(or);// se imprime true el valor de la variable or

//NOT
let not = !(10 > 5);
console.log(not);// se imprime false el valor de la variable not

//Operadores de concatenación

//Concatenación
let concatenacion = 'Hola ' + 'Mundo';
console.log(concatenacion);// se imprime Hola Mundo el valor de la variable concatenacion

//Concatenación y asignación
let concatenacion2 = 'Hola '; 
concatenacion2 += 'Mundo';//concatenacion2 = concatenacion2 + 'Mundo'
console.log(concatenacion2);// se imprime Hola Mundo el valor de la variable concatenacion2

//Operadores ternarios
// Ejemplo 1: Asignar un valor a una variable basado en una condición
let edad = 15;
let tipo = edad >= 18 ? 'Adulto' : 'Menor';
console.log(tipo); // Se imprime 'Menor'

// Ejemplo 2: Elegir qué función ejecutar basado en una condición
let saludable = true;
saludable ? console.log('Puedes salir a correr') : console.log('Deberías descansar');

// Ejemplo 3: Elegir qué valor retornar en una función
function obtenerPrecio(tieneDescuento) {
  return tieneDescuento ? 9.99 : 19.99;
}
console.log(obtenerPrecio(true)); // Se imprime 9.99

// Operadores de flujo

//If
let edad2 = 15;
if (edad2 >= 18) {
  console.log('Eres mayor de edad');
}

//If...else
let edad3 = 15;
if (edad3 >= 18) {
  console.log('Eres mayor de edad');
} else {
  console.log('Eres menor de edad');
}

//If...else if...else
let edad4 = 15;
if (edad4 >= 18) {
  console.log('Eres mayor de edad');
} else if (edad4 >= 13) {
  console.log('Eres un adolescente');
} else {
  console.log('Eres un niño');
}

//Switch
let dia = 3;
switch (dia) {
  case 1:
    console.log('Lunes');
    break;
  case 2:
    console.log('Martes');
    break;
  case 3:
    console.log('Miércoles');
    break;
  case 4:
    console.log('Jueves');
    break;
  case 5:
    console.log('Viernes');
    break;
  case 6:
    console.log('Sábado');
    break;
  case 7:
    console.log('Domingo');
    break;
  default:
    console.log('Día inválido');
}// se imprime Miércoles el valor de la variable dia

//For se ejecuta un número determinado de veces
for (let i = 0; i < 5; i++) {
  console.log(i);
}// se imprime 0 1 2 3 4

//While se ejecuta prieramente si la condición es verdadera, y se detiene cuando la condición es falsa
let i = 0;
while (i < 5) {
  console.log(i);
  i++;
}// se imprime 0 1 2 3 4

//Do...while se ejecuta al menos una vez, y luego se ejecuta mientras la condición sea verdadera
let i2 = 0;
do {
  console.log(i2);
  i2++;
} while (i2 < 5);// se imprime 0 1 2 3 4

/*
 DIFICULTAD EXTRA(opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
  * entre 10 y 55(incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
*/

console.log('DIFICULTAD EXTRA(opcional):');

for (let i = 10; i <= 55; i++) {//extra inicia en 10 y se ejecuta mientras extra sea menor que 56
  if (i % 2 === 0 && i !== 16 && i % 3 !== 0) { //si el numero es par y no es 16 y no es multiplo de 3
    console.log(i); //imprime el numero en extra
  }
}

console.log('Ejericio con While');

let extra = 10; //extra inicia en 10
while (extra <= 55) { //se ejecuta mientras extra sea menor que 56
  if (extra % 2 === 0 && extra !== 16 && extra % 3 !== 0) { //si el numero es par y no es 16 y no es multiplo de 3
    console.log(extra); //imprime el numero en extra
  }
  extra++; //extra se incrementa en 1
}

console.log('FIN');
