"""
Crea ejemplos de funciones básicas que representen las diferentes posibilidades del lenguaje:
- Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
"""
# Función sin parámetros ni retorno
print("Función sin parámetros ni retorno \n")
def basicFuntion ():
    print("Esto es una función básica \n")
    
basicFuntion()

# Función con uno o más parámetros
print("Función con uno parámetro \n")
def saludar(nombre):
    print(f"Hola {nombre} \n")

saludar("Pepe")

print("Función con dos parámetros \n")
def saludarEdad(nombre,edad):
    print(f"Hola {nombre}, tienes {edad} \n")

saludarEdad("Pepe",34)

# Función con retorno
print("Función con retorno \n")
def comporbarEdad(edad):
    if edad in range(0,18):
        return f"Eres menor de edad con {edad} años \n"
    else:
        return f"Eres mayor de edad con {edad} años \n"

print(comporbarEdad(13))
print(comporbarEdad(21))


# Función con un parámetro por defecto
print("Función con un parámetro por defecto \n")
def saludarDefault(nombre="pepito"):
    print(f"Hola {nombre} \n")

saludarDefault()

# Función con un parámetro por defecto y otro no
print("Función con un parámetro por defecto y otro no \n")
def saludarDefaultTwo(nombre="pepito",edad=int):
    print(f"Hola {nombre}, tienes {edad} \n")

saludarDefaultTwo(edad=34)


# Función con retorno de más de un parámetro
print("Función con retorno de más de un parámetro \n")
def saludoYEdaCompuesto():
    return "Hola","Pepito"

saludo, nombre = saludoYEdaCompuesto()
print(f"{saludo}, {nombre}!\n")


""" 
- Comprueba si puedes crear funciones dentro de funciones.
- Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
- Pon a prueba el concepto de variable LOCAL y GLOBAL.
- Debes hacer print por consola del resultado de todos los ejemplos.
(y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
""" 
# Función dentro de otra función
print("Función dentro de otra función \n")
PI = 3.14 # Constante del valor Pi
shapetype = "circle" # Tipo de figura
area=1 # variable fuera de la función

def AreaCalc(shape,medida):
    # variable dentro de la función que iniciamos a 0
    area = 0
    print(f"Valor de área dentro de la función: {area} \n")
    # Función dentro de otra función
    def calcularAreaCircunferencia(medida):
            area = PI * medida ** 2
            print(f"El varlor del área de la circunferencia es: {area}")
    # Comprobamos el tipo en y enviamos a la función interna que corresponda
    if shape == "circle":
        calcularAreaCircunferencia(medida)

AreaCalc(shapetype,25)
print(f"Valor de área fuera de la función: {area} \n")

# Funciones que ya vienen con el sistema
print(f"Función max(1,2,3,4,5): {max(1,2,3,4,5)}")
print(f"Función min(1,2,3,4,5): {min(1,2,3,4,5)}")
print(f"Función len('Hola Mundo!'): {len("Hola Mundo!")}")

# Función con una variable de argumentos
print("Función con una variable de argumentos \n")
def mesesAno(*meses):
    # Imprimimos tantas veces como meses nos han pasado
    for mes in meses:
        print(f"Mes: {mes}")
    
mesesAno("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre")
    
# Función con una variable de argumentos con palabra clave
print("Función con una variable de argumentos con palabra clave \n")

def mesesAnoClave(**valores):
    # Imprimimos tantas veces como valores se nos han pasado
    for clave, valor in valores.items():
        print(f"- El mes {clave} tiene {valor} días")

mesesAnoClave(Enero=31,
         Febrero=28,
         Marzo=31,
         Abril=30,
         Mayo=31,
         Junio=30,
         Julio=31,
         Agosto=31,
         Septiembre=30,
         Octubre=31,
         Noviembre=30,
         Diciembre=31)

""" 
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

print("\nEJERCICIO EXTRA\n")
 
def contrarCadenas(primerTexto,segundoTexto):
    # Contador que usaremos para el return
    contador = 0
    # Usaremos un bucle for
    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
            print(f"{i} - {primerTexto+segundoTexto}")
        elif i % 3 == 0:
            print(f"{i} - {primerTexto}")
        elif i % 5 == 0:
            print(f"{i} - {segundoTexto}")
        else:
            print(i)
            contador += 1
    # Retornamos el resultado del contador
    return f"Números que no son múltiplos de 3 ni de 5: {contador}"
 
print(contrarCadenas("Este es un ejemplo de primer texto","Este es el segundo texto para calcular \n"))


