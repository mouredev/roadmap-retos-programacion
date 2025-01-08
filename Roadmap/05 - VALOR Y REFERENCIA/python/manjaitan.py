# asignar variales por valor

var1 = 10
print (var1)

# asignar por referencia

list_refer_a = [1,2]
list_refer_b = list_refer_a
list_refer_b.append(3)
print (list_refer_a)
print (list_refer_b)

 # Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 # *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.

variable2 = [10,20,30]

def byRefer (entrada):
    entrada.append (40)

byRefer(variable2)
print (variable2)




