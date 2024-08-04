#02 FUNCIONES Y ALCANCE
'''
/*
 * EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 */
 '''
 
# Funciones básicas:
# Sin parámetros ni retorno
def funcion_hola():
    print('Hola')

funcion_hola()
print('*********************************************\n')

# Con un parámetro
def funcion_con_parametro(nombre):
    print(f'Hola {nombre}')

funcion_con_parametro('Mouredev')
print('*********************************************\n')

# Con un parámetro por defecto
def funcion_par_def(nombre='Mouredev'):
    print(f'Hola {nombre}')

funcion_par_def()        # Ejecutará con valor por defecto
funcion_par_def('Brais') # Ejecutará cambiando el valor por defecto  
print('*********************************************\n')

# Con 2 o más parámetros
def funcion_parametros(nombre,id):
    print(f'Bienvenido {nombre} su código es: {id}')

funcion_parametros('Pepe',3)
print('*********************************************\n')

# Con n parámetros
def funcion_n_parametros(*nombres):
    for nombre in nombres:
        print(f'Bienvenido {nombre}')

funcion_n_parametros('Rodrigo','Brais','Alan')
print('*********************************************\n')

# Con n parámetros y una llave
def funcion_kn_parametros(**nombres):
    for llave, nombre in nombres.items():
        print(f'{llave} : {nombre}')

funcion_kn_parametros(
    nombre = 'Rodrigo',
    edad = 25
)
print('*********************************************\n')

# Devuelve un parámetro
def bienvenido():
    return 'Bienvenido!'

print(bienvenido())
print('*********************************************\n')

# Con un parámetro y devuelve un parámetro
def bienvenido_nombre(nombre):
    return f'Bienvenido {nombre}!'

print(bienvenido_nombre('Brais'))
print('*********************************************\n')

# Funciones dentro de funciones
def funcion_externa():
    def funcion_interna():
        print('Bienvenido al reto Mouredev!')
    funcion_interna()
    
funcion_externa()
print('*********************************************\n')

# Funciones del lenguaje
# Función len()
print('Corto' if len("Brais") < 5 else 'largo')
print('*********************************************\n')

# Entorno de variables
print('Ambito global:')
variable_global = 'Brais'

def saludo():
    print('\tAmbito local de la función:')
    variable_local = 'Mouredev'
    print(f'\tBienvenido {variable_local} tu nombre global es {variable_global}')
    
saludo()
print(f'\nVariable global: {variable_global}')
#print(f'Variable global {variable_local}') # No se puede acceder por estar restringido al ambito de la función saludo()
print('*********************************************\n')

'''
/*DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
*/
'''
def extra(texto_1, texto_2) -> int:
    contador = 0
    for numero in range(1,101):
        if numero % 3 == 0 and numero % 5 == 0:
            print(f'{texto_1} {texto_2}')
        elif numero % 3 == 0:
            print(texto_1)
        elif numero % 5 == 0:
            print(texto_2)
        else:
            print(numero)
            contador += 1
    return contador

print(extra('Texto 1','Texto 2'))