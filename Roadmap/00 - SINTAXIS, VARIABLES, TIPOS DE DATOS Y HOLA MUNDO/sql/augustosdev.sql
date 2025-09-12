-- https://www.sql.org/

-- Comentario en una linea 

/* Comentario en
varias lineas 
*/

DECLARE @my_var VARCHAR(50);
SET @my_var = 'Esta es la variable';

-- Datos Primitivos
DECLARE @type_numeric INTEGER;
SET @type_numeric = 14;
DECLARE @type_real REAL;
SET @type_real = 10.5;
DECLARE @type_char CHAR;
SET @type_char = 'sinEspacios';
DECLARE @type_varchar VARCHAR;
SET @type_varchar = 'Con espacios';
DECLARE @type_boolean BOOLEAN;
SET @type_boolean = true;
DECLARE @type_date DATE;
SET @type_date = '2024-04-21';
DECLARE @type_time TIME;
SET @type_time = '21:54:12';
DECLARE @type_timestamp TIMESTAMP;
SET @type_char = '2024-04-21 21:55:15';

PRINT "Hola, SQL";

