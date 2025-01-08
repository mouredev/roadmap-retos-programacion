'''
Exercise #01: Operadores y estructuras de control
- Create examples using all the operators of your language:
    Arithmetic, logics, comparison, asignation, identity, belonging, bits...
- Using the operations with the operators you want, make examples
that represent all control structures that are available on your language:
    Conditionals, iterations, exceptions...
- You must print on the terminal the result of all the examples.

Difficulty Extra (optional):
- Build a program that prints by console all the numbers between 10 and 55 (included), even numbers and are either multiple of 3 nor the 16
'''

def logics():
    num1 : float = 2.5
    num2 : int = 7
    word : str = 'hello world'
    list_num : list = [2, 5, 8, 20, 38]

    if 2.5 == num1 and 7 == num2:
        print(f'num1 is 2.5 and num2 is 7')
    
    if 2.5 != num1 or 2.5 != num2:
        print(f'Num1 is 2.5 or num2 is 2.5')
    
    for letter in word:
        print(letter)

    t = 0
    while t in range(len(list_num)):
        print(list_num[t]) 
        t += 1

def arithmetic_operations():
    '''
    Examples of all arithmetic operations possible on python
    '''
    sum = 2 + 3
    print(f'2 + 3 = {sum}')
    diff = 9 - 4
    print(f'9 - 4 = {diff}')
    multiply = 2 * 3
    print(f'2 * 3 = {multiply}')
    exponent = 2 ** 6
    print(f'2^6 = {exponent}')
    division = 4 / 2
    print(f'4 / 2 = {division}')
    low_division = 7 // 2
    print(f'7 // 2 = {low_division}')
    module = 3 % 2
    print(f'3 % 2 = {module} (is the rest of the division 3 / 2)' )
    
def comparison():
    '''
    Examples of all comparison opartions possibles on python
    '''

    equal_comparison = 4 == 4
    print(f'4 == 4 --> {equal_comparison}')
    not_equal_comparison = 4 != 4
    print(f'4 != 4 --> {not_equal_comparison}')
    greater_comparison = 3 > 2
    print(f'3 > 2 --> {greater_comparison}')
    less_comparison = 3 < 2
    print(f'3 < 2 --> {less_comparison}')
    
    greater_or_equal_comparison = 3 >= 5
    print(f'3 >= 5 --> {greater_or_equal_comparison}')
    less_or_equal_comparison = 3 <= 5
    print(f'3 <= 5 --> {less_or_equal_comparison}')

def difficult_part():
    print('\n ======= DIFFICULT PART OUTPUT =======')
    for i in range(10, 56):
        if 16 == i:
            continue
        elif 0 == (i % 3):
            continue
        elif 0 == (i % 2):
            print(i)

if __name__ == '__main__':
    arithmetic_operations()
    comparison()
    logics()
    difficult_part()
