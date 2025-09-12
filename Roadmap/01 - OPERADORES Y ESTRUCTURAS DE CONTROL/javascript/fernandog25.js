//Operadores aritméticos

var  a = 3
var  b = 2

suma = a + b
resta = a - b
mult = a * b
div = a / b
mod = a % b
incr = ++a
decr = a--
neg= -a
exp = b**a

console.log("Operadores aritméticos: \n")
console.log("La suma de 3 y 2 es igual a " + suma)
console.log("La diferencia entre 3 y 2 es igual a " + resta)
console.log("La multiplicacion entre 3 y 2 es igual a " + mult)
console.log("La division entre 3 y 2 es igual a " + div)
console.log("El resto entre 3 y 2 es igual a " + mod)
console.log("El incremento de 3 es " + incr)
console.log("La negacion de 3 es " + neg)
console.log("2 elevado al cubo es igual a" + exp)



//Operadores lógicos

var  c = true
var  d = false

and = c && d
or  = c || d
not = !c

console.log("\nOperadores lógicos: \n")
console.log("True and false da " + and)
console.log("True or false da " + or)
console.log("La negacion de true es " + not)



//Operadores de comparación


console.log("\nOperadores de comparación: \n")
console.log("2 es igual a 3: ", a==b )
console.log("2 no es igual a 3:", a!=b)
console.log("2 es estrictamente igual a 3:", a===b)
console.log("2 es estrictamente desigual a 3:", a!==b)
console.log("2 es mayor a 3:", a>3)
console.log("2 es mayor o igual a 3:", a>=b)
console.log("2 es menor a 3:", a<b)
console.log("2 es menor o igual a 3:", + a<=b)



//Operadores de asignación

console.log("\nOperadores de asignación \n")

a = b // asignación
console.log("asignacion: a = " + a + ", b = " + b)

a += b // asignación de adicion
console.log("asignacion de adicion: a = " + a + ", b = " + b)

a -= b // asignación de resta
console.log("asignacion de resta: a = " + a + ", b = " + b)

a *= b // asignación de multiplicación
console.log("asignacion de multiplicacion: a = " + a + ", b = " + b)

a /= b // asignación de división
console.log("asignacion de division: a = " + a + ", b = " + b)

a %= b // asignación de residuo
console.log("asignacion de residuo: a = " + a + ", b = " + b)

a **= b // asignación de exponenciación
console.log("asignacion de exponenciacion: a = " + a + ", b = " + b)

a <<= b // asignación de desplazamiento a la izquierda
console.log("asignacion de desplazamiento a la izquierda: a = " + a + ", b = " + b)

a >>= b // asignación
console.log("asignacion: a = " + a + ", b = " + b)

a = b // asignación de desplazamiento a la derecha
console.log("asignacion de desplazamiento a la derecha: a = " + a + ", b = " + b)

a >>>= b // asignación de desplazamiento a la derecha sin cargo
console.log("asignacion de desplazamiento a la derecha sin cargo: a = " + a + ", b = " + b)

a &= b // asignación and bit a bit
console.log("asignacion and bit a bit: a = " + a + ", b = " + b)

a ^= b // asignación xor bit a bit
console.log("asignacion xor bit a bit: a = " + a + ", b = " + b)

a |= b // asignación or bit a bit
console.log("asignacion or bit a bit: a = " + a + ", b = " + b)

a &&= b // asignación and logico
console.log("asignacion and logico: a = " + a + ", b = " + b)

a ||= b // asignación or logico
console.log("asignacion or logico: a = " + a + ", b = " + b)

a ??= b // asignación de anulación lógica
console.log("asignacion de anulacion logica: a = " + a + ", b = " + b)



//Operadores bit a bit

var e = 4 //100
var f = 6 //110

console.log("\nOperadores bit a bit \n")
console.log("and: ", e & f)
console.log("or: ", e | f)
console.log("xor: ", e ^ f)
console.log("not: ", e % f) //acomodar
console.log("desplazamiento a la izquierda: ", e << f)
console.log("desplazamiento a la derecha de propagacion de signo: ", e >> f)
console.log("desplazamiento a la derecha de relleno cero: ", e >>> f)



//Estructuras de control

num1 = 1;
num2 = 2;

console.log("\nif\n")
if (num1 == num2)
console.log("Los numeros son iguales")
else if (num1 > num2)
console.log("num1 es mayor a num2")
else
console.log("num 1 es menor a num2")

console.log("\nswitch\n")

animal = "perro"

switch (animal)
{
case "gato":
    console.log("El animal es un gato")
    break
case "perro":
    console.log("El animal es un perro")
    break
case "oso":
        console.log("El animal es un oso")
        break
case "gallina":
    console.log("El animal es una gallina")
break
default:
    console.log("No se encuentra el animal")
}

console.log("\nfor\n")

for(var i = 0; i<=10; i++)
{
    console.log(i)
}

console.log("\nwhile\n")

numero = 0
console.log("Numeros pares")
while(numero < 11)
{
    if (!(numero % 2))
        console.log(numero)
    numero++
}



/*Ejercicio extra 
Crea un programa que imprima por consola todos los números comprendidos
entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.*/



console.log("\nEjercicio extra\n")


for(var i = 10; i<56; i++)
{
    if (!(i % 3) || i == 16)
    {

    }
        else if (i % 2 == 0)
    console.log(i)
}