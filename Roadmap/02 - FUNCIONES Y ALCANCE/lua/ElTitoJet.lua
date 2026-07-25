-- Función sin parámetros ni retorno
function saludar()
    print("Hola desde una función sin parámetros ni retorno")
end

saludar()

-- Función con un parámetro
function saludarNombre(nombre)
    print("Hola, " .. nombre)
end

saludarNombre("Jose")

-- Función con varios parámetros y retorno
function sumar(a, b)
    return a + b
end

local resultado = sumar(10, 20)
print("Suma:", resultado)

-- Función que retorna múltiples valores
function operaciones(a, b)
    return a + b, a - b, a * b, a / b
end

local suma, resta, mult, div = operaciones(8, 2)
print("Resultados:", suma, resta, mult, div)

-- Funciones anidadas (funciones dentro de funciones)
function externa()
    print("Estoy en la funcion externa")

    local function interna()
        print("Estoy en la funcion interna")
    end

    interna()
end

externa()


-- Formatos de texto
local texto = "lua es genial"
print("Texto original:", texto)
print("Texto en mayusculas:", string.upper(texto))
print("Longitud del texto:", string.len(texto))
print("¿Empieza con 'lua'? :", string.sub(texto, 1, 3) == "lua")


-- Variables locales vs Globales

-- Variable global
globalVar = "Soy global"



function mostrarVariables()
    -- Variable local
    local localVar = "Soy local"
    print("Global:", globalVar)
    print("Local:", localVar) -- localVar solo es accesible si está en el mismo alcance
end

mostrarVariables()




-- DIFICULTAD EXTRA
function fizzBuzzPersonalizado(palabra3, palabra5)
    local contador = 0

    for i = 1, 100 do
        local salida = ""

        if i % 3 == 0 and i % 5 == 0 then
        salida = palabra3 .. palabra5
        elseif i % 3 == 0 then
        salida = salida .. palabra3
        elseif i % 5 == 0 then
        salida = salida .. palabra5
        end

        if salida == "" then
            print(i)
            contador = contador + 1
        else
            print(salida)
        end
    end

    return contador
end

local vecesNumero = fizzBuzzPersonalizado("Fizz", "Buzz")
print("Veces que se imprimio el numero directamente:", vecesNumero)
