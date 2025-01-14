-- Comentario de una línea
-- Sitio oficial: https://www.haskell.org/

{- 
   Comentario de varias líneas

   Documentación oficial: https://www.haskell.org/documentation/
-}

-- Las variables en Haskell son inmutables

i :: Integer  -- Enteros
i = 1

d :: Double   -- Real de Punto Flotante de doble precision
d = 1.0

fl :: Float   -- Real Punto Flotante de simple precisión
fl = 1.0

c :: Char     -- Caracter
c = 'a'

s :: String   -- Cadena
s = "Haskell"

t :: Bool     -- Booleanos
t = True      -- Verdadero

f :: Bool
f = False     -- Falso

o :: Integer
o = 0o10      -- 8 en notación octal

h :: Integer
h = 0x10      -- 16 en hexadecimal

b :: Integer
b = 0b1111    -- 15 en binario

u :: ()       -- Tipo de la expresión (), llamada unit
u = ()

main :: IO () -- Tipo de una expresión que representa una subrutina de IO que retorna ()
main = putStrLn "¡Hola, Haskell!"
