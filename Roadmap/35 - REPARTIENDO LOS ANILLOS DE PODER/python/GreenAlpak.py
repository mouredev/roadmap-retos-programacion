import math 


def dame_los_anillos():
    try:
        anillos=int(input("Cuantos anillos vamos a repartir?"))
    except Exception as e:
        print(f"Introduzca un elemento valido: {e}")
        dame_los_anillos()
    return anillos

def impares(num_anillos):
    return [anillo for anillo in range(1,num_anillos+1) if anillo%2==1]

def pares(num_anillos):
    return [anillo for anillo in range(1,num_anillos+1) if anillo%2==0]

def primos(num_anillos):
    result=[]
    enc=False
    j=2
    for i in range(2,num_anillos+1):
        primo=True
        for j in range(2,math.ceil(math.sqrt(i))+1):
            if i%j==0:
                primo=False
                break
        if primo:
            result.append(i)

    return result

def backtrack(lists,target,current_sum=0,index=0,current_combination=[]):
    if index==len(lists):
        if current_sum==target:
            return current_combination
        else:
            return None
    for num in lists[index]:
        result=backtrack(lists,target,current_sum+num,index+1,current_combination+[num])
        if result is not None:
            return result
    return None

        

def evalua_opciones(num_anillos,l_pares,l_impares,l_primos,sauron):
    print(f"""{num_anillos = }\n 
          {l_pares = }\n 
          {l_impares = }\n 
          {l_primos = }\n """)
    result=backtrack([l_pares,l_impares,l_primos,sauron],num_anillos)
    
    if result is None:
        print("No hay combinacion posible con esos anillos")
    else:
        print(f"Los anillos se han repartido con esta combinacion: {result}")

       
if __name__=="__main__":
    num_anillos=dame_los_anillos()
    l_impares=impares(num_anillos)
    l_primos=primos(num_anillos)
    l_pares=pares(num_anillos)
    sauron=[1]
    evalua_opciones(num_anillos,l_pares,l_impares,l_primos,sauron)

