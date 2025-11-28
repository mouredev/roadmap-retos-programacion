# Sitio web oficial de Julia: https://julialang.org

# Comentario de una sola línea en Julia

#=
Julia soporta la escritura de comentarios 
en múltiples líneas
=#

# También soporta comentarios a continuación de un comando
d = 17 # asigné a la variable a el valor 17


# Declaración de una variable
variable_texto = "Cadena de texto"

# Se pueden asignar multiples variables de la siguiente forma
a = (b = 2 + 2) + 3

# Julia también soporta caracteres Unicode como nombre de variable
α = 30
Η = 3.14

# Julia soporta declaración de constantes. 
const c = 3.14159 

# Tipos de datos primitivos 

#Enteros
numero_entero_64b::Int = 64 # Int es por default un entero de 64bits
numero_entero_64bU::UInt = 64 # es un entero de 64bits sin signo, lo que permite obtener un entero mayor
#=
También existen Int16, Int32, Int64 e Int128
y las mismas opciones con UInt
Por ejemplo el entero más grande con Int128 es 2^127 - 1
y con UInt128 2^128 - 1
=#

#Reales
numero_flotante::Float64 = 64.10 # Float64
# Existe la posibilidad de trabajar con precisión media Float16 o con simple Float32


cadena_de_texto::String = "Hola mundo" # String


booleano::Bool = true # Bool


# Imprimir a la terminal al REPL Hola Julia
lenguaje_de_programacion = "Julia"
print("¡Hola, $(lenguaje_de_programacion)!") 

