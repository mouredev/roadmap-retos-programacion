-- URL oficial del lenguaje de programación Haskell: https://www.haskell.org/

-- Esto es un comentario de una sola línea en Haskell

{-
   Esto es un comentario
   de varias líneas en Haskell
-}

{-
 Crear una variable (en Haskell, las variables son inmutables por defecto)
 Aunque la declaratividad no es obligatoria es muy aconsejable
-}
numero :: Int --Esta es la declaratividad
numero = 42

-- Crear una constante (en Haskell todas las variables son básicamente constantes)
piConstante :: Double
piConstante = 3.1416

-- Crear variables representando diferentes tipos de datos primitivos
nombre :: String  -- Cadena de texto
nombre = "Haskell"

verdadero :: Bool  -- Booleano
verdadero = True

entero :: Int  -- Entero
entero = 10

flotante :: Float  -- Número de punto flotante
flotante = 10.5

main :: IO ()
main = putStrLn ("¡Hola, " ++ nombre ++ "!")
