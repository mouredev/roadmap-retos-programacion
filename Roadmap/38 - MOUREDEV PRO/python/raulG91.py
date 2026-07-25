import csv
import os
import random

def read_csv(filename):
    values = []
    try:
        with open(filename,newline='') as csvfile:
            reader = csv.reader(csvfile,delimiter="|")
            for index,row in enumerate(reader):
                if index != 0 and row[2].lower()=="activo":
                    values.append(row)
    except:
        print("Error opening the file")
    return values
          

#Get path for the file 
path = os.path.join(os.path.dirname(__file__),"file.csv")
#Read csv values from the file
values = read_csv(path)

if len(values)>=3:
    #Get 3 random elements from the list
    list_winners = random.sample(values,k=3)

    #First one win a subscription
    print(f'Ganadaor de la subscripcion {list_winners[0][1]} con id: {list_winners[0][0]}')

    #Second wins a discount
    print(f'Ganador del descuento {list_winners[1][1]} con id {list_winners[1][0]}')

    #Third one wins a book
    print(f'Ganador del libro {list_winners[2][1]} con id {list_winners[2][0]}')
else:
    print("Debe haber al menos 3 usuarios")