/*
 * EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
 */

//Refiere a cómo se manejan los valores y las direcciones de memoria cuando se asignan variables en un programa

//Asignación por valor
/*
En la asignación por valor, se copia el contenido de la variable original en la nueva variable.
Las dos variables son independientes y ocupan ubicaciones de memoria diferentes.
 */
let variableoriginal= 10
let variablecopia= variableoriginal //Asignación por valor
variableoriginal=20

console.log(`La variable original ahora vale ${variableoriginal} mientras que la variable copia 
guarda el primer valor de la original en este caso ${variablecopia}`)

//Asignación por referencia
/*
En la asignación por referencia, la nueva variable hace referencia a la misma ubicación de memoria que la variable original.
 En este caso, cualquier cambio en una variable afectará a la otra, ya que comparten la misma ubicación de memoria.
*/

let arrayoriginal = ["Hola","Alexdevrep","Mundo"]
let arraycopia = arrayoriginal

arraycopia[2] = "JavaScript" 

console.log (arrayoriginal)
/*Como podemos obsevar aunque hayamos modificado el array copia tambien se modifica el original
ya que ambos apuntan a la misma ubicación de memoria */

//Funciones con variables por valor

function saludar(saludo){
     let mi_saludo = `Hola, ${saludo}`
    return mi_saludo
}

let holamundo = "JavaScript"
let resultado = saludar(holamundo)
console.log(holamundo) //La variable original no se modifica
console.log(resultado)

//Funciones con variables por referencia

function agregarelemento(array,elemento){
    array.push(elemento)

}
//Vamos a usar el arrayoriginal creado anteriormente
agregarelemento(arrayoriginal,"Mundo")
console.log(arraycopia)//Imprimimos el arraycopia para comprobar que efectivamente ambos array apuntan a la misma ubicación de la memoria


//DIFICUALTAD EXTRA
/* DIFICULTAD EXTRA (opcional):
* Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
* - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
*   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
*   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
*   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
*   Comprueba también que se ha conservado el valor original en las primeras.
*/

let valor1 = 3
let valor2 = 5
let objetoOriginal= { valor1: "Hola", valor2:"JavaScript"}
let objetoNuevo = programa2(objetoOriginal)

function programa1 (valor1,valor2){
    valor1 = 5
    valor2 = 3
    return [valor1, valor2]

}

function programa2 (objeto){
    let intercambio =objeto.valor1
    objeto.valor1=objeto.valor2
    objeto.valor2 = intercambio
    return objeto
   
}

console.log ("Resultado del programa 1: ")
console.log (`El valor de la variables originales es ${valor1} para la variable valor1 y ${valor2} para la variable valor2`)
let [valor1nuevo, valor2nuevo] = programa1(valor1,valor2)
console.log("El valor1 ahora será:" + valor1nuevo)
console.log("El valor2 ahora será:"+valor2nuevo)
console.log("-------------------------------------")
console.log ("Resultado del programa 2: ")

console.log ("Valores originales:", objetoOriginal.valor1,objetoOriginal.valor2)
console.log ("Valores nuevos:", objetoNuevo.valor1,objetoNuevo.valor2)












