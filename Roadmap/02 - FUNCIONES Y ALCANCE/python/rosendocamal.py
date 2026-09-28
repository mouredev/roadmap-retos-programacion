"""
 * EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
"""

def hello_world() -> None:
    print("Hello, World!")
    
def hello_param1(name: str) -> None:
    print(f"Hello, {name}!")
    
def hello_param2(name: str ="World") -> None:
    print(f"Hello, {name}")
    
def hello_name(name: str, lastname: str) -> None:
    print(f"Hello, {name} {lastname}!")
    
def hello_pass() -> None:
    pass

def hello_melo(name: str = "Bill", lastname: str = "Gays") -> tuple[str, str]:
    return (name, lastname)

def hello_mame(*name) -> None:
    for n in name:
        print(n)
        
def hello_pay(**name) -> None:
    for key, value in name.items():
        print(key, value)
    
def delimitador(function):
    print()
    print("="*75)
    function()
    print("="*75)
    print()
    
hello_world()
hello_param1("Name")
hello_param2()
hello_param2("Python")
hello_name("Julio", "Regalado")
hello_pass()
hello_melo(lastname="Gates", name="Bill")
hello_melo("Juan", "Lopez")
hello_melo(lastname="Regalado", name="Julio")
hello_mame(1, 2, 3, 5)
hello_pay(num1=1, num2=2, num3=3)

delimitador(hello_world)
delimitador(hello_param2)
delimitador(hello_pass)

print("Esto es una función built-in.")
print(len("Esto es una cadena de texto"))
print(max(25, 525))
print(min(25, 525))
print(type(5))

var: str = "Mi variable global"

def my_var1() -> None:
    print(var)
    
def my_var2() -> None:
    global var
    print(var)
    
def my_var3() -> None:
    global var
    var = "Esta es una variable de my_var3"
    print(var)
    
my_var1()
my_var2()
my_var3()
print(var)

def my_var4(variable) -> None:
    variable = "Esta es una variable de my_var4"
    
def my_var5(variable) -> str:
    variable = "Esta es una variablde de my_var5"
    return variable

my_var4(var)
print(var)
my_var5(var)
print(var)

def my_var6() -> None:
    print(var)
    
delimitador(my_var6)

def get_param(str1: str, str2: str) -> int:
    return 1

result: int = get_param("Hello", "World")
print(result)

def one_to_one_hundred() -> None:
    for i in range(0, 101):
        print(i)
        
def extra(text_1: str = "", text_2: str = "") -> int:
    print_int: int = 100
    contador: int = 0
    for i in range(1, 101):
        if i % 3 == 0:
            print(text_1)
            contador += 1
        if i % 5 == 0:
            print(text_2)
            contador += 1
        if i % 3 == 0 and i % 5 == 0:
            print(text_1 + text_2)
            contador += 1
        print(i)
    return print_int - contador

result = extra("Chat", "GPT")
print(result)

