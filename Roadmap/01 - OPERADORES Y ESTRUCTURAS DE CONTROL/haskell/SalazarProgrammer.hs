{-
  EJERCICIO:
  - Operadores: Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
  - Estructuras de control: Condicionales, iterativas, excepciones...
  - Debes hacer print por consola del resultado de todos los ejemplos.
-}

module Main where

-- Operadores Aritméticos
operadoresAritmeticos :: IO ()
operadoresAritmeticos = do
    putStrLn "\n--- OPERADORES ARITMÉTICOS ---"
    putStrLn $ "5 + 3 = " ++ show (5 + 3)      -- Suma: 8
    putStrLn $ "5 - 3 = " ++ show (5 - 3)      -- Resta: 2
    putStrLn $ "5 * 3 = " ++ show (5 * 3)      -- Multiplicación: 15
    putStrLn $ "10 / 3 = " ++ show (10 / 3)    -- División: 3.333...
    putStrLn $ "10 `div` 3 = " ++ show (10 `div` 3)  -- División entera: 3
    putStrLn $ "10 `mod` 3 = " ++ show (10 `mod` 3)  -- Módulo: 1
    putStrLn $ "2 ^ 3 = " ++ show (2 ^ 3)      -- Potencia: 8

-- Operadores de Comparación
operadoresComparacion :: IO ()
operadoresComparacion = do
    putStrLn "\n--- OPERADORES DE COMPARACIÓN ---"
    putStrLn $ "5 == 3 = " ++ show (5 == 3)    -- Igualdad: False
    putStrLn $ "5 /= 3 = " ++ show (5 /= 3)    -- Desigualdad: True
    putStrLn $ "5 > 3 = " ++ show (5 > 3)      -- Mayor que: True
    putStrLn $ "5 < 3 = " ++ show (5 < 3)      -- Menor que: False
    putStrLn $ "5 >= 5 = " ++ show (5 >= 5)    -- Mayor o igual: True
    putStrLn $ "5 <= 3 = " ++ show (5 <= 3)    -- Menor o igual: False

-- Operadores Lógicos
operadoresLogicos :: IO ()
operadoresLogicos = do
    putStrLn "\n--- OPERADORES LÓGICOS ---"
    putStrLn $ "True && False = " ++ show (True && False)  -- AND: False
    putStrLn $ "True || False = " ++ show (True || False)  -- OR: True
    putStrLn $ "not True = " ++ show (not True)            -- NOT: False

-- Operadores a Nivel de Bits
operadoresBits :: IO ()
operadoresBits = do
    putStrLn "\n--- OPERADORES A NIVEL DE BITS ---"
    putStrLn $ "5 .&. 3 = " ++ show (5 .&. 3)  -- AND bit a bit: 1
    putStrLn $ "5 .|. 3 = " ++ show (5 .|. 3)  -- OR bit a bit: 7
    putStrLn $ "5 `xor` 3 = " ++ show (5 `xor` 3)  -- XOR: 6
    putStrLn $ "complement (5 :: Int) = " ++ show (complement (5 :: Int))  -- Complemento: -6

-- En Haskell no hay operadores de asignación como en lenguajes imperativos
-- Las variables son inmutables por defecto

-- Estructuras de Control Condicionales
estructurasCondicionales :: IO ()
estructurasCondicionales = do
    putStrLn "\n--- ESTRUCTURAS CONDICIONALES ---"

    -- If-Then-Else
    let resultado1 = if 5 > 3 then "Mayor" else "Menor"
    putStrLn $ "If-Then-Else: " ++ resultado1

    -- Guardas (Guards)
    let clasificar x
            | x > 10   = "Grande"
            | x > 5    = "Mediano"
            | otherwise = "Pequeño"
    putStrLn $ "Guardas (7): " ++ clasificar 7

    -- Pattern Matching
    let factorial 0 = 1
        factorial n = n * factorial (n - 1)
    putStrLn $ "Pattern Matching (factorial 5): " ++ show (factorial 5)

-- Estructuras Iterativas (Haskell usa recursión en lugar de bucles)
estructurasIterativas :: IO ()
estructurasIterativas = do
    putStrLn "\n--- ESTRUCTURAS ITERATIVAS ---"

    -- Recursión
    let sumaLista [] = 0
        sumaLista (x:xs) = x + sumaLista xs
    putStrLn $ "Recursión (suma [1,2,3,4]): " ++ show (sumaLista [1,2,3,4])

    -- Map (transformación)
    let duplicar = map (*2)
    putStrLn $ "Map (duplicar [1,2,3]): " ++ show (duplicar [1,2,3])

    -- Filter (filtrado)
    let pares = filter even
    putStrLn $ "Filter (pares [1,2,3,4,5]): " ++ show (pares [1,2,3,4,5])

    -- Fold (acumulación)
    let producto = foldl (*) 1
    putStrLn $ "Fold (producto [1,2,3,4]): " ++ show (producto [1,2,3,4])

-- Manejo de Excepciones
estructurasExcepciones :: IO ()
estructurasExcepciones = do
    putStrLn "\n--- MANEJO DE EXCEPCIONES ---"

    -- Usando Maybe
    let divisionSegura _ 0 = Nothing
        divisionSegura a b = Just (a / b)

    case divisionSegura 10 2 of
        Just resultado -> putStrLn $ "División segura (10/2): " ++ show resultado
        Nothing -> putStrLn "Error: división por cero"

    case divisionSegura 10 0 of
        Just resultado -> putStrLn $ "División segura: " ++ show resultado
        Nothing -> putStrLn "Error: división por cero (manejado con Maybe)"

{-
  DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
-}

-- DIFICULTAD EXTRA
dificultadExtra :: IO ()
dificultadExtra = do
    putStrLn "\n--- DIFICULTAD EXTRA ---"
    putStrLn "Números entre 10 y 55 (pares, no 16, no múltiplos de 3):"

    let numeros = [x | x <- [10..55], even x, x /= 16, x `mod` 3 /= 0]
    mapM_ (putStrLn . show) numeros
    putStrLn $ "Total: " ++ show (length numeros) ++ " números"

-- Función principal
main :: IO ()
main = do
    operadoresAritmeticos
    operadoresComparacion
    operadoresLogicos
    operadoresBits
    estructurasCondicionales
    estructurasIterativas
    estructurasExcepciones
    dificultadExtra

-- FIN
