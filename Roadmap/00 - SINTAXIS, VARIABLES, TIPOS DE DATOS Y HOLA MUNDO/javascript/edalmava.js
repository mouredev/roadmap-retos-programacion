// Comentario de una línea
// La especificación oficial del lenguaje es ECMAScript(ECMA-262)
// Sitio oficial: https://ecma-international.org/publications-and-standards/standards/ecma-262/
// Ultima edición a 26/06/2024: https://262.ecma-international.org/14.0/

/* 
  Comentario de varias líneas o multilinea
*/

/* 
   Para declarar una variable se usa la palabra reservada var, let o const
   Para variables mutables se usa var y let
   Actualmente se debería usar let 

   Para variables inmutables(contantes) se usa la palabra reservada const

   Se asignan valores usando el operador =

   La asignación sigue la siguiente sintaxis:
       nombre_variable = valor
*/

// Tipos de datos y valores

// Tipos primitivos

// Tipo null
const tipo_null = null

// Tipo undefined - cualquier variable a la que no se le ha asignado un valor tiene le valor undefined
let tipo_undefined       // El valor de la variable es undefined 

// Tipo Boolean - dos valores true y false
const verdadero = true
const falso = false

// Tipo cadena(String)
const lenguaje = "JavaScript"
const cadena2 = 'Otra cadena'
const mensaje = `¡Hola, ${lenguaje}!` 

// Tipo Symbol - Representan identificadores únicos
const id = Symbol("id")

// Tipos Númericos
// Tipo Number - Representan valores de doble precisión de 64 bits siguiendo el formato IEEE 754-2019 
const numero = 5
const numero2 = 5.0
const no_es_un_numero = NaN  // valor especial de 'Not-a-Number' 
const mas_infinito = +Infinity   // valor especial infinito positivo 
const menos_infinito = -Infinity // valor especial infinito negativo

// Tipo BigInt - Representan valores enteros muy grandes que no se pueden alamacenar de forma segura como tipo NUmber
const bigInt = 1234567890123456789012345678901234567890n;  // Se agrega la n al final del número entero

// Tipos no primitivos
// Tipo Object
const objeto = {

}

console.log(mensaje)
