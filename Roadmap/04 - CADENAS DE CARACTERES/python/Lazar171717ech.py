## 1. STRINGS ##

string_uno = "Hola" # Esto es una cadena de caracteres, también conocidas como strings o str
# También podemos definir un string con la triple comilla, ponré un ejemplo más tarde.
print(string_uno)
print(f"string_uno + ', soy Juan' = {string_uno + ', soy Juan'}") # Podemos concatenarlos con el simbolo +
print(f"'Hola' ', soy Juan' = {'Hola' ', soy Juan'}") # Podemos concatenar dos str poniendolos juntos (no funciona con variables)
print(f"string_uno * 5 = {string_uno * 5}") # Podemos hacer que se repita con el simbolo * y el numero de repeticiones
string_uno += ", soy Juan"
print(string_uno) # También se le aplican los operadores de reasignación
print(f" len(string_uno) = {len(string_uno)}") # Con la función len podemos saber la longitud de un string
print(f"string_uno.lower() = {string_uno.lower()}") # Con el método lower se cambiarán las mayúsculas por minúsculas
print(f"string_uno.upper() = {string_uno.upper()}") # Con el método upper se cambiarán las minúsculas por mayúsculas
print(f"string_uno.replace('Juan', 'Ernesto') = {string_uno.replace('Juan', 'Ernesto')}") # con el método replace sustituimos un string dentro del principal por otro
# A cada caracter del string se le asigna un valor numérico de izquierda a derecha empezando por el 0. 
print(f"string_uno.find('Juan') = {string_uno.find('Juan')}") # Con el método find podemos saber en que posición se encuentra un string dentro de otro,
# En caso de haber varios se debuelve el primero por la izquierda y en caso de no encontrar debuelve -1
print(f"string_uno.count('a') = {string_uno.count('a')}") # Al igual que en listas podemos usar el método count para saber cuantas veces está us string en otro.
# Esto lo explico porque lo usaré en el ejercicio extra.
print(f"string_uno[4] = {string_uno[4]}") # Podemos mostrar el caracter en una posicion con la sintaxix: variable_str[posición]
print(f"string_uno[1:7] = {string_uno[1:7]}") # Podemos mostrar una parte del string con la sintaxis: variable_str[posición para empezar:posición para finalizar]
# Podemos quitar las posiciones si queremos que empieze por el principio o termine por el final.
print(f"string_uno[1:-3] = {string_uno[1:-3]}") # Si ponemos un número negativo simplemente nos referimos a la posición comenzando por la derecha comenzando por -1.
print(f"string_uno[-4] = {string_uno[-4]}") # También funciona para mostrar los caracteres
print(f"string_uno[::-1] = {string_uno[::-1]}") # Si usamos el [::-1] estaríamos invirtiendo el string
print(f"\n{string_uno}") # Usando \n en un string sería como insertar un salto de línea
print(f"\t{string_uno}") # Usando \t en un string sería como insertar una tabulación
string_en_lineas = """Hola, soy Juan 
Hola, soy Ernesto""" #Como ya he dicho se puede definir un str en varias líneas con la triple comilla
string_en_lineas2 = "Hola, soy Juan\nHola, soy Ernesto"
print(f"Es igual usar n que triple comilla? = {string_en_lineas == string_en_lineas2}") # Sí
#Se puede usar un bucle for para recorrer un string:
for index in string_uno:
    print(index)
print(f"'Juan' in string_uno = {'Juan' in string_uno}") # Se puede saber si un string está en otro string usando in:
#Llevo usandolo todo el rato pero se pueden usar tanto comillas simples como comillas dobles. Esto es para poder usar un tipo de comillas en un string
print(f"Él dijo: '{string_uno}'.")
print(f"Él dijo: \"{string_uno}\"") #También se puede usar el mismo tipo si ponemos \ + las comillas
print(r"\n <-- No se está leyendo como un salto de línea") # usando r delante podemos hacer que lea \ como el caracter
print(fr"\n {string_uno}") # Podemos unsar el formateo (f) y el raw (r) al mismo tiempo
#Por supuesto el formateo se usa poniendo f delante y lo que haya entre {} dentro del string se leerá como codigo a imprimir
string_dos = "\n \t\nHola Juan\n\t \t"
print(f"string_dos.strip() = {string_dos.strip()}") # Con el método strip eliminamos los espacios, saltos de línea y tabulaciones innecesarios al principio y al final
# Si solo los queremos quitar de uno de los lados podemos usar rstrip o lstrip
print(f"string_dos.rstrip() = {string_dos.rstrip()}")
print(f"string_dos.lstrip() = {string_dos.lstrip()}")
print(f"string_dos.split() = {string_dos.split()}") # Con el método split convertimos el split en una lista con todos los strings separados por " ", \n o \t
print(f"string_dos.split(' ') = {string_dos.split(' ')}") # Si le pasamos un argumento serán los strings separados por el argumento dado
 
## 2. Dificultad Extra ##

def anagrama(wrd1, wrd2):
    wrd1,wrd2 = wrd1.lower(),wrd2.lower()
    for i in wrd1:
        if i in wrd2 and wrd1.count(i) == wrd2.count(i): pass
        else: return(False)
    return(True)

def isograma(wrd1, wrd2):
    wrd1,wrd2 = wrd1.lower(),wrd2.lower()
    for i in wrd1:
        if wrd1.count(i) == 1: pass
        else: return(False)
    for i in wrd2:
        if wrd2.count(i) == 1: pass
        else: return(False)
    return(True)

def palindromo(wrd1, wrd2):
    wrd1,wrd2 = wrd1.lower(),wrd2.lower()
    if wrd1 != wrd1[::-1]: return False
    if wrd2 != wrd2[::-1]: return False
    else: return True

def queson(string1, string2):
    if palindromo:
        print("Ambos son palíndromos")
    elif anagrama(string1, string2):
        print("Son anagramas")
    elif isograma(string1, string2):
        print("Ambos son isogramas")
    else: print("No son ninguno")
