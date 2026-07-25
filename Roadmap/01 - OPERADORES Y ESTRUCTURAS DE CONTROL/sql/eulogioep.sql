-- Creación de una tabla de ejemplo
CREATE TABLE empleados (
    id INT PRIMARY KEY,
    nombre VARCHAR(50),
    salario DECIMAL(10, 2),
    departamento VARCHAR(50)
);

-- Inserción de datos de ejemplo
INSERT INTO empleados (id, nombre, salario, departamento) VALUES
(1, 'Juan', 30000, 'IT'),
(2, 'María', 35000, 'Ventas'),
(3, 'Carlos', 28000, 'IT'),
(4, 'Ana', 40000, 'Recursos Humanos'),
(5, 'Pedro', 32000, 'Ventas');

-- 1. Operadores Aritméticos
SELECT 
    'Suma' AS operacion, 5 + 3 AS resultado
UNION ALL
SELECT 'Resta', 10 - 4
UNION ALL
SELECT 'Multiplicación', 6 * 2
UNION ALL
SELECT 'División', 15.0 / 3
UNION ALL
SELECT 'Módulo', 17 % 5;

-- 2. Operadores de Comparación
SELECT 
    nombre, 
    salario,
    CASE 
        WHEN salario > 30000 THEN 'Alto'
        WHEN salario < 30000 THEN 'Bajo'
        ELSE 'Medio'
    END AS nivel_salario
FROM empleados;

-- 3. Operadores Lógicos
SELECT *
FROM empleados
WHERE departamento = 'IT' AND salario > 25000;

-- 4. Operadores de Conjunto
SELECT departamento FROM empleados
UNION
SELECT 'Marketing' AS departamento;

-- 5. Funciones de Agregación (equivalente a operadores en otros lenguajes)
SELECT 
    AVG(salario) AS promedio_salario,
    MAX(salario) AS salario_maximo,
    MIN(salario) AS salario_minimo,
    COUNT(*) AS total_empleados
FROM empleados;

-- 6. Subconsultas (una forma de control de flujo en SQL)
SELECT nombre, salario
FROM empleados
WHERE salario > (SELECT AVG(salario) FROM empleados);

-- 7. Joins (otra forma de combinar y controlar el flujo de datos)
SELECT e1.nombre AS empleado, e2.nombre AS companero
FROM empleados e1
JOIN empleados e2 ON e1.departamento = e2.departamento AND e1.id < e2.id;

-- 8. Estructuras de Control (usando procedimientos almacenados - la sintaxis puede variar según el DBMS)
DELIMITER //
CREATE PROCEDURE clasificar_salarios()
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE emp_nombre VARCHAR(50);
    DECLARE emp_salario DECIMAL(10, 2);
    DECLARE cur CURSOR FOR SELECT nombre, salario FROM empleados;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    OPEN cur;

    read_loop: LOOP
        FETCH cur INTO emp_nombre, emp_salario;
        IF done THEN
            LEAVE read_loop;
        END IF;
        
        IF emp_salario > 35000 THEN
            SELECT CONCAT(emp_nombre, ' tiene un salario alto');
        ELSEIF emp_salario < 30000 THEN
            SELECT CONCAT(emp_nombre, ' tiene un salario bajo');
        ELSE
            SELECT CONCAT(emp_nombre, ' tiene un salario medio');
        END IF;
    END LOOP;

    CLOSE cur;
END //
DELIMITER ;

-- Llamada al procedimiento
CALL clasificar_salarios();

-- 9. DIFICULTAD EXTRA (adaptada a SQL)
-- Imprimimos números pares entre 10 y 55, excluyendo 16 y múltiplos de 3
WITH RECURSIVE numeros(n) AS (
    SELECT 10
    UNION ALL
    SELECT n + 1 FROM numeros WHERE n < 55
)
SELECT n
FROM numeros
WHERE n % 2 = 0 
  AND n != 16 
  AND n % 3 != 0;