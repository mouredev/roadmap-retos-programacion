--[[
 * EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
]]
--funciones sin argumento ni retorno
function holaMundo()
    print("Hola Mundo")
end
holaMundo()
function foo()
    print("Inicio de funcion foo")
    holaMundo()
    function goo()
        print("Se inicia la funcion goo dentro de foo")
    end
    goo()
    print("Fin de la funcion foo")
end
foo()

function funConParam(arg1, arg2)
    return arg1 + arg2
end

suma = funConParam(1, 2)
print("Llamamos a la funcion para sumar dos numeros: ", suma)

--lo intentamos un una excepcion en lua
function suma()
    local x = 10
    local y = 2
    return x + y
end
function resta(a, b)
    return a - b
end

local status, resultado = pcall(resta, 10, y)

if status then
    print("El esultado es :", resultado)
else
    print("Esa variable no es global")
end

function extra(string1, string2)
    count = 1
    for i = 1, 100 do
        if i % 3 == 0 and i % 5 == 0 then
            print(string1, string2)
        elseif i % 3 == 0 then
            print(string1)
        elseif i % 5 == 0 then
            print(string2)
        else
            print(i)
            count = count + 1
        end
    end
    print("Numero de veces que se imprimio un numero: ", count)
end
extra("Hola", "Mundo")
