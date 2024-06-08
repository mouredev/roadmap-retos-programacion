'''
funciones basicas en python
Ejemplos:
'''
# funciones sin parametros
def decir_hola_mundo():
     print("hola mundo")
decir_hola_mundo() #esta funcion solo imprime lo indicado en el 'print'

#funciones con parametros
def saludar(nombre):
    print("como va tu dia " + nombre + "?" )
saludar("michael") #estamos indicando un parametro extra que pondremos en los parentesis 

#funcions con retorno
def multiplica():
    return 3 * 2
#aquí lo que hicimos fue indicar que cuando vamos a imprimir la funcion el valor del return sea usado 

valor = multiplica()
print(valor)
# aquí vemos que cuando la imprimimos el resultado es 6 porque la multuplicacion de el return es 2 * 3
# la variable es por estetica, se puede solo poner 'print(multiplica())' y funciona igual

'''
funciones dentro de funciones
'''
def funcion_externa():
    def funcion_interna():
        print("soy la funcion interna")
    funcion_interna()
funcion_externa()

'''
funciones del lenguaje
'''

'''función max()'''
print(max(1,2,3,4,16))
#la funcion max nos da el valor mas grande de lo que estemos usando
list = ['a','b','c','d','h']
print(max(list))

'''función min()'''
print(min(1,2,3,4,16))
list = ['a','b','c','d','h']
print(min(list))

'''función divmod()'''
print(divmod(10,2))
# divide los numeros y nos da el cociente (10 // 2) y el resto (10 % 2) que en este caso seria '5 , 0'

'''función len()'''
print(len("hola amigos"))
# esta funcion nos cuenta la cantidad de caracteres del texto incluyendo los espacios 
list1 = [123, 'abc', 'limon'] 
print(len(list1))
# tambien funciona para contar cuantos objetos hay en una lista y demas usos similares para contar

'''función hex()'''
print(hex(24)) 
# funcion que los da un numero hexadecimal con el prefijo 'ox' en este caso seria 'ox18'

'''función ord()'''
print(ord("j"))
#es una funcion que tranforma un caracter en el numero unicode de ese caracter
#en este caso el numero Unicode de la letra 'J' es 106

'''función chr()'''
print(chr(106))
#transforma un numero Unicode en el caracter que representa (lo contrario a la funcion 'ord()')
#en este caso el numero Unicode 106 representa el la letra 'J' y el numero Unicode 6 representa el caracter '♠'
#si es numero que se escriba en la funcion no tiene un caracter Unicode, dara error. Ejemplo: print(chr(-10))

'''función input()'''
'''age = int(input("por favor ingresa tu edad: "))
print(age)'''
# input es una funcion que nos permite interactuar con el codigo ingresando informacion 
# en el ejemplo quiero solicitar la edad y ya que imput lee todo como un Str es bueno especificar el tipo de dato
# en este caso como es la edad es un numero entero = int 
#si quieres probar el ejemplo porfavor quita las comillas ya que a lo largo del codigo tendras que ingresar el dato cuando lo ejecutes

'''función type()'''
print(type(4))
#la funcion type() me permite saber el tipo de dato que pongo en la funcion, en este caso un INT

'''variables locales y globales'''
#list es una varible definida es la linea 28
print(list)
list
#es una variable global ya que puedo acceder a ella en cualquier momento porque esta en el cuerpo del codigo

def variable_local():
    my_new_list = ['l', 'm', 'n', 'ñ']
    print(my_new_list)
variable_local()

'''print(my_new_list)
'my_new_list' es una variable local, solo la puedo usar llamando la funcion.
Y si tratara de hacer un print normal daria error
'''

'''ejercicio extra'''
def juego(parametro1, parametro2):
    numeros = 0 
    for i in range(1 , 101):
        if i % 3 == 0 and i % 5 == 0:
            print(parametro1 , parametro2)
        elif i % 3 == 0:
            print(parametro1)
        elif i % 5 == 0:
            print(parametro2)
        else:
            numeros += 1
            print(i)
    return ("numero de veces que se imprimio un numero ", numeros)  
print(juego("multiplo de 3", "multiplo de 5")) 
