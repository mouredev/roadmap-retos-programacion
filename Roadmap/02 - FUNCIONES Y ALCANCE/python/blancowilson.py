# Funciones practica semana 2 Blancowilson



def validate_has_letter(word, letter):
    #function into another function
    def addition(a,b):
        return a + b
    
    print(addition(3,5))
    
    return letter in word   

print(validate_has_letter("palabra",'e'))

count = 0

def increment_count():
    global count
    count += 1

def another_increment_count():
    cou += 1


increment_count()
another_increment_count()
print(count) # Output: 1