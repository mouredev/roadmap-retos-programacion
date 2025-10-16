-- EJERCICIO:
-- - Crea un comentario en el código y coloca la URL del sitio web oficial del lenguaje de programación que has seleccionado.
--   No hay un único sitio web oficial para SQL, ya que es un estándar, pero un buen recurso es: https://www.iso.org/standard/63555.html

-- - Representa las diferentes sintaxis que existen de crear comentarios en el lenguaje (en una línea, varias...).

-- Esto es un comentario de una línea

/*
Esto es un comentario
de varias líneas.
*/

-- - Crea una variable (y una constante si el lenguaje lo soporta).
-- La sintaxis para variables depende del dialecto de SQL (T-SQL, PL/SQL, etc.).
-- Ejemplo en T-SQL (SQL Server):
DECLARE @my_variable VARCHAR(20) = 'Mi variable';

-- SQL no tiene un concepto de constante como otros lenguajes, pero se puede usar un valor literal.

-- - Crea variables representando todos los tipos de datos primitivos del lenguaje (cadenas de texto, enteros, booleanos...).
-- En SQL, más que variables, se definen columnas en tablas con tipos de datos.
-- Ejemplo de creación de una tabla para mostrar los tipos:
/*
CREATE TABLE TiposDeDatos (
    columna_varchar VARCHAR(255), -- Cadena de texto
    columna_int INT,             -- Entero
    columna_decimal DECIMAL(10, 2),-- Decimal
    columna_boolean BOOLEAN,       -- Booleano (la disponibilidad varía)
    columna_date DATE            -- Fecha
);
*/

-- - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
-- La forma estándar de devolver un valor o "imprimir" es con una sentencia SELECT.
SELECT '¡Hola, SQL!';
