/*
 * EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 */

/*
 Variable / constante global
 */
let firstString = "Hello"



/*
 Función sin parámetros ni retorno
 */
func printFirstString() {
    print(firstString)
}

printFirstString()



/*
 Función con un parámetro y sin retorno
 */
func printSecondString(secondString: String) {
    print(secondString)
}

printSecondString(secondString: "World")



/*
 Función con varios parámetros y con retorno
*/
func concatStrings(firstString: String, secondString: String) -> String {
    let localVariable = "\(firstString) \(secondString)"
    
    return localVariable
}

print(concatStrings(firstString: "Hello", secondString: "world"))



/*
 Función con varios parámetros y varios retornos
*/
func concatSpecialPhrase(firstString: String, secondString: String) -> (cutePhrase: String, normalPhrase: String) {
    let cutePhrase = "\(firstString), have a nice day!"
    let normalPhrase = "\(secondString), bye"
    
    return (
        cutePhrase,
        normalPhrase
    )
}

let (cutePhrase, normalPhrase) = concatSpecialPhrase(firstString: "Hello", secondString: "Hello")

print(cutePhrase)
print(normalPhrase)



/*
 Función dentro de otra función
*/
func printGreetings() {
    let firstString = "Hello"
    let secondString = "Today is a good day"
    
    let (cutePhrase, normalPhrase) = concatSpecialPhrase(
        firstString: firstString,
        secondString: secondString
    )
    
    print(cutePhrase, ".", normalPhrase)
}

printGreetings()



/*
 Funciones ya creadas en el lenguaje
*/
let exists = [1, 2, 3].contains(2)

print("[1, 2, 3].contains(2) = \(exists)")



/*
 Extra
*/

print("\n ------EXTRA------")


func extraExercise(firstString: String, secondString: String) -> Int {
    var totalNumberPrinted: Int = 0
    
    for value in 1...100 {
        let isMultipleOfThree = value % 3 == 0
        let isMultipleOfFive = value % 5 == 0
        
        if (isMultipleOfThree && isMultipleOfFive) {
            print(firstString, secondString)
        } else if (isMultipleOfThree) {
            print(firstString)
        } else if (isMultipleOfFive) {
            print(secondString)
        } else {
            totalNumberPrinted += 1
        }
    }
    
    return totalNumberPrinted
}

let totalNumberPrinted = extraExercise(firstString: "% 3", secondString: "% 5")

print("Original numbers was printed: \(totalNumberPrinted) times")
