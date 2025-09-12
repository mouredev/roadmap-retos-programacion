// FOR
console.log('FOR')
for(let i: number = 0; i <= 10; i++){
  console.log(i)
}

// FOREACH
console.log('FOREACH')
const numbers: Array<number> = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers.forEach(i => {
  console.log(i)
});


// FOR IN
console.log('FOR IN')
for(const i in numbers){
  console.log(numbers[i])
}

// FOR OF
console.log('FOR OF')
for(const i of numbers){
  console.log(i)
}

// WHILE
console.log('WHILE')
let w: number = 0
while(w < 11){
  console.log(w)
  w++
}


// DO-WHILE
console.log('DO-WHILE')
let d: number = 0
do{
  console.log(d)
  d++
}while(d < 11)


