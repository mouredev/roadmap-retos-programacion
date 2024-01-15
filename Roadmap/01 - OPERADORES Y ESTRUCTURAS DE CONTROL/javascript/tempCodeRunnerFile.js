//✔️ESTRUCTURAS DE CONTROL
//✔️WHILE
let contadorWhile = 0;
while (contadorWhile < 5) {
    console.log(`Iteración: ${contadorWhile}`);
    contadorWhile++;
}

//✔️DO WHILE
let contadorDoWhile = 0;

do {
    console.log(`Iteración: ${contadorDoWhile}`);
    contadorDoWhile++;
} while (contadorDoWhile < 5);

//✔️FOR
for (let i = 0; i < 5; i++) {
    console.log(`Iteración: ${i}`);
}

//✔️FOR OF
let arrayForOf = [10, 20, 30];

for (let valor of arrayForOf) {
    console.log(`Valor elemento arrayForOf: ${valor}`);
}

//✔️FOR IN
let objetoForIn = { a: 1, b: 2, c: 3 };

for (let propiedad in objetoForIn) {
    console.log(`Propiedad ${propiedad} = ${objetoForIn[propiedad]}`);
}

//✔️FOR EACH
let arrayForEach = [1, 2, 3];

arrayForEach.forEach(function (elemento) {
    console.log(`Elemento: ${elemento}`);
});