#=
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */
=#

# Operadores aritméticos 
using Printf
x = 3;
y = 2;

print(" * * * * * * * * * * * * * * * \n");
print("Operadores aritméticos \n");
print(" * * * * * * * * * * * * * * *\n");

@printf "variables x = %d, y = %d \n" x y;

@printf "Suma x+y = %d \n" x+y;

@printf "Resta x+y = %d \n" x-y;

@printf "Multiplicación x*y = %d \n" x*y;

@printf "División decimal x/y = %0.4f \n" x/y; #4 decimales

@printf "Cociente de la división x/y = %d \n" x÷y; # Por medio de \div + tab se coloca el signo

@printf "Residuo de la división x/y = %d \n" x%y; # también es posible usando rem(x,y)

@printf "División inversa y/x = %f \n" x\y;

@printf "Potencia x^y = %d \n" x^y;

print(" * * * * * * * * * * * * * * *\n");
a = true;
b = false;
print("Operadores booleanos \n");
print(" * * * * * * * * * * * * * * *\n");

@printf "variables a = %s, b = %s \n" a b;

@printf "Operación AND(a,b): %s \n" a&&b;

@printf "Operación OR(a,b): %s \n" a||b;

@printf "Negación !a: %s \n" !a;

print(" * * * * * * * * * * * * * * *\n");
print("Operadores de comparación \n");
print(" * * * * * * * * * * * * * * *\n");

@printf " 3 == 0: %s \n" 3==0; # también puede teclearse el comando isequal(a,b)

@printf " 3 ≠ 0: %s \n" 3 ≠ 0; # para el signo no igual se teclea \ne + tab, el mismo operador es ! =  

@printf " 3 > 0: %s \n" 3 > 0 ; 

@printf " 3 < 0: %s \n" 3 < 0;

print(" * * * * * * * * * * * * * * *\n");
print("Operadores de asignación \n");
print(" * * * * * * * * * * * * * * *\n");

@printf "variables x = %d, y = %d \n" x y;

@printf "Suma + asignación x+=2: %d \n" x+=2;

@printf "Resta + asignación y-=2: %d \n" y-=2;

x = 3; y = 2;

@printf "Multiplicación + asignación: x*=2 %d \n" x*=2;

@printf "División + asignación: y/=2 %0.2f \n" y/=2;


print(" * * * * * * * * * * * * * * *\n");
print("Operadores a nivel bit (bitwise) \n");
print(" * * * * * * * * * * * * * * *\n");

@printf "Not ~123 = %d \n" ~123;

@printf "And 1 & 2 = %d \n" 1&2;

@printf "Or 1 | 2 = %d \n" 1|2;

@printf "XOR 1 ⊻ 2 = %d \n" 1⊻2; #símbolo \xor + TAB o xor(1,2)

@printf "NAND 1 ⊼ 2 = %d \n" 1⊼2; #símbolo \nand + TAB o nand(1,2)

print(" * * * * * * * * * * * * * * *\n");
print("Estructuras de control \n");
print(" * * * * * * * * * * * * * * *\n");

print("Expresiones compuestas \n");
# Una expresión compuesta evalúa dos o más expresiones en conjunto
# En este caso evaluaremos x^2+y^2 en conjunto
begin #inicio de la expresión
    x=3; y=4;
    x^2+y^2;
    z=√x; # \sqrt para el operador raíz cuadrada 
end # fin de la expresión

@printf "Expresión compuesta caso 1: sqrt(x^2+y^2) = %d \n" z;

# Otra forma de escribir la expresión
z = (x=3; y=4; x^2+y^2; r=√x);

@printf "Expresión compuesta caso 2: sqrt(x^2+y^2) = %d \n" z;

print("Condicionales \n");

x = -3;
if x>0
    println("El número x es positivo");
else
    println("El número x es negativo");
end

# Otra forma de usar Condicionales
#= con el comando ? se puede evaluar una expresión, se agrega el caso
 positivo y el caso negativo separados por un ":" =#
println(x>0 ? "x es mayor a cero" : "x no es mayor a cero"); #debe haber espacio entre ":"

x = 0;
# Condicional múltiple
function test(x)
    if x<0
        println("X es menor que cero");
    elseif x==0
        println("x es igual a cero");
    else
        println("x es menor que cero");
    end
end
test(x);

println("Ciclo while");

j=1;
while j<=5
    println(j);
    global j +=1; #nueva sintaxis para asignar j en el contexto global
end

for r=1:3
    @printf "r = %d\n" r;
end

# For each en Julia:
l = ["hola","somos","strings","desde","un","array"];

for str_text ∈ l #para el signo se teclea \in + TAB 
    println(str_text);
end

# También existe el método zip como en Python
for (f,g) in zip([0,1,2],[3,4,5])
    println((f,g))
end

print(" * * * * * * * * * * * * * * *\n");
print("Excepciones \n");
print(" * * * * * * * * * * * * * * *\n");

# Excepciones de dominio
f(x) = x>0 ? 1/x : throw(DomainError(x,"El argumento debe ser mayor a cero"))
#f(-1)
f(4)
#println(4)

# Excepciones "custom"
try
    sqrt("one")
catch e
    println("Error: El valor a ingresar debe ser numérico");
end
print(" * * * * * * * * * * * * * * *\n");
print("DIFICULTAD EXTRA \n");
print(" * * * * * * * * * * * * * * *\n");

nums = range(10,step=1,stop=55);

for num ∈ nums
    if num%3!=0 && num%2==0 && num != 16
        println(num)
    end
end