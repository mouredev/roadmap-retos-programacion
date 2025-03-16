# for -> Se ejecuta un número determinado de veces
for i in range(1, 11):
    print(i, end=" ")
print("\n")

# While -> Se ejecuta mientras la condición sea verdadera
i = 1
while i <= 10:
    print(i, end=" ")
    i += 1
print("\n")

# Recursividad -> La función se llama a sí misma
def cuenta_diez(i=1):
    if i <= 10:
        print(i, end=" ")
        cuenta_diez(i + 1)

cuenta_diez()
print("\n")

# Map -> Aplica una función a cada elemento de una lista
def impresion(i):
    print(i, end=" ")

list(map(impresion, range(1, 11)))
print("\n")