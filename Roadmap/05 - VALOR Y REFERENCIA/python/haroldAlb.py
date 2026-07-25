### Asignación de variables por VALOR ###

num1= 23
num2= 3.1416
string1= "Hola Mario"
bool1= True

### Asignación de variables por REFERENCIA ###

nums1= [10, 100, 30]
nums2= (11, 101, 31)

### funciones con variables por valor ###
def func_valor(n):
    n -= 2
    print(f"variable modificada en la funcion: {n}")

print(f"Variable antes de la función: {num1}")
func_valor(num1)
print(f"Variable despues de la función: {num1}")

### funciones con variables por referencia ###

def func_referencia(n):
    for i, v  in enumerate(n):
        n[i] -= 1 
    print(f"variable modificada en la funcion: {n}")

print(f"Variable antes de la función: {nums1}")
func_referencia(nums1)
print(f"Variable despues de la función: {nums1}")

### EXTRA ###
print("\n### EXTRA ###\n")
def intercambio_val(valor1, valor2):
    aux= valor1
    valor1= valor2
    valor2= aux
    return valor1, valor2

var1= 333
var2= 666
char1= ["hola", "Mario"]
char2= ["Mario", "Albiñana"]

new1, new2= intercambio_val(var1, var2)
print(f"{var1} -> {new1}\n{var2} -> {new2}")

nc1, nc2= intercambio_val(char1, char2)
print(f"\n{char1} -> {nc1}\n{char2} -> {nc2}")
