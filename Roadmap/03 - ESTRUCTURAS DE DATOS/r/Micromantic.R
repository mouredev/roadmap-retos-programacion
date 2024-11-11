#
# EJERCICIO:
# - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
# - Utiliza operaciones de inserción, borrado, actualización y ordenación.
#

### Estructuras de datos

## Vector

# Creacion

vector_de_numeros <- c(1:10)

vector_de_numeros

# Insercion

vector_de_numeros <- c(vector_de_numeros, 11:20)

vector_de_numeros

# Borrado

vector_de_numeros <- vector_de_numeros[-(5:15)]

vector_de_numeros

# Actualizacion

vector_de_numeros <- vector_de_numeros * 5

vector_de_numeros

# Ordenacion

vector_de_numeros <- sort(vector_de_numeros, decreasing = TRUE)

vector_de_numeros

## Lista

# Creacion

lista <- list(
  string = "hola",
  enteros = 1:10,
  booleano = TRUE,
  lista_pequeña = list("chao", 11:20, FALSE)
)

lista

# Insercion

lista <- list(lista, complejo = 5i)

lista

# Borrado

lista <- lista[-1]

lista

# Actualizacion

lista$booleano <- TRUE

lista

# Ordenacion

lista <- lista[order(unlist(lista), decreasing = TRUE)]

lista

## Data frame

# Creacion

data_frame <- data.frame(
  "Materias" = c(
    "Matematica",
    "Estadistica",
    "Computacion"
  ),
  "Notas" = sample(1:20,
    size = 3,
    replace = TRUE
  )
)
data_frame

# Insercion

data_frame <- cbind(data_frame, "Semestre" = "I")

data_frame

# Borrado

data_frame <- data_frame[1:2]

data_frame

# Actualizacion

data_frame$Notas <- data_frame$Notas / 2

data_frame

# Ordenacion

data_frame <- sort_by(
  x = data_frame,
  y = data_frame$Notas
)

data_frame

## Matrix

# Creacion

matrix <- matrix(c(1:9),
  nrow = 3,
  ncol = 3
)
matrix

# Insercion

matrix <- cbind(matrix, c(10:12))

matrix

# Borrado

matrix <- matrix[1:3, 2:3]

matrix

# Actualizacion

matrix <- matrix^2

matrix

# Ordenacion

matrix <- sort(x = matrix)

matrix

## Factor

# Creacion

factor <- factor(c(
  "Carro",
  "Moto"
))

factor

# Insercion

factor <- factor(c(as.character(factor), "Barco"))

factor

# Borrado

factor <- factor[-2]

factor <- droplevels(factor)

factor

# Actualizacion

factor <- factor(paste0(as.character(factor), " azul"))

factor
levels(factor)

# Ordenacion

factor <- factor(factor, levels = sort(levels(factor), decreasing = TRUE))

factor


# DIFICULTAD EXTRA (opcional):
# Crea una agenda de contactos por terminal.
# - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
# - Cada contacto debe tener un nombre y un número de teléfono.
# - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
#   los datos necesarios para llevarla a cabo.
# - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
#   (o el número de dígitos que quieras)
# - También se debe proponer una operación de finalización del programa.
#

# Crear un data frame para la agenda

## Para crear la agenda, me apoyé en otras funciones:
## La primera genera nombres aleatorios usados en EEUU (paquete "babynames").
## La segunda genera numeros de teléfono falsos con un formato similar al usado en Venezuela.
## La tercera se usa para validar que los números de teléfono sean numericos y que su longitud sea de 11.

library(babynames)
library(tidyverse)

generar_tlf <- function(x) {
  numero <- c()

  for (i in 1:x) {
    digitos <- sprintf("%07d", sample(0000000:9999999, size = 1))
    numero <- c(numero, paste0("0422", digitos))
  }
  numero
}

construir_agenda <- function(x = 10) {
  
  agenda <<-data.frame(
    "Nombre" = sample(c(unique(babynames::babynames$name)), size = x),
    "Telefono" = sample(c(generar_tlf(x)))
  ) 
}

validar_telefono <- function(telefono) {
  return(grepl("^[0-9]{11}$", telefono))
}


construir_agenda()

revisar_agenda <- function() {
  repeat {
    cat("Selecciona una operación: 1) Buscar 2) Insertar 3) Actualizar 4) Eliminar 5) Salir\n")
    opcion <- readLines(con = stdin(), n = 1)

    if (opcion == "1") {
      cat("Ingresa el nombre de la persona: (ej: Daniel, sin comillas)\n")

      buscar_nombre <- readLines(con = stdin(), n = 1)

      while (!(buscar_nombre %in% agenda$Nombre)) {
        cat("Ese nombre no está en la agenda, por favor, intenta nuevamente:")
        buscar_nombre <- readLines(con = stdin(), n = 1)
      }

      print(agenda %>% filter(Nombre == buscar_nombre))

      cat("\nRegresarás al menú principal.\n\n")
      
    } else if (opcion == "2") {
      cat("Ingresa el nombre de la persona que quieres agregar: (ej: Daniel, sin comillas)\n")

      agregar_nombre <- readLines(con = stdin(), n = 1)

      cat("Ingresa el número de teléfono: (ej: 04221234567)\n")

      agregar_numero <- readLines(con = stdin(), n = 1)

      while (validar_telefono(agregar_numero) == FALSE) {
        cat("Ese teléfono no es válido, por favor, intenta nuevamente:")
        agregar_numero <- readLines(con = stdin(), n = 1)
      }

      agenda <<- rbind(agenda, c(agregar_nombre, agregar_numero))
      
      cat("\nEl número de", agregar_nombre, "fue agregado con éxito. Regresarás al menú principal.\n\n")
      
    } else if (opcion == "3") {
      cat("Ingresa el nombre de la persona que quieres actualizar: (ej: Daniel, sin comillas)\n")

      actualizar_nombre <- readLines(con = stdin(), n = 1)

      while (!(actualizar_nombre %in% agenda$Nombre)) {
        cat("Ese nombre no está en la agenda, por favor, intenta nuevamente:")
        actualizar_nombre <- readLines(con = stdin(), n = 1)
      }

      cat("Ingresa el nuevo número de teléfono: (ej: 04221234567)\n")

      actualizar_numero <- readLines(con = stdin(), n = 1)

      while (validar_telefono(actualizar_numero) == FALSE) {
        cat("Ese teléfono no es válido, por favor, intenta nuevamente:")
        actualizar_numero <- readLines(con = stdin(), n = 1)
      }

      agenda <<- agenda %>% mutate(Telefono = if_else(Nombre == actualizar_nombre,
        actualizar_numero,
        Telefono
      ))

      cat("\nEl número de", actualizar_nombre, "fue actualizado con éxito. Regresarás al menú principal.\n\n")
      
    } else if (opcion == "4") {
      cat("Ingresa el nombre de la persona que quieres eliminar: (ej: Daniel, sin comillas)\n")

      eliminar_nombre <- readLines(con = stdin(), n = 1)

      while (!(eliminar_nombre %in% agenda$Nombre)) {
        cat("Ese nombre no está en la agenda, por favor, intenta nuevamente:")
        eliminar_nombre <- readLines(con = stdin(), n = 1)
      }

      agenda <<- agenda %>% filter(Nombre != eliminar_nombre)

      cat("\nEl número de", eliminar_nombre, "fue eliminado con éxito. Regresarás al menú principal.\n\n")
    }
    if (opcion == "5") break
    # Implementa el resto de opciones aquí
  }
}

revisar_agenda()
