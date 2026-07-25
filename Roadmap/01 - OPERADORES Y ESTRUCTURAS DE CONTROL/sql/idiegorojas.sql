/* 
01 - Operadores y estructuras de control 
*/


/* Operadores aritmeticos */
-- Se usan para realizar cálculos matemáticos sobre columnas numéricas.
-- + (Suma)
-- - (Resta)
-- * (Multiplicación)
-- / (División)
-- % (Módulo, resto de una división)

SELECT precio * 1.10 AS precio_con_iva FROM productos;

-- Operadores de comparacion
-- Se utilizan para comparar valores en condiciones, como en la cláusula WHERE.
-- = (Igual)
-- <> o != (Diferente)
-- < (Menor que)
-- > (Mayor que)
-- <= (Menor o igual que)
-- >= (Mayor o igual que)

SELECT nombre FROM empleados WHERE salario > 3000;

-- Operadores Lógicos
-- Combinan condiciones para filtrar datos.
-- AND (Y lógico: ambas condiciones deben ser ciertas)
-- OR (O lógico: al menos una condición debe ser cierta)
-- NOT (Negación: invierte el resultado de una condición)

SELECT nombre FROM clientes WHERE ciudad = "Madrid" AND edad > 25;

-- Operadores Especiales
-- LIKE: Compara patrones en cadenas (con % para cualquier secuencia y _ para un solo carácter).
WHERE nombre LIKE 'A%' (nombres que empiezan con A).
-- IN: Comprueba si un valor está en una lista.
WHERE id IN (1, 2, 3).
-- BETWEEN: Filtra valores dentro de un rango.
WHERE salario BETWEEN 2000 AND 5000.
-- IS NULL / IS NOT NULL: Verifica si un valor es nulo o no.
WHERE telefono IS NULL.


/* Estrucutras de control */
-- SQL es principalmente un lenguaje declarativo, lo que significa que especificas qué quieres obtener, no cómo hacerlo. 
-- Sin embargo, en algunos sistemas de bases de datos (como PostgreSQL, SQL Server o MySQL), se incorporan extensiones procedurales (como PL/SQL o T-SQL) que incluyen estructuras de control para escribir programas o scripts más complejos. 
-- Estas estructuras permiten manejar lógica condicional, bucles y más.

-- 1. Condicionales: IF y CASE
-- IF: Usado en bloques procedurales (no en SQL estándar puro).
IF (SELECT COUNT(*) FROM empleados) > 10
    PRINT 'Hay más de 10 empleados';
ELSE
    PRINT 'Hay 10 o menos empleados';

-- CASE: Similar a un "switch" o "if-else" en consultas SQL estándar.
SELECT nombre,
       CASE 
           WHEN salario > 5000 THEN 'Alto'
           WHEN salario > 2000 THEN 'Medio'
           ELSE 'Bajo'
       END AS nivel_salario
FROM empleados;

-- 2. Bucles
-- Solo están disponibles en lenguajes procedurales como PL/SQL o T-SQL, no en SQL puro.

-- WHILE: Repite un bloque mientras una condición sea verdadera.
DECLARE @contador INT = 0;
WHILE @contador < 5
BEGIN
    PRINT 'Contador: ' + CAST(@contador AS VARCHAR);
    SET @contador = @contador + 1;
END;

-- FOR / LOOP: Varía según el sistema (por ejemplo, en PL/SQL de Oracle):
FOR i IN 1..5 LOOP
    DBMS_OUTPUT.PUT_LINE('Iteración: ' || i);
END LOOP;

-- 3. Control de Excepciones
-- En lenguajes como PL/SQL, puedes manejar errores.
BEGIN
    INSERT INTO empleados (id, nombre) VALUES (1, 'Juan');
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
        DBMS_OUTPUT.PUT_LINE('Error: ID duplicado');
END;