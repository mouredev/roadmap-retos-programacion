'''
Crea ejemplos de funciones básicas que representen 
las diferentes posibilidades del lenguaje:
Sin parámetros ni retorno, con uno o varios parámetros, 
con retorno...
'''
# Sin parámetro ni retorno
def restar():
    print(f'10-3 = {10-3}')
restar()

# Con uno parámetro
def miNombre(nombre):
    print(f'Mi nombre es {nombre}')
miNombre('Pedro')

# Con varios parámetros y retorno
def sumar(n1, n2):
    return n1+n2
print(f'El resultado de la suma es: {sumar(10,3)}')

'''
Comprueba si puedes crear funciones dentro de funciones.
Sí se puede crear una función dentro de otra, pero la función interna 
solo puede ser llamada en la función externa. Es decir, en este caso, solo 
puede utilizarse saludar() en nombrar().
'''
def nombrar(nombre):
    def saludar():
        print(f'Hola, {nombre}')
    saludar()

nombrar('Paco')

'''
Utiliza algún ejemplo de funciones ya creadas en el lenguaje
'''
color = 'amarillo'
longitud = len(color)
print(f'La longitud de "amarillo" es: {longitud} ')

lista = [0, 1, 3, 89]
print(f'El mayor número de la lista es: {max(lista)}')

'''
Pon a prueba el concepto de variable LOCAL y GLOBAL.
Como se ve, 'apellido' al ser definida de forma global, puede
ser utilizada en ambas funciones, pero 'nombre' se ha definido dentro
de una función, teniendo utilidad solo dentro de ella.
'''
apellido = 'González' # variable GLOBAL

def saludar():
    nombre = 'Lucía' # varibale LOCAL
    print(f'Mi nombre es {nombre} y {apellido}')
    
def saludar2():
    print(f'Mi nombre es {nombre} y {apellido}')

saludar()
# saludar2() # Error


'''
DIFICULTAD EXTRA
'''

def mostrarNumero(texto1, texto2):
    contadorNumber = 0
    for n in range(1, 101):
        if n%3==0 and n%5==0:
            print(texto1 + texto2)    
        elif n%3 == 0:
            print(texto1)  
        elif n%5 == 0:
            print(texto2)  
        else:
            print(n)
            contadorNumber+= 1
    return f'Número de veces que se ha impreso el número en lugar de los textos: {contadorNumber}'

resultado = mostrarNumero('Choco', 'late')
print(resultado)






