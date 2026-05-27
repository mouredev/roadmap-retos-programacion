-- #31 SIMULADOR JUEGOS OLÍMPICOS - SisaRoot (SQLite)

CREATE TABLE IF NOT EXISTS events (
    id   INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS participants (
    id       INTEGER PRIMARY KEY AUTOINCREMENT,
    event_id INTEGER NOT NULL REFERENCES events(id),
    name     TEXT NOT NULL,
    country  TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS results (
    id             INTEGER PRIMARY KEY AUTOINCREMENT,
    event_id       INTEGER NOT NULL REFERENCES events(id),
    gold_name      TEXT NOT NULL, gold_country    TEXT NOT NULL,
    silver_name    TEXT NOT NULL, silver_country  TEXT NOT NULL,
    bronze_name    TEXT NOT NULL, bronze_country  TEXT NOT NULL
);

-- == REGISTRAR EVENTOS ==
INSERT INTO events (name) VALUES
    ('100m Atletismo'), ('Natacion 200m'), ('Ciclismo de Pista');

-- == REGISTRAR PARTICIPANTES ==
INSERT INTO participants (event_id, name, country) VALUES
    (1,'Marcell Jacobs','Italia'),
    (1,'Fred Kerley','Estados Unidos'),
    (1,'Trayvon Bromell','Estados Unidos'),
    (1,'Adam Gemili','Reino Unido'),
    (2,'Caeleb Dressel','Estados Unidos'),
    (2,'Kristof Milak','Hungria'),
    (2,'Tom Dean','Reino Unido'),
    (2,'Kyle Chalmers','Australia'),
    (3,'Harrie Lavreysen','Paises Bajos'),
    (3,'Jeffrey Hoogland','Paises Bajos'),
    (3,'Jack Carlin','Reino Unido'),
    (3,'Nicholas Paul','Trinidad y Tobago');

-- == SIMULAR EVENTOS (aleatorio) ==
INSERT INTO results (event_id, gold_name, gold_country, silver_name, silver_country, bronze_name, bronze_country)
SELECT p1.event_id, p1.name, p1.country, p2.name, p2.country, p3.name, p3.country
FROM
    (SELECT *, ROW_NUMBER() OVER (PARTITION BY event_id ORDER BY RANDOM()) rn FROM participants) p1
    JOIN (SELECT *, ROW_NUMBER() OVER (PARTITION BY event_id ORDER BY RANDOM()) rn FROM participants) p2
      ON p1.event_id=p2.event_id AND p2.rn=2 AND p1.name<>p2.name
    JOIN (SELECT *, ROW_NUMBER() OVER (PARTITION BY event_id ORDER BY RANDOM()) rn FROM participants) p3
      ON p1.event_id=p3.event_id AND p3.rn=3 AND p1.name<>p3.name AND p2.name<>p3.name
WHERE p1.rn=1;

-- == GANADORES POR EVENTO ==
SELECT e.name AS Evento,
    r.gold_name   ||' ('||r.gold_country  ||')' AS Oro,
    r.silver_name ||' ('||r.silver_country||')' AS Plata,
    r.bronze_name ||' ('||r.bronze_country||')' AS Bronce
FROM results r JOIN events e ON e.id=r.event_id;

-- == RANKING POR PAÍS ==
WITH m AS (
    SELECT gold_country   country, 1 g, 0 s, 0 b FROM results
    UNION ALL SELECT silver_country, 0,1,0 FROM results
    UNION ALL SELECT bronze_country, 0,0,1 FROM results
)
SELECT ROW_NUMBER() OVER (ORDER BY SUM(g) DESC,SUM(s) DESC,SUM(b) DESC) Pos,
    country Pais, SUM(g) Oro, SUM(s) Plata, SUM(b) Bronce, SUM(g+s+b) Total
FROM m GROUP BY country ORDER BY SUM(g) DESC,SUM(s) DESC,SUM(b) DESC;
