import random
def is_prime(number:int)->bool:
    for i in range(2,int(number ** 0.5) +1):
       if number % i == 0:
           return False
    return True          

def distribute_rings(number_rings:int)->list:
    sauron = 1
    pending_rings = number_rings -1
    division = []
    for human in range(2,pending_rings,2):
        for elf in range(1,pending_rings,2):
            dwarves = pending_rings -  human - elf

            if dwarves > 0 and is_prime(dwarves):
                division.append({

                    'sauron':sauron,
                    'human': human,
                    'elf':elf,
                    'dwarves': dwarves
                }
                )
    return division            

number_rings = int(input("Enter number of rings "))
if number_rings >=5:
    result = distribute_rings(number_rings)
    if result:
        print(random.choices(result))

else:
    print("At least 5 rings are needed ")    