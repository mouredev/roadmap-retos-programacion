### Operadores en Julia

# Operadores aritméticos
a = 14
b = 3

suma = a + b
resta = a - b
multiplicacion = a * b
division::Float32 = a / b
division_entera::Int32 = a ÷ b
modulo::Int32 = a % b
potencia = a ^ b

println("Operadores aritméticos:")
println("a = $a, b = $b")
println("a + b = $suma")
println("a - b = $resta")
println("a * b = $multiplicacion")
println("a / b = $division")
println("a ÷ b = $division_entera")
println("a % b = $modulo")
println("a ^ b = $potencia") 

# Operadores de comparación
println("\nOperadores de comparación:")
println("a es igual a b: $(a == b)")
println("a es distinto de b: $(a != b)")
println("a es mayor que b: $(a > b)")
println("a es menor que b: $(a < b)")
println("a es mayor o igual que b: $(a >= b)")
println("a es menor o igual que b: $(a <= b)")

# Operadores lógicos
x = true
y = false
println("\nOperadores lógicos:")
println("x = $x, y = $y")
println("x AND y: $(x && y)")
println("x OR y: $(x || y)")
println("NOT x: $(!x)")

# Operadores de asignación (=)
println("\nOperadores de asignación:")
c = 20
println("c después de la asignación inicial: c = $c")
c += 5  # c = c + 5
println("c después de la nueva asignación: c = $c")

# Operador de identidad (===)
d = [1, 2, 3]
e = d
f = copy(d)
println("\nOperador de identidad:")
println("d es e: $(d === e)")  # Verdadero, porque e es una referencia a d
println("d es f: $(d === f)")  # Falso, porque f es una copia de d

# Operador de pertenencia
println("\nOperador de pertenencia:")
println("1 está en d: $(1 in d)")
println("4 está en d: $(4 in d)")

# Operadores de bits
g = 0b00001010  # 10 en binario
h = 0b00001100  # 12 en binario
println("\nOperadores de bits:")
print("g = $(string(g, base=2)), ")
println("h = $(string(h, base=2))")
println("g AND h: $(string(g & h, base=2))")  
println("g OR h: $(string(g | h, base=2))")   
println("g XOR h: $(string(g ⊻ h, base=2))")  
println("NOT g: $(string(~g, base=2))")        
println("NOT h: $(string(~h, base=2))")  

### Estructuras de control en Julia

## Estructuras de control condicionales en Julia
println("\nEstructuras de control condicionales:")

# Condicional simple
if a > b
    println("a es mayor que b")
else
    println("a no es mayor que b")
end

# Condicional compuesto con elseif
if x < y
    println("x es menor que y")
elseif x == y
    println("x es igual a y")
else
    println("x es mayor que y")
end

# Condicional con operadores lógicos
if x < 20 && x > 10
    println("x está entre 10 y 20")
else
    println("x no está entre 10 y 20")
end

# Simulación de un switch usando if-elseif-else 
day = 3
println("día = $day")
print("Hoy es ")
if day == 1
    println("lunes")
elseif day == 2
    println("martes")
elseif day == 3
    println("miércoles")
elseif day == 4
    println("jueves")
elseif day == 5
    println("viernes")
elseif day == 6
    println("sábado")
elseif day == 7
    println("domingo")
else
    println("día NO VÁLIDO !!!")
end

## Estructuras de control iterativas en Julia
println("\nEstructuras de control iterativas:")

# Bucle for con un rango específico
println("\nBucle for con un rango específico")
for i in 10:15
    println("Número: $i")
end

# Bucle for sobre un array
println("\nBucle for sobre un array")
nombres = ["Ana", "Luis", "Pedro"]
for nombre in nombres
    println("Hola, $nombre")
end

# Bucle while
println("\nBucle while")
contador = 1
while contador <= 5
    println("El contador es: $contador")
    global contador += 1  
end

# Manejo de excepciones
println("\nManejo de excepciones:")
try
    error("Esto es un error de prueba")
catch exception
    println("Se capturó una excepción: $exception")
end

# DIFICULTAD EXTRA: Números entre 10 y 55, pares, no 16 ni múltiplos de 3
println("\nNúmeros entre 10 y 55, pares, no 16 ni múltiplos de 3:")
for n in 10:55
    if n % 2 == 0 && n != 16 && n % 3 != 0
        println(n)
    end
end
