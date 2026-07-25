/*
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

-- 🔥 Ejemplo:
-- TABAL 1
CREATE DATABASE Ejercici01;
USE Ejercici01;

CREATE TABLE Empleados (
	ID INT,
	NOMBRE varchar(20),
	APELLIDO varchar(30),
	EDAD numeric(2),
	TELEFONO numeric(10),
	DIRECCION varchar(100),
	FECHA_NACIMIENTO date,
	SALARIO decimal (18,2),
	ACTIVO char(2)
);

insert into empleados values (1, 'Juan', 'Pérez', 25, 1234567890, 'Calle 123', '1978-06-15', 2500.00, 'SI');
insert into empleados values (2, 'María', 'López', 30, 9876543210, 'Avenida 456', '1980-03-20', 3000.00, 'SI');
insert into empleados values (3, 'Carlos', 'González', 28, 5555555555, 'Calle 789', '1979-11-10', 2800.00, 'SI');
insert into empleados values (4, 'Ana', 'Martínez', 35, 9998887770, 'Avenida 012', '1977-09-05', 3500.00, 'SI');
insert into empleados values (5, 'Pedro', 'Sánchez', 22, 1112223334, 'Calle 567', '1980-01-25', 2000.00, 'SI');
insert into empleados values (6, 'Laura', 'Ramírez', 31, 4444444444, 'Avenida 890', '1978-07-12', 3200.00, 'SI');
insert into empleados values (7, 'Luis', 'Torres', 29, 7777777777, 'Calle 345', '1979-04-18', 2700.00, 'SI');
insert into empleados values (8, 'Carmen', 'Hernández', 27, 6666666666, 'Avenida 678', '1980-02-03', 2600.00, 'SI');
insert into empleados values (9, 'Jorge', 'García', 33, 2223334445, 'Calle 901', '1977-12-27', 3400.00, 'SI');
insert into empleados values (10, 'Silvia', 'Lara', 24, 8889990000, 'Avenida 234', '1980-05-09', 2200.00, 'SI');
insert into empleados values (11, 'Roberto', 'Rojas', 26, 3334445556, 'Calle 567', '1979-02-14', 2400.00, 'SI');
insert into empleados values (12, 'Patricia', 'Cruz', 32, 2223334444, 'Avenida 890', '1978-08-21', 3100.00, 'SI');
insert into empleados values (13, 'Daniel', 'Gómez', 29, 5556667778, 'Calle 123', '1979-06-06', 2800.00, 'SI');
insert into empleados values (14, 'Sara', 'Vargas', 34, 6667778889, 'Avenida 456', '1977-04-01', 3300.00, 'SI');
insert into empleados values (15, 'Hugo', 'Orozco', 23, 9998887776, 'Calle 789', '1980-03-16', 2100.00, 'SI');

-- TABLA 2
CREATE TABLE NUMEROS (
	id INT,
	n1 INT,
	n2 INT
);

INSERT INTO NUMEROS VALUES (1, 5, 8);
INSERT INTO NUMEROS VALUES (2, 7, 9);
INSERT INTO NUMEROS VALUES (3, 7, 0);


-- 🔥 a. Operadores artiméticos
SELECT
	n1 as 'Numero 1',
	n2 as 'Numero 2',
	n1 + n2 AS Suma,
	n1 - n2 AS Resta,
	n1 * n2 AS Multiplicacion,
	n1 / CAST(n2 AS FLOAT) AS Division,
	n1 % n2 AS Modulo
FROM NUMEROS
WHERE n2 <> 0;


-- 🔥 b. Operadores de Comparación
SELECT * FROM Empleados WHERE ID = 15;
SELECT * FROM Empleados WHERE EDAD <> 15;
SELECT * FROM Empleados WHERE EDAD != 15;
SELECT * FROM Empleados WHERE EDAD > 15;
SELECT * FROM Empleados WHERE EDAD < 15;
SELECT * FROM Empleados WHERE EDAD <= 15;
SELECT * FROM Empleados WHERE EDAD >= 15;

SELECT * FROM Empleados WHERE EDAD BETWEEN 30 AND 35; -- Si esta dentro del rango, incluye los extremos
SELECT * FROM Empleados WHERE NOMBRE IN ('Juan', 'María', 'Carlos'); -- Compara si el valor está
SELECT * FROM Empleados WHERE APELLIDO LIKE 'L%'; -- Apellidos que empiezan con 'L'
SELECT * FROM Empleados WHERE TELEFONO IS NULL; -- Valores NULL
SELECT * FROM Empleados WHERE TELEFONO IS NOT NULL; -- Valores no NULL


-- 🔥 c. Operadores Lógicos

PRINT 'Obtener empleados cuya edad sea mayor a 25 y cuyo salario sea mayor a 2500.';
SELECT Nombre, Edad, Salario FROM Empleados WHERE (EDAD > 25) AND (salario > 2500); -- AND

PRINT 'Obtener empleados cuyo salario sea mayor a 3000 o cuyo nombre sea "Juan".';
SELECT Nombre, Salario FROM Empleados WHERE (salario > 3000) OR (nombre = 'Juan'); -- OR

PRINT 'Obtener empleados que no estén activos (no tengan "SI" en la columna ACTIVO).';
SELECT Nombre, Activo FROM Empleados WHERE NOT Activo = 'SI'; -- NOT 

PRINT  'Obtener empleados cuya edad sea mayor a 30 o cuyo salario sea mayor a 3500, pero solo si están activos.';
SELECT * FROM Empleados WHERE ((edad > 30) OR (salario > 3500)) AND (activo = 'SI');

PRINT 'Obtener empleados cuya edad esté entre 25 y 35, y cuyo salario sea mayor a 2500, pero que no sean activos.';
SELECT * FROM Empleados WHERE (edad BETWEEN 25 AND 35) AND (salario>2500) AND ( NOT activo = 'SI');

PRINT 'Obtener empleados con un salario superior a 3000 y que tengan la letra 'G' en su apellido, o aquellos que tengan un nombre que comience con "M".';
SELECT * FROM Empleados WHERE (salario>3000 AND apellido LIKE 'G%') OR (nombre LIKE 'M%')

PRINT 'Obtener empleados que no sean de la calle "Avenida 456" ni tengan un teléfono específico.';
PRINT 'num : 999111999';
SELECT * FROM Empleados WHERE (NOT DIRECCION = 'Avenida 456') AND  teléfono <> 999111999;


-- 🔥 d. Operadores de Asignación

-- Ejemplo de " = ".
UPDATE Empleados SET ACTIVO = 'NO' WHERE ID = 1;

-- Incremento con " += "
UPDATE Empleados SET SALARIO += 500 WHERE ID = 2;

-- Decremento con " -= "
UPDATE Empleados SET SALARIO -= 200 WHERE ID = 3;

-- Multiplicación  con " *= " 
UPDATE Empleados SET SALARIO *= 1.10 WHERE ID = 4;

-- División con " /= "
UPDATE Empleados SET SALARIO /= 2 WHERE ID = 5;

-- Basada en una condicion
--Cambiar el estado "ACTIVO" a "NO" para empleados mayores de 30 años.
UPDATE Empleados SET ACTIVO = 'NO' WHERE EDAD > 30;

-- EJEMPLO de una combinacion de cálculos y asignación
/*
Ajustar el salario de todos los empleados dependiendo de su edad:
Si la edad es menor a 25 años, incrementar en un 15%.
Si la edad es entre 25 y 30 años, incrementar en un 10%.
Si la edad es mayor a 30 años, incrementar en un 5%.
*/
UPDATE Empleados
SET SALARIO = 
    CASE 
        WHEN EDAD < 25 THEN SALARIO * 1.15
        WHEN EDAD BETWEEN 25 AND 30 THEN SALARIO * 1.10
        ELSE SALARIO * 1.05
    END;

