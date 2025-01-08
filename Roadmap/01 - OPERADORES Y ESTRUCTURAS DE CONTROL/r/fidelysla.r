# * EJERCICIO:
#  * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
#  *   Aritméticos, lógicos, de comparación, asignación, identidad,
#  *   pertenencia, bits...
#  *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)

#  * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
#  *   que representen todos los tipos de estructuras de control que existan
#  *   en tu lenguaje:
#  *   Condicionales, iterativas, excepciones...
#  * - Debes hacer print por consola del resultado de todos los ejemplos.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Crea un programa que imprima por consola todos los números comprendidos
#  * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
#  *
#  * Seguro que al revisar detenidamente las posibilidades has
#  * descubierto algo nuevo.

# ? TIPOS DE OPERADORES

# **Operadores de asignación (<-) **

x <- 2
# 2 -> i
s <- "Hola"
v <- c(1:10)
m <- matrix(c(1, 2, 3, 4), nrow = 2, ncol = 2)
l <- list(a = 1, b = 2, c = 3)
f <- factor(c("a", "b", "c"))
df <- data.frame(a = 1, b = 2, c = 3)
obj <- function(x) {
    return(x + 1)
}
ad <<- 12 # Asignación lexicográfica izquierda (avanzado)


# **Operadores Aritmeticos**

num1 <- 3
-num1 # -3

num1 + num1
num1 - num1
num1 * num1
num1 / num1
num1^num1
num1**num1

12 %% 5 # Módulo
5 %/% 3 # División entera

a <- matrix(c(1, -2, 3), nrow = 1)
b <- matrix(c(4, 5, 6))
a %*% b # Multiplicación matricial

a <- c(1, 2, 3)
b <- c(4, 5)
a %o% b # Producto Externo

w <- matrix(c(1, 2, 3, 1), nrow = 2, byrow = TRUE)
z <- matrix(c(0, 3, 2, 1), nrow = 2, byrow = TRUE)
w %x% z # Producto Kronecker
a %x% b # Producto Kronecker

# **Operadores de comparacion**

3 > 5 # FALSE
3 < 5 # TRUE
3 >= 5 # FALSE
3 <= 5 # TRUE
3 == 5 # FALSE
3 != 5 # TRUE

1:10 > 5

x <- c(12, 4, 14)
y <- c(3, 4, 15)

x >= y # TRUE TRUE FALSE
x <= y # FALSE TRUE TRUE
x == y # FALSE TRUE FALSE
x != y # TRUE FALSE  TRUE


# **Operadores Logicos**

3 | 4 # TRUE
40 & 5 > 30 # FALSE
40 | 5 > 30 # TRUE
!TRUE # FALSE
!FALSE # TRUE
!5 # FALSE

# ** & y | **
# Estos operadores son vectorizados y realizan operaciones
# elemento por elemento en vectores lógicos. Devuelven un
# vector lógico del mismo tamaño que los vectores de entrada.
# Si tienes dos vectores lógicos a y b, a & b realizará la
# operación AND elemento por elemento, y a | b realizará la
# operación OR elemento por elemento.

# ** && y || **
# Estos operadores son escalares y evalúan solo el primer
# elemento de cada vector lógico. Devuelven un único valor lógico.
# a && b evaluará como TRUE solo si tanto el primer elemento
# de a como el primer elemento de b son TRUE.
# a || b evaluará como TRUE si al menos uno de los primeros
# elementos de a o b es TRUE.

x <- c(3, 4, 5)
y <- c(3, 5, 1)

x & y # TRUE TRUE TRUE
x | y # TRUE TRUE TRUE

x && y # TRUE
x || y # TRUE

!x # FALSE FALSE FALSE
xor(x, y) # FALSE FALSE FALSE


# **Operadores Miscelaneos**

4 %in% c(1, 2, 3)

df <- data.frame(x = c(7, 9, 2), y = c(5, 9, 5))
# Accedemos a la variable x ($)
df$x

# Secuencia de 1 a 5 (:)
1:5

# Función rnorm del paquete stats (::)
stats::rnorm(10)

# Fórmula modelo lineal (~)
lm(df$x ~ df$y)

# %>% (Se utiliza para encadenar operaciones en un flujo más legible)
# %<>% (Se utiliza para asignar y actualizar una variable en un solo paso),
# ?mean (Se utiliza para obtener información de ayuda sobre un objeto o función)


# ? Ejemplos de tipos de estructuras de control

# ! **Condicionales**

#* If-else

is_string <- TRUE
is_num <- FALSE

if (is_string && is_num) {
    print("Son tipos de datos verdaderos")
} else if (is_string || is_num) {
    print("Por lo menos uno es tipo de dato verdadero")
}

if (15 > 16) {
    print("Consola 1")
} else if (15 < 16) {
    print("Consola 2")
}

#* Switch
day <- as.POSIXlt(Sys.Date())$wday
switch(day,
    "1" <- print("Hoy es Lunes"),
    "2" <- print("Hoy es Martes"),
    "3" <- print("Hoy es Miércoles"),
    "4" <- print("Hoy es Jueves"),
    "5" <- print("Hoy es Viernes"),
    "6" <- print("Hoy es Sábado"),
    "7" <- print("Hoy es Domingo"),
)

# ! **Ciclos**

#* For

for (i in c(0:10)) {
    if (i %% 2 == 0) {
        print(i)
    }
}

abc <- c("a" = 1, "b" = 2, "c" = 3)
for (key in names(abc)) {
    value <- abc$key
    r <- sprintf("%s: %d", key, value)
    cat(r, sep = "\n")
}

arr1 <- c("a", "b", "c", "d", "e")
for (el in arr1) {
    print(el)
}

for (index in seq_along(arr1)) {
    value <- arr1[[index]]
    out <- sprintf("Index: %d, Value: %s", index, value)
    print(out)
}


#* While
# Numeros entre 10 y 55 (incluidos), pares, y que no son ni
# el 16 ni múltiplos de 3.

num3 <- 10
while (num3 <= 55) {
    if (num3 %% 3 == 0 || num3 == 16) {

    } else {
        print(num3)
    }
    num3 <- num3 + 2
}

# Otra forma de hacer lo mismo en r
sequencia <- seq(from = 10, to = 55, by = 2)
numeros_deseados <- sequencia[!(sequencia %% 3 == 0 | sequencia == 16)]


# **Manejo de Errores**

x <- 5
y <- 0

tryCatch({
    resultado <- x / y
    cat("Resultado:", resultado, "\n")
}, error = function(e) {
    if (inherits(e, "try-error") && grepl(
        "non-numeric argument to binary operator",
        conditionMessage(e)
    )) {
        cat("Error: División por cero!\n")
    } else {
        # Manejo de otros errores que no sean división por cero
        stop(e)
    }
}, finally = {
    cat("Ejecutando la cláusula finalmente\n")
})
