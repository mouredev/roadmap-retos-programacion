// Función sin parámetros ni retornos.
func saludar() {
    print("Hola, soy una función sin parámetros ni retornos!")
}

saludar()

// Función con varios parámetros.
func variosParametros(nombre: String, happy: Bool) {

    if happy {
        var pais = "México" // Variable Local
        print("Hola \(nombre) feliz que vive en \(pais).")
    } else {
        print("Adios \(nombre).")
    }
}

variosParametros(nombre: "karys", happy: true)

// Función con parámetro y retorno.
func diaFavorito(dia: String) -> String {

    switch dia {
    case "Viernes":
    return "Casi se acerca el fin de semana"
    case "Sábado":
    return "El mejor día del fin de semana"
    case "Domingo":
    return "Día completo para descansar"    
    default:
    return "No es un día válido"
     }  
}

diaFavorito(dia: "Sábado")


/*DIFICULTAD EXTRA (opcional):
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

 func imprimirNumeros(cadena1: String, cadena2: String) -> Int {
   
    var contador = 0 // Variable Global
    for numero in 1...100 {
        if (numero % 3 == 0) && (numero % 5 == 0) {
            print("El número \(numero) es \(cadena1) y es \(cadena2)")  
            contador += 1
            
        } else if numero % 3 == 0 {
            print("El número \(numero) es \(cadena1)")
            contador += 1
            
        } else if numero % 5 == 0 {
             print("El número \(numero) es \(cadena2)")
             contador += 1 
        }
    } 
    print("Se imprimieron \(contador) números.") 
    return contador
 }

imprimirNumeros(cadena1: "múltiplo de 3",cadena2: "múltiplo de 5")
