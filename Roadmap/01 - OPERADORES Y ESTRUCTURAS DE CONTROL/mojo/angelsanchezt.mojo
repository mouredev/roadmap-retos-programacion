"""
#01 OPERADORES Y ESTRUCTURAS DE CONTROL
Dificultad: Fácil | Publicación: 02/01/24 | Corrección: 08/01/24

EJERCICIO:
 - Crea ejemplos de funciones básicas que representen las diferentes
    posibilidades del lenguaje:
    Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
  - Comprueba si puedes crear funciones dentro de funciones.
  - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
  - Pon a prueba el concepto de variable LOCAL y GLOBAL.
  - Debes hacer print por consola del resultado de todos los ejemplos.
    (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 
  DIFICULTAD EXTRA (opcional):
  Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
  - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
    - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
    - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
    - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
    - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 
  Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
  Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
"""

"""
Run a Mojo file.
1. Instalación del Mojo SDK 
  https://docs.modular.com/mojo/manual/get-started/

2. Run a Mojo file.
  mojo angelsanchezt.mojo
"""

"""
Operadores
"""

fn main():
    # Operadores ariméticos
    let a = 10 # a es inmutable
    let b = 3
    
    var z = a + b # z es mutable
    print("Suma: " + str(a) + " + " + str(b) + " = " + str(z))

    z = a - b
    print("Resta: " + str(a) + " - " + str(b) + " = " + str(z))

    z = a * b
    print("Multiplicación: " + str(a) + " * " + str(b) + " = " + str(z))

    let w: Float64 = a / b
    print("División: " + str(a) + " / " + str(b) + " = " + str(w))
    
    z = a % b
    print("Módulo: " + str(a) + " % " + str(b) + " = " + str(z))

    z = a ** b
    print("Exponente: " + str(a) + " ** " + str(b) + " = " + str(z))

    z = a // b
    print("División entera: " + str(a) + " // " + str(b) + " = " + str(z))
    
    # Operadores de comparación
    var resultado = a == b
    print("Igualdad: ", str(a), " == ", str(b), " es ", str(resultado) )
    
    resultado = a != b
    print("Desigualdad: ", str(a), " != ", str(b), " es ", str(resultado) )

    resultado = a > b
    print("Mayor que: ", str(a), " > ", str(b), " es ", str(resultado) )

    resultado = a < b
    print("Menor que: ", str(a), " < ", str(b), " es ", str(resultado) )

    resultado = a >= b
    print("Mayor o igual que: ", str(a), " >= ", str(b), " es ", str(resultado) )

    resultado = a <= b
    print("Menor o igual que: ", str(a), " <= ", str(b), " es ", str(resultado) )

    # Operadores lógicos
    resultado = (10 + 3 == 13) and (5 - 1 == 4)
    print("AND &&: 10 + 3 == 13 and 5 - 1 == 4 es ", str(resultado))

    resultado = (10 + 3 == 14) or (5 - 1 == 4)
    print("OR ||: (10 + 3 == 14) or (5 - 1 == 4) es", str(resultado))

    resultado = not (10 + 3 == 14)
    print("NOT !: not (10 + 3 == 14) es ", str(resultado))

    # Operadores de asignación
    var my_number = 11 # asignación
    print(my_number)
    my_number += 1  # suma y asignación
    print(my_number)
    my_number -= 1  # resta y asignación
    print(my_number)
    my_number *= 2  # multiplicación y asignación
    print(my_number)
    my_number /= 2  # división y asignación
    print(my_number)
    my_number %= 2  # módulo y asignación
    print(my_number)
    my_number **= 1  # exponente y asignación
    print(my_number)
    my_number //= 1  # división entera y asignación
    print(my_number)

    # Operadores de bit
    let c = 10  # 1010
    let d = 3  # 0011
    print("AND: 10 & 3 = ", c & d)  # 0010
    print("OR: 10 | 3 =", c | d)  # 1011
    print("XOR: 10 ^ 3 = ", 10 ^ 3)  # 1001
    print("NOT: ~10 = ", ~10)
    print("Desplazamiento a la derecha: 10 >> 2 = ", 10 >> 2)  # 0010
    print("Desplazamiento a la izquierda: 10 << 2 = ", 10 << 2)  # 101000


    """
    Estructuras de control
    """

    # Condicionales

    let my_string = "Brais"

    if my_string == "MoureDev":
        print("my_string es 'MoureDev'")
    elif my_string == "Brais":
        print("my_string es 'Brais'")
    else:
        print("my_string no es 'MoureDev' ni 'Brais'")
    
    # Iterativas

    for i in range(11):
        print(i)

    var i = 0
    while i <= 10:
      print(i)
      i += 1

    # Manejo de excepciones
    try:
        print(10 / 0)
    except:
        print("Se ha producido un error")
    finally:
        print("Ha finalizado el manejo de excepciones")

  
    """
    Extra
    """

    for number in range(10, 56):
        if number % 2 == 0 and number != 16 and number % 3 != 0:
            print(number)
