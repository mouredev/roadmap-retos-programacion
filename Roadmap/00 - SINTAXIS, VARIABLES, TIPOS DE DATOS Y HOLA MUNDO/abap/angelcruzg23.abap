* Link official https://help.sap.com/doc/abapdocu_750_index_htm/7.50/en-US/index.htm

* Comentario de toda la linea de codigo, solo se colocar el asterisco al inicio 
" También se puede utilizar comillas dobles 

* Como se crea una variable en ABAP

" Se utiliza la palabra reservada DATA al inicio con el tipo que corresponda
data my_var type string value 'Mi Variable'.
my_var = 'Nuevo valor'. " Al final de cada sentencia se finaliza con punto (.).

" En la nueva sintaxis se crean variables en linea 
data(my_var_inline) = 'Variable en linea'.

" Las constantes se crean con la sintaxis CONSTANTS
CONSTANTS MY_CONSTANT type String value 'No Me Cambies'.

" Crear variable tipo entero 
data my_int type I.
my_int = 1.

" Crear variable tipo decimal
data my_dec TYPE p LENGTH 8 DECIMALS 2.
my_dec = 10.02

" Como se escriben en pantalla las variables 

write:/ myvar.
write:/ my_var_inline.
write:/ my_int.

