languages = ['python', 'c', 'php']

#Añade un elemento al final
languages.append('ruby')

#Añade un elemento al principio
languages.insert(0, 'java') 

#Añade varios elementos al bloque final
other_languages = ['javascript', 'rust']
languages.extend(other_languages)

#Añade varios elementos en una posición concreta
languages[2:2] = ['Go', 'Kotlin']

#Elimina elementos de una posición concreta
languages.pop(4)

#Actualiza el valor de una posición concreta
languages[2] = 'go'

#Comprueba si un elemento esta en un conjunto
if 'python' in languages:
    print("Elemento encontrado")
else:
    print("Elemento no encontrado")

#Elimina todo el contenido del conjunto
languages.clear()

print(languages)

#EXTRA

number_list_1 = {1, 2, 3, 5}
number_list_2 = {4, 5, 6, 7}

#Unión
union_list = number_list_1.union(number_list_2)
print(f"La unión de los dos conjuntos es: {union_list}")

#Intersección
intersection_list = number_list_1.intersection(number_list_2)
print(f"La intersección de los dos conjuntos es: {intersection_list}")

#Diferencia
difference_list = number_list_2.difference(number_list_1)
print(f"La diferencia entre los dos conjuntos es: {difference_list}")

#Diferencia simétrica
symmetric_list = number_list_1.symmetric_difference(number_list_2)
print(f"La diferencia simétrica de los conjuntos es: {symmetric_list}")