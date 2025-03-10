# https://www.python.org/
# Comentario simple
'''Comentario en varias
líneas sin problemas'''
"""Esta es otra forma
de comentario en varias líneas"""
first_var = ''
var_str = str("hello")
var_int = int(1)
var_float = float(1)
var_bool = bool(0)
var_comp = complex(1j)
MY_CONSTANT = "CONSTANTE" # por convención
var_leng = 'Python'
print(f'Hola {var_leng}!!!')
print(f'La variable definida "{first_var}" es de tipo: {type(first_var)}')
print(f'La variable definida "{var_str}" es de tipo: {type(var_str)}')
print(f'La variable definida "{var_int}" es de tipo: {type(var_int)}')
print(f'La variable definida "{var_float}" es de tipo: {type(var_float)}')
print(f'La variable definida "{var_bool}" es de tipo: {type(var_bool)}')
print(f'La variable definida "{var_comp}" es de tipo: {type(var_comp)}')
print(f'La constante definida {MY_CONSTANT} es de tipo: {type(MY_CONSTANT)}')

var_str = 1
var_int = True
var_float = "pero que pasa"
var_bool = 1+2j
var_comp = 3.25
MY_CONSTANT = 3.14

print(f'La variable definida "{first_var}" es de tipo: {type(first_var)}')
print(f'La variable definida "{var_str}" es de tipo: {type(var_str)}')
print(f'La variable definida "{var_int}" es de tipo: {type(var_int)}')
print(f'La variable definida "{var_float}" es de tipo: {type(var_float)}')
print(f'La variable definida "{var_bool}" es de tipo: {type(var_bool)}')
print(f'La variable definida "{var_comp}" es de tipo: {type(var_comp)}')
print(f'La constante definida {MY_CONSTANT} es de tipo: {type(MY_CONSTANT)}')