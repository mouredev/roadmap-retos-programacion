# variable GLOBAL.

A = 6
B = 6



# Funciones sin retorno de variables ni valores.

def saludo():
    print ('Hola Mundo')
    
    
saludo()

# Funciones con varios parametros.

def saludo_parametros(nombre,apellidos):
    print ('Hola gracias por pasarme los valores de nombre y apellidos: ' + nombre + apellidos)
    def antisaludo():
        print ('Ha solicitado el antisaludo')
        
    
    
    
saludo_parametros('Pedro ', 'Martinez Pérez')


# Funcion con retorno de valores, con ejemplo de variables GLOBALES.

def suma(A,B):
    return (A+B)
    
resultadoSuma =  suma(A,B)
print (resultadoSuma)

# Funcion con retorno de valores, con ejemplo de variables locales.

def resta (a,b):
    return (a-b)
    
resultadoResta = resta (8,7)
print (resultadoResta)