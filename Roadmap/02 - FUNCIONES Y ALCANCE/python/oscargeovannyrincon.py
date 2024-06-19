'''/*
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
 */'''

def area_cuadrado():
     lado=8
     print(f'\nEl area de un cuadrado de lado {lado} metros es {lado*lado} metros cuadrados')

area_cuadrado()

def area_circulo(radio):
     area_circulo=3.1416*(radio**2)
     return(print(f'\nEl area de un circulo de radio {radio}m es {area_circulo} metros cuadrados '))
area_circulo(0.01)

def area_poligono(apotema,perimetro):
     poligono=(apotema*perimetro)
     return(print(f'\nEl area de cualquier poligono solo necesita el apotema y el perimetro\nEl area del poligono de apotema={apotema}cm y perimetro={perimetro}cm es {poligono}cm cuadrados'))

area_poligono(perimetro=90,apotema=50)

def mi_peso(masa,acc_gravedad):
     mi_peso=masa*acc_gravedad
     return(mi_peso)
print(f'\nMi masa es de 75kg y la acceleracion de la gravedad es 9.81m/s, mi peso sera de {mi_peso(75,9.81)}N')

def multiplo_3(numero):
     if numero%3==0:
          #print('multilplo de tres')
          return(True)
     else:
          return(False)
num=399
print(f'\nEl numero {num} es multiplo de 3?')
print(multiplo_3(num))


def area_poligono(apotema,perimetro=90):
     poligono=(apotema*perimetro)
     return(print(f'\nEl area de cualquier poligono solo necesita el apotema y el perimetro\nEl area del poligono de apotema={apotema}cm y perimetro={perimetro}cm es {poligono}cm cuadrados'))

area_poligono(50)
area_poligono(apotema=50,perimetro=100)
area_poligono(60)


#FUNCION DENTRO DE UNA FUNCION
#La verdad no le encuentro sentido a una funcion dentro de otra funcion

def outer_function():
     def inner_function(name):
          print(f'Funcion interna: Hola, {name}')
     inner_function('Oscar')
     
outer_function()

def variable_key_arg_greet(**names):
     for key, value in names.items():
          print(f'Hola, {value} ({key})!')

variable_key_arg_greet(Nombre='Oscar', Apellido='Rincon',Edad=35, Lenguaje='Python')


#Utiliza algún ejemplo de funciones ya creadas en el lenguaje.

x=(5<3)
print(bool(x))

print(ord('^'))

numeros=[24,37,-54,36,89]
print(sum(numeros))

print(hex(1333))

nombre='Oscar Geovanny Rincon Fuentes'
print(nombre.replace('a','e'))

#Variables globales y locales

pi=3.1416
rad=20

def area_circulo(radio):
     area=pi*(radio**2)
     return area

print(f'El area de la circunferecia de radio {rad}cm es {area_circulo(rad)}cm cuadrados')

ang_grados=270
def longitud_arco(radio,angulo_grados):
     angulo_radianes=angulo_grados*(pi/360)
     long=radio*angulo_radianes
     return long

print(f'La longitud de arco de radio {rad}cm y un angulo de {ang_grados}° es {longitud_arco(rad,ang_grados)}cm')

'''* DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.'''
 
def tic_tac(texto_1,texto_2):
     rep=0
     for num in range(1,101):
          if num%3==0 and num%5==0:
               print(texto_1+texto_2)
          elif num%3==0:
               print(texto_1)
          elif num%5==0:
               print(texto_2)
          else:
               print(num)
               rep += 1
     return f'\n El numero de veces que se imprimio el numero fue {rep}'

print(tic_tac('tic','tac'))