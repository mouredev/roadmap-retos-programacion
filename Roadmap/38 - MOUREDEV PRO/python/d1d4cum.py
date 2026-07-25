import csv
import random

PATH = './d1d4cum.csv'

def main():
    active_users = []

    with open(PATH, mode='r', newline='', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)

        for row in csv_reader:
            if row[2] == 'activo':
                active_users.append(row)

    print("> Ganador de la suscripción:")
    sus_winner = random.choice(active_users)
    print(f"{sus_winner[0]} - {sus_winner[1]}")
    active_users.remove(sus_winner)

    print("> Ganador de un descuento:")
    dis_winner = random.choice(active_users)
    print(f"{dis_winner[0]} - {dis_winner[1]}")
    active_users.remove(dis_winner)

    print("> Ganador de un libro:")
    book_winner = random.choice(active_users)
    print(f"{book_winner[0]} - {book_winner[1]}")
    active_users.remove(book_winner)




if __name__ == '__main__':
    main()
