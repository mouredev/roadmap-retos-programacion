-- Este es un comentario de una línea

{-
  Este es un comentario
  que abarca varias líneas.
-}

{-
  {- Comentario anidado -}
-}

{-
  Sitio oficial: https://elm-lang.org/
-}

{-
  Las variables en Elm son inmutables
  
  nombreVariable : Tipo
  nombreVariable = valor
-}

import Html

pi : Float
pi = 3.141516

nombre : String
nombre = "Elm"

-- Si no se proporciona un tipo Elm infiere el tipo

entero = 5

numeros = [1, 2, 3, 4, 5]  -- Lista
persona = { nombre = "Alice", edad = 30 } -- Registro

main =
  Html.text "¡Hola, Elm!"
