x='b'

def saludo (): 
    print ("Hola, soy Elba")
    
## con retorno

def retorno ():
    return "Hola, soy Elba con retorno"    

saludo()
# variableretornada= retorno()
print (retorno() )

## con argumentos

def argumento (nombre):
    return "Hola, soy " + nombre

print (argumento("Elba marina"))

def argumento2 (accion, nombre):
    return accion + " soy " + nombre

print (argumento2("Hello, ", "Elba marina"))

def pordefecto (nombre="Python"):
    return "Hola, soy " + nombre

print (pordefecto())
print (pordefecto("Elba marina"))

print (argumento2(nombre="Hello, ", accion="Python"))

# retorno varias argumentos

def retorno2 (nombre, apellido):
    print ( f"{nombre}, {apellido} " )
    


print  (retorno2  ("Elba", "Mujica"))


def retorno3 ():
    return ('python', 'clase3', 'funciones')

lenguaje,nroc,tema=retorno3()
print (lenguaje)
print (nroc)
print (tema)


# Funciones con numero variable de argumentos

def varios (*organiza):
    for orga in organiza:
        print (f"{orga}")

varios("GEMTE", "VNQ", "RED")


# Funciones con numero variable de argumentos con clave

def variosc (**organiza):
    for key,orga in organiza.items():
        print (f" Hola {orga}({key})")

variosc(trabajo="GEMTE", contrata="VNQ", segmento="RED")


# variables locales y globales

def pruebas ():
      def interna ():
         x=10
         print (f' x local {x}') 
      interna()


pruebas () 
print (x)


# Dificultad Extra

def rutina (param1,param2):
    for i in range(1, 101):
        if (i % 3) == 0 and (i % 5) != 0:
             print (f" Es multiplo de  {param1} {i}")
        elif (i % 3) != 0 and (i % 5) == 0 :
                print (f" Es multiplo de  {param2} {i}") 
        elif (i % 3) == 0 and (i % 5) == 0 :
                print (f" Es multiplo de  {param1} y {param2} {i}")
        else:
            print (f" Es otro numero {i}")


rutina("tres", "cinco")                
        