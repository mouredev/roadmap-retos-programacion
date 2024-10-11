
# while True:
# n1 = int(input("Ingrese Dividendo:"))
# n2 = int(input("Ingrese Divisor:"))
# try:
#     r= n1 / n2
#     print(r)
# except:
#     print("No se puede dividir entre 0")
    


# frutas = ['mango','bananos','durazno','fresa']
# try:
#     print(f'la fresa se encuentra en la posición',frutas[4])
# except Exception:
#     print('El indice no existe')
#     print('intentalo de nuevo')



def studentNotes(codigo,materia,notas):
    lista = []
    try:
        try:
            with open(notas) as file:
                for line in file:
                    try:
                        datos = line.strip().split(',')
                        #print(datos)
                        if len(datos) != 3:
                            raise IndexError(f'La línea no tiene el formato esperado: {line.strip()}') 


                        estudiante = {'id':int(datos[0]), 'Nombre':datos[1],'Promedio':int(datos[2])}
                        lista.append(estudiante) 
                    except ValueError:
                        print(f"Error de conversión en la línea : {line.strip()}. Se espera un entero en 'id' o 'promedio'.")
                    except IndexError as e:
                        print(e)

        except FileNotFoundError as fnf_error:
            print(fnf_error)
            print(f'Explanation: We cannot load the {notas}')
    except IOError:
        print(f'Error al abrir el archivo {notas}.Verifica los permisos a la ruta ')

    print(f"codigo de Materia:{codigo}, Matería: {materia}")
    for estudiante in lista:
        print(estudiante)


studentNotes(43,'Matemáticas','notas.txt')

