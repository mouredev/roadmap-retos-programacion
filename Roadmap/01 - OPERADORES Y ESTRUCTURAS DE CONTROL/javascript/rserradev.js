// Ejemplos con operadores

// Operadores de asignación
let asignacion = 1;
asignacion += 1; //suma
asignacion -= 1; //resta
asignacion *= 1; //multriplicacion
asignacion /= 1; //division
asignacion %= 1; //porcentaje
asignacion **= 1; //elevado o exponente
asignacion <<= 1; //desplazar izquierda
asignacion >>= 1; //desplazar derecha
asignacion &= 1; //AND
asignacion |= 1; //OR
asignacion ||= 1; //OR logico
asignacion ??= 1; //anulacion

//Operadores de comparacion
let var1 = 1;
let var2 = 2;

console.log(var1 == var2); //Igualdad (false)
console.log(var1 != var2); //No es igual (true)
console.log(var1 === var2); //Igualdad estrictor (False)
console.log(var1 !== var2); //No es igualdad estricto (False)
console.log(var1 > var2); //Mayor que (false)
console.log(var1 < var2); //Menor que (true)
console.log(var1 >= var2); //Mayor o igual que (False)
console.log(var1 <= var2); //menor o Igualdad (true)

//Operadores aritméticos
console.log(++var2); //Incremento
console.log(--var2); //Decremento
console.log(-var2); //Negativo
console.log(+var2); //Negativo
console.log(var2 ** var2); //Exponente

// Operadores bit a bit
console.log(var2 & var2); // AND de bits
console.log(var2 | var2); // OR de bits
console.log(var2 ^ var2); // XOR de bits
console.log(~var2); // NOT de bits

// Operadores logicos
let var3 = 10;
let var4 = "10";

console.log(var3 && var4); // AND Logico
console.log(var3 || var4); // OR Logico
console.log(!var3); // NOT Logico

// Operadores de cadena
console.log("Esta es una" + "cadena");

// Operadores condicionales (ternario)
let edad = 25;
let isOld = edad >= 18 ? true : false;
console.log(isOld);

// Operadores relacionales
let numeros = [1,2,3,4,5];
console.log(0 in numeros);
console.log(6 in numeros);
let numero55 = 55;

// Imprimir por consola numeros pares entre 10 y 55 descartando el 16 y multiplos de 3
for (let index = 10; index <= numero55; index++) {
    if (index != 16) {
        for (let i = 0; i <= numero55; i++) {
            if (2 * i == index) {
            console.log(index);
            }
        }
    }
}