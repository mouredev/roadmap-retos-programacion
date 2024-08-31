'''
  EJERCICIO
'''


def divide(dividend, divisor):
    try:
        quotient = dividend / divisor
        print(f'{dividend} / {divisor} = {quotient}')
    except ZeroDivisionError as e:
        print(f'Error: {type(e).__name__}, no se puede dividir por cero.')


divide(15, 5)
divide(19, 4)
divide(321, 0)


def showList(list):
    try:
        if not list:
            raise IndexError
        print('List items:')
        for item in list:
            print(f'-{item}')
    except IndexError as e:
        print(f'Error: {type(e).__name__}, la lista esta vacía.')


showList([1, 5, 53, 'Cuatroscientos quince'])
my_list = [10, 'str', True]
showList(my_list)
list_empty = []
showList(list_empty)


'''
  EXTRA
'''


class MyError(Exception):
    def __init__(self, msg):
        self.message = msg


def add():
    num1 = input('Dame un número: ')
    num2 = input('Dame otro número: ')
    exceptDetect(num1, num2)
    print('Ejecución finalizada. ;D')


def exceptDetect(num1, num2):
    try:
        if num1.lower() == 'error' or num2.lower() == 'error':
            raise MyError('Invocaste este error')
        op1 = int(num1)
        op2 = int(num2)
        print(f'{op1} + {op2} = {op1 + op2}')
        print('No se produjo ningún error')
    except ValueError as e:
        print(f'Error: {type(e).__name__}, no introduciste un número válido')
    except KeyboardInterrupt as e:
        print(f'Error: {type(e).__name__}, haz interrumpido el programa')
    except MyError as e:
        print(f'Error: {type(e).__name__}, {e.message}')


add()
