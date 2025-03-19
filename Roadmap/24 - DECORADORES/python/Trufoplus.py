###############################################################################
###  EJERCICIO: DECORADORES
###############################################################################

### Decorador simple:
def my_decorator(func):
    """
    Un decorador que agregar funcionalidades a tus funciones, la 
    funcion se le pasa como argumento.
    """
    def wrap ():
        """
        wrap significa envolver, es lo que envuelve a la funcion
        """
        print("Inicializando la funcion...")
        func()
        print("Terminando el tema que ya es hora...")
    return wrap

@my_decorator #Con el @ aplico el decorador creado a la funcion
def my_func():
    """
    Una funcion chorra para probar que el decorador funciona
    """
    print("Esta es mi funcion que hace cosas molonas")

print('\nDecorador simple:')
my_func()



### Decorador con argumentos:
def my_decorator_with_argument(argument):
    """
    Un decorador al que se le pueden pasar argumentos
    """
    def my_decorator(func):
        def wrap():
            print(f"{argument}, Inicializando la funcion...")
            func()
            print("Terminando el tema que ya es hora...")
        return wrap
    return my_decorator

@my_decorator_with_argument("Hola") #Decorador con argumentos
def my_func():
    print("Esta es mi funcion que hace cosas molonas")

print('\nDecorador con argumentos:')
my_func()



### Decorador para funciones con argumentos
def my_decorator(func):
    def wrap(*args, **kwargs):
        print("Inicializando la funcion...")
        result = func(*args, **kwargs)
        print("La funcion ha terminado")
        return result
    return wrap

@my_decorator 
def my_func(a:int, b:int):
    print(f'{a} + {b} = {a + b}')


print('\nDecorador para una funcion con argumentos:')
my_func(4, 5)


### Aplicando decoradores a una clase:
class MyClass:
    @my_decorator
    def method(self, value:int):
        print(f'Su valor es {value}')


print('\nAplicando un decorador a una clase:')
object = MyClass()
object.method(1980)



### Aplicando varios decoradores a una misma funcion (Decoradores anidados)
def my_first_decorator(func):
    def wrap():
        print('Este es mi primer decorador: ')
        func()
        print('fin del primer decorador')
    return wrap

def my_second_decorator(func):
    def wrap():
        print('Este es mi segundo decorador: ')
        func()
        print('fin del segundo decorador')
    return wrap


@my_first_decorator
@my_second_decorator
def my_func():
    print('Esta es mi funcion')

print('\nUsando varios decoradores para en una funcion: ')
my_func()



###############################################################################
### DIFICULTAD EXTRA
###############################################################################
def my_counter():
    counts = 0
    def decorator(func):
        def wrap():
            nonlocal counts
            func()
            counts += 1
            if counts == 1:
                print(f'\t** Se ha llamado {counts} vez a la funcion **')
            else:
                print(f'\t** Se ha llamado {counts} veces a la funcion **')
        return wrap
    return decorator

@my_counter()
def my_func():
    print('\nEsta funcion hace cosas alucinantes que no puedes ver')


my_func()
my_func() 
my_func() 
my_func()     


    


        
        
    
    