"""
* EJERCICIO:
* Explora el concepto de manejo de excepciones según tu lenguaje.
* Fuerza un error en tu código, captura el error, imprime dicho error
* y evita que el programa se detenga de manera inesperada.
* Prueba a dividir "10/0" o acceder a un índice no existente
* de un listado para intentar provocar un error.
"""

def dividir(x: int, y: int):
    print(f"vamos a intentar dividir '{x}' entre '{y}'")
    try:
        return x/y;
    except ZeroDivisionError:
        print("❌ No puedes dividir entre 0, melón! 🍈")
        return None

a = 10
b = 0

dividir(a, b)

lista = ['a', 'b','c']
print(lista.__len__())
for i in range(0, lista.__len__()+1):
    try:
        print(f"pos {i}: {lista[i]}")
    except IndexError as e:
        print(f"❌ {type(e).__name__}:Te has salidon del array!")



