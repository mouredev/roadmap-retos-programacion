# https://www.ruby-lang.org/es/

# *** Diferentes sintaxis de comentarios ***

# 1. Comentario de una línea

lenguaje = 'Ruby'
puts "Hola #{lenguaje}" # 2. Comentario sobre línea de código

=begin
  3. Comentario de
  varías líneas
=end

# *** Declaración de una variable y una constante ***

mi_var = 'Esto es una cadena' # Variable Local

MI_CONST = 3.1416 # Constante

# Alcances de una variable (scope)
=begin
  Nombre comienza con | Alcance variable
  $                   | Variable global
  @                   | Variable de instancia
  @@                  | Variable de clase
  [a-z] o _           | Variable local
  [A-Z]               | Una constante
=end

# *** Tipos de datos ***
# Casi todo en Ruby es un objeto
# Clases Números

mi_entero = 5
mi_float = 5.0

# Cadenas

mi_cadena = 'Esto es una cadena de texto'
mi_cadena = "Esto es otra cadena de texto"

# Booleanos: los valores true y false

verdadero = true
falso = false # En Ruby solo se evalúa a falso el valor false y nil
