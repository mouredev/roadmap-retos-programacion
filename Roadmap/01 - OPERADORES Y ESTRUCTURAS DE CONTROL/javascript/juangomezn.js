/*-----------
 * OPERADORES
-------------
*/

//Operadores Aritmeticos
let a = 8
let b = 5

//Suma
suma = a + b
console.log(suma)

//Resta
resta = a - b
console.log(resta)

//Multiplicación
multiplicación = a * b
console.log(multiplicación)

//División 
division = a / b
console.log(division)

//Módulo
modulo = a % b
console.log(modulo)

//Potenciación
potenciacion = a ** 2
console.log(potenciacion)


//Operadores de Asignación 

//Asignación
c = 5 // Se le da el valor de 5 a x
console.log(c)

//Asignación con Suma
c = 5
c += 5 // Se le da el valor de 5 a x y se suma 5 lo que da un valor de 10
console.log(c)

//Asignación con Resta
c = 5
c -= 5 // Se le da el valor de 5 a x y al restarle 5 da un valor de 0
console.log(c)

//Asignación con multiplicación
c = 5 
c *= 5 // Se le da un valor de 5 a x y al multiplicarle 5 da un valor de 25
console.log(c)

//Asignación con división 
c = 5
c /= 5 //Se le da un valor de 5 a x y al dividirlo entre 5 da un valor de 1
console.log(c)

//Asignación con módulo
c = 5
c %= 5 // Se le da el valor de 5 a x y al dividirlo entre 5 el rsultado del modulo seria 0
console.log(c)

//Asignación con Potenciación
c = 5
c **= 2 //Se le da un valor de 5 a x y al potenciarlo por 2 da un resultado de 25
console.log(c)


//Operadores de Comparación

let d = 10
let e = 5

console.log(d == e) //(Este operador representa "igual a")
console.log(d === e) //(Este operador representa "igual a con tipo")
console.log(d != e) //(Este operador representa "no igual a")
console.log(d !== e) //(No igual a con tipo)
console.log(d > e) //Mayor que
console.log(d < e) // Menor que
console.log(d >= e) //Mayor o igual que
console.log(d <= e) // Menor o igual que


//Operadores Logicos

f = true
g = false

console.log(f && g) // Este operador representa Y Logico 
console.log(f || g) // Este operador representa O Logico 
console.log(!f) // Este operador representa Negación Logica


//Operadores de Cadena (String)

str1 = "Hola"
str2 = "Mundo"

console.log(str1 + " " + str2) // Concatenación = Hola Mundo
console.log(str1 + " " + "Amigo") //Concatenación con Asignación = Hola Amigo


//Operadores Ternarios

edad = 18
esAdulto = (edad >= 18) ? "Adulto" : "Menor";
console.log(esAdulto)


//Operadores de Tipo

number = 42
text = "Hola"

console.log(typeof number) //Operador utilizao para identificar el tipo de dato en este caso es number
console.log(typeof text) //Operador utilizado para identificat el tipo de dato en este caso es string
console.log(number instanceof Number) // False ya que "number" no es una instancia de "Number"

//Operadores de Desestructuración

let arr = [1,2,3];
let [first, second] = arr
console.log(first,second); 

let obj = {name : "Juan", age : 25}
let{name, age} = obj
console.log(name, age);


/* 
 * ----------------------
 * Estructuras de Control
 * ----------------------    
 */
 
//Condicionales

let myString = "";

if (myString == "JuanG") {
    console.log("My String es JuanG");
}else if (myString == "DavidG") {
    console.log("My String es DavidG");
} else {
console.log('My String no es "JuanG" ni "DavidG"');
}
    
 //Iterativas

 for (let i = 0; i < 11; i++) {
    console.log(i)
}

//Manejo de excepciones

try {
    print(10/0)
} catch (error) {
    console.log("Se ha producido un error")
} finally{
console.log("Ha finalizado el manejo de excepciones")
}

/* 
 * ----------------
 * Dificultad Extra
 * ----------------
 */

for (let i = 10; i <= 55; i++) {
    if (i % 2 === 0 && i !==16 && i % 3 !== 0){
    console.log(i)
    }
}