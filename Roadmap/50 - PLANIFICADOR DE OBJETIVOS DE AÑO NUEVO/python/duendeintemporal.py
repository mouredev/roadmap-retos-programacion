#50 { Retos para Programadores } PLANIFICADOR DE OBJETIVOS DE AÑO NUEVO 

# Bibliography reference:
# I use GPT as a reference and sometimes to correct or generate proper comments.

"""
 * EJERCICIO:
 * El nuevo año está a punto de comenzar...
 * ¡Voy a ayudarte a planificar tus propósitos de nuevo año!
 *
 * Programa un gestor de objetivos con las siguientes características:
 * - Permite añadir objetivos (máximo 10)
 * - Calcular el plan detallado
 * - Guardar la planificación
 *
 * Cada entrada de un objetivo está formado por (con un ejemplo):
 * - Meta: Leer libros
 * - Cantidad: 12
 * - Unidades: libros
 * - Plazo (en meses): 12 (máximo 12)
 *
 * El cálculo del plan detallado generará la siguiente salida:
 * - Un apartado para cada mes
 * - Un listado de objetivos calculados a cumplir en cada mes
 *   (ejemplo: si quiero leer 12 libros, dará como resultado
 *   uno al mes)
 * - Cada objetivo debe poseer su nombre, la cantidad de
 *   unidades a completar en cada mes y su total. Por ejemplo:
 *
 *   Enero:
 *   [ ] 1. Leer libros (1 libro/mes). Total: 12.
 *   [ ] 2. Estudiar Git (1 curso/mes). Total: 1.
 *   Febrero:
 *   [ ] 1. Leer libros (1 libro/mes). Total: 12.
 *   ...
 *   Diciembre:
 *   [ ] 1. Leer libros (1 libro/mes). Total: 12.
 *
 * - Si la duración es menor a un año, finalizará en el mes
 *   correspondiente.
 *
 * Por último, el cálculo detallado debe poder exportarse a .txt
 * (No subir el fichero)

"""

log = print

import os

file_path = 'goals.txt'
max_goals = 10
goals = []

month_names = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

def menu():
    log('\n--- New Year Goals Planner ---')
    log('1. Add Goal')
    log('2. View Goals')
    log('3. Calculate Detailed Year Plan')
    log('4. Export Plan to .txt')
    log('5. Exit')
    option = input('Select an option: ')
    handle_menu_option(option)

def handle_menu_option(option):
    if option == '1':
        add_goal()
    elif option == '2':
        view_goals()
    elif option == '3':
        calculate_detailed_year_plan()
    elif option == '4':
        export_plan()
    elif option == '5':
        exit_program()
    else:
        log('Invalid option, choose a number between 1 and 5. Please try again.')
        menu()

def add_goal():
    if len(goals) >= max_goals:
        log('Maximum number of goals reached.')
        return menu()

    ask_goal_name()

def ask_goal_name():
    log('Examples of goals: Learn, Read, Practice')
    name = input('Goal Name: ')
    if not name:
        log('Goal name cannot be empty. Please try again.')
        return ask_goal_name()
    ask_quantity(name)

def ask_quantity(name):
    log('Please enter a positive number for the quantity.')
    quantity = input('Quantity: ')
    try:
        quantity_num = int(quantity)
        if quantity_num <= 0:
            raise ValueError
    except ValueError:
        log('Quantity must be a positive number. Please try again.')
        return ask_quantity(name)
    ask_units(name, quantity_num)

def ask_units(name, quantity):
    log('Examples of units: Books, Courses, Languages')
    units = input('Units: ')
    if not units:
        log('Units cannot be empty. Please try again.')
        return ask_units(name, quantity)
    ask_deadline(name, quantity, units)

def ask_deadline(name, quantity, units):
    log('Deadline must be a number between 1 and 12 months.')
    deadline = input('Deadline (in months, max 12): ')
    try:
        deadline_num = int(deadline)
        if deadline_num < 1 or deadline_num > 12:
            raise ValueError
    except ValueError:
        log('Deadline must be a number between 1 and 12. Please try again.')
        return ask_deadline(name, quantity, units)
    
    goals.append({'name': name, 'quantity': quantity, 'units': units, 'deadline': deadline_num})
    log('Goal added!')
    menu()

def view_goals():
    if not goals:
        log('No goals registered.')
    else:
        log('\nGoals:')
        for index, goal in enumerate(goals):
            log(f"{index + 1}. {goal['name']} - {goal['quantity']} {goal['units']} over {goal['deadline']} months")
    menu()

def capitalize_first_letter_of_each_word(string):
    return ' '.join(word.capitalize() for word in string.split())

