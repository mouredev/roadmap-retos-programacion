# Comentario en Elixir

# Sitio oficial: https://elixir-lang.org/

# Tipos de datos
# las variables inician con letra minúscula
# Debido a que no se usan las variables se les antepone _ para prevenir warning

# Átomo
_atomo = Cancelado     # Inicia con letra mayúscula
_atomo2 = :cancelado   # Anteponiendo los dos puntos (:)

# Booleanos o lógicos
_verdadero = true
_verdadero2 = :true
_falso = false
_falso2 = :false

# Valor nulo nil o ausencia de tipo
_nulo = nil
_nulo2 = :nil

# Números
_entero = 5
_real = 10.0
_octal = 0o10
_binario = 0b1010
_hexadecimal = 0xff
_numero_grande = 1_000_000_000

# Listas
_lista = [1, 2, 3, 4, 5]

# Listas de Caracteres
# Tipo específico de lista.  Lista homogénea de elementos representables
# como caracteres
_lista_caracteres = 'Hola'  # Comilla sencilla

# Cadenas de texto
_cadena = "Cadena de Texto" # Comillas dobles
saludo = "Hola"
lenguaje = "Elixir"

IO.puts "¡#{saludo}, #{lenguaje}!"
