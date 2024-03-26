### 06-RECURSIVIDAD ###

def cont_regresivo(num:int):
    if num >= 0 :
        print(num)
        cont_regresivo(num-1)
    else :
        print("Fin conteo regresivo")

cont_regresivo(100)

def factorial(number) -> int:
    if number == 0:
        return 1
    elif number < 0:
        print("El numero debe ser entero positivo")
        return 0
    else    :
        return  number * factorial(number - 1)
    

my_num = 8
res = factorial (my_num)
print (f"El factorial de {my_num} es {res}")
print("--------------------------------")

def fibo(pos):
  if pos <= 0:
     print("la posicion debe ser un entero positivo")
     return 0
  elif pos == 1:
      return 0
  elif pos == 2 :
      return 1
  else :
      return fibo(pos - 1) + fibo(pos - 2)
  
my_pos = 6

res_fibo = fibo(my_pos)
print(f"El valor de la serie fibonacci en la posicion {my_pos} es {res_fibo} ")