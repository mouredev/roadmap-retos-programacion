/*
  * Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
  * números del 1 al 10 mediante iteración.
*/

// For
console.log('For')
for (let i = 1; i <= 10; i++) {
  console.log(i)
}

// While
console.log('While')
let i = 1
while (i <= 10) {
  console.log(i)
  i++;
}

// Do while
console.log('Do While');
let j = 1
do {
  console.log(j)
  j++
} while(j <= 10)

/*
  * DIFICULTAD EXTRA (opcional):
  * Escribe el mayor número de mecanismos que posea tu lenguaje
  * para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?
*/

// for in

const list = [1,2,3,4,5]

for(item in list) {
  console.log(item)
}

// for of

for(item of list) {
  console.log(item)
}