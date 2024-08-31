// OPERADORES

//Operadores de asignación

y = 1
x = y //Asignación
console.log (x)

//Operadores Bit a Bit

x = x << y //Asignación de desplazamiento a la izquierda: Desplaza x
// en representación binaria y bits hacia la izquierda, desplazándose en ceros desde la derecha.
console.log (x)
x = x >> y //Asignación de desplazamiento a la derecha: Desplaza x
// en representación binaria y bits hacia la derecha, descartando los bits desplazados.
console.log (x)
x = x >>> y //Asignación de desplazamiento a la derecha sin signo: Desplaza x
// en representación binaria y bits hacia la derecha, descartando los bits desplazados y desplazándose en ceros desde la izquierda.
console.log (x)
x = x & y //Asignación AND bit a bit: Devuelve 1 cuando los bits de cada número es 1, sino es 0.
console.log (x)
x = x ^ y //Asignación XOR bit a bit: Devuelve 0 para bits iguales y 1 para bits diferentes de los números evaluados.
console.log (x)
x = x | y //Asignación OR bit a bit: Devuelve 1 si uno de los bits de los números es 1, sino es 0.
console.log (x)
x = ~x //Invierte los bits del operando.
console.log (x)

//Operadores aritmeticos

a = 1 + 2 //Adición 
console.log (a)
b = 2 - 1 //Resta
console.log (b)
c = 2 * 1 //Multiplicación
console.log (c)
d = 2 / 1 //División
console.log (d)
f = 2 % 1 //Residuo
console.log (f)
g = 2 ** 2 //Exponenciación
console.log (g)
g++ //Incremento en uno
console.log (g)
g-- //Decremento en uno
console.log (g)
g = -g //Negación unaria: Coloca en negativo el número
console.log (g)
g = "3"
g = +g //Positivo unario: convierte operador en un número
console.log (g)

//Operadores de comparación
z = 3
y = 4
p = z == y //True si los operadores son iguales
console.log (p)
p = z != y //True si los operadores son diferentes
console.log (p)
p = z === y //True si los operadores son iguales y del mismo tipo
console.log (p)
p = z !== y //True si los operadores son del mismo tipo pero no iguales
console.log (p)
p = z > y
console.log (p)
p = z >= y
console.log (p)
p = z < y
console.log (p)
p = z <= y
console.log (p)

//Operadores Lógicos
var1 = true
var2 = false
var3 = var1 && var2 //AND lógico: Para booleanos, devuelve true 
//si ambos operandos son true; de lo contrario, devuelve false
console.log (var3)
var3 = var1 || var2 // OR Lógico: devuelve true 
//si alguno de los operandos es true; de lo contrario, devuelve false
console.log (var3)
var3 = !var3
console.log (var3)

//Operador de concatenación

console.log ("yo soy " + "Batman")

//Operador Condicional Ternario

precio = 3000
var valor = precio >= 30000 ? "Costoso" : "Barato" 
//Operador que asigna un valor a la variable inicial dependiendo del resutado de la comparación.
//Si la condición es true, asigma el valor costoso, de lo contrario es barato.
console.log (valor)

//Operadores unarios

x = 4
var prueba = {p: 2}
var5 = delete x //operador delete: elimina la propiedad de un objeto.
//Si la puede elimiar devuelve true, sino false.
var6 = delete prueba.p
console.log (var5)
console.log (var6)

var7= typeof x //Indica el tipo de dato de la variable
console.log (var7)

//Operadores relacionales

var animales = ["Leon", "Conejo", "Serpiente", "Aguila"]
var refIn = 2 in animales //In: Indica si la propiedad especificada existe en el
//objeto especificado. En este caso, valida si existe un objeto en la posición 2.
console.log (refIn)

//ESTRUCTURAS DE CONTROL

//Bucles

//While
var contador = 1
while (contador > 0){ //Mientras se cumpla la condición se ejecuta el bucle
    console.log (contador)
    contador--
}

//do-while
var contador1 = 1
do { //Do lo que permite es que la función dentro del bucle se ejecute al menos
    //una vez y luego se repita si cumple la condición.
    console.log (contador1)
    contador1--
    } while (contador > 0);

//For
var contador2 = 3
for (i = 0; i <= contador2; i++){//Se ejecuta el código mientras se cumpla la condición
    console.log (i)
}

//Condicionales

 //If-else
    var numero = -1
    if (numero >= 0) { //Si se cumple la condición ejecute el siguiente código
        console.log("Número positivo")
        }
    else console.log ("Número negativo") //Sino, ejecuta este código

//Switch
var animo = 3;
switch (animo) {//Dependiendo del valor indicado en la variable animo, se ejecuta
    //el segmento de código asociado al valor y se sale del switch
case 1:
console.log ("Estoy feliz");
break;
case 2:
console.log ("Estoy triste");
break;
case 3:
console.log ("Estoy Ansioso");
break;
default:
console.log("No se como me siento");
}

//Manejo de excepciones

//Try...catch: Try permite ejecutar una sección de código para encontrar errores
//catch permite manejar los errores encontrados

try {
    console.log ("Probemos el código"); //Se ejecuta está sección
    fallo; //Variable fallo no definida, genera error
    console.log ("El código fue exitoso"); //Sección que no se ejecuta
}//Para que try and catch funciones el código debe ser ejecutable, sin errores de sintaxis
catch (err){
    console.log ('Se encontro el error:' + err); //Catch captura error y lo muestra
}
//Finally: permite ejecutar código posterior a try and catch, a pesar del resultado
finally {
    console.log ("Está sección siempre se ejecuta")
}

//Crea un programa que imprima por consola todos los números comprendidos
// * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
//var number = 55
for (var i = 10; i <= 55; i++) {
    var j = i % 2
    var h = i % 3
    if (i === 16 || h === 0 || j != 0){
        i++
        }
    else {
        console.log (i)
        i++
         }
    }
