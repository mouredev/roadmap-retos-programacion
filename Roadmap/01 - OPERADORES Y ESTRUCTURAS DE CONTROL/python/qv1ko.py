a = 3
b = 4

sum = a + b
print(f"Number A + Number B = {sum}")

sub = a - b
print(f"Number A - Number B = {sub}")

mul = a * b
print(f"Number A * Number B = {mul}")

div = a / b
print(f"Number A / Number B = {div}")

res = a % b
print(f"Number A % Number B = {res}")

pow = a ** b
print(f"Number A ** Number B = {pow}")

flo = a // b
print(f"Number A // Number B = {flo}")

a = b;
print(f"a = b\t Number A:  {a}")

a += b;
print(f"a += b\t Number A:  {a}")

a -= b;
print(f"a -= b\t Number A:  {a}")

a *= b;
print(f"a *= b\t Number A:  {a}")

a /= b;
print(f"a /= b\t Number A:  {a}")

a %= b;
print(f"a %= b\t Number A:  {a}")

a //= b;
print(f"a //= b\t Number A:  {a}")

if a == b:
    print(f"Number A equals number B")

if a != b: print(f"Number A does not equal number B")

if a > b:
    print(f"Number A is greater than number B")
elif a < b:
    print(f"Number A is less than number B")
else:
    print(f"Number A equal number B")

print("Number A is greater than or equal to number B") if a >= b else print("Number A is less than number B")

while a > b or b == 3:
    a += 1

for i in [1, 2, 3]:
    print(i)

for i in range(3, 5):
    print(i)

try:
  print(a)
except:
  print("Exception") 

def program():
    for i in range(10, 55):
        if i % 2 != 0 or i == 16 or i % 3 == 0:
            continue
        else:
            print(f"\n{i}")

program()
