import pandas as pd

print('''\n
#=======================================================================================================================
# 50 - Planificador de objetivos de año nuevo
#=======================================================================================================================
''')

print('''
Te ayudaré a planificar tus objetivo para el nuevo año.

Tus objetivos deben seguir el siguiente modelo:
- Meta: Leer libros
- Cantidad: 12
- Unidades: libros
- Plazo (en meses): 12 (máximo 12)

Por favor ingresa la información necesaria y sigue las indicaciones:
''')

objectives = pd.DataFrame()
count = 0

while count <= 10:

    count += 1

    if count > 10:
        print('Has ingresado el numero maximo de objetivos.')
        break

    print(f'''
Ingresa informacion del objetivo {count}:
    ''')

    objective = {}

    objective['Meta'] = [input('Nombre de la meta: ')]
    objective['Cantidad'] = [int(input('Cantidad: '))]
    objective['Unidad'] = [input('Unidad de medida: ')]
    objective['Plazo'] = [int(input('Plazo: '))]

    objectives = pd.concat([objectives, pd.DataFrame(objective)], ignore_index=True)

    action = int(input('''
Para ingresar el siguiente objetivo digita 0.
Para terminar digita 1.
                '''))

    if action > 0:
        break

objectives['Frecuencia'] = objectives['Cantidad'] / objectives['Plazo']

mounths = ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Setiembre','Octubre','Noviembre','Diciembre']

mounth_num = 0

text = ''

for mounth in mounths[:objectives['Plazo'].max()]:

    mounth_num += 1

    text += f'\n{mounth}:'

    for index, row in objectives.iterrows():
        if mounth_num <= row['Plazo']:
            text += f'\n{index+1}. {objectives['Meta'][index]} ({objectives['Frecuencia'][index]} {objectives['Unidad'][index]}/mes): Total: {objectives["Cantidad"][index]}'
        else:
            pass

print(f'\nFelicidades, aquí tienes tu planificación de objetivos:\n{text}')

save = input('\n¿Desea exportar su planificación (SI/NO)?: ').upper()

if save == 'SI':
    with open("planificacion_2025.txt", "w") as archivo:
        archivo.write(text)

    print('Archivo exporta exitosamente ¡Adios!')

else:
    print('\nNo hay problema ¡Adios!')
