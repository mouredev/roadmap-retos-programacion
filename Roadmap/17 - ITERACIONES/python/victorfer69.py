#EJERCICIO

for i in range(1, 11):
    print(i)
print("==============")

i = 1
while(i < 11):
    print(i)
    i += 1
print("==============")

def function_recursive(i:int):
    if i == 10:
        print(i)
    else:
        print(i)
        i += 1
        function_recursive(i)

function_recursive(1)
print("==============")

#EJERCICIO EXTRA

for i in [1, 2, 3]:
    print(i)
print("==============")

for i in {1, 2, 3}:
    print(i)
print("==============")

for i in {1: "a", 2: "b", 3: "c"}:
    print(i)
print("==============")

print(*[i for i in range(1, 11)], sep="\n")
print("==============")