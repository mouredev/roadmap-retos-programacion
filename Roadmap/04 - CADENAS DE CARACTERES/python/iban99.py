#Suma
a = 'Miriam'
b = 'Iban'
c = "Señor4"

print(a + " " + b) #Concatenación
print(a*3) #Repetición
print(len(a)) #Len
print(a.upper()) #Mayúscula
print(a.lower()) #Minúscula
print(a.title()) #Las primeras letras todas en mayúscula
print(a.capitalize()) #Primera letra en mayúscula
print(a[1]) #Acceder a una posición - Indexación
print(a[1:3]) #Subcadena - Slicing - Porción
print(a.find("r")) #Buscar posición
print("r" in a) #True si está dentro de la cadena
print(a.count("i")) #Contar letras/subcadenas
print(a.isalnum()) #True si son todos caracteres alfanuméricos
print(c.isalpha())#True si todos los cracteres son alfabéticos
print(c.isnumeric())#True si todos los cracteres son números
print(a.strip()) #Elimina el caracter que se le introduce 
print(a.join(["Hola ",b])) #Une caracteres
l1=[a, ",", b, "Gil"]
print(" ".join(l1)) #Transformación de lista en cadena
print("Python,Java,C".split(",")) #Separa por el caracter que se introduce
print(a.startswith("Mi")) #Empieza por
print(a.endswith("im")) #Termina por
print(a.split("r")) #División
print(a.replace("i", "I")) #Reemplazo
print("Nombre: {}, apellido: {}!". format(a,b)) #Formateo
print(f"Nombre: {a}, apellido: {b}!") #Interpolación
print(list(a)) #Crear lista


for letra in a:
    print(letra) #Recorrer
    
print(a[1])


#Extra
def palabras(palabra1, palabra2):
    
    #Palíndromas
    print(f"La palabra {palabra1} es palíndroma? {palabra1.lower() == palabra1[::-1].lower()}")
    print(f"La palabra {palabra2} es palíndroma? {palabra2.lower() == palabra2[::-1].lower()}")
    
    #Anagramas
    print(f"¿{palabra1} es anagrama de {palabra2}? : {sorted(palabra1) == sorted(palabra2)}")
    
    #Isograma
    print(f"¿{palabra1} es un isograma? : {len(palabra1) == len(set(palabra1))}")
    print(f"¿{palabra2} es un isograma? : {len(palabra2) == len(set(palabra2))}")
    
    def isogram(word_string) -> bool:
    
        word_dict = dict()
        for word in palabra2:
            word_dict[word] = word_dict.get(word, 0) + 1
        
        isograma = True   
        values = list(word_dict.values())
        isogram_len = values[0]
        for word_count in values:
            if word_count != isogram_len:
                isogram = False
                break
        return isograma
        
    print(f"¿{palabra1} es un isograma? : {isogram(palabra1)}")
    print(f"¿{palabra2} es un isograma? : {isogram(palabra2)}")
    
    
palabras("radar", "pythonpythonpythonpython")
#palabras("amor", "roma")