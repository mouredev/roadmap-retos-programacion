# Realizado con https://www.ruby-lang.org/es/
# Comentario de una lína
=begin
  Comentario
  de varias
  líneas
=end

variable = "Una variable"
CONSTANTE = "Una constante"

# En Ruby no hay primitivos, casi todo es un objeto
=begin
Numéricos:
- Integer
    - Fixnum
    - Bignum
- Float
- Complex
- BigDecimal
- Rational
=end
numero = 1_000

=begin
Texto
=end
cadena_de_texto = "Ruby"

# Arrays
un_array = [1, 2, 3]

# Hash
un_hash = { "uno" => 1, "dos" => 2}
otro_hash = { :uno => 1, :dos => 2}
otro_hash_mas = { uno: 1, dos: 2}

# Range
primera_guerra_mundial = 1914..1918   # Entre 1914 y 1918 inclusive
segunda_guerra_mundial = 1939...1946  # Entre 1939 y 1946 (se excluye 1946)

# Symbol
simbolo = :simbolo

# Booleans
verdadero = true
falso = false

# Nulo
nulo = nil

puts "¡Hola, #{cadena_de_texto}!"
