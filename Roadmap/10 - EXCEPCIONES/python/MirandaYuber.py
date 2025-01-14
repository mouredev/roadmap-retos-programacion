print("""
EXCEPCIONES
""")

try:
    resultado = 10 / 0
except Exception as e:
    print(e)

try:
    languages = ['PHP', 'Python', 'JavaScript']
    print(languages[3])
except Exception as e:
    print(e)

try:
    suma = number_1 + 1
    print(suma)
except Exception as e:
    print(e)

try:
    resta = '2' - 1
    print(resta)
except Exception as e:
    print(f'Error: {e} ({type(e).__name__})')

print("""
EXTRA
""")


class NegativeNumberError(Exception):
    pass


def operaciones_aritmeticas(number_1: int, number_2: int, operation: int):
    if operation == 4 and number_2 == 0:
        raise ZeroDivisionError()
    elif operation > 4 or operation < 1:
        raise ValueError()
    resultado = 0
    match operation:
        case 1:
            resultado = number_1 + number_2
        case 2:
            resultado = number_1 - number_2
        case 3:
            resultado = number_1 * number_2
        case 4:
            resultado = number_1 / number_2

    if resultado < 0:
        raise NegativeNumberError('El resultado de la operación ha sido negativo')

    print()
    print(f'El resultado de la operación es: {resultado}')


try:
    print("""
    1. Suma
    2. Resta
    3. Multiplicación
    4. División
    """)
    operation = int(input('Ingrese el número corespondiente a la operación que desea resolver: '))
    number_1 = int(input('Ingrese el primer número: '))
    number_2 = int(input('Ingrese el segundo número: '))

    operaciones_aritmeticas(number_1, number_2, operation)

except ZeroDivisionError as error:
    print(f'({type(error).__name__}): El número 2 tiene que ser difente de cero cuando quiera dividir')

except ValueError as error:
    print(f'({type(error).__name__}): Debe ingresar un valor correspondiente a las operaciones disponibles')

except NegativeNumberError as error:
    print(f'({type(error).__name__}): {error}')

except Exception as error:
    print(f'({type(error).__name__}): Error inesperado: {error}')

else:
    print('El programa se ejecuto sin ningun problema')

finally:
    print('El programa finalizo')