def calculate_detailed_year_plan():
    if not goals:
        log('No goals to calculate.')
        return menu()

    plan = {}
    for goal in goals:
        total_tasks = goal['quantity']
        total_months = goal['deadline']
        monthly_goal = total_tasks // total_months
        remainder = total_tasks % total_months

        for month in range(1, total_months + 1):
            if month not in plan:
                plan[month] = []

            tasks_for_month = monthly_goal
            if month <= remainder:
                tasks_for_month += 1  # Distribute the remainder tasks

            capitalized_goal_name = capitalize_first_letter_of_each_word(goal['name'])
            capitalized_goal_units = capitalize_first_letter_of_each_word(goal['units'])

            plan[month].append(f"{capitalized_goal_name} ({tasks_for_month} {capitalized_goal_units}/month). Total: {goal['quantity']}. Deadline: {month_names[total_months - 1]}.")

    log('\n--- Detailed Year Plan ---')
    for month in range(1, 13):
        log(f"{month_names[month - 1]}:")
        if month in plan:
            for index, item in enumerate(plan[month]):
                log(f"[ ] {index + 1}. {item}")
        else:
            log('No goals for this month.')
    menu()

def export_plan():
    plan = []
    for goal in goals:
        monthly_goal = -(-goal['quantity'] // goal['deadline'])  # Ceiling division
        for month in range(1, goal['deadline'] + 1):
            plan.append(f"Month {month}: {goal['name']} ({monthly_goal} {goal['units']}/month). Total: {goal['quantity']}.")

    with open(file_path, 'w') as file:
        file.write('\n'.join(plan))
    
    log(f'Plan exported to {file_path}')
    menu()

def exit_program():
    log('Exiting the program.')
    exit()

# Start the program
menu()

# Output Example:
"""   
--- Detailed Year Plan ---
January:
[ ] 1. Learn (3 Martial Arts Skills/month). Total: 30. Deadline: December.
[ ] 2. Read (4 Diverse Articules/month). Total: 48. Deadline: December.
[ ] 3. Practice (1 Languages/month). Total: 8. Deadline: December.
February:
[ ] 1. Learn (3 Martial Arts Skills/month). Total: 30. Deadline: December.
[ ] 2. Read (4 Diverse Articules/month). Total: 48. Deadline: December.
[ ] 3. Practice (1 Languages/month). Total: 8. Deadline: December.
March:
[ ] 1. Learn (3 Martial Arts Skills/month). Total: 30. Deadline: December.
[ ] 2. Read (4 Diverse Articules/month). Total: 48. Deadline: December.
[ ] 3. Practice (1 Languages/month). Total: 8. Deadline: December.
April:
[ ] 1. Learn (3 Martial Arts Skills/month). Total: 30. Deadline: December.
[ ] 2. Read (4 Diverse Articules/month). Total: 48. Deadline: December.
[ ] 3. Practice (1 Languages/month). Total: 8. Deadline: December.
May:
[ ] 1. Learn (3 Martial Arts Skills/month). Total: 30. Deadline: December.
[ ] 2. Read (4 Diverse Articules/month). Total: 48. Deadline: December.
[ ] 3. Practice (1 Languages/month). Total: 8. Deadline: December.
June:
[ ] 1. Learn (3 Martial Arts Skills/month). Total: 30. Deadline: December.
[ ] 2. Read (4 Diverse Articules/month). Total: 48. Deadline: December.
[ ] 3. Practice (1 Languages/month). Total: 8. Deadline: December.
July:
[ ] 1. Learn (2 Martial Arts Skills/month). Total: 30. Deadline: December.
[ ] 2. Read (4 Diverse Articules/month). Total: 48. Deadline: December.
[ ] 3. Practice (1 Languages/month). Total: 8. Deadline: December.
August:
[ ] 1. Learn (2 Martial Arts Skills/month). Total: 30. Deadline: December.
[ ] 2. Read (4 Diverse Articules/month). Total: 48. Deadline: December.
[ ] 3. Practice (1 Languages/month). Total: 8. Deadline: December.
September:
[ ] 1. Learn (2 Martial Arts Skills/month). Total: 30. Deadline: December.
[ ] 2. Read (4 Diverse Articules/month). Total: 48. Deadline: December.
[ ] 3. Practice (0 Languages/month). Total: 8. Deadline: December.
October:
[ ] 1. Learn (2 Martial Arts Skills/month). Total: 30. Deadline: December.
[ ] 2. Read (4 Diverse Articules/month). Total: 48. Deadline: December.
[ ] 3. Practice (0 Languages/month). Total: 8. Deadline: December.
November:
[ ] 1. Learn (2 Martial Arts Skills/month). Total: 30. Deadline: December.
[ ] 2. Read (4 Diverse Articules/month). Total: 48. Deadline: December.
[ ] 3. Practice (0 Languages/month). Total: 8. Deadline: December.
December:
[ ] 1. Learn (2 Martial Arts Skills/month). Total: 30. Deadline: December.
[ ] 2. Read (4 Diverse Articules/month). Total: 48. Deadline: December.
[ ] 3. Practice (0 Languages/month). Total: 8. Deadline: December.

"""