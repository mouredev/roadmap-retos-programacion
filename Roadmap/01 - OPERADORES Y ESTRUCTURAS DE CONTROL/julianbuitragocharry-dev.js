
//✔️OPERADORES
// Elemento encargado de manipular los operandos. Junto a sus operandos conforman una expresion que da como resultado un valor.

//✔️OPERADORES ARITMETICOS
// Son los operadores matematicos que de toda la vida conocemos [+ , - , * , / , %]. 
// Asimismo existen OPERADORES DE DECREMENTO E INCREMENTO.
let num1 = 1;
let num2 = 4;

/*1️⃣ PRE INCREMENTO*/        x++; //Equivalente a: x = x + 1 
/*2️⃣ POST INCREMENTO*/       ++x; //Equivalente a: x = x + 1                      
/*3️⃣ PRE DECREMENTO*/        x--; //Equivalente a: x = x - 1                               
/*4️⃣ POST DECREMENTO*/       --x; //Equivalente a: x = x - 1


//✔️OPERADORES DE ASIGNACIÓN
// Asignan valores a las variables u operando izquierdo, (🟰). 
let x = 7;
let y = 12; 

/*1️⃣ ASIGNACIÓN BÁSICA*/                                         x = y;
/*2️⃣ ASIGNACIÓN DE ADICIÓN*/                                     x += y; // Equivalente a: x = x + y
/*3️⃣ ASIGNACIÓN DE RESTA*/                                       x -= y; // Equivalente a: x = x - y
/*4️⃣ ASIGNACIÓN DE MULTIPLICACIÓN*/                              x *= y; // Equivalente a: x = x * y
/*5️⃣ ASIGNACIÓN DE DIVISIÓN*/                                    x /= y; // Equivalente a: x = x / y
/*6️⃣ ASIGNACIÓN DE RESIDUO*/                                     x %= y; // Equivalente a: x = x % y
/*7️⃣ ASIGNACIÓN DE EXPONENTE*/                                   x **= y; // Equivalente a: x = x ** y
/*8️⃣ ASIGNACIÓN DE DESPLAZAMIENTO A LA IZQUIERDA*/               x <<= y; // Equivalente a: x = x << y
/*9️⃣ ASIGNACIÓN DE DESPLAZAMIENTO A LA DERECHA*/                 x >>= y; // Equivalente a: x = x >> y
/*🔟 ASIGNACIÓN DE DESPLAZAMIENTO A LA DERECHA SIN SIGNO*/      x >>>= y; // Equivalente a: x = x >>> y
/*1️⃣1️⃣ ASIGNACIÓN AND BIT A BIT*/                                x &= y; // Equivalente a: x = x & y
/*1️⃣2️⃣ ASIGNACIÓN XOR BIT A BIT*/                                x ^= y; // Equivalente a: x = x ^ y
/*1️⃣3️⃣ ASIGNACIÓN OR BIT A BIT*/                                 x |= y; // Equivalente a: x = x | y
/*1️⃣4️⃣ ASIGNACIÓN AND LÓGICO*/                                   x &&= y; // Equivalente a: x = x && y
/*1️⃣5️⃣ ASIGNACIÓN OR LÓGICO*/                                    x ||= y; // Equivalente a: x = x || y
/*1️⃣6️⃣ ASIGNACIÓN DE ANULACIÓN*/                                 x ??= y; // Equivalente a: x = x ?? y


//✔️OPERADORES DE COMPARACIÓN
// Encargados de devolver un valor booleano TRUE[☑️] or FALSE[❎], aceptando operandos numéricos, de cadena, lógicos u objetos... 
let z = 3;
let w = 4; 

/*1️⃣ IGUAL*/                   z == w; // Devuelven {true} si los operadores son iguales 
/*2️⃣ NO ES IGUAL*/             z != w; // Devuelve {true} si los operadores no son iguales 
/*3️⃣ ESTRICTAMENTE IGUAL*/     x === y; // Devuelve {true} si los operadores son iguales y del mismo tipo
/*4️⃣ DESIGUALDAD ESTRICTA*/    x !== y; // Devuelve {true} si los operadores no son iguales y son de diferente tipo 
/*5️⃣ MAYOR QUE*/               x > y; // Devuelve {true} si el operando izquierdo es mayor que el derecho
/*6️⃣ MAYOR O IGUAL QUE*/       x >= y; // Devuelve {true} si el operando izquierdo es mayor o igual que el derecho
/*7️⃣ MENOR QUE*/               x < y; // Devuelve {true} si el operando izquierdo es menor que el derecho 
/*8️⃣ MENOR O IGUAL QUE*/       x <= y; // Devuelve {true} si el operando izquierdo es menor o igual que el derecho

//✔️OPERADORES LOGICOS
//Son utilizados para obtener booleanos, son el equivalente a las tablas de verdades.
let bool_1 = true;
let bool_2 = false;

/*1️⃣ AND LOGICO*/     bool_1 && bool_2 //Devuelve {true} si ambos valores son {true} 
/*2️⃣ OR LOGICO*/      bool_1 || bool_2 //Devuelve {true} si alguno de los dos es {true}
/*3️⃣ NOT LOGICO*/     !bool_1 //Sirve para negar el booleano

//✔️OPERADOR TERNIARIO
// Se evalua como una condicion equivalente a un if {} else {}.
var status = age >= 18 ? "adult" : "minor";

//✔️OPERADOR UNITARIO DELETE
// Elimina propiedades de objetos.
delete object.property;
delete object[propertyKey];
delete objectName[index];
delete property; // legal solo dentro de una declaración with

//❗NOTA: devuelve true si la operación es posible; devuelve false si la operación no es posible.

//✔️OPERADOR DE RELACION IN
// El operador in devuelve true si la propiedad especificada está en el objeto especificado. La sintaxis es:
propNameOrNumber in objectName; //Devuelve true si dicha propNameOrNumber se encuentra en el objeto.
                                //Es util tambien para recorrer Arrays.



//✔️ESTRUCTURAS DE CONTROL