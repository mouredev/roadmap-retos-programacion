from datetime import datetime
#  EJERCICIO:
#  * Explora el concepto de funciones de orden superior en tu lenguaje 
#  * creando ejemplos simples (a tu elección) que muestren su funcionamiento.
#  *

#Funcion map
print("Convertidor de pesos mexicanos a dolares")
money = [5, 20, 1, 10]
convert = list(map(lambda moneda: moneda * 18.00, money ))
print(f"La conversion de dinero que tenias en tu cajita es la siguiente{money} a {convert}")

#funcion max and min
print("Buscador de precios de productos en el mercado")
list_products = [20000, 18000, 21000, 22000, 17500]
max_value = max(list_products)
min_value = min(list_products)
print(f"El precio mas alto del prodcto en el mercado es {max_value} y precion mas bajo es de {min_value}")

#funcion flitrer
print("Filtrador de productos con mas del 50%")
porcent_products = [{
    "name": "Reloj Casio",
    "descuento" : "50%"},
    {
    "name": "Pantalla LG",
    "descuento" : "20%"},
    {
    "name": "Liquadora Ninja",
    "descuento" : "52%"},
    {
    "name": "Colchon Matrimonial",
    "descuento" : "60%"},
    {
    "name": "Laptop Asus",
    "descuento" : "10%"}
    ]
func_filter = list(filter(lambda f : f["descuento"] >= "50%" , porcent_products))
func_desc = list(map(lambda z : z["name"], func_filter))
print(func_desc)

#funcion sorted
print("Macro que ordena usuarios por edad de menor a mayor")
list_age = [19,15,14,16,28,30,22,20,18]
usersbyage = sorted(list_age, reverse = False)
print(f"Los usuarios estan acomadados por edad{usersbyage}")



#  DIFICULTAD EXTRA (opcional):
#  * Dada una lista de estudiantes (con sus nombres, fecha de nacimiento y 
#  * lista de calificaciones), utiliza funciones de orden superior para 
#  * realizar las siguientes operaciones de procesamiento y análisis:
#  * - Promedio calificaciones: Obtiene una lista de estudiantes por nombre
#  *   y promedio de sus calificaciones.
#  * - Mejores estudiantes: Obtiene una lista con el nombre de los estudiantes
#  *   que tienen calificaciones con un 9 o más de promedio.
#  * - Nacimiento: Obtiene una lista de estudiantes ordenada desde el más joven.
#  * - Mayor calificación: Obtiene la calificación más alta de entre todas las
#  *   de los alumnos.
#  * - Una calificación debe estar comprendida entre 0 y 10 (admite decimales).

alumns = [
    {
    "name" : "Tomas",
    "fechanacimiento" : "1997/5/11",
    "calificaciones" : [10,9,8,8,8]},
    {
    "name" : "Angel",
    "fechanacimiento" : "2000/4/08",
    "calificaciones" : [7,8.5,9,10,7]},
    {
    "name" : "pepito",
    "fechanacimiento" : "2002/11/03",
    "calificaciones" : [6,6,6,9,7]},
    {
    "name" : "panchito",
    "fechanacimiento" : "2006/10/28",
    "calificaciones" : [10,9,10,9,9.5]},
    {
    "name" : "Juan",
    "fechanacimiento" : "2007/4/15",
    "calificaciones" : [8,6,7,6,7]}
    ]


def fun_prom (datos) :
    notas  = datos["calificaciones"] 
    promedio = sum(notas) / len((notas))
    return [datos["name"], promedio]
list_prom = list(map(fun_prom,alumns))
print(f"\nLista de Alumnos y promedio de sus calificaciones {list_prom}")


better_alumn = list(filter(lambda list_better : list_better[1] >= 9, list_prom))
name_better_alumn = list(map(lambda x: x[0], better_alumn))
print(f"\nLista de los alumnos con mejores promedios{name_better_alumn}")

func_date =  lambda fechas : datetime.strptime(fechas["fechanacimiento"], "%Y/%m/%d")
almnbydate = list(sorted(alumns, key= func_date, reverse = True))
print(f"\nEsta es la lista de alumnos ordenada por fecha de nacimiento{almnbydate}")


find_cal = list(map(lambda calificaciones : max(calificaciones["calificaciones"]), alumns))
mayor_cal = max(find_cal)
print(f"\nLa calificacion mas alta es de: {mayor_cal}")