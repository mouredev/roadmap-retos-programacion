
numero = 1
while numero <= 10:
    print(numero)
    numero += 1

for i in range (1, 11):
    print(i)

def numeros(numero):
    if numero <= 10:
        print(numero)
        numero += 1
        numeros(numero)

numeros(1)

# DIFICULTAD EXTRA:


# Siempre usando el for hay muchas opciones, pero no deja de ser un for