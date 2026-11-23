"""
    RECURSIVITY
"""

def is_the_final_countdown (value:int) -> None:
    if value >= 0:
        print(value)
        is_the_final_countdown(value - 1)


is_the_final_countdown(100)

"""
    Extra Exercise
"""

def factorial(value:int) -> int:
    if value < 0:
        print("Negative numbers are not valid")
        return 0
    elif value == 0:
        return 1
    else:
        return value * factorial(value - 1)

print(factorial(5))


def fibonacci(value:int) -> int:
    if value <= 1:
        return value
    return fibonacci(value - 1) + fibonacci(value - 2)

print(fibonacci(5))


"""
    FIBONACCI SEQUENCE TURTLE DRAWING
"""

def draw_fibonacci_sequence(n: int):
    fibonacci_values = [str(fibonacci(i)) for i in range(n)]
    print(' '.join(fibonacci_values))

    import turtle
    values_to_draw = [int(v) for v in fibonacci_values if int(v) > 1]
    turtle.speed(1)
    turtle.bgcolor('dark gray')
    turtle.pensize(2)
    turtle.hideturtle()
    for v in values_to_draw:
        turtle.color('green')
        turtle.circle(v, 90)
        turtle.color('black')
        turtle.write(str(v), font=("Arial", 10, "normal"))

    #turtle.done()

draw_fibonacci_sequence(15)