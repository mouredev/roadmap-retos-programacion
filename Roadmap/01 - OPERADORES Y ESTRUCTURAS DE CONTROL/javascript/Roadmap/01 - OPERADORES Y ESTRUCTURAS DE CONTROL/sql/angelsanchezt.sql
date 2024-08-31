/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
*/
-- Aritméticos
DECLARE @a INT = 10, @b INT = 5;

PRINT @a + @b;  -- Suma
PRINT @a - @b;  -- Resta
PRINT @a * @b;  -- Multiplicación
PRINT @a / @b;  -- División

PRINT 'Suma: ' + CAST(@a + @b AS VARCHAR(10));
PRINT 'Resta: ' + CAST(@a - @b AS VARCHAR(10));
PRINT 'Multiplicación: ' + CAST(@a * @b AS VARCHAR(10));
PRINT 'División: ' + CAST(@a / @b AS VARCHAR(10));

-- Lógicos
DECLARE @x BIT = 1, @y BIT = 0;
PRINT @x AND @y;  -- AND lógico
PRINT @x OR @y;   -- OR lógico
PRINT NOT @x;     -- NOT lógico

PRINT 'AND lógico: ' + CAST(@x AND @y AS VARCHAR(5));
PRINT 'OR lógico: ' + CAST(@x OR @y AS VARCHAR(5));
PRINT 'NOT lógico: ' + CAST(NOT @x AS VARCHAR(5));

-- De comparación
PRINT @a = @b;    -- Igual a
PRINT @a <> @b;   -- Diferente de
PRINT @a > @b;    -- Mayor que
PRINT @a < @b;    -- Menor que
PRINT @a >= @b;   -- Mayor o igual a
PRINT @a <= @b;   -- Menor o igual a

PRINT 'Igual a: ' + CAST(@a = @b AS VARCHAR(5));
PRINT 'Diferente de: ' + CAST(@a <> @b AS VARCHAR(5));
PRINT 'Mayor que: ' + CAST(@a > @b AS VARCHAR(5));
PRINT 'Menor que: ' + CAST(@a < @b AS VARCHAR(5));
PRINT 'Mayor o igual a: ' + CAST(@a >= @b AS VARCHAR(5));
PRINT 'Menor o igual a: ' + CAST(@a <= @b AS VARCHAR(5));


-- De asignación
DECLARE @resultado INT;
SET @resultado = @a + @b;
PRINT 'Resultado de asignación: ' + CAST(@resultado AS VARCHAR(10));


-- Pertenencia
DECLARE @frutas TABLE (fruta VARCHAR(50));
INSERT INTO @frutas VALUES ('Manzana'), ('Banana'), ('Naranja');
PRINT 'Banana' IN (SELECT fruta FROM @frutas);

-- Bits
DECLARE @bit1 INT = 5, @bit2 INT = 3;
PRINT @bit1 & @bit2;  -- AND a nivel de bits
PRINT @bit1 | @bit2;  -- OR a nivel de bits
PRINT ~@bit1;         -- NOT a nivel de bits

PRINT 'AND a nivel de bits: ' + CAST(@bit1 & @bit2 AS VARCHAR(10));
PRINT 'OR a nivel de bits: ' + CAST(@bit1 | @bit2 AS VARCHAR(10));
PRINT 'NOT a nivel de bits: ' + CAST(~@bit1 AS VARCHAR(10));



-- Ejemplos de Estructuras de Control
DECLARE @edad INT = 18;
DECLARE @mensaje VARCHAR(50);

SET @mensaje = CASE
                WHEN @edad < 18 THEN 'Menor de edad'
                WHEN @edad >= 18 AND @edad < 65 THEN 'Adulto'
                ELSE 'Adulto mayor'
               END;

PRINT 'Mensaje condicional: ' + @mensaje;

DECLARE @contador INT = 1;

WHILE @contador <= 5
BEGIN
    PRINT 'Iteración: ' + CAST(@contador AS VARCHAR(10));
    SET @contador = @contador + 1;
END;


-- MANEJO de EXCEPCIONES
BEGIN TRY
    -- Intenta ejecutar una operación que podría generar un error
    DECLARE @division INT = 10 / 0;
END TRY
BEGIN CATCH
    -- Maneja la excepción
    PRINT 'Error: División por cero';
END CATCH;

-- Programa que Imprime Números Específicos
DECLARE @numero INT = 10;

WHILE @numero <= 55
BEGIN
    IF @numero % 2 = 0 AND @numero != 16 AND @numero % 3 != 0
        PRINT 'Número especial: ' + CAST(@numero AS VARCHAR(10));
    
    SET @numero = @numero + 1;
END;
