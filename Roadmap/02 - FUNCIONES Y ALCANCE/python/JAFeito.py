#Solo la aprte de dificultad extra
stream_1 = "Multiplo de 3"
stream_2 = "Multiplo de 5"
def numeros(stream_1,stream_2):
    cantidad = 0
    for x in range(1,101):
        if x % 3 == 0 :
            if (x % 5 == 0):
                print(stream_1 +" y "+ stream_2)
            else:
               print(stream_1)    
        elif (x % 5 == 0):
              print(stream_2)  

        else:
            cantidad +=1
            print(x)
    return cantidad
print(f"Total de numeros inpresos: ", numeros(stream_1,stream_2))