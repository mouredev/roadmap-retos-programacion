import datetime

# Funcion sin paramametros
def print5Numbers() :
    for i in range(1, 6):
        print(i)

# Función con retorno
def ageVerification(age):
    return (age > 18)

print(ageVerification(21))

# Funcion con varios parametros
def getFullName(name, last_name):
    name = name.capitalize()
    last_name = last_name.capitalize()
    return f"{name} {last_name}"

print(getFullName('yeromi', 'zavala'))

# Funciones dentro de funciones
db = {
    'yeromi': {
        'full_name': 'Yeromi Zavala',
        'password': '123'
    },
    'william': {
        'full_name': 'William Zavala',
        'username': 'zavala',
        'password': '12345',
    },
}

def login(username, password):
    
    def getUser(username):
        return db.get(username)
    
    def validatePassword(user, password):
        return user.get('password') == password
    
    user = getUser(username)
    
    if user:
        if validatePassword(user, password):
            print(f'Bienvenido {user.get('full_name')}')
        else:
            print(f'Contraseña incorrecta.')
    else:
        print('Credenciales incorrectas.')
        
login('yeromi', '123')

# Variables locales y globales
name = "Yeromi"
last_name = "Zavala Castillo"
dni = 75880289
birth = datetime.date(2004, 7, 1)

def printFullData():
    global name
    
    name = 'Alberto'
    last_name = 'Garcia Quispe'
    dni = 19694343
    birth = datetime.date(2008, 3, 1)
    
    full_data = f"""
        Nombre: {name}
        Apellido: {last_name}
        Dni: {dni}
        Nacimiento: {birth}
    """
    
    print(full_data)
    
printFullData()

print(name) # Unica variable modificada globalmente
print(last_name)
print(dni)
print(birth)

"""
* DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
"""
def fromOnetoOneHundred(chain1, chain2):
    count = 0
    
    for i in range (1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(f'{chain1} {chain2}')
        elif i % 3 == 0:
            print(chain1)
        elif i % 5 == 0:
            print(chain2)
        else:
            print(i)
            count += 1
        
    return count

print("Cantidad de veces en las que se imprimio numeros: " + str(fromOnetoOneHundred('Tres', 'Cinco')))