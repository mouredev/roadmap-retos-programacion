for (let i = 1; i <= 10; i++) {
  console.log(`Iteracion de for número ${i}`);
}

let i = 1
while (i <= 10) {
  console.log(`Iteracion de while número ${i}`);
  i++
}

i = 1
do {
  console.log(`Iteracion de do while número ${i}`);
  i++
} while (i <= 10)

// ------------------------------------- DIFICULTAD EXTRA -------------------------------------
  // constantes, variables, funciones necesarias
const obj = {1: 1,2: 2,3: 3,4: 4,5: 5,6: 6,7: 7,8: 8,9: 9,10: 10}
const arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
const initialValue = 0
const isBelowThreshold = (x) => x < 11
async function* foo() {
  yield 1;
  yield 2;
  yield 3;
  yield 4;
  yield 5;
  yield 6;
  yield 7;
  yield 8;
  yield 9;
  yield 10;
}

// ITERACIONES (empiezo desde 4 ya que arriba hay 3 del ejercicio anterior "for", "while", "do while")
  // #4 (for in)
  for (const key in obj) {
    console.log(`Iteracion de for in número ${obj[key]}`)
  }

  // #5 (for of)
  for (const i of arr) {
    console.log(`Iteracion de for of número ${i}`)
  }

  //#6 (forEach)
  arr.forEach(element => {console.log(`Iteracion de forEach número ${element}`)});

  //#7 (for await of)
  (async () => {
    for await (const num of foo()) {
      console.log(`Iteracion de for await of número ${num}`);
    }
  })();

  //#8 (map)
  const mapped = arr.map((x) => console.log(`Iteracion de map número ${x}`))

  //#9 (filter)
  const filtered = arr.filter((x) => console.log(`Iteracion de filter número ${x}`))

  //#10 (reduce)
  const reduced = arr.reduce((accumulator, currentValue) => console.log(`Iteracion de reduce número ${currentValue}`),initialValue)

  //#11 (reduceRight)
  const reducedRight = arr.reduceRight((accumulator, currentValue) => console.log(`Iteracion de reduceRight número ${11 - currentValue}`),initialValue)

  //#12 (every)
  arr.every(num => {
    console.log(`Iteracion de every número ${num}`)
    return true
  })

  //#13 (some)
  const some = arr.some((x) => console.log(`Iteracion de some número ${x}`))

  //#14 (find)
  const find = arr.find((x) => console.log(`Iteracion de find número ${x}`))

  //#15 (findIndex)
  const findIndex = arr.findIndex((x) => console.log(`Iteracion de findIndex número ${x}`))

  //#16 (findLast)
  const findLast = arr.findLast((x) => console.log(`Iteracion de findLast número ${11 - x}`))

  //#17 (findLastIndex)
  const findLastIndex = arr.findLastIndex((x) => console.log(`Iteracion de findLastIndex número ${11 - x}`))

  //#18 (flatMap)
  const flatMap = arr.flatMap((x) => console.log(`Iteracion de flatMap número ${x}`))

  //#19 (entries)
  console.log([...arr.entries()])

  //#20 (keys)
  console.log([...arr.keys()])

  //#21 (values)
  console.log([...arr.values()])

  //#22 ([Symbol.iterator])
  console.log([...arr[Symbol.iterator]()])

  //#23 ('...' spread operator)
  console.log([...arr])

  //#24 (from)
  Array.from(arr, (x) => console.log(`Iteracion de from número ${x}`))