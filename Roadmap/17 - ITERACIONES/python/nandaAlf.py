# /*
#  * EJERCICIO:
#  * Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
#  * números del 1 al 10 mediante iteración.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Escribe el mayor número de mecanismos que posea tu lenguaje
#  * para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?
#  */

# 1 for Loop
print("**********1**********")
for i in range(10):
    print(i+1)

# 2 while Loop
print("\n**********2**********")
i=1
while i<11:
    print(i)
    i+=1

#3 while loop using IN
print("\n**********3**********")
i=1
while i in [1,2,3,4,5,6,7,8,9,10]:
    print(i)
    i+=1

#4 function iter()
print("\n**********4**********")
numbers = iter(range(1, 11))
for n in numbers:
    print(n)

#5 functions iter() and next()
print("\n**********5**********")
numbers = iter(range(1, 11))
while(True):
    try:
        n=next(numbers)
        print(n)
    except StopIteration:
        break

#6 generator
print("\n**********6**********")
def generator(n):
    for i in range(1,n+1):
        yield i
for i in generator(10):
    print(i)

#7 list Compression
print("\n**********7**********")
number1=[i for i in range(1,11)]
for n in number1:
    print(n)

#8 function enumerate()
print("\n**********8**********")
for index,number in enumerate(range(1,11),1):
    print(index)

#9 class
print("\n**********9**********")
class Nums:
    def __init__(self, n):
        self.n = n
        self.i = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.i > self.n:
            raise StopIteration
        number = self.i
        self.i += 1
        return number

numbers2 = Nums(10)
for n in numbers2:
    print(n)

# 10 function map()
print("\n**********10*********")
number5=map(lambda x:x,[1,2,3,4,5,6,7,8,9,10])
for n in number5:
    print(n)