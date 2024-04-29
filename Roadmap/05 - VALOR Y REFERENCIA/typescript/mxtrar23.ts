//- Muestra ejemplos de asignación de variables "por valor" y "por referencia", según su tipo de dato.

//por valor
const texto1 = 'TypeScript'
const texto2 = texto1

console.log(texto1);
console.log(texto2);

// por referencia
const array1 = [1,2,3]
let array2 = array1

array2.push(4)

console.log(array1);
console.log(array2);


// - Muestra ejemplos de funciones con variables que se les pasan "por valor" y  "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.


//por valor
const function1 = (param:number) :void => {
  param = 2
  console.log(param);
}

const num = 1
function1(num)
console.log(num);


// por referencia
const function2 = (param:number[]) :void => {
  param.push(4)
  let array2 = param
  array2.push(5)

  console.log(param);
  console.log(array2);
}

const arr = [1,2,3]
function2(arr)
console.log(arr);