-- Asignación a varias columnas simultáneamente
UPDATE Empleados
SET NOMBRE = 'Laura María',
    APELLIDO = 'Ramírez López',
    SALARIO = 3500
WHERE ID = 6;


-- 🔥 e. Operadores de Pertenencia

-- IN - seleccionar
SELECT * FROM Empleados WHERE NOMBRE IN ('Juan', 'María', 'Carlos');

-- NOT IN - Excluir
SELECT * FROM Empleados WHERE ID NOT IN (1, 3, 5);


-- 🔥 f. Operadores de Bits

-- agregamos una tabla
ALTER TABLE Empleados ADD PERMISOS INT;

-- Actualizamos los valores de permisos con números representativos
UPDATE Empleados
SET PERMISOS = ID * 2; -- Simplemente asignamos un valor basado en el ID.


-- AND a nivel de bit (&)

-- Obtenemos empleados cuyos permisos tienen activado el segundo bit (valor 2 en binario):
SELECT ID, NOMBRE, PERMISOS
FROM Empleados
WHERE PERMISOS & 2 = 2;


-- OR a nivel de bit (|)

-- Añadimos un permiso al primer bit (valor 1 en binario):
SELECT ID, NOMBRE, PERMISOS, (PERMISOS | 1) AS NUEVOS_PERMISOS
FROM Empleados;


