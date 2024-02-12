
// Operadores Arifméticos
let n = 10
let m = 3

console.log(`Suma: ${n}+${m}: ${n+m}`)
console.log(`Resta: ${n}-${m}: ${n-m}`)
console.log(`Multiplicacion: ${n}*${m}: ${n*m}`)
console.log(`Division: ${n}/${m}: ${n/m}`)
console.log(`Módulo: ${n}%${m}: ${n%m}`)

// Operadores Incremento y Decremento
let k = 5
let l = 10
console.log(`Incremento : ${k++}++: ${k}`)
console.log(`Decremento : ${l++}--: ${l}`)

// Operadores de asignación
let x = 3;
let y = 4;
console.log(`Adicion: x=${x}; x+=${y}: ${x+=y}`)

x = 6;
y = 3;
console.log(`Resta: x=${x}; x-=${y}: ${x-=y}`)

x = 2;
y = 3;
console.log(`Multiplicacion: x=${x}; x-*${y}: ${x*=y}`)

x = 10;
y = 5;
console.log(`Division: x=${x}; x-*${y}: ${x*=y}`)
console.log('====================================================');


//Operadoes Comparación
let i = 5
console.log(`Igual estricto: ${i}===${i}: ${i===i}`)
console.log(`No Igual estricto: ${i}!==${i}: ${i!==i}`)
console.log(`Menor Igual que: ${i}<=${i}: ${i<=i}`)
console.log(`Mayor Igual que: ${i}>=${i}: ${i>=i}`)
console.log(`Menor que: ${i}<${i}: ${i<i}`)
console.log(`Mayor que: ${i}>${i}: ${i>i}`)
console.log('====================================================');

// Condicionales

let diaParaProgramar = true;

if (diaParaProgramar) {
  console.log("¡Siii! Mi momento para mostrar mis habilidades ha llegado");
} else {
  console.log("No hay problema, hay que mantener la esperanza");
}
console.log('====================================================');

// Iterativas

for (let index = 0; index < 10; index++) {
  console.log(`For: ${index}`);
}
console.log('====================================================');

let index = 0;
while (index<=10) {
  console.log(`While: ${index++}`);
}
console.log('====================================================');

//Manejo de Exepciones
try {
  for (let i = 0; i < 10; i++) {
    if (i<3) {
      console.log(i);
    } else {
      throw new Error('No es valido para i < 3')
    }
  }
} catch (error) {
  console.log('ERROR',error.message);
}

console.log('====================================================');
console.log('============== DIFICULTAD EXTRA ======================');
  for (let num = 10; num <= 55; num++) {
    if (num%2==0 && num != 16 && num%3!=0) console.log(num)
  }
console.log('====================================================');







