#? Imprimir numeros del 1 al 10
print("for:")
for i in range(1, 11):
    print(i)

print("while")
i = 1
while i <= 10:
    print(i)
    i += 1

print("recurvivo")
def numeros(n: int) -> int:
    print(n)
    if n < 10:
        numeros(n+1)
        
numeros(1)

#! Extra

lista = [1,2,3,4,5,6,7,8,9,0]
diccionario = {
    "1" : "uno",
    "2" : "dos",
    "3" : "tres",
    "4" : "cuatro",
    "5" : "cinco",
    "6" : "seis",
    "7" : "siete",
    "8" : "ocho",
    "9" : "nueve",
    "0" : "cero"
}
tupla = (1,2,3,4,5,6,7,8,9,0)
sets = {"1","2","3","4","5","6","7","8","9","0"}
texto = "hola mundo"

print("Lista")
for i in lista:
    print(i)

print("diccionario")
for i in diccionario:
    print(i + diccionario[i])

print("tupla")
for i in tupla:
    print(i)

print("sets")
for i in sets:
    print(i)

print("Texto")
for i in texto:
    print(i)