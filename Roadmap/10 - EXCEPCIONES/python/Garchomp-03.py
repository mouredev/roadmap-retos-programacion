try:
    division = 10 / 0
except ZeroDivisionError as error:
    print(f'Error: {error}')
else:
    print('Sin errores')
finally:
    print('El proceso continua')

# EXTRA

def operaciones(num1, num2, num3):
    division = num1 / num2 + num3


try:
    operaciones(True, 5, 6)
except ValueError as e:
    print(f'Error: {e}')
except TypeError as e:
    print(f'Error: {e}')
except Exception as error_personalizado:
    print(f'Error: {error_personalizado}')
else:
    print('No hay errores')
finally:
    print('Fin del proceso')