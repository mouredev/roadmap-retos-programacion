require 'set'

=begin
    array
=end

cars = ['bwm', 'ferrari']

# insert
cars << 'mazda'
cars.push('chevrolet')
cars.unshift('toyota') # add to the end

puts cars

# insert

cars[0] = 'peugeot'

puts cars

# delete

cars.pop # delete to the end
cars.shift # delete to the first
cars.delete('ferrari') # deletes by value
cars.delete_at(1) # deletes by index

puts cars

=begin
    hashes
=end

grades = { :mark => 15, :jimmy => 10, :jack => 10 }

# insert

grades.store(:elon, 13)

puts grades

# edit

grades[:mark] = 14

puts grades

# delete

grades.delete(:elon)

puts grades

=begin
    Sets
=end

fruits = Set['apple', 'orange', 'lemon']


# insert

fruits.add('banana') # add and return set
fruits.add?('banana') # add and return nil if value exists

puts fruits

# delete

fruits.delete('banana') # deletes and return set
fruits.delete?('banana') # deletes and return nil if value exists

puts fruits

=begin
    Exercise
=end

option = 0
data = {}

while option != 5 do

    puts "\033c"

    puts '1. search'
    puts '2. add'
    puts '3. edit'
    puts '4. delete'
    puts '5. exit'

    print 'choose an option: '
    option = gets.to_i

    case option
        when 1
            print 'name: '
            name = gets

            puts data[name]

            sleep(5)
        when 2
            print 'name: '
            name = gets
            print 'number: '
            number = gets

            data.store(name, number)
        when 3
            print 'name: '
            name = gets
            print 'number: '
            number = gets

            data[name] = number
        when 4
            print 'name: '
            name = gets

            data.delete(name)
    end

end