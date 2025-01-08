
# Create .txt with filename your Github repository, with your name, age and favurite progaming language
import os

path = os.path.join(os.path.dirname(__file__),"raulG91.txt")

with open(path,"w") as file:
    file.write("Raul Garcia"+"\n")
    file.write("32"+"\n")
    file.write("Python"+"\n")

file.close()

#Read the file that we have created

with open(path,"r") as file:
    for line in file:
        print(line)

#Remove the file
os.remove(path)        

def check_product_file(product_name:str,file:str)->tuple:
    product = ()
    try:
        with open(file,"r")as file:
            for line in file:
                name,amount,price = line.split(",")
                if name == product_name:    
                    return (name,amount,price)
    except Exception as e:
        pass
    return product
def delete_product(product_name:str,file:str):
    try:
        with open(file,"r+") as file:
            lines = file.readlines()
            file.seek(0)

            for line in lines:
                name,amount,price = line.split(",")
                if name != product_name:
                    file.write(line)
            file.truncate()          
    except Exception as e:
        print("Error opening the file")   
def update_product(product_name:str,new_amount:int,new_price:float,file:str):
    try:
        with open(file,"r+") as file:
            lines = file.readlines()
            file.seek(0)

            for line in lines:
                name,amount,price = line.split(",")
                if name == product_name:
                    file.write(f'{product_name},{new_amount},{new_price}\n')
                else:
                    file.write(line)    
            file.truncate()          
    except Exception as e:
        print("Error opening the file")   
def total_sales(file_name,product_name = ""):
    total_amount = 0
    total_price = 0
    lines = []
    try:
        with open(file_name,"r") as file:
            lines = file.readlines() 
    except Exception as e:
        print("Error opening the file")  
                 
    for line in lines:
        name,amount,price = line.split(",")
        if product_name != "" and name == product_name:
            amount = int(amount)
            price = float(price)
            total_amount +=amount
            total_price += (price*amount)
        elif product_name == "":
            amount = int(amount)
            price = float(price)
            total_amount +=amount
            total_price += (price*amount)               


    print(f'Total amount: {total_amount} total price: {total_price}')

                          
file = os.path.join(os.path.dirname(__file__),"sales.txt")
while True:
    print("Choose option: ")
    print("Press 1: Add product")
    print("Press 2: Check product")
    print("Press 3: Update product")
    print("Press 4: To delete product")
    print("Press 5: Total sales")
    print("Press 6: Sales for product")
    print("Press 7: To exit")
    option = int(input())

    if option == 1:
        name = str(input("Insert product name: "))  
        product = check_product_file(name,file)
        if not product:
            amount = int(input("Enter amount: "))
            price = float(input("Insert price: "))
            with open(file,"a") as f:
                f.write(f'{name},{amount},{price}\n')
        else:
            print("Product already exist in the file")        
    elif option == 2:
        name = str(input("Insert product name: "))
        product = check_product_file(name,file)
        if product:
            print(f'Product: {product[0]} amount: {product[1]} price: {product[2]}')
        else:
            print("Product doesn't exist in the file")
    elif option == 3:
        name = str(input("Insert product name: "))
        product = check_product_file(name,file)
        if product:
            new_amount = int(input("Enter new amount "))
            new_price = float(input("Insert new price "))
            update_product(name,new_amount,new_price,file)
        else:
            print("Product doesn't exist in the file")    
    elif option == 4:
        name = str(input("Insert product name: "))
        product = check_product_file(name,file)
        if product:
          delete_product(name,file)
        else:
            print("Product doesn't exist in the file")
    elif option == 5:
        total_sales(file_name=file)
    elif option == 6:
        name = str(input("Insert product name: "))
        product = check_product_file(name,file)
        if product:
            total_sales(file_name=file,product_name=name)
        else:
            print("Product doesn't exist in the file")                         
    elif option == 7:
        try:
            os.remove(file)
        except:
            print("Error removing file")    
        break
    else:
        print("Invalid option")
