-- URL del sitio web oficial de SQL (estándar ANSI)
-- https://www.iso.org/standard/63555.html

-- Diferentes formas de crear comentarios en SQL:

-- 1. Comentario de una línea

/*
 * 2. Comentario
 * de varias
 * líneas
 */

-- Creación de una tabla para demostrar los tipos de datos
CREATE TABLE EjemploTipos (
    id INT PRIMARY KEY,
    texto VARCHAR(50),
    numero_entero INT,
    numero_decimal DECIMAL(10, 2),
    fecha DATE,
    hora TIME,
    fecha_hora DATETIME,
    booleano BOOLEAN
);

-- Inserción de datos para demostrar los tipos
INSERT INTO EjemploTipos (id, texto, numero_entero, numero_decimal, fecha, hora, fecha_hora, booleano)
VALUES (1, 'Hola, SQL!', 42, 3.14, '2024-09-11', '12:00:00', '2024-09-11 12:00:00', TRUE);

-- Consulta para mostrar los datos (equivalente a "imprimir")
SELECT 'Hola, SQL!' AS saludo;

-- Consulta para mostrar todos los datos insertados
SELECT * FROM EjemploTipos;

-- Uso de variables (en algunos sistemas de gestión de bases de datos)
-- Nota: La sintaxis puede variar según el sistema que se use

-- En MySQL:
SET @mi_variable = 'Valor de ejemplo';
SELECT @mi_variable;

-- En SQL Server:
DECLARE @mi_variable VARCHAR(50) = 'Valor de ejemplo';
SELECT @mi_variable;

-- En PostgreSQL:
DO $$
DECLARE
    mi_variable VARCHAR(50) := 'Valor de ejemplo';
BEGIN
    RAISE NOTICE 'Mi variable: %', mi_variable;
END $$;

-- Creación de una constante (simulada mediante una vista)
CREATE VIEW ConstanteEjemplo AS
SELECT 42 AS MI_CONSTANTE;

-- Consulta de la constante
SELECT * FROM ConstanteEjemplo;