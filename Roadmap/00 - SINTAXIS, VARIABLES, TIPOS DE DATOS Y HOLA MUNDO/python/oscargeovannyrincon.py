#   https://www.python.org/doc/     #

#   comentario de una linea     #
"""comentario de varias
lineas con doble comilla"""
'''comentario de varias
lineas con comilla simple'''



print('RETO_01')

my_variable="Mi variable"
MY_CONSTANT="MI CONSTANTE"

print(my_variable,'\t',type(my_variable))
print(MY_CONSTANT,'\t',type(MY_CONSTANT))


my_integer=123
my_float=123.456
my_string='hola'+'python'
my_boolean=True
print(my_integer,'\t',type(my_integer))
print(my_float,'\t',type(my_float))
print(my_string,'\t',type(my_string))
print(my_boolean,'\t',type(my_boolean))
print("Este el primer reto y sus impresiones entero {}, flotante {}, string {} y boolean {}".format(my_integer, my_float, my_string, my_boolean))

print('FIN DEL RETO')