def extra(inicio, fin):
    for i in range(inicio, fin+1):
        num = f"{i}"
        if i != 16 and i % 3 != 0:
            num += " (no es ni 16 ni multiplo de 3)"
        if i % 2 == 0:
            num += " (par)"
        print(num)

extra(10,55)