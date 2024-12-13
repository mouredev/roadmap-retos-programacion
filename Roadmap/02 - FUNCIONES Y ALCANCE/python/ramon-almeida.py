

def extra(p1: list, p2: list):
    count = 0
    for i in range(1, 101):
        if i % 3 == 0:
            print(p1)
        elif i % 5 == 0:
            print(p2)
        elif i % 3 == 0 and i % 5 == 0:
            print(p1, p2)
        else:
            print(i)
            count += i
    return count


extra(('animo', 'vamos'), ('tu puedes', 'estamos contigo'))
