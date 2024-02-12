/*
 * EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
 */


// Pass by Value
let num1 = 20
let num2 = num1 // Assigning the value of 'num1' to 'num2', creating a new copy of the value
num2 = 40 // Modifying the value of 'num2', does not affect 'num1' as they are independent variables

console.log(`Value of num1: ${num1}`) // 'num1' retains its original value of 20
console.log(`Value of num2: ${num2}`) // 'num2' has been modified to 40

// Pass by Reference 
    // Objects:
const obj1 = {x: 20, y: 30}
const obj2 = obj1 // Assigning the reference of 'obj1' to 'obj2', so both now point to the same object in memory
obj2.x = 40 // Modifying the 'x' property of 'obj2', which also affects 'obj1' since they share the same reference

console.log(`Value of obj1:`)
console.log(obj1) // Both 'obj1' and 'obj2' now have an 'x' value of 40
console.log(`Value of obj2:`)
console.log(obj2) // 'obj2' reflects the change made to 'obj1'

    // Arrays:
const arr1 = [1, 2, 3]
const arr2 = arr1 // Assigning the reference of 'arr1' to 'arr2', so both now point to the same array in memory
arr2[0] = 4 // Modifying the first element of 'arr2', which also affects 'arr1' since they share the same reference

console.log(`Value of arr1:`)
console.log(arr1) // Both 'arr1' and 'arr2' now have an index0 value of 4
console.log(`Value of arr2:`)
console.log(arr2) // 'arr2' reflects the change made to 'arr1'

// Functions with Pass by Value
function increment(num) {
  num++;
  return num;
}

const num = 5;
const numIncremented = increment(num);
console.log(`num: ${num}`) // num retains its original value of 5
console.log(`numIncremented: ${numIncremented}`) // numIncremented has the value of 6

// Functions with Pass by Reference
function changeValue(obj){
    obj.x= 50
    return obj
}
const object1 = {x: 10, y: 20}
const objChanged = changeValue(object1)

console.log(`object1: `)
console.log(object1) // object1 has changed its original value to {x: 50, y: 20}
console.log(`objChanged: `)
console.log(objChanged) // objChanged has the value of {x: 50, y: 20}


// EXTRA TASK:
function swapValues(value1, value2) {
    let temp1 = value1
    value1 = value2
    value2 = temp1
    return [value1, value2]
}

function swapObjectValues(obj) {
    let copy = {...obj}
    let temp1 = copy.val1
    copy.val1 = copy.val2
    copy.val2 = temp1
    return copy
}

const value1 = 10
const value2 = 50
const [newValue1, newValue2] = swapValues(value1, value2)
console.log(`Value1: ${value1}, Value2: ${value2}`)
console.log(`NewValue1: ${newValue1}, NewValue2: ${newValue2}`)

const obj = {val1: 10, val2: 50}
const newObj = swapObjectValues(obj)
console.log(`Obj: `)
console.log(obj)
console.log(`NewObj: `)
console.log(newObj)
