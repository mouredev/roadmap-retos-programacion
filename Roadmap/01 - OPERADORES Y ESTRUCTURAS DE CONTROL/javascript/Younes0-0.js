//Operadores de asignación
let x  = 5
x = x + 5   // abreviado x += 5
x = x - 5   // abreviado x -= 5
x = x * 5   // abreviado x *= 5
x = x / 5   // abreviado x /= 5
x = x ** 5  // abreviado x **= 5
x = x % 5   // abreviado x %= 5


// Desestructuración 
let identidad  = {
    nombre : "Younes",
    apellido : "Ozux",
    edad : 30,
    ciudad : "Almería",
    pais : "España",
    hobby : "Programar"
}

let {nombre, apellido} = identidad

//Operadores de comparación
let operacion 
// Igualdad
operacion = (10 == 10)      
// Distinto
operacion = (10 != 10)      
// Estrictamente igual
operacion = (10 === 10)     
// Estrictamente desigual
operacion = (10 !== 10)     
// Mayor que
operacion = (10 > 10)       
// Menor que
operacion = (10 < 10)       
// Mayor o igual que
operacion = (10 >= 10)      
// Menor o igual que
operacion = (10 <= 10)      

//Operadores aritméticos
// Residuo de la división
let residuo = 10 % 3
// Incremento
let incremento = 10
incremento++
// Decremento
let decremento = 10
decremento--
// Negación unaria	
let negacion = 10
negado = -negacion
// Operador de exponenciación
let exponenciacion = 10
exponenciacion **= 2

//Operadores bit a bit
let a = 15 // 1111 
let b = 9 // 1001  
let resultado
//AND
resultado = a & b // 1001 
//OR
resultado = a | b // 1111 
//XOR
resultado = a ^ b // 0110 
//NOT
resultado = ~a // 0000  
//Desplazamiento a la derecha
resultado = b >> 2 // 0010  
//Desplazamiento a la izquierda
resultado = b << 2 // 100100 

//Operadores lógicos
let p = true
let q = false
p && q      //AND lógico
p || q      //OR lógico
!p          //NOT lógico

//Operadores de cadena
let s = "Hola"
let t = "Mundo"
saludo = s + " " + t //Concatenación

//Operador condicional (ternario)
saludo = (a > b) ? "a es mayor que b" : "a es menor que b"

//Operador coma
var w = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
var h = [w, w, w, w, w]

for (var i = 0, j = 9; i <= j; i++, j--)
  //                              ^
  console.log("a[" + i + "][" + j + "]= " + h[i][j]);


//Operadores unarios es una operación con un solo operando.

// delete -> elimina la propiedad de un objeto.
let property = {name: "Younes"}
delete property.name 
/*Si el operador delete tiene éxito, elimina la propiedad del objeto. Intentar acceder a él después dará como resultado undefined. 
El operador delete devuelve true si la operación es posible; devuelve false si la operación no es posible.*/

// typeof -> devuelve una cadena que indica el tipo de operando
typeof property
console.log(typeof property, property.name)

// void -> especifica una expresión que se evaluará sin devolver un valor.
resultado = void( 10 > 5)
resultado = void 10

//Operadores relacionales

// in -> devuelve true si la propiedad existe en el objeto.
let object = {name: "Younes"}
console.log("name" in object)

// instanceof -> devuelve true si el objeto es una instancia de una clase.
class Persona {}
let persona = new Persona()
console.log(persona instanceof Persona)

// Expresiones -> es cualquier unidad de código válida que se resuelve en un valor.

// Expresiones primarias -> Palabras clave básicas y expresiones generales en JavaScript.

// this -> es el contexto donde se ejecuta el código.(dueño de la función)
// Función tradicional
function getName() {
    console.log(this.nick);
}

// Función de flecha
var getAge = () => console.log(this.nick)


// global === globalThis === window === this
global.nick = "younes"
getName() // imprime "younes" porque el dueño de la función es el objeto global

var younes = {
    nick : "yuyu",
    getName : getName,
    getAge : getAge,
    age : 36
}
younes.getName() // imprime "yuyu" porque el dueño de la función es el objeto younes
    
// En las funciones de flecha no pueden ser dueñas por lo tanto no tiene contexto de ejecución 
younes.getAge() // imprime "undefined" 

// Expresiones del lado izquierdo

// new -> crea una nueva instancia de un tipo de objeto definido.
function Car(make, model, year) {
    this.make = make;
    this.model = model;
    this.year = year;
}
  
const car1 = new Car('Eagle', 'Talon TSi', 1993);

// super -> es usada para acceder y llamar funciones del padre de un objeto.class Rectangle {

class Rectangle {
    constructor() {}
    static logNbSides() {
      return "Tengo 4 lados";
    }
}
  
class Square extends Rectangle {
    constructor() {}
    static logDescription() {
      return super.logNbSides() + " que son todos iguales";
    }
}

