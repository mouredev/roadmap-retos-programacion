import Foundation
/* EJERCICIO:
- Muestra ejemplos de asignación de variables "por valor" y "por referencia", según su tipo de dato.
 
 - Muestra ejemplos de funciones con variables que se les pasan "por valor" y "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 
 (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 */

/* Por valor:
 Creamos una copia independiente de la variable original que no afecta a la original.
 
 Ejemplo:
 Tenemos una receta de un pastel que le hacemos una copia y se la pasamos a un amigo si este decide modificar esa copia
 cambiar las cantidades, ingredientes.. nuestra receta orginal que tenemos nosotros no se va ver afectada. */

var recetaOriginal = "Harina, azúcar, huevos" // Receta original
var recetaCopia = recetaOriginal // Copia de la receta que le damos a nuestro amigo

recetaCopia += ", chocolate" // El colega que es un Gotxo añade chocolate a su copia
print(recetaOriginal) // Imprimimos la receta original
print(recetaCopia) // imprimimos la receta de nuestro amigo


/* Por referencia:
 En lugar de crear copias de esos valores pasarmos una referenica a una variable que si luego la modificas vas a modificar el
 valor de la original
 
 Ejemplo:
 El colega del pastel y tu compartis coche cada uno tiene una copia de la llave con lo que tenemos acceso a la clase coche
 que no es una copia si no el mismo coche, nuestro amigo le cambia el color al coche, nosotros podemos acceder al coche pero
 nos a cambiado el coche */

class Coche {
    var color = "Rojo"
}

var cocheCompartido = Coche() // ahi tenemos nuestro coche compartido
cocheCompartido.color = "Azul" // nuestro amigo va y nos cambia el color
print(cocheCompartido.color) // imprimira el color azul


/* DIFICULTAD EXTRA (opcional):
Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
* - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
*   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
*   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
*   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
*   Comprueba también que se ha conservado el valor original en las primeras.
 */

func intercambiaPorValor(a: String, b: String) -> (String, String) {
    // Aquí estamos intercambiando los valores a y b.
    // Como los Strings se pasan por valor, las modificaciones se hacen en copias.
    return (b, a)
}

// Variables originales
var valor1 = "Manzana"
var valor2 = "Banana"

// Intercambio valores
let (nuevoValor1, nuevoValor2) = intercambiaPorValor(a: valor1, b: valor2)

// Imprimo valores originales y nuevos
print("Original: \(valor1), \(valor2)") // Manzana, Banana
print("Intercambiado: \(nuevoValor1), \(nuevoValor2)") // Banana, Manzana


class Envoltura {
    var contenido: String

    init(contenido: String) {
        self.contenido = contenido
    }
}

func intercambiaPorReferencia(a: Envoltura, b: Envoltura) {
    // intercambiando los contenidos de a y b.
    // Como Envoltura es una clase, a y b se pasan por referencia.
    let temporal = a.contenido
    a.contenido = b.contenido
    b.contenido = temporal
}

// Instancias de clase pasadas por referencia
var envoltura1 = Envoltura(contenido: "Chocolate")
var envoltura2 = Envoltura(contenido: "Vainilla")

// Intercambiando contenidos
intercambiaPorReferencia(a: envoltura1, b: envoltura2)

// Imprimolos contenidos después del cambio
print("Envoltura 1: \(envoltura1.contenido), Envoltura 2: \(envoltura2.contenido)") // Vainilla, Chocolate
