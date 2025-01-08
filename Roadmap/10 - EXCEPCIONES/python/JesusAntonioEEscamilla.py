# #10 - Python -> Jesus Antonio Escamilla

"""
EJERCIÓ
"""
def division_by_zero():    
    try:
        print(10/0)
    except Exception as e:
        print(f"Se encontró un error: {e} {(type(e).__name__)}")

def access_index_invalid():
    try:
        print([1,2,3,4][4])
    except Exception as e:
        print(f"Se encontró un error: {e} {(type(e).__name__)}")

# Ejemplo
print("\nIntentando dividir por cero:")
division_by_zero()
    
print("\nIntentando acceder a un índice inválido:")
access_index_invalid()



"""
EXTRA
"""
# Pendiente