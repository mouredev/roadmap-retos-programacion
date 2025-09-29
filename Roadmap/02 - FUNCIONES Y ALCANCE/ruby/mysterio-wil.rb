#
# EJERCICIO:
# - Crea ejemplos de funciones básicas que representen las diferentes
#   posibilidades del lenguaje:
#   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
# - Comprueba si puedes crear funciones dentro de funciones.
# - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
# - Pon a prueba el concepto de variable LOCAL y GLOBAL.
# - Debes hacer print por consola del resultado de todos los ejemplos.
#   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
#
# DIFICULTAD EXTRA (opcional):
# - Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
# - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
# - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
# - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
# - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
# - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
#
# Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
# Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
#

# --- Variable Global ---
$global_var = "Soy una variable global"

puts "===> Funciones (métodos) básicas <==="

# Sin parámetros ni retorno
def greet
    puts "Hola, Ruby!"
end
greet

# Con un parámetro
def greet_person(name)
    puts "Hola, #{name}!"
end
greet_person("Wilmer")

# Con varios parámetros
def add(a, b)
    puts "La suma de #{a} y #{b} es #{a + b}"
end
add(5, 3)

# Con retorno (en Ruby, el retorno es implícito)
def multiply(a, b)
    a * b
end
result = multiply(5, 3)
puts "El resultado de la multiplicación es #{result}"

# Con parámetros por defecto
def greet_default(name, greeting = "Hola")
    puts "#{greeting}, #{name}!"
end
greet_default("MoureDev")
greet_default("Wilmer", "Hello")

# Con parámetros de longitud variable (splat operator)
def print_args(*args)
    puts "Argumentos variables (*args, a.k.a. splat operator):"
    args.each do |arg|
        puts "- #{arg}"
    end
end
print_args(1, "texto", true, [1, 2])


puts "\n===> Funciones dentro de funciones (Lambdas) <==="
def outer_function
    puts "Esta es la función externa."
    # Ruby no tiene funciones anidadas directamente, pero usa lambdas o procs.
    inner_function = -> { puts "Esta es una función lambda (interna)." }
    inner_function.call
end
outer_function


puts "\n===> Métodos del core de Ruby <==="
my_list = [1, 2, 3, 4, 5]
puts "Usando el método .length de un Array: El array tiene #{my_list.length} elementos."
puts "Usando el método .max de un Array: El valor máximo es #{my_list.max}."


puts "\n===> Variable LOCAL y GLOBAL <==="
def my_function_scope
    local_var = "Soy una variable local"
    # Las variables globales ($) son accesibles directamente desde cualquier scope.
    puts $global_var
    puts local_var
end
my_function_scope

def modify_global
    $global_var = "He modificado la variable global"
end

puts "Antes de modificar: #{$global_var}"
modify_global
puts "Después de modificar: #{$global_var}"


#
# DIFICULTAD EXTRA (opcional):
#
puts "\n====> DIFICULTAD EXTRA <===="
def fizz_buzz_extra(text1, text2)
    count = 0
    (1..100).each do |i|
        is_multiple_of_3 = (i % 3 == 0)
        is_multiple_of_5 = (i % 5 == 0)

        if is_multiple_of_3 && is_multiple_of_5
            puts "#{text1}#{text2}"
        elsif is_multiple_of_3
            puts text1
        elsif is_multiple_of_5
            puts text2
        else
            puts i
            count += 1
        end
    end
    return count
fizz_buzz_extra("Fizz", "Buzz")
puts "\nEl número se imprimió un total de #{times_printed_number} veces."
