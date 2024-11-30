/*
 * Este ejercicio se resuelve en base a SQL Server
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

-- Tipos de operadores en SQL 

-- 1. Operadores Aritméticos

DECLARE @numero1 INT = 10;
DECLARE @numero2 INT = 5;
DECLARE @numero3 INT = 3;

DECLARE @suma INT = @numero1 + @numero2;                     -- Suma
DECLARE @resta INT = @numero1 - @numero2;                    -- Resta
DECLARE @multiplicacion INT = @numero1 * @numero2;           -- Multiplicación
DECLARE @division INT = @numero1 / @numero2;                 -- División entera
DECLARE @producto INT = @numero1 % @numero3;                 -- Resto de la división

PRINT CONCAT('Suma: ', @suma);                               -- Imprime 15
PRINT CONCAT('Resta: ', @resta);                             -- Imprime 5
PRINT CONCAT('Multiplicación: ', @multiplicacion);           -- Imprime 50
PRINT CONCAT('División: ', @division);                       -- Imprime 2           
PRINT CONCAT('Producto: ', @producto);                       -- Imprime 1



-- 2. Operadores de Comparación

DECLARE @igualQue VARCHAR(5) = CASE WHEN @numero1 = @numero2 THEN 'TRUE' ELSE 'FALSE' END;            -- Igual
DECLARE @mayorQue VARCHAR(5) = CASE WHEN @numero1 > @numero2 THEN 'TRUE' ELSE 'FALSE' END;            -- Mayor que
DECLARE @menorQue VARCHAR(5) = CASE WHEN @numero1 < @numero2 THEN 'TRUE' ELSE 'FALSE' END;            -- Menor que
DECLARE @mayorIgual VARCHAR(5) = CASE WHEN @numero1 >= @numero2 THEN 'TRUE' ELSE 'FALSE' END;         -- Mayor o igual que
DECLARE @menorIgual VARCHAR(5) = CASE WHEN @numero1 <= @numero2 THEN 'TRUE' ELSE 'FALSE' END;         -- Menor o igual que
DECLARE @distinto VARCHAR(5) = CASE WHEN @numero1 <> @numero2 THEN 'TRUE' ELSE 'FALSE' END;           -- Distinto

PRINT CONCAT('Igual que: ', @igualQue);                 -- Imprime 0
PRINT CONCAT('Mayor que: ', @mayorQue);                 -- Imprime 1
PRINT CONCAT('Menor que: ', @menorQue);                 -- Imprime 0
PRINT CONCAT('Mayor o igual que: ', @mayorIgual);       -- Imprime 1
PRINT CONCAT('Menor o igual que: ', @menorIgual);       -- Imprime 0
PRINT CONCAT('Distinto: ', @distinto);                  -- Imprime 1



-- 3. Operadores Lógicos

DECLARE @edad INT = 16;
DECLARE @estaAcompanado BIT = 0;

DECLARE @puedeVerPelicula BIT = CASE WHEN @edad >= 18 OR (@edad >= 16 AND @estaAcompanado = 1) THEN 1 ELSE 0 END;
PRINT CONCAT('Puede ver la película: ', @puedeVerPelicula);                                                         -- Imprime 1
PRINT CONCAT('Puede ver la película: ', CASE WHEN NOT @puedeVerPelicula = 1 THEN 'TRUE' ELSE 'FALSE' END);          -- Imprime FALSE



-- 4. Operadores de Conjuntos

-- Crear tabla CLIENTES
CREATE TABLE CLIENTES (ID INT PRIMARY KEY,Nombre VARCHAR(50),Ciudad VARCHAR(50));
-- Insertar datos en CLIENTES
INSERT INTO CLIENTES (ID, Nombre, Ciudad) VALUES (1, 'Ana', 'Madrid'), (2, 'Juan', 'Barcelona'), (3, 'María', 'Valencia'), (4, 'Pedro', 'Madrid'), (5, 'Laura', 'Sevilla'); 

-- Crear tabla EMPLEADOS
CREATE TABLE EMPLEADOS (ID INT PRIMARY KEY, Nombre VARCHAR(50), Departamento VARCHAR(50), Activo BIT);
-- Insertar datos en EMPLEADOS
INSERT INTO EMPLEADOS (ID, Nombre, Departamento, Activo) VALUES(101, 'Juan', 'Ventas', 1),(102, 'María', 'Recursos Humanos', 0),(103, 'Carlos', 'IT', 1),(104, 'Ana', 'Marketing', NULL),(105, 'Pedro', 'Finanzas', 0);

SELECT Nombre FROM CLIENTES UNION SELECT Nombre FROM EMPLEADOS;             -- UNION: Obtener todos los nombres de CLIENTES y EMPLEADOS (sin duplicados)
SELECT Nombre FROM CLIENTES UNION ALL SELECT Nombre FROM EMPLEADOS;         -- UNION ALL: Obtener todos los nombres de CLIENTES y EMPLEADOS (con duplicados)
SELECT Nombre FROM CLIENTES INTERSECT SELECT Nombre FROM EMPLEADOS;         -- INTERSECT: Obtener los nombres de los CLIENTES que también son EMPLEADOS
SELECT Nombre FROM CLIENTES EXCEPT SELECT Nombre FROM EMPLEADOS;            -- EXCEPT: Obtener los nombres de los CLIENTES que no son EMPLEADOS



-- 5. Operadores de Cadenas

SELECT Nombre + ' del departamento de ' + Departamento AS INFORMACIÓNCLIENTE FROM EMPLEADOS;                -- Concatenar cadenas
SELECT * FROM EMPLEADOS WHERE Nombre LIKE 'A%';                                                             -- LIKE: Buscar nombres que empiecen por 'A'
SELECT * FROM CLIENTES WHERE Nombre LIKE '____a';                                                           -- LIKE: Buscar nombres que tengan 5 letras y terminen en 'a'
SELECT LEN(Nombre) AS LongitudNombre FROM EMPLEADOS;                                                        -- LEN: Obtener la longitud de los nombres
SELECT SUBSTRING(Departamento, 1, 5) AS Primeros10Caracteres FROM EMPLEADOS;                                -- SUBSTRING: Obtener los primeros 5 caracteres del Departamento 
SELECT REPLACE(Nombre, 'a', 'o') AS NuevoNombreRaro FROM CLIENTES;                                          -- REPLACE: Reemplazar 'a' por 'o' en los nombres
SELECT UPPER(Nombre) AS NombreMayusculas, LOWER(Departamento) AS DepartamentoMinusculas FROM EMPLEADOS;     -- UPPER Convertir a mayúsculas y LOWER Convertir a minúsculas

-- 6. Otros Operadores de verificación

SELECT * FROM CLIENTES WHERE ID BETWEEN 2 AND 4;                                                                        -- Obtener los clientes cuyo ID está entre 2 y 4
SELECT * FROM CLIENTES WHERE CIUDAD IN ('Madrid', 'Barcelona');                                                         -- Obtener los clientes que son de Madrid o Barcelona
SELECT * FROM EMPLEADOS WHERE Activo IS NULL;                                                                           -- Obtener los empleados que no están activos
SELECT * FROM EMPLEADOS WHERE Nombre IS NOT NULL;                                                                       -- Obtener los empleados cuyo nombre está registrado
SELECT Nombre FROM CLIENTES c WHERE EXISTS (SELECT * FROM EMPLEADOS e WHERE e.Nombre = c.Nombre AND e.Activo = 1);      -- Obtener los clientes que se llaman igual que los empleados activos


-- DIFICULTAD EXTRA - Crea un programa que imprima por consola todos los números comprendidos entre 10 y 55 (incluidos)
-- pares, y que no son ni el 16 ni múltiplos de 3.

DECLARE @numero INT = 10;
DECLARE @limite INT = 55;

WHILE @numero <= @limite
BEGIN
    IF @numero % 2 = 0 AND @numero <> 16 AND @numero % 3 <> 0
    BEGIN
        PRINT @numero;
    END
    SET @numero = @numero + 1;
END