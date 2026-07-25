#
  # EJERCICIO:
# Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
# en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
# - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
#   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
#

## Operaciones con cadenas de caracteres

# Concatenación

cat("Hola,", "R")

# Repeticion

strrep("Hola, R.", 3)

# Longitud de una cadena de caracteres

nchar("Murcielago")

# Subcadenas

substr("Murcielago", start = 4, stop = 8)
substr("Murcielago", 4, 7)

# Cambio de mayúsculas/minúsculas

toupper("Murcielago")
tolower("MURCIELAGO")
tools::toTitleCase("murcielago")

# Eliminación de espacios al principio y al final

trimws(" Murcielago en el ático.        ")

# Reemplazo de patrones
# gsub cambia el patrón en todas las ocasiones, mientras que sub solamente la primera vez

sub(x = "Murcielago en el lago", pattern = "la", replacement = "ga")

gsub(x = "Murcielago en el lago", pattern = "la", replacement = "ga")

# Dividir cadenas

strsplit(x = c("1,2,3,4,5"), split = ",")

strsplit(x = c("Murcielago en el lago"), split = " ")

# Buscar patrones

# grep devuelve la posición donde se cumple el patrón de la regex
grep("[a-z]", c("123", "b"))

grep("[a-z]", c("12d3", "b"))

# grepl devuelve si el patrón se cumple o no

grepl("[a-z]", c("123", "b"))

grepl("[a-z]", c("12d3", "b"))

# Coincidencias de patrones

# regexpr indica la posición del patrón en la primera aparición
regexpr(c("Murcielago en el lago"), pattern = "el")

# gregexpr indica la posición del patrón en todas las repeticiones 
gregexpr(c("Murcielago en el lago"), pattern = "el")

# Formateo de texto

s1 <- "Hola"
s2 <- "R"

sprintf("Saludo: %s, lenguaje: %s!", s1, s2)



# DIFICULTAD EXTRA (opcional):
# Crea un programa que analice dos palabras diferentes y realice comprobaciones
# para descubrir si son:
# - Palíndromos
# - Anagramas
# - Isogramas
#

analizar_palabras <- function(x, y) {
  
  x_lower <- tolower(x)
  y_lower <- tolower(y)
  
  x_letras <- unlist(strsplit(x_lower, split = ""))
  y_letras <- unlist(strsplit(y_lower, split = ""))
  
  x_inversa <- rev(x_letras)
  y_inversa <- rev(y_letras)
  
  x_sorted <- sort(x_letras)
  y_sorted <- sort(y_letras)
  
  x_unique <- unique(x_sorted)
  y_unique <- unique(y_sorted)
  
  verificar_palindromo <- function(palabra, letras, letras_inv) {
    
    if (all(letras == letras_inv)) {
    cat("La palabra", palabra, "es un palíndromo.\n")
    } else cat("La palabra", palabra, "no es un palíndromo.\n")
  }
  
  verificar_palindromo(x, x_letras, x_inversa)
  verificar_palindromo(y, y_letras, y_inversa)
  
  if (length(x_sorted) == length(y_sorted) && all(x_sorted == y_sorted)) {
    cat("Las palabras", x, "y", y, "son anagramas.\n")
    } else cat("Las palabras", x, "y", y, "no son anagramas.\n")
  
  verificar_isograma <- function(palabra, letras_ord, letras_uniq) {
    
    if (length(letras_ord) == length(letras_uniq)) {
      cat("La palabra", palabra, "es un isograma.\n")
      } else if (sum(table(letras_ord)) / length(table(letras_ord)) == table(letras_ord)[[1]]) {
        cat("La palabra", palabra, "es un isograma.\n")
        } else cat("La palabra", palabra, "no es un isograma.\n")
  }
  
  verificar_isograma(x, x_sorted, x_unique)
  verificar_isograma(y, y_sorted, y_unique)
}

analizar_palabras("Roma", "Amor")
analizar_palabras("arepera", "salas")

