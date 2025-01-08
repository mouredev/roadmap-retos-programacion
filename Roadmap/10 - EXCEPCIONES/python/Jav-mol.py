# --- 10-Excepciones ---
# --- Javier Molina ---

# Capturar un Error
try:
    print(10 / 2)
    print(10 / 0)
except Exception as e:
    print(f'Error: [{e}] [{type(e).__name__}]')
    
        
# --- Extra ---

class NumerosIguales(Exception):
    pass

try:
    a = int(input('Ingrese un numero: '))
    b = int(input('Ingrese un numero: '))

    if a == b:
        raise NumerosIguales('Los numeros son iguales')
    
    a / b
    
except Exception as e:
    print(f'Error: [{e}] [{type(e).__name__}]')
    