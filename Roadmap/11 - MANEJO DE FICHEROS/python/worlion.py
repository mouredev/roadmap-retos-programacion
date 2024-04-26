import os

global global_file_path 
global_file_path = "./worlion.txt"

class Student:
    def __init__(self, name: str, age:int, lang: str) -> None:
        self.name: str = name
        self.age:int = age
        self.lang: str = lang
    
def write_student(file_path: str, student: Student):
    my_file = open(file_path, 'w')
    my_file.write(f"\nName: {student.name}")
    my_file.write(f"\nAge: {student.age}")
    my_file.write(f"\nFavourite language: {student.lang}")
    my_file.close()

def read_students(file_path: str, ):
    my_file_read = open(file_path, 'r')
    print(my_file_read.read())
    my_file_read.close()

def remove_file(file_path: str, ):
    os.remove(file_path)

def test_students_in_files():
    student: Student = Student("Worlion", 40, "Python")
    print("\nEscribiendo en fichero...")
    write_student(global_file_path, student)
    print("\nLeyendo fichero...")
    read_students(global_file_path)
    print("\nBorrando fichero...")
    remove_file(global_file_path)
    
test_students_in_files()
