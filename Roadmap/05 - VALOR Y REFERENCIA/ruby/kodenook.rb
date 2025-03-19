
=begin
    Assignment By Value
=end

var1 = 3
var2 = var1

var1 = 5

puts var1
puts var2

=begin
    Assignment By Assignment
=end

var1 = [10, 30]
var2 = var1

var1.push(50)

puts var1
puts var2

=begin
    Exercise
=end

def ByValue(a, b)
    c = b
    d = a

    return c, d
end

original1 = 20
original2 = 30
value1, value2 = ByValue(original1, original2)

puts 'By Values'
puts 'Original Values'
puts original1
puts original2
puts 'After Function Values'
puts value1
puts value2

def ByReference(a, b)
    c = b
    d = a

    return c, d
end

original1 = 20
original2 = 30
value1, value2 = ByReference(original1, original2)

puts 'By Values'
puts 'Original Values'
puts original1
puts original2
puts 'After Function Values'
puts value1
puts value2
