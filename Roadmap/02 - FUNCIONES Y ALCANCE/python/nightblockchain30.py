"""
- Crea ejemplos de funciones básicas que representen las diferentes
    posibilidades del lenguaje:
    Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
"""
print("\n**** PART 1 - FUNCTIONS ****\n")

def no_params_no_return_void_function():
    pass

def no_params_no_return():
    print("function no_params_no_return()")

def no_params_return():
    print("function no_params_return(): returns 'result'")
    return "result"

def params_return(x,y):
    result=x+y
    print(f"function params_return(x,y): returns {result}")
    return result


def arbitrary_params(*elements):
    result=sum(element for element in elements)
    print(f"arbitrary_params(*elements): returns {result}")
    return result

def keywords_params(dividend, divisor):
    result=dividend/divisor
    print(f"keywords_params(dividend, divisor): returns {result}")
    return result

def keyword_arbitrary_params(**elements):
    result = 0
    if ("dividend" in elements and "divisor" in elements):
        result = elements["dividend"]/elements["divisor"]
    print(f"keyword_arbitrary_params(**elements): returns {result}")
    return result

def default_value(name="Mickey"):
    print(f"function default_value(name='Mickey'): param = {name}")

def list_value(brands):
    print("function list_value(brands)")
    for brand in brands:
        print(f" - {brand}")

def positional_only_arguments(x, y, /):
    result = x * y
    print(f"function positional_only_arguments(x, y, /): returns {result}")
    return x * y

def keyword_only_arguments(*, x, y):
    result = x * y
    print(f"function keyword_only_arguments(*, x, y): returns {result}")
    return result
    
def keyword_only_positional_only_and_arguments(x, y, /, *, a, b):
    result = f"positional : {str(x*y)} ... keyword: {str(a*b)}"
    print(f"function positional_only_arguments(x, y, /): returns {result}")
    return result


def use_lambda_power_of_2(element):
    lambda_func = lambda base: pow(2,base)
    print(f"lambda function: {lambda_func}")
    result = lambda_func(element)
    print(f"function use_lambda_power_of_2: result = {result}" )
    return result

def recursion_power(base,exponent):
    print(f"function recursion_power(base,exponent): params= ({base},{exponent})")
    if exponent == 0:
      return 1
    elif (exponent == 1):
      return base
    elif (exponent == -1):
       return 1/base
    else:
        exponent -= 1 if exponent > 0 else -1
        return recursion_power(base * base, exponent)

# calling functions

print("\ncalling no_params_no_return_void_function()")
no_params_no_return_void_function()

print("\ncalling no_params_no_return()")
no_params_no_return()

print("\ncalling params_return(5,9)")
print(params_return(5,9))

print("\ncalling arbitrary_params(1,2,3,4,5,6)")
print(arbitrary_params(1,2,3,4,5,6))

print("\ncalling keywords_params(divisor=1,dividend=0)")
print(keywords_params(divisor=1,dividend=0))

print("\ncalling keywords_params(divisor=1,dividend=0)")
print(keywords_params(divisor=1,dividend=0))

print("\ncalling keyword_arbitrary_params(divisor=1)")
print(keyword_arbitrary_params(divisor=1))

print("\ncalling default_value()")
default_value()
print("\ncalling default_value('Pluto')")
default_value("Pluto")

print("\ncalling list_value('Apple','Samsung','Xiaomi')")
list_value(["Apple","Samsung","Xiaomi"])

print("\ncalling positional_only_arguments(5,9)")
print(positional_only_arguments(5,9))

print("\ncalling keyword_only_arguments(x=3,y=4)")
print(keyword_only_arguments(x=3,y=4))

print("\ncalling keyword_only_positional_only_and_arguments(5,9,a=3,b=4)")
print(keyword_only_positional_only_and_arguments(5,9,a=3,b=4))

print("\ncalling use_lambda_power_of_2(5))")
print(use_lambda_power_of_2(5))


print("\ncalling recursion_power(1,0)")
print(recursion_power(1,0))
print("\ncalling recursion_power(2,4)")
print(recursion_power(2,4))
print("\ncalling recursion_power(2,-2)")
print(recursion_power(2,-2))


""" - Comprueba si puedes crear funciones dentro de funciones."""
print("\n**** PART 2 - INNER FUNCTIONS ****\n")

def with_inner(a,b,c,d):
    result=a+b
    
    def inner_function(c,d):
        result=c+d
        print(f"function inner_function(c,d): returns {result}")
        return result
    
    result +=  inner_function(c,d)
    print(f"function with_inner(a,b,c,d): returns {result}")
    return result

print("\ncalling with_inner(1,4,10,100) that contains an inner function")
print(with_inner(1,4,10,100))

print("\ninner function cannot be called directly: inner_function(10,100)")

# Inner function cannot be called: inner_function(1))


""" - Utiliza algún ejemplo de funciones ya creadas en el lenguaje."""
print("\n**** PART 3 - BUILT-IN FUNCTIONS ****\n")

def slice_tuple_pairs_without_first(list):
    slice_function=slice(1,len(list),2)
    return list[slice_function]
print(slice_tuple_pairs_without_first(['banana','apple','orange','strawberry','pear','avocado','pineapple']))
print(f"\ncalling slice_tuple_pairs_without_first(['banana','apple','orange','strawberry','pear','avocado','pineapple'])")


def sort_reverse_and_add(list,element):
    list.append(element)
    return sorted(list,reverse=1)
print(f"\ncalling sort_reverse_and_add(['banana','apple','orange','strawberry','pear','avocado','pineapple'],'peach')")
print(sort_reverse_and_add(['banana','apple','orange','strawberry','pear','avocado','pineapple'],'peach'))


""" - Pon a prueba el concepto de variable LOCAL y GLOBAL"""
print("\n**** PART 4 - GLOBAL AND LOCAL SCOPES FOR VARIABLES ****\n")

print("setting global variable var1=1")
var1=1

def sum_local_variables(element):
    var1=3
    result = var1+element
    print(f"function sum_local_variables: result = {result}")
    return result

def sum_global_variable(element):
    result = var1+element
    print(f"function sum_global_variable: result = {result}")

    return result

def printing_local_variable():
    var2="a"
    print(f"function printing_local_variable: var2 = {var2}")

print("\ncalling sum_local_variables(10)")
sum_local_variables(10)
print("\ncalling sum_global_variable(10)")
sum_global_variable(10)

print("\ncalling printing_local_variable()")
printing_local_variable()
print("\nprinting local variable from printing_local_variable() doesn't compiles: print(var2)")


"""
DIFICULTAD EXTRA (opcional):
Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
- La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
- Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
- Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
- Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
- La función retorna el número de veces que se ha impreso el número en lugar de los textos.
"""
print("\n**** PART 5 - EXTRA FUNCTION ****\n")

def print_and_count(text1,text2):
    counter = 0
    for eachNumber in range(1,101):
        result = ''
        if(eachNumber % 3 == 0):
            result += text1
        if(eachNumber%5 == 0):
            result += text2
        if(len(result) == 0):
            counter+=1
            result=str(eachNumber)
        print(result)
    return counter

print(f"Calling print_and_count('mul3','mul5'):\n")
print(f"\nresult = {print_and_count('mul3','mul5')}")

print("\n") 