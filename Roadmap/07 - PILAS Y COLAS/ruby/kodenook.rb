=begin
    Stacks
=end

letters = ['a', 'b', 'c', 'd']

=begin
    Insert
=end

letters.unshift('e')
letters.unshift('f')

puts letters
puts

=begin
    Delete
=end

letters.shift()

puts letters

=begin
    Queue
=end

letters = ['a', 'b', 'c', 'd']

=begin
    Insert
=end

letters.push('e')
letters.push('f')

puts
puts letters
puts

=begin
    Delete
=end

letters.pop()

puts letters

=begin
    Exercise
=end

def webNavigation()

    stack = []
    option = ''

    while option.strip != 'exit'
        puts 'give a url or next, before, exit'
        option = gets

        case option.chomp
            when 'next'
            when 'before'
                stack.shift()
                puts 'you are in %s' % stack.first()
            else
                stack.unshift(option)
                puts 'you are in %s' % stack.first()
            end
    end
end

webNavigation()

def sharedPrint()
    queue = []
    option = ''

    while option.strip != 'exit'
        puts 'give a document or print, exit'
        option = gets

        case option.chomp
            when 'print'
                document = queue.shift()
                puts 'you printed %s' % document
            else
                queue.push(option)
            end
    end
end

sharedPrint()