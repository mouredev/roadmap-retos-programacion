"""ejecrcio"""
try :
    print(10/1)
    my_list = [1,2,3,4]
    print(my_list[4])
except Exception as e:
    print(f"Hay un error: {e}")

"""Extra"""

class Errorpassword(Exception):
        pass
def user (id : int, name : str, password: str):
    if isinstance(password,int) or len(password) < 8:
        raise Errorpassword("La contrasena debe ser mayor o igual a 8 digitos")
    elif not isinstance(id ,int):
        raise TypeError("Error, deber ser un entero ")
    elif id<0:
        raise ValueError("El id debe ser un numero positivo") 
    elif not isinstance(name ,str):
        raise TypeError("Error, solo se permite letras")
    else:
        return name, id


try :
    a = user(1,"Tomas", "12345678")

except Errorpassword as e:
        print(f"Se ha presentado el siguiente: Errorpassword -> {e}")
except TypeError as e:
        print(f"Se ha presentado el siguiente: TypeError -> {e}")
except ValueError as e:
    print(f"Se ha presentado el siguiente: ValueError -> {e}")
except Exception as e:
    print("Ha sucedido un error")
else:
        print(f" No se ha presentado ningun error el usuario {a} se a agregado  ")
finally:
        print("Saliendo del login")




