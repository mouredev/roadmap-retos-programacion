# Funciones y alcance

variable_global = "Hola Python!"

def imprime_diez():
    print("Diez")

def suma(num1, num2):
    print(num1+num2)

def resta(num1, num2):
    return num1 - num2

def multiplicacion(num1, num2):
    producto = num1 * num2

    def imprime_valor_por_diez(v):
        print(v * 10)
    
    imprime_valor_por_diez(producto)

def division():
    var_local1 = 10
    var_local2 = 12
    print(var_local1 / var_local2)

# Dificultad extra

def dificultad_extra(str3, str5):
    contador = 0
    for index in range(1, 101):
        if (index % 3 == 0) and (index % 5 == 0):
            print(f"{index} " + str3 + " y " + str5)
        elif index % 3 == 0:
            print(f"{index} " + str3)
        elif index % 5 == 0:
            print(f"{index} " + str5)
        else: 
            print(index)
            contador += 1


    return contador



imprime_diez()
suma(10, 20)
print(resta(20, 10))
multiplicacion(10, 10)
print(len(variable_global))
division()
numero_de_veces = dificultad_extra("Multiplo de 3", "Multiplo de 5")
print(f"Números no multiplos de 3 y/o de 5: {numero_de_veces}")




