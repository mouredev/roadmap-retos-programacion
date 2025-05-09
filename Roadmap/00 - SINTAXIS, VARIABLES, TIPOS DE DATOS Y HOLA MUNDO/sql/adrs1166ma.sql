
/*
EJERCICIO:
- Crea un comentario en el código y coloca la URL del sitio web oficial del
  lenguaje de programación que has seleccionado.
- Representa las diferentes sintaxis que existen de crear comentarios
  en el lenguaje (en una línea, varias...).
- Crea una variable (y una constante si el lenguaje lo soporta).
- Crea variables representando todos los tipos de datos primitivos
  del lenguaje (cadenas de texto, enteros, booleanos...).
- Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
*/

/*
🔥 sitio web oficial
https://www.sql.org

sitio web oficial Server
https://learn.microsoft.com/en-us/sql

Documentacion 
https://www.quackit.com/sql_server/sql_server_2017/tutorial/create_a_database_in_sql_server_2017.cfm
*/


-- 🔥 Comentario en una linea 

/*  🔥Comentario en
varias lineas 
*/


-- 🔥 Variables y Tipos de datos 

DECLARE @nombre VARCHAR(50) = 'SQL Server'; -- Variable
DECLARE @entero INT = 10; -- Entero
DECLARE @decimal DECIMAL(10,2) = 99.99; -- Decimal
DECLARE @booleano BIT = 1; -- SQL no tiene booleanos puros, se usara BIT (1 = true, 0 = false)
DECLARE @fecha DATE = '2025-01-29'; -- Fecha
DECLARE @texto NVARCHAR(100) = 'Hola, SQL Server!'; -- Cadena de texto
DECLARE @my_var VARCHAR(50);
SET @my_var = 'Esta es la variable';

DECLARE @fecha DATE; -- variable de tipo DATE
SET @fecha = '2025-01-29'; -- Asignación
PRINT @fecha; -- Imprimirlo

/*

char -- almacenar tipo de datos de ancho fijo.
varchar -- almacena tipo de datos alfanumericos de ancho variable.
text -- almacena tipos de datos texto.
nchar -- almacenar tipo de datos de ancho fijo.
nvarchar -- almacena tipo de datos alfanumericos de ancho variable.
bit -- almacena valores de 1 y 0
int -- almacena valores entre -2,147,483,648 y 2,147,483,647.
bigint -- almacena valores entre -9,223,372,036,854,775, 808 and 9,223,372,036,854, 775, 807
decimal -- almacena valores entre -10^38 + 1 to 10^38-1.
numeric -- almacena valores entre -10^38 + 1 to 10^38-1.
money -- almacena valores entre -9,223,372,036,854,775,808 and 9,223,372,036,854, 775, 807
float -- almacena valores entre -1.79E + 308 to 1.79E + 308.

*/
-- 🔥 Imprimir en la consola:
PRINT '¡Hola, ' + @nombre + '!';
