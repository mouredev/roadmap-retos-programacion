# Funciones
# Sin parámetros ni retorno, con uno o varios parámetros, con retorno...

## Funcion sin parametros ni retorno
def funcion_normal():
    print("Hola, esta es una funcion sin parametros ni retorno")
# Se llama la funcion para ejecutarla
funcion_normal()

## Funcion con varios parametros sin retorno
def funcion_2_parametros(nombre, edad):
    print(f"Hola {nombre}, tu edad es: {edad}")
# Llamando la funcion
funcion_2_parametros("Alvaro", 19)

## Funcion con varios parametros con retorno
def funcion_con_parametros_con_retorno(examen, nota):
    if examen and nota:
        if nota >= 9 and not nota <= 9:
            return print(f"Muy bien! en {examen}")
        if nota <= 6 and nota >= 5:
            return print(f"Bien hecho! en {examen}")
        if nota <= 4 and nota > 1:
            return print(f"Puedes mejorar en {examen}")
        else:
            return print(f"A mejorar!")
nota = funcion_con_parametros_con_retorno("Matematicas", 1)
print(nota)

## Funcion con parametros usando args:
def suma(*args):
    resultado = 0
    for arg in args:
        resultado += arg
    return resultado
# Usando la funcion
suma_grande = suma(1,2,3,4,5)
print(suma_grande)