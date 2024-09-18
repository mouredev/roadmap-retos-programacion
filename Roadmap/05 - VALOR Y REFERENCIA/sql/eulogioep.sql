-- Creación de tablas
CREATE TABLE Empleados (
    id INT PRIMARY KEY,
    nombre VARCHAR(50),
    salario DECIMAL(10, 2)
);

CREATE TABLE Departamentos (
    id INT PRIMARY KEY,
    nombre VARCHAR(50),
    jefe_id INT,
    FOREIGN KEY (jefe_id) REFERENCES Empleados(id)
);

-- Inserción de datos
INSERT INTO Empleados (id, nombre, salario) VALUES
(1, 'Juan', 50000),
(2, 'María', 60000),
(3, 'Carlos', 55000);

INSERT INTO Departamentos (id, nombre, jefe_id) VALUES
(1, 'Ventas', 1),
(2, 'Marketing', 2);

-- Analogía de "paso por valor"
-- Actualizar el salario de un empleado
UPDATE Empleados
SET salario = salario * 1.1
WHERE id = 1;

-- Verificar el cambio
SELECT * FROM Empleados WHERE id = 1;

-- Analogía de "paso por referencia"
-- Cambiar el jefe de un departamento
UPDATE Departamentos
SET jefe_id = 3
WHERE id = 1;

-- Verificar el cambio
SELECT d.nombre AS Departamento, e.nombre AS Jefe
FROM Departamentos d
JOIN Empleados e ON d.jefe_id = e.id
WHERE d.id = 1;

-- Procedimiento almacenado para simular "paso por valor"
DELIMITER //
CREATE PROCEDURE AumentarSalario(IN empleado_id INT, IN aumento DECIMAL(10, 2))
BEGIN
    DECLARE salario_actual DECIMAL(10, 2);
    
    -- Obtener el salario actual
    SELECT salario INTO salario_actual FROM Empleados WHERE id = empleado_id;
    
    -- Aumentar el salario (solo dentro del procedimiento)
    SET salario_actual = salario_actual + aumento;
    
    -- Mostrar el nuevo salario (que no afecta a la tabla real)
    SELECT salario_actual AS NuevoSalario;
END //
DELIMITER ;

-- Procedimiento almacenado para simular "paso por referencia"
DELIMITER //
CREATE PROCEDURE CambiarJefeDepartamento(IN departamento_id INT, IN nuevo_jefe_id INT)
BEGIN
    -- Actualizar el jefe del departamento (afecta a la tabla real)
    UPDATE Departamentos SET jefe_id = nuevo_jefe_id WHERE id = departamento_id;
    
    -- Mostrar el cambio
    SELECT d.nombre AS Departamento, e.nombre AS NuevoJefe
    FROM Departamentos d
    JOIN Empleados e ON d.jefe_id = e.id
    WHERE d.id = departamento_id;
END //
DELIMITER ;

-- Ejemplos de uso de los procedimientos
CALL AumentarSalario(1, 5000);
SELECT * FROM Empleados WHERE id = 1;  -- El salario real no cambia

CALL CambiarJefeDepartamento(2, 3);
SELECT * FROM Departamentos WHERE id = 2;  -- El jefe sí cambia en la tabla real