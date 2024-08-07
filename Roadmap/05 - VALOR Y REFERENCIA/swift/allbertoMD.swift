import Foundation


class Word {
    var word: String

    init(word: String) {
        self.word = word
    }

}


// Variables por valor
print("\nVARIABLES POR VALOR")

print("\nAsignación del String \"Hola\" a la Variable valueVariable1")
// Asigna el string "Hola" a la variable valueVariable1
var valueVariable1: String = "Hola"
// Imprime el valor de la variable valueVariable1
print(valueVariable1)

print("\nAsignación del valor de la variaable valueVariable1 a valueVariable2")
// Asigna el valor de la variable valueVariable1 a valueVariable2
var valueVariable2: String = valueVariable1
// Imprime el valor de la varible valueVariable2
print(valueVariable2)

print("\nCambio Del Valor de la Variable valueVariable1 al String \"Adios\"")
// Cambia el valor de la variable valueVariable1 al String "Adios"
valueVariable1 = "Adios"
print("El Valor de la Variable valueVariable1 Cambia a \"Adios\"")
// Imprime la variable valueVariable1 
print(valueVariable1)

print("\nEl Valor de la Variable valueVariable2 no Cambia Por Que es una Varaable Por Valor")
// Imprime la variable valueVariable2
print(valueVariable2)

// Función variable por valor
func modifiesValueVariable(value str: String) -> String {
    str + ", Mundo"
}

print("\nAsignación Del Retorno de la Función a la Variable valueVariable3")
// Asigna el retorno de la función a la variable valueVariable3
var valueVariable3 = modifiesValueVariable(value: "Hola")
// Imprime el valor de la variable valueVariable1
print(valueVariable3)

print("\nAsignación Del Valor de la Variable valueVariable3 a valueVariable4")
// Asigna el valor de la variable valueVariable1 a valueVariable4
var valueVariable4 = valueVariable3
// Imprime el valor de la variable valueVariable4
print(valueVariable4)

print("\nCambiao Del Valor Del Parametro de la Función y Asignación Del Retorno a la Variable valueVariable3")
// Cambia el valor del valor parametro de la función y asigna el retorno a la variable valueVariable3
valueVariable3 = modifiesValueVariable(value: "Adios")
print("El Valor de la Variable valueVariable3 Cambia a \"Adios, Mundo\"")
// Imprime la variable valueVariable1
print(valueVariable3)

print("\nEl Valor de la Variable valueVariable4 no Cambia Por Que es Una Variable Por Valor")
// Imprime la variable valueVariable4
print(valueVariable4)


// VARIABLES POR REFERENCIA
print("\n\nVARIABLES POR REFERENCIA")

print("\nInstancia de la Clase Word() en la Variable referenceVariable1, y Asignación Del String \"Hola\" a la Propiedad word")
// Instacia la clase Word() en la variable referenceVariable1, y asigna el valor del String "Hola"
var referenceVariable1 = Word(word: "Hola")
// Imprime el valor de la propiedas word de la variable referenceVariable1
print(referenceVariable1.word)

print("\nCopia de la Instancia de Word() de la variable refeenceVariable1 a referenceVariable2")
// Copia la instancia de la clase Word() de referenceVariable1 a referenceVariable2
var referenceVariable2 = referenceVariable1
// Imprime el valor de la variable referenceVariable2
print(referenceVariable2.word)

print("\nCambio Del Valor de la Propiedad word de la Variable referenceVariable1 al String \"Adion\"")
// Cambia el valor de la propiedad word de la variable referenceVariable1 al string "Adios"
referenceVariable2.word = "Adios"
print("El Valor de la Propiedad word de la Variable referenceVariable1 Cambia a \"Adion\"")
// Imprime la variable referenceVariable1
print(referenceVariable1.word)

print("\nEl Valor de la propiedad word de la variable referenceVariable2 Cambia Por Que es Una Variable Por Referencia")
// Imprime la variable referenceVariable2
print(referenceVariable2.word)

// Función variable pro referencia
func modifierReferenceVariable(reference ref: String) -> String {
    "\(ref), Mundo"
}