-- XOR a nivel de bit (^)

--Verificamos qué permisos cambiarían si aplicamos un XOR con 3:

SELECT ID, NOMBRE, PERMISOS, (PERMISOS ^ 3) AS XOR_RESULTADO
FROM Empleados;


-- Desplazamiento de bits a la izquierda (<<)

-- Multiplicamos los permisos por un factor de 2 desplazando los bits a la izquierda:
SELECT ID, NOMBRE, PERMISOS, (PERMISOS << 1) AS PERMISOS_DOBLE
FROM Empleados;


-- Desplazamiento de bits a la derecha (>>)

-- Dividimos los permisos entre 2 desplazando los bits a la derecha:
SELECT ID, NOMBRE, PERMISOS, (PERMISOS >> 1) AS PERMISOS_DIVIDIDO
FROM Empleados;


-- Complemento a nivel de bit (~)

-- Invertimos todos los bits de los permisos:
SELECT ID, NOMBRE, PERMISOS, (~PERMISOS) AS COMPLEMENTO
FROM Empleados;


-- 🔥 g. Estructuras de Control

-- IF - ELSE
-- ejm: Verifica si un empleado tiene un salario mayor a 3000 y realiza acciones:
IF (SELECT SALARIO FROM Empleados WHERE ID = 1) > 3000
BEGIN
    PRINT 'Salario alto';
END
ELSE
BEGIN
    PRINT 'Salario bajo';
END

-- CASE
-- ejm: Consulta empleados categorizando por salario:
SELECT NOMBRE, 
	CASE 
		WHEN SALARIO > 3000 THEN 'Alto'
		WHEN SALARIO BETWEEN 2000 AND 3000 THEN 'Medio'
		ELSE 'Bajo'
	END AS Categoria
FROM Empleados;

-- WHILE
-- ejm: Itera sobre IDs de empleados para realizar acciones:
DECLARE @ID INT = 1;

WHILE @ID <= (SELECT MAX(ID) FROM Empleados)
BEGIN
    PRINT 'Procesando empleado con ID: ' + CAST(@ID AS VARCHAR);
    SET @ID = @ID + 1;
END;


-- Manejo de errores TRY - CATCH
-- ejm: T-SQL
BEGIN TRY
    -- Intentar insertar un valor duplicado (error)
    INSERT INTO Empleados (ID, NOMBRE) VALUES (1, 'Prueba');
END TRY
BEGIN CATCH
    PRINT 'Ocurrió un error: ' + ERROR_MESSAGE();
END CATCH;




-- DIFICULTAD EXTRA  🔥🔥🔥
CREATE TABLE #Numeros (
    Numero INT
);

DECLARE @i INT = 10;

WHILE @i <= 55
BEGIN
    INSERT INTO #Numeros (Numero)
    VALUES (@i);

    SET @i = @i + 1;
END;

SELECT Numero
FROM #Numeros
WHERE Numero % 2 = 0
	AND Numero <> 16
	AND Numero % 3 <> 0;

-- Limpiar por si las dudas
DROP TABLE #Numeros;
