// *** OPERADORES DE ASIGNACION ***

//Asignacion
let x: number = 5 
let y: number = 10
console.log('Asignacion:', x, y)

//Asignacion de Adicion
x = x + y
console.log('Adicion 1:', x)
x += y
console.log('Adicion 2:', x)

//Asignacion de Resta
x = x - y
console.log('Resta 1:', x)
x -= y
console.log('Resta 2:', x)

//Asignacion de Multiplicacion
x = x * y
console.log('Multiplicacion 1:', x)
x *= y
console.log('Multiplicacion 2:', x)

//Asignacion de Division
x = x / y
console.log('Division 1:', x)
x /= y
console.log('Division 2:', x)

//Asignacion de Residuo
x = x % y
console.log('Residuo 1:', x)
x %= y
console.log('Residuo 2:', x)

//Asignacion de Exponente
x = x ** y
console.log('Exponente 1:', x)
x **= y
console.log('Exponente 2:', x)

//Asignacion AND logico
x = x && (x = y)
console.log('AND logico 1:', x)
x &&= y
console.log('AND logico 2:', x)

//Asignacion OR logico
x = x || (x = y)
console.log('OR logico 1:', x)
x ||= y
console.log('OR logico 2:', x)

//Asignacion Anulacion logico
x = x ?? (x = y)
console.log('Anulacion logico 1:', x)
x ??= y
console.log('Anulacion logico 2:', x)




// *** OPERADORES DE COMPARACION ***
let a: number = 4
let b: number = 8

//Igual
console.log('Igual: ', a == b)

//No es igual
console.log('No es igual: ', a != b)

//Igualdad estricta
console.log('Igualdad estricta: ', a === b)

//Desigualdad estricta
console.log('Desigualdad estricta: ', a !== b)

//Mayor que
console.log('Mayor que: ', a > b)

//Mayor o igual que
console.log('Mayor o igual que: ', a >= b)

//Menor que
console.log('Menor que: ', a < b)

//Menor o igual que
console.log('Menor o igual que: ', a <= b)



// *** OPERADORES ARITMETICOS ***
let num1: number = 10
let num2: number = 4

//Residuo
console.log('Residuo: ', num1 % num2)

//Incremento
console.log('Incremento antes de imprimir: ', ++num1) 
console.log('Incremento despues de imprimir: ', num1++) //Se vuelve 12 luego de imprimir

//Decremento
console.log('Decremento antes de imprimir: ', --num1)
console.log('Decremento despues de imprimir: ', num1--) //Se vuelve 10 luego de imprimir

//Negacion unitaria
console.log('Negacion unitaria: ', -num1)

//Positivo unitaria
console.log('Negacion unitaria: ', +num1)

//Exponenciacion
console.log('Exponenciacion: ', num1 ** num2)



// *** OPERADORES BIT A BIT ***
let bit1: number = 6
let bit2: number = 8

//Desplazamiento a la izquierda
console.log('Desplazamiento a la izquierda:', bit1 << bit2)

//Desplazamiento a la derecha
console.log('Desplazamiento a la derecha:', bit1 >> bit2)

//AND
console.log('AND bit a bit:', bit1 & bit2)

//OR
console.log('AND bit a bit:', bit1 | bit2)

//XOR
console.log('AND bit a bit:', bit1 ^ bit2)

//NOT
console.log('AND bit a bit:', bit1 ~ bit2)


// *** OPERADORES LOGICOS ***
const exp1 = true
const exp2 = false

//AND logico
console.log('AND Logico: ', exp1 && exp2)

//OR logico
console.log('OR Logico: ', exp1 || exp2)

//NOT logico
console.log('NOT Logico: ', !exp1)




// *** OPERADORES DE CADENA ***
console.log("mi " + "cadena")



// *** OPERADOR CONDDICIONAL TERNARIO ***
const result = true ? true : false
console.log(result)



// *** OPERADORES RELACIONALES ***
interface IObj {
  id: string
  name: string
  age: number
}

const user: IObj = {
  id: '1',
  name: 'Andres',
  age: 86
}

console.log('Existe "age" en el objeto user?: ', 'age' in user)
console.log('Existe "country" en el objeto user?: ', 'country' in user)




// *** ESTRUCTURAS DE CONTROL ***

// * CONDICIONAL *
let num = 25

// IF-ELSE
if(num > 18){
  console.log('Es mayor de edad')
}else{
  console.log('Es menor de edad')
}


//SWITCH
switch(num){
  case 20:
    console.log('Es 20')
    break
  case 25:
    console.log('Es 25')
    break
  case 30:
    console.log('Es 30')
    break
  default:
    console.log('Default')
    break
}


// * BUCLES *
let i: number = 10
let w: number = 15

//WHILE
while(i < w){
  i++
  console.log('Nuevo valor de i:', i)
}


//DO-WHILE
i = 10

do{
  i++
  console.log('Nuevo valor de i:', i)
} while(i < w)

//FOR
for(let i = 0; i < 10; i++){
  console.log('Nuevo valor de i:', i)
}



// *** EJERCICIO EXTRA ***
console.log('EJERCICIO EXTRA')
for(let i = 10; i <= 55; i++){
  if(i % 2 === 0){
    if(i === 16){
      console.log('Ignorar')
    }else if(i % 3 === 0){
      console.log('Multiplo de 3')
    }else{
      console.log(i)
    }
  }else{
    console.log('No es par')
  }
}