print("\nInstanciación de la Clase Word() en la Variable referenceVariable3 Usando el Retorno de la Función")
// Instancia la clase Word() en la variable referenceVariable3 usando el retrono de la funcioón
var referenceVariable3 = Word(word: modifierReferenceVariable(reference: "Hola"))
// Imprime el valor de la propiedad word de la variable referenceVariable3
print(referenceVariable3.word)

print("\nCopia de la Instancia de la Clase Word() de la Variable referenceVariable3 a referenceVariable4")
// Copia la instancia de la clase Word() a la variable referenceVariable4
var referenceVariable4 = referenceVariable3
// Imprime el valor de la propiedad word de la variable referenceVariable4
print(referenceVariable4.word)

print("\nCambio Del Valor de la Propiedad word de la Variable referenceVariable3 al String \"Adion\" Usando la Función")
// Cambia el valor de la propiedad word de la variable referenceVariable3 al string "Adios" usando la funcioón
referenceVariable3.word = modifierReferenceVariable(reference: "Adios")
print("El Valor de la Propiedad word de la Variable referenceVariable3 Cambia a \"Adion\"")
// Imprime la variable referenceVariable1
print(referenceVariable3.word)

print("\nEl Valor de la propiedad word de la variable referenceVariable4 Cambia Por Que es Una Variable Por Referencia")
// Imprime la variable referenceVariable4
print(referenceVariable4.word)




// Dificultad Extra
print("\n\nDIFICULTAD EXTRA")


// Programa de intercambio de variables por valor
print("\nPrograma de Intercambio de Variables Por Valor")

// Declara variable con el String "España"
var value1 = "España"
// Declara variable con el String "Portugla"
var value2 = "Portugal"

// Define la funcion que intercabiara las variable value1 por value2 y value2 por value1
func exchangeValue(value1 val1: String, value2 val2: String) -> (String, String) {
    let v1 = val2
    let v2 = val1

    return (v1, v2)
}

// Declara una variable con una tupla y le asigna el retorno de la tupla de la funcion
var (newValue1, newValue2) = exchangeValue(value1: value1, value2: value2)
print("\nEl Valor Del String \"España\" Ahora es \"Portugal\"")
// Imprime el valor de value2 en lugar de value1
print(newValue1)
print("El Valor Del String \"Portugal\" Ahora es \"España\"")
// Imprime el valor de value1 en lugar de value2
print(newValue2)
print("\nEl Valor Del String \"España\" no ha Cambiado")
// Imprime el valor original sin cambiar
print(value1)
print("El Valor Del String \"Portugal\" no ha Cambiado")
// Imprime el valor original sin cambiar
print(value2)


// Progama de intercabio de variables pro referencia
print("\nPrograma de Intercambio de Variables Por Referencia")

// Instancia de la clase Word() y asigna el String "Alemania" a la propiedad word
var reference1 = Word(word: "Alemania")
// Instancia de la clase Word() y asigna el Sting "Italia" a la propiedad word
var reference2 = Word(word: "Italia")

// Define la funcion que intercabiara las variable reference1 por reference2 y reference2 por referencde1
func exchangeReference(reference1 ref1: Word, reference2 ref2: Word) -> (Word, Word) {
    let r1 = ref2
    let r2 = ref1

    return (r1, r2)
}

// Declara una variable con una tupla y le asigna el retorno de la tupla de la funcion
var (newReference1, newReference2) = exchangeReference(reference1: reference1, reference2: reference2)
print("\nEl Valor Del String \"Alemania\" Ahora es \"Italia\"")
// Imprime el valor de reference2 en lugar de reference1
print(newReference1.word)
print("El Valor Del String \"Italia\" Ahora es \"Alemania\"")
// Imprime el valor de reference1 en lugar de reference2
print(newReference2.word)
print("\nEl Valor Del String \"Alemania\" no ha Cambiado")
// Imprime el valor original sin cambiar
print(reference1.word)
print("El Valor Del String \"Italia\" no ha Cambiado")
// Imprime el valor original sin cambiar
print(reference2.word)
