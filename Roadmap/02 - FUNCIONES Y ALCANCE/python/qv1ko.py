a = 5

def main():
    func1()
    print(func2())
    func3(a, "\nParameterized and non-return function:\nGlobal variable A: ")
    print(func4(-4, "\nFunction with return and with parameters:\nGlobal variable A: "))

def func1():
    b = 4
    print(f"\nFunction without return and without parameters:\nGlobal variable A: {a}\nLocal variable B: {b}")

def func2():
    txt = "\nFunction with return and without parameters:\nGlobal variable A: " + str(a)
    return txt

def func3(num, txt):
    print(f"{txt}{num}")

def func4(num, txt):
    text = txt + str(a) + "\nAbsolute number: " + str(abs(num))
    return text

main()

print("\nProgram:")

def program(zip, zap):

    count = 0

    for i in range(1, 100):
        if i % 3 == 0 and i % 5 == 0:
            print(zip + zap)
        elif i % 3 == 0:
            print(zip)
        elif i % 5 == 0:
            print(zap)
        else:
            count += 1
    
    return count

print("\nNumber of times a text was not printed: " + str(program("zip", "zap")))
