-- Crear la tabla de contactos
CREATE TABLE contactos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre VARCHAR(100) NOT NULL,
    telefono VARCHAR(11) NOT NULL,
    CONSTRAINT telefono_valido CHECK (telefono REGEXP '^[0-9]{1,11}$')
);

-- Insertar algunos contactos de ejemplo
INSERT INTO contactos (nombre, telefono) VALUES ('Juan Pérez', '12345678901');
INSERT INTO contactos (nombre, telefono) VALUES ('María García', '98765432100');

-- Buscar un contacto
SELECT nombre, telefono FROM contactos WHERE nombre = 'Juan Pérez';

-- Añadir un nuevo contacto
INSERT INTO contactos (nombre, telefono) VALUES ('Ana López', '55566677788');

-- Actualizar un contacto
UPDATE contactos SET telefono = '11122233344' WHERE nombre = 'María García';

-- Eliminar un contacto
DELETE FROM contactos WHERE nombre = 'Ana López';

-- Mostrar todos los contactos
SELECT nombre, telefono FROM contactos ORDER BY nombre;

-- Procedimiento almacenado para añadir un contacto (si el RDBMS lo soporta)
DELIMITER //
CREATE PROCEDURE añadir_contacto(IN p_nombre VARCHAR(100), IN p_telefono VARCHAR(11))
BEGIN
    IF p_telefono REGEXP '^[0-9]{1,11}$' THEN
        INSERT INTO contactos (nombre, telefono) VALUES (p_nombre, p_telefono);
        SELECT 'Contacto añadido con éxito' AS mensaje;
    ELSE
        SELECT 'Número de teléfono no válido' AS mensaje;
    END IF;
END //
DELIMITER ;

-- Llamada al procedimiento almacenado
CALL añadir_contacto('Carlos Rodríguez', '12345678901');

-- Vista para mostrar todos los contactos
CREATE VIEW vista_contactos AS
SELECT nombre, telefono FROM contactos ORDER BY nombre;

-- Usar la vista
SELECT * FROM vista_contactos;