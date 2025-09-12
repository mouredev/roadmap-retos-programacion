import datetime
variable = str("Esta es la Variable global")
# --------------------------  TIPOS DE FUNCIONES EN PYTHON -------------------------- 

def main():
    
    # Función sin retorno
    def hola_mundo():
        print("-------------------------------------------------------------------")
        print("FUNCION SIN RETORNO:")
        print("¡Hola Mundo!")
        print("-------------------------------------------------------------------")
    
    hola_mundo()
    

    # Función con retorno
    def fecha_actual():
        
        print("-------------------------------------------------------------------")
        print("FUNCION CON RETORNO:")
        return datetime.datetime.now()

    print("La fecha actual es: ", fecha_actual())
    print("-------------------------------------------------------------------")

    # Función con parametros
    nombre = str("Arthuro")
    apellido = str("Dugarte")

    def saludo(nombre, apellido):
        print("-------------------------------------------------------------------")
        print("FUNCION CON PARAMETROS:")
        print(f"¡Hola {nombre} {apellido}!")
        print("-------------------------------------------------------------------")

    saludo(nombre, apellido)

    # Función dentro de una función
    def modificar_palabra(palabra):

        print("-------------------------------------------------------------------")
        print("FUNCION DENTRO DE UNA FUNCION:")

        def palabra_invertida(palabra):
            return palabra[::-1]
        return palabra_invertida(palabra)

    print(modificar_palabra("Hola"))
    print("-------------------------------------------------------------------")

    # Función ya creada en el lenguaje
    def anio():
        return datetime.datetime.now().year
    
    print("-------------------------------------------------------------------")
    print("FUNCION YA CREADA EN EL LENGUAGE:")
    print(anio())
    print("-------------------------------------------------------------------")

    # Función con variables locales y globales
    def variable_local():
        variable = str("Esta es la Variable local")
        print("-------------------------------------------------------------------")
        print("VARIABLES:")
        print(variable)
        print(globals()["variable"])
        print("-------------------------------------------------------------------")
    variable_local()

    # Dificultad extra
    print("-------------------------------------------------------------------")
    print("DIFICULTAD EXTRA:")
    def textos(text1, text2):
        cont = 0
        for i in range(1, 101):
            if i % 3 == 0 and i % 5 == 0:
                print(f"{text1} {text2}")
                cont += 1
            elif i % 3 == 0:
                print(text1)
                cont += 1
            elif i % 5 == 0:
                print(text2)
                cont += 1
            else:
                print(i)
        return (100 - cont)
    
    total = textos("Soy multiplo de 3.", "Soy multiplo de 5.")
    print("-------------------------------------------------------------------")
    print("El numero de palabras que no son multiplos de 3 o 5 es:", total)
    print("-------------------------------------------------------------------")


if __name__ == "__main__":
    main()