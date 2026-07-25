# Operaciones con caracteres #

x = "Hola"
y = "mundo"

print(x + " " + y)  # Concatenación
print(x * 5)  # Repetición
print(x[0])  # Indexación
print(len(y))  # Longitud
print(y[2:4] + " " + y[3:] + " " + y[:3])  # Slicing
print("o" in y)  # Busqueda
print(x.replace("a", "o"))  # Reemplazo
print(y.split("n"))  # División
print(y.upper())  # Mayuscula
print(x.lower())  # Minuscula
print("string test".title())  # Titulo
print("string test".capitalize())  # Capitalizar
print(x.startswith("H"))  # Busqueda al principio
print(x.endswith("F"))  # Busqueda al final
print(x.find("o"))  # Busqueda
print("spring test".count("t"))  # Busqueda de ocurrencias
print(list(x))  # Transformación en lista de caracteres
l = [x, " ", y]
print("".join(l)) # Transformación de lista en cadena de caracteres
# Comprobaciones
print("46735".isalnum())
print("Hola".isalpha())
print("Hola".isdigit())

# Extra #
def check(w1 : str, w2 : str):
    # Palindromos
    print(f"¿\"{w1}\" es palindromo?: {w1 == w1[::-1]}")
    print(f"¿\"{w2}\" es palindromo?: {w2 == w2[::-1]}")

    # Anagramas
    print(f"¿\"{w1}\" es anagrama de \"{w2}\"?: {sorted(w1) == sorted(w2)}")

check("seres", "hola")
check("iman", "mani")