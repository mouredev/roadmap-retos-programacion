import random

def generar_arbol(altura, estrella, bolas, luces, encendidas):
    arbol = []
    for i in range(altura):
        nivel = [' '] * (altura + i + 1)
        start = altura - i
        for j in range(i * 2 + 1):
            if (start + j) in luces and encendidas:
                nivel[start + j] = '+'
            elif (start + j) in bolas:
                nivel[start + j] = 'o'
            else:
                nivel[start + j] = '*'
        arbol.append("".join(nivel))
    
    if estrella:
        arbol[0] = arbol[0][:altura] + '@' + arbol[0][altura+1:]
    
    tronco = [' ' * (altura - 1) + '|||' for _ in range(2)]
    return "\n".join(arbol + tronco)

def agregar_bolas(bolas, altura):
    posibles = [i for i in range(altura*2-1) if i not in bolas]
    if len(posibles) >= 2:
        bolas.update(random.sample(posibles, 2))
        print("Se añadieron dos bolas al árbol.")
    else:
        print("No hay espacio suficiente para más bolas.")

def eliminar_bolas(bolas):
    if len(bolas) >= 2:
        bolas -= set(random.sample(list(bolas), 2))
        print("Se eliminaron dos bolas del árbol.")
    else:
        print("No hay bolas suficientes para eliminar.")

def agregar_luces(luces, bolas, altura):
    posibles = [i for i in range(altura*2-1) if i not in luces and i not in bolas]
    if len(posibles) >= 3:
        luces.update(random.sample(posibles, 3))
        print("Se añadieron tres luces al árbol.")
    else:
        print("No hay espacio suficiente para más luces.")

def eliminar_luces(luces):
    if len(luces) >= 3:
        luces -= set(random.sample(list(luces), 3))
        print("Se eliminaron tres luces del árbol.")
    else:
        print("No hay luces suficientes para eliminar.")

def main():
    altura = int(input("Ingrese la altura del árbol: "))
    estrella = True
    bolas = set()
    luces = set()
    encendidas = True
    
    while True:
        print("\n" + generar_arbol(altura, estrella, bolas, luces, encendidas))
        print("Opciones: (1) Estrella (2) Bolas (3) Luces (4) Apagar/Encender (5) Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            estrella = not estrella
            print("Se ha modificado la estrella.")
        elif opcion == '2':
            subopcion = input("(A) Añadir bolas (B) Eliminar bolas: ").upper()
            if subopcion == 'A':
                agregar_bolas(bolas, altura)
            elif subopcion == 'B':
                eliminar_bolas(bolas)
        elif opcion == '3':
            subopcion = input("(A) Añadir luces (B) Eliminar luces: ").upper()
            if subopcion == 'A':
                agregar_luces(luces, bolas, altura)
            elif subopcion == 'B':
                eliminar_luces(luces)
        elif opcion == '4':
            encendidas = not encendidas
            print("Se han " + ("encendido" if encendidas else "apagado") + " las luces.")
        elif opcion == '5':
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()