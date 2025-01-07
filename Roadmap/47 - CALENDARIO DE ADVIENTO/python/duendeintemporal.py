#47 { Retos para Programadores } CALENDARIO DE ADVIENTO 

# Bibliography reference:
# I use GPT as a reference and sometimes to correct or generate proper comments.

"""
 * EJERCICIO:
 * ¡Cada año celebramos el aDEViento! 24 días, 24 regalos para
 * developers. Del 1 al 24 de diciembre: https://adviento.dev
 *
 * Dibuja un calendario por terminal e implementa una
 * funcionalidad para seleccionar días y mostrar regalos.
 * - El calendario mostrará los días del 1 al 24 repartidos
 *   en 6 columnas a modo de cuadrícula.
 * - Cada cuadrícula correspondiente a un día tendrá un tamaño
 *   de 4x3 caracteres, y sus bordes serán asteríscos.
 * - Las cuadrículas dejarán un espacio entre ellas.
 * - En el medio de cada cuadrícula aparecerá el día entre el
 *   01 y el 24.
 *
 * Ejemplo de cuadrículas:
 * **** **** ****
 * *01* *02* *03* ...
 * **** **** ****
 *
 * - El usuario seleccioná qué día quiere descubrir.
 * - Si está sin descubrir, se le dirá que ha abierto ese día
 *   y se mostrará de nuevo el calendario con esa cuadrícula
 *   cubierta de asteríscos (sin mostrar el día).
 *
 * Ejemplo de selección del día 1
 * **** **** ****
 * **** *02* *03* ...
 * **** **** ****
 *
 * - Si se selecciona un número ya descubierto, se le notifica
 *   al usuario.

"""

log = print

import sys

prices = [
    "$29.99 and Basic Linux Terminal Usage course",
    "$39.99 and How to Perform Smart Commits? course",
    "$49.99 and Introduction to Programming Logic course",
    "$49.99 and Database Fundamentals course",
    "$49.99 and Best Practices in Python course",
    "$59.99 and Functional Programming Fundamentals course",
    "$59.99 and IoT: Current Applications course",
    "$69.99 and Software Design Patterns in Python course",
    "$69.99 and 0 to Hero in PostgreSQL course",
    "$79.99 and Qt4 Interface Development course",
    "$79.99 and Applying SOLID Patterns in Java course",
    "$79.99 and Go: The Language of the Future? course",
    "$89.99 and C# Development course",
    "$89.99 and Artificial Intelligence Fundamentals course",
    "$99.99 and Agile Methodologies Diploma course",
    "$99.99 and Django Rest Framework (DRF) Primer course",
    "$99.99 and Optimization Algorithms in C++ course",
    "$109.99 and Building REST Services with AWS API Gateway and Lambda course",
    "$119.99 and Data Science with Python and R course",
    "$79.99 and Object-Oriented Programming in Java course",
    "$89.99 and Traditional Methodologies Paradigm: Still Relevant? Applicable Cases course",
    "$69.99 and NumPy and Pandas in Python course",
    "$59.99 and Blockchain Fundamentals course",
    "$79.99 and Microservices Architecture with Spring Boot course",
    "$89.99 and Ethical Hacking and Cybersecurity Essentials course"
]

def draw_calendar(discovered_days):
    COLUMNS_COUNT = 6
    CELL_WIDTH = 4
    CELL_HEIGHT = 3

    calendar = ''

    for row in range(CELL_HEIGHT):
        for day in range(1, 25):
            if row == 1:
                if day in discovered_days:
                    calendar += '*' * CELL_WIDTH
                else:
                    calendar += f'*{str(day).zfill(2)}*'
            else:
                calendar += '*' * CELL_WIDTH
            
            if day % COLUMNS_COUNT == 0:
                calendar += '\n'
            else:
                calendar += ' '
        calendar += '\n'

    return calendar

def handle_user_input(discovered_days):
    while True:
        try:
            day = int(input('Enter the day you want to discover (1-24): '))
            if day < 1 or day > 24:
                log('\nInvalid day. Please enter a number between 1 and 24.\n')
                continue

            if day in discovered_days:
                log(f'\nDay {day} has already been discovered.\n')
            else:
                log(f'\nGift of the day {day}: {prices[day - 1]} 🎁 ')
                log(f'\nYou have discovered day {day}!\n')
                return discovered_days + [day]
        except ValueError:
            log('\nInvalid input. Please enter a number between 1 and 24.\n')

def main():
    discovered_days = []

    while len(discovered_days) < 24:
        log('\n     Adviento Calendar!\n')
        log(draw_calendar(discovered_days))
        discovered_days = handle_user_input(discovered_days)

    log('\n     Adviento Calendar!\n')
    log(draw_calendar(discovered_days))
    log('Congratulations! You have discovered all 24 days.')

if __name__ == '__main__':
    main()
