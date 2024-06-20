//Ejercicio

//Función superior es aquella que recibe una función como argumento o devuelve a otra función

/* Recibe función como argumento */

const arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11];

function filterArr(arr, callback) {
  let filterNum = [];
  for (let i = 0; i < arr.length; i++) {
    callback(arr[i]) ? filterNum.push(arr[i]) : null;
  }
  return filterNum;
}

function isOdd(x) {
  return x % 2 !== 0;
}

function isEven(x) {
  return x % 2 === 0;
}

console.log(filterArr(arr, isEven));
console.log(filterArr(arr, isOdd));

/* Retorno de una función */

function calculate(operation) {
  switch (operation) {
    case 'ADD':
      return function (a, b) {
        console.log(`${a} + ${b} = ${a + b}`);
      };
    case 'SUBTRACT':
      return function (a, b) {
        console.log(`${a} - ${b} = ${a - b}`);
      };
  }
}

const calculateAdd = calculate('ADD');
calculateAdd(3, 5);
calculate('SUBTRACT')(13, 8);

//Extra

const students = [
  {'name': 'Ángel', 'birthdate': '16-09-1979', 'grades': [7, 7.2, 6.5, 9]},
  {'name': 'María', 'birthdate': '06-10-1980', 'grades': [5, 7.2, 6.5, 8]},
  {'name': 'Rosa', 'birthdate': '23-01-1985', 'grades': [7.1, 7.2, 6, 8.5]}
];

function average(grades) {
  let initialValue = 0;
  return grades.reduce(
    (accumulator, currentValue) => accumulator + currentValue,
    initialValue,
  )/grades.length;
}

function nameAndAverage(n) {
  return {'name': n['name'], 'grades': n['grades']};
}

console.log(students.map(nameAndAverage));