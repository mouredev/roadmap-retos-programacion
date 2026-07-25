-- Operaciones con cadenas en SQL

-- Creamos una tabla temporal para nuestros ejemplos
CREATE TEMPORARY TABLE IF NOT EXISTS ejemplos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    texto VARCHAR(100)
);

-- Insertamos algunos datos de ejemplo
INSERT INTO ejemplos (texto) VALUES 
('Hola, mundo!'),
('TypeScript'),
('amor'),
('roma');

-- 1. Longitud de la cadena
SELECT texto, LENGTH(texto) AS longitud
FROM ejemplos;

-- 2. Conversión a mayúsculas y minúsculas
SELECT texto, 
       UPPER(texto) AS mayusculas, 
       LOWER(texto) AS minusculas
FROM ejemplos;

-- 3. Subcadenas
SELECT texto, 
       SUBSTRING(texto, 1, 4) AS subcadena
FROM ejemplos;

-- 4. Reemplazo
SELECT texto, 
       REPLACE(texto, 'mundo', 'SQL') AS reemplazo
FROM ejemplos
WHERE texto LIKE '%mundo%';

-- 5. Concatenación
SELECT CONCAT(e1.texto, ' ', e2.texto) AS concatenacion
FROM ejemplos e1, ejemplos e2
WHERE e1.id = 1 AND e2.id = 2;

-- 6. Recorte de espacios
SELECT TRIM('  Hola Mundo  ') AS recorte_espacios;

-- 7. Verificación
SELECT texto,
       texto LIKE 'Hola%' AS empieza_con_hola,
       texto LIKE '%!' AS termina_con_exclamacion,
       texto LIKE '%mundo%' AS contiene_mundo
FROM ejemplos;

-- DIFICULTAD EXTRA

-- Función para verificar si una palabra es un palíndromo
DELIMITER //
CREATE FUNCTION esPalindromo(palabra VARCHAR(100)) 
RETURNS BOOLEAN
DETERMINISTIC
BEGIN
    RETURN palabra = REVERSE(palabra);
END //
DELIMITER ;

-- Función para verificar si dos palabras son anagramas
DELIMITER //
CREATE FUNCTION sonAnagramas(palabra1 VARCHAR(100), palabra2 VARCHAR(100)) 
RETURNS BOOLEAN
DETERMINISTIC
BEGIN
    RETURN LOWER(palabra1) REGEXP CONCAT('^[', LOWER(palabra2), ']+$')
           AND LENGTH(palabra1) = LENGTH(palabra2);
END //
DELIMITER ;

-- Función para verificar si una palabra es un isograma
DELIMITER //
CREATE FUNCTION esIsograma(palabra VARCHAR(100)) 
RETURNS BOOLEAN
DETERMINISTIC
BEGIN
    RETURN LENGTH(palabra) = LENGTH(DISTINCT palabra);
END //
DELIMITER ;

-- Probamos las funciones
SELECT texto,
       esPalindromo(texto) AS es_palindromo,
       sonAnagramas(texto, 'roma') AS es_anagrama_de_roma,
       esIsograma(texto) AS es_isograma
FROM ejemplos
WHERE texto IN ('amor', 'roma', 'TypeScript');