-- OPERADORES

-- Aritmeticos
SELECT 5 + 3 AS suma;
SELECT 5 - 3 AS resta;
SELECT 5 * 3 AS multiplicacion;
SELECT 9 / 3 AS divison; 
SELECT 10 % 3 AS modulo;

--COMPARACION
SELECT CASE WHEN 5 > 3 THEN 'Verdadero' ELSE 'Falso' END AS mayor;
SELECT CASE WHEN 5 = 3 THEN 'Verdadero' ELSE 'Falso' END AS igual;
SELECT CASE WHEN 5 != 3 THEN 'Verdadero' ELSE 'Falso' END AS diferente;
SELECT CASE WHEN 5 < 3 THEN 'Verdadero' ELSE 'Falso' END AS menor;
SELECT CASE WHEN 5 <= 3 THEN 'Verdadero' ELSE 'Falso' END AS menor_igual;
SELECT CASE WHEN 5 >= 3 THEN 'Verdadero' ELSE 'Falso' END AS mayor_igual;

--LOGICOS
SELECT CASE WHEN 5 > 3 AND 5 < 10 THEN 'Verdadero' ELSE 'Falso' END AS logico_and;
SELECT CASE WHEN 5 > 3 OR 5 < 10 THEN 'Verdadero' ELSE 'Falso' END AS logico_or;
SELECT CASE WHEN NOT (5 BETWEEN 1 AND 10) THEN 'Fuera de rango' ELSE 'Dentro de rango' END AS resultado;

--OPERADORES DE CONCATENACION
SELECT CONCAT('Hola', ' ', 'mundo') AS concatenacion;

--OPERADORES DE ASIGNACION
DECLARE @mi_variable VARCHAR(50);
SET @mi_variable = 'El igual(=) asigna valor a la variable';

--OPERADORES DE RANGO
SELECT CASE WHEN 5 BETWEEN 1 AND 10 THEN 'Dentro de rango' ELSE 'Fuera de rango' END AS rango;
SELECT CASE WHEN 5 NOT BETWEEN 1 AND 10 THEN 'Dentro de rango' ELSE 'Fuera de rango' END AS rango;

--OPERADORES DE EXISTENCIA
SELECT CASE WHEN EXISTS (SELECT * FROM tabla WHERE columna = 'valor') THEN 'Existe' ELSE 'No existe' END AS existencia;
