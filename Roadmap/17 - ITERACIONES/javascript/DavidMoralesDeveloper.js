// Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
//  * números del 1 al 10 mediante iteración.

// for  --------------
let arr = []
for(let i = 0; i < 10; i++){
arr.push(i)
console.log(i  + 'crando numeros en for y push en arr')
}



// forech 
arr.forEach( a  => {
    console.log(a + 'dentro de  forech')
});

// for in
for (const numer in arr) {
    console.log(numer + 'forin')
}

//for of
for (let i of arr) {
    console.log(i + 'forof');
  }


// do while ----------------
let result = '';
let i = 0;

do {
  i = i + 1;
  console.log(i + 'dowhile')
  result = result + i;
} while (i < 10);

console.log(  result + ' dowhile me da un string de el 1 al 10' );

// while ------------------------------ 
let y = 0
let z = 0
 while (y < 10) {
    y++
    z += y
    console.log(y + 'dentro de while')
 }
console.log(z + 'fuera de while')

