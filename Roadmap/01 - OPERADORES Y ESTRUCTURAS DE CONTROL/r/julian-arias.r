#EJERCICIO 01 - OPERADORES Y ESTRUCTURAS DE CONTROL

# 1. Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:  Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits... (Ten en cuenta que cada lenguaje puede poseer unos diferentes)

# Operadores ariméticos

print(paste("Suma:",10 + 5))
print(paste("Resta:",10 - 5))
print(paste("Multiplicación:",10 * 5))
print(paste("División:",10 / 5))
print(paste("Modulo:",10 %% 7))
print(paste("Exponente", 10 ** 3))
print(paste("Raíz cuadrada:", sqrt(25)))
print(paste("Raíz cubíca:", raiz_nesima(2)))
print(paste("División entera", 400 %/% 6))

raiz_nesima <- function(x) {
  return(x ^ (1/3))
}

# Operadores de comparación

x <- 35
y <- 88

print(paste("Igualdad, x == y es:", x == y))
print(paste("Desigualdad, X != y es:", x != y))
print(paste("Mayor que, X > y es:", x > y))
print(paste("Mayor igual que, X >= y es:", x >= y))
print(paste("Menor que, X < y es:", x < y))
print(paste("Menor igual que , X <= y es:", x <= y))

# Operadores lógicos

print(paste("AND or && es:", (x < y) && (y %% 2 ==0)))
print(paste("OR or | es:", (x > y) | is.character(y)))
print(paste("NOT or ! es:", !(x < y)))

# Operador de asignación

z <- "Julián"
z

# En R no existen operadores de asignación combinados como =+, =-, =*, =/, entre otros.

# Operador de identidad

a <- 5
b <- 5.0

a == b  # Se valida una igualdad, que son igual valor, devuelve True

identical(5,5.1)  # Se valida que es una identidad, en este caso No son identicos porque el primer elemento es 5 y el otro es 5.1. Devuelve False

# Operadores de pertenencia

a1 <- 10    # Comparando un elemento de a1 contra los elementos de b1, devuelve TRUE
b1 <- c(78,10)

if (a1 %in% b1) {
  print("a1 pertenece a b1")
} else {
  print("a1 no pertenece a b1")
}

a2 <- c(10,8,23)  # Comparando todos los elementos de a2 con los de b2, devuleve FALSE
b2 <- c(78,10)

if (all(a2 %in% b2)) {
  print("a2 pertenece a b2")
} else {
  print("a2 no pertenece a b2")
}

# 2. Utilizando las operaciones con operadores que tú quieras, crea ejemplos que representen todos los tipos de estructuras de control que existan en tu lenguaje:   Condicionales, iterativas, excepciones. Debes hacer print por consola del resultado de todos los ejemplos.

# Estructuras de control

# Condicionales

edad3 <- 80

if (edad3 < 18) {
  print(paste("Es menor de edad y tiene",edad3,"años"))
} else if (edad3 >= 18 && edad3 <= 60){
  print(paste("Es adulto y tiene",edad3,"años"))
} else {
  print(paste("Es adulto mayor y tiene",edad3,"años"))
}

# Iterativos

for (p in LETTERS) {
  print(p)
}

p <- 0

while (p <= 10) {
  print(p)
  p <- p + 1
}

# Manejo de excepciones

x2 <- 10/0
x2

tryCatch(
  {
    x2 <- 10 / 0
    print(x2)
  },
  warning = function(w){
    print("Ocurrió un error en la división")
    invokeRestart("muffleWarning")
  }
)

# DIFICULTAD EXTRA (opcional):
# Crea un programa que imprima por consola todos los números comprendidos
# entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.

for (j in 10:55) {
  if (j %% 2 == 0 & j != 16 & j %% 3 == 0) {
    print(j) 
  }
}


