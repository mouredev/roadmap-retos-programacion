# Sintaxis básica de una función
function f(x, y)
    x + y                 # El valor de la última expresión evaluada es retornada
end

# Forma de asignación
f1(x , y) = x + y         # Se usa con expresiones simples

println(f(2, 3))
println(f1(4, 5))

# Los nombres de funciones pueden ser valores Unicode
∑(x, y) = x + y

println("")
println(∑(6, 7))

# Usando la palabra reservada return
function g(x,y)
    return x * y          # Retorna este valor
    x + y               
end

println(g(2, 3))

# Tipo de Retorno
# Para especificar un tipo de retorno se usa el operador ::

function g1(x, y)::Int8
    return x * y
end;

println(typeof(g1(5, 10)))  # Devuelve Int8

# Retornando nothing - Funciones que no retornan nada
function printx(x)
    println("x = $x")
    return nothing
end

printx(1)

# Operadores como funciones
println(+(1, 2, 3, 4))   # Retorna la suma que es 10

# Funciones anónimas
# x -> x^2 + 2x - 1
# Se usan por lo general en funciones que toman otras funciones como argumentos (funciones de orden superior)

println(map(x -> x^2 + 2x - 1, [1, 3, -1]))  # Retorna [2, 14, -2]

# Función sin parámetros ni retorno
function x()
    return nothing
end

x()

# Funciones Varargs - Funciones de número variable de argumentos
bar(a,b,x...) = (a,b,x)

println(bar(1,2,3,4,5,6))

# RETO EXTRA
println("")
println("*****RETO EXTRA*****")
println("")

function imprimir(cadena1, cadena2)
    num = 0
    for i = 1:100
        if i % 3 == 0 && i % 5 == 0
            println(cadena1, cadena2)
        elseif i % 3 == 0
            println(cadena1)
        elseif i % 5 == 0
            println(cadena2)
        else 
            num += 1
            println(i)
        end
    end
    return num
end

cantNumImp = imprimir("Hola", "Mundo")
println("Número de veces que fue impreso un número: $cantNumImp")
