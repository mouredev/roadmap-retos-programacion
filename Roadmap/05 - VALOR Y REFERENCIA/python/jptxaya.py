#Paso por valor
#Originales
print("#####Paso por valor#####")
print("Valores originales")
my_string = "Hola Mundo"
my_int = 10
my_boolean = True
my_float = 1.5
print(my_string)
print(my_int)
print(my_boolean)
print(my_float)

#Paso por valor
def paso_valor(mstring, mint, mboolean, mfloat):
    mtring = "New String"
    mint = 20
    mboolean = False
    mfloat = 2.5

paso_valor(my_string, my_int, my_boolean, my_float)
print("Despues")
print(my_string)
print(my_int)
print(my_boolean)
print(my_float)

#Paso por referencia
#Originales
print("######Paso por referencia######")
print("Valores originales")
my_list = [1,2,3]
my_tuple = ("first","second","third")
my_dict = {0: "zero",1: "one", 2:"two"}
my_set = {10,11,12}
print(my_list)
print(my_tuple)
print(my_dict)
print(my_set)

def paso_referencia(mlist:list,mtuple:tuple,mdict:dict,mset:set):
    mlist.append("4")
    mdict[1] = "Valor modificado"
    mtuple = ("zero")
    mset.add(13)

paso_referencia(my_list,my_tuple,my_dict,my_set)
print("Despues")
print(my_list)
print(my_tuple) #La tupla es inmutable
print(my_dict)
print(my_set)

#Dificultad extra
print("***DIFICULTAD EXTRA***")
print("#####Paso por valor#####")
print("Valores originales")
my_string = "Hola Mundo"
my_int = 10
print(f"String orig: {my_string}")
print(f"Int orig: {my_int}")

def dif_valor( mstring, mint):
    mstring = "Fin"
    mint = 0
    return mstring, mint

my_new_string, my_new_int = dif_valor(my_string,my_int)
print(f"New String: {my_new_string}")
print(f"New Int: {my_new_int}")
print(f"String orig: {my_string}")
print(f"Int orig: {my_int}")

print("#####Paso por referencia#####")
print("Valores originales")
my_list = [1,2,3]
my_dict = {0: "zero",1: "one", 2:"two"}
print(f"List orig: {my_list}")
print(f"Dict orig: {my_dict}")

def dif_referencia( mlist, mdict):
    mlist.append(4)
    mdict[1] = "Valor modificado"
    return mlist, mdict

my_new_list, my_new_dict = dif_referencia(my_list,my_dict)
print(f"New List: {my_new_list}")
print(f"New Dict: {my_new_dict}")
print(f"List orig: {my_list}")
print(f"Dict orig: {my_dict}")






