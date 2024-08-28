class Person:

    def __init__(self,id:int,name:str):
        self.id = id
        self.name = name
        self.patner = None
        self.childs = []
    def getId(self):
        return self.id
    def getName(self):
        return self.name
    def getPatner(self):
        return self.patner
    def getChilds(self):
        return self.childs
    def addPatner(self,person):
        if self.patner:
            print(f'{self.name} already has a patner')
        else:
            self.patner = person    
    def addChild(self,person):
        self.childs.append(person)

def exist(iterator:list[Person],id)->int:
    for index,element in enumerate(iterator):
        if element.getId()==id:
            return index
    return -1 
def check_child_has_parents(child_id:int,iterator:list[Person]):
    #Check if the child has parents 
   for element in iterator:
       child_list = element.getChilds()
       if child_id in child_list:
           return True

   return False    

    
def print_tree(iterator:list[Person]):
   for element in iterator:
       patner_name = ""
       if element.getPatner():
        patner_name = iterator[exist(iterator,element.getPatner())].getName()
       childs = element.getChilds()
       childs_names = list(map(lambda x: iterator[exist(iterator,x)].getName(),childs))
       print(f'Person {element.getId()}, name: {element.getName()} patner: {patner_name}, childs: {childs_names}')
       
       
def main():
    people:list[Person] = []
    while True:
        print("What do you want to do?")
        print("Press 1 to add a person")
        print("Press 2 to delete a person")
        print("Press 3 to add a patner")
        print("Press 4 to add a child to one person")
        print("Press 5 to print tree ")
        print("Press 6 to exit the program")
        option = int(input("Which option do you choose? "))

        match option:
            case 1: 
                id = int(input("Enter person id "))
                if exist(people,id) == -1:
                    #If person doesn't exist
                    name = input("Enter person name ")
                    new_person = Person(id,name)
                    people.append(new_person)
                else:
                    print(f'Person {id} already exist')    
            case 2:
                id = int(input("Enter the person id to be deleted "))
                index = exist(people,id)
                if index >= 0:
                    people.pop(index)
                else:
                    print(f'Person {id} doesn\'t exist')    
            case 3:
                patner1_id = int(input("Enter the id for patner 1 "))
                patner1_index = exist(people,patner1_id)
                if patner1_index >= 0:
                    if not people[patner1_index].getPatner():
                        patner2_id = int(input("Enter the id for patner 2 "))
                        patner2_index = exist(people,patner2_id)
                        if patner2_index >=0:
                            #Check if patner doesn't have a patner
                            if not people[patner2_index].getPatner():
                                if patner1_id != patner2_id:
                                    people[patner1_index].addPatner(people[patner2_index].getId())
                                    people[patner2_index].addPatner(people[patner1_index].getId())
                                else:
                                    print("A patner could not be the same person")    
                            else:
                                print(f'Person {patner2_id} has already a patner {people[patner2_index].getPatner()}')    
                        else:
                            print(f'Person {patner2_id} doesn\'t exist ')
                    else:
                        print(f'Person {patner1_id} has already a patner {people[patner1_index].getPatner()}')
                else:
                    print(f'Person {patner1_id} doesn\'t exist')    

            case 4:
                child_id = int(input("Enter the id for the person to be added as child "))
                child_index = exist(people,child_id)
                if child_index >= 0:
                    #If the person exist, let user to 
                    if not check_child_has_parents(child_id,people):
                        mother_id = int(input("Enter id of the mother "))
                        mother_index = exist(people,mother_id)
                        if mother_index >= 0:
                            #Find father 
                            father_id = int(input("Enter id of the father "))
                            father_index = exist(people,father_id)

                            if father_index >= 0:
                                if father_id != mother_id:
                                    people[mother_index].addChild(people[child_index].getId())
                                    people[father_index].addChild(people[child_index].getId())
                                else:
                                    print("Father and mother could not be the same person ")    
                            else:
                                print(f'Person {father_id} doesn\'t exist')     
                        else:
                            print(f'Person {mother_id} does not exit')
                    else:
                        print("Person already has parents")
                else:
                    print(f'Person {child_id} doesn\'t exist')
            case 5:
                print_tree(people)          
            case 6: 
                break

main()