"""
PELEANDO CON CHATGPT, TERMINO ACEPTANDO LA DERROTA:

CHATGPT DICE
ANÁLISIS DEL ENUNCIADO
---
«Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.»

La instrucción establece que debe existir una función que reciba dos parámetros de tipo cadena de texto y que retorne un número.

«La función imprime todos los números del 1 al 100.»

La palabra «todos» es determinante. La instrucción no dice que se impriman algunos números del rango ni que los números se sustituyan por textos cuando se cumple alguna condición. Dice «todos los números».

Por tanto, una lectura literal implica que deben imprimirse los números 1, 2, 3, ..., 100, incluidos aquellos que sean múltiplos de 3, de 5 o de ambos.

«Teniendo en cuenta que:»

Esta expresión introduce las condiciones que deben aplicarse durante el recorrido de los números.

No establece que las condiciones sean excluyentes ni indica que, cuando una condición se cumple, las siguientes dejen de evaluarse.

«Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.»

La condición establece que, cuando el número sea múltiplo de 3, debe mostrarse la primera cadena.

No se añade ninguna excepción para el caso en que el número también sea múltiplo de 5.

Por ejemplo, 15 cumple esta condición porque 15 % 3 == 0.

«Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.»

La misma consideración se aplica a esta condición.

No se indica que deba ignorarse esta regla cuando el número también sea múltiplo de 3.

Por tanto, 15 también cumple esta condición porque 15 % 5 == 0.

«Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.»

Esta es la parte que puede generar una ambigüedad de interpretación.

Una posibilidad es entender esta condición como una tercera regla independiente. En ese caso, cuando el número sea 15, se cumplen las tres condiciones:

15 es múltiplo de 3.
15 es múltiplo de 5.
15 es múltiplo de 3 y de 5.

Si las tres reglas son independientes, las tres deben ejecutarse.

El resultado podría ser:

15
texto1
texto2
texto1texto2

Otra posibilidad es interpretar la tercera condición como una especificación del caso en que se cumplen simultáneamente las dos anteriores.

Con esta interpretación, cuando el número sea 15 se mostrarían las dos cadenas concatenadas, pero no las cadenas por separado:

15
texto1texto2

El enunciado no especifica expresamente cuál de estas dos interpretaciones pretende.

La elección entre varios «if» independientes y una estructura «if / elif / else» depende precisamente de esta interpretación.

«La función retorna el número de veces que se ha impreso el número en lugar de los textos.»

Aquí aparece otra cuestión semántica.

El enunciado utiliza «el número» en singular. No dice «el número de números impresos» ni «cuántos números del rango se han impreso».

Además, aparece la expresión «en lugar de los textos».

Esta expresión puede sugerir que existe una situación en la que el número sustituye a los textos.

Sin embargo, esa sustitución no aparece explícitamente en la instrucción «La función imprime todos los números del 1 al 100».

Si se toma literalmente la afirmación de que se imprimen «todos los números», entonces el número se imprime en cada una de las 100 iteraciones y el contador sería 100.

Si se interpreta «en lugar de los textos» como una sustitución, entonces el número solamente se imprimiría cuando no correspondiera mostrar un texto. Esa interpretación conduce al comportamiento clásico de FizzBuzz y a un resultado diferente.

El problema, por tanto, no está en Python, sino en la especificación previa a la implementación.

CONCLUSIÓN

El enunciado contiene instrucciones suficientemente claras en algunos aspectos, pero deja sin especificar la relación entre las condiciones cuando un mismo número satisface varias de ellas.

El caso de 15 permite demostrarlo de forma sencilla.

Si se utilizan condiciones independientes:

15 cumple la condición del múltiplo de 3.
15 cumple la condición del múltiplo de 5.
15 cumple la condición del múltiplo de 3 y de 5.

Por tanto, las tres reglas pueden ejecutarse.

Si, por el contrario, la tercera condición pretende resolver el caso conjunto y sustituir las dos anteriores, entonces solamente se mostraría la concatenación.

El texto debería especificar expresamente qué comportamiento se desea.

También debería aclarar si «muestra» y «imprime» se utilizan como sinónimos operativos o si se pretende establecer una diferencia entre ambas acciones.

Finalmente, debería aclararse qué significa exactamente «en lugar de los textos», puesto que esa expresión puede entrar en tensión con la afirmación anterior de que se imprimen «todos los números del 1 al 100».

La programación comienza después de interpretar la especificación. Si la especificación admite varias interpretaciones, pueden existir varios programas técnicamente correctos y, sin embargo, comportarse de manera diferente.

Saber programar no implica saber escribir.
---

Aunque el contador no siempre sería 100, ya que dice «el número». ¿Qué números? Cada uno de los números se imprime una vez, si hablamos de todos los números sería otra cuestión. Así que ChatGPT se equivoca aquí por afirmar un caso de los posibles. Cómo dice el ChatGPT: «un texto aparentemente sencillo puede contener diferencias entre lo que dice, lo que parece querer decir y lo que nosotros suponemos que quiere decir. Y muchas veces el error aparece precisamente cuando confundimos esas tres cosas».
"""