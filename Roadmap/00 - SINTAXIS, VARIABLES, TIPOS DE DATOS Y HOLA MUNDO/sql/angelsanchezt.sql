-- URL del sitio web oficial de SQL: https://www.sql.org/
-- https://www.iso.org/standard/76583.html

/*
 También el SQL a veces se describe como un lenguaje declarativo, también incluye elementos procesales.
*/

-- Este es un comentario de una sola línea en SQL.

/* 
    Este es un comentario
    que puede ocupar múltiples líneas en SQL. 
*/


-- Variables
DECLARE @mi_variable INT;
SET @mi_variable = 42;

-- Constantes (No todos los sistemas de base de datos admiten constantes)
DECLARE @mi_constante INT;
SET @mi_constante = 100;

-- Tipos de Datos Primitivos:
DECLARE @entero INT;
DECLARE @decimal DECIMAL(10, 2);
DECLARE @cadena VARCHAR(50);
DECLARE @fecha DATE;
DECLARE @booleano BIT;

-- Impresión por Terminal:
DECLARE @saludo NVARCHAR(50);
SET @saludo = '¡Hola, SQL!';
PRINT @saludo;

