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
    
arg_personal("José", 25, "Masculino", "Venezolana")

# Con un argumento predeterminado (si es que no se diera el argumento del parámetro)
def default_arg_saludo(nombre="Usuario"):
      print(f"Bienvenido, {nombre}!")

default_arg_saludo()
default_arg_saludo("Figueroa")

# Con argumentos y return
def args_return(saludo, persona):
      return f"{saludo}, {persona}"

print(args_return(default_arg_saludo(),arg_saludo("José A.")))