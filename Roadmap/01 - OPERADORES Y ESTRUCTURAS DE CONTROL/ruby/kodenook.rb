
num1 = 3
num2 = 4

=begin
    Arithmetics Operators
=end

# addition
puts "sum: #{num1 + num2}"
# subtraction
puts "subtraction: #{num1 - num2}"
# multiplication
puts "multiplication: #{num1 * num2}"
# division
puts "division: #{num1 / num2}"
# modulus
puts "modulus: #{num1 % num2}"
# exponentation
puts "exponentation: #{num1 ** num2}"

=begin
    Assignment Operators
=end

puts num3 = 5 # assignment
puts num3 +=  5 # addition
puts num3 -= 6 # subtraction
puts num3 *= 2 # multiplication
puts num3 /= 3 # division
puts num3 %= 3 # modulus
puts num3 **= 2 # exponentation

=begin
    Comparison Operators
=end

puts num1 == num2 # equal
puts num1 != num2 # not equal
puts num1 > num2 # greater than
puts num1 < num2 # less than
puts num1 >= num2 # greater than or equal than
puts num1 <= num2 # less than or equal than
puts num1 <=> num2 # spaceship (return -1,0 or 1)
puts num1 === num2 # Used to test equality within a when clause of a case statement
puts num1.eql?(num2) # return true if are type equals and value equals
puts num1.equal?num2 # return true if have the same object id

=begin
    Bitwise Operators
=end

puts 6 & 3 # compare each bit and set it to 1 if both are 1, otherwise it is set to 0
puts 6 | 3 # compare each bit and set it to 1 if one or both are 1, otherwise it is set to 0
puts 6 ^ 3 # compare each bit and set it to 1 if only one is 1, otherwise it is set to 0
puts ~3 # inverts each bit, 0 becomes 1 and 1 becomes 0
puts 3 << 2 # insert the specified numbers of 0's (in this case 2) from the right
puts 8 >> 2 # insert the specified numbers of 0's (in this case 2) from the left

=begin
    Logical Operators
=end

puts num1 and num2 # true if both are true
puts num1 or num2 # true if either are true
puts num1 && num2 # true if both are true
puts num1 || num2 # true if either are true
puts !num1 # true if not true
puts not(num1) # true if not true

=begin
    Conditional Assignment
=end

puts num1 ? 'true' : 'false' # ternary
puts num1 || 'false' # null coalescing

=begin
    Range Operators
=end

puts (1..10).to_a # range from start point to end point inclusive
puts (1...10).to_a # range from start point to end point exclusive

=begin
    If
=end

if num1 == num2
    puts 'equal'
elsif num2 < num1
    puts 'less'
else
    puts 'none'
end

=begin
    Short hand if
=end

puts 'true' if 0 == 0

=begin
    nnless
=end

unless num1 != num2
    puts 'equals'
else
    puts 'not equals'
end

=begin
    Short hand unless
=end

puts 'false' unless 0 != 0

=begin
    Case
=end

age =  5
case age
    when 0 .. 2
    puts 'baby'
    when 3 .. 6
    puts 'little child'
    when 7 .. 12
    puts 'child'
    when 13 .. 18
    puts 'youth'
    else
    puts 'adult'
end

=begin
    Loop While
=end

i = 0
num = 5

while i < num  do
   puts "Inside the loop i = #{i}"
   i += 1
end

=begin
    Loop While Modifier
=end

i = 0
num = 5
begin
   puts "Inside the loop i = #{i}"
   i += 1
end while i < num

=begin
    Loop Until
=end

i = 0
num = 5

until i > num  do
   puts "Inside the loop i = #{i}"
   i += 1;
end

=begin
    Loop Until Modifier
=end

i = 0
num = 5
begin
   puts "Inside the loop i = #{i}"
   i += 1;
end until i > num

=begin
    Loop For
=end

for i in 0..5
   puts "Value of variable is #{i}"
end

(0..5).each do |i|
   puts "Value of variable is #{i}"
end

=begin
    Words For Loops
=end

# break | finish the loop
# next | junp to next loop
# redo | restart iteration
# retry | restart from the begin

=begin
    Exceptions
=end

# begin
#     if 1 == 1
#         raise 'error'
#     end
# rescue
#     puts 'there was a error'
# end

# begin
#     if 1 == 1
#         raise 'there was a error'
#     end
# rescue Exception => e
#     puts e.message
#     puts e.backtrace.inspect
#     puts e.code
# else
#     puts 'executed when are not errors'
# ensure
#     puts 'always is executed'
# end

=begin
    Exceptions
=end

(10..55).each do |i|
    puts i if i % 2 == 0 and i != 16 and i % 3 != 0
end
