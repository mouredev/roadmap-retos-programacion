// Sitio oficial: https://fsharp.org/
// F# Basics: https://dotnet.microsoft.com/es-es/languages/fsharp
// http://learn.microsoft.com/dotnet/fsharp

// Variables en F#
// Después de asignar un valor, no se puede cambiar, es inmutable
// Para hacer que sea mutable se emplea la palabra reservada mutable
// Con inferencia de tipos
let nombre_variable = "Valor"   // variable string
let entero = 5                     // variable int
let float = 1.0                  // variable float
let char = 'a'                    // variable char
let booleano = true               // variable bool - true o false

// Con tipos
let cadena : string = "Hola"
let entero2 : int = 10
let float2 : float = 5.0e2
let double : double = 20.0
let char2 : char = '@'
let booleano2 : bool = false

// variables mutables
let mutable name = "Chris"
name <- "Luis" 

let fsharp = "F#"

printfn $"¡Hola, {fsharp}!"   // Imprime la cadena en stdout y agrega un caracter de nueva línea
