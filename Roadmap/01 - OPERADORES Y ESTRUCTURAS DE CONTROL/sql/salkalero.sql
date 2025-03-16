-- Operadores Aritméticos

SELECT "Suma: 5+2=",(5+2);
SELECT "Resta: 5-2=",(5-2);
SELECT "Multiplicación: 5x2=",(5*2);
SELECT "División: 5/2=",(5/2);
SELECT "Módulo: 5%2=",(5%2);

-- Operadores de Comparación

SET @a := 25;
SET @b := 125;
SELECT "Igual a: ¿25 es igual que 125?", if (@a = @b, "Verdadero", "Falso");
SELECT "Diferente a: ¿25 es diferente que 125?", if (@a <> @b, "Verdadero", "Falso");
SELECT "Mayor que : ¿25 es mayor que 125?", if (@a > @b, "Verdadero", "Falso");
SELECT "Menor que: ¿25 es menor que 125?", IF (@a < @b, "Verdadero", "Falso");
SELECT "Mayor o igual que: ¿25 es mayor o igual que 125?", IF (@a >= @b, "Verdadero", "Falso");
SELECT "Menor o igual que: ¿25 es menor o igual que 125?", IF (@a <= @b, "Verdadero", "Falso");

-- Operadores Lógicos

SET @c := 2;
SET @d := 1;
SELECT "Operando AND: c y d =",( @c AND @d );
SELECT "Operando OR: c or d =",( @c OR @d );
SELECT "Operando NOT: c not d =",( NOT @c);


-- Operadores de Asignación

SET @a := 5 , @b := 25 ;
SET @suma = @a + @b;
SELECT'Resultado de asignación := ',(@suma);

-- Estructura de control

delimiter //

create procedure Sumar( in Valor1 int,in Valor2 int )
begin
	SET @1 := Valor1 , @2 := Valor2;
	SELECT "Suma: a+b=",(@1+@2);
end //

delimiter ;

delimiter //

create procedure Igualdad(in valor1 int, in valor2 int)
begin
	SET @a := valor1;
	SET @b := valor2;
	SELECT "¿Primera cifra es mayor o igual?",@a,@b, IF (@a >= @b, "Verdadero", "Falso");
end //

delimiter ;


delimiter //

create procedure Condicional(in a int, in b int)
begin
	declare resultado char(20);
    if a > b then
		set resultado = "a es mayor";
	elseif a < b then
		set resultado = "b es mayor";
	else
		set resultado = "a y b son iguales";
	end if;
    select resultado;
end //

delimiter ;


delimiter //

create procedure Mes(in mes int)
begin
	declare resultado char(50);
    case
		when mes = 1 then set resultado = "Enero";
        when mes = 2 then set resultado = "Febrero";
        when mes = 3 then set resultado = "Marzo";
        when mes = 4 then set resultado = "Abril";
        when mes = 5 then set resultado = "Mayo";
        when mes = 6 then set resultado = "Junio";
        when mes = 7 then set resultado = "Julio";
        when mes = 8 then set resultado = "Agosto";
        when mes = 9 then set resultado = "Septiembre";
        when mes = 10 then set resultado = "Octubre";
        when mes = 11 then set resultado = "Nobiembre";
        when mes = 12 then set resultado = "Diciembre";
        else set resultado= "Mes inválido, por favor indique del 1 al 12";
	end case;
    select resultado;
end //

delimiter ;


-- Extra

DELIMITER //

CREATE PROCEDURE Extra()
BEGIN
    DECLARE counter INT DEFAULT 10;

    WHILE counter <= 55 DO
        IF counter % 2 = 0 AND counter <> 16 AND counter % 3 <> 0 THEN
            SELECT counter AS number;
        END IF;
        SET counter = counter + 1;
    END WHILE;
END //

DELIMITER ;

call sumar(500,512);
call igualdad(24,25);
call Condicional(22,22);
call Mes(3);
call Extra()