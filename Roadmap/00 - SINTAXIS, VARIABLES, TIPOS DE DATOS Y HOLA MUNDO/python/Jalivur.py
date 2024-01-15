# Pagina web Fuente de recursos e informaión: https://python.land/python-tutorial
"""
EJERCICIO:
- Crea un comentario en el código y coloca la URL del sitio web oficial del
    lenguaje de programación que has seleccionado.
- Representa las diferentes sintaxis que existen de crear comentarios
    en el lenguaje (en una línea, varias...).
- Crea una variable (y una constante si el lenguaje lo soporta).
- Crea variables representando todos los tipos de datos primitivos
    del lenguaje (cadenas de texto, enteros, booleanos...).
- Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
"""
#COMENTARIOS:
#Se pueden hacer de una sola liena como este, o de varias como el siguente.
"""
Python es fácil de utilizar y es un verdadero lenguaje de programación ofreciendo mucha más estructura y soporte para programas grandes que la que ofrecen scripts de shell o archivos por lotes. 
Por otro lado, Python también ofrece mayor comprobación de errores que C y siendo un lenguaje de muy alto nivel tiene tipos de datos de alto nivel incorporados como listas flexibles y diccionarios. 
Debido a sus tipos de datos más generales, Python es aplicable a más dominios que Awk o Perl, aunque hay muchas cosas que son tan sencillas en Python como en esos lenguajes.
"""
#tambien admite comillas simples.
'''
Esto tambien es un comentario, 
de varias lienas en 
Python.
'''

#VARIABLES Y TIPOS DE DATOS PRIMITIVOS:

'''
Python es un lenguaje de tipado dinamico, por lo que no existenten constantes como tal,
el tipo de una variable puede cambiar en cualquier momento en tiempo de ejcución, por lo que es algo a tener 
muy en cuenta.
'''
"""
Aquí hay algunos nombres de variables válidos:
    - name_1
    - name_2
    - _database_connection
Estos son nombres no válidos:

    - 1tomany (no empiezan con numeros)
    - my-number (- no esta permitido)
    - my number (espacions no permitidos)
Asi como tampoco esta pirmitido camelCase, como en otros lenguajes.
"""
#tambien se pueden insertar comentarios junto a la linea de codigo.
#str, Cadenas de texto, mas adelante veremos mas opciones de su sintaxis.
my_first_var="esta es mi primera variable" #en este caso se trata de una string o cadena de texto.
#por combencion, se pueden establecer constantes por llamarlas asi a variables que no se van a manipular en tiempo de ejcucion.
MY_FIRT_CONSTANT="esto es una constante entre comillas" #se declaran en mayusculas, y por combencion se establece que son variables a consultar, solo de lectura.
#int, puede almacenar números de -2^31 a 2^31 – 1, o lo que es lo mismo, de -2.147.483.648 a 2.147.483.647.
my_second_var=1 #tambien exixten variables numericas, en este caso un int o integer (entrero).
print(type(my_second_var))
#float, culla capacidad es 2.2250738585072014e-308 y la máxima 1.7976931348623157e+308, equivale a un doble de C.
my_third_var=5.5 #floating point number, numero de coma flotante.
print(type(my_third_var))
#complex, Los números complejos tienen una parte real y otra imaginaria, ambas representadas con números en coma flotante.
my_fourth_var=3+5j
print(type(my_fourth_var))
#Tambien tenemos datos de tipo bool.
my_bool_var=True #son valores binarios, True(uno) o False (cero). 
print(type(my_bool_var))

#sintaxis en cadenas de caracteres.
my_string='esta es otra cadena de texto.'#tambien se pueden usar comillas simples.
'''
En cadenas de texto, se pueden usar \ para escapar los caracters especiales, y que no sean interpretados.
De esta manera podemos incluirlos en el texto,
sin que el interprete los interprete como codigo.
O por el contrario, para que el codigo reacciones como nos interesa.
'''
#my_none_scape_string='doesn't' #en este caso si no escapamos el apostrofe, lo interpreta como cierre de comillas, y genera un error.
#SyntaxError: unterminated string literal (detected at line 53), esto se produce si decomentas liena 53.
my_scape_string='doesn\'t'
print(my_scape_string)
'''
Si no quieres que los caracteres precedidos por \ se interpreten como caracteres especiales, 
puedes usar cadenas sin formato agregando una r antes de la primera comilla:
'''
print(f'C:\some\name')#salto de linea y con formato de string
print(r'C:\some\name')#cadena de una liena
my_special_string="esta es una cadena \ncon salto de linea" #esta cadena se establede en dos lineas.
print(my_special_string)
my_multiline_string="""tambien puedes hacer estring de varias lineas,
alnacenadolas cen variables de esta forma,
tantas lienas como quieras."""
print(my_multiline_string)
print(my_first_var[0])#indicando un idice podemos extraer los caracteres de una str, en este caso la primera letra.
print(my_first_var[6])#en este caso la posicion 7.
print(my_first_var[-1])#ultima posicion.
print(my_first_var[-2])#penultima posicion.
print(my_first_var[0:5])#rango de posicion 0 a 5 excluyendo el ultimo.
print(my_first_var[3:7])#rango de 4 a 8 sin 8.
print(my_first_var[:8])#rango posicion inicial a 8.
print(my_first_var[2:])#rango de 3 posicion en adelante.
print(my_first_var[-6:])#rango de posicion -6 a final.
print(len(my_first_var))#len() funcion para contavilizar longitud de la variable.



#tambien disponemos de almacenes de datos como listas.
my_list=[]#esto es una lista vacia.
my_list=["hola", 3, 3.5, 3+6j, True]#esta es una lista con todos los timpos de datos en ella.
'''
Las listas se pueden manejar como las cadenas de texto,
a la hora de buscar en ellas algun valor en concreto,
o valores.
'''
""" 
Exixten infinidad de operaciones posibles con
cada uno de los tipos de datos, en los que se pueden ir profundizando,
a medida que se abanza o se necesita.
"""
#hola mundo.
print("¡Hola, Python!")








