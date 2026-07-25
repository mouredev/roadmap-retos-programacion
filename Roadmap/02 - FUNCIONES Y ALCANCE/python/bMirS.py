#FUNCION DINAMICA EN PARAMETROS
def  diferentessaludos(*nombres):
    for nombre in nombres:
        print(f"Hola, {nombre}")
#Ejemplo de llamado diferentessaludos("Python", "Luisa", "Maria")
#FUNCIÓN CON PARAMETROS TIPO CLAVE Y DATO
def nombres(**nombres):
    for clave, valor in nombres.items():
        print(f" Clave: {clave}, Valor: {valor}")
"""Llamada de la funcion
nombres(
edad="87"
nombre="Maria"
escuela="FESA"

)"""
#FUNCIÓN VACIA 

def figuras():

    tam = int(input("Ingresa el tamaño de la X (número impar): "))

    for fila in range(0, tam):
        for columna in range(0, tam):
            
            if fila == columna or fila + columna == tam - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()
#FUNCIÓN CON PARAMETROS
def figurasp(opc, tam):
    match opc:
            case "1": #Triangulo normal

                for fila in range(0, tam):
                    for columna in range(0, fila+1):
                        print("*", end="")
                    print()

            case "2":
                for fila in range(0, tam):
                    for columna in range(0, tam):
                        if(fila+columna>=tam-1):
                            print("*", end="")
                        else:
                            print(" ", end="") 
                    print() 

            case "3": #diamante 
                tam2 = tam // 2

                for fila in range(0, tam2 + 1):
                
                    print(" " * (tam2 - fila) + "*" * (2 * fila + 1))
                for fila in range(1, tam2+1):
                    print(" "*(fila)+"*"*(tam-(2*fila)))
            case "4": #Reloj fijo
                tam=5
                for i in range(0, 3):
                    print(" "*i+"*"*(tam-2*i))
                for i in range(1, 3):
                    print(" "*(2-i)+"*"*(2*i+1))
#FUNCIONES CON VALORES POR DEFECTO
def divEnter(num=5, num2=6):
    return num//3
def saludo(greet, name):
    return f"{greet}, {name}"
def misaludo():
    return "Hola", "Barbara"
figuras()
print("Elige una opcion 1,2,3")
opcion=input("La opción es: ")
tama=int(input("Ingresa el tamaño de tu figura: "))
figurasp(opc=opcion, tam=tama)
divEnter() #-> Se usa parametros por defecto

#IMPRIMIR EL RETORNO
print(saludo(name="Barbara", greet="Hi"))
#Guardar los valores del return 
greet,name=misaludo()
print(greet)
diferentessaludos("Python", "Luisa", "Maria")
 
#VARIABLE GLOBAL 
variableglobal="Maria"
def funcionM():
    varlocar="Hola"
    print(variableglobal)  #Mi función reconoce el nombre de la variable aunque no este 
#print(varlocal) Da error por que es una variable local

"""* DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 */"""
def fizzbuzzmod(parametro1:str, parametro2:str)-> int:
     contador=0
     for i in range(1,101):
        if i%3==0 and i%5==0:
            print(parametro1+parametro2)
            
        elif i%3==0:
            print(parametro1)
            
        elif i%5==0:
            print(parametro2)
            
        else:
            print(i)
            contador=contador+1
     return contador

fizzbuzzmod(parametro2="texto1", parametro1="texto2")