#Value and Reference

# Data types passed by value

my_int_a = 5
my_int_b = my_int_a   # my_int_b gets a *copy* of the value 5
my_int_b = 15         # changing my_int_b does NOT affect my_int_a

print(my_int_a)   # 5
print(my_int_b)   # 15

# Data types passed by reference

my_list_a = [1, 2]
my_list_b = my_list_a  # both point to the same list in memory
my_list_b.append(3)    # modifies the *same* object

print(my_list_a)   # [1, 2, 3]
print(my_list_b)   # [1, 2, 3]

# Functions with data passed by value

def my_int_func(my_int: int):
    my_int = 100                                         # Inside function: 100
    print("Inside function:", my_int)

my_int_c = 50
my_int_func(my_int_c)
print("Outside function:", my_int_c)                     # Outside function: 50

# Functions with data passed by reference

def my_list_func(my_list: list):
    my_list.append(3)       # modifies the original list
    my_list_d = my_list
    my_list_d.append(4)     # also modifies the same object
    print("Inside function:", my_list)    # [1, 2, 3, 4]
    print("Alias variable:", my_list_d)   # [1, 2, 3, 4]

my_list_c = [1, 2]
my_list_func(my_list_c)
print("Outside function:", my_list_c)  # [1, 2, 3, 4]


#Extra 

bon1 = 12
bon2 = 32

def pro_v(bon_1:int, bon_2:int):
    yum = bon_1 
    bon_1 = bon_2
    bon_2 = yum
    return bon_1, bon_2

bon3, bon4 = pro_v(bon1, bon2)
print(f"{bon1}, {bon2}")
print(f"{bon3}, {bon4}")

#--------------------------------------------------------------------------

bun1 = [23, 56]
bun2 = [21, 45]

def pro_r(bun_1:list, bun_2:list):
    yum = bun_1 
    bun_1 = bun_2
    bun_2 = yum
    return bun_1, bun_2

bun3, bun4 = pro_v(bun1, bun2)
print(f"{bun1}, {bun2}")
print(f"{bun3}, {bun4}")