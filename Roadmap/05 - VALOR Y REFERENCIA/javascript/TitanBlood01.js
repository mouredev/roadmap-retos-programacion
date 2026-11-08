//Ejercicio 05 Asignaciones por valor y asignaciones por referencia

//Por valor
//Todos los tipos de datos primitivos son pasados por valor es decir crean una copia
//y en caso de ser asignados en una nueva variable, esta sera independiente y no afectara su valor
//int o number
let a = 50;
let b = a;
b*=5;
console.log(a)//mantiene 50 
console.log(b)// es afectado
//Strings
let str1 = 'Este es un string primitivo'
let str2 = str1

str2 = 'Cambio de valor en esta variable'
console.log(str1)//mantiene
console.log(str2)//cambia
//boolean
let bool1 = false
let bool2 = bool1

bool2 = 5>4
console.log(bool1)//se mantiene
console.log(bool2)//cambia

/* Por referencia
para este tipo de asignacion lo que se realiza de manera interna es una especie de "puntero" es decir
en ves de que la variable tenga el valor puro o en si de la variable lo que realiza es una referencia al
espacio de memoria en el que se ubica, por lo que cualquier cambio que se haga en estas variables, afectara
tambien a la otra que contiene la misma referencia, los tipos de datos que trabajan de esta manera son los
complejos como ser: arrays, sets, maps y los mismos objects
*/
//Arrays
let arr1 = [0,13,98,72,46]
let arr2 = arr1

arr2.push('nuevo valor')
console.log(arr1)// cambio igual que el arr2
console.log(arr2)// de igual manera por que hace referencia al mismo espacio de memoria
//objects

let obj1 = {
    prop1: 'nombre',
    prop2: 65,
    prop3: false
}

let obj2 = obj1
obj2.prop4 = 'nuevo'
console.log(obj1)// se modifico igual con el nuevo valor
console.log(obj2)// mismo caso

/* la mejor manera de poder trabajar con los objetos o los tipos que son asingados por referencia es
con las herramientas de propagacion y desestructuracion, permitiendo copiar todos los valores dentro
de los objetos, arrays, sets o maps que se esten usando, y dejando el original intacto*/

//descomposicion
let myarr1 = [0,1,2,3,4,'valor 5'];
let myarr2 = [...myarr1]

myarr2.push(true)
myarr1.pop()
console.log(myarr1)// Fue modificado, pero es diferente al de myarr2
console.log(myarr2)// Modificado tambien, diferente al array 1

//descomposicion para objetos
let myObj1 = {
    prop1: "Primera propiedad",
    prop2: 45
}

let myObj2 = {...myObj1}

myObj2.prop3 = 45.7
console.log(myObj1)//el primero objeto no fue modificado
console.log(myObj2)//este objeto si es modificado.

/* 
    DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como
 * variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime
 *   el valor de las variables originales y las nuevas, comprobando que se ha invertido
 *   su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
*/

let myvar = "primer variable"
let myvar2 = 504
function programByValue(par1, par2) {
    [par1, par2] = [par2, par1]  

    return [par1, par2]
}

[parametro1, parametro2] = programByValue(myvar, myvar2)
console.log(myvar)
console.log(myvar2)
console.log(parametro1)
console.log(parametro2)


let myvar3 = ['uno', 'dos', 3 ,4];
let myvar4 = {
    prop1 : 'nombre',
    prop2 : 'edad',
    prop3 : 5
}
function programByReference(par1, par2) {
    [par1, par2] = [par2, par1]  

    return [par1, par2]
}

[parametro3, parametro4] = programByReference(myvar3, myvar4)
console.log(myvar3)
console.log(myvar4)
console.log(parametro3)
console.log(parametro4)