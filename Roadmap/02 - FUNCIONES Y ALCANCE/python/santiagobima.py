
'''
Funciones definidas por el usuario
'''

#simple
def hola():
    print("Hola, soy Santiago Bima")
    
hola()


#retorno

def otrafuncion2(numero1,numero2):
    return numero1+numero2

retorno = otrafuncion2(1,2)

print(retorno)


#con un argumento

def argumento(nombre):
    print(f'hola,{nombre}')
    
argumento('santiago')


#con dos argumentos
def otrafuncion(numero, nombre):
    print('Hola soy '+nombre+' y mi numero favorito es'+ str(numero))
    
otrafuncion(7, 'Santiago Bima')


#con argumento predeterminado

def pordefecto(name='santiago'):
    print('hola,',{name})
    




#con retorno de varios valores , tupla de valores:

def multiplosderetornos():
    return 'Que tal', 'Santiago'

saludo,nombre = multiplosderetornos()

print(saludo)
print(nombre)
    



#con un numero variable de argumentos

def variable_greet(*nombres):
    for name in nombres:
        print(f'Hola,{name}')
        
        
variable_greet('botella','marcos','Clara')



#con un numero variable de argumentos con palabra clave


def variable_kwargs(**nombres):
    for param,name in nombres.items():
        print(f'Hola,{name}({param})')
        
variable_kwargs(lugar='rastro',
                ciudad='berlin',
                capita='ny')
        




#funcion dentro de funcion

def funcion_porfuera():
    print('esta es una funcion por fuera') 
    
    def funcion_por_dentro():
        print('esta es una función por dentro')
    
    funcion_por_dentro()
    
funcion_porfuera()






#funciones propias de python

def convertir_a_mayusculas(lista_cadenas):
    return list(map(str.upper,lista_cadenas))
    
cadenas = ['me','llamo','santiago','bima']

cadenas_mayusculas = convertir_a_mayusculas(cadenas)
print(cadenas_mayusculas)


print(len('santiago'))
print(type(10))





#variables globales y locales (SCOPE//AMBITO)

contador_global = 0

def incrementar_contador_local():
    contador_local = 0
    contador_local += 1
    print('Contador local:', contador_local)
    
def incrementar_contador_global():
    global contador_global
    contador_global += 1
    print('contador global:', contador_global)

print(f'Contador global antes de llamar : {contador_global}')

incrementar_contador_local()
incrementar_contador_global()
incrementar_contador_global()
incrementar_contador_local()
print(f'contador global final: {contador_global}')




#EXTRA 

from word2number_es import w2n

def dificultad_extra(parametro1:str,parametro2:str) -> int:
    contador = 0
    
    for numero in range(1,101):
        if numero % 3 == 0 and numero % 5 == 0:
            print(parametro1 + parametro2)
            
        elif numero % 3 == 0:
            print(parametro1)
            
        elif numero % 5 == 0:
            print(parametro2)
            
        else:
            print(numero)
            contador +=1
            
    return contador
    


resultado = dificultad_extra('aloha','mora')

print('cantidad de numeros reemplazados', resultado)


print('LISTO!')