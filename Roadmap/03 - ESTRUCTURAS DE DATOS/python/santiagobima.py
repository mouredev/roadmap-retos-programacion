#Muestra  ejemplos de creacion de todas las estructuras soportadas por defecto en tu lenguaje

#lista: Estructura ordenada / también conocido como array , en python como tal Array en python no exite.
#ordenada y modificable. Su orden es su orden de insercion de los elementos.

lista = ['carlos','pedro','santiago','marcos','maria']
print(lista)

lista.append('fabiana') #insercion

lista.remove('carlos') #borrar

print(lista[1])

lista[1] = 'antonella'

lista[0] = 'geremy'

lista.sort()   ###ordenacion### #por defecto de forma ascendente y alfabetica 

print(lista)
print(type(lista))


#TUPLAS // Se usan en estructuras de datos rígidos para no meter la mano.

mitupla= ('fabiana','victoria','40','boligrafo')

print(mitupla[0])
print(mitupla[1])
mitupla = tuple(sorted(mitupla)) ##LO que nos devuelve es una lista si solo dejo sorted.!! Ademas tuve que poner el 40 en string. sino no lo deja acomodar.
print(type(mitupla))


#SETS
#Estructura no ordenada pero no permite duplicados.
#EL SET POR DEFINICION ES UNA ESTRUCTURA DESORDENADA ! ! NO ME PUEDO FIAR DE LA POSICION DE UN ELEMENTO !!

#Sets no tengo operacion de acceso !!!  No hay nada que me asegure que va haber en esa posición.


miset = {'3434','13435','40349','549340','santiago'}
miset.add('jorge')
miset.add('jorge') ###NO lo va a dejar de duplicar.
miset.add('santiago@gmail.com')
miset.remove('3434') #La eliminacion si funciona !!!
#Lo mejor si quiero reemplazar un dato es elimianr ese dato y agregar otro.

miset = set(sorted(miset)) #Por deficiion el set no se puede ordenar. No es una estructura ordenada.!

print(type(miset))
print(miset)



#Por definicion los diccionarios no son ordenados pero en realidad si acaba siendo ordenados por la forma en que en python han decidido que sean ordenados pero ha sudio una decision de implementacion. Por eso solo puedo acceder a valores por clave.

diccionario = {'nombre':'santiago','edad':37,'nacionalidad': 'hungaro'}

diccionario['idioma'] = 'ingles' #agrego un valor.

diccionario['nombre'] = 'jeremy' #modifico un valor.

del diccionario['edad'] #elimino #del es una operacion reservada del sistema.

#si solo le paso sorted solo pilla las claves
diccionario = dict(sorted(diccionario.items())) #acabo terminando esta lista de tuplas en un diccionario. 

print(type(diccionario))
print(diccionario)


#BONUS -->>>:  D IFI CULTA D EX TR A 

def telefono(nombre,agenda):
    
    numero = input('dame el numero')
    if numero.isdigit() and len(numero) <= 11:
        
        agenda[nombre] = numero
        
    else:
        print('no cumple con los requisitos basicos')
                 
def agendita():
    
    agenda = {}
          
    while True:
        
        print("1. Buscar contacto")
        print("2. Insertar contacto")
        print("3. Actualizar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")
        
        opcion = input('\ndame un numero y vamos a ver ')
        
        #En PYTHON EL SWICHT SE LLAMA MATCH:
        
        match opcion:
            
            case '1':
                nombre = input('dame el nombre a buscar')
                if nombre in agenda:
                    print(nombre)
                    
                else:
                    print('no esta en la agenda')
                    
            case '2':
                nombre = input('dame el nombre a agregar')
                
                telefono(nombre,agenda)
                
            case'3':
                
               nombre = input('dame el nombre a actualizar')
               if nombre in agenda:
                   telefono(nombre,agenda)
               else:
                   print('no existe')
                    
            
            case '4':
                
               name = input('dime a quien debemos eliminar')
               
               if name in agenda:
                   del agenda[name] 
                   
               else:
                   print(f'el contadto {name} no existe bro')
                
            case '5':
                print('saliendo del programa')
                break
            case _:
                print('Opcion no valida. Elige una opcion del 1 al 5.')
                

if __name__ == '__main__':
    agendita()
