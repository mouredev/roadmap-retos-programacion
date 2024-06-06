#Exceptions

#Capturing specific exception
array = []
try:
    array[2]
except IndexError:
    print("Element out of index")  

#Capturing generic exception
try:
    10/0
except Exception as e:
    print("Error: ",e,type(e))


class CustomError(Exception):
    def __ini__(self,message):
        super.__init__(message)


def function_execption(value:int):

    if value == 0:
        raise ZeroDivisionError
    elif value == 1:
        raise ValueError("Incorrect value")
    elif value == 3:
        raise CustomError("Custom exception")
    

try:
    #function_execption(0)
    #function_execption(1)
    function_execption(3)

except ZeroDivisionError:
    print("Not posible to divide by 0")
except ValueError:
    print("Incorrect value")
except CustomError as e:
    print(e)        
else:
    print("No execption")
finally:
    print("Finishing execution")        

  