let index = 1
const numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

console.log(`-----  FOR -----`)
for (index = 1; index <= 10; index++) {
  console.log(index)
}

console.log(`-----  FOREACH -----`)
numeros.forEach(numero => console.log(numero))

console.log(`-----  FOR IN -----`)
index = 1
for (index in numeros) {
  console.log(numeros[index])
}

console.log(`-----  MAP -----`)
numeros.map(numero => console.log(numero))

console.log(`-----  WHILE -----`)
index = 1
while (index <= 10) {
  console.log(index)
  index++
}

console.log(`-----  DO WHILE -----`)
index = 1
do {
  console.log(index)
  index++
} while (index <= 10);

console.log(`-----  function* -----`)
index = 1
function* iteracion() {
  while (index <= 10) yield index++
}

const iterar = iteracion()
console.log(iterar.next().value)
console.log(iterar.next().value)
console.log(iterar.next().value)
console.log(iterar.next().value)
console.log(iterar.next().value)
console.log(iterar.next().value)
console.log(iterar.next().value)
console.log(iterar.next().value)
console.log(iterar.next().value)
console.log(iterar.next().value)