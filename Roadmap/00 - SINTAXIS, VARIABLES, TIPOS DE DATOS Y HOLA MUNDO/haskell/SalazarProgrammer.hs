-- Sitio web oficial de Haskell: https://www.haskell.org/

-- Comentario de una línea con el uso de dos guiones.

{-
  Comentario de varias lineas
  con el uso de llaves y guiones
-}

{-|
  Comentario de varias lineas
  con el uso de llaves,
  guiones y barra
-}

{-|
Variables y constantes: En Haskell, todas las variables son inmutables por defecto (se comportan como constantes)
-}

-- Variable
miVariable :: String
miVariable = "Hola, Haskell!"

-- Constante
miConstante :: Double
miConstante = 1.100

{-
  Tipos de Datos Primitivos:
  - Enteros (Int e Integer): Int - Enteros de 32/64 bits/ Integer - Enteros de precisión arbitraria
  - Números de punto flotante: Float - Números de punto flotante/ Double - Números de doble precisión
  - Booleanos (Bool): (True/False)
  - Caracteres (Char): Caracteres individuales
  - Cadenas de texto (String): equivalente a [Char]
-}

-- Enteros
entero :: Int
entero = 45

integer :: Integer
integer = 1234567890

-- Números de Punto Flotante
flotante :: Float
flotante = 1.10

double :: Double
double = 1.1000

-- Booleanos
verdadero :: Bool
verdadero = True

falso :: Bool
falso = False

-- Caracteres
caracter :: Char
caracter = 'J'

-- Cadenas de Texto (String es sinónimo de [Char])
cadena :: String
cadena = "Haskell es lo mejor"

{-|
  Estructuras de datos:
  - Listas: [a] - colección homogénea de elementos
  - Tuplas: (a, b, c) - colección heterogénea de tamaño fijo
-}

-- Listas de enteros
listaEnteros :: [Int]
listaEnteros = [1, 2, 3, 4, 5, 6]

-- Tuplas
tuplaEnteros :: (Int, String, Bool)
tuplaEnteros = (1, "Haskell", False)

-- Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
main :: IO ()
main = putStrLn "¡Hola, Haskell!"

-- Fin
