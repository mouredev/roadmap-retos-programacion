let numeroX = 5;
let numeroY = 8;
let numeroP = "5";

let resultadoOperacion;

console.log('----------------------')
console.log('OPERADORES MATEMATICOS');
console.log('----------------------')

//Suma "+"

resultadoOperacion = numeroX + numeroY
console.log('\nSUMA');
console.log(`El resultado de la suma es ${resultadoOperacion}`);

//Resta "-"
resultadoOperacion = numeroY - numeroX;
console.log('RESTA');
console.log(`El resultado de la resta es ${resultadoOperacion}`);

//Multiplicación "*"
console.log('MULTIPLICACIÓN');
resultadoOperacion = numeroX * numeroY;
console.log(`El resultado de la multiplicación es ${resultadoOperacion}`);

//División "/"
resultadoOperacion = numeroY / numeroX;
console.log('DIVISIÓN');
console.log(`El resultado de la División es ${resultadoOperacion}`);

//Resto "%"
resultadoOperacion = numeroY % numeroX;
console.log('RESTO');
console.log(`El resultado  es ${resultadoOperacion}`);

console.log('----------------------')
console.log('OPERADORES LOGICOS Y DE COMPARACIÓN');
console.log('----------------------')

//(==)igual a 
console.log('\n(==)igual a ');
resultadoOperacion = numeroX == numeroY;
console.log(`El numero ${numeroX} y el numero ${numeroY} son iguales?`);
console.log(resultadoOperacion);

resultadoOperacion = numeroX == numeroX;
console.log(`El numero ${numeroX} y el numero ${numeroX} son iguales?`);
console.log(resultadoOperacion);


//(===)valor igual y tipo

console.log('\n(===)valor igual y tipo');
resultadoOperacion = numeroX === numeroX;
console.log(`El numero ${numeroX} y el numero ${numeroX} son iguales?`);
console.log(resultadoOperacion);

resultadoOperacion = numeroX === numeroP;
console.log(`El numero ${numeroX} y el numero ${numeroP}(string) son iguales?`);
console.log(resultadoOperacion);

//(!=)No igual
console.log('\n(!=)No igual');
resultadoOperacion = numeroX != numeroY;
console.log(`El numero ${numeroX} y el numero ${numeroY} son iguales?`);
console.log(resultadoOperacion);

//(!==)no igual en valor o tipo diferente 
console.log('\n(!==)no igual en valor o tipo diferente');
resultadoOperacion = numeroX !== numeroP;
console.log(`El numero ${numeroX} y el numero ${numeroP}(string) son iguales?`);
console.log(resultadoOperacion);

//(>) Mayor Que
console.log('\n(>) Mayor Que');
resultadoOperacion = numeroX > numeroY;
console.log(`El numero ${numeroX} es mayor que el numero ${numeroY} ?`);
console.log(resultadoOperacion);

//(<) Menor Que
console.log('\n(<) Menor Que');
resultadoOperacion = numeroX < numeroY;
console.log(`El numero ${numeroX} es menor que el numero ${numeroY} ?`);
console.log(resultadoOperacion);

//(>=) Mayor Que o igual a
console.log('\nMayor Que o igual a');
resultadoOperacion = numeroX >= numeroY;
console.log(`El numero ${numeroX} es mayor o igual que el numero ${numeroY} ?`);
console.log(resultadoOperacion);

//(<=) Menor Que o igual a
console.log('\n(<) Menor Que o igual a');
resultadoOperacion = numeroX <= numeroY;
console.log(`El numero ${numeroX} es menor o igual que el numero ${numeroY} ?`);
console.log(resultadoOperacion);

//(&&) y
console.log('\n(&&) y');
resultadoOperacion = (numeroX < 100 && numeroY > 10);
console.log(`El numero ${numeroX} es menor que 100 y el numero ${numeroY} es mayor 10 ?`);
console.log(resultadoOperacion);


//(!) no
console.log('\n(!) no');
resultadoOperacion = !(numeroX == numeroY);
console.log(`El numero ${numeroX} es igual que el numero ${numeroY} ?`);
console.log(resultadoOperacion);

//(?) operador ternario
console.log('\noperador ternario');
resultadoOperacion = (numeroX == numeroY)? "verdadero" : "falso";
console.log(`El numero ${numeroX} es igual que el numero ${numeroY} ?`);
console.log(resultadoOperacion);

console.log('\n----------------------');
console.log('Condicionales, iterativas, excepciones');
console.log('----------------------');

/*Condicionales, iterativas, excepciones*/

//ciclo for
console.log('\n-------Ciclo For--------');
for(i = 0; i <= 9; i++ ){
    console.log(i);
}

//switch
console.log('\n-------Switch--------');
let fruta = "Manzana";
switch (fruta){
    case "Manzana":
        console.log("Es Mazana");
        break;

    case "Pera":
        console.log("Es Pera");
        break;

    case "Mango":
        console.log("Es Mango");
        break;

    default:
    console.log("No es manzana");
    break;
}

//while
console.log('\n-------while--------');
let contador = 0;
while (contador <= 10) {
  console.log("número " + contador);
  contador++;
}

// Do while
console.log('\n-------Do while--------');
contador = 0;
do {
  console.log("número " + contador);
  contador++;
} while (contador <= 10);



/*
 DIFICULTAD EXTRA (opcional):
 Crea un programa que imprima por consola todos los números comprendidos
 entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
*/

console.log('\n------Ejercicio Extra-----------');

let numeroEntre = 10;
for (numeroEntre ; numeroEntre <= 55; numeroEntre++) {
    if((numeroEntre % 2 === 0) && (numeroEntre !== 16) && (numeroEntre % 3 !== 0)){
        console.log(numeroEntre);
    }
}










