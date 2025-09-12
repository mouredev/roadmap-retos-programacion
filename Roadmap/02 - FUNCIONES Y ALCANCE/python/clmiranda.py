# Funciones sin parámetros ni retorno
def hello():
    print("Hello World from Python")

hello()


from datetime import datetime
def actual_date():
    now = datetime.now()
    print(now.strftime("%d/%m/%Y"))

actual_date()


# Funciones con parámetros y retorno
def even_numbers(lst: [int]) -> [int]:
    return [i for i in lst if i % 2 == 0]

print(even_numbers([3, 8, 19, 28, 46, 105, 17, 34, 79]))


# Funciones anidadas
def calculate_discount(price: float, discount: int) -> float:
    return price - price * float(f'0.{discount}')

def calculate_total_price(product: str, price: float, discount: int) -> str:
    discount_applied = calculate_discount(price, discount)
    return f"The {product} price with the discount applied is {round(discount_applied, 2)}"

print(calculate_total_price("laptop HP", 4700.90, 15))


# Funciones propias de Python
values = [17, 4, 89, 103, 45, 28, 70, 8]

print(f"Valor mínimo: {min(values)}, Valor maximo: {max(values)}")
print(sorted(values, reverse=True))


# Variable Local
var_local = "Esta es una variable local fuera de una función"
def funcion_local():
    var_local = "Hola Mundo desde una función con variable local"
    print(var_local)

print(var_local)
funcion_local()


# Variable Global
var_global = "Esta es una variable global"
def funcion_global():
    global var_global
    var_global = "Este es el nuevo valor de la variable global"
    print(var_global)

funcion_global()
print(var_global)


# Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
def reto(txt1: str, txt2: str) -> int:
    counter = 0
    for i in range(1, 101):
        if i % 3 == 0:
            print(txt1)
        elif i % 5 == 0:
            print(txt2)
        elif i % 3 == 0 and i % 5 == 0:
            print(f"{txt1}{txt2}")
        else:
            print(i)
            counter += 1
    return counter

print(f"Cantidad de veces que se han impreso números en lugar de textos: {reto("Hello", "World")}")