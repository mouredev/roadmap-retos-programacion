# 02 FUNCIONES Y ALCANCE

""" * EJERCICIO:
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
 */ 
 """

# variable global
saludo = "Hola!"
# Funciones dentro de funcion main
def main():

    # Funcion sin parametro
    def func_sin_parametro():
        print(f"1. {saludo}")
    
    func_sin_parametro()

    # Funcion con parametro
    def func_con_parametro(string):
        # variable local "nombre"
        #nombre = input("2. Ingresa tu nombre: ")
        print(f"Hola, {string}!")

    func_con_parametro("Daniel")

    # Funcion con retorno
    def func_con_retorno():
        # variable local "nombre"
        nombre = input("3. Ingresa el nombre de quien quieras saludar: ")
        return print(f"Hola, {nombre}!")
    
    func_con_retorno()

    # Con un argumento predeterminado
    def saludo_pred(nombre="Luis"):
        print(f"5. Hola, {nombre}!")

    saludo_pred("4. Daniel")
    saludo_pred()

    # Con argumentos y return
    def return_args_greet(greet, name):
        return f"{greet}, {name}!"

    print(return_args_greet("6. Hola", "Daniel"))

    # Con retorno de varios valores
    def multiple_return_greet():
        return "Hola", "Python"

    greet, name = multiple_return_greet()
    print("7. Saludo al reves")
    print(name)
    print(greet)
    
    def multiple_args(*args):
        print(args)
    
    multiple_args("Hola", "Soy", "Daniel")

    '''def extra_para_mi(*args):
        for i in args:
            print(i)
    
    lista = [1,2,3,4]
    extra_para_mi(f",".join(map(str,lista)))'''
if __name__=="__main__":
    main()