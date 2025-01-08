### cadena de caracteres ###

#operaciones:
my_string = "hola, "
my_other_string = "Python!"

#concatenación:

my_add_string = my_string + my_other_string
print(my_add_string)
#tambien se pueden concatenar variables con caracteres, espacios, etc. 
print(my_string + " " + my_other_string + "!" )

# repetición o multiplicación:

print(my_add_string * 2)

#indexación o desempaquetado

my_string = "Python"
print(my_string[1])

###Funciones del sistema###

#longitud de la cadena de texto

my_length = len(my_string) 
print(my_length)

#Slicing (porción)

print(my_add_string[6:-1])# la opción sin colocar nada en el segundo indice tambien es válido 
print(my_add_string[6:])
print(my_add_string[::-1]) # invierte la palabra al imprimirla desde el final al principio. 

#busqueda

print("Py" in my_add_string)

#Metodo
#reemplazo: 

print(my_string.replace("o", "a"))

#division: 
print(my_add_string.split(" "))

# mayusculas y minusculas

print(my_add_string.capitalize())#convierte a mayuscula la primer letra de la cadena de texto a mayusculas
print(my_add_string.title())#convierte la primera letra de cada palabra de la cadena de texto a mayusculas
print(my_string.upper())#convierte todas las letras a mayusculas
print(my_string.lower())#convierte todas las letras a minusculas

#eliminacion de espacios al principio y final de la cadena de texto

print(my_add_string.strip())

#busqueda al principio o final
print(my_string.startswith("ho"))
print(my_string.endswith("a"))

#busqueda de posición

print(my_add_string.find("thon"))

#busqueda de ocurrencia o conteo

print(my_add_string.count("o"))

#formateo

print("Saludo: {},  lenguaje: {}".format(my_string, my_other_string))

#interpolación: f string (interpretará que todo lo que esta entre{} hace referencia a una variable)

print(f"saludo: {my_string} lenguaje: {my_other_string}")

#tranformacion en lista de caracteres:
print(list(my_add_string))

#transformación metodo join
print(" ".join(my_add_string))



###Extra###

#quitar espacios y pasar a minusculas: ok
def limpiar_palabra (word:str)-> str:
    return word.replace(" ", "").lower()
    
#función palindromo: 
def check_palindromo(word:str)-> bool:
    clean_word = limpiar_palabra(word)
    invert_word = clean_word[::-1] # invierte la palabra utilizando slicing:    
    return clean_word == invert_word #comprobación
        
#función anagrama: con retorno 
def check_anagrama(word_1:str, word_2:str)-> bool:
    clean_word_1 = limpiar_palabra(word_1)
    clean_word_2 = limpiar_palabra(word_2)
   
    #comprobación:
    return sorted(clean_word_1) == sorted(clean_word_2)

        
#funcion isograma:con conteo
def check_isograma(word):
    for i in word:
        conteo = word.count(i)
        if conteo != 1:
            return False
    return True 
      
          

### main:###
word_1 = input("ingrese una palabra\n")
word_2 = input("ingrese otra palabra\n")

#comprobación palindromo:
res_pal = check_palindromo(word_1)
print(f"la palabra {word_1} {'es ' if res_pal else 'no es '} palindromo ")
res_pal = check_palindromo(word_2)
print(f"la palabra {word_2} {'es ' if res_pal else 'no es '} palindromo ")

#comprobación anagrama:
res_ana = check_anagrama(word_1, word_2)
print(f"la palabra {word_1} y {word_2} {'son' if res_ana else 'no son '} anagramas.")

#comprobación isograma:
res_isograma= check_isograma(word_1)
print(f"la palabra {word_1} {'es ' if res_isograma else 'no es '} isograma ") 
res_isograma= check_isograma(word_2)
print(f"la palabra {word_2} {'es ' if res_isograma else 'no es '} isograma ") 



"""
#Notas de lo aprendido:
1) se debe llamar a la función por cada palabra a ser analizada
2) para retotno booleano no es necesario utilizar comprobación if/else
3) operadores ternario if/else se pueden utilizar en un f-string para decidir qué texto incluir basado en una condición.
4) iograma: otra forma es convertir los elementos de la "palabra" ingresada en un set y comparar la longitud (cantidad de elementos)
entre "palabra" original y  set(palabra). len(palabra)==len(set(palabra))    
5) un set guarda sólo los elementos únicos (sin repeticiones) eje: set(palabra)-> len(p,l,a,b,r) -> 5 elementos
mientras que len(palabra) -> 7 elemntos
"""