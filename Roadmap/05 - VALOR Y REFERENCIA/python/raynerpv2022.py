"""
 * EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
"""


def x_valor():
    # int. string, float, tuplas
    X_coin = 12
    z_coin = X_coin
    z_coin  = 0
    print(X_coin, f"Direccion memoria {id(X_coin)}")
    print(z_coin,f"Direccion memoria {id(z_coin)}")

    n_coin = "CUBACoin"
    a_coin =  n_coin+"Hav_coin"
    a_coin = "asasa"

    print(n_coin,f"Direccion memoria {id(n_coin)}")
    print(a_coin,f"Direccion memoria {id(a_coin)}")

    t1 = (1,2,3,4,5,6)
    t2 = (t1)
    t2 = t1+t1
    print(t1,f"Direccion memoria {id(t1)}")
    print(t2,f"Direccion memoria {id(t2)}")



def x_referencia():

    # dic , list, set
    l1 = [1,2,3,4,5,6]
    l2 = l1
    l2.append("00")
    print(l1,f"Direccion memoria L1 {id(l1)}")
    print(l2,f"Direccion memoria L2 {id(l2)}")

    d1 = {1:"a",2:"b" }
    d2 = d1
    d2[3] = "c"
    print(d1,f"Direccion memoria d1 {id(d1)}")
    print(d2,f"Direccion memoria d2 {id(d2)}")

    s1 = {1 ,2  }
    s2 = s1
    s2.add(9)
    print(s1,f"Direccion memoria s1 {id(s1)}")
    print(s2,f"Direccion memoria s2 {id(s2)}")
    def x_ref(lista1):
        lista1.append("q")
        return lista1
    l100 = x_ref(l1)
    print(l1,f"Direccion memoria L1 {id(l1)}")
    print(l100,f"Direccion memoria L100 {id(l100)}")



x_valor()
x_referencia()

"""
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
 """

nomb1 = "HOla"
nomb2 = "Python"

def prog_X_valor(cad1, cad2: str):
    
    cad1,cad2  = cad2, cad1
    return cad1, cad2

qq1, qq2 =  prog_X_valor(nomb1,nomb2)
print(nomb1, nomb2)
print(qq1, qq2)




def prog_X_ref(dic1, dic2: dict):
    
    # dic1 = dic2
    # dic1["Francia"] = "Paris"
    dic1, dic2 = dic2, dic1
    return dic1,dic2


k_v1 = {"Cuba":"Havana"}
k_v2 = {"Rusia":"Moscu"}
zz1 , zz2 = prog_X_ref(k_v1,k_v2)
print(k_v1," y " ,k_v2)
print(k_v1,f"Direccion memoria d2 {id(k_v1)}")
print(k_v2,f"Direccion memoria d2 {id(k_v2)}")
print(zz1, " y ", zz2)
print(zz1,f"Direccion memoria d2 {id(zz1)}")
print(zz2,f"Direccion memoria d2 {id(zz2)}")

   
