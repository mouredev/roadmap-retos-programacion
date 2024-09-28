-- Asumimos que estamos usando MySQL para este ejemplo

-- Creamos una base de datos para nuestros ejemplos
CREATE DATABASE IF NOT EXISTS ejemplos_funciones;
USE ejemplos_funciones;

-- Creamos una tabla para almacenar un contador global
CREATE TABLE IF NOT EXISTS contador_global (
    valor INT DEFAULT 0
);
INSERT INTO contador_global (valor) VALUES (0);

-- 1. Procedimiento almacenado sin parámetros ni retorno
DELIMITER //
CREATE PROCEDURE saludar()
BEGIN
    SELECT 'Hola, mundo!' AS mensaje;
END //
DELIMITER ;

-- 2. Procedimiento almacenado con un parámetro y sin retorno
DELIMITER //
CREATE PROCEDURE saludarPersona(IN nombre VARCHAR(50))
BEGIN
    SELECT CONCAT('¡Hola, ', nombre, '!') AS mensaje;
END //
DELIMITER ;

-- 3. Función con múltiples parámetros y retorno
DELIMITER //
CREATE FUNCTION sumar(a INT, b INT) RETURNS INT
DETERMINISTIC
BEGIN
    RETURN a + b;
END //
DELIMITER ;

-- 4. Función que simula una "función dentro de otra"
-- (En SQL no podemos definir funciones dentro de otras, pero podemos simular el comportamiento)
DELIMITER //
CREATE FUNCTION operacionMatematica(a INT, b INT) RETURNS INT
DETERMINISTIC
BEGIN
    DECLARE resultado INT;
    SET resultado = a * b + 10;
    RETURN resultado;
END //
DELIMITER ;

-- 5. Uso de una función incorporada en SQL
SELECT CURRENT_DATE() AS fecha_actual;

-- 6. Demostración de variable local vs global
DELIMITER //
CREATE PROCEDURE incrementarContador()
BEGIN
    DECLARE contador_local INT DEFAULT 0;
    SET contador_local = contador_local + 1;
    
    UPDATE contador_global SET valor = valor + 1;
    
    SELECT contador_local AS contador_local, valor AS contador_global 
    FROM contador_global;
END //
DELIMITER ;

-- DIFICULTAD EXTRA
DELIMITER //
CREATE PROCEDURE imprimirYContar(IN texto1 VARCHAR(50), IN texto2 VARCHAR(50), OUT numeros_puros INT)
BEGIN
    DECLARE i INT DEFAULT 1;
    DECLARE resultado VARCHAR(100);
    SET numeros_puros = 0;
    
    WHILE i <= 100 DO
        IF i % 3 = 0 AND i % 5 = 0 THEN
            SET resultado = CONCAT(texto1, texto2);
        ELSEIF i % 3 = 0 THEN
            SET resultado = texto1;
        ELSEIF i % 5 = 0 THEN
            SET resultado = texto2;
        ELSE
            SET resultado = CAST(i AS CHAR);
            SET numeros_puros = numeros_puros + 1;
        END IF;
        
        SELECT resultado;
        
        SET i = i + 1;
    END WHILE;
END //
DELIMITER ;

-- Llamadas a los procedimientos y funciones
CALL saludar();

CALL saludarPersona('Alice');

SELECT sumar(5, 3) AS suma;

SELECT operacionMatematica(4, 5) AS resultado_operacion;

CALL incrementarContador();
CALL incrementarContador();

CALL imprimirYContar('Fizz', 'Buzz', @numeros_puros);
SELECT @numeros_puros AS numeros_sin_reemplazar;