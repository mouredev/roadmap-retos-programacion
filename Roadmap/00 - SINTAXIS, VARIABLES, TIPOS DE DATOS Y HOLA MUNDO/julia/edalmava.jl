# Comentario de una línea en Julia

#=
   Comentario de varias líneas en Julia
=#

#=
   Sitio oficial: https://julialang.org/
   Documentación: https://docs.julialang.org/en/v1/
=#

# Expresiones de Asignación
# variable = valor

# Tipos Primitivos

# Tipos Enteros
ent = 10                # Int32 o Int64 según el sistema
ent = 3000000000        # Int64
# - Hexadecimales
hex = 0x1               # UInt8
hex = 0x123             # UInt16
hex = 0x1234567         # UInt32
hex = 0x123456789abcdef # UInt64
# - Binarios 
bin = 0b10
# - Octales
oct = 0o010
# - Booleanos
verdadero = true        # (1)
falso = false           # (0)

# Tipo Punto Flotante
flo = 1.0               # Float64
flo = -1.23             # Float64
flo = 1e10              # Float64
flo = 2.5e-4            # Float64

flo = 0.5f0             # Float32 - se cambia e por f

# - Valores especiales de Punto Flotante
infinito_positivo = Inf
infinito_negativo = -Inf
Not_a_Number = NaN

# Strings
# - Tipo Char
car = 'X'
unicode = '\u78'       # Unicode \u seguido por los 4 digitos hexadecimales 
unicode = '\U10ffff'   # o \U seguido por los 6 u 8 digitos hexadecimales
# - Cadenas Básicas
lenguaje = "Julia"

# Constantes 
const gravedad = 9.8
const a, b = 1, 2

#print("¡Hola, ", lenguaje, "!")  # Usando concatenación
print("¡Hola, $(lenguaje)!")      # Usando interpolación
