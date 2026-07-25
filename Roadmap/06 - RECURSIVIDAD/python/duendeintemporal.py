#6 { Retos para Programadores } Recursividad
"""
 * EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición).
 """

log = print  # Shortening print function to log

# A recursive function typically is formed when a function calls itself by name
def count_back(n):
    log(n)
    if n == 0:
        return # None
    return count_back(n - 1)

log(count_back(100))

# Without recursion
def power_v1(base, exponent):
    result = 1 if exponent == 0 else base
    for i in range(2, exponent + 1):
        result *= base
    return result

log(power_v1(4, 3))  # 64

# With recursion
def power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * power(base, exponent - 1)

log(power(4, 3))  # 64

# This is rather close to the way mathematicians define exponentiation and
# arguably describes the concept more clearly than the looping variant.
# The function calls itself multiple times with ever smaller exponents to achieve the
# repeated multiplication.

# But this implementation has one problem: in typical Python implementations,
# it’s about three times slower than the looping version. Running through
# a simple loop is generally cheaper than calling a function multiple times.

# In the case of the power function, the inelegant (looping) version is still fairly
# simple and easy to read. It doesn’t make much sense to replace it with the
# recursive version.

# Extra difficulty exercises

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

log(factorial(5))  # 120


# This function returns the number equivalent to the position in the Fibonacci series
def fibonacci_num(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_num(n - 1) + fibonacci_num(n - 2)

log(fibonacci_num(17))  # 1597

# Note: The recursive version with memoization is more efficient than the simple recursive one,
# as it avoids redundant calculations. However, it still uses the call stack, which can be a problem for very large values of n.

def fibonacci_num_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    if n == 1:
        return 1
    memo[n] = fibonacci_num_memo(n - 1, memo) + fibonacci_num_memo(n - 2, memo)
    return memo[n]

log(fibonacci_num_memo(17))  # 1597

# The iterative approach is generally more efficient in terms of time and space, as it does not use the call stack of recursion.
""" The iterative approach not handle very large Fibonacci numbers properly due to the limitations of standard integer representation in some programming languages. However, Python's integers can grow as large as the memory allows, so it should work fine for large Fibonacci numbers like fibonacci(4222). """

def iterative_fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    a, b = 0, 1
    resultado = 0

    for i in range(2, n + 1):
        resultado = a + b
        a = b
        b = resultado
    return resultado

log(iterative_fibonacci(4222))  # This will likely result in a very large number
''' 991589988362642070289381809859238899810818978690066481567009961084370343355020445771885410736432350985748230736466733366235493773173353807008180411573721923522628193615012792654580349124839525370327127087212639668504243599805635642440051280951077467227974758307254927414086395913327066620720820654856388551207498973370655978255046381155991312335751278534594089041280672977552114511923101524007980516923288134966032329067540128365146684772558653549788584628220581142887000982711896691538088856557710641299562290047382724565369870585638339456142817193642656279468367921367028940944988116809057276755968908731893570902338692496954534233789481260096044188777018433397442568357873891235554198879570974119614520991455054319986189584806128290103014082993662230000784648446189143070226650569527550697283718937846526095749543627404591780914731497810266886509088704777805009571566121451309311 '''
log(iterative_fibonacci(453))  # 20985341020594289480596202471862246559405946478745659997715004840583924030397583511583383173698

# Simulating a window load event (not applicable in standard Python, but for demonstration)
def on_load():
    body_style = {
        'background': '#000',
        'text-align': 'center'
    }
    
    title = {
        'text': 'Retosparaprogramadores #6.',
        'font-size': '3.5vmax',
        'color': '#fff',
        'line-height': '100vh'
    }
    
    # Simulating a delay (not applicable in standard Python, but for demonstration)
    import time
    time.sleep(2)

    log("Title:", title['text'])

# Call the simulated load function
on_load()