// 1. for
for(let i:number = 1; i <= 10; i++) {
  console.log(i)
}

// 2. while
let i:number = 1
while (i <= 10) {
  console.log(i)
  i++
}

// 3. do while
let j: number = 1
do {
  console.log(j)
  j++
} while (j <= 10)

// extra


const numbers: number[] = [1, 2, 3, 4, 5]

// 4. for of
console.log("4. for...of")
for (const number of numbers) {
  console.log(number)
}

// 5. for in
console.log("5. for...in")
for (const index in numbers) {
  console.log(numbers[index])
}

// 6. forEach
console.log("6. forEach")
numbers.forEach((number) => {
  console.log(number)
});

// 7. map
console.log("7. map")
numbers.map((number) => {
  console.log(number)
});

// 8. filter
console.log("8. filter")
numbers.filter((number) => {
  console.log(number)
  return true
});

// 9. reduce
console.log("9. reduce");
numbers.reduce((_, number) => {
  console.log(number)
  return 0
}, 0)

// 10. every
console.log("10. every");
numbers.every((number) => {
  console.log(number)
  return true
})
