
##
# The `recursion` function in Ruby recursively prints numbers from the input number down to 0.
#
# Args:
#   number: The `recursion` method takes a parameter `number`, which is used to control the recursion.
# The method will output the value of `number` and then call itself recursively with `number-1` until
# `number` is less than or equal to 0.
def recursion(number)
    puts number
    recursion(number-1) if number > 0
end

recursion(100)

=begin
    Exercise
=end

##
# The above Ruby function calculates the factorial of a given number recursively.
#
# Args:
#   number: The `number` parameter in the `factorial` function represents the integer for which you
# want to calculate the factorial. The factorial of a non-negative integer `n`, denoted as `n!`, is
# the product of all positive integers less than or equal to `n`.
#   resultado: The `resultado` parameter in the `factorial` function is used to keep track of the
# intermediate result as the factorial calculation progresses through recursive calls. It starts with
# a default value of 1 and gets updated with the multiplication of the current number and the previous
# result in each recursive call. Defaults to 1
def factorial(number, resultado = 1)
    if number > 1
        factorial(number-1, number*resultado)
    else
        puts resultado
    end
end

factorial(5)

##
# The above Ruby function calculates the Fibonacci number at a given position using recursion.
#
# Args:
#   position: The `fibonacci` function you provided calculates the Fibonacci number at a given
# position in the sequence. The Fibonacci sequence starts with 1, 1, and each subsequent number is the
# sum of the two preceding numbers.
#
# Returns:
#   The code is a recursive function to calculate the Fibonacci number at a given position. If the
# position is greater than 2, it recursively calls itself to calculate the Fibonacci number by adding
# the previous two Fibonacci numbers. If the position is 2 or less, it returns 1.
def fibonacci(position)
    if position > 2
        return fibonacci(position - 1) + fibonacci(position - 2)
    else
        return 1
    end
end

puts fibonacci(7)