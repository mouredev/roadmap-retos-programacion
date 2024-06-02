import Foundation

/*
 * EJERCICIO:
 * Utilizando tu lenguaje, explora el concepto de expresiones regulares,
 * creando una que sea capaz de encontrar y extraer todos los números
 * de un texto.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea 3 expresiones regulares (a tu criterio) capaces de:
 * - Validar un email.
 * - Validar un número de teléfono.
 * - Validar una url.
 */

func textExample() {
    let text = """
        La serie Naruto tiene 987 capitulos, con 2 temporadas. La serie fue vista en su
        estrenos por millones de personas en cerca de mas de 50 paises. Cada temporada conto con 456 capitulos con una 
        duracion de 20 minutos cada uno.
    """
    do {
        let serie = try Regex("[0-5]")
    } catch {
        print("Se ha encontrado un error al extraer los numeros \(error.localizedDescription)")
    }
}

let newSerie = textExample()
print(newSerie)

// Extra 
func validEmail(email: String) -> Bool { // Validar Email
    return email.hasSuffix("@gmail.com")
}
let newEmail = validEmail(email: "@yahoo.com")
print(newEmail)

func validNumber(numero: Int) -> Bool { // Validar numero de telefono
    return numero != 50987654
}
let newNumero = validNumber(numero: 564356785678)
print(newNumero)

func validUrl(url: String) -> Bool {
    return url.hasSuffix("www.google.com")
}
let newUrl = validUrl(url: "www.yahoo.com")
print(newUrl)

func validTodo(email: String, numero: Int, url: String) -> Bool { // Validar Todo 
    return validEmail(email: email) && validNumber(numero: numero) && validUrl(url: url)
}
let new = validTodo(email: "@yahoo.com", numero: 65789065, url: "www.yahoo.com")
print(new)






