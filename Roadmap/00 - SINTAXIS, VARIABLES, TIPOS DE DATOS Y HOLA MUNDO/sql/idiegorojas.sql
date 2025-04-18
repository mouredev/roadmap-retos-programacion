/*
01 Sintaxis, Variables y Tipos de Datos
*/

-- Crea un comentario en el código y coloca la URL del sitio web oficial del lenguaje de programación que has seleccionado.
-- Representa las diferentes sintaxis que existen de crear comentarios en el lenguaje (en una línea, varias...).
-- Crea una variable (y una constante si el lenguaje lo soporta).
-- Crea variables representando todos los tipos de datos primitivos del lenguaje (cadenas de texto, enteros, booleanos...).
-- Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"

-- El lenguaje de programación seleccionado es SQL.
-- URL de uno de los sitios web oficiales: https://www.oracle.com/database/technologies/appdev/sql.html

-- Comentario de una linea

/* 
Comentario de varias lineas
*/

-- Declaración de una variable
DECLARE @variable_name datatype;
SET @variable_name = value;

-- Declaración de una constante
DECLARE @constant_name datatype;
SET @constant_name = value;

-- Ejemplo:
DECLARE @totalSales INT;
SET @totalSales = (SELECT SUM(sales) FROM sales_table);


/*
Tipos de datos
*/

-- Tipos de datos numéricos:
-- INT: Enteros.
-- SMALLINT: Enteros pequeños.
-- BIGINT: Enteros grandes.
-- FLOAT: Números de punto flotante.
-- REAL: Números de punto flotante de precisión simple.
-- DECIMAL: Números decimales con una precisión específica.
-- NUMERIC: Similar a DECIMAL, pero conforme al estándar SQL.

-- Tipos de datos de caracteres:
-- CHAR(n): Cadena de caracteres de longitud fija.
-- VARCHAR(n): Cadena de caracteres de longitud variable.
-- TEXT: Cadena de caracteres de longitud variable, usada para texto largo.

-- Tipos de datos de fecha y hora:
-- DATE: Fecha (año, mes y día).
-- TIME: Hora (hora, minuto y segundo).
-- DATETIME: Combinación de fecha y hora.
-- TIMESTAMP: Marca de tiempo.
-- YEAR: Año.

-- Tipos de datos binarios:
-- BINARY: Datos binarios de longitud fija.
-- VARBINARY: Datos binarios de longitud variable.
-- BLOB: Objeto binario grande, usado para almacenar datos binarios como imágenes o archivos.

-- Tipos de datos booleanos:
-- BOOLEAN: Valores de verdadero o falso.

CREATE TABLE example_table(
    id INT,
    name VARCHAR(50),
    birthdate DATE,
    salary FLOAT
);

-- Hola SQL
PRINT "¡Hola, SQL!";