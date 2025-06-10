# VARIABLES por valor y por referencia

# Por valor
"""
x = 10
    def funcionValor(entrada):
        entrada = 0
        print(entrada)
        
    funcionValor(x)
"""
# Por referencia
x = [10, 20, 30]
def funcionReferencia (entrada):
    entrada.append(40)
    
funcionReferencia(x)
print(x)

"""
Extra
"""
# Por valor
def swap_by_value(a, b):
    a, b = b, a
    return a, b

# Variables originales
x = 10
y = 20

# Intercambiar por valor
new_x, new_y = swap_by_value(x, y)

print("Intercambio por valor:")
print(f"Original x: {x}, Original y: {y}")
print(f"Nuevo x: {new_x}, Nuevo y: {new_y}")

def swap_by_reference(a, b):
    a[0], b[0] = b[0], a[0]

# Variables originales
x_ref = [10]
y_ref = [20]

# Intercambiar por referencia
swap_by_reference(x_ref, y_ref)

print("Intercambio por referencia:")
print(f"Original x_ref: {10}, Original y_ref: {20}")
print(f"Nuevo x_ref: {x_ref[0]}, Nuevo y_ref: {y_ref[0]}")
