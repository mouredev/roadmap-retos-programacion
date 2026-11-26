# python no tiene asignaciones de variables por valor o referencia, todo es igual, pero el comportamiento depende del tipo de objeto.
# Mutable: list, dict, set 
# Inmutable: int, str, tuple

# Una variable no guarda un dato, sino que, es una etiqueta que apunta a un objeto, en este caso, a y b apuntan al mismo objeto, por ende si hago un append en b, y despues imprimo a, me va a salir lo mismo que en b.
a = [1,2,3] 
b = a

b.append(4)
print(a) 

#Con los numeros es distinto, estos son inmutables, o sea que, no se puede cambiar el objeto 5 por dentro. O sea que, "y" no modifica el objeto 5, sino que hace que y apunte a otro objeto que seria 6. x sigue apuntando a 5.
x = 5
y = x
y += 1

#Con las funciones es igual, al pasar un argumento pasa lo mismo que b = a, el paramentro es una etiqueta nueva apuntando al mismo objeto.
def funcion(numero, lista):
    numero = numero + 1
    lista.append(4)

num = 3
lista_1 = [1,2,3]
funcion(num, lista_1)
print(num, lista_1)

#----------------EXTRA------------------
x = 10
y = 1
numeros = [1,2,3,4]
letras = ["a","b","c"]
def programa1(num1, num2):
    num1 , num2 = num2 , num1
    return num1, num2

def programa2(num_lista,let_lista):
    num_lista,let_lista=let_lista,num_lista
    num_lista.append(5)
    let_lista.append("d")
    return num_lista,let_lista

numero1,numero2 = programa1(x,y)
lista1,lista2 = programa2(numeros,letras)


print(x,y,numero1,numero2, "-----" ,numeros,letras, lista1,lista2)

