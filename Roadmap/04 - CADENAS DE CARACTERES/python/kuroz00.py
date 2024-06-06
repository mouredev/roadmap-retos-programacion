#Imprimir una cadena de caracteres por pantalla
varEjemplo = 'Hola a todos! '
varEjemplo2 = 'Que tal estan?'
print(varEjemplo) #hola a todos

#Buscar un caracter en especifico
if '!' in varEjemplo:
    print('" ! " si existe dentro de varEjemplo')

#FIND Retornara la pocision en la que se encuentra el caracter o cadena señalada como parametro
print(varEjemplo.find('!'))

#Eliminar espacios en blanco a los costados de la cadena de caracteres
varEjemplo.strip()

#Concatenar 2 o mas cadenas de caracteres 
varEjemplo += varEjemplo2
print(varEjemplo) 

#Buscar una palabra en particular
if 'todos' in varEjemplo:
    print('"todos" si existe dentro de varEjemplo')

#Averiguar la longitud
print('La longitud de varEjemplo es: ', len(varEjemplo))

  #Ahora sin los espacios en blanco entre medio
if " " in varEjemplo:
    varEjemplo = varEjemplo.replace(" ", "")
print('La longitud de varEjemplo sin espacios es: ', len(varEjemplo))

#subcadenas 
  #slicing 
print(varEjemplo[:4]) # hola
print(varEjemplo[4:11]) # a todos!
print(varEjemplo[11:]) # que tal estna?


#Recorrer la cadena de caracteres (comentado para no saturarme la terminal)
#for x in range(len(varEjemplo)):
   # print(varEjemplo[x]) #impresion de todos sus caracteres uno por uno

#Conversion 
varEjemplo = 'HOla a toDos, ESTO es una CADENA De caraCTereS'

    #Mayus
print('Conversion a mayusculas  ->' ,varEjemplo.upper())
    #Minus
print('Conversion a minusculas  ->' ,varEjemplo.lower())
    #convertir en una lista y de paso ordenarla (tambien se puede en tuple y set)
print(sorted(varEjemplo))

#Reemplazar palabras al interior
varEjemplo = 'Hola mundo!'
if 'Hola' in varEjemplo:
    varEjemplo = varEjemplo.replace('Hola', 'Adios') #Adios mundo! (suena re sad)
    print(varEjemplo)

#Dividir SPLIT
varEjemplo = 'Esto es una cadena de varias palabras '
varEjemplo = varEjemplo.split()
print(varEjemplo) #Dividi todas las palabras las cuales quedaron en una lista

#Unir JOIN
varEjemplo = " ".join(varEjemplo)
print(varEjemplo)

#Interpolacion
numero = 500
saludo1 = 'Hola'
saludo2 = ' a todos'
PI = 3.14

print('%i + 500 = 1000' %(numero))
print('%.2f es el valor de PI!' %(PI))
print('%s %s' %(saludo1,saludo2))

# * DIFICULTAD EXTRA (opcional):

'''   Funciones   '''
def palinfromo(palabra):
    palabra = palabra.lower().replace(' ', '')
    return palabra == palabra[::-1]


def anagrama(palabra1, palabra2):
    palabra1 = palabra1.lower().replace(' ', '')
    palabra2 = palabra2.lower().replace(' ', '')       
    return sorted(palabra1) == sorted(palabra2)       

def isograma(palabra1, palabra2):
    palabra1 = palabra1.lower().replace(' ', '')
    palabra2 = palabra2.lower().replace(' ', '')
    return len(set(palabra1)) == len(set(palabra2))


print('palindromo: ', palinfromo('radar'))
print('anagrama: ', anagrama('radar', 'rada'))
print('isograma: ',isograma('rueda', 'ruedo'))


