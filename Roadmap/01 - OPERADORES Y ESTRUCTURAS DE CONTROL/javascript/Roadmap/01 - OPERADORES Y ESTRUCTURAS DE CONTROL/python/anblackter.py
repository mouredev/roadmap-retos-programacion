# Aritmetric operators are (+ sum) (- rest) (* multiplciation) (/ division)
# Those are also complement of aritmetric operators (// floor division) (% remainder) (** squared root)

print(f'sum {1 + 2}')
print(f'rest {2 - 1}')
print(f'multiplication {2 * 2}')
print(f'division {2 / 2}')
print(f'floor division {23 // 2}')
print(f'division remainder {23 % 3}')
print(f'square {3 ** 2}')

# Comparative operations uses (< less than) (> greater than) (<= less or equal than) (>= greater or equal than)
# (== equals) (!= different)
print(f'less than {1 < 2}')
print(f'less than {1 > 2}')
print(f'greater or equal than {2 >= 2}')
print(f'less or equal than {10 <= 2}')
print(f'different {10 != 2}')
print(f'equals {10 == 10}')

# Logical operators are (and) (or) (not)
print(f' and {10 != 2 and 2 == 2}')
print(f' or {10 != 2 or 2 == 2}')
print(f' not {not (10 != 2)}')

# Iterations are (for) (while)
for i in range(10):
    print(i)

counter = 0
while counter < 10:
    print(counter)

# Conditionals are (if, else)
if 1 <= 2:
    print('1 is less or equal than 2')
elif 2 >= 1:
    print('2 is greater or equal than 1')
else:
    print('None of those conditions true')

# Exceptions
try:
    print(a)
except:
    print('This is an error, a is undefined before used')
else:
    print('This print appears if not exception occurs when run into try block')
finally:
    print('This print always appear at the end of teh try except blocks. Doesn\'t matter is exception occurs or not')

