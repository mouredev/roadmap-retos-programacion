# https://elixir-lang.org/#

# Este es un comentario de una línea

# Para comentario multi íneas
# Se usa el símbolo # en cada línea

# La convención en Elixir es snake_case, pero se antepone un _ por recomendacion para las variables no usadas.
_ejemplo_de_variable = 42
# No existen constantes reales en Elixir

# Tipos de datos
entero = 1
_decimal = 3.14
cadena = "Elixir"
_booleano = true
atomo = :elixir
_booleanos_tambien_son_atomos = :true # :false
_lista = [1, 2, 3]
_tupla = {atomo, true, "string", entero}
_mapas = %{:nombre => "Juan", "entero" => entero}

IO.puts("Hola " <> cadena)
