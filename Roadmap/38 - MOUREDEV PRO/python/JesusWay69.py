import os, platform, csv, random, time

if (platform.platform().startswith("macOS") or platform.platform().startswith("Linux")):
    os.system('clear')
else:
    os.system('cls')

""" * EJERCICIO:
 * He presentado mi proyecto más importante del año: mouredev pro.
 * Un campus para la comunidad, que lanzaré en octubre, donde estudiar
 * programación de una manera diferente.
 * Cualquier persona suscrita a la newsletter de https://mouredev.pro
 * accederá a sorteos mensuales de suscripciones, regalos y descuentos.
 *
 * Desarrolla un programa que lea los registros de un fichero .csv y
 * seleccione de manera aleatoria diferentes ganadores.
 * Requisitos:
 * 1. Crea un .csv con 3 columnas: id, email y status con valor "activo"
 *    o "inactivo" (y datos ficticios).
 *    Ejemplo: 1 | test@test.com | activo
 *             2 | test2@test.com | inactivo
 *    (El .csv no debe subirse como parte de la corrección)
 * 2. Recupera los datos desde el programa y selecciona email aleatorios.
 * Acciones:
 * 1. Accede al fichero .csv y selecciona de manera aleatoria un email
 *    ganador de una suscripción, otro ganador de un descuento y un último
 *    ganador de un libro (sólo si tiene status "activo" y no está repetido).
 * 2. Muestra los emails ganadores y su id.
 * 3. Ten en cuenta que la primera fila (con el nombre de las columnas)
 *    no debe tenerse en cuenta."""

my_file = "newsletter_users.csv"
columns = ['id', 'email', 'status']
users = [{'id':1, 'email':'supermario@mouredev.com', 'status':'activo'},
         {'id':2, 'email':'darkvader@mouredev.com', 'status':'activo'},
         {'id':3, 'email':'pikachu@mouredev.com', 'status':'activo'},
         {'id':4, 'email':'joseluistorrente@mouredev.com', 'status':'activo'},
         {'id':5, 'email':'homersimpson@mouredev.com', 'status':'activo'},
         {'id':6, 'email':'mickeymouse@mouredev.com', 'status':'activo'},
         {'id':7, 'email':'sansastark@mouredev.com', 'status':'activo'},
         {'id':8, 'email':'fionagalagher@mouredev.com', 'status':'activo'},
         {'id':9, 'email':'michaelscott@mouredev.com', 'status':'activo'},
         {'id':10, 'email':'sheldoncooper@mouredev.com', 'status':'activo'},
         {'id':11, 'email':'spiderman@mouredev.com', 'status':'activo'},
         {'id':12, 'email':'walterwhite@mouredev.com', 'status':'activo'},
         {'id':13, 'email':'petergriffin@mouredev.com', 'status':'activo'},
         {'id':14, 'email':'rachelgreen@mouredev.com', 'status':'activo'},
         {'id':15, 'email':'jessicajones@mouredev.com', 'status':'activo'},
         {'id':16, 'email':'ricksanchez@mouredev.com', 'status':'activo'},
         {'id':17, 'email':'maxrockatansky@mouredev.com', 'status':'activo'},
         {'id':18, 'email':'hackerman@mouredev.com', 'status':'activo'},
         {'id':19, 'email':'elliotalderson@mouredev.com', 'status':'activo'},
         {'id':20, 'email':'jesusway69@mouredev.com', 'status':'activo'},]

def create_csv(users_list:list):
    with open(my_file, mode='w', newline='') as file:
        writer = csv.DictWriter(file, delimiter = ';', fieldnames = columns )
        writer.writeheader()
        for user in users_list:
           writer.writerow(user)
    


def read_dict_csv():
    with open(my_file) as file:
        content_dict_csv = csv.DictReader(file, delimiter = ';')
        for row in content_dict_csv:
            print("ID:", '{:<4}'.format(row['id']), "Email:", '{:<30}'.format(row['email']), "Estado: ", row['status'])
            content_dict_csv
    print()

def lottery()->list:
    active_list = []
    with open(my_file) as file:
        content_dict_csv = csv.DictReader(file, delimiter = ';')
        content_list_csv = list(content_dict_csv)
    for user in content_list_csv:
        if user['status'] == 'activo':
            active_list.append(dict(user))  
    if len(active_list) < 3:
        print("No quedan suficientes participantes para lanzar los 3 sorteos, fin del programa.")
        return []
    return active_list  

        
def menu():
    while True:
        print("""\n1- Mostrar listado de participantes
2- Lanzar sorteo
3- Resetear toda la lista de participantes con estado activo 
4- Salir""")
        option = input("Elija entre estas 4 opciones -> ")
        if not option.isdigit() or int(option) < 1 or int(option) > 4:
            print("Sólo se pueden introducir números del 1 al 3")
        elif option == '1':
            read_dict_csv()
        elif option == '2':
            if len(lottery()) == 0:
                break
            subscription_winner = random.choice(lottery())
            print(f"\nEl ganador de la subscripción tiene el ID: {subscription_winner['id']} y su email es {subscription_winner['email']}")
            subscription_winner['status'] = 'inactivo'
            create_csv(list(lottery()))
            time.sleep(1)

            discount_winner = random.choice(lottery())
            print(f"El ganador del descuento tiene el ID: {discount_winner['id']} y su email es {discount_winner['email']}")
            discount_winner['status'] = 'inactivo'
            create_csv(list(lottery()))
            time.sleep(1)

            book_winner = random.choice(lottery())
            print(f"El ganador del libro tiene el ID: {book_winner['id']} y su email es {book_winner['email']}")
            book_winner['status'] = 'inactivo'
            create_csv(list(lottery()))

        elif option == '3':
            create_csv(users)
        else:
            break
menu()





        







#ejemplos: https://pywombat.com/articles/archivos-csv-python