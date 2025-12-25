{-
  EJERCICIO:
  - Funciones básicas: sin parámetros, con parámetros, con retorno
  - Funciones dentro de funciones
  - Funciones ya creadas en el lenguaje
  - Variables LOCAL y GLOBAL
-}

module Main where

-- Variable GLOBAL (a nivel de módulo)
variableGlobal :: String
variableGlobal = "Soy una variable global"

-- 1. Función sin parámetros ni retorno (en Haskell, retorna IO ())
funcionSinParametros :: IO ()
funcionSinParametros = putStrLn "¡Hola desde función sin parámetros!"

-- 2. Función con un parámetro y sin retorno explícito
funcionUnParametro :: String -> IO ()
funcionUnParametro nombre = putStrLn ("Hola, " ++ nombre ++ "!")

-- 3. Función con varios parámetros y retorno
funcionVariosParametros :: Int -> Int -> Int
funcionVariosParametros a b = a + b

-- 4. Función con retorno explícito
funcionConRetorno :: Float -> Float -> Float
funcionConRetorno x y = x * y

-- 5. Función dentro de función (usando where)
funcionExterna :: Int -> Int
funcionExterna x = funcionInterna x * 2
    where
        funcionInterna :: Int -> Int
        funcionInterna y = y + 5

-- 6. Función dentro de función (usando let)
funcionConLet :: Int -> Int
funcionConLet x =
    let funcionInterna y = y * 3
    in funcionInterna x + 1

-- 7. Uso de funciones ya creadas en Haskell
usoFuncionesNativas :: IO ()
usoFuncionesNativas = do
    putStrLn $ "Longitud de 'Haskell': " ++ show (length "Haskell")
    putStrLn $ "Reverse de 'Haskell': " ++ reverse "Haskell"
    putStrLn $ "Máximo de [1,5,3,2]: " ++ show (maximum [1,5,3,2])
    putStrLn $ "Suma de [1..5]: " ++ show (sum [1..5])

-- 8. Prueba de variables LOCALES y GLOBALES
pruebaAlcanceVariables :: IO ()
pruebaAlcanceVariables = do
    putStrLn $ "Variable global: " ++ variableGlobal

    -- Variable LOCAL dentro de la función
    let variableLocal = "Soy una variable local"
    putStrLn $ "Variable local: " ++ variableLocal

    -- Función con variable local interna
    let funcionConVariableLocal x =
            let variableInterna = x * 2
            in variableInterna + 1

    putStrLn $ "Función con variable local (5): " ++ show (funcionConVariableLocal 5)

-- DIFICULTAD EXTRA
dificultadExtra :: String -> String -> Int
dificultadExtra texto1 texto2 = contador
  where
    -- Función auxiliar para procesar cada número
    procesarNumero n
        | n `mod` 15 == 0 = putStrLn (texto1 ++ texto2) >> return False
        | n `mod` 3 == 0  = putStrLn texto1 >> return False
        | n `mod` 5 == 0  = putStrLn texto2 >> return False
        | otherwise       = putStrLn (show n) >> return True

    -- Lista de resultados (True si se imprimió el número)
    resultados = map procesarNumero [1..100]

    -- Contar cuántas veces se imprimió el número (True)
    contador = length (filter id resultados)

-- Versión alternativa más funcional de la dificultad extra
dificultadExtraFuncional :: String -> String -> Int
dificultadExtraFuncional texto1 texto2 = length numerosImpresos
  where
    numerosImpresos = [n | n <- [1..100], imprimirNumero n]

    imprimirNumero n
        | n `mod` 15 == 0 = putStrLn (texto1 ++ texto2) False
        | n `mod` 3 == 0  = putStrLn texto1 False
        | n `mod` 5 == 0  = putStrLn texto2 False
        | otherwise       = putStrLn (show n) True

-- Función auxiliar para imprimir y retornar valor
putStrLn :: String -> Bool -> Bool
putStrLn mensaje retorno = do
    Prelude.putStrLn mensaje
    return retorno

-- Función principal
main :: IO ()
main = do
    putStrLn "=== FUNCIONES BÁSICAS ==="
    funcionSinParametros
    funcionUnParametro "Mundo"
    putStrLn $ "Función con varios parámetros (3 + 4): " ++ show (funcionVariosParametros 3 4)
    putStrLn $ "Función con retorno (2.5 * 3.0): " ++ show (funcionConRetorno 2.5 3.0)

    putStrLn "\n=== FUNCIONES DENTRO DE FUNCIONES ==="
    putStrLn $ "Función externa (5): " ++ show (funcionExterna 5)
    putStrLn $ "Función con let (4): " ++ show (funcionConLet 4)

    putStrLn "\n=== FUNCIONES NATIVAS DE HASKELL ==="
    usoFuncionesNativas

    putStrLn "\n=== ALCANCE DE VARIABLES ==="
    pruebaAlcanceVariables

    putStrLn "\n=== DIFICULTAD EXTRA ==="
    putStrLn "Ejecutando dificultadExtra con 'Fizz' y 'Buzz':"
    resultado <- return (dificultadExtra "Fizz" "Buzz")
    putStrLn $ "\nNúmeros impresos (no reemplazados): " ++ show resultado

    putStrLn "\nEjecutando versión funcional:"
    resultado2 <- return (dificultadExtraFuncional "Fizz" "Buzz")
    putStrLn $ "Números impresos: " ++ show resultado2

-- Fin del programa