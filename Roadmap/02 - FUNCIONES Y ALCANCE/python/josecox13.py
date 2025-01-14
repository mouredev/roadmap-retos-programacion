
#Funciones definidas por el usuario

#Simple
def nombre():
    print('Mi nombre es Jose')

nombre()
#Con retorno
def return_nombre():
    return('Mi nombre es Jose')
print(return_nombre())

#Con argumento
def nombre_arg(nombre):
    print(f'Mi nombre es {nombre}')
nombre_arg('Pepe')

#Valores por defecto
def predet_nombre(nombre = 'Jose'):
    print(f'Mi nombre es {nombre}')
predet_nombre()
predet_nombre('Pepe')

#Con dos argumentos y posicionales
def city_country(city, country):
    print(f'{city} está en {country}')

city_country('Madrid', 'España')
city_country(country='España', city='Madrid')

#Especificando el tipo de dato de los argumentos
def suma_tipoarg(num1: int, num2:int):
    return num1+num2
print(suma_tipoarg(3,5))

#Especificando el tipo de dato de salida
def suma_tiposal(num1,num2) -> int:
    return(num1+num2)
print(suma_tiposal(3,5))


#Función que retorne varios valores
def suma_producto(num1, num2):
    return num1, num2
print(suma_producto(3,6))
suma, producto = suma_producto(3,6)
print(suma)
print(producto)

#Funciones con número variable de argumentos
def suma_var(*num):
    contador = 0
    for i in num:
        contador += i
    return contador
print(suma_var(4,5,6,7,8))


#Funciones dentro de funciones
def impresion_suma(num1,num2):
    def suma_interna(num1,num2):
        return num1+num2
    print(f'La suma es {suma_interna(num1,num2)}')

impresion_suma(5,6)

#Funciones bult-in
print('Hola')
print(len('Caracola'))
range(9)
print(type('Hola'))
print('Hola'.upper())

#Variable local y global
#Variable global, su ámbito es superior a lo queremos afectar
numero = 45
def mostrar_num():
    local_var = 'Esto es una variable local'
    print(f'El numero es {numero}')

mostrar_num()
#print(local_var) dará error, ya que local_var solo está definida dentro de la función mostrar_num()


#Ejercicio extra
print('Ejercicio extra')
def ejercicio_extra(string1:str, string2:str):
    counter = 0
    for i in range(101):
        if i%3 == 0 and i%5 == 0:
            print(string1,string2,sep='')
        elif i%3 == 0:
            print(string1)
        elif i%5 == 0:
            print(string2)
        else:
            print(i)
            counter += 1
    return counter

print(ejercicio_extra('cara','cola'))
