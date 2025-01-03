# Operadores Aritméticos

x = 10
y = 20

print("*****OPERADORES ARITMETICOS*****\n\n")

print("Valor de x = $x\n")
print("Valor de y = $y\n\n")

print("Suma de x + y = $(x + y)\n")
print("Resta de y - x = $(x - y)\n")
print("Multiplicación de x * y = $(x * y)\n")
print("División de x / y = $(x / y)\n")
print("División entera de x ÷ y = $(x ÷ y)\n")
print("División inversa de x \\ y = $(x \ y) (Equivalente a y / x)\n")
print("Potenciación x ^ y = $(x ^ y)\n")
print("Módulo de 10 % 2 = $(10 % 2)\n")

print("\n\n*****OPERADORES BOOLEANOS*****\n\n")

a = true
b = false

print("Valor de a = $a\n")
print("Valor de b = $b\n\n")

print("Negación de !a = $(!a)\n")
print("Negación de !b = $(!b)\n")
print("Operador AND(y) -> a && b = $(a && b)\n")
print("Operador OR(o) -> a || b = $(a || b)\n")

print("\n\n*****OPERADORES A NIVEL DE BIT (BITWISE)*****\n\n")

print("Operador not ~123 = $(~123)\n")
print("Operador y 123 & 234 = $(123 & 234)\n")
print("Operador o 123 | 234 = $(123 | 234)\n")
print("Operador xor(o exclusivo) 123 ⊻ 234 = $(123 ⊻ 234)\n")
print("Operador nand(not and) 123 ⊼ 123 = $(123 ⊼ 123)\n")
print("Operador nor(not or) 123 ⊽ 124 = $(123 ⊽ 124)\n")

print("\n\n*****OPERADORES DE ACTUALIZACIÓN*****\n\n")

x = 1
print("Valor de x + 5 = $(x += 5)\n")  # x = x + 5
print("Valor de x - 5 = $(x -= 5)\n")  # x = x - 5
print("Valor de x * 5 = $(x *= 5)\n")  # x = x * 5
print("Valor de x / 5 = $(x /= 5)\n")  # x = x / 5
print("Valor de x \\ 5 = $(x \= 5)\n") # x = x \ 5
print
#=
  Otros operadores ÷=, %=, ^=, &=, |=, ⊻=, >>>=, >>=, <<=
=#

print("\n\n*****OPERADORES PUNTO (DOT) VECTORIZED*****\n\n")
# TODO: Falta este operador

print("\n\n*****OPERADORES DE COMPARACIÓN*****\n\n")

print("Operador de igualdad: 1 == 1 = $(1 == 1)\n")
print("Operador de inegualdad: 1 != 1 (≠) = $(1 != 1)\n")
print("Operador menor que: 1 < 2 = $(1 < 2)\n")
print("Operador menor o igual que: 1 <= 2 (≤) = $(1 <= 2)\n")
print("Operador mayor que: 10 > 2 = $(10 > 2)\n")
print("Operador mayor o igual que: 10 >= 2 (≥) = $(10 >= 2)\n")

print("\n\n*****ESTRUCTURAS DE CONTROL*****\n\n")

println("Evaluación Condicional")
x = 5
y = 10
println("x = $x y = $y")
if x < y
    println("x es menor que y")
elseif x > y
    println("x es mayor que y")
else
    println("x es igual a y")
end

println("")
println("Ciclos")

println("")
println("Ciclo While")
i = 1
while i <= 3
    println(i)
    global i += 1
end 

println("")
println("Ciclo for")
for i = 1:3
    println(i)
end

println("Usando in")
for i in [1,4,0]
    println(i)
end

println("Usando ∈")
for s ∈ ["foo","bar","baz"]
    println(s)
end

println("")
println("Uso de Break")
i = 1
println("Con while")
while true
    println(i)
    if i >= 3
        break
    end
    global i += 1
end
println("Con for")
for j = 1:1000
    println(j)
    if j >= 3
        break
    end
end

print("\n\n*****LA SENTENCIA Try/catch*****\n\n")
try
    sqrt("ten")
catch e
    println("Debía haber ingresado un valor numérico")
end

print("\n\n*****RETO EXTRA*****\n\n")

for i = 10:55
    if i % 2 == 0 && i != 16 && i % 3 != 0
        println("$(i)")
    end
end
