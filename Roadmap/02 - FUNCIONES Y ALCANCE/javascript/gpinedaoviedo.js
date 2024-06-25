//variable global
var total;

//variable local
let num1, num2;
num1 = 8;
num2 = 10;

//funcion basica
const operation = () => {
    total = num1 + num2;
    console.log(total);
};
operation();

///////////////////////////

//funcion con parametros y return
const operation2 = (suma, division) => {
    total2 = (suma + total) / division; //uso de var global
    return total2;
};
console.log(operation2(20, 2));

///////////////////////////

//funcion dentro de otra funcion
const operation3 = () => {
    const opInFuntion = (num, multip) => {
        total3 = num * multip;
        return total3;
    };
    console.log(opInFuntion(5,5));
};
operation3();

////////////////////////////

//DIFICULTAD EXTRA
const operationExtra = (txt1, txt2) => {
    let count = 0;
    for (let i = 1; i <= 100; i++) {
        if (i % 3 === 0 && i % 5 === 0) {
            console.log(`${txt1} y ${txt2}`);
        } else if (i % 3 === 0) {
            console.log(txt1);
        } else if (i % 5 === 0) {
            console.log(txt2);
        } else {
            console.log(`numero: ${i}`);
            count++;
        }
    }
    return count;
};
const txt1 = "multiplo de 3";
const txt2 = "multiplo de 5";
const result = operationExtra(txt1, txt2);
console.log(`El número de veces que se ha impreso el número es: ${result}`)
