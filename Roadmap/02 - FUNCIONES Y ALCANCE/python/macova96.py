"""
/*
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
 */

ESTRUCTURA DE UNA FUNCION
def nombre_de_la_funcion (parametros): 
    codigo de la funcion
    return valor_de_retorno

"""

def menu_inicio ():
    print("calculadora_propinas\t---> 1")
    print("funcion_2\t---> 2")
    print("funcion_3\t---> 3")
    print("funcion_4\t---> 4")

    return(input("elije una opcion: "))

def calculadora_propinas ():
    total_cuenta= float(input("Ingresa el total de la cuenta: \n $"))
    porcentaje_propina= float(input("Ingrese el porcentaje de la propina: \n ")) 
    numero_personas = float(input("Ingrese el numero de personas a dividir las cuenta: \n"))

    def calculo(total_cuenta, porcentaje_propina, numero_personas = 1 ):
        return (total_cuenta + (total_cuenta * ( porcentaje_propina / 100 ))) / numero_personas
    
    total_pagar = calculo(total_cuenta , porcentaje_propina , numero_personas)
    return total_pagar

def impresora_banner ():
    print("""
     _______     _  _          _______             _     _           _       
(_______)   | |(_)        (_______)           (_)   | |         | |      
 _____ _____| | _ _____    _     _ _____ _   _ _  __| |_____  __| |      
|  ___) ___ | || (___  )  | |   | (____ | | | | |/ _  (____ |/ _  |      
| |   | ____| || |/ __/   | |   | / ___ |\ V /| ( (_| / ___ ( (_| |      
|_|   |_____)\_)_(_____)  |_|   |_\_____| \_/ |_|\____\_____|\____|      
                                                                         
 _                             _          _______       _             _  
| |                           | |        (_______)     (_)           | | 
| |____  ____  _   _ ____   __| | ___     _______ ____  _ ____  _____| | 
| |  _ \|    \| | | |  _ \ / _  |/ _ \   |  ___  |  _ \| |    \(____ | | 
| | | | | | | | |_| | | | ( (_| | |_| |  | |   | | | | | | | | / ___ | | 
|_|_| |_|_|_|_|____/|_| |_|\____|\___/   |_|   |_|_| |_|_|_|_|_\_____|\_)
                                                                         
    """)

def main ():
    opcion =menu_inicio()
    if opcion == "1":
        total = calculadora_propinas()
        print(f"El total a pagar es ${total} por persona")
    elif opcion == "2":
        impresora_banner()
    elif opcion == "3":
        print("Funcion no disponible")
    elif opcion == "4":
        print("Funcion no disponible")


if __name__ == "__main__":
    main()