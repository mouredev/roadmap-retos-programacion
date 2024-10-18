#
  # EJERCICIO:
# - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
#   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
#   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
# - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
#   que representen todos los tipos de estructuras de control que existan
#   en tu lenguaje:
#   Condicionales, iterativas, excepciones...
# - Debes hacer print por consola del resultado de todos los ejemplos.
#
  
  # DIFICULTAD EXTRA (opcional):
# Crea un programa que imprima por consola todos los números comprendidos
# entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
#
# Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
#

### Operadores

## Operadores aritméticos:

# Suma 

2 + 2

# Resta

5 - 2

# Multiplicación

7 * 2

# División

21 / 7

# Exponenciación

3 ^ 2

# Módulo

18 %% 2
18 %% 4

# División entera

18 %/% 2
18 %/% 4

## Operadores de asignación:

# Asignación izquierda

esto_es_una_variable <- 5+5
esto_tambien = 4+4

# Asignación derecha

3+3 -> y_esto_tambien

## Operadores de comparación:

# Igual a

5 == 5
"casa" == "casa"
"bueno" == "malo"

# Diferente de

5 != 5
"casa" != "casa"
"bueno" != "malo"

# Mayor que

5 > 5
5 > 4
5 > 3

# Menor que

5 < 5
5 < 4
5 < 3

# Mayor o igual que

5 >= 5
5 >= 4
5 >= 3

# Menor o igual que

5 <= 5
5 <= 4
5 <= 3

## Operadores lógicos

#Y lógico

5 > 4 && 4 %% 2 == 0
5 > 4 && 4 %% 2 != 0

c(5, 2) > c(3, 1) & 4 %% 2 == 0
c(5, 2) > c(3, 1) & 4 %% 2 != 0

#O lógico

5 > 7 || 4 %% 2 == 0
5 > 7 || 4 %% 2 != 0

c(5, 2) > c(3, 1) | 4 %% 2 == 0
c(5, 2) > c(3, 1) | 4 %% 2 != 0

# Negación lógica

!(TRUE)
!(FALSE)
!(5 == 4)
!(5 == 5)

## Operadores de secuencia:

# Crear secuencia

1:10

# Operadores de acceso:

# Acceso a listas o data frames

lista <- list(string = "hola",
              enteros =  1:10,
              booleano = TRUE,
              lista_pequeña = list("chao", 11:20, FALSE))
lista$string

# Subconjuntos y acceso a elementos

lista[1]
lista[[1]]

### Estructuras de control

## De selección

# If

if (3 > 5) {
  print("La condición se cumple")
}

# If y else

if (3 > 5) {
  print("La condición se cumple")
} else {
    print("La condición no se cumple")
  }

# Ifelse

notas <- data.frame(
  materia = c("Matemática I", "Computación I", "Estadística I"),
  nota = sample(1:20, size = 3, replace = TRUE)
)

notas$comentario <- ifelse(notas$nota >= 10,
                           "Aprobado",
                           "Reprobado")

notas

# Switch

mensaje_final <- function(x) {
  comentario <- switch(x,
                       "Aprobado" = "¡Felicitaciones!",
                       "Reprobado" = "Sigue intentando",
                       "No hay información")
  return(comentario)
}

## Iterativas

# For

for (i in 1:5) {
  print(i + 10)
}

# While

i <- 0

while (i < 10) {
  print(i + 1)
  i <- i + 1
}

# Repeat

i <- 0

repeat {
  print(i + 1)
  i <- i + 1
  if (i >= 10) {
    break
  }
}

mensaje_final("Aprobado")
mensaje_final("Reprobado")


# Crea un programa que imprima por consola todos los números comprendidos
# entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
#
  # Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
#

vector <- c()
for (i in 10:55) {
  if (i %% 2 == 0 & i %% 3 != 0 & i != 16) {
    vector <- c(vector, i)
  }
}

vector

