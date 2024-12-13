"""
 * EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
"""
# Funciones definidas por el usuario

# Simple
def saludo():
    print("Hola! Soy una función simple")

saludo()


# Con retorno
def return_saludo():
        return "Hola, Función con retorno"

print(return_saludo())


# Con un argumento
def arg_saludo(nombre):
      print(f"Hola, {nombre}!")
    
arg_saludo("José Alberto")


# Con varios argumentos
def arg_personal(nombre, edad, sexo, nacionalidad):
      print(f"Nombre: {nombre}. Edad: {edad}. Sexo: {sexo}. Nacionalidad: {nacionalidad}")
    
arg_personal("José", 26, "Masculino", "Venezolana")


# Con un argumento predeterminado (si es que no se diera el argumento del parámetro)
def default_arg_saludo(nombre="Usuario"):
      print(f"Bienvenido, {nombre}!")

default_arg_saludo()
default_arg_saludo("Figueroa")


# Con argumentos y return
def args_return(saludo, persona):
      return f"{saludo}, {persona}"

print(args_return("Hola!","José A."))


# Con retorno de valores separados
def multiple_return_saludo():
      return "Hola", "Python"

saludo, name = multiple_return_saludo()
print(saludo)
print(name)


# Con un número variable de argumentos
def variable_arg_saludo(*nombres):
      for nombres in nombres:
            print(f"Hola, {nombres}!")

variable_arg_saludo("Mundo", "Python", "Git", "José", "MoureDev")


# Con un número variable de argumentos con palabra clave
def variable_key_arg(**nombres):
      for key, value in nombres.items():
            print(f"{key}: '{value}'")

variable_key_arg(
      lenguaje = "Python",
      nombre = "José",
      ocupacion = "Estudiante",
      alias = "JoseAlberto13",
      años = 26
)


# Funciones dentro de Funciones
def outer_function():
      def inner_function():
            print("inner function: Función dentro de la función")
      inner_function()

outer_function()


# Funciones dentro del lenguaje
print(len("José"))
print(type(25.5))
print(sorted({4,2,7,1,5,6,3}))


# Variables locales y globales
variable_global = "Esto es global!"
print(variable_global)

def conVaribale_Global():
      variable_local = "Esto es local!"
      print(f"Funciónes: local={variable_local} global={variable_global}")

conVaribale_Global()

print(variable_global)
# print(variable_local) no funciona fuera de la funcion definida


"""
DIFICULTAD EXTRA
"""

def lafuncion(texto1, texto2) -> int:
      count = 0
      for i in range(1,101):
            if i % 5 == 0 and i % 3 == 0:
                  print(texto1 + texto2)
            elif i % 3 == 0:
                  print(texto1)
            elif i % 5 == 0:
                  print(texto2)
            else:
                  print(i)
                  count += 1
      return count

print(lafuncion("Texto #1","Texto #2"))