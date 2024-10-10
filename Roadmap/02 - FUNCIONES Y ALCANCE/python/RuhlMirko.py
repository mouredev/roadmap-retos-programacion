print("Funciones")


def hola_mundo():  # Funcion que imprime en consola
    print("¡Hola mundo!")


def return_hola_mundo():  # Funcion que devuelve un valor
    return "¡Hola Python!"


def suma(a, b):  # Funcion con argumentos
    return a + b


def greet_user(user, language="Python"):  # Funcion con argumento predeterminado
    return f"Hello, {user}. You are working in {language}"


def greet_the_team(*names):  # Funcion con numero variable de argumentos
    for name in names:
        print(f"Hello, {name}")


def greet_the_dictionary(**search_term):  # Funcion con numero variable de argumentos
    for word, definition in search_term.items():
        print(f"{word} definition: {definition}")


def al_cuadrado(a, b):  # Funcion dentro de otra funcion y con multiples return
    resultado_suma = suma(a, b)  # Llamada de funcion externa
    resultado_cuadrado = resultado_suma ** 2
    return resultado_cuadrado, resultado_suma


hola_mundo()
print(return_hola_mundo())
print(suma(b=5, a=2))  # Ejemplo de envio de argumentos en orden especifico
print(greet_user("Mirko"))
greet_the_team("Python", "JavaScript", "C++")
greet_the_dictionary(
    python="A language made for better readability",
    javascript="A language good por OOP",
    c="An improved version of C"
)

print("\nFunciones dentro de funciones")
result_cuadrado, result_suma = al_cuadrado(5, 2)  # Multiples return
print(f"Resultado de suma: {result_suma}")
print(f"Resultado al cuadrado: {result_cuadrado}")

print("\nFunciones de Pyhton")
print(dir(" "))  # Devuelve los comandos posibles del elemento
print(len(return_hola_mundo()))  # Devuelve la longitud del elemento
print(return_hola_mundo().upper())  # Pone en mayusculas el string dado
print(type(suma(5, 2)))  # Devuelve el tipo del elemento
print(("a", "b", "c", "d")[slice(1, 3)])  # Separa un objeto de sus otras partes
print(float("6.6"))  # Convierte un string a un float
print(max(2, 3, 5, 7, 11, 1))  # Devuelve el numero mas grande de un objeto
print(round(6.8))  # Redondea un numero float

print("\nVariable LOCAL y GLOBAL")


def hello_python():
    print(f"Hello, {language}")


language = "Python"  # Variable Global
print(language)
hello_python()

print("\nDificultad Extra:")


def fizzbuzz(a, b):
    count_numbers = 0
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(a + b)
        elif i % 3 == 0:
            print(a)
        elif i % 5 == 0:
            print(b)
        else:
            count_numbers += 1
            print(i)
    return count_numbers


contador_de_numeros = fizzbuzz("Fizz", "Buzz")
print(f"Cantidad de numeros mostrados: {contador_de_numeros}")
