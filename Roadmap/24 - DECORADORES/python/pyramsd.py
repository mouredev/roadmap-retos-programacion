def decorador(func):
    def opp(a, b):
        print(f'llamada a la funcion {func.__name__}')
        resultado = func(a, b)
        return ''.join([f'Resultado de la funcion {func.__name__}: ', str(resultado)])
    return opp

@decorador
def suma(a,b):
    return a+b

@decorador
def resta(a,b):
    return a-b

print(suma(5, 5))
print(resta(5, 5))


'''
EXTRA
'''
def contador_de_llamada(func):
    func.contador = 0
    def counter():
        func.contador += 1
        print(f'Se ha llamado {func.contador} veces a la funcion {func.__name__}')
        return func
    return counter

@contador_de_llamada
def llamar_funcion():
    print()

llamar_funcion()
llamar_funcion()
