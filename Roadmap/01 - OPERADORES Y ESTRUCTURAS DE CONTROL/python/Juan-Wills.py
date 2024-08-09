#assigment operators (assign values to variables or constants)
num1= 2
num2= 3

#Aritmethic operators (returns numbers)
2+3      #addition
2-3      #substraction
2*3      #multiplication
2/3      #division
2%3      #module
2**3     #exponent
2//3     #floor division

num1+=7         #increment by 'X'         
num2-=2         #decrement by 'X'
num1*=6         #multiplication by 'X'
num2/=3         #division by 'X'
num1%=9         #module by 'X'
num2**=4        #power by 'X'
num1//=5        #floor division by 'X'

#Comparative operators (returns boolean)
num1<num2    #Bigger than
num1>num2    #Smaller than
num1<=num2   #Bigger or equal than
num1<=num2   #Smaller or equal than
num1==num2   #Equal to
num1!=num2   #Not equal to

#Logic operators (returns booleans)
num1 and num2    #Are they both true?
num2 or num1     #Are only one of them true?
not num1         #Changes the boolean state to its contrapart

#Membership operators (returns booleans)
array=['car','bicycle','motorcycle','truck']
'bicycle' in array      #the string is into the list of the array
'van' not in array  #the string in not into the list of the array

#Identity operators (returns booleans)
obj1=['phone','printer']
obj2=['phone','printer']
obj3=obj1
obj1 is obj3     #obj3 is the same as obj1  
obj1 is not obj2 #despite both has the same content, they're different and are store in distint slots in memory

#Bitwise operators (returns numbers)
"""
These are hard to explain so I'll 
just skip them, you can always search
by your own in google tho
"""
bit= num1 & num2
bit= num1 | num2
bit= ~num1

#Ternary operators
'num1 is the smallest' if (num1<num2) else 'num2 is the smallest'
    #Help to make decisions between two options
'Option 1 (true)' if (num1>num2) else('Option 2 (false-true)' if (num1==num2) else 'Option 3 (false-false)')
    #Ternary operators can be nested

#if-elif-else
age=17
if (age<=17 and age>0):
    print('User is younger than 18')
elif (age==18):
    print('User has 18 years old')
else:
    print('User is older than 18')

#while-loop
i=12
print('list of number from 0 to 9:')
while (i<12):
    i+=1
    if (i==11):
        break       #Used to stop the loop despite the condition is still true

    if(i==4):
        print('number three skipped')    
        continue    #Used to pass to the next iteration 
            
    print(i-1)
else:               #Used to run code once condition is no longer true
    print('we have reached the top!')

#for-loop
List=[2,3,4,5,6,7]
for i in range(len(List)):      #for repeats according to the length of the item of any sequence
    print(List[i], end="," if i!=(len(List))-1 else "")
    print(" I was printed",i+1,"times.")
    break                       #else statement won't be triggered if break executes
print("\n")

for j in range(1,11,2):         #default start value is 0, the third number is to add incremente or decrement
    print(j)
else:
    print("We have printed all the numbers in the range.")

student_list=0
student_names=["Juan","Santi","Jose","Maria","Josefa"]
for name in student_names:      #'name' is the item of the list according to the iteration
    if name=="Jose":
        student_list+=1
        continue
    print("Student",student_list,":",name)

for i in range(10,56):
    if i%2==0 and i!=16 and i%3!=0:
        print(i)
