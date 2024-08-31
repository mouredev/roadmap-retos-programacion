'''
Crea ejemplos de funciones básicas que representen las diferentes posibilidades del lenguaje
'''
def func_sinParametros_niRetorno():
    result = 3 + 5
    print(result)
func_sinParametros_niRetorno()


def func_sinParametros_conRetorno():
    result = 5 + 5
    return result
print(func_sinParametros_conRetorno())


def func_conParametro_sinRetorno(a):
    result = a + 5
    print(result)
func_conParametro_sinRetorno(6)


def func_conParametro_conRetorno(a):
    result = a - 5
    return result
print(func_conParametro_conRetorno(7))


def func_conParametros_sinRetorno(a, b):
    result = a * b
    print(result)
func_conParametros_sinRetorno(2, 5)


def func_conParametros_conRetorno(a, b):
    result = a * b
    return result
print(func_conParametros_conRetorno(4, 5))


print()

'''
Comprueba si puedes crear funciones dentro de funciones
'''
def cuadrado_y_cubo(n1, n2):
    
    def cuadrado(n):
        return n ** 2
    
    def cubo(n):
        return n ** 3
    
    nAlCuadrado = cuadrado(n1)
    nAlcubo = cubo(n2)

    return nAlCuadrado, nAlcubo
print(cuadrado_y_cubo(4, 5))

print()

'''
Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
NOTA: "print" ya es una funcion creada del lenguaje, pero por las dudas usararé otras dos
'''
# funcion round
print(round(3.7))

# funcion max
lista = [12,35,453,46,8,45]
print(max(lista))

print()

'''
Pon a prueba el concepto de variable LOCAL y GLOBAL.
'''
# NOTA: una variable local puede siempre estar fuera de funciones, pero no podrá ser modificada dentro de una.
# * Para eso usamos 'global [nombre de la variable global]' dentro de una funcion para poder modificarlo.
# * Y las varables locales no podrán ser llamadas fuera de su respectiva funcio funcion 
glob_var = 10
def func_globalLocal():
    global glob_var
    glob_var += 1
    local_var = 12
    print(f'{glob_var}, {local_var}')
func_globalLocal()

print()

'''
Extra:
Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
'''
def extra(s1: str, s2: str):
    n_veces = 0
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(f'{s1}{s2}')
        elif i % 3 == 0:
            print(s1)
        elif i % 5 == 0:
            print(s2)
        else:
            print(i)
            n_veces += 1

    return f'Se ha impreso el numero {n_veces} veces'
print(extra('arco', 'iris'))
