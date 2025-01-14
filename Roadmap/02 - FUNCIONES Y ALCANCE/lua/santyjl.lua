--[[
/*
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
 */
]]

--funcion si parametros ni retornos
function escalera ()
    local valor = "*"
    print("\n")
    for i=1 , 10 do
        print(valor)
        valor = valor .. "*" -- con .. se pueden concatenar tanto string como listas
    end
end

escalera()

print("")

-- funcion con parametros y retornos
function sumador(num1 , num2)
    return num1 + num2      -- return te da el valor para que lo puedas usar
end

print(sumador(2 , 3))

-- funciones dentro de funciones
print("")

function correr()
    function caminar()
        return "caminando"
    end

    local accion = ""
    accion = caminar()
    print(accion)
    accion = "corriendo"
    print(accion)
end

print(correr())
print("que estas haciendo ? : " .. caminar())

local numero_random = math.random(0 , 100)
local numero_maximo = math.max(7 , numero_random , 40)
local cuadrado = math.sqrt(numero_random)
local texto = "Hola mundo day"
print("\nfunciones matematicas")

print("numero random : " .. numero_random)
print("el maximo entre el numero 7 " .. numero_random .. " y el  40 : " .. numero_maximo)
print("la raiz cuadrado del numero " .. numero_random .. " es : " .. cuadrado)

print("\nfunciones de string : ")
print(string.upper(texto) .. " funcion string.upper()")
print(string.lower(texto) .. " funcion string.lower()")
print(string.len(texto) .. " funcion string.len()")

local variable_local = "esta es una varible local , solo funciona en este archivo"
variable_glogal = "esta es una varible global se puede usar en otro archivos .lua"

print("")
print(variable_local)
print(variable_glogal)

-- Extra

local function fizz_buzz(a , b)
    local contador = 1
    while contador <= 100  do
        if contador % 3 == 0 and contador % 5 == 0 then
            print(contador .. a .. b)

        else if contador % 5 == 0  then
            print(contador .. b)

        else if contador % 3 == 0 then
            print(contador .. a)

        else
            print(contador)

        end
        end
        end
        contador = contador + 1

    end

end

print(fizz_buzz(" fizz" , " buzz"))