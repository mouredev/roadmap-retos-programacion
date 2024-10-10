// 1. Uso de la sintaxis for .. of
const array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for (let num of array) console.log(num)

// Symbol.iterator
let range = {
    from: 1,
    to: 10
}
range[Symbol.iterator] = function() {
    return {
        current: this.from,
        last: this.to, 
        next() {
            if (this.current <= this.last) {
                return { done: false, value: this.current++ }
            } else {
                return { done: true }
            }
        }
    }
}
for (let num of range) console.log(num)

// Uso de Array.from

let arr = Array.from(range)
for (let num of arr) console.log(num)

// Funciones generadoras

range = {
  from: 1,
  to: 10,

  *[Symbol.iterator]() { 
    for (let value = this.from; value <= this.to; value++) {
      yield value;
    }
  }
};
for (let value of range) console.log(value)

// 2. Uso de for .. in
for (let num in array) console.log(++num)

// 3. Uso de forEach
array.forEach(e => console.log(e))

// 4. Uso de for 
for (let i = 1; i <=10; i++) console.log(i)

// 5. Uso de while
let i = 1
while (i <= 10) {
    console.log(i)
    i++
}

// 6. Uso de do .. while
i = 1
do {
    console.log(i)
    i++
} while (i <= 10)
