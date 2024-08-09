"""
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
"""

def func_sin_p():
  print("hoy es   6 de agosto")

def func_1_p(mes):
  print(f"hoy es  6 de {mes}")

def func_2_p(dia, mes):
  print(f"hoy es  {dia} de {mes}")

def func_value_default(dia = 26,mes="enero"):
  print(f"hoy es  {dia} de {mes}")

def func_value_dmult(dia = 26,mes="enero"):
  return dia, mes

def func_par_var(*var):
  
  if len(var) >0:
    print(f" existen {len(var)} parametros")
    for i in var:
        print(i)
  else :
    print("No existen Parametros")

def func_k_v(** data):
  for k,v in data.items():
    print(f"key : {k}, value : {v}")




#  Dificultad Extra
def print_number(cad1, cad2):
 number = 0
 for i in range(1, 101):
   
   if i % 3 ==0 and i % 5 ==0:
     print(cad1+" "+cad2)
   elif i % 3 == 0 :
      print(cad1)
   elif i % 5 == 0:
     print(cad2)
   else:
     number+=1
     print(i)
 return number

print(print_number("TRES","CINCO"))
func_sin_p()
func_1_p("enero")
func_2_p(6,"diciembre")
func_value_default(22,"diciembre")
func_value_default()
dia = func_value_dmult()[0]
mes = func_value_dmult()[1]
print(dia, mes)
func_par_var(1,2,3,4,5)
func_par_var()
func_k_v(a=1,b=2,c=3)

# local y global variables
global_var = "ray"
print("Global ", global_var)

def local_Function():
  global_var = "21"
  print("LOcal variable", global_var)
local_Function()
print("Global ", global_var)

