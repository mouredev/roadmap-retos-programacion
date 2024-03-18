'''
╔═══════════════════════════════════════╗
║ Autor:  tekatoki                      ║
║ GitHub: https://github.com/tekatoki   ║
║ 2024 -  Python                        ║
╚═══════════════════════════════════════╝

Exercise:
- Create examples of basic functions that represent the difereents
possibilities of the language:
    Without parametres nor return, with one or other parametres, with return values...
- Checks if you can create functions inside functions
- LOCAL and GLOBAL variables
- You must print in the CLI the results of all the examples made

Extra dificulty (optional):
- Create a function that has two string parametres and returns an int
The function prints all numbers from 1 to 100. Considering:
    - If the number is multiple of 3, show the text of the first parametre
    - If the number is multiple of 5, show the text of the second parametre
    - If the number is multiple of 3 and 5, show the two parametres concadenated
'''
def extra_difficulty (text_1:str, text_2:str):
    for num in range(1, 100 + 1):
        if 0 == num % 3 and 0 == num % 5:
            print(text_1 + text_2)
        elif 0 == num % 3:
            print(text_1)
        elif 0 == num % 5:
            print(text_2)

def checks_multiple_2(num:int):
    if num % 2 == 0:
        return True
    else:
        return False

def personal_greet(name:str, surname:str, formality:bool = False):
    if formality:
        print(f'Hello, dear {surname}')
    else:
        print(f'Hello, {name} {surname}')


def greet():
    print('Hello, python!')

if __name__ == '__main__':
    greet() # Without parametres and returns

    user_name:str = input('Introduce your name>')    
    user_surname:str = input('Introduce your surname>')

    personal_greet(user_name, user_surname, formality=False) # With three parametres
    print(checks_multiple_2(4)) # Function that returns something

    extra_difficulty('Python', 'Mathematics')

