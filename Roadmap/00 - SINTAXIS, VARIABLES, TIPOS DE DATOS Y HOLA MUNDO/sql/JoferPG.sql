--https://www.microsoft.com/es-co/sql-server/sql-server-downloads

--comentario simple de una linea

/*Comentario compuesto 
de varias lineas/*

--Tipo de variable:
DECLARE @my_variable INT; --Variable local
SET @my_varible = 10;

DECLARE @@my_varible#2 INT; --Variable global
SET @@my_varible#2 = 10;

--Constante (en SQL las constantes son un valor especifico)
DECLARE @My_Constante INT;
SET @My_constante = 10;

--tipos de datos primitivos

DECLARE @char CHAR(60);
        @date DATE;
        @binary BINARY;
        @money MONEY:
        @time TIME;
        @float FLOAT;
        @int INT;

SET @char = Zapato;
    @date = 01/08/2024;
    @binary = 1;
    @money = 3000.29;
    @time = 12:45:32.345;
    @float = 4.7;
    @int = 5;

--Imprimir terminal de texto 
PRINT ("Hola, SQL");
