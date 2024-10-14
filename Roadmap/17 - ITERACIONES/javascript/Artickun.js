
// ⚡ Iteraciones

// 1. While
let i = 0;
while (i < 10) {
    console.log(i);
    i++;
};

// 2. Do While
let j = 0;
do {
    console.log(j);
    j++;
} while (j < 10);

// 3. For
for (let k = 0; k < 10; k++) {
    console.log(k);
};


/*
DIFICULTAD EXTRA (opcional):

  - Escribe el mayor número de mecanismos que posea tu lenguaje
  - para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?

*/

// For in
const obj = {a: 1, b: 2, c: 3, d: 4, e: 5, f: 6, g: 7, h: 8, i: 9, j: 10};
for (let key in obj) {
    console.log(obj[key]);
};

// For of
const array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
for (let item of array) {
    console.log(item);
};

// For each
array.forEach(function(element) {
    console.log(element);
});

// For await
async function asyncFunction() {
    for await (const element of array) {
        console.log(element);
    }
};
asyncFunction();

//map
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10].map( num => console.log(num) );

//filter
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10].filter( num => {
    console.log(num);
    return false;
});

//every
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10].every(num => {
    console.log(num);
    return true;
});
