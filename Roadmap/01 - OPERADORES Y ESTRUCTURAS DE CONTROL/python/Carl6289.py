# Operadores aritméticos
resultado_1 = 55 + 45 # Suma
print(resultado_1)

resultado_2 = 1000 - 500 # Resta
print(resultado_2)

resultado_3 = 7 * 8 # Multiplicación
print(resultado_3)

resultado_4 = 600 / 200 # División
print(resultado_4)

# Operadores lógicos
# Ejemplo de and
calificacion = 16
pago = True
entregar_certificado = (calificacion >= 15) and pago 
print(f"¿Entregar certificado? {entregar_certificado}")

# Ejemplo de or
padre = False
gasto = 5092
descuento = padre or (gasto >= 5000)
print(f"¿Descuento del día del padre? {descuento}")

# Ejemplo de not
alumno_becado = False
alumno_no_becado = not alumno_becado
print(f"¿El alumno está becado? {alumno_becado}")
print(f"¿El alumno no está becado? {alumno_no_becado}")

# Operadores de comparación
# Ejemplo de igualdad y desigualdad
x = 75
y = 103
es_igual = x == y
print(f"¿Es igual? {es_igual}")

es_distinto = x != y
print(f"¿Es distinto? {es_distinto}")

# Ejemplo de mayor y menor
edad = 17
mayor_de_edad = edad >= 18
print(f"¿Es mayor de edad? {mayor_de_edad}")

menor_de_edad = edad < 18
print(f"¿Es menor de edad? {menor_de_edad}")

# Operadores de asignación
saldo = 75
saldo += 25
print(saldo)

# Operadores de identidad
# Ejemplo de is
a = 1
b = a
print(a is b)

# Ejemplo de is not
c = 3
d = 4
print(c is not d)

# Operadores de pertenencia
# Ejemplo de in
desarrollador = ["maria", "luis", "karina", "carlos"]
es_desarrollador = "carlos" in desarrollador
print(f"¿Carlos es desarrollador? {es_desarrollador}")

# Ejemplo de not in
edad_nino = (8, 6, 9, 11)
hay_10 = 10 not in edad_nino
print(f"¿No hay niños de 10 años? {hay_10}")

# Operadores de bits
# Ejemplo de &
num_1 = 10
num_2 = 4
resultado_5 = num_1 & num_2
print(resultado_5)

# Ejemplo de |
num_3 = 10
num_4 = 4
resultado_6 = num_3 | num_4
print(resultado_6)

# Ejemplo de ^
num_5 = 10
num_6 = 4
resultado_7 = num_5 ^ num_6
print(resultado_7)

# Ejemplo de <<
num_7 = 5
resultado_8 = num_7 << 2
print(resultado_8)

# Ejemplo de >>
num_8 = 20
resultado_9 = num_8 >> 2
print(resultado_9)

# Operador de concatenación (+)
saludo = "Hola"
nombre = "Brais"
frase = saludo + " " + nombre + "!"
print(frase)

# Operador de repetición
risa = "ja" * 5
print(risa)

# Operador de indexación
colores = ["amarillo", "azul", "rojo"]
primer_color = colores [0]
print(primer_color)

tercer_color = colores [2]
print(tercer_color)

# Operador de segmentación
seleccion_color = colores [0:2]
print(seleccion_color)

# Estructuras de control condicionales
# Ejemplo de if y else
calificacion_2 = 11
if calificacion_2 >= 10:
   print("Aprobado!")
else:
   print("Reprobado!")

# Ejemplo de if, elif y else
calificacion_3 = 18
if calificacion_3 >= 19:
   print("Calificación: A")
elif calificacion_3 >= 15:
   print("Calificación: B")
elif calificacion_3 >= 10:
   print("Calificación: C")
elif calificacion_3 >= 6:
   print("Calificación: D")
else:
   print("Calificación: E")

# Estructuras de control iterativas
# Ejemplo del bucle for
pasos = ["1. Calentar el sarten", "2. Romper el huevo", "3. Sazonar y cocinar", "4. Servir"]
for receta in pasos:
   print(receta)

# Ejemplo del bucle while
contador = 1
while contador <= 10:
   print(contador)
   contador += 1 

# Estructura de control de excepciones
# Ejemplo de try y except
capitales = {"Argentina": "Buenos Aires", "Chile": "Santiago"}
pais_buscado = "Venezuela"
try:
    capital = capitales[pais_buscado]
    print(f"La capital de {pais_buscado} es {capital}")
except KeyError:
    print(f"El país '{pais_buscado}' no se encuentra en la base de datos.")
    print("El programa sigue funcionando.")

# Ejercicio de dificultad extra
print("***Programa 01***")
contador_prog = 10
while contador_prog <= 55: 
   if contador_prog % 2 == 0 and contador_prog != 16 and not contador_prog % 3 == 0:
    print(contador_prog)
   elif contador_prog == 55:
      print(contador_prog)
   contador_prog += 1