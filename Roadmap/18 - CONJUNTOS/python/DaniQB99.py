'''
EJERCICIO:
Utilizando tu lenguaje crea un conjunto de datos y realiza las 
siguientes operaciones (debes utilizar una estructura que las soporte):

- Añade un elemento al final.
- Añade un elemento al principio.
- Añade varios elementos en bloque al final.
- Añade varios elementos en bloque en una posición concreta.
- Elimina un elemento en una posición concreta.
- Actualiza el valor de un elemento en una posición concreta.
- Comprueba si un elemento está en un conjunto.
- Elimina todo el contenido del conjunto.


DIFICULTAD EXTRA (opcional):
Muestra ejemplos de las siguientes operaciones con conjutos:
- Unión.
- Intersección.
- Diferencia.
- Diferencia simétrica.
'''

def conjunto_datos():
    
    data = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    set1 = set()
    set2 = set()
            
    while True:
        
        def sets():
            set1_input = input("Indica el conjunto 1 (Separados por coma): ")
            set1 = {int(num.strip()) for num in set1_input.split(",") if num.strip().isdigit()}  # Asegura que sean enteros

            set2_input = input("Indica el conjunto 2 (Separados por coma): ")
            set2 = {int(num.strip()) for num in set2_input.split(",") if num.strip().isdigit()}

            return set1, set2
    
        switch = input("""\nElige una de las siguientes opciones:
            1- Añade un elemento al final
            2- Añade un elemento al principio
            3- Añade varios elementos en bloque al final
            4- Añade varios elementos en bloque en una posición concreta
            5- Elimina un elemento en una posición concreta
            6- Actualiza el valor de un elemento en una posición concreta
            7- Comprueba si un elemento está en un conjunto
            8- Elimina todo el contenido del conjunto
            9- Unión
            10- Intersección
            11- Diferencia 
            12- Diferencia simétrica  
            13- Salir \n""")
        
        # ----- EJERCICIOS -----
        
        # Unión al final
        if switch == "1":
            data.append(input("Añade un elemento al final: "))
            print(data)
        
        # Unión al principio
        elif switch == "2":
            data.insert(0, input("Añade un elemento al principio: "))
            print(data)
            
        # Union en bloque al final
        elif switch == "3":
            final_block = input("Añade varios elementos en bloque al final: ")
            data.extend(final_block)
            print(data)
           
        # Union en bloque en una posición concreta
        elif switch == "4":
            block = input("Añade varios elementos separados por coma en bloque en una posición concreta: ")
            block = [str(num.strip()) for num in block.split(",")]  # Convierte el input en una lista de strings
            position = int(input("Indica la posición: "))

            if position > len(data):
                print("Posición incorrecta")
                continue

            data[position:position] = block # Inserta los valores en la posición indicada
            print(data)
          
        # Elimina un elemento en una posición concreta
        elif switch == "5":
            print(data)
            element_remove = input("Indica la posición del elemento a eliminar: ")
            del data[int(element_remove)]
            print(data)

        # Actualiza el valor de un elemento en una posición concreta
        elif switch == "6":
            print(data)
            data[int(input("Indica la posición: "))] = input("Actualiza el valor de un elemento en una posición concreta: ")
            print(data)
          
        # Comprueba si un elemento está en un conjunto
        elif switch == "7":
            print(data)
            element_find = input("Indica el elemento a buscar: ")
            if element_find in data:
                print("El elemento está en el conjunto")
            else: 
                print("El elemento no está en el conjunto")
            
        # Elimina todo el contenido del conjunto
        elif switch == "8":
            data.clear()
            print(data)
            
            
        # ----- EJERCICIOS EXTRA -----
            
        
        # Unión
        elif switch == "9":  
            set1, set2 = sets()  # Asignamos  los valores de la función a set1 y set2
            print(f"La unión de {set1} y {set2} es:", set1.union(set2) )
         
        # Intersección
        elif switch == "10":
            set1, set2 = sets()  
            print(f"La intersección de {set1} y {set2} es:", set1.intersection(set2))
            
        # Diferencia 
        elif switch == "11":
            set1, set2 = sets() 
            
            print(f"La diferencia de {set1} y {set2} es:", set1.difference(set2))
           
        # Diferencia simétrica
        elif switch == "12":
            set1, set2 = sets()
            print(f"La diferencia simétrica de {set1} y {set2} es:", set1.symmetric_difference(set2))
            
        # Salir   
        elif switch == "13":
            exit()
            
        # Error
        else:
            print(f"Opción {switch} no disponible")
            
conjunto_datos()