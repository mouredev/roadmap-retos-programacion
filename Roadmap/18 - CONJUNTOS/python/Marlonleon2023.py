"""* EJERCICIO:
 * Utilizando tu lenguaje crea un conjunto de datos y realiza las siguientes
 * operaciones (debes utilizar una estructura que las soporte):
 * - Añade un elemento al final.
 * - Añade un elemento al principio.
 * - Añade varios elementos en bloque al final.
 * - Añade varios elementos en bloque en una posición concreta.
 * - Elimina un elemento en una posición concreta.
 * - Actualiza el valor de un elemento en una posición concreta.
 * - Comprueba si un elemento está en un conjunto.
 * - Elimina todo el contenido del conjunto.
 """

print("-----------------Ejercicios---------------")

listConjunto =["hola","marlon","casa","avion","carro","persona","nombre"]
# Se añade un elmento al final
listConjunto.append("edifico")
# Se añade un elemeto al principio
listConjunto.insert(0,"feliz")
# varios elementos en el bloque final
agregarbloqueFinal=["escuela","colegio","aeropueto","viaje"]
listConjunto.extend(agregarbloqueFinal)
# Añadir varios elementos en bloque en una posicion concreta
agregarEspecifico=["libro","bolso","papel"]
posicion=5
listConjunto[posicion:posicion]=agregarEspecifico

#Elimina un elemento en una posición concreta.
listConjunto.remove("carro")
#Actualiza el valor de un elemento en una posición concreta.
posicion1=3
nuevoValor="Bacaciones"
listConjunto[posicion1]=nuevoValor
print(type(listConjunto))
print(listConjunto)
#Comprueba si un elemento está en un conjunto.
print("Comprobacion si un elemento estaen un conjunto")
print("Bacaciones" in listConjunto)
#Elimina todo el contenido del conjunto.
print("Eliminacion del contenido del conjunto")
listConjunto.clear()
print("marlon" in listConjunto)


""" * DIFICULTAD EXTRA (opcional):
 * Muestra ejemplos de las siguientes operaciones con conjuntos:
 * - Unión.
 * - Intersección.
 * - Diferencia.
 * - Diferencia simétrica."""
 
print("----------------Dificulta Extra----------------")
 
instrumentosComunes={"guitarra","tiple","flauta"}
instrumentosRaros={"arpa","birimbao","derbake"}
# Unión.
print("Union------------")
conjuntoInstrumentos=instrumentosComunes.union(instrumentosRaros)
conjuntoInstrumentos=instrumentosComunes|instrumentosRaros
print(conjuntoInstrumentos)
#Intersección.
print("Intersección----------------")
number1={1,2,3,4}
number2={4,5,6,6,7,1}

interset=number1.intersection(number2)
interset=number1 & number2
print(interset)

#Diferencia.
print("Diferencia---------")
diferencia=number1.difference(number2)
diferencia=number1-number2
print(diferencia)

# Diferencia Simetrica
print("Diferencia Dimetrica-----------")
diferSimetrica=number1.symmetric_difference(number2)
diferSimetrica=number1 ^ number2
print(diferSimetrica)


