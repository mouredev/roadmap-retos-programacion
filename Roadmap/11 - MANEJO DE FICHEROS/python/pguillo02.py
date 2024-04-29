import os

with open("pguillo02.txt", "w") as f:
    f.write("Pablo Guilló \n")
    f.write("21 años \n")
    f.write("Python \n")

with open("pguillo02.txt", "r") as f:
    print(f.read())

os.remove("pguillo02.txt")