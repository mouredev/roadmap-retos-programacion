# /*
#  * EJERCICIO:
#  * Explora el concepto de funciones de orden superior en tu lenguaje 
#  * creando ejemplos simples (a tu elección) que muestren su funcionamiento.
#  *
#  * DIFICULTAD EXTRA (opcional):
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
#  */

# Pasar una función como argumento a otra función.

def Get_something(f,x):
    return f(x)
d = {"a":1,"b":2,3:"c"}
k = Get_something(dict.keys,d )
print(f"las Keys son {list(k)}")

# Retornar funcion

def Get_etwas():
    def Get_value(dddd: dict):
        return dddd.values()
    return Get_value

values = Get_etwas()
print(f"los Valores son {list(values(d))}")

# oporque Get_etwas retorna una funcion
print(Get_etwas()(d))

# funciones del sistema
# map
a= [9,"8",7,True,5,[1,2,3],{11,2,3},(2,4,5),d,0.1]
type_all = list(map(type,a))
print(type_all)

# filter
def only_int(v):
    return isinstance(v,(int)) and not isinstance(v,(bool))

only_digi = list(filter(only_int,a))
print(only_digi)

# reduce
a = [1,2,3,4,5,6]
from functools import reduce


def sum_all(n,m):
       
         return n+m 
# n es el valor acumulativo y el que retorna al final
       
suma = reduce(sum_all,a)
print(suma)


# sorted
 
ordenado = sorted(a, key=lambda x: -x)
print(ordenado)

# EXTRA
import datetime,random,string

def random_name(size = 8):
     letter = string.ascii_letters
     return ''.join( random.choice(letter)  for _ in range(size))

class Student:
     name: str
     date_born: datetime.datetime
     notes: dict
     average: float
     best_note: dict

     def __init__(self,name,date,notes, ave = 0, ) -> None:
          self.name = name
          self.date_born = date
          self.notes = notes
          self.average = ave
          self.best_note ={}
           

     def set_best_note(self):
        
        best_notes =  (sorted(self.notes.items(), key= lambda x: x[1]))
        # best_notes.reverse()
        # print("set beste note", type(best_notes[0]),best_notes[0][0], best_notes[0][1])
        self.best_note[best_notes[0][0]]  =   best_notes[0][1]
         


     def set_average(self):
        notes_temp = []
        for _,i in self.notes.items():
             notes_temp.append(i)
        suma_note = reduce(lambda x,y: x+y,notes_temp)
        result = round(suma_note/len(notes_temp),2)
        self.average = result
    
     def display(self):
          print(f" Nombre: {self.name}\n Fecha Nac: {self.date_born}\n Notas: {self.notes}\n Promedio: {self.average}\n")

student = []
 
for i in range(10):
     
     student.append(
          Student(random_name(),
          datetime.date(random.randint(1990,2020),random.randint(1,12),random.randint(1,30)),
          {"mate":round(random.uniform(5.0,10.0),2), "L":round(random.uniform(5.0,10.0),2), "G":round(random.uniform(5.0,10.0),2), "E":round(random.uniform(5.0,10.0),2)}
          ))

  
     
     

print("Listado Original")
for i in student:
    i.set_average()
    i.display()

list_average = sorted(student, key = lambda x: -x.average)
print("Listado ordenado por promedio")
for i in list_average:
    i.display()

print("Listado ordenado alumnos con promedio superior a 9")
best_student = list(filter(lambda x: x.average >=9, student))
if  len(best_student):
     
    for i in best_student:
        i.display()
else:
     print("no hay estudientes con nota mayores a 9")

print("Listado ordenado por edad")
age = sorted(student,key=lambda x: x.date_born)
age.reverse()
for i in age:
     i.display()

 

print("Listado con mejor nota de cada alumno")
# for i in student:
#      i.set_best_note()
#      print(f" Nomber: {i.name} mejor nota  { i.best_note}")

print(list(map(lambda s:(s.set_best_note(),f"Nomber: {s.name} mejor nota: { s.best_note}")[1],student)))







 