/* Este es un comentario poderoso

https://www.sql.org

*/

-- Este es otro tipo de comentario mas poderoso que el anterior 


-- Variables y tipos de datos
DECLARE @nombre VARCHAR(50) = 'SQL Server'; -- Variable 
DECLARE @entero INT = 10; -- Entero
DECLARE @decimal DECIMAL(10,2) = 99.99; -- Float
DECLARE @booleanod BIT = 1 
DECLARE @fecha DATE = '2025-02-21'; -- Fecha
DECLARE @texto NVARCHAR(100) = 'Hola, SQL'; -- Cadena de texto
DECLARE @my_var VARCHAR(50);
SET @my_var = 'Esta es una variable';

PRINT  'Hola', @nombre, 'esto se escribio en ', @fecha; -- Imprimirlo