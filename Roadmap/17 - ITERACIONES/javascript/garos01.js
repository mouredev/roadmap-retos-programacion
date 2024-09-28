// Método 1: Bucle for
console.log("Método 1: Bucle for");
for (let i = 1; i <= 10; i++) {
  console.log(i);
}

// Método 2: Bucle while
console.log("Método 2: Bucle while");
let j = 1;
while (j <= 10) {
  console.log(j);
  j++;
}

// Método 3: Bucle do-while
console.log("Método 3: Bucle do-while");
let k = 1;
do {
  console.log(k);
  k++;
} while (k <= 10);

// Ejercicio extra

// Método 1: Bucle for clásico
console.log("Método 1: Bucle for clásico");
for (let i = 1; i <= 10; i++) {
  console.log(i);
}

// Método 2: Bucle while
console.log("Método 2: Bucle while");
let l = 1;
while (l <= 10) {
  console.log(l);
  l++;
}

// Método 3: Bucle do-while
console.log("Método 3: Bucle do-while");
let m = 1;
do {
  console.log(m);
  m++;
} while (m <= 10);

// Método 4: forEach() en arrays
console.log("Método 4: forEach()");
const array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
array.forEach((item) => console.log(item));

// Método 5: map() en arrays
console.log("Método 5: map()");
const newArray = array.map((item) => item);
console.log(newArray);

// Método 6: filter() en arrays
console.log("Método 6: filter()");
const filteredArray = array.filter((item) => item <= 10);
console.log(filteredArray);

// Método 7: reduce() en arrays
console.log("Método 7: reduce()");
const sum = array.reduce(
  (accumulator, currentValue) => accumulator + currentValue
);
console.log(sum);

// Método 8: for...of en iterables
console.log("Método 8: for...of");
for (const item of array) {
  console.log(item);
}

// Método 9: for...in en objetos
console.log("Método 9: for...in");
const obj = { a: 1, b: 2, c: 3 };
for (const key in obj) {
  console.log(obj[key]);
}

// Método 10: for await...of en iterables asíncronos (ejemplo simplificado)
console.log("Método 10: for await...of (ejemplo simplificado)");
const asyncIterable = {
  [Symbol.asyncIterator]() {
    return {
      i: 0,
      async next() {
        if (this.i < 10) {
          await new Promise((resolve) => setTimeout(resolve, 1000));
          return { value: ++this.i, done: false };
        } else {
          return { done: true };
        }
      },
    };
  },
};

(async () => {
  for await (const item of asyncIterable) {
    console.log(item);
  }
})();
