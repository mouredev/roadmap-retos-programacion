# @author Alberto Revel

"""
 Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
"""

# 1. Arithmetic operators
print("\n**** PART 1 - Operators ****\n")
print("\n** 1. Arithmetic Operators **\n")
print (" - Addition (1+2) -> " + str(1+2)) 
print (" - Subtraction (3-4) -> " + str(3-4)) 
print (" - Multiplication (7*11) -> " + str(7*11)) 
print (" - Division (float) (40/6) -> " + str(40/6)) 
print (" - Division (floor) (40//6) -> " + str(40//6)) 
print (" - Modulus (40%6) -> " + str(40%6)) 
print (" - Power (2**8) -> " + str(2**8)) 
print ("\n")

# 2. Assignment operators
print("\n** 2. Assignment Operators **\n")
var1 = 15
var2 = 8
print (f" - var1 = 15, var2 = 8 -> var1:  {var1} , var2: {var2}") 
var1+=var2
print (f" - var1 += var2 ->  {var1}") 
var1-=var2
print (f" - var1 -= var2 ->  {var1}") 
var1*=var2
print (f" - var1 *= var2 ->  {var1}") 
var1/=var2
print (f" - var1 /= var2 ->  {var1}") 
var1%=8
print (f" - var1 %= 8 ->  {var1}") 
var1//=3
print (f" - var1 //= 3 ->  {var1}") 
var1**=var2
print (f" - var1 **= var2 ->  {var1}") 
var2&=3
print (f" - var2 &= 3 ->  {var2}") 
var2|=32
print (f" - var2 |= 32 ->  {var2}") 
var2^=5
print (f" - var2 ^= 5 ->  {var2}") 
var2<<=8
print (f" - var2 <<= 8 ->  {var2}") 
var2>>=10
print (f" - var2 >>= 10 ->  {var2}") 
print ("\n")

# 3. Logic operators
print("\n** 3. Logic Operators **\n")
var3 = 15
print("Being var3 = 15\n")
print(" - var3 > 0 and var3 > 50: " + str(var3 > 0 and var3 > 50))
print(" - var3 > 0 or var3 > 50: " + str(var3 > 0 or var3 > 50))
print(" - not(var3 > 0 and var3 > 50): " + str(not(var3 > 0 and var3 > 50)))
print ("\n")

# 4. Identity operators
print("\n** 4. Identity Operators **\n")
var4 = 7
var5 = 15
print("""Being var3 = 15
      var 4 = 7
      var5 = 15""")
print("var3 is var5: " + str(var3 is var5))
print("var4 is not var5: " + str(var4 is not var5))
print ("\n")

# 5. Comparison operators
print("\n** 5. Comparison Operators **\n")
print("""Being var3 = 15
      var 4 = 7
      var5 = 15""")
print("var4 == var5: " + str(var4 == var5))
print("var3 != var5: " + str(var3 != var5))
print("var3 > var5: " + str(var3 > var5))
print("var4 < var5: " + str(var4 < var5))
print("var3 >= var5: " + str(var3 >= var5))
print("var4 <= var5: " + str(var4 <= var5))
print ("\n")

# 6. Membership  operators
print("\n** 6. Membership  Operators **\n")
list1 = ["iPhone", "Pixel"]
print("""Being list1 = ["iPhone", "Pixel"]""")
print(""" - "Samsung" in list1: """ + str("Samsung" in list1))
print(""" - "Samsung" not in list1: """ + str("Samsung" not in list1))
print ("\n")

# 7. Bitwise  operators
print("\n** 7. Bitwise  Operators **\n")
var6=10 # 1010
var7=4 # 0100
print("""Being var6=10 # 1010
      var7=4 # 0100""")
print (" - var6 | var7 -> " + str(var6|var7)) 
print (" - var6 ~ var7 -> " + str(~var6)) 
print (" - var6 & var7 -> " + str(var6&var7)) 
print (" - var6 ^ var7 -> " + str(var6^var7)) 
print (" - var6 >> 1 -> " + str(var6>>1)) 
print (" - var6 << var7 -> " + str(var6<<var7)) 
print ("\n")


"""
Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
"""
print("\n**** PART 2 - Control structures ****\n")
print("\n** 1. Conditionals **\n")
print("""Being var5=15
      var6=10
      var7=4""")
if (var6 > var7):
    print("- var6 is greater than var7")
elif (var6 < var7):
    print("- var6 is lower than var7")
else:
    print("- var6 is equals to var7")
print("- var5 is greater than var6") if var5 > var6 else print(" - var6 is not greater than var5")
if var5>0: print("- var5 is greater than 0")

print("\n** 2. While **\n")
print("\n - Simple loop")
index = 1
while index < 6:
  print(f"  · iteration {index}")
  index += 1
else:
  print(f" - End of loop, index value = {index}")

print("\n - Break at pairs")
index = 0
while index < 6:
  index += 1
  if (index % 2 == 0): 
     break
  print(f"  · iteration {index}")
else:
  print(f" - End of loop, index value = {index}") # Not executed because of break

print("\n - Continue at pairs")
index = 0
while index < 6:
  index += 1
  if (index % 2 == 0): 
     continue
  print(f"  · iteration {index}")
else:
  print(f" - End of loop, index value = {index}")


# 3. For loop
print("\n** 3. For loop **\n")
list1 = ["iPhone", "Pixel", "Poco","Samsung"]
print("- Array list")
for element in list1:
    print(f"  · {element}")
print ("\n")

print("- Looping through string chars in string 'iPhone'")
for eachChar in list1[0]:
    print(f"  · {eachChar}")
print ("\n")

print("- Nested loop")
for element in list1:
    for eachChar in element:
        print(f"  · {eachChar}")
print ("\n")

print("- Continue on words containing letter 'o'")
for element in list1:
    if "o" in element:
      continue
    print(f"  · {element}")
print ("\n")


print("- Range function -> range(5)")
for element in range(5):
    print(f"  · {element}")
print ("\n")

print("- Range function -> range(2,5)")
for element in range(2,5):
    print(f"  · {element}")
print ("\n")

print("- Range function -> range(1,20,3)")
for element in range(1,20,3):
    print(f"  · {element}")
else:
   print("Finished")
print ("\n")

print("- Range function with pass -> range(1,3)")
for element in range(1,3):
   pass
print ("\n")



print("\n** 4. Exceptions **\n")
print("print('Try block')")
try:
  print("Try block")
except:
  print("Exception thrown")
else:
  print("No exception, not except block reached")
print ("\n")

print("print(var10)")
try:
  print(var10)
except NameError:
  print("Exception thrown of type NameError")
except:
  print("Exception thrown (not of type NameError)")
print ("\n")

print("print(1/0)")
try:
  print(1/0)
except NameError:
  print("Exception thrown of type NameError")
except:
  print("Exception thrown (not of type NameError)")
print ("\n")


"""
 DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
"""
print("\n**** PART 3 - OPTIONAL ****\n")
for eachValue in range(10,56,2):
   if (eachValue == 16 or eachValue % 3 == 0):
      continue
   print(f" - {eachValue}")
   