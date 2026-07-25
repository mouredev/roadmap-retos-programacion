#concatenacion
hello = "Hello World" + "!"
print(hello)

#slicing
countries = "Venezuela, Colombia, Brasil, Argentina, Chile, Paraguay, Uruguay, Bolivia"
print(countries[0:5])
print(countries[10:18])
print(countries[19:27])

#upercase
fruit = "apple"
print(fruit.upper())

#lowercase
fruit = "APPLE"
print(fruit.lower())

#remove space
fruit = " apple "
print(fruit.strip())

#split
fruits = "apple,banana,orange"
print(fruits)
print(fruits.split(","))

#concatenar
number = "noventa"
print(number + " y ocho")

# String methods

#capitalize
txt = ["hello","and", "welcome","to","my","world"]
for i in txt:
    print(i.capitalize())

#casefold
txt = ["Hello","And", "Welcome","TO","My","World"]
for i in txt:
    print(i.casefold())

#center
txt = "banana"
print(txt.center(20,"*"))

#count
txt = "I love the chocolate and the apples, the chocolate is my favorite"
print(txt.count("chocolate"))

#encode
txt = "My name is Ståle"
print(txt.encode(encoding="ascii",errors="backslashreplace"))

#endwith
txt = "Hello, welcome to my world."
y = txt.endswith("red")
x = txt.endswith(".")
print(x,y)

#expand tabs
txt = "H\te\tl\tl\to"

print(txt)
print(txt.expandtabs())
print(txt.expandtabs(2))
print(txt.expandtabs(4))
print(txt.expandtabs(10))

#find
txt = "Hello, welcome to my world."
print(txt.find("welcome",2,20))
print(txt.find("world",2,20))

#format
txt = "the price is {} dollars\n".format(500)
txt2 = "My name is {0}, I'm {1}".format("John",36)
print(txt,txt2)

#index
txt = "Hello, welcome to my world."
print(txt.index("welcome"))
print(txt.index("world",2))

#extra

def check_word(msg1, msg2:str):
    #polindromo
    print(f"¿{msg1} es un polindromo? {msg1 == msg1[::-1]}")
    print(f"¿{msg2} es un polindromo? {msg2 == msg2[::-1]}")

    #anagramas
    print(f"¿{msg1} y {msg2} son anagramas? {sorted(msg1) == sorted(msg2)}")

    #isogramas
    def isogram(word:str) -> bool:
        word_dict = dict()
        for character in word:
            word_dict[character] = word_dict.get(character, 0) + 1
        
        isogram = True
        values = list(word_dict.values())
        isogram_len = values[0]
        for word_count in values:
            if word_count != isogram_len:
                isogram = False
                break
        return isogram
    print(f"¿{msg1} es un isograma? {isogram(msg1)}")
    print(f"¿{msg2} es un isograma? {isogram(msg2)}")

check_word("oso","hola")
check_word("amor","roma")

