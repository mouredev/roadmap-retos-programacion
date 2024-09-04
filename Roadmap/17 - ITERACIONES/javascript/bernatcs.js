// ** EJERCICIO 

// for
for (let index = 1; index <= 10; index++) {
    console.log(index)
    
}

// while
let index2 = 1
while (index2 <= 10) {
    console.log(index2);
    index2++
}

// forEach
let index3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
index3.forEach(element => {
    console.log(element)
});

// ** DIFICULTAD EXTRA ** -----------------------------------------------------------------------------------------------------------

// for...of
let index4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for (let element of index4) {
    console.log(element)
}

// for...in --> La diferencia con el of es que devuelve los índices 
let index5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for (let element in index5) {
    console.log(Number(element) + 1)
}

