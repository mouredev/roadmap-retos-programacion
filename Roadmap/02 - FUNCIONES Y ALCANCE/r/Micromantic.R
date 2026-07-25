#
  # EJERCICIO:
# - Crea ejemplos de funciones básicas que representen las diferentes
#   posibilidades del lenguaje:
#   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
# - Comprueba si puedes crear funciones dentro de funciones.
# - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
# - Pon a prueba el concepto de variable LOCAL y GLOBAL.
# - Debes hacer print por consola del resultado de todos los ejemplos.
#   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)


#### Funciones definidas por el usuario

# Simple

saludar <- function() {
  print("¡Hola, R!")
}

saludar()

# Con retorno

saludar_con_retorno <- function() {
  return("¡Hola, R!")
}

print(saludar_con_retorno())

saludo <- saludar_con_retorno()

saludo

# Con un argumento

saludar_con_argumento <- function(x) {
  cat("¡Hola, ", x,"!", sep = "")
}

saludar_con_argumento("Micromantic")

# Con dos argumentos

saludar_con_argumentos <- function(x, y) {
  cat("¡", x, ", ", y, "!", sep = "")
}

saludar_con_argumentos("Buenas", "Micromantic")

# Con un argumento por defecto

saludar_con_argumento_por_defecto <- function(x = "R") {
  cat("¡Hola, ", x,"!", sep = "")
}

saludar_con_argumento("Micromantic")

# Con dos argumentos por defecto

saludar_con_argumentos_por_defecto <- function(x = "Hola" , y = "R") {
  cat("¡", x, ", ", y, "!", sep = "")
}

saludar_con_argumentos("Buenas", "Micromantic")

# Con retorno de varios valores

saludar_con_multiple_retorno <- function() {
  
  return(c("Hola", "R"))
}

saludar_con_multiple_retorno()

saludo <- saludar_con_multiple_retorno()[1]
lenguaje <- saludar_con_multiple_retorno()[2]

saludo
lenguaje

# Con un número variable de argumentos

saludo_con_argumentos_variables <- function(...) {
  for (i in list(...)) {
    print(paste0("Hola, ", i))
    
  }
}

saludo_con_argumentos_variables("Carlos", "Daniel")

# Con un número variable de argumentos con palabras clave

saludo_con_argumentos_variables_clave <- function(...) {
  
  claves <- list(...)
  for (clave in names(claves)) {
    cat("Hola,", "mi", clave, "es", claves[[clave]], "\n")
  }
}

saludo_con_argumentos_variables_clave(
  nombre = "Daniel",
  lenguaje = "R",
  apodo = "Micromantic",
  edad = "30"
  )

# Función dentro de otra función

por_100 <- function(x) {
  
  y <- x * 100
  
  por_5 <- function(y) {
  resultado <- (y * 5)
  return(resultado)
  }
  print(por_5(y))
}

por_100(x = 1)

# esta funcion recibe un argumento, lo multiplica por 100 y luego usa una
# función interna para multiplicar el resultado por 5

#### Funciones del lenguaje R

### Funciones sin retorno

## Con parametros

rm(list = ls())

# Al ser aplicada de esta manera, la función rm borra todos los objetos del environment

## Sin parametros

graphics.off()

# graphics.off cierra todos los dispositivos gráficos abiertos (por ejemplo, las visualizaciones en el panel Plots)

### Funciones con retorno

## Con parametros

sum(2, 2)

## Sin parametros

Sys.Date()

# la función Sys.Date arroja la fecha actual en el formato "YYYY-MM-DD"


### Concepto de alcance LOCAL y GLOBAL

# Al definir la función por_5 dentro de la función por_100, ya estamos explorando el concepto de alcance LOCAL y GLOBAL.
# La función por_5 está definida dentro del alcance local de la función por_100.
# Eso quiere decir que no se puede llamar la función por_5() en ninguna otra parte del script
# En cambio, cuando se definen objetos fuera de funciones, estos se guardan en el ambiente global,
# esos objetos sí pueden llamarse en cualquier parte del script.

por_100 <- function(x) {
  
  y <- x * 100
  
  por_5 <- function(y) {
    resultado <- (y * 5)
    return(resultado)
  }
  print(resultado)
  print(por_5(y))
}

# por_100 está en el ambiente global
# las variables "y", y la función "por_5" están en el ambiente local de la función "por_100"
# la variable "resultado" está en el ambiente local de la función "por_5"




# DIFICULTAD EXTRA (opcional):
# Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
# - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
#   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
#   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
#   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
#   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
#
# Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
# Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.


imprimir_numeros <- function(x, y) {
  vector <- 1:100
  multiplos_3_5 <- c()
  
  for (i in vector) {
    if(i %% 3 == 0 & i %% 5 == 0) {
      print(paste0(x, y, sep = " "))
      } else if(i %% 3 == 0) {
        print(x)
        } else if(i %% 5 == 0) {
          print(y)
          } else { 
            print(i)
            multiplos_3_5 <- c(multiplos_3_5, i)
            }
  }
  multiplos_3_5
  paste0("Hubo un total de ", length(multiplos_3_5), " números impresos en vez de textos.")
}

imprimir_numeros("Fizz", "Buzz")
