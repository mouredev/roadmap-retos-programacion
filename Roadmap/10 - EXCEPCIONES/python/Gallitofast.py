#HELLOWORLD
print ("^"*100)
try:                
    div = 10/0  
    print(f"10 divided by 0 is: {div}")

except ZeroDivisionError as zde:
    print(zde,"ERROR!! ")

print ("^"*100)
#Type error
try:
    var_1= 10
    if not type(var_1) is str:
        raise TypeError("Tis is NOT A STRING")
    else:
        print (var_1)

except TypeError as zde :                    
    print (zde)


print ("^"*100)

"""EXTRA DIFFICULTY"""

class StrError (Exception):
     pass

def process_parameters(a:list):
       
        if type(a[0])==str or type(a[1])==str:
             raise StrError("Error, You can't divide strings")
        elif len(a)>2:
             raise Exception ("THE FUNCTION CAN ONLY DIVIDE 2 NUMBERS!")
        elif a[1]==0:
             raise ZeroDivisionError("You cant divide by 0!!")
      
        return (a[0]/a[1])



try:
#These are tests that are going to fail so that we can see the exceptions management.
    print (process_parameters([3,0])) #Division by 0 error
    #print (process_parameters(["a",3])) #Error can't divide strings
    #print (process_parameters([3,2,5])) #More than 2 nubers
    

except ZeroDivisionError as se:
    print ("Error type:", se)
except StrError as st:
    print (st)
except Exception as e:
    print (e)

else:
     print ("There has been no errors")

finally:
     print ("The execution has been finalized")




