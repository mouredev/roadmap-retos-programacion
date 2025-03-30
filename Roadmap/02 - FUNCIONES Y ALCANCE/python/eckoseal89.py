def TextoAEnt(n1,n2):
    c = 0
    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
            print(f"{n1}, {n2}")
        elif i % 3 == 0:
            print(f"{n1}")
        elif i % 5 == 0:
            print(f"{n2}")
        else:
            c += 1
            print(i)
    return (f"Se ha mostrado un número {c} veces.")

TextoAEnt("hola", "adios")
