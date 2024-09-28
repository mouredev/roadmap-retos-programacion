def decorador(funcion):
    def wrapper(*a, **b):
        print("La función no se ha llamado")
        funcion(*a, **b)
        print("La función ha sido llamada")
        return 
    return wrapper
       
@decorador
def funcion(a, b):
    pass

funcion(1, 2)
        
print("")
print("***RETO EXTRA***")
print("")

def contar(funcion):
    def wrapper(*a):
        wrapper.contador += 1
        funcion(*a)
        veces = 'vez' if wrapper.contador == 1 else 'veces'
        print(f"La función ha sido llamada { wrapper.contador } { veces }")
        
    wrapper.contador = 0
    return wrapper

@contar
def sumar(a, b):
    return a + b

sumar(1, 2)
sumar(3, 4)
sumar(5, 6)
