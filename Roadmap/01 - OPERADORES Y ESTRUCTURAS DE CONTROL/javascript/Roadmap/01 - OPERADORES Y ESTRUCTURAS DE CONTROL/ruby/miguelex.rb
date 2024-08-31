# Operadores de asignación

x = 10    
puts ("El valor de x es: #{x}")                  
x += 5
puts ("El valor nuevo valor de x tras sumarle 5 es: #{x}")                         
x -= 5 
puts ("El valor nuevo valor de x tras restarle 5 es: #{x}")                        
x *= 5  
puts ("El valor nuevo valor de x tras multiplicarlo por 5 es: #{x}")                       
x /= 5 
puts ("El valor nuevo valor de x tras dividirlo por 5 es: #{x}")                        
x %= 5 
puts ("El valor nuevo valor de x tras hacerle el módulo 5 es: #{x}")                        
x **= 5   
puts ("El valor nuevo valor de x tras elevarlo a 5 es: #{x}")                  

# Operadores aritmeticos
a = 3
b = 2

puts ("El valor de a es: #{a}")   
puts ("El valor de b es: #{b}")   
puts ("La suma de a + b es: #{a+b}")
puts ("La resta de a - b es: #{a-b}")
puts ("La multiplicación de a * b es: #{a*b}")
puts ("La división de a / b es: #{a/b}")
puts ("El módulo de a % b es: #{a%b}")
puts ("El exponente de a ** b es: #{a**b}")
puts ("La negación de -a es: #{-a}")

# Operadores de comparación
puts ("El valor de a es: #{a}")
puts ("El valor de b es: #{b}")
puts ("a es menor que b: #{a<b}")
puts ("a es mayor que b: #{a>b}")
puts ("a es menor o igual que b: #{a<=b}")
puts ("a es mayor o igual que b: #{a>=b}")
puts ("a es igual que b: #{a==b}")
puts ("a es distinto que b: #{a!=b}")
puts ("operacion combinada a <=> b: #{a<=>b}")
puts ("igualdad de casos a === b: #{a===b}")

# Operadores lógicos
puts ("El valor de a es: #{a}")
puts ("El valor de b es: #{b}")
puts ("a && b: #{a&&b}")
puts ("a || b: #{a||b}")
puts ("!a: #{!a}")

# operadores bit a bit 
puts ("El valor de a es: #{a}")
puts ("El valor de b es: #{b}")
puts ("a & b: #{a&b}")
puts ("a | b: #{a|b}")
puts ("a ^ b: #{a^b}")
puts ("~a: #{~a}")
puts ("a << b: #{a<<b}")
puts ("a >> b: #{a>>b}")

# operador ternario
puts ("El valor de a es: #{a}")
puts ("El valor de b es: #{b}")
puts ("a > b ? a : b --> #{a>b ? a : b}")

# if
puts ("El valor de a es: #{a}")
puts ("El valor de b es: #{b}")
if a>b
    puts ("a es mayor que b")
else
    puts ("a es menor que b")
end

# unless
puts ("El valor de a es: #{a}")
puts ("El valor de b es: #{b}")
unless a>b
    puts ("a es menor que b")
else
    puts ("a es mayor que b")
end

# case
puts ("El valor de a es: #{a}")
puts ("El valor de b es: #{b}")
case a<=>b
when -1
    puts ("a es menor que b")
when 0
    puts ("a es igual que b")
when 1
    puts ("a es mayor que b")
end

# while
puts ("El valor de a es: #{a}")
puts ("El valor de b es: #{b}")
while a<b
    puts ("a es menor que b")
    a+=1
end

# until
puts ("El valor de a es: #{a}")
puts ("El valor de b es: #{b}")
until a>b
    puts ("a es menor que b")
    a+=1
end

# for
puts ("El valor de a es: #{a}")
puts ("El valor de b es: #{b}")
for i in a..b
    puts ("i es: #{i}")
end

# each
puts ("El valor de a es: #{a}")
puts ("El valor de b es: #{b}")
(a..b).each do |i|
    puts ("i es: #{i}")
end

# times
puts ("El valor de a es: #{a}")
puts ("El valor de b es: #{b}")
a.times do |i|
    puts ("i es: #{i}")
end

# break
puts ("El valor de a es: #{a}")
puts ("El valor de b es: #{b}")
while a<b
    puts ("a es menor que b")
    a+=1
    break if a==b
end

# next
puts ("El valor de a es: #{a}")
puts ("El valor de b es: #{b}")
while a<b
    puts ("a es menor que b")
    a+=1
    next if a==b
end

# try catch
puts ("El valor de a es: #{a}")
puts ("El valor de b es: #{b}")
begin
    puts ("a es menor que b")
    a+=1
    raise if a==b
rescue
    puts ("a es igual que b")
end

# throw catch
puts ("El valor de a es: #{a}")
puts ("El valor de b es: #{b}")
catch (:exit) do
    while a<b
        puts ("a es menor que b")
        a+=1
        throw :exit if a==b
    end
end

# Extra

puts("A continuación vamos a mostrar el ejercicio extra")
for i in 10..55
    if (i % 2 == 0) && (i != 16) && (i % 3 != 0)
        puts ("#{i}")
    end
end
