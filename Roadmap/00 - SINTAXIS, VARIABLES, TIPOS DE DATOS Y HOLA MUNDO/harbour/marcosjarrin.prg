/*

web oficial:
https://harbour.github.io/

Distribución utilizada:
https://www.hmgextended.com/

Comentario en varias lineas

*/

// Comentario en una linea

** Comentario en una linea

#define CONSTANTE "Valor no Cambia"

function main()

local Entero, Flotante, Logico
local Cadena
local Fecha

	Cadena   := "Hola harbour"
	Entero   := 1
	Flotante := 10.25
	Fecha    := ctod('04-26-2024')
    Logico   := .T.
	Logico   := .F.

	/*
	  Se puede crear variables con tipado dinámico sin especificar su alcance, pero no es
	  recomendable, el compilador identifica el tipo de datos automáticamente .
	  Es case insensitive
	  ValorCualquiera := "Cadena"  	  Valorcualquiera := 12  	valorCualquiera := 12.45
	  es la misma variable.
	*/
	ValorCualquiera := "Cadena"
	Valorcualquiera := 12
	valorCualquiera := 12.45

	? 'Hola Harbour'

return NIL
