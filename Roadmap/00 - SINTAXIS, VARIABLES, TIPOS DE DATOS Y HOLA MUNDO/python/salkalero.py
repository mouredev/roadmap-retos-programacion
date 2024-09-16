# Con este elemento "#" podemos crear los comentarios en una línea.

#La Web oficial de Python es la siguiente. https://www.python.org
print("\n"*0)#Con esto añado separaciones entre los resultados del código
print("Hello, World!")#Se puede añadir los comentarios al final de una orden.

#pint("Hello,World!")#Se pueden usar para evitar que se ejecuten cualquier orden.

#Python no dispone de una sintaxis para crear varias líneas de comentarios
#para ello se pueden ir añadiendo "#" en cada línea para crear comentarios
#con varias líneas.

"""Pero, dado que python ignorará los literales de cadena que no estén
asignados a una variable, se puede crear un comentario usando doble 
comillas tres veces, como el usado en este comentario.Hay que 
tener en cuenta, que esta cadena no puede estar asignada
 a una variable.
"""
print("\n"*0)#Con esto añado separaciones entre los resultados del código
print("""Si sale este mensaje, el comentario usando las triples 
      comillas es un éxito!!!. Recuerda que la cadena no
      debe de estar asignada a una  variable.""")


print("\n"*0)#Con esto añado separaciones entre los resultados del código
#Creando una variable.
my_Variable = "Estos son variables"
print (my_Variable)
a = 250
b = "doscientos cincuenta"
c = 250.0
print (a)
print (b)
print (c)
print (250,"doscientos cincuenta",250.0)
print (a,b,c,"[con formato print (a,b,c)]")
print("\n"*0)#Con esto añado separaciones entre los resultados del código
"""En python no existe la variable constante, pero existe un concenso 
que si te encuentras una variable escrita en mayúsculas, esto quiere 
decir que esa variable hay que considerarla como si fuera una 
constante, por lo que no hay que cambiar el valor.
"""
MY_CONSTANTE = """En python no existe la variable constante, pero existe un concenso 
que si te encuentras una variable escrita en mayúsculas, esto quiere 
decir que esa variable hay que considerarla como si fuera una 
constante, por lo que no hay que cambiar el valor."""
print (MY_CONSTANTE)
print("\n"*0)#Con esto añado separaciones entre los resultados del código
#Creamos variables con los distintos tipos de datos que soporta python.
#Usamos la función "type() para mostrar el tipo de datos"
print ("A continuación se representa varios tipos de variables")
print("\n"*0)
a = 100
b = "Cien"
c = 27.6
d = 1j
print((a),type(a),(b),type(b),(c),type(c),(d),type(d))

print("\n"*0)#Con esto añado separaciones entre los resultados del código
a = ["manzana","peras","limones","mango"]
b = ("manzana","peras","limones","mango")
c = range(15)
d = {"name" : "Salvador" , "altura" : "325Cm" , "age" : 12.5}
print((a),type(a),(b),type(b),(c),type(c),(d),type(d))
print("\n"*0)

e = {"vaso" , "botellas" ,"sartén" }
f = frozenset({"cuchara" , "cuchillo" , "tenedor"})
g = True
h = b"Hola"
print((e),type(e),(f),type(f),(g),type(g),(h),type(h))

print("\n"*0)

i =bytearray(1)
j = memoryview(bytes(2))
k = None

print((i),type(i),(j),type(j),(k),type(k))
print("ªn"*0)
#Imprimiendo "Hola,Python"
print("Hola,Python")
