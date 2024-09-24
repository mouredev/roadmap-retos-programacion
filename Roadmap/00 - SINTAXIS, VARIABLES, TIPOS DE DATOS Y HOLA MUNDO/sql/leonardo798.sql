
-- 1. Documentación oficial en  https://www.iso.org/standard/76583.html
-- Documentación complementaria en https://www.w3schools.com/sql/ se divide por cada gestor de base de datos y por ejemplos.

-- 2. Tipos de comentarios.

-- Comentario de una línea en SQL

/*
Comentario de varias líneas
en SQL
*/

-- 3. Vairables y Constantes segun lenguaje
-- En SQL Nativo no existe una forma de declarar variables ni constantes, por lo cual depende del SGBD (sistema gestor de base de datos)


-- SQL Server
-- Declarar una variable
DECLARE @variable VARCHAR(50);
-- Asignar un valor a una variable
SET @variable = 'SQL Server'; 
-- Todo junto
DECLARE @otraVariable INT = 20;


-- Oracle
DECLARE
  mi_variable NUMBER;
BEGIN
  mi_variable := 10;
END;


-- MySQL
SET @miVariable = 10;


-- 4. Tipos de datos primitivos.
-- Tipos numéricos:

DECLARE @variable INTEGER(10);          -- Números enteros.
DECLARE @variable2 INT;                 -- Números enteros.
DECLARE @variable3 SMALLINT;            -- Enteros pequeños.
DECLARE @variable4 BIGINT;              -- Enteros grandes.
DECLARE @variable5 DECIMAL(10,2);       -- Números decimales de precisión fija.
DECLARE @variable6 FLOAT(10);           -- Números de punto flotante.
DECLARE @variable7 REAL;                -- Números de punto flotante de precisión simple.
DECLARE @variable8 DOUBLE PRECISION;    -- Números de punto flotante de doble precisión.

-- Tipos de caracteres:

DECLARE @variable9 CHAR(10);            -- Cadena de caracteres de longitud fija. Ocupa la misma cantidad de espacio en disco.
DECLARE @variable10 VARCHAR(10);        -- Cadena de caracteres de longitud variable. Ocupa solo el espacio usado por la cantidad de caractres.
DECLARE @variable11 CHARACTER VARYING(10); -- Cadena de caracteres de longitud variable. Equivalente a VARCHAR se diferencia solo por el nombre segun estandar ANSI SQL

-- Tipos de fecha y hora:

DECLARE @variable12 DATE;               -- Fecha (año, mes, día).
DECLARE @variable13 TIME;               -- Hora (hora, minuto, segundo).
DECLARE @variable14 TIMESTAMP;          -- Combinación de fecha y hora.
DECLARE @variable15 INTERVAL;           -- Representa un intervalo de tiempo.

-- Tipos booleanos:

DECLARE @variable16 BOOLEAN;            -- Valor booleano. Puede almacenar TRUE, FALSE o NULL.

-- Tipos binarios:

DECLARE @variable17 BINARY(10);         -- Datos binarios de longitud fija.
DECLARE @variable18 VARBINARY(10);      -- Datos binarios de longitud variable.

-- Otros tipos:

DECLARE @variable19 CLOB;              -- Caracteres grandes.
DECLARE @variable20 BLOB;              -- Binarios grandes.


-- 5. Imprimir en consola.

PRINT '¡Hola, ' + @variable + '!';

