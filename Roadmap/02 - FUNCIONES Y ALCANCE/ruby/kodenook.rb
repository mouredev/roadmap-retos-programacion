
def name() :nil
    puts 'kodenook'
end

name()

def full_name(fname: string = 'my', lname: string = 'name') :nil
    puts "#{fname} #{lname}"
end

full_name(lname: 'lname')

def addition(*nums) :int
    result = 0

    nums.each do |num|
        result += num
    end

    return result
end

puts addition(1, 1.2, 5.5, -4)

def first() :nil
    puts 'first'

    def second() :nill
        puts 'second'
    end

    second()
end

first()

$global = 'global'

def scope(local: string = 'local', local2: string = 'local2') :nil
    puts $global
    puts local
end

scope()

=begin
    Exercise
=end

def exercise(word1, word2) :int
    number_count = 0

    (0..100).each do |number|
        if number % 3 == 0 && number % 5 == 0
            puts "#{word1} #{word2}"
        elsif number % 3 == 0
            puts word1
        elsif number % 5 == 0
            puts word2
        else
            number_count += 1
        end
    end

    return number_count
end

puts "number of times it was a number and not words: #{exercise('hello', 'ruby')}"