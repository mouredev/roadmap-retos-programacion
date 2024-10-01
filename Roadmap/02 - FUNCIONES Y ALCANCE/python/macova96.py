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
#Este menú (funcion) sirve para imprimir por consola las funciones que he usado como ejemplo y retornar la eleccion del usuario
def menu_inicio ():
    print("CALCULADORA PROPINAS\t---> 1")
    print("BANNER\t\t\t---> 2")
    print("DIFICULTAD EXTRA\t---> 3")
    

    return(input("elije una opcion: "))

#funcione dentro de funciones 
def calculadora_propinas ():
    #Declaro las variables que se tendrán en cuenta para el calculo de la propina y en el total a pagar por persona 
    total_cuenta= float(input("Ingresa el total de la cuenta: \n $"))
    porcentaje_propina= float(input("Ingrese el porcentaje de la propina: \n ")) 
    numero_personas = float(input("Ingrese el numero de personas a dividir las cuenta: \n"))

    def calculo(total_cuenta, porcentaje_propina, numero_personas = 1 ):
        #Esta funcion solo se encarga de calcular la propina y en total a pagar por persona 
        return (total_cuenta + (total_cuenta * ( porcentaje_propina / 100 ))) / numero_personas
    
    #uso es return de la funcion interna asignadolo a la variable de total a pagar 
    total_pagar = calculo(total_cuenta , porcentaje_propina , numero_personas)
    return total_pagar



def impresora_banner ():
    #esta funcion solo imprime un banner, sin parametros ni retornos usando la funcion interna PRINT
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

def dificultad_extra ():
    texto_1 = str (input("ingrese el primer texto \t---> "))
    texto_2 = str (input("ingrese el segundo texto \t---> "))
    contador = 1
    
    for numero in range(1, 101):
        if (numero % 3) == 0:
            print(texto_1)
        elif (numero % 5) == 0:
            print(texto_2)
        elif (numero % 3) == 0 and (numero % 5) == 0:
            print(texto_1 + texto_2)
        else:
            print(numero)
            contador += 1

    print(f"El numero se ha impreso {contador} veces.")




def main ():
    #esta funcion utiliza el retorno de la funcion menu_inicio y dependiendo de la respuesta llama alguna de las funciones creada
    opcion =menu_inicio()
    if opcion == "1":
        total = calculadora_propinas()
        print(f"El total a pagar es ${total} por persona")
    elif opcion == "2":
        impresora_banner()
    elif opcion == "3":
        dificultad_extra()



if __name__ == "__main__":
    main()