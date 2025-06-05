nombre_esudiante = input("ingresa tu nombre: ")

lista_de_notas = []
contador = 1 

#uso del bucle while
while contador <=3:
    lista_de_notas.append(float(input("Ingresa una calificación: ")))
    contador += 1

#uso de operadores aritmeticos para el promedio
print(lista_de_notas)
promedio_de_notas = (sum(lista_de_notas))/3
print(promedio_de_notas)

#condicional y uso del operador lógico and
if promedio_de_notas >= 6 and all(nota > 4 for nota in lista_de_notas):
    print(f"El estudiate {nombre_esudiante} a sido aprobado")
else:
    print(f"El estudiante {nombre_esudiante} a sido reprobado")


"""
DIFICULTAD EXTRA
"""

for i in range(10,56,2):
    if i % 3 != 0 and i != 16:
        print(i)