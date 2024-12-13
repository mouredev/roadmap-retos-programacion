let i:number = 1;

for(i; i<=10; i++){
    console.log(i);
}

while(i<=10){
    console.log(i);
    i++;
}

function imprimir(numero:number):void{
    if(numero<=10){
        console.log(numero);
        imprimir(numero+1);
    }else return;
}

imprimir(i);

/*Extraaaaa */

let j = 1;
do {
    console.log(j);
    j++;
} while (j <=10);

const array = [1, 2, 3, 4, 5];
for (const value of array) {
    console.log(value);
}

const object = { a: 1, b: 2, c: 3 };
for (const key in object) {
    if (object.hasOwnProperty(key)) {
        console.log(`${key}: ${object[key]}`);
    }
}

const numbers = [1, 2, 3, 4, 5];
numbers.forEach((number) => {
    console.log(number);
});

const doubled = numbers.map((number) => number * 2);
console.log(doubled);

const sum = numbers.reduce((acc, number) => acc + number, 0);
console.log(sum);

const hasEvenNumber = numbers.some((number) => number % 2 === 0);
console.log(hasEvenNumber); // true

