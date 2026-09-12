Num1 = 9
Num2 = 8.0
Log1 = True
Log2 = False
Cadena = "Elna"

print(f"Suma de un float y un int {Num1 + Num2}")
print(f"Operador O {Log1 or Log2}, Operador Y {Log1 and Log2}")
print(f"Es True > False {Log1 > Log2}")
print(Cadena * 5)

if "E" in Cadena:
	print("\nEncontré la 'E'")

print(f"División entera de 9 entre 8 {Num1//Num2}")
print(f"Cociente {Num1/Num2}")

for i in range(5):
	Num1 -= 1
print(f"En esto ha quedado Num1 {Num1}")

persona = {"name": "Brais", "age": 37, "country": "Galicia"}

for item in persona:
	print(f"{item}: {persona[item]}")

while Num2 > 0:
	if Num2 % 2 == 0:
		print(f"Num2 es {int(Num2)} y es par")			
	Num2 -= 1

i = 10
while i>=10 and i<=55:
	if i%2==0 and i!=16 and i%3!=0:
		print(i)
	i += 1		
