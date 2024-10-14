# Función sin parámetros ni return
function funcion_sin_parametros()
    println("Esta es una función sin parámetros ni return")
end

# Función con un parámetro sin return
function funcion_con_un_parametro(x)
    println("El parámetro recibido de esta función es: $x")
end

# Función con varios parámetros y return
function suma(a::Number, b::Number) 
    resultado = a + b
    println("La suma de $a y $b es: $resultado")
    return resultado
end

# Función que devuelve nothing según el valor de un parámetro
function division(dividendo::Number, divisor::Number)
    if divisor == 0
        println("Error: División por cero")
        return nothing  # Retornamos nothing si el divisor es cero
    else
        return dividendo / divisor  # Retornamos el resultado de la división
    end
end

# Función dentro de otra función
function funcion_externa()
    println("Esta es la función externa.")
    
    # Definición de la función interna
    function funcion_interna()
        println("Esta es la función interna, llamada desde la función externa.")
    end
    
    # Llamada a la función interna
    funcion_interna()  
end

# Uso de funciones ya creadas en el lenguaje
function longitud_arreglo(arr::Vector)::Int
    # La función `length` nos devuelve la longitud de un array
    longitud = length(arr)
    println("La longitud del arreglo es: $longitud")
    return longitud
end

# Variables locales y globales
global_var::Int = 10  # Variable global

function variable_local()
    local_var::Int = 5  # Variable local
    println("Dentro de la función:")
    println("Variable local: $local_var")
    println("Variable global: $global_var")
end

#  Función que recibe dos cadenas de texto y retorna un número
function imprimir_numeros(cadena1::String, cadena2::String)::Int
    contador::Int = 0  # Contador para los números impresos
    println("Imprimiendo números del 1 al 100:")
    
    for n in 1:100
        if n % 3 == 0 && n % 5 == 0
            println("$cadena1$cadena2")  # Imprime la concatenación si es múltiplo de 3 y 5
        elseif n % 3 == 0
            println(cadena1)  # Imprime cadena1 si es múltiplo de 3
        elseif n % 5 == 0
            println(cadena2)  # Imprime cadena2 si es múltiplo de 5
        else
            println(n)  # Imprime el número si no es múltiplo de 3 ni de 5
            contador += 1  # Incrementa el contador
        end
    end
    return contador  # Devuelve el contador de números impresos
end

# Llamadas a las funciones anteriores
println("=== Función sin parámetros ===")
funcion_sin_parametros()

println("\n=== Función con un parámetro ===")
funcion_con_un_parametro(42)

println("\n=== Función con varios parámetros y return ===")
resultado_suma = suma(3, 5) 

println("\n=== Función externa e interna ===")
funcion_externa()

println("\n=== Función que devuelve nothing ===")
division(12,0)

println("\n=== Función de longitud de array con `length` ===")
longitud = longitud_arreglo([1, 2, 3, 4, 5])

println("\n=== Variables locales y globales ===")
variable_local()

println("\n=== Función ejercicio opcional ===")
contador_resultado = imprimir_numeros("Fizz", "Buzz")
println("Total de números impresos en pantalla: $contador_resultado")
