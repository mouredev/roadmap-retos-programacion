/*
  * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
  *   su tipo de dato.
*/

//Asignación por valor
let number1 = 10;
let number2 = number1;
console.log(number1);
console.log(number2);

//asignacion por referencia
let myArray1 = [10, 20];
let myArray2 = myArray1;

myArray2.push(30);

console.log(myArray1);
console.log(myArray2);

/*
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
*/

const porValor = (x) => {
  let y = x;
  console.log("Dentro de porValor:");
  console.log("Original:", x);
  console.log("Copia:", y);
  y = 20;
  console.log("Después de modificar la copia en porValor:");
  console.log("Original:", x);
  console.log("Copia:", y);
}

const porReferencia = (arr) => {
  let copiaArr = arr;
  console.log("Dentro de porReferencia:");
  console.log("Original:", arr);
  console.log("Copia:", copiaArr);
  copiaArr.push(4);
  console.log("Después de modificar la copia en porReferencia:");
  console.log("Original:", arr);
  console.log("Copia:", copiaArr);
}

porValor(10);

const originalArray = [1, 2, 3];
porReferencia(originalArray);


/*
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
*/

//por Valor

let number3 = 10;
let number4 = 20;

const program1 = (param1, param2) => {
  let temp = param1;
  param1 = param2;
  param2 = temp;
  return { param1, param2 };
}

const resultados = program1(number3, number4);

const rtaParam1 = resultados.param1;
const rtaParam2 = resultados.param2;

console.log(`Parametro 1 Original: ${number3}, Nuevo: ${rtaParam1}`);
console.log(`Parametro 2 Original: ${number4}, Nuevo: ${rtaParam2}`);


//por referencia

let list1 = [10, 20];
let list2 = [30, 40];

const program2 = (param1, param2) => {
  let temp = param1;
  param1 = param2;
  param2 = temp;
  return [  param1, param2 ];
}

const resultados2 = program2(list1, list2);

const rtaList1 = resultados2[0]
const rtaList2 = resultados2[1]

console.log(`Parametro 1 Original: ${JSON.stringify(list1)}, Nuevo: ${JSON.stringify(rtaList1)}`);
console.log(`Parametro 2 Original: ${JSON.stringify(list2)}, Nuevo: ${JSON.stringify(rtaList2)}`);
