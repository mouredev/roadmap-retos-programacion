
//* VALOR Y REFERENCIA

/*

VALOR (Value):

Cuando asignas un valor primitivo a una variable 
(como un número, una cadena o un booleano), estás manipulando el valor real.
La asignación de un valor a otra variable crea una copia independiente de ese valor. 
Cambiar la copia no afectará al valor original.

*/

let a = 5;
let b = a;
b = 10;

console.log(a); // Output: 5
console.log(b); // Output: 10


/*

REFERENCIA (Reference):

Cuando asignas un objeto (incluidos arreglos y funciones) a una variable, 
estás manipulando una referencia al objeto en la memoria, no el objeto en sí mismo.
Asignar la referencia a otra variable significa que ambas variables apuntan al mismo 
objeto en la memoria.

*/

let array1 = [1, 2, 3];
let array2 = array1;
array2.push(4);

console.log(array1); // Output: [1, 2, 3, 4]
console.log(array2); // Output: [1, 2, 3, 4]

/*

En este caso, modificar array2 afecta a array1 porque ambas comparten la misma 
referencia al objeto en la memoria.

*/

//* TIPOS DE DATOS POR VALOR

//Number
let num1 = 10;
let num2 = num1;
num2 = 20;

console.log(num1); // Output: 10
console.log(num2); // Output: 20

//String
let str1 = "Hola";
let str2 = str1;
str2 = "Adiós";

console.log(str1); // Output: Hola
console.log(str2); // Output: Adiós

//Boolean
let bool1 = true;
let bool2 = bool1;
bool2 = false;

console.log(bool1); // Output: true
console.log(bool2); // Output: false

//Undefined
let undefinedValue = undefined;
let anotherUndefined = undefinedValue;

console.log(undefinedValue);   // Output: undefined
console.log(anotherUndefined); // Output: undefined

//Null
let nullValue = null;
let anotherNull = nullValue;

console.log(nullValue);   // Output: null
console.log(anotherNull); // Output: null


//* TIPOS DE DATOS POR REFERENCIA

//Objeto
let obj1 = { key: 'value' };
let obj2 = obj1;
obj2.key = 'new value';

console.log(obj1.key); // Output: new value
console.log(obj2.key); // Output: new value

//Array
let arr1 = [1, 2, 3];
let arr2 = arr1;
arr2.push(4);

console.log(arr1); // Output: [1, 2, 3, 4]
console.log(arr2); // Output: [1, 2, 3, 4]

//Funciones
function greet(name) {
    return `Hello, ${name}!`;
}

let greetFunction1 = greet;
let greetFunction2 = greetFunction1;

console.log(greetFunction1('Alice')); // Output: Hello, Alice!
console.log(greetFunction2('Bob'));   // Output: Hello, Bob!


//* EJEMPLOS DE FUNCIONES POR VALOR

//Numero
function modifyNumber(value) {
    console.log( value = 20 );
}

let num = 10;

modifyNumber(num);  // Output: 20

console.log( num ); // Output: 10

/*
En este ejemplo, el valor de num no cambia aun después de llamar 
a la función modifyNumber, ya que los números se pasan "por valor".
osea se creo una copia de num
*/

//String
function modifyString(value) {
    console.log( value = "Adiós" );;
}

let str = "Hola";

modifyString(str);// Output: Adiós

console.log(str); // Output: Hola

/*
Similar al caso anterior, el valor de str no se modifica después de llamar 
a la función modifyString.
*/

//*EJEMPLOS DE FUNCIONES POR REFERENCIA

//Objeto
function modifyObject(obj) {
    obj.key = 'new value';
}

let obj = { key: 'value' };

console.log( obj.key ); // Output: value

modifyObject(obj);

console.log( obj.key ); // Output: new value

/*
En este caso, la función modifyObject modifica directamente la propiedad 
del objeto, y este cambio se refleja fuera de la función.
*/


//Array
function modifyArray(arr) {
    arr.push(4);
}

let arr = [1, 2, 3];

console.log( arr ); // Output: [1, 2, 3]

modifyArray(arr);

console.log( arr ); // Output: [1, 2, 3, 4]

/*
Al igual que con el objeto, la función modifyArray modifica el arreglo 
directamente, y este cambio afecta al arreglo fuera de la función.
*/

//*  DIFICULTAD EXTRA (opcional):
/*
Crea dos programas que reciban dos parámetros (cada uno) definidos como 
variables anteriormente.

Cada programa recibe, en un caso, dos parámetros por valor, 
y en otro caso, por referencia.

Estos parámetros los intercambia entre ellos en su interior, 
los retorna, y su retorno se asigna a dos variables diferentes a las originales. 

A continuación, imprime el valor de las variables originales y las nuevas, 
comprobando que se ha invertido su valor en las segundas.

Comprueba también que se ha conservado el valor original en las primeras.

*/

// PROGRAMA 1 con Strings ( por referencia )
let value1 = 'Hola';
let value2 = 'Mundo';

let programa1 = ( param1,param2 ) => {
    let invert1 = param2;
    let invert2 = param1;
    return [invert1, invert2 ='Soy ArticKun'];
};

// Obtener los nuevos valores y asignarlos a variables diferentes
let [newValue1, newValue2] = programa1(value1, value2);

console.log("Originales:", value1, value2);   // 'Hola Mundo
console.log("Nuevos:", newValue1, newValue2); // Mundo soy ArticKun


// PROGRAMA 2 con Arrays( por referencia )
let arreglo1 = ['Iron Man','Hulk','Thor'];
let arreglo2 = ['Spidey','Cap','Ant Man'];

let programa2 = ( param1,param2 ) =>{
    let invert1 = param2;
    let invert2 = param1;
    return[invert1, invert2];
};

let [newArr1, newArr2] = programa2(arreglo1, arreglo2);

console.log("Originales:", arreglo1, arreglo2);
console.log("Nuevos:", newArr1, newArr2);


// PROGRAMA 2 con objetos ( por referencia )
let objeto1 = { nombre: 'Iron Man', poder: 'Tecnología avanzada' };
let objeto2 = { nombre: 'Hulk', poder: 'Fuerza sobrehumana' };

let programa2Objetos = (param1, param2) => {
    [param1.nombre, param2.nombre] = [param2.nombre, param1.nombre];
    [param1.poder, param2.poder] = [param2.poder, param1.poder];
};

console.log("Originales:", objeto1, objeto2);
programa2Objetos(objeto1, objeto2);
console.log("Nuevos:", objeto1, objeto2);